from __future__ import annotations

import asyncio
import json
import sys
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import AsyncMock, MagicMock

import pytest

TOOLS_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(TOOLS_ROOT))

import batch_runner  # noqa: E402
from batch_runner import extract_system_prompt, run_batch  # noqa: E402

MASTER_PROMPT = TOOLS_ROOT.parent / "master-prompt-v1.md"


def _fake_response(text: str, input_tokens: int = 100, output_tokens: int = 200) -> SimpleNamespace:
    """Mimic the shape of an Anthropic Messages API response object."""
    return SimpleNamespace(
        content=[SimpleNamespace(text=text)],
        usage=SimpleNamespace(input_tokens=input_tokens, output_tokens=output_tokens),
    )


def _install_fake_client(
    monkeypatch: pytest.MonkeyPatch,
    create_mock: AsyncMock,
) -> None:
    """Replace AsyncAnthropic with a stub whose .messages.create is our mock."""
    fake = MagicMock()
    fake.messages = MagicMock()
    fake.messages.create = create_mock
    monkeypatch.setattr(batch_runner, "AsyncAnthropic", lambda api_key=None: fake)


def _make_input_dir(tmp_path: Path, names: list[str]) -> Path:
    d = tmp_path / "inputs"
    d.mkdir()
    for n in names:
        (d / n).write_text(f"<input>{n}</input>", encoding="utf-8")
    return d


def test_extract_system_prompt_from_real_master_prompt() -> None:
    assert MASTER_PROMPT.is_file(), "master prompt fixture missing"
    body = extract_system_prompt(MASTER_PROMPT)
    # Should start with the real prompt content — not with the wrapper markdown.
    assert body.startswith("You are CLIENT REVIEW INTELLIGENCE")
    assert "Confirm you understand" in body


def test_extract_system_prompt_missing_block(tmp_path: Path) -> None:
    p = tmp_path / "no-prompt.md"
    p.write_text("# Something\nNo prompt section here.", encoding="utf-8")
    with pytest.raises(ValueError, match="Could not find"):
        extract_system_prompt(p)


def test_batch_happy_path(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    input_dir = _make_input_dir(tmp_path, ["client-a.md", "client-b.md", "client-c.md"])
    output_dir = tmp_path / "outputs"

    create_mock = AsyncMock(side_effect=lambda **kwargs: _fake_response("OK"))
    _install_fake_client(monkeypatch, create_mock)

    exit_code = asyncio.run(
        run_batch(
            input_dir=input_dir,
            output_dir=output_dir,
            prompt_path=MASTER_PROMPT,
            model="claude-test",
            concurrency=2,
            max_tokens=1000,
            api_key="fake",
        )
    )
    assert exit_code == 0

    for name in ["client-a.md", "client-b.md", "client-c.md"]:
        assert (output_dir / name).read_text(encoding="utf-8") == "OK"

    metadata = json.loads((output_dir / "_run-metadata.json").read_text(encoding="utf-8"))
    assert metadata["n_clients"] == 3
    assert metadata["n_success"] == 3
    assert metadata["n_failed"] == 0
    assert metadata["model"] == "claude-test"
    assert metadata["total_input_tokens"] == 3 * 100
    assert metadata["total_output_tokens"] == 3 * 200
    assert "timestamp" in metadata
    assert create_mock.call_count == 3


def test_batch_error_isolation(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    input_dir = _make_input_dir(tmp_path, ["ok-a.md", "boom.md", "ok-b.md"])
    output_dir = tmp_path / "outputs"

    async def fake_create(**kwargs):
        content = kwargs["messages"][0]["content"]
        if "boom" in content:
            raise RuntimeError("simulated permanent error")
        return _fake_response("OK")

    # Patch MAX_RETRIES=1 so retry loop doesn't slow the test
    monkeypatch.setattr(batch_runner, "MAX_RETRIES", 1)
    _install_fake_client(monkeypatch, AsyncMock(side_effect=fake_create))

    exit_code = asyncio.run(
        run_batch(
            input_dir=input_dir,
            output_dir=output_dir,
            prompt_path=MASTER_PROMPT,
            model="claude-test",
            concurrency=3,
            max_tokens=1000,
            api_key="fake",
        )
    )
    # One failure → exit 1, but the other two still complete
    assert exit_code == 1
    assert (output_dir / "ok-a.md").is_file()
    assert (output_dir / "ok-b.md").is_file()
    assert not (output_dir / "boom.md").exists()

    metadata = json.loads((output_dir / "_run-metadata.json").read_text(encoding="utf-8"))
    assert metadata["n_success"] == 2
    assert metadata["n_failed"] == 1


def test_batch_respects_concurrency(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    """5 files with concurrency=2 → observed concurrent calls must never exceed 2."""
    input_dir = _make_input_dir(
        tmp_path,
        [f"c-{i}.md" for i in range(5)],
    )
    output_dir = tmp_path / "outputs"

    active = 0
    peak = 0
    lock = asyncio.Lock()

    async def fake_create(**kwargs):
        nonlocal active, peak
        async with lock:
            active += 1
            peak = max(peak, active)
        # Yield so other coroutines can enter the semaphore
        await asyncio.sleep(0.01)
        async with lock:
            active -= 1
        return _fake_response("OK")

    _install_fake_client(monkeypatch, AsyncMock(side_effect=fake_create))

    exit_code = asyncio.run(
        run_batch(
            input_dir=input_dir,
            output_dir=output_dir,
            prompt_path=MASTER_PROMPT,
            model="claude-test",
            concurrency=2,
            max_tokens=1000,
            api_key="fake",
        )
    )
    assert exit_code == 0
    assert peak <= 2, f"concurrency breached: peak={peak}"
    assert peak == 2, f"expected to saturate at 2, saw peak={peak}"


def test_empty_input_dir(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    input_dir = tmp_path / "inputs"
    input_dir.mkdir()
    output_dir = tmp_path / "outputs"
    _install_fake_client(monkeypatch, AsyncMock())
    exit_code = asyncio.run(
        run_batch(
            input_dir=input_dir,
            output_dir=output_dir,
            prompt_path=MASTER_PROMPT,
            model="claude-test",
            concurrency=2,
            max_tokens=1000,
            api_key="fake",
        )
    )
    assert exit_code == 1

#!/usr/bin/env python3
"""Async parallel runner: call Anthropic Claude on a folder of pseudonymized inputs.

One input file → one user message → one output file in the mirror directory.
The master prompt (a markdown file with a single fenced ```...``` block under
`## Prompt`) is sent as the system prompt.
"""
from __future__ import annotations

import argparse
import asyncio
import json
import os
import re
import sys
import time
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path

from anthropic import APIStatusError, AsyncAnthropic
from tqdm import tqdm


# Match the first fenced block ```...``` under "## Prompt".
PROMPT_BLOCK_RE = re.compile(
    r"##\s+Prompt\s*\n+```[^\n]*\n(?P<body>.*?)\n```",
    re.DOTALL,
)

DEFAULT_MODEL = "claude-opus-4-7"
DEFAULT_CONCURRENCY = 5
DEFAULT_MAX_TOKENS = 8000
MAX_RETRIES = 3
BACKOFF_SECONDS = (1.0, 3.0, 9.0)


def extract_system_prompt(master_prompt_path: Path) -> str:
    """Extract the content of the first fenced code block under '## Prompt'."""
    text = master_prompt_path.read_text(encoding="utf-8")
    match = PROMPT_BLOCK_RE.search(text)
    if match is None:
        raise ValueError(
            f"Could not find a fenced ``` block under '## Prompt' in {master_prompt_path}. "
            "Make sure the file has a '## Prompt' header followed by a triple-backtick block."
        )
    return match.group("body").strip()


@dataclass
class RunResult:
    name: str
    success: bool
    input_tokens: int = 0
    output_tokens: int = 0
    error: str | None = None


@dataclass
class BatchStats:
    results: list[RunResult] = field(default_factory=list)

    @property
    def n_success(self) -> int:
        return sum(1 for r in self.results if r.success)

    @property
    def n_failed(self) -> int:
        return sum(1 for r in self.results if not r.success)

    @property
    def total_input_tokens(self) -> int:
        return sum(r.input_tokens for r in self.results)

    @property
    def total_output_tokens(self) -> int:
        return sum(r.output_tokens for r in self.results)


async def call_one(
    *,
    client: AsyncAnthropic,
    model: str,
    system: str,
    user_content: str,
    max_tokens: int,
) -> tuple[str, int, int]:
    """Call the Anthropic API with bounded retries. Returns (text, in_tokens, out_tokens)."""
    last_exc: Exception | None = None
    for attempt in range(MAX_RETRIES):
        try:
            response = await client.messages.create(
                model=model,
                system=system,
                max_tokens=max_tokens,
                messages=[{"role": "user", "content": user_content}],
            )
            # Collect text from content blocks.
            parts: list[str] = []
            for block in response.content:
                text = getattr(block, "text", None)
                if text:
                    parts.append(text)
            return (
                "".join(parts),
                getattr(response.usage, "input_tokens", 0) or 0,
                getattr(response.usage, "output_tokens", 0) or 0,
            )
        except APIStatusError as exc:  # includes 429
            last_exc = exc
            # Only retry on 429 and 5xx
            if exc.status_code == 429 or (500 <= exc.status_code < 600):
                # Honour Retry-After if present, otherwise exponential backoff.
                wait = BACKOFF_SECONDS[min(attempt, len(BACKOFF_SECONDS) - 1)]
                retry_after = getattr(exc.response, "headers", {}).get("retry-after")
                if retry_after is not None:
                    try:
                        wait = max(wait, float(retry_after))
                    except (TypeError, ValueError):
                        pass
                await asyncio.sleep(wait)
                continue
            raise
        except Exception as exc:
            # Network errors etc. — retry with backoff.
            last_exc = exc
            if attempt < MAX_RETRIES - 1:
                await asyncio.sleep(BACKOFF_SECONDS[attempt])
                continue
            raise
    raise RuntimeError(f"exhausted retries: {last_exc!r}")


async def run_batch(
    *,
    input_dir: Path,
    output_dir: Path,
    prompt_path: Path,
    model: str,
    concurrency: int,
    max_tokens: int,
    api_key: str,
) -> int:
    system_prompt = extract_system_prompt(prompt_path)

    files = sorted(p for p in input_dir.iterdir() if p.is_file() and p.suffix == ".md")
    if not files:
        print(f"error: no .md files found in {input_dir}", file=sys.stderr)
        return 1

    output_dir.mkdir(parents=True, exist_ok=True)

    client = AsyncAnthropic(api_key=api_key)
    semaphore = asyncio.Semaphore(concurrency)
    stats = BatchStats()
    start = time.monotonic()

    async def process(file_path: Path) -> RunResult:
        async with semaphore:
            user_content = file_path.read_text(encoding="utf-8")
            try:
                text, in_tok, out_tok = await call_one(
                    client=client,
                    model=model,
                    system=system_prompt,
                    user_content=user_content,
                    max_tokens=max_tokens,
                )
            except Exception as exc:
                print(f"failed: {file_path.name}: {exc}", file=sys.stderr)
                return RunResult(name=file_path.name, success=False, error=str(exc))

            out_path = output_dir / file_path.name
            out_path.write_text(text, encoding="utf-8")
            return RunResult(
                name=file_path.name,
                success=True,
                input_tokens=in_tok,
                output_tokens=out_tok,
            )

    tasks = [asyncio.create_task(process(f)) for f in files]
    for fut in tqdm(asyncio.as_completed(tasks), total=len(tasks), desc="calls"):
        result = await fut
        stats.results.append(result)

    duration = time.monotonic() - start

    metadata = {
        "timestamp": datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds"),
        "model": model,
        "n_clients": len(files),
        "n_success": stats.n_success,
        "n_failed": stats.n_failed,
        "total_input_tokens": stats.total_input_tokens,
        "total_output_tokens": stats.total_output_tokens,
        "duration_seconds": round(duration, 2),
        "concurrency": concurrency,
    }
    (output_dir / "_run-metadata.json").write_text(
        json.dumps(metadata, indent=2) + "\n", encoding="utf-8"
    )

    print(
        f"done: {stats.n_success}/{len(files)} ok, {stats.n_failed} failed, "
        f"{stats.total_input_tokens} in / {stats.total_output_tokens} out tokens, "
        f"{duration:.1f}s",
        file=sys.stderr,
    )
    return 0 if stats.n_failed == 0 else 1


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Call the Anthropic Claude API over a folder of pseudonymized markdown "
            "inputs, in parallel, writing one output file per input. All inputs should "
            "already be pseudonymized — this tool does not redact."
        )
    )
    parser.add_argument("--input-dir", required=True, type=Path)
    parser.add_argument("--output-dir", required=True, type=Path)
    parser.add_argument("--prompt", required=True, type=Path, help="Master prompt markdown path")
    parser.add_argument("--model", default=DEFAULT_MODEL)
    parser.add_argument("--concurrency", type=int, default=DEFAULT_CONCURRENCY)
    parser.add_argument("--max-tokens", type=int, default=DEFAULT_MAX_TOKENS)
    args = parser.parse_args(argv)

    if not args.input_dir.is_dir():
        print(f"error: --input-dir not a directory: {args.input_dir}", file=sys.stderr)
        return 1
    if not args.prompt.is_file():
        print(f"error: --prompt not a file: {args.prompt}", file=sys.stderr)
        return 1

    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print(
            "error: ANTHROPIC_API_KEY is not set. Export it in your shell "
            "(e.g. `export ANTHROPIC_API_KEY=sk-ant-...`) before running.",
            file=sys.stderr,
        )
        return 1

    try:
        return asyncio.run(
            run_batch(
                input_dir=args.input_dir,
                output_dir=args.output_dir,
                prompt_path=args.prompt,
                model=args.model,
                concurrency=args.concurrency,
                max_tokens=args.max_tokens,
                api_key=api_key,
            )
        )
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())

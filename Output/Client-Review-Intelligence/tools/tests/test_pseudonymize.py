from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest

TOOLS_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(TOOLS_ROOT))

from pseudonymize import (  # noqa: E402
    load_mapping,
    pseudonymize,
    validate_mapping,
)

EXAMPLES = TOOLS_ROOT / "examples"


def _write_mapping(path: Path, mapping: dict[str, dict[str, str]]) -> None:
    path.write_text(json.dumps(mapping), encoding="utf-8")


def test_round_trip(tmp_path: Path) -> None:
    raw = EXAMPLES / "input-raw-example.md"
    mapping = EXAMPLES / "mapping-example.json"

    pseudo = tmp_path / "pseudo.md"
    recovered = tmp_path / "recovered.md"

    assert pseudonymize(raw, mapping, pseudo) == 0
    assert pseudonymize(pseudo, mapping, recovered, reverse=True) == 0

    flat = load_mapping(mapping)

    # The pseudonymized file must not contain any real identifier (long enough to matter).
    pseudo_text = pseudo.read_text(encoding="utf-8")
    for original in flat:
        if len(original) >= 8:
            assert original not in pseudo_text, (
                f"Original identifier leaked into pseudo output: {original!r}"
            )

    # The recovered file must contain no pseudonym tokens.
    recovered_text = recovered.read_text(encoding="utf-8")
    for pseudonym in set(flat.values()):
        assert pseudonym not in recovered_text, (
            f"Pseudonym token leaked into recovered output: {pseudonym!r}"
        )


def test_longest_match_first(tmp_path: Path) -> None:
    mapping_path = tmp_path / "map.json"
    _write_mapping(
        mapping_path,
        {
            "names": {
                "Marc": "SHORT",
                "Marc Perrin": "LONG",
            }
        },
    )
    input_path = tmp_path / "in.md"
    input_path.write_text("Marc Perrin met Marc today.", encoding="utf-8")
    output_path = tmp_path / "out.md"

    assert pseudonymize(input_path, mapping_path, output_path) == 0
    assert output_path.read_text(encoding="utf-8") == "LONG met SHORT today."


def test_warn_on_already_pseudonymized(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    mapping_path = tmp_path / "map.json"
    _write_mapping(
        mapping_path,
        {"names": {"Marc Perrin": "Client_A"}},
    )
    input_path = tmp_path / "in.md"
    input_path.write_text("Client_A is already tokenized", encoding="utf-8")
    output_path = tmp_path / "out.md"

    assert pseudonymize(input_path, mapping_path, output_path) == 0
    captured = capsys.readouterr()
    assert "double-pseudonymization" in captured.err


def test_strict_promotes_warnings_to_failure(tmp_path: Path) -> None:
    mapping_path = tmp_path / "map.json"
    _write_mapping(
        mapping_path,
        {"names": {"Marc Perrin": "Client_A"}},
    )
    input_path = tmp_path / "in.md"
    input_path.write_text("Client_A is already tokenized", encoding="utf-8")
    output_path = tmp_path / "out.md"

    assert pseudonymize(input_path, mapping_path, output_path, strict=True) == 1


def test_abort_if_original_is_substring_of_pseudonym() -> None:
    # "abc" is a substring of pseudonym "abcdef" — would loop on reverse.
    with pytest.raises(ValueError, match="round-trip"):
        validate_mapping({"abc": "abcdef"})


def test_duplicate_original_conflict(tmp_path: Path) -> None:
    mapping_path = tmp_path / "map.json"
    _write_mapping(
        mapping_path,
        {
            "a": {"Marc": "X"},
            "b": {"Marc": "Y"},  # Same original, different pseudonym
        },
    )
    with pytest.raises(ValueError, match="Duplicate"):
        load_mapping(mapping_path)

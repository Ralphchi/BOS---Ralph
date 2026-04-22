#!/usr/bin/env python3
"""Pseudonymize (forward) or re-identify (reverse) CRI input/output markdown files.

Forward: raw client data → tokenized markdown safe to send to the Claude API.
Reverse: tokenized API output → final markdown with real identifiers restored.

The mapping file stays on the advisor's workstation. Nothing is logged to disk
beyond the output file itself.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


# Stored broadly — reviewer can edit if new Swiss-specific patterns emerge.
SUSPICIOUS_PATTERNS: list[tuple[str, re.Pattern[str]]] = [
    ("IBAN-like", re.compile(r"CH\d{2}[\s\d]{15,}")),
    ("Swiss phone", re.compile(r"\+41[\s\d]{7,}")),
    # Honorific followed by a capitalized word — weak signal, intentionally noisy.
    ("Honorific+name", re.compile(r"\b(?:Dr\.|Mme|Mlle|M\.|Herr|Frau)\s+[A-Z][a-zA-ZÀ-ÿ'-]{2,}")),
]


def load_mapping(path: Path) -> dict[str, str]:
    """Load a bucketed JSON mapping and flatten to {original: pseudonym}."""
    raw = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(raw, dict):
        raise ValueError(f"Mapping root must be an object, got {type(raw).__name__}")

    flat: dict[str, str] = {}
    for bucket_name, bucket in raw.items():
        # Keys starting with "_" are treated as metadata (e.g. "_comment") and skipped.
        if bucket_name.startswith("_"):
            continue
        if not isinstance(bucket, dict):
            raise ValueError(
                f"Bucket '{bucket_name}' must be an object of {{original: pseudonym}} pairs"
            )
        for original, pseudonym in bucket.items():
            if not isinstance(original, str) or not isinstance(pseudonym, str):
                raise ValueError(
                    f"In bucket '{bucket_name}': both keys and values must be strings "
                    f"(got {original!r} → {pseudonym!r})"
                )
            if original in flat and flat[original] != pseudonym:
                raise ValueError(
                    f"Duplicate original '{original}' mapped to two different pseudonyms: "
                    f"'{flat[original]}' vs '{pseudonym}'"
                )
            flat[original] = pseudonym
    return flat


def validate_mapping(flat: dict[str, str]) -> None:
    """Ensure no original is a substring of any pseudonym (would break reverse mode)."""
    pseudonyms = set(flat.values())
    for original in flat:
        for pseudonym in pseudonyms:
            if original != pseudonym and original in pseudonym:
                raise ValueError(
                    f"Mapping is unsafe for round-trip: original '{original}' is a "
                    f"substring of pseudonym '{pseudonym}'. Pick a different token."
                )


def apply_replacements(text: str, pairs: list[tuple[str, str]]) -> tuple[str, int]:
    """Apply (source → target) pairs sequentially, longest source first.

    Returns (new_text, total_replacements).
    """
    total = 0
    for source, target in pairs:
        count = text.count(source)
        if count:
            text = text.replace(source, target)
            total += count
    return text, total


def scan_suspicious(text: str, mapping: dict[str, str]) -> list[str]:
    """Return human-readable warnings for leftover identifier-shaped patterns."""
    warnings: list[str] = []
    for label, pattern in SUSPICIOUS_PATTERNS:
        matches = pattern.findall(text)
        # Filter out hits that are themselves pseudonyms or known-mapped originals.
        novel = [m for m in matches if m not in mapping and m not in mapping.values()]
        if novel:
            # Show up to 3 examples, no more — we don't want to leak a lot to stderr.
            sample = ", ".join(repr(m) for m in novel[:3])
            warnings.append(
                f"suspicious {label} pattern (x{len(novel)}): {sample}"
                + ("…" if len(novel) > 3 else "")
            )
    return warnings


def pseudonymize(
    input_path: Path,
    mapping_path: Path,
    output_path: Path,
    *,
    reverse: bool = False,
    strict: bool = False,
) -> int:
    """Run the pseudonymization pipeline. Returns the exit code (0 ok, 1 error)."""
    mapping = load_mapping(mapping_path)
    validate_mapping(mapping)

    text = input_path.read_text(encoding="utf-8")

    if reverse:
        # When multiple originals map to the same pseudonym (e.g. "Dr. Marc Perrin" and
        # "Dr. Perrin" both → "Client_A"), reverse is inherently ambiguous. We pick the
        # canonical form = the first original listed in the mapping JSON.
        canonical: dict[str, str] = {}
        for original, pseudonym in mapping.items():
            if pseudonym not in canonical:
                canonical[pseudonym] = original
        pairs = list(canonical.items())
        pairs.sort(key=lambda p: len(p[0]), reverse=True)
    else:
        pairs = [(original, pseudonym) for original, pseudonym in mapping.items()]
        pairs.sort(key=lambda p: len(p[0]), reverse=True)

    # Warn if the input appears to already be pseudonymized (forward mode only).
    if not reverse:
        already = [p for p in mapping.values() if p in text]
        if already:
            msg = (
                f"warning: input already contains {len(already)} pseudonym token(s) — "
                f"possible double-pseudonymization"
            )
            print(msg, file=sys.stderr)
            if strict:
                return 1

    new_text, total = apply_replacements(text, pairs)

    # Post-pass: scan for identifier-shaped leftovers (forward only; reverse puts them back).
    if not reverse:
        warnings = scan_suspicious(new_text, mapping)
        for w in warnings:
            print(f"warning: {w}", file=sys.stderr)
        if warnings and strict:
            return 1

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(new_text, encoding="utf-8")

    distinct = sum(1 for src, _ in pairs if src in text)
    direction = "reverse" if reverse else "forward"
    print(
        f"[{direction}] Replaced {total} token(s) across {distinct} distinct entr{'y' if distinct == 1 else 'ies'} → wrote {output_path}"
    )
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Pseudonymize (forward) or re-identify (reverse) markdown files using "
            "a local JSON mapping. Output is written to --output; nothing else touches disk."
        )
    )
    parser.add_argument("--input", required=True, type=Path, help="Input markdown path")
    parser.add_argument("--mapping", required=True, type=Path, help="JSON mapping path")
    parser.add_argument("--output", required=True, type=Path, help="Output markdown path")
    parser.add_argument(
        "--reverse",
        action="store_true",
        help="Reverse mode: replace pseudonyms back with originals",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Exit 1 on any warning (suspicious patterns, double-pseudonymization)",
    )
    args = parser.parse_args(argv)

    if not args.input.is_file():
        print(f"error: input file not found: {args.input}", file=sys.stderr)
        return 1
    if not args.mapping.is_file():
        print(f"error: mapping file not found: {args.mapping}", file=sys.stderr)
        return 1

    try:
        return pseudonymize(
            args.input,
            args.mapping,
            args.output,
            reverse=args.reverse,
            strict=args.strict,
        )
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())

from __future__ import annotations

import sys
from pathlib import Path

import pytest

TOOLS_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(TOOLS_ROOT))

from md_to_pdf import (  # noqa: E402
    extract_client_name,
    render,
    render_html,
    split_client_advisor,
)

EXAMPLES = TOOLS_ROOT / "examples"


def test_section6_split_detected() -> None:
    text = (EXAMPLES / "output-example.md").read_text(encoding="utf-8")
    client, advisor, found = split_client_advisor(text)
    assert found is True
    assert "TALKING POINTS" in advisor
    assert "TALKING POINTS" not in client


def test_section6_missing_graceful() -> None:
    text = "# No section 6 here\n=== 1. SUMMARY ===\nJust a summary."
    client, advisor, found = split_client_advisor(text)
    assert found is False
    assert client == advisor


def test_client_name_extraction_from_cher() -> None:
    text = "=== 1. EXECUTIVE SUMMARY ===\nCher Dr. Perrin, le trimestre…"
    assert extract_client_name(text) == "Dr. Perrin"


def test_client_name_extraction_from_h1() -> None:
    text = "# Dr. Marc Perrin — Q1 2026\nSome content."
    assert extract_client_name(text) == "Dr. Marc Perrin — Q1 2026"


def test_render_html_strips_section6_from_client_body() -> None:
    text = (EXAMPLES / "output-example.md").read_text(encoding="utf-8")
    client_md, advisor_md, _ = split_client_advisor(text)
    client_html = render_html(
        body_md=client_md,
        firm_name="Heritage Advisors SA",
        firm_logo_uri=None,
        client_name="Dr. Perrin",
    )
    advisor_html = render_html(
        body_md=advisor_md,
        firm_name="Heritage Advisors SA",
        firm_logo_uri=None,
        client_name="Dr. Perrin",
    )
    assert "TALKING POINTS" not in client_html
    assert "TALKING POINTS" in advisor_html


def test_full_render_produces_valid_pdfs(tmp_path: Path) -> None:
    input_path = EXAMPLES / "output-example.md"
    output_path = tmp_path / "review.pdf"

    assert render(
        input_path=input_path,
        output_path=output_path,
        firm_name="Heritage Advisors SA",
        firm_logo=None,
        client_name_override=None,
    ) == 0

    client_pdf = tmp_path / "review.pdf"
    advisor_pdf = tmp_path / "review_advisor-only.pdf"

    assert client_pdf.is_file() and client_pdf.stat().st_size > 1000
    assert advisor_pdf.is_file() and advisor_pdf.stat().st_size > 1000

    # Magic bytes
    assert client_pdf.read_bytes()[:5] == b"%PDF-"
    assert advisor_pdf.read_bytes()[:5] == b"%PDF-"

    # Compliance firewall is asserted at the HTML level in
    # test_render_html_strips_section6_from_client_body — the PDF is a faithful
    # rendering of that HTML. We also sanity-check that the advisor PDF is
    # strictly larger than the client one (Section 6 adds content and a watermark).
    assert advisor_pdf.stat().st_size > client_pdf.stat().st_size


def test_missing_input_file(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    from md_to_pdf import main

    exit_code = main(
        [
            "--input", str(tmp_path / "nope.md"),
            "--output", str(tmp_path / "out.pdf"),
            "--firm-name", "X",
        ]
    )
    assert exit_code == 1
    assert "not found" in capsys.readouterr().err

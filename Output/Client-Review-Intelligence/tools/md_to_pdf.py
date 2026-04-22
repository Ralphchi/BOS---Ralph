#!/usr/bin/env python3
"""Render a CRI agent output (markdown) to premium A4 PDFs.

Produces TWO PDFs:
  - <output>.pdf                  — client-safe (Section 6 "TALKING POINTS (ADVISOR-ONLY)" stripped)
  - <output-stem>_advisor-only.pdf — full version with Section 6, watermarked

The Section 6 firewall is a compliance safeguard — even if the model slips,
the tool enforces the discretion rule at the output boundary.
"""
from __future__ import annotations

import argparse
import base64
import re
import sys
from pathlib import Path

import markdown as md_lib
from weasyprint import CSS, HTML


SECTION_6_MARKER_RE = re.compile(
    r"^=== 6\.\s*TALKING POINTS\s*\(ADVISOR-ONLY\)\s*===\s*$",
    re.MULTILINE,
)

# "=== N. TITLE ===" — rewritten to styled <h2 class="section"> blocks.
SECTION_HEADER_RE = re.compile(
    r"^===\s*(\d+)\.\s*(.+?)\s*===\s*$",
    re.MULTILINE,
)

# Client name extraction fallback: first "Cher(e) <name>," opening line.
CLIENT_NAME_OPENING_RE = re.compile(
    r"Cher(?:e|ère)?\s+([^,\n]{2,80})\s*[,\n]",
    re.IGNORECASE,
)


def split_client_advisor(markdown_text: str) -> tuple[str, str, bool]:
    """Return (client_md, advisor_md, section_6_found).

    client_md excludes Section 6; advisor_md is the full document.
    If no Section 6 marker is found, client_md == advisor_md and the caller
    should emit a warning (the model may legitimately have omitted it).
    """
    advisor = markdown_text
    match = SECTION_6_MARKER_RE.search(markdown_text)
    if match is None:
        return markdown_text, advisor, False
    client = markdown_text[: match.start()].rstrip() + "\n"
    return client, advisor, True


def extract_client_name(markdown_text: str) -> str | None:
    """Best-effort client name from the markdown. Returns None if nothing plausible."""
    match = CLIENT_NAME_OPENING_RE.search(markdown_text)
    if match:
        return match.group(1).strip()
    # Fallback: first H1 line
    for line in markdown_text.splitlines():
        stripped = line.strip()
        if stripped.startswith("# "):
            return stripped[2:].strip() or None
    return None


def rewrite_section_headers(html: str) -> str:
    """Replace the markdown-default rendering of "=== N. TITLE ===" with styled headers."""
    # After markdown conversion, "=== 1. TITLE ===" becomes either <p>=== 1. TITLE ===</p>
    # or a setext-style underlined header depending on neighbours. Normalise via regex on
    # the markdown source would be cleaner, but we do it on HTML for simplicity and
    # robustness: match any <p>...=== N. TITLE ===...</p> or h1/h2 wrapping the same.
    pattern = re.compile(
        r"<(?P<tag>p|h[1-6])[^>]*>\s*===\s*(?P<num>\d+)\.\s*(?P<title>[^=<]+?)\s*===\s*</(?P=tag)>",
        re.IGNORECASE,
    )
    return pattern.sub(
        lambda m: f'<h2 class="section"><span class="section-num">{m.group("num")}.</span> {m.group("title").strip()}</h2>',
        html,
    )


def preprocess_markdown(text: str) -> str:
    """Normalise section header lines so the markdown lib doesn't swallow them.

    Ensure each "=== N. TITLE ===" lives alone on its own paragraph so it becomes
    <p>=== N. TITLE ===</p> rather than being absorbed by surrounding content.
    """
    # Ensure a blank line before and after each section marker.
    def _ensure_blank(match: re.Match[str]) -> str:
        return "\n\n" + match.group(0).strip() + "\n\n"

    return SECTION_HEADER_RE.sub(_ensure_blank, text)


def encode_logo(logo_path: Path) -> str:
    """Return a data: URI for the firm logo, inlined so the HTML is self-contained."""
    mime = "image/png"
    suffix = logo_path.suffix.lower()
    if suffix in {".jpg", ".jpeg"}:
        mime = "image/jpeg"
    elif suffix == ".svg":
        mime = "image/svg+xml"
    data = base64.b64encode(logo_path.read_bytes()).decode("ascii")
    return f"data:{mime};base64,{data}"


def build_css(*, firm_name: str, client_name: str, watermark: bool) -> str:
    """Return CSS tuned for A4 client-facing deliverables (premium EAM register)."""
    # Escape any quotes in dynamic strings — CSS @page string() doesn't like them.
    safe_firm = firm_name.replace('"', "'")
    safe_client = client_name.replace('"', "'")

    watermark_css = ""
    if watermark:
        watermark_css = """
        @page {
            @top-center {
                content: "ADVISOR ONLY — NOT FOR CLIENT";
                font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
                font-size: 9pt;
                color: #b33a3a;
                letter-spacing: 0.15em;
                text-transform: uppercase;
            }
        }
        body::before {
            content: "ADVISOR ONLY";
            position: fixed;
            top: 45%;
            left: 50%;
            transform: translate(-50%, -50%) rotate(-30deg);
            font-size: 96pt;
            font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
            color: rgba(179, 58, 58, 0.08);
            font-weight: 700;
            letter-spacing: 0.1em;
            z-index: -1;
        }
        """

    return f"""
    @page {{
        size: A4;
        margin: 2.2cm 2cm 2.2cm 2cm;
        @top-left {{
            content: "{safe_client}";
            font-family: 'EB Garamond', Garamond, Georgia, serif;
            font-size: 9pt;
            color: #666;
            font-style: italic;
        }}
        @top-right {{
            content: "{safe_firm}";
            font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
            font-size: 9pt;
            color: #1a1a1a;
            letter-spacing: 0.05em;
        }}
        @bottom-center {{
            content: "Page " counter(page) " / " counter(pages);
            font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
            font-size: 8pt;
            color: #999;
        }}
    }}

    html {{
        font-family: 'EB Garamond', Garamond, Georgia, 'Times New Roman', serif;
        font-size: 11pt;
        line-height: 1.5;
        color: #1a1a1a;
    }}

    body {{
        margin: 0;
    }}

    .firm-header {{
        display: flex;
        align-items: center;
        gap: 14px;
        border-bottom: 1px solid #d4c9b2;
        padding-bottom: 10px;
        margin-bottom: 22px;
    }}

    .firm-header img {{
        max-height: 36px;
        width: auto;
    }}

    .firm-header .firm-name {{
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
        font-size: 12pt;
        letter-spacing: 0.08em;
        color: #1a1a1a;
        text-transform: uppercase;
    }}

    h1 {{
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
        font-size: 18pt;
        font-weight: 500;
        letter-spacing: 0.02em;
        color: #1a1a1a;
        margin-top: 0;
        margin-bottom: 8px;
    }}

    h2.section {{
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
        font-size: 11pt;
        font-weight: 600;
        letter-spacing: 0.18em;
        text-transform: uppercase;
        color: #6d4e2a;
        border-bottom: 0.5pt solid #d4c9b2;
        padding-bottom: 4px;
        margin-top: 22pt;
        margin-bottom: 10pt;
        page-break-after: avoid;
    }}

    h2.section .section-num {{
        color: #b3a88f;
        margin-right: 8px;
        font-weight: 400;
    }}

    p {{
        margin: 0 0 10pt 0;
        text-align: justify;
        hyphens: auto;
    }}

    ul {{
        margin: 0 0 12pt 18pt;
        padding: 0;
    }}

    ul li {{
        margin-bottom: 6pt;
    }}

    strong {{
        color: #6d4e2a;
    }}

    {watermark_css}
    """


def render_html(
    *,
    body_md: str,
    firm_name: str,
    firm_logo_uri: str | None,
    client_name: str,
) -> str:
    preprocessed = preprocess_markdown(body_md)
    html_body = md_lib.markdown(preprocessed, extensions=["extra", "tables"])
    html_body = rewrite_section_headers(html_body)

    if firm_logo_uri:
        header_html = (
            f'<div class="firm-header">'
            f'<img src="{firm_logo_uri}" alt="" />'
            f'<div class="firm-name">{firm_name}</div>'
            f"</div>"
        )
    else:
        header_html = f'<div class="firm-header"><div class="firm-name">{firm_name}</div></div>'

    return f"""<!DOCTYPE html>
<html lang="fr">
<head><meta charset="utf-8"><title>{client_name}</title></head>
<body>
{header_html}
{html_body}
</body>
</html>"""


def build_pdf(
    *,
    body_md: str,
    output_path: Path,
    firm_name: str,
    client_name: str,
    firm_logo_uri: str | None,
    watermark: bool,
) -> None:
    html_str = render_html(
        body_md=body_md,
        firm_name=firm_name,
        firm_logo_uri=firm_logo_uri,
        client_name=client_name,
    )
    css_str = build_css(
        firm_name=firm_name,
        client_name=client_name,
        watermark=watermark,
    )
    output_path.parent.mkdir(parents=True, exist_ok=True)
    HTML(string=html_str).write_pdf(
        target=str(output_path),
        stylesheets=[CSS(string=css_str)],
    )


def render(
    *,
    input_path: Path,
    output_path: Path,
    firm_name: str,
    firm_logo: Path | None,
    client_name_override: str | None,
) -> int:
    text = input_path.read_text(encoding="utf-8")

    client_md, advisor_md, section_6_found = split_client_advisor(text)
    if not section_6_found:
        print(
            "warning: no Section 6 (TALKING POINTS (ADVISOR-ONLY)) found — "
            "client and advisor PDFs will be identical. Proceeding.",
            file=sys.stderr,
        )

    client_name = (
        client_name_override
        or extract_client_name(text)
        or "Client"
    )

    firm_logo_uri: str | None = None
    if firm_logo is not None:
        if not firm_logo.is_file():
            print(f"error: firm logo not found: {firm_logo}", file=sys.stderr)
            return 1
        firm_logo_uri = encode_logo(firm_logo)

    output_path = output_path.with_suffix(".pdf")
    advisor_path = output_path.with_name(output_path.stem + "_advisor-only.pdf")

    build_pdf(
        body_md=client_md,
        output_path=output_path,
        firm_name=firm_name,
        client_name=client_name,
        firm_logo_uri=firm_logo_uri,
        watermark=False,
    )
    build_pdf(
        body_md=advisor_md,
        output_path=advisor_path,
        firm_name=firm_name,
        client_name=client_name,
        firm_logo_uri=firm_logo_uri,
        watermark=True,
    )

    print(f"wrote {output_path} (client-safe)")
    print(f"wrote {advisor_path} (advisor-only, watermarked)")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Render a CRI agent output (markdown) into client-safe + advisor-only "
            "A4 PDFs. Section 6 (TALKING POINTS (ADVISOR-ONLY)) is stripped from "
            "the client-facing PDF as a compliance firewall."
        )
    )
    parser.add_argument("--input", required=True, type=Path, help="Input markdown path")
    parser.add_argument("--output", required=True, type=Path, help="Output PDF path (stem)")
    parser.add_argument("--firm-name", required=True, help="Firm display name (shown in header)")
    parser.add_argument(
        "--firm-logo",
        type=Path,
        default=None,
        help="Path to firm logo (PNG/JPG/SVG). Optional.",
    )
    parser.add_argument(
        "--client-name",
        default=None,
        help="Override auto-extracted client name.",
    )
    args = parser.parse_args(argv)

    if not args.input.is_file():
        print(f"error: input file not found: {args.input}", file=sys.stderr)
        return 1

    try:
        return render(
            input_path=args.input,
            output_path=args.output,
            firm_name=args.firm_name,
            firm_logo=args.firm_logo,
            client_name_override=args.client_name,
        )
    except Exception as exc:  # WeasyPrint errors etc.
        print(f"error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())

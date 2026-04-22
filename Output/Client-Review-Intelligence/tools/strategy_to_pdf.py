#!/usr/bin/env python3
"""Render a generic strategic markdown document to a premium A4 PDF.

Unlike md_to_pdf.py (which is specialised for CRI client reviews with a Section 6
firewall), this tool renders any markdown to a single clean PDF using the same
Garamond/Helvetica register. No firm-name header, no watermark, optional TOC.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

import markdown as md_lib
from weasyprint import CSS, HTML


H2_RE = re.compile(r"^##\s+(.+?)\s*$", re.MULTILINE)


def slugify(text: str) -> str:
    s = re.sub(r"[^\w\s-]", "", text.lower())
    s = re.sub(r"[-\s]+", "-", s).strip("-")
    return s or "section"


def inject_anchors(html: str, headings: list[str]) -> str:
    """Add id="..." to each <h2> in the rendered HTML so TOC can link to it."""
    idx = [0]

    def repl(match: re.Match[str]) -> str:
        if idx[0] >= len(headings):
            return match.group(0)
        anchor = slugify(headings[idx[0]])
        idx[0] += 1
        return f'<h2 id="{anchor}"{match.group(1)}>{match.group(2)}</h2>'

    return re.sub(
        r"<h2([^>]*)>(.+?)</h2>",
        repl,
        html,
        flags=re.DOTALL,
    )


def build_toc(headings: list[str]) -> str:
    items = "\n".join(
        f'<li><a href="#{slugify(h)}">{h}</a></li>' for h in headings
    )
    return f'<nav class="toc"><h2 class="toc-title">Contents</h2><ol>{items}</ol></nav>'


def build_css() -> str:
    return """
    @page {
        size: A4;
        margin: 2.2cm 2cm 2.2cm 2cm;
        @bottom-center {
            content: "Page " counter(page) " / " counter(pages);
            font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
            font-size: 8pt;
            color: #999;
        }
    }

    @page:first {
        @bottom-center { content: none; }
    }

    html {
        font-family: 'EB Garamond', Garamond, Georgia, 'Times New Roman', serif;
        font-size: 11pt;
        line-height: 1.55;
        color: #1a1a1a;
    }

    body { margin: 0; }

    .cover {
        page-break-after: always;
        padding-top: 35%;
        text-align: left;
        border-top: 2px solid #6d4e2a;
        padding-top: 2cm;
    }
    .cover h1 {
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
        font-size: 28pt;
        font-weight: 500;
        letter-spacing: 0.01em;
        margin: 0 0 10pt 0;
        color: #1a1a1a;
    }
    .cover .subtitle {
        font-family: 'EB Garamond', Garamond, Georgia, serif;
        font-style: italic;
        font-size: 13pt;
        color: #6d4e2a;
        margin-bottom: 40pt;
    }
    .cover .meta {
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
        font-size: 9pt;
        letter-spacing: 0.15em;
        color: #999;
        text-transform: uppercase;
    }

    .toc {
        page-break-after: always;
    }
    .toc-title, .section-body h1 {
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
        font-size: 11pt;
        font-weight: 600;
        letter-spacing: 0.18em;
        text-transform: uppercase;
        color: #6d4e2a;
        border-bottom: 0.5pt solid #d4c9b2;
        padding-bottom: 4px;
        margin-top: 0;
        margin-bottom: 14pt;
    }
    .toc ol {
        list-style: none;
        counter-reset: item;
        padding: 0;
        margin: 0;
    }
    .toc ol li {
        counter-increment: item;
        margin: 0 0 10pt 0;
        font-family: 'EB Garamond', Garamond, Georgia, serif;
        font-size: 12pt;
    }
    .toc ol li::before {
        content: counter(item, decimal-leading-zero) "  ";
        color: #b3a88f;
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
        font-size: 10pt;
        letter-spacing: 0.1em;
    }
    .toc a {
        color: #1a1a1a;
        text-decoration: none;
    }
    .toc a::after {
        content: " " leader(".") " " target-counter(attr(href), page);
        color: #b3a88f;
    }

    h2 {
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
        font-size: 11pt;
        font-weight: 600;
        letter-spacing: 0.18em;
        text-transform: uppercase;
        color: #6d4e2a;
        border-bottom: 0.5pt solid #d4c9b2;
        padding-bottom: 4px;
        margin-top: 0;
        margin-bottom: 14pt;
        page-break-before: always;
        page-break-after: avoid;
    }

    h3 {
        font-family: 'EB Garamond', Garamond, Georgia, serif;
        font-style: italic;
        font-size: 13pt;
        font-weight: 400;
        color: #1a1a1a;
        margin-top: 18pt;
        margin-bottom: 8pt;
        page-break-after: avoid;
    }

    h4 {
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
        font-size: 10pt;
        font-weight: 600;
        letter-spacing: 0.08em;
        text-transform: uppercase;
        color: #6d4e2a;
        margin-top: 14pt;
        margin-bottom: 6pt;
    }

    p {
        margin: 0 0 10pt 0;
        text-align: justify;
        hyphens: auto;
    }

    ul, ol {
        margin: 0 0 12pt 18pt;
        padding: 0;
    }

    li { margin-bottom: 6pt; }

    strong { color: #6d4e2a; }

    em { color: #1a1a1a; }

    table {
        width: 100%;
        border-collapse: collapse;
        margin: 10pt 0 14pt 0;
        font-size: 10pt;
    }
    th, td {
        border-bottom: 0.5pt solid #d4c9b2;
        padding: 5pt 8pt;
        text-align: left;
        vertical-align: top;
    }
    th {
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
        font-size: 9pt;
        font-weight: 600;
        letter-spacing: 0.08em;
        text-transform: uppercase;
        color: #6d4e2a;
        border-bottom: 1pt solid #6d4e2a;
    }

    blockquote {
        margin: 12pt 0;
        padding: 8pt 14pt;
        border-left: 2pt solid #6d4e2a;
        font-style: italic;
        color: #4a4a4a;
    }

    code {
        font-family: 'SF Mono', 'Menlo', 'Consolas', monospace;
        font-size: 9.5pt;
        background: #f5f1e8;
        padding: 1pt 4pt;
        border-radius: 2pt;
    }

    pre {
        font-family: 'SF Mono', 'Menlo', 'Consolas', monospace;
        font-size: 9pt;
        background: #f5f1e8;
        padding: 10pt 12pt;
        border-left: 2pt solid #d4c9b2;
        white-space: pre-wrap;
        margin: 10pt 0;
    }

    hr {
        border: none;
        border-top: 0.5pt solid #d4c9b2;
        margin: 18pt 0;
    }
    """


def render(
    *,
    input_path: Path,
    output_path: Path,
    title: str,
    subtitle: str | None,
    meta: str | None,
    skip_toc: bool,
) -> int:
    text = input_path.read_text(encoding="utf-8")
    headings = [m.group(1).strip() for m in H2_RE.finditer(text)]

    html_body = md_lib.markdown(text, extensions=["extra", "tables", "sane_lists"])
    html_body = inject_anchors(html_body, headings)

    cover_html = f"""<section class="cover">
<h1>{title}</h1>
{'<p class="subtitle">' + subtitle + '</p>' if subtitle else ''}
{'<p class="meta">' + meta + '</p>' if meta else ''}
</section>"""

    toc_html = "" if skip_toc or not headings else build_toc(headings)

    full_html = f"""<!DOCTYPE html>
<html lang="en">
<head><meta charset="utf-8"><title>{title}</title></head>
<body>
{cover_html}
{toc_html}
{html_body}
</body>
</html>"""

    output_path.parent.mkdir(parents=True, exist_ok=True)
    HTML(string=full_html).write_pdf(
        target=str(output_path),
        stylesheets=[CSS(string=build_css())],
    )
    print(f"wrote {output_path}")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Render a strategic markdown document to a premium A4 PDF."
    )
    parser.add_argument("--input", required=True, type=Path, help="Input markdown")
    parser.add_argument("--output", required=True, type=Path, help="Output PDF path")
    parser.add_argument("--title", required=True, help="Cover title")
    parser.add_argument("--subtitle", default=None, help="Cover subtitle")
    parser.add_argument("--meta", default=None, help="Cover meta line (date, author)")
    parser.add_argument("--no-toc", action="store_true", help="Skip table of contents")
    args = parser.parse_args(argv)

    if not args.input.is_file():
        print(f"error: input file not found: {args.input}", file=sys.stderr)
        return 1

    try:
        return render(
            input_path=args.input,
            output_path=args.output.with_suffix(".pdf"),
            title=args.title,
            subtitle=args.subtitle,
            meta=args.meta,
            skip_toc=args.no_toc,
        )
    except Exception as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())

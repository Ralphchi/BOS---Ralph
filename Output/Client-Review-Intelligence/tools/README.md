# CRI Toolchain — Local CLIs for Client Review Intelligence

Three offline-first Python CLIs that compress the manual friction of delivering quarterly review packages to near-zero, while keeping the Swiss compliance posture intact.

| Tool | Job | Offline? |
|---|---|---|
| `pseudonymize.py` | Swap real client identifiers ↔ tokens using a local mapping | yes |
| `batch_runner.py` | Call the Anthropic Claude API in parallel over a folder of pseudonymized inputs | calls api |
| `md_to_pdf.py` | Render the agent output to a premium A4 PDF (+ a watermarked advisor-only variant) | yes |

**Compliance design (Swiss Banking Act art. 47, FINMA 2023/1, FINMA Guidance 08/2024):** real client identifiers never leave the advisor's workstation. The Anthropic API is US-cloud, so only pseudonymized inputs are ever sent. The mapping file is the only place where real ↔ token live together; keep it local, don't commit it, don't upload it.

## Install

```bash
# macOS system deps for WeasyPrint (PDF rendering)
brew install pango cairo gdk-pixbuf libffi

# Python deps
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Anthropic API key (for batch_runner only)
export ANTHROPIC_API_KEY=sk-ant-...
```

Requires Python 3.11+.

## End-to-end walkthrough (using `examples/`)

```bash
# 1. Pseudonymize raw client data → safe-to-send markdown
python pseudonymize.py \
  --input examples/input-raw-example.md \
  --mapping examples/mapping-example.json \
  --output pseudo-client-a.md

# 2. Call Claude over a folder of pseudo inputs
mkdir -p inputs outputs
mv pseudo-client-a.md inputs/
python batch_runner.py \
  --input-dir inputs/ \
  --output-dir outputs/ \
  --prompt ../master-prompt-v1.md

# 3. Re-identify the output (tokens → real names) locally
python pseudonymize.py \
  --input outputs/pseudo-client-a.md \
  --mapping examples/mapping-example.json \
  --output final-client-a.md \
  --reverse

# 4. Render the final review to PDF (client + advisor-only)
python md_to_pdf.py \
  --input final-client-a.md \
  --output review-q1-2026.pdf \
  --firm-name "Heritage Advisors SA"
# → produces review-q1-2026.pdf (client-safe)
#   and review-q1-2026_advisor-only.pdf (watermarked)
```

## CLI reference

### `pseudonymize.py`

```
--input       input markdown path
--mapping     JSON mapping path
--output      output markdown path
--reverse     reverse direction (tokens → originals)
--strict      exit 1 on any warning (suspicious patterns, double-pseudonymization)
```

**Mapping format:** JSON with buckets (`client_identifiers`, `addresses`, `portfolio_values`, …). Bucket names are organizational only. Keys starting with `_` are treated as metadata (e.g. `_comment`) and skipped. See `examples/mapping-example.json`.

**Longest-match-first:** `"Marc Perrin"` is always replaced before `"Marc"`, so partial substrings can't leak. Many-to-one mappings (e.g. `"Dr. Marc Perrin"` and `"Dr. Perrin"` both → `"Client_A"`) are supported; reverse mode picks the first-listed original as canonical.

### `batch_runner.py`

```
--input-dir     folder of .md files (one per client, pseudonymized)
--output-dir    where to write outputs (same filenames, plus _run-metadata.json)
--prompt        path to master-prompt-v1.md (system prompt extracted from first ``` block under "## Prompt")
--model         default: claude-opus-4-7
--concurrency   default: 5
--max-tokens    default: 8000
```

Reads `ANTHROPIC_API_KEY` from env. Retries on 429 and 5xx with exponential backoff (respects `Retry-After`). One file failing does not abort the batch; exit code is 1 if any failed.

### `md_to_pdf.py`

```
--input        markdown input (typically the reverse-pseudonymized agent output)
--output       output PDF path (stem — the advisor-only variant gets the _advisor-only suffix)
--firm-name    firm display name (required, shown in the page header)
--firm-logo    optional logo path (PNG/JPG/SVG) — inlined in the header
--client-name  override auto-extracted client name (shown in the page header)
```

**Section 6 firewall:** content below the `=== 6. TALKING POINTS (ADVISOR-ONLY) ===` marker is stripped from the client-facing PDF. The advisor-only PDF includes it and is watermarked on every page (`ADVISOR ONLY` diagonal + top-center banner) so the two documents are impossible to confuse.

## Compliance notes

- **Pseudonymization is the advisor's responsibility.** This tool replaces what's in the mapping — if you forget to map a name, the warnings flag suspicious patterns (IBAN-shaped strings, Swiss phone numbers, honorific+capitalized-name) but cannot catch everything. Review before sending.
- **Mapping files stay local.** Treat them like client data. The `.gitignore` in this folder refuses to commit `mapping-*.json` except the fictional `examples/mapping-example.json`.
- **Nothing is logged to disk** beyond the output file and the batch metadata. No audit trail of cleartext identifiers is created by these tools.
- **API calls go to US-cloud.** That's why pseudonymization is a prerequisite, not an option.

## Troubleshooting

- **`weasyprint` fails to import on macOS:** run `brew install pango cairo gdk-pixbuf libffi`. If it still fails, set `DYLD_FALLBACK_LIBRARY_PATH=/opt/homebrew/lib`.
- **`Fontconfig warning: ignoring UTF-8`** when rendering PDFs: harmless, ignore.
- **`ANTHROPIC_API_KEY is not set`:** export it in the shell you run the tool from (or add it to `~/.zshrc`).
- **PDF client name says "Client" instead of the real name:** the auto-extraction looks for `Cher(e) Name,` or the first `# H1` line. Pass `--client-name "Dr. Marc Perrin"` to override.

## Tests

```bash
pytest tests/
```

Tool 2's tests mock the Anthropic SDK — no API key required to run the suite.

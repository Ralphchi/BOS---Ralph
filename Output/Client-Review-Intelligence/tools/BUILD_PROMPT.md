# Build prompt — Client Review Intelligence tools (3 mini-tools)

**Usage :** copy-paste ce prompt entier dans une nouvelle session Claude Code (ou Cursor avec Claude), lancée depuis le dossier `/Users/ralphchidiac/Projects/BOS-Ralph/Output/Client-Review-Intelligence/`. Laisse Claude Code builder les 3 tools, les tester, écrire les README. Durée estimée : 6-10h de session Claude Code (tu peux l'éteindre et reprendre).

**Avant de lancer la session :**
1. `cd /Users/ralphchidiac/Projects/BOS-Ralph/Output/Client-Review-Intelligence/`
2. Vérifie que tu as Python 3.11+ (`python3 --version`)
3. Vérifie que tu as une clé API Anthropic (tu en auras besoin à la fin pour tester le tool 2) — https://console.anthropic.com/ → API Keys. Configure-la en variable d'env : `export ANTHROPIC_API_KEY="sk-ant-..."` (Mac : ajoute la ligne dans ton `~/.zshrc`)

---

## Prompt à coller

```
You are helping Ralph Chidiac, final-year EPFL Communication Systems student, build a local toolchain for his AI consultancy "Client Review Intelligence" (CRI) — an AI review agent for Swiss external asset managers (EAMs).

## Context of the project

The CRI product is a voice-trained AI agent that takes (a) a portfolio snapshot, (b) quarterly market context, (c) two of the firm's past commentaries, and produces a quarterly review package for HNWI clients. The master prompt is already written and validated (see `/Users/ralphchidiac/Projects/BOS-Ralph/Output/Client-Review-Intelligence/master-prompt-v1.md`).

Until now, the delivery workflow is fully manual: advisor pseudonymizes client data by hand, pastes the 5 input blocks into a Claude Project, receives the output, formats it manually, sends it.

Ralph is opening a Q2 pilot cohort with 3 Swiss EAMs. To prepare for pilot delivery (not to productize — this remains advisor-in-the-loop), we need 3 small local Python tools that compress the manual friction to near-zero.

## Compliance constraint (critical)

Swiss Banking Act (art. 47 BA) + FINMA Circular 2023/1 + FINMA Guidance 08/2024: client identifiers must NEVER leave the Swiss perimeter. All tools operate LOCALLY on the advisor's workstation. Anthropic's Claude API is US-cloud, so we call it only with pseudonymized inputs. Pseudonymization mapping tables stay local, never uploaded, never logged in cleartext to any cloud.

## Three tools to build

Build in this exact order, in this exact directory structure:

```
/Users/ralphchidiac/Projects/BOS-Ralph/Output/Client-Review-Intelligence/tools/
├── pseudonymize.py          # Tool 1
├── batch_runner.py          # Tool 2
├── md_to_pdf.py             # Tool 3
├── requirements.txt
├── README.md                # top-level usage docs
├── examples/
│   ├── mapping-example.json
│   ├── input-raw-example.md
│   ├── input-pseudo-example.md
│   ├── output-example.md
│   └── output-example.pdf
└── tests/
    ├── test_pseudonymize.py
    ├── test_batch_runner.py
    └── test_md_to_pdf.py
```

### Tool 1 — `pseudonymize.py`

**Purpose:** takes a markdown file containing raw client data (in the CRI 5-block input format), replaces all sensitive values with tokens using a local mapping table, outputs a pseudonymized markdown file safe to paste into Claude. Also supports reverse mode: takes an AI-generated output containing tokens, replaces tokens back with real values, outputs the final document for the client.

**Usage CLI:**
```
# Forward (before sending to Claude)
python pseudonymize.py --input raw-client.md --mapping firm-mapping.json --output pseudo-client.md

# Reverse (after receiving Claude output)
python pseudonymize.py --input agent-output-pseudo.md --mapping firm-mapping.json --output agent-output-final.md --reverse
```

**Mapping file format (JSON):**
```json
{
  "client_identifiers": {
    "Dr. Marc Perrin": "Client_A",
    "Marc Perrin": "Client_A",
    "Sylvie Perrin": "Spouse_A",
    "Banque Pictet": "Custodian_CH_12"
  },
  "portfolio_values": {
    "CHF 4 250 000": "CHF 4.0-4.5M"
  },
  "addresses": {
    "Cologny": "Canton of Geneva"
  }
}
```

**Requirements:**
- Forward mode: scan the input text, replace each `original` with its mapped `pseudonym`, preserving surrounding context. Use longest-match-first to avoid partial substitutions (e.g. "Marc Perrin" should match BEFORE "Marc").
- Reverse mode: same but in the opposite direction.
- Preserve markdown structure (code blocks, headers, lists).
- Warn if a pseudonym appears in the input during forward mode (suggests double-pseudonymization) or if a real identifier remains after forward (scan for common Swiss names / patterns — optional).
- Log nothing to disk beyond the output file. Mapping stays on the advisor's workstation.
- Exit code 0 on success, 1 on error with clear stderr message.

### Tool 2 — `batch_runner.py`

**Purpose:** takes a directory of pseudonymized input files (one per client), loads the master prompt, calls the Anthropic Claude API in parallel for each client, writes the output to a mirror directory.

**Usage CLI:**
```
python batch_runner.py --input-dir pseudo-inputs/ --output-dir pseudo-outputs/ --prompt /Users/ralphchidiac/Projects/BOS-Ralph/Output/Client-Review-Intelligence/master-prompt-v1.md --model claude-opus-4-7 --concurrency 5
```

**Requirements:**
- Use the official `anthropic` Python SDK (latest version).
- Read the master prompt from the file path provided — extract only the content between the triple-backticks in the "## Prompt" section (don't send the markdown wrapper).
- For each input file in `--input-dir`, use it as the user message. The file name (e.g. `client-a.md`) maps to an output with the same name in `--output-dir`.
- Async / parallel with asyncio, respecting `--concurrency`. Default concurrency: 5. Rate-limit aware (Anthropic tier-dependent — log and back off on 429).
- Show a progress bar (use `tqdm` or a simple counter).
- Model default: `claude-opus-4-7`. Fallback to `claude-sonnet-4-6` if passed via `--model`.
- Write run metadata (timestamp, model, n_clients, total_tokens, duration) to `output-dir/_run-metadata.json`.
- Gracefully handle API errors: log to stderr, skip that file, continue with the rest. Don't stop the batch on one failure.
- Exit code 0 if all succeed, 1 if any failed (but still complete the rest).
- Read `ANTHROPIC_API_KEY` from environment. Fail fast with clear error if missing.

### Tool 3 — `md_to_pdf.py`

**Purpose:** takes a markdown file (the agent's output after reverse-pseudonymization), converts it to a premium-looking A4 PDF ready to send to the client.

**Usage CLI:**
```
python md_to_pdf.py --input agent-output-final.md --output client-review-q1-2026.pdf --firm-logo firm-logo.png --firm-name "Heritage Advisors SA"
```

**Requirements:**
- Use `weasyprint` (preferred) or `markdown2` + `wkhtmltopdf`. Choose the cleanest dependency stack that works on Mac.
- Convert markdown to HTML first, then wrap in a CSS template for A4 rendering.
- CSS template characteristics:
  - A4 page size, 2cm margins
  - Serif font for body (Garamond, Georgia, or similar — premium register)
  - Sans-serif for section headers
  - Small firm logo + firm name in header (top-right)
  - Page number in footer
  - Client name in header (top-left, if extracted from the markdown — first line or H1)
- Sections (=== 1. EXECUTIVE SUMMARY ===, etc.) are rendered as styled section headers.
- **IMPORTANT:** Section 6 "TALKING POINTS (ADVISOR-ONLY)" must NEVER be included in the client-facing PDF. The tool should detect that section and produce TWO outputs:
  - `<output>.pdf` — client-safe PDF (sections 1-5 only)
  - `<output>_advisor-only.pdf` — full version including section 6, for the advisor
- Exit code 0 on success, 1 on error.
- If `--firm-logo` is not provided, use a minimal header with just firm name.

### Tests

Write minimal tests for each tool using `pytest`. Critical cases only:
- `test_pseudonymize.py`: forward + reverse round-trip, longest-match-first, warn on suspicious patterns
- `test_batch_runner.py`: mock the Anthropic API (use `unittest.mock`), verify concurrency, verify metadata, verify error handling
- `test_md_to_pdf.py`: verify section 6 is stripped from client PDF, verify advisor PDF includes it, verify PDF is valid (non-empty, proper mimetype)

### README.md (top level of `tools/`)

Write a clear, concise README (~100 lines max) with:
- Purpose of the toolchain (one paragraph)
- Install: `python3 -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt`
- Usage walkthrough for each tool, with a real example end-to-end (using the files in `examples/`)
- Security / compliance note (pseudonymization is the advisor's responsibility; mapping file stays local; API calls go to US)

### Examples

Populate `examples/` with:
- `mapping-example.json` — a realistic mapping for a fictional Swiss EAM client
- `input-raw-example.md` — a raw input file in the CRI 5-block format (can be based on the existing Perrin dataset; see `/Users/ralphchidiac/Projects/BOS-Ralph/Output/Client-Review-Intelligence/dataset-perrin-fictif.md`)
- `input-pseudo-example.md` — the pseudonymized version
- `output-example.md` — a sample agent output (can be based on `/Users/ralphchidiac/Projects/BOS-Ralph/Output/Client-Review-Intelligence/sample-output-q1-2026.md` v1 run)
- `output-example.pdf` — the rendered PDF (client-safe version)

### requirements.txt

Minimal, pinned versions:
- `anthropic>=0.40.0`
- `weasyprint` (or chosen PDF engine)
- `markdown` (for md→html)
- `tqdm` (for progress)
- `pytest` (dev only — optional)

## Quality standards

- Python 3.11+.
- Use argparse for CLI.
- Use type hints everywhere.
- Use `pathlib` for file paths (never raw strings).
- Clear error messages with actionable next steps.
- Each tool runs fast (seconds, not minutes) for a single client. Batch runner parallelizes for multiple.
- No internet calls except Anthropic API (tool 2). Tools 1 and 3 are fully offline.
- No heavy frameworks — keep dependencies minimal.

## Out of scope

Do NOT build:
- Any UI (CLI only)
- Any PMS integration (Assetmax / WealthArc / etc.) — data extraction from PMS is manual by the advisor
- Any user management / auth — single-user local tool
- Any database — flat files only
- Any Docker / containerization — runs on Ralph's Mac directly
- Any cloud deployment — fully local
- Any logging beyond stderr — no audit trail files

## Deliverables

When you're done:
1. All 3 tools work end-to-end on the example files
2. All tests pass
3. README is clear enough that Ralph can onboard a new firm in <1 hour using only the docs
4. Commit and push the changes (or report what you changed and let Ralph commit)

Start with Tool 1 (pseudonymize.py). Build, test, then move to Tool 2, then Tool 3. Stop and ask Ralph if you hit a decision point (e.g., PDF engine choice, how to handle an edge case in pseudonymization).

Go.
```

---

## Notes pour Ralph (ne pas inclure dans le prompt Claude)

- Budget temps estimé pour la session Claude : 4-8h si tout se passe bien, peut être moins en parallèle.
- Tu peux laisser Claude tourner et revenir. Il demandera de la permission pour les commandes sensibles (install deps, push git).
- Si Claude choisit weasyprint (Python), il faudra installer les deps système sur Mac : `brew install pango cairo gdk-pixbuf libffi`.
- Une fois fini, tu auras un toolchain que tu peux demo en screen-share pendant les sales calls ("look, we have the pipeline : pseudonymization CLI → batch runner → PDF generator").
- Si tu veux zéro friction, commence Tool 1 + Tool 3 ce week-end (les plus simples, pas besoin d'API key), et Tool 2 en semaine quand tu as la clé.

# Wiki Log

Append-only, chronological record of what the LLM agent did and when.
Each entry starts with `## [YYYY-MM-DD] <op> | <description>` so the log is
greppable: `grep "^## \[" wiki/log.md | tail -10` shows recent activity.

Operations: `ingest`, `query`, `synthesis`, `lint`, `schema`.

---

## [2026-04-18] schema | Initialized LLM Wiki
- Created `CLAUDE.md` with the schema and operating rules.
- Initialized `wiki/index.md` (empty catalog, ready for first ingest).
- Initialized `wiki/log.md` (this file).
- Folder conventions defined: `raw/`, `raw/assets/`, `wiki/sources/`, `wiki/entities/`, `wiki/concepts/`, `wiki/syntheses/`.
- Subfolders under each wiki category will be created lazily (≥5 pages).

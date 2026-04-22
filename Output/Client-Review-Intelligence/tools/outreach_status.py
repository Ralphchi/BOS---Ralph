#!/usr/bin/env python3
"""Outreach status dashboard — reads the tracking table from outreach-wave-1-drafts.md
and prints a one-screen summary: funnel stats, today's due actions, overdue items.

Run from the tools/ directory:
    python outreach_status.py

Or from anywhere with an explicit path:
    python outreach_status.py --source ../outreach-wave-1-drafts.md
"""
from __future__ import annotations

import argparse
import datetime as dt
import re
import sys
from dataclasses import dataclass
from pathlib import Path


DEFAULT_SOURCE = Path(__file__).parent.parent / "outreach-wave-1-drafts.md"
DATE_RE = re.compile(r"(\d{4}-\d{2}-\d{2})")


@dataclass
class Row:
    num: str
    wave: str
    target: str
    firm: str
    channel: str
    sent_d0: str | None  # YYYY-MM-DD or None
    accepted: str  # raw cell
    d3_sent: str  # raw cell
    response: str  # raw cell
    d7_sent: str  # raw cell
    meeting: str  # raw cell
    status: str

    def sent_date(self) -> dt.date | None:
        if not self.sent_d0:
            return None
        m = DATE_RE.search(self.sent_d0)
        return dt.date.fromisoformat(m.group(1)) if m else None


def parse_tracking_table(source: Path) -> list[Row]:
    """Pull the main tracking table (the one with ` # | Wave | Target | ...` header)."""
    text = source.read_text(encoding="utf-8")
    rows: list[Row] = []
    in_table = False
    for line in text.splitlines():
        if not in_table:
            if line.strip().startswith("| #") and "Wave" in line and "Target" in line:
                in_table = True
            continue
        if not line.strip().startswith("|"):
            break
        # skip separator `|---|---|...`
        if set(line.strip()) <= {"|", "-", " ", ":"}:
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 12:
            continue
        rows.append(
            Row(
                num=cells[0],
                wave=cells[1],
                target=cells[2],
                firm=cells[3],
                channel=cells[4],
                sent_d0=cells[5] or None,
                accepted=cells[6],
                d3_sent=cells[7],
                response=cells[8],
                d7_sent=cells[9],
                meeting=cells[10],
                status=cells[11] if len(cells) > 11 else "",
            )
        )
    return rows


def non_empty(cell: str) -> bool:
    """True if the cell has something other than whitespace."""
    return bool(cell.strip())


def funnel_stats(rows: list[Row]) -> dict[str, int]:
    sent = sum(1 for r in rows if non_empty(r.sent_d0 or ""))
    accepted = sum(1 for r in rows if non_empty(r.accepted) and r.accepted.lower() not in {"no", "n"})
    responded = sum(1 for r in rows if non_empty(r.response) and r.response.lower() not in {"no", "n"})
    meetings = sum(1 for r in rows if non_empty(r.meeting) and r.meeting.lower() not in {"no", "n"})
    # Pilot column may not exist in the current table — detect via status
    pilots = sum(1 for r in rows if "pilot signed" in r.status.lower() or "signed" in r.status.lower())
    return {
        "total": len(rows),
        "sent": sent,
        "accepted": accepted,
        "responded": responded,
        "meetings": meetings,
        "pilots": pilots,
    }


def pct(num: int, den: int) -> str:
    return f"{num / den * 100:.0f}%" if den else "—"


def due_today_and_overdue(rows: list[Row], today: dt.date) -> tuple[list[tuple[Row, str]], list[tuple[Row, str]]]:
    """Return (due_today, overdue). Each item = (row, which_followup)."""
    due_today: list[tuple[Row, str]] = []
    overdue: list[tuple[Row, str]] = []
    for r in rows:
        sd = r.sent_date()
        if not sd:
            continue
        # Accepted? (we consider follow-ups only if accepted is not explicitly "no")
        if r.accepted.lower() in {"no", "n"}:
            continue
        # D+3 follow-up — only makes sense if accepted
        if non_empty(r.accepted) and r.accepted.lower() not in {"no", "n"} and not non_empty(r.d3_sent):
            target = sd + dt.timedelta(days=3)
            if target == today:
                due_today.append((r, "D+3 follow-up"))
            elif target < today:
                overdue.append((r, "D+3 follow-up"))
        # D+7 follow-up — if D+3 sent but no response yet
        if non_empty(r.d3_sent) and not non_empty(r.response) and not non_empty(r.d7_sent):
            target = sd + dt.timedelta(days=7)
            if target == today:
                due_today.append((r, "D+7 value-add"))
            elif target < today:
                overdue.append((r, "D+7 value-add"))
        # D+14 close — if nothing has moved
        if non_empty(r.d7_sent) and not non_empty(r.response) and not non_empty(r.meeting):
            target = sd + dt.timedelta(days=14)
            if target == today:
                due_today.append((r, "D+14 close"))
            elif target < today:
                overdue.append((r, "D+14 close"))
    return due_today, overdue


def bar(done: int, total: int, width: int = 20) -> str:
    filled = int(round(width * done / total)) if total else 0
    return "█" * filled + "░" * (width - filled)


def render(rows: list[Row], today: dt.date) -> str:
    stats = funnel_stats(rows)
    due_today, overdue = due_today_and_overdue(rows, today)
    lines: list[str] = []
    lines.append("")
    lines.append("  CLIENT REVIEW INTELLIGENCE — OUTREACH STATUS")
    lines.append(f"  {today.isoformat()}")
    lines.append("  " + "─" * 54)
    lines.append("")

    # Funnel
    lines.append("  FUNNEL")
    lines.append(f"    Sent       {bar(stats['sent'], stats['total'])}  {stats['sent']}/{stats['total']}")
    lines.append(f"    Accepted   {bar(stats['accepted'], stats['total'])}  {stats['accepted']}/{stats['total']}  ({pct(stats['accepted'], stats['sent'])} of sent)")
    lines.append(f"    Responded  {bar(stats['responded'], stats['total'])}  {stats['responded']}/{stats['total']}  ({pct(stats['responded'], stats['accepted'])} of accepted)")
    lines.append(f"    Meetings   {bar(stats['meetings'], stats['total'])}  {stats['meetings']}/{stats['total']}  ({pct(stats['meetings'], stats['responded'])} of responded)")
    lines.append(f"    Pilots     {bar(stats['pilots'], stats['total'])}  {stats['pilots']}/{stats['total']}  ← P1 target: 1 by 2026-06-30")
    lines.append("")

    # Today's actions
    lines.append("  TODAY'S ACTIONS")
    if due_today:
        for row, action in due_today:
            lines.append(f"    ▸ {action:15s}  {row.target:24s}  ({row.firm})")
    else:
        lines.append("    (nothing due today)")
    lines.append("")

    # Overdue
    if overdue:
        lines.append("  OVERDUE — handle first")
        for row, action in overdue:
            sd = row.sent_date()
            delta = (today - (sd + dt.timedelta(days=3 if "D+3" in action else 7 if "D+7" in action else 14))).days
            lines.append(f"    ✗ {action:15s}  {row.target:24s}  ({row.firm})  — {delta}d late")
        lines.append("")

    # Activity roster
    lines.append("  ROSTER")
    for r in rows:
        accepted_mark = "✓" if non_empty(r.accepted) and r.accepted.lower() not in {"no", "n"} else (" " if not non_empty(r.accepted) else "✗")
        responded_mark = "✓" if non_empty(r.response) and r.response.lower() not in {"no", "n"} else (" " if not non_empty(r.response) else "✗")
        meeting_mark = "✓" if non_empty(r.meeting) and r.meeting.lower() not in {"no", "n"} else (" " if not non_empty(r.meeting) else "✗")
        sent_str = r.sent_d0 or "-"
        lines.append(f"    W{r.wave} #{r.num}  {r.target:24s}  sent:{sent_str:12s}  conn:[{accepted_mark}]  resp:[{responded_mark}]  mtg:[{meeting_mark}]")
    lines.append("")

    # Reminders / rules
    lines.append("  RULES")
    lines.append("    · Max 3 messages per target (connect, D+3, D+7). D+14 is the close.")
    lines.append("    · Space 3 messages/day apart (2-3h between LinkedIn sends).")
    lines.append("    · If wave 1 response rate is <10% after D+7 → pause, re-challenge message before wave 2.")
    lines.append("    · Update the tracking table in outreach-wave-1-drafts.md after every action.")
    lines.append("")
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Print outreach status dashboard.")
    parser.add_argument("--source", type=Path, default=DEFAULT_SOURCE, help="Path to the markdown file containing the tracking table.")
    parser.add_argument("--date", type=str, default=None, help="Override today (YYYY-MM-DD). Useful for testing.")
    args = parser.parse_args(argv)

    if not args.source.is_file():
        print(f"error: tracking source not found: {args.source}", file=sys.stderr)
        return 1

    today = dt.date.fromisoformat(args.date) if args.date else dt.date.today()
    rows = parse_tracking_table(args.source)
    if not rows:
        print("warning: no tracking rows found in source", file=sys.stderr)
        return 1

    print(render(rows, today))
    return 0


if __name__ == "__main__":
    sys.exit(main())

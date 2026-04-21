# Client Review Intelligence — Leave-Behind Pack

**Usage :** source markdown pour le PDF 2-3 pages envoyé en email après chaque discovery call avec un EAM intéressé.

**Workflow :**
1. Export PDF via Google Docs (coller markdown, export PDF) ou Typora / Pandoc
2. Rename : `Ralph Chidiac — Client Review Intelligence Pack.pdf`
3. Envoyer en pièce jointe après chaque 15-min call

**Version :** 1.0 (2026-04-21).

---

---

<!-- PAGE 1 : positionnement + offre -->

# Client Review Intelligence

**AI commentary layer for Swiss external asset managers — built by Ralph Chidiac (EPFL) with his brother.**

---

## The problem

A Swiss EAM advisor spends 3 to 4 hours preparing each quarterly client review. For a 50-client book, that is 150 to 200 hours every quarter — 25 workdays per quarter, up to 100 workdays a year. **Five months of one advisor's full-time work, annually, lost to manual commentary.**

## What we built

An AI system that, in under two minutes, delivers for each client:

- Executive summary (80-120 words, in the firm's voice)
- Performance review with rigorous attribution math
- Market themes tied to the client's actual holdings (not generic commentary)
- Outlook & positioning section
- Meeting agenda for the advisor to structure the conversation
- **Advisor-only talking points** — discretion-sensitive items the client never sees

The tone is trained on two past commentaries from your firm. The output is ready for the advisor to edit and send — not to start from scratch.

## How we plug in

- PMS-agnostic : works with Assetmax, WealthArc, WIZE, Expersoft, or custodian PDFs
- No data migration required
- 2-hour onboarding for advisors
- Dedicated support during rollout

## Compliance posture

- **Pilot phase :** pseudonymized inputs. Direct client identifiers never leave your perimeter. Aligned with art. 47 BA, FINMA Circular 2023/1 (critical data), FINMA Guidance 08/2024 (AI governance), SBA Cloud Guidelines (3rd ed., 2025), revised FADP.
- **Full deployment :** Swiss-hosted (Azure Switzerland), FINMA 08/2024-aligned governance.
- DPA provided. Anthropic commercial tier — no training on inputs.

## The pilot offer

**CHF 2 400, 30 days, one advisor, 20 real clients (pseudonymized inputs).**

- Baseline self-logged by your advisor in week 0 (3 representative reviews, timer-based)
- Intervention over weeks 1-4
- Remeasure in week 4 (3 matched reviews)
- If time savings don't hit 50% vs baseline, **full refund**
- The pilot fee is credited 100% against the full deployment price (CHF 7 900 setup + CHF 499/month) if you convert

## Contact

**Ralph Chidiac**
EPFL engineering · Incoming IE Madrid FinTech (Sept 2026) · Geneva
Email: ralph@ralphchidiac.ch
Book a 15-min discovery call: calendly.com/ralphchidiac

---

<!-- PAGE 2 : compliance condensé -->

# How we handle your data

## Data flow (pilot phase)

```
┌────────────────────┐   ┌──────────────────────┐   ┌──────────────┐
│ Advisor worksta-   │ → │  PSEUDONYMIZATION    │ → │ Claude API   │
│ tion (full client  │   │  local, by advisor   │   │ (commercial  │
│ data)              │   │  BEFORE paste        │   │  tier)       │
└────────────────────┘   └──────────────────────┘   └──────────────┘
         ↑                                                  │
         │               ┌──────────────────────┐           │
         └────────────── │  Re-personalization  │ ←─────────┘
                         │  local, by advisor   │
                         └──────────────────────┘
```

**Principle:** no direct client identifiers leave the advisor's perimeter.

## Fields we tokenize before processing

| Field | Original | Tokenized |
|---|---|---|
| Client name | Dr. Marc Perrin | Client_A |
| Spouse / children | Sylvie, 3 children (ages) | Spouse_A, Child_A_1..3 (age bracket) |
| Residence | Cologny (address) | Canton of Geneva |
| Portfolio size | CHF 4 250 000 | CHF 4.0–4.5M |
| Custody IDs | Account references | Internal ref only |
| DOB | 1963-05-12 | Age bracket 60-65 |

Your advisor tokenizes in your own local tooling (template provided). We never receive pseudonymization keys.

## What Anthropic does (and does not) with inputs

- **Commercial tier :** inputs and outputs NOT used to train models.
- Retention: up to 30 days for abuse monitoring, then deleted. Enterprise retention terms available if needed.
- Sub-processors: AWS (compute), DPAs in place.

## Post-pilot: Swiss-hosted path

Full deployment migrates to Azure Switzerland (Claude in-region endpoints as of 2025) OR Swiss-hosted open-weights model on Infomaniak / Exoscale. At that point, pseudonymization becomes optional.

## Contractual instruments provided

1. Pilot Services Agreement (scope, price, measurement protocol, refund trigger)
2. Data Processing Addendum (roles, sub-processors, audit rights)
3. Pseudonymization SOP + advisor template
4. Mutual NDA

---

<!-- PAGE 3 : measurement protocol condensé -->

# Pilot measurement protocol

No ambiguity on the refund trigger. Documented, reproducible, logged by your advisor.

## Timeline (30 calendar days)

| Phase | When | What |
|---|---|---|
| Baseline | D-7 to D0 | Your advisor prepares Q1 review on 3 representative clients (conservative / balanced / growth) WITHOUT the tool. Logs minutes with timer. |
| Kickoff | D0 | 60-min call with Ralph. Access setup, pseudonymization SOP walkthrough, anchors set. |
| Intervention | D1-D28 | Your advisor uses the tool on 20 real clients. |
| Remeasure | D28 | 3 matched-type reviews WITH the tool, same timer protocol. |
| Decision | D29-D30 | Joint review. Refund per formula below. |

## What we measure

**Time spent on quarterly review preparation** = start when the advisor opens the client file, stop when the review is ready to send to the client.

**Included :** reading portfolio snapshot, drafting commentary, drafting market themes, formatting, proofreading.

**Excluded :** live client meeting time, unrelated admin, tool setup (tracked separately).

## The formula

```
baseline_avg      = mean(minutes on 3 baseline reviews WITHOUT tool)
intervention_avg  = mean(minutes on 3 matched reviews WITH tool)

savings_pct = (baseline_avg − intervention_avg) / baseline_avg

→ Refund triggered if savings_pct < 0.50
```

### Worked example

- Baseline avg : 205 min
- Intervention avg : 88 min
- Savings : (205 − 88) / 205 = **57%** → pilot validated, no refund

Or:
- Baseline avg : 205 min
- Intervention avg : 135 min
- Savings : 34% → **full refund**, pilot failed

## Logging template (shared sheet)

| Client ref | Phase | Date | Start | End | Minutes | Notes |
|---|---|---|---|---|---|---|
| Client_A | Baseline | 2026-05-02 | 09:10 | 12:35 | 205 | Q1 review, no tool |
| ... | ... | ... | ... | ... | ... | ... |

**Ralph has read-only access at remeasure.** The advisor owns the log.

## Key design choices

- Any ambiguity in measurement resolves in the advisor's favour (i.e., refund triggered). Keeps Ralph's incentive to make the tool actually work.
- Tool unavailability >48h during pilot pauses the clock.
- Pilot fee is credited 100% against the full deployment if you convert.

---

**Ready to pilot?** ralph@ralphchidiac.ch · calendly.com/ralphchidiac · +41 [phone]

*Document version 1.0 — 2026-04-21. Superseded versions available on request.*

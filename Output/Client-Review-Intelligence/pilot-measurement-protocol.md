# Pilot Measurement Protocol — Client Review Intelligence

**Purpose :** éliminer toute ambiguïté sur le refund trigger du pilote CHF 2 400 / 30 jours. Le protocole est documenté, reproductible, et logé par l'advisor (pas par Ralph) pour éviter tout soupçon de manipulation.
**Annexé à :** Pilot Services Agreement.
**Version :** 1.0 (2026-04-21).

---

## 1. The promise

> « 30-day pilot at CHF 2,400. You run the tool on 20 clients. If time savings on your quarterly review preparation don't hit 50% vs your baseline, we refund you in full. »

This document defines **time savings** precisely, so neither party leaves the pilot with room to argue.

---

## 2. Timeline (30 calendar days)

| Day | Phase | Who does what |
|---|---|---|
| **D-7 to D0** | Baseline setup | Advisor identifies 3 "baseline clients" representative of his book (one each: conservative, balanced, growth). Prepares Q1 review on each WITHOUT the tool, using current process. Logs time with timer. |
| **D0** | Kickoff call | 60-min call with Ralph. Install Claude Project access. Walk through pseudonymization SOP. Set baseline anchors. |
| **D1–D28** | Intervention | Advisor uses the tool on 20 real clients (pseudonymized). Can use it on the 3 baseline clients if Q2 review falls in window; else use on any matched-type clients. |
| **D28** | Remeasure | Advisor prepares 3 matched-type reviews WITH the tool. Logs time same way. |
| **D29–D30** | Report & decision | Joint review of numbers. Refund decision per §4. |

---

## 3. What is measured

**Time spent on "quarterly review preparation"** = start when the advisor opens the client file, stop when the review is ready to send to the client (PDF saved, no more edits).

**Included:**
- Reading portfolio snapshot
- Drafting performance commentary
- Drafting market themes section
- Formatting / branding
- Proofreading

**Excluded:**
- Live client meeting time
- Admin tasks unrelated to the review itself (sending, filing, follow-up notes)
- Tool setup time (counted separately in D0 kickoff)

---

## 4. The formula

```
baseline_avg    = mean(minutes on 3 baseline reviews WITHOUT tool)
intervention_avg = mean(minutes on 3 matched-type reviews WITH tool)

savings_pct = (baseline_avg − intervention_avg) / baseline_avg
```

**Refund triggered if :** `savings_pct < 0.50`

**Example :**
- Baseline : 3h20 + 3h50 + 3h05 = avg **3h25** (205 min)
- Intervention : 1h30 + 1h15 + 1h40 = avg **1h28** (88 min)
- Savings : (205 − 88) / 205 = **57%** → no refund, pilot validated.

Or:
- Baseline avg : 3h25 (205 min)
- Intervention avg : 2h15 (135 min)
- Savings : (205 − 135) / 205 = **34%** → **full refund**, pilot failed.

---

## 5. Logging template (provided to advisor)

Shared Google Sheet or Excel template:

| Client ref | Phase | Date | Start time | End time | Minutes | Notes |
|---|---|---|---|---|---|---|
| Client_A | Baseline | 2026-05-02 | 09:10 | 12:35 | 205 | Q1 review, no tool |
| Client_B | Baseline | 2026-05-03 | 14:20 | 17:50 | 210 | Q1 review, no tool |
| Client_C | Baseline | 2026-05-04 | 08:45 | 11:45 | 180 | Q1 review, no tool |
| Client_D | Intervention | 2026-05-28 | 09:00 | 10:25 | 85 | Q2 review, tool used |
| ... | ... | ... | ... | ... | ... | ... |

Timer rule: pause counts pause. The advisor is trusted on this (it's their own data). Ralph audits the sheet at remeasure only.

---

## 6. Edge cases

- **Advisor forgets to log one session :** that session is excluded from the average. Minimum 3 measurements per phase required for refund decision.
- **Fewer than 3 matched-type reviews in the intervention window :** extend pilot by max 14 days to complete.
- **Client types differ significantly between baseline and intervention :** default to the "most similar" pairing; if contested, re-log using 3 fresh matched pairs.
- **Tool unavailability >48h during pilot :** pilot clock pauses for the duration.

---

## 7. What this is NOT

- **Not a quality assessment.** We measure time, not the quality of the reviews. Quality is validated by the advisor's own sign-off before sending.
- **Not a client-outcomes measure.** Whether the client loves the review is a downstream question handled post-pilot, if conversion happens.
- **Not a benchmark against other tools.** Baseline is your current process, full stop.

---

## 8. Adoption of this protocol

Both parties sign off on §2–§4 at D0 kickoff. Template sheet is shared. Ralph does NOT have edit rights on the advisor's log during the pilot — read-only at remeasure.

Dispute resolution: any disagreement on the numbers is resolved in favour of the advisor (i.e., refund triggered on ambiguity). This keeps Ralph's incentive to make the tool actually work, not to negotiate the scoreboard.

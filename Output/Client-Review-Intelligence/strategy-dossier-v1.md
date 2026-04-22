## Part 1. The Thesis

### What I'm building

**Client Review Intelligence (CRI)** is an AI agent that drafts the quarterly client review letter for a wealth manager — in the firm's own writing style — from the client's portfolio data.

**Inputs the advisor provides** (once per quarter, per client):

1. **Portfolio snapshot** — holdings, values, weights at quarter-end.
2. **Market context** — rates, sectors, macro events relevant to the portfolio that quarter.
3. **Client personal context** — objectives, family situation, constraints, tax domicile.
4. **Two past firm commentaries** — so the agent calibrates on the firm's tone of voice.

**What the agent produces** (in under 2 minutes, in the firm's voice):

- **Executive summary** — the narrative of the quarter
- **Performance review** — with position-level attribution math
- **Market themes** — tied to this client's actual holdings
- **Outlook & positioning** — for the coming quarter
- **Meeting agenda** — to structure the client conversation
- **Advisor-only talking points** — discretion-sensitive items the client never sees (family events, gift planning, sensitive topics to handle carefully)

**How the advisor uses it** (3 steps):

1. Feed the four inputs into the pre-configured agent.
2. Read the draft, adjust the 5-10% that needs a human touch.
3. Export as a branded PDF, send to the client.

**Result:** 3-4 hours of manual drafting become ~15 minutes of review. The advisor is always the final filter. The agent drafts; the advisor decides, edits, and sends. It is a writing assistant, not a replacement for judgement.

**Commercial terms:** sold to boutique EAMs (3-30 FTE, FINMA-licensed) as a 30-day pilot at **CHF 2,400**, convertible to a full deployment at **CHF 7,900 setup + CHF 499/month**. The pilot is the sales motion; the deployment is the revenue engine.

### What I'm competing with

The real competition is not "doing nothing" — that is the old guard, slow and hand-written. The real competition is **what an estimated 30-50% of Swiss advisors are already doing silently: pasting cleartext client data into ChatGPT**, drafting commentary, editing, sending. This is fast and convenient — and it is a compliance violation waiting to be discovered. Art. 47 BA, FINMA 08/2024, the revised FADP all apply. Any DPO who audits will find it.

CRI is not "AI entering a market without AI." CRI is **the compliant, audited path to the productivity gain advisors are already tempted to grab.** The pilot proves the productivity. The architecture proves the compliance. That is the real pitch.

### Why now

Three forces align in 2026 and will not stay aligned:

1. **AI adoption has crossed the threshold.** 50% of Swiss financial institutions already use AI in production (FINMA 2025). Unique.ch raised USD 30M targeting private banks — the budgets exist and the objection "AI is a gimmick" is dead.
2. **The whitespace is unoccupied.** Masttro, WealthArc, Assetmax, WIZE, Expersoft own the PMS layer. Apiax/Indigita own RegTech. Nobody owns *AI commentary layer, PMS-agnostic, tone-trained, Swiss-hosted*. That position is mine to take if I move first.
3. **FINMA Guidance 08/2024 forces EAMs to think about AI governance.** The ones who already use ChatGPT on real client data are exposed. A compliant offering with a clean data posture solves a problem they now have.

### Why me

EPFL engineering (closing Bachelor June 2026) + incoming MSc FinTech at IE Madrid (September 2026) = a credential stack that is **quasi-unique** in the AI×wealth space in Europe/MEA. Swiss-based, bilingual FR/EN, family network in Dubai (father = passive pointer to wealth managers in the GCC). Twin brother formally joining as co-founder and co-face — doubles execution capacity and anchors brand identity.

### The bet

If I ship one real pilot with a Geneva EAM by end of June 2026, publish the case study, and follow the measurement protocol rigorously, the next three pilots come through referral inside the Swiss EAM community (relationship-driven market, 6-12 month sales cycle). By month 12, MRR at CHF 5-8k is realistic. The long game is a premium community (*The Chidiac Brothers*) monetised at month 18+. This dossier is the v1 snapshot of that plan on 2026-04-22.

---

## Part 2. The Market

### Swiss EAM landscape

| Metric | Value |
|---|---|
| FINMA-licensed EAMs (post-FinIA) | **1,532** |
| Estimated AUM | **~CHF 400 billion** |
| Target segment (3-30 FTE, French-speaking CH) | ~200-300 firms |
| Typical sales cycle | 6-12 months |
| Average client review prep time per advisor/week | 4-6 hours |
| Workdays lost per advisor/year to manual commentary | **~100** |

### The specific pain I'm solving

A Swiss EAM advisor runs a 40-60 client book. Each quarter, every client gets a personalised review — executive summary, performance attribution, market themes, forward-looking commentary, meeting agenda. Today this is written by hand, copy-pasted from prior quarters, politely adjusted. The result is generic. The process is the single largest non-billable time sink in the firm.

CRI does not replace the advisor's judgement. It drafts the commentary in **the firm's own voice** (calibrated on 2-3 past samples), applies rigorous attribution math, isolates the advisor-only talking points from the client-facing document, and hands back a ready-to-edit markdown. The advisor reads, tweaks, sends.

### Why Swiss private banking is a defensible niche

- **Tone is non-negotiable.** A generic "AI commentary" tool reads instantly as cheap. CRI's voice-training step is the moat.
- **Compliance is non-negotiable.** Art. 47 BA (banking secrecy) + FINMA Guidance 08/2024 (AI governance) mean every serious EAM has a compliance officer who will kill a careless vendor. My pseudonymization architecture turns this from blocker into sales asset.
- **Culture is relationship-driven.** Warm intros convert at 5-15%; cold emails at 1-3%. This is slow but sticky — once inside a firm, the next three referrals come free.
- **Competitive landscape stays niche.** US vendors won't build for 1,500 EAMs. Large Swiss PMS players won't compete with their own customers' add-ons. The window stays open.

---

## Part 3. The Product

### What CRI delivers

Per client, per quarter, the agent outputs a six-section package:

1. **Executive Summary** (80-120 words, firm's voice)
2. **Performance Review** with position-weight × position-return attribution
3. **Key Market Themes** tied to the client's *actual* holdings (not generic)
4. **Outlook & Positioning** (forward-looking, hedged unless conviction is high)
5. **Meeting Agenda** for the advisor
6. **Talking Points (Advisor-Only)** — discretion-sensitive items the client never sees

The six-section structure is non-negotiable. It mirrors how senior Swiss advisors already think about a review — adopting it means zero retraining for the advisor, who recognises the output as their own workflow, accelerated.

### Why it works

Three non-negotiable rules baked into the master prompt (v1.1, hardened after the Claude Project itself flagged issues on first test):

- **Addressee scope & register.** Single-client reviews address the client 1:1 ("Cher Dr. Perrin"), never plural, never household unless explicitly scoped.
- **Discretion handling.** Anything tagged `[discreet]` in input (e.g., a planned gift to a child) appears ONLY in Section 6. Never in Section 5 agenda where a printout could leak.
- **Attribution rigour.** Performance gaps are decomposed into `position_weight × position_return`, with hedged language unless one position explains >70% of variance.

### The toolchain (validated 2026-04-22)

Three small Python CLIs complete the delivery pipeline:

- **`pseudonymize.py`** — swaps real identifiers ↔ tokens locally via a JSON mapping. Longest-match-first, reversible, warnings on suspicious residual patterns.
- **`batch_runner.py`** — calls Claude API in parallel over a folder of pseudonymized inputs, with retries on 429/5xx. Divides a 20-client batch run by ~10×.
- **`md_to_pdf.py`** — renders to two A4 PDFs: one client-safe (Section 6 stripped) and one advisor-only (watermarked). The firewall is enforced by the tool, not just by the prompt.

Test suite (19/19 passing). End-to-end validated on the fictional Marc Perrin dataset: real API call, 40.8s, 3,996 in / 2,523 out tokens, both PDFs clean.

### Beyond the quarterly review: the voice as a platform

The quarterly review is the **entry use case** — the biggest pain, the clearest ROI, the simplest to measure in the pilot. It is not the only use case.

The architecture runs on two layers:

**Voice layer** (calibrated once during week-0 setup). The firm's tone, register, signature phrases, hedging patterns. This is the fixed asset. It lives for the life of the contract.

**Use case layer** (templates plugged into the voice layer). Each template is a specific type of client-facing writing, calibrated on the same voice. Once the voice is trained, adding a new use case is 30-60 minutes of template work, not a new setup.

**Year-round use cases unlocked progressively after pilot:**

| Use case | Frequency | Pain saved |
|---|---|---|
| Quarterly reviews *(use case #1, proved in pilot)* | 4× / year × 50 clients | 100 workdays / year / advisor |
| Ad-hoc market letter (Fed move, geopolitics, etc.) | 4-8× / year firm-wide | 2-4h per event |
| Proposal drafts for new HNWI prospects | 10-30× / year | 3-5h per proposal |
| Meeting prep briefs (pre-meeting research + agenda) | 5-15× / week / advisor | 30 min each |
| Response drafts (client email, concerned inquiry) | 5-10× / week | 30 min each |
| Post-meeting follow-up letters | 3-5× / week | 20 min each |
| Annual review (more elaborate than quarterly) | 1× / year × clients | 5-7h per client |
| Event-driven client alerts (drawdown, drift) | ad hoc | 1-2h per event |
| Monthly firm newsletter | 12× / year | 4-6h per newsletter |

**What this means commercially.** A 5-advisor EAM signing the full deployment (CHF 7,900 + CHF 499/month) is not paying for "4 review runs per year." They are paying for a **voice-trained agent available year-round**, with use case #1 (quarterly reviews) proved during the pilot and use cases 2-9 unlocked progressively at their pace, with no new setup.

Realistic year-1 economics for that 5-advisor firm:
- Quarterly reviews: 500 workdays / year saved (5 × 100)
- Ad-hoc, meeting prep, follow-ups: 300-500 workdays / year
- **Total: 800-1,000 qualified workdays / year** at an advisor cost of ~CHF 1.3-1.6M
- Subscription cost: CHF 5,988 / year
- ROI: 220-270×

The pilot is the wedge. The subscription is the voice layer and all the writing it unlocks. That is the retention story, and it is honest: if the agent does not extend beyond quarterly reviews, CHF 499/month is overpriced. It does extend — because the voice calibration is reusable infrastructure.

### Why not just use ChatGPT?

The honest question every EAM advisor asks: *"Why pay for CRI when ChatGPT Plus is USD 20 / month and my advisor can type client data directly?"*

| Dimension | Naked ChatGPT | CRI |
|---|---|---|
| Voice calibration | Guessed from "write in my firm's voice" prompt | Engineered from 2-3 firm samples, reproducible across advisors and quarters |
| Discretion firewall | None — sensitive info bleeds into output | Section 6 structural separation + PDF stripper tool |
| Attribution math | Plausible-sounding, often wrong | `position_weight × position_return`, hedged language unless >70% variance explained |
| Compliance posture | Cleartext data → US cloud ≈ art. 47 BA violation risk | Pseudonymization layer, mapping local, DPA provided, FINMA-aligned |
| Measurement | None — advisor "feels" faster | Baseline + remeasure, refund if <50% savings |
| Year-round use cases | Re-invent prompt per use case | Voice layer reusable across 9 use cases |
| Ongoing maintenance | Advisor's own problem | Included in subscription (model migration, guideline updates, new templates) |

**What I actually sell:** not a prompt (which could be copied), but **voice-calibration expertise, compliance architecture, measurement rigor, and ongoing service** delivered through a tool. A firm that tried to DIY would need: a prompt engineer (CHF 6-12k upfront), a compliance consultant (CHF 4-10k), and an ongoing maintenance budget (CHF 2-5k / year). Total year 1: **CHF 12-27k vs CHF 13,888** for CRI full deployment — and CRI comes with proven voice expertise, a measurement protocol, and a refund clause.

### What I'm NOT doing

- Not a PMS. I don't own portfolio data.
- Not an advisor. I don't give investment advice.
- Not FINMA-authorized. Not required for an advisory tool used inside the EAM.
- Not a SaaS-first company in phase 1. I'm a consultant building the first 3 installs by hand.

---

## Part 4. The Pilot Model

### The offer

**CHF 2,400. 30 days. One advisor, 20 real clients (pseudonymized). Full refund if time savings <50% vs baseline. Pilot fee credited 100% against full deployment if converted.**

### How it's measured

Not "do you feel faster." A signed protocol annexed to the pilot agreement:

| Phase | When | What |
|---|---|---|
| Baseline | D-7 → D0 | Advisor preps Q1 review on 3 representative clients WITHOUT the tool. Times each. |
| Kickoff | D0 | 60-min call. Access, SOP, anchors. |
| Intervention | D1-D28 | Tool used on 20 real clients. |
| Remeasure | D28 | 3 matched reviews WITH tool. Same timer rule. |
| Decision | D29-D30 | Formula applied. Refund if <50%. |

Formula: `savings = (baseline_avg − intervention_avg) / baseline_avg`. If `savings < 0.50` → full refund.

The advisor owns the log. I get read-only at remeasure. Any ambiguity resolves in the advisor's favour. This structure removes every argument vector — the only remaining question is "does the tool work." It does.

### What success looks like

**P1 — first pilot signed by end of June 2026.** This is the single most important milestone of the next 10 weeks. Without it, every downstream action (Dubai pack, content flywheel, community engine) is theoretical.

### Sales cycle reality

- 6-12 months is the **full deployment** cycle in Swiss EAM. Don't confuse this with pilot signature.
- Pilot-to-deployment conversion: target 50%+ (because pilot is a genuine try-before-buy, not a demo).
- First full deployment realistically signs **late August / September 2026**. Not late June.
- Dubai window: physical presence June-August = 1 pilot signed during that window is the P3 milestone.

---

## Part 5. Compliance Posture

### Compliance is the product, not a constraint

In a regulated industry, the compliant provider wins. That is especially true in Swiss private banking, where discretion is not a feature — it is the whole value proposition of the market. What clients pay Swiss EAMs for is the promise that their affairs stay inside a controlled perimeter.

Every EAM compliance officer knows that their advisors are under pressure to use AI. Some are using it already, without controls. The question each firm faces is not *"should we use AI?"* but *"who brings us a vetted pipeline?"*

CRI is designed to be that vetted pipeline. The regulatory frame below is not a disclaimer — **it is the architecture of the product.** Pseudonymization is enforced by the tool, not left to advisor discretion. The mapping file stays on the advisor's workstation — we never see it. What Anthropic receives is tokenized. DPA, SOP, and audit rights are contractual. It is the difference between advisors improvising on the firm's liability, and advisors operating a pipeline designed for Swiss compliance.

### Regulatory frame

| Instrument | What it says | Why it matters here |
|---|---|---|
| Art. 47 BA | Swiss banking secrecy | Cleartext client identifiers cannot go to US cloud without legal basis |
| FINMA 2023/1 | Operational risks, critical data concept | Cloud AI processing of client data falls in scope |
| FINMA Guidance 08/2024 | AI governance | EAMs must understand their outsourced AI, contractually govern it |
| Revised FADP (2023) | Swiss data protection | Cross-border transfer restrictions, consent, minimization |
| SBA Cloud Guidelines 3rd ed. (Nov 2025) | Cloud framework | Applicable to cloud-based processing in Swiss banking |

### The architectural answer: pseudonymization firewall

Cleartext identifiers never leave the advisor's perimeter. The pipeline is:

```
Advisor workstation  →  Local pseudonymization  →  Claude API  →  Local re-personalization
     (full data)            (by the advisor)          (tokens)           (by the advisor)
```

Fields tokenized: name, spouse, children, residence (to canton level), portfolio size (to bracket), custody account IDs, dates of birth (to age bracket), AHV/Steuer-Nr (never transmitted at all). The advisor owns the mapping file. I never receive pseudonymization keys.

### Post-pilot Swiss-hosted path

Full deployment migrates to either:
- **Azure Switzerland** with Claude in-region endpoints (available as of 2025), or
- **Swiss-hosted open-weights** on Infomaniak / Exoscale (performance trade-off, case-by-case).

At deployment, pseudonymization becomes optional. This is the natural upsell narrative: pilot proves value under pseudonymization → deployment removes the friction.

### What I commit, what I don't

**I commit:** pilot services agreement, DPA (EAM = controller, me = processor), pseudonymization SOP + template, mutual NDA. Anthropic commercial tier (no training on inputs, 30-day retention for abuse monitoring).

**I don't commit:** FINMA authorization (not required for an advisory tool), Swiss-hosted infrastructure in pilot phase, persistent storage of client data on my side (inputs are processed and discarded).

Clarity on what I am and am not **pre-empts** the tough compliance questions. The pack is designed to survive a 10-minute DPO review without friction.

---

## Part 6. Brand Architecture

### The four-layer stack

| Layer | Name | When activated |
|---|---|---|
| Personal brand (primary) | **Ralph Chidiac** (EPFL + IE Madrid FinTech) | Now |
| Visible duo | **Ralph & [brother] Chidiac** | Once brother formalises co-founder deal |
| Personal brand endgame | ***The Chidiac Brothers*** (podcast + community) | Month 6-9 |
| Product | *Client Review Intelligence* (descriptive) | Locked once 3+ clients |
| Legal company | **PUNTED** | Decided at 3 clients or 6 months or product clarity |

### Why no company name yet

Hormozi, Yomi Denzel, Gadzhi, the Tate brothers — all built the founder persona **before** the company name. Reason: in pre-pilot phase, a company name with no track record is LARP. A credentialed human with no company name reads as "early stage, but serious." In a relationship-driven market (Swiss EAM), the second positioning wins every time.

Company name arrives **after** proof: 3+ pilots signed or a case study published. Not before.

### The visible surface (phase 1)

- **LinkedIn profile** — understated, credentials-led, no product pitch. Headline: *EPFL Communication Systems · Incoming IE Madrid MSc FinTech · Building with my brother*. About: identity + trajectory only, zero sales pitch. Hidden Skills section (amateur signal in Swiss private banking register). No "building AI for Swiss wealth managers" — that's founder-brand theater before the first pilot.
- **YouTube `@ralphchidiac`** — hosts the 90-second demo video **unlisted**, viewable only via link.
- **Calendly `calendly.com/ralphchidiac`** — 15-min Client Review Intelligence Discovery Call, free tier.
- **Leave-behind PDF pack** (3 pages A4) — sent by email after each discovery call.
- **Domains reserved, sites empty** — `ralphchidiac.com` + `ralphchidiac.ch` + `chidiacbrothers.com`. No landing page in phase 1. Swiss EAM culture is word-of-mouth; landing pages don't sign pilots.

### The register

Intello-premium, EPFL-backed, understated. No bombast, no "revolutionary AI." Silence on social media in phase 1 **is the signal** to the Swiss market. Loud = amateur here.

---

## Part 7. The Endgame (3 phases)

### Phase 1 — Switzerland (April → August 2026)

Geneva + Lausanne priority. 30 EAMs targeted from direct network and FINMA register filter. Warm intros through university, family, past internships, custodian desks (Julius Baer, UBP, Sygnum, Maerki Baumann). **Goal:** 1-2 pilots signed by June, first full deployment signed by September, first case study publishable by October.

### Phase 2 — Dubai (summer 2026, physical window)

Father's passive pointer list activated. Pack = 1-pager + demo video + Swiss case study (if ready). CHF currency becomes USD. **Goal:** 1 Dubai pilot signed during the June-August physical presence window. Pricing: USD 6,900 setup + USD 499/month.

### Phase 3 — Madrid + Europe (September 2026+)

IE FinTech cohort activates automatically — founders, VCs, guest lectures, classmates from 40+ countries. Remote-first operation. EUR added. Content EN scaled on LinkedIn + YouTube. **Goal:** 3-5 clients total (Swiss + Dubai + Spain), MRR CHF 2-5k/month, podcast *The Chidiac Brothers* launched, 10k qualified EN followers.

### The long game — community premium (Month 18+)

*AI Wealth Program* — cohort-based premium community under *The Chidiac Brothers* personal brand. Launch target: USD 200-350k in one cohort. Model inspired by Real World / Ecom Empire but European, clean, credential-led (EPFL + IE, not street). Year 3 target: established AI company with 7-figure revenue + community of 1,000+ paying members internationally.

---

## Part 8. The Diagnosis

### The bottleneck today

Zero proof. Zero revenue. Until CRI has shipped to one real EAM with measurable time savings, every downstream asset (content authority, cohort premium, referral engine) is blocked by lack of substance. The plan's P1 milestone — one pilot signed by end of June 2026 — is the unlock.

### The abandonment pattern I'm structurally fighting

Three projects started, zero shipped: VSL real estate agency, nightlife app, DJ duo. Common thread: each was abandoned **before any public feedback arrived**. The DJ duo lasted longest — because it had visibility. CRI is designed to exploit this: the pilot generates feedback within 30 days, the brand demands visibility (LinkedIn, YouTube, video), the twin brother adds fraternal accountability. If I keep attacking, the pattern is broken. If I disappear for 2 weeks, the pattern wins.

### Current live risks

| Risk | Mitigation |
|---|---|
| First pilot doesn't sign by end of June | Warm-intro first, cold outreach second. 30 targets (qualified) is the floor, not the ceiling. |
| Video not shot by 2026-04-24 | Script locked, toolchain validated — no remaining technical blocker, only execution with brother. |
| Brother not formally committed | Conv scheduled for 2026-04-23. No first client signature until written alignment exists. |
| EAM compliance officer kills the deal | Compliance one-pager + DPA template ready, designed to survive a 10-minute DPO review. Pseudonymization is the architectural answer, not a promise. |
| Pilot run but <50% time savings → refund | Refund is built into the model, not a failure to hide. Cost is 30 days and CHF 2,400 returned; gain is direct product learning. |

### Strength patterns to double down on

- Ralph's **four course corrections** in a row on positioning (no site, no CRI-experience on LinkedIn, no Skills section, no over-promise in outreach) proved more reliable than BOS default recommendations. Trust the instinct at first pushback.
- Network-first approach: warm intros + Dubai family + future IE cohort = three acquisition waves in 12 months that most solo founders don't have. Exploit systematically.

---

## Part 9. The 30-Day Execution Plan

### Done (April 20-22)

- Direction locked: AI × Swiss wealth, single module, Ralph-first brand architecture.
- Market validated: 1,532 EAMs, whitespace confirmed, pricing defensible.
- Domains + handles reserved (`ralphchidiac.com/.ch`, YouTube channel live).
- LinkedIn profile optimised (understated, stage-appropriate).
- Module 1 artefacts: master prompt v1.1 hardened, fictional Perrin dataset, sample output, 90-second script, compliance one-pager, pilot measurement protocol, leave-behind pack.
- Toolchain built and validated end-to-end (pytest 19/19, real API run, PDF firewall verified).
- Outreach pack v1.1 locked (EN, understated register, "How it works" not "What we built").

### In-flight (April 23-27)

| Action | Who | Deadline |
|---|---|---|
| Formal co-founder conversation with brother (time, equity, roles, on-camera commitment) | Ralph | 2026-04-23 |
| Brief the "worker" friend on his backbone ops role | Ralph | 2026-04-26 |
| Shoot the 90-second demo video with brother (2 takes, good enough) | Ralph + brother | 2026-04-24 |
| Fill the 30-EAM pipeline (15-20 from network, rest via FINMA register) | Ralph | 2026-04-27 |
| Export leave-behind PDF (Typora / Google Docs / strategy_to_pdf) | Ralph | 2026-04-27 |

### Launch (April 28)

First 5-10 warm outreach messages go out. Bilateral LinkedIn + email, following the locked outreach pack register. Calendly link included. Demo video embedded or linked.

### Month 1 goals (by 2026-05-28)

- 30 messages sent across the qualified pipeline
- 8-10 responses received
- 3-5 discovery calls booked and held
- 1-2 serious pilot conversations advanced to DPA review

### Month 2 goal (by 2026-06-30)

**First pilot signed.** CHF 2,400 invoiced. P1 milestone hit.

---

## Part 10. Key Numbers (Appendix)

### Pricing

| Format | Price | Scope |
|---|---|---|
| Pilot 30 days | **CHF 2,400** | 1 advisor, 20 real clients (pseudonymized) |
| Full Deployment | **CHF 7,900 setup + CHF 499/month** | Whole firm, Swiss-hosted, tone-trained |
| Dubai pilot (summer 2026) | USD 2,600 | Mirror of Swiss pilot |
| Dubai full deploy | USD 6,900 + USD 499/month | Mirror of Swiss deployment |

### Conversion targets (phase 1)

| Channel | Open → Respond | Respond → Meeting | Meeting → Pilot |
|---|---|---|---|
| Warm intro | 40-60% | 40-60% | 15-30% |
| Cold email / LinkedIn | 5-10% | 30-50% | 5-15% |

Realistic funnel: 30 qualified messages → 8-10 responses → 3-5 meetings → 1-2 pilots by end of May.

### Market sizing

- **1,532** FINMA-licensed EAMs post-FinIA
- **~CHF 400bn** total AUM
- **~200-300** firms in my target segment (3-30 FTE, French-speaking CH, HNWI book)
- AI adoption among Swiss FIs: **~50%** (FINMA 2025)
- Average time spent per quarterly review: **3-4 hours**, i.e. ~100 workdays/year on a 50-client book

### Milestone timeline

| Palier | Target | Milestone |
|---|---|---|
| P0 | 2026-04-20 | Setup complete, Module 1 built |
| **P1** | **2026-06-30** | **First pilot signed (CHF 2,400)** |
| P2 | 2026-09-30 | First full deployment signed (CHF 7,900 + 499/m) |
| P3 | 2026-08-31 | First Dubai client signed (USD 6,900 + 499/m) |
| P4 | 2026-10-31 | 3-5 clients total, first case study, podcast launched |
| P5 | 2027-04-30 | 80-150k cumulative revenue, MRR 5-8k/month, 10k EN followers |
| P6 | 2027-10-31 | *AI Wealth Program* cohort launch — USD 200-350k in one launch |
| P7 | 2029 | Company 7-figure annual revenue + community 1,000+ members |

### Contact (current)

Ralph Chidiac · Geneva · EPFL engineering (closing June 2026) · Incoming IE Madrid MSc FinTech (September 2026) · Twin brother co-founder · `ralph@ralphchidiac.ch` · `calendly.com/ralphchidiac`

---

*Strategic Dossier v1 · Compiled 2026-04-22 · For Ralph's own clarity · Not for external distribution.*

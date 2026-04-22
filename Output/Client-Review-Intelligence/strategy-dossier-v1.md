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

### What I'm competing with — three horizons

CRI does not compete against a single alternative. It competes across three horizons simultaneously, and its moat has to hold against all three.

**Horizon 1 — today.** Inside any given EAM, the quarterly review gets written in one of four ways:
- *Hand-written from scratch* by senior advisors who don't trust AI. The dominant mode in the old guard.
- *Silent improvisation* on naked ChatGPT by advisors who have figured out the shortcut but not the compliance framework. Fast and fragile — a compliance violation waiting for a DPO to discover it.
- *Junior analyst or intern* drafting under senior review. Common in mid-sized boutiques.
- *Offshore drafting services* (Asia). Cheapest, compliance nightmare, used only by firms that have accepted the trade-off.

CRI's pilot wedge lands on the second and third modes — where the productivity pain is acute and the advisor is already reaching for a tool.

**Horizon 2 — the next 12 to 24 months.** The real structural threat: PMS vendors adding AI commentary features natively. The current state of their public AI narratives (audited April 2026):
- **WealthArc** has the clearest AI push: in 2025 it launched an *AI Agent* that converts financial documents (account statements, capital-call notices, performance reports) into structured data, plus a *"Chat with your Data"* Q&A feature. It is **not** a quarterly-letter generator yet, but it is the vendor closest to that frontier.
- **Masttro** markets *"Masttro Intelligence"* — natural-language Q&A on portfolio data, agentic AI for capital calls / alternatives document capture. Positioned for family offices (10,000+ users, 650+ custodian feeds), not Swiss EAM boutiques at the 5-30 FTE size CRI targets.
- **Assetmax**, **WIZE by TeamWork**, **Expersoft** have no publicly announced AI commentary features as of the audit. Likely in roadmap, not in market.

(Sources: WealthArc AI agent launch coverage 2025; Masttro Intelligence product pages; vendor websites, all accessed 2026-04-22. See `audit-sources.md`.)

CRI's moat against this horizon: the PMS vendor's AI layer faces the same Swiss compliance problem any cloud LLM faces — cleartext client data routed through a model hosted outside the Swiss perimeter. The PMS does not magically solve the FinIA art. 69 (professional secrecy, covers EAMs), nFADP cross-border transfer rules, and FINMA Guidance 08/2024 governance obligations just because it holds the data. CRI's pseudonymization architecture, by contrast, is enforced by design: tokenization happens on the advisor's workstation *before* anything leaves the perimeter. That is the forward-looking defense — CRI is deployable PMS-agnostic, and its compliance posture is not contingent on whichever PMS the firm happens to use.

**Horizon 3 — 24+ months.** Market consolidation. CRI's survival depends on: expanding into a multi-use-case voice agent (already the v1.2 reframe), or being acquired by a PMS vendor as their compliance-grade AI layer, or becoming the recognised leader in compliance-first AI tooling for Swiss private wealth.

CRI is not "AI entering a market without AI." CRI is **the compliant, audited path to the productivity gain advisors are already reaching for — deployable independently of whichever PMS the firm uses, and defensible even when the PMS vendors launch their own AI features.** The pilot proves the productivity. The architecture proves the compliance. The PMS-agnostic design is the 24-month hedge.

### Why now

Three forces align in 2026 and will not stay aligned:

1. **AI adoption has crossed the threshold.** FINMA's own April 2025 survey of ~400 licensed institutions reports roughly **50% already use AI or have applications in development**, and another ~25% plan to within three years. Of the 187 institutions actively using AI, 91% also use generative AI. (FINMA press release, 24 Apr 2025.) Swiss EAMs are under-represented in that survey — they sit in the small "other institutions" bucket — which means the objection *"AI is a gimmick"* is dead for banks, and EAMs know they are the lagging segment the regulator is watching. Unique.ai closed a **USD 30 M Series A in February 2025** (CommerzVentures + DN Capital, with VI Partners and Pictet Group) serving Pictet, UBP, SIX, LGT, Partners Group — proof the budgets exist in Swiss wealth.
2. **The whitespace is unoccupied at the Swiss EAM boutique tier.** WealthArc and Masttro have launched AI features but on data Q&A and document structuring, not quarterly-letter drafting. Assetmax, WIZE, Expersoft have no publicly announced AI commentary yet. Apiax and Indigita are RegTech, not competitors. Nobody, as of this writing, ships a production *"voice-calibrated, pseudonymization-first, PMS-agnostic quarterly review agent"* for boutique Swiss EAMs. That position is mine to take before the PMS vendors close the gap in 12-24 months.
3. **FINMA Guidance 08/2024 (18 Dec 2024) directly applies to EAMs.** The guidance's four pillars — governance, data quality, testing/explainability/bias, documentation — are addressed to all FINMA-supervised institutions including portfolio managers and trustees under FinIA. Every EAM compliance officer now has a checklist they did not have 14 months ago. The ones whose advisors are already improvising on ChatGPT are exposed against that checklist. A vendor that arrives with a governance-ready architecture (DPIA-friendly, DPA-ready, pseudonymization-enforced, vendor contract aligned to the Guidance's requirements) solves an audit problem they now have.

### Why me

EPFL engineering (closing Bachelor June 2026) + incoming MSc FinTech at IE Madrid (September 2026) = a credential stack that is **quasi-unique** in the AI×wealth space in Europe/MEA. Swiss-based, bilingual FR/EN, family network in Dubai (father = passive pointer to wealth managers in the GCC). Twin brother formally joining as co-founder and co-face — doubles execution capacity and anchors brand identity.

### The bet

If I ship one real pilot with a Geneva EAM by end of June 2026, publish the case study, and follow the measurement protocol rigorously, the next three pilots come through referral inside the Swiss EAM community (relationship-driven market, 6-12 month sales cycle). By month 12, MRR at CHF 5-8k is realistic. The long game is a premium community (*The Chidiac Brothers*) monetised at month 18+. This dossier is the v1 snapshot of that plan on 2026-04-22.

---

## Part 2. The Market

### Swiss EAM landscape (sourced)

| Metric | Value | Source |
|---|---|---|
| FINMA-approved portfolio managers + trustees (Art. 17 FinIA, 28 Feb 2025) | **1,532** (of 1,864 applications; 131 withdrawn; 94 under review) | FINMA press release 11 Mar 2025 |
| Of which, genuine EAMs (excluding pure trustees) — industry estimate | **~1,300-1,500** | finews/Aquila sector study |
| Total AUM (SAM members only) | **~CHF 500 bn** | SAM / VSV / ASG |
| Total AUM (full Swiss IAM sector, extrapolated) | **~CHF 887 bn** | FIN21/finews |
| Share of Swiss wealth management market (IAM sector) | ~15% | FIN21/finews |
| >80% of IAM firms employ | **≤10 people** | FIN21/finews |
| Two-thirds of firms AUM range | **CHF 100 m – CHF 2 bn** | FIN21/finews |
| Two-thirds of managing directors | **>50 years old** (succession indicator) | FIN21/finews |
| FINMA-licensed Supervisory Organisations | **5 SOs** (AOOS, OSIF, SO-FIT, OSFIN, FINcontrol) | FINMA |
| SAM / VSV / ASG members | **>2,500** | VSV/ASG |
| Typical Swiss wealth-vendor sales cycle | **6-12 months** | industry estimate, directionally supported by B2B financial-services avg 60-120 days |
| Advisor book size (industry: US/global benchmark) | **50-100 "real" client relationships** (Kitces) | Kitces Research |
| Advisor time on meeting prep (US/global) | **5.3 hrs/week** (Kitces) | Kitces Research |
| Derived time per quarterly review | **~3-4 hrs** (Kitces-derived: 5.3h prep / 3.8 quarterly meetings per week) | Derived; no Swiss-primary source |
| Workdays/year recovered per advisor at 50-client book × 3-4h × 4 quarters ÷ 8h/day | **75-100 workdays** | Calculated |

See `audit-sources.md` for URL list and access dates.

### Regulatory and supervisory context

Swiss EAMs post-FinIA (2020) are supervised through a two-tier structure: **FINMA licenses and retains enforcement authority**, while one of **five Supervisory Organisations (SOs)** handles ongoing compliance monitoring — AOOS (Zurich, the largest, founded by SAM/VSV), OSIF (Geneva), SO-FIT (Geneva), OSFIN (Neuchâtel), and FINcontrol Suisse (Bern, VQF-owned). This structure is the regulatory context a compliance officer lives inside every day, and it is the audit environment CRI must survive.

The **Swiss Association of Wealth Managers (SAM / VSV / ASG)** is the dominant industry association. >2,500 members collectively managing ~CHF 500 bn. Relevant as a distribution channel: directory access, events, model contracts, mandatory ombudsman affiliation. Annual membership fee CHF 5,000 + VAT. Competing association worth noting: **Alliance of Swiss Wealth Managers (ASWM)**, which counts Prime Partners and other larger boutiques among its members.

### The specific pain I'm solving

A Swiss EAM advisor runs a 50-client book (Kitces-consistent benchmark for "real" advisor relationships at this tier). Each quarter, every client gets a personalised review — executive summary, performance attribution, market themes, forward-looking commentary, meeting agenda. Today this is written by hand, copy-pasted from prior quarters, politely adjusted. The result is generic. The process is the single largest non-billable time sink in the firm.

Time per quarterly review is **3 to 4 hours** — derived from Kitces Research (5.3 hrs/week on meeting prep, ~3.8 quarterly meetings/week). For a 50-client book, that is **150-200 hours every quarter, or 600-800 hours per advisor per year, or 75-100 workdays annually**. At a Swiss senior advisor loaded cost of **CHF 200-400/hour** (derived from Glassdoor/PayScale/WealthBriefing compensation data + Swiss employer loading), the year-round time cost is **CHF 120,000-320,000 per advisor**. For a 5-advisor firm, up to **CHF 1.6 million in recoverable qualified time annually**.

CRI does not replace the advisor's judgement. It drafts the commentary in **the firm's own voice** (calibrated on 2-3 past samples), applies rigorous attribution math, isolates the advisor-only talking points from the client-facing document, and hands back a ready-to-edit markdown. The advisor reads, tweaks, sends. Senior judgement stays with the senior advisor; drafting labour leaves.

### Why Swiss private banking is a defensible niche

- **Tone is non-negotiable.** A generic "AI commentary" tool reads instantly as cheap. CRI's voice-training step is the moat — each firm's 2-3 past samples become the calibration asset that competitors cannot replicate without onboarding the same firm.
- **Compliance is non-negotiable.** FinIA Art. 69 (professional secrecy for EAMs, parallel to Art. 47 BA for banks), FINMA Guidance 08/2024 (AI governance), the revised FADP (Sept 2023), and — flowing down from custodian banks — FINMA Circular 2023/1 + SBA Cloud Guidelines 3rd ed. (Nov 2025) collectively mean every serious EAM has a compliance officer who will kill a careless vendor. CRI's pseudonymization-at-source architecture and vendor-contract package (DPA with Swiss FADP addendum, SOP, audit rights) turn this from blocker into sales asset.
- **Culture is relationship-driven.** Warm intros in Swiss wealth B2B convert at **40-60% response and 15-25% meeting conversion**; cold email at ~3.4% (financial services benchmark), cold LinkedIn at 26-29% acceptance with ~11% reply. Adjust down 0.7-0.8× for Swiss / DACH vs US baseline. Slow but sticky — once inside a firm, the next three referrals come free.
- **Competitive landscape stays niche.** US vendors won't build for a 1,300-1,500-firm market. Large Swiss PMS players will launch AI features natively in 12-24 months (the Horizon 2 risk, addressed in Part 1); the CRI window is the time it takes them to get there, and CRI's PMS-agnostic + compliance-first design is the hedge against their arrival.

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
| Compliance posture | Cleartext client data → US cloud = FinIA Art. 69 and nFADP cross-border transfer exposure, FINMA 08/2024 governance gaps | Pseudonymization-at-source, mapping key retained locally, Anthropic DPA with Swiss FADP addendum, ISO 42001 AI governance, ZDR available on enterprise contract |
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

### Regulatory frame (sourced, primary-instrument-first)

An important precision first: **Art. 47 Banking Act (BA) does not directly cover EAMs**. It applies to banks and securities firms. EAMs licensed under the Financial Institutions Act (FinIA, 2020) are subject to a parallel professional-secrecy regime under **Art. 69 FinIA**, with penalties broadly similar — custodial up to three years or a monetary penalty for intentional unauthorised disclosure (CapLaw, Global Investigations Review, accessed 2026-04-22). Art. 47 BA reaches the EAM **indirectly**, through its custodian relationship: custodian banks will flow down their own Art. 47 BA and FINMA Circular 2023/1 obligations to the EAM contractually. This two-layer reality — direct FinIA Art. 69, plus indirect Art. 47 BA via custodians — is how a Swiss EAM compliance officer thinks about the framework.

| Instrument | What it says | Applies to EAM | Why it matters here |
|---|---|---|---|
| **FinIA Art. 69** (professional secrecy for portfolio managers / trustees) | Criminalises intentional unauthorised disclosure of client data by EAM directors, employees, agents, liquidators. Custodial up to 3 years or monetary penalty. | **Directly** — primary instrument for EAMs | Any cleartext identifier leaving the EAM perimeter without legal basis is an Art. 69 exposure. |
| **FINMA Guidance 08/2024** on governance and risk management when using AI (18 Dec 2024) | Four pillars: governance & AI inventory, data quality, testing/explainability/bias, documentation/independent review. Explicitly extends to third-party AI. | **Directly** — all FINMA-supervised institutions including FinIA-licensed EAMs | The compliance checklist every EAM must apply before deploying a vendor AI tool. CRI's documentation is designed to fit this checklist. |
| **Revised FADP (nFADP, in force 1 Sept 2023)** | Swiss data protection law. Pseudonymized data remains personal data when re-identification is possible. Cross-border transfer requires adequacy, SCCs, or derogation. DPIA mandatory for high-risk processing (Art. 22). | **Directly** | CRI inputs, even tokenized, count as personal data from the EAM's perspective. Cross-border transfer rules apply. |
| **Swiss-US Data Privacy Framework** (adequacy route, in force 15 Sept 2024) | Adds the US to the Swiss adequacy list for transfers to **DPF-certified** US recipients. Non-certified recipients require SCCs. | **Directly** | CRI's transfer pathway to Anthropic (US-hosted) rides on either DPF certification status — to be verified on Anthropic's trust portal — or on Swiss SCCs as a fallback. |
| **FINMA Circular 2023/1** (Operational Risks and Resilience — Banks; in force 1 Jan 2024) | Principle-based operational-risk regime for banks. Introduces "critical data" concept (broader than the old CID). Addresses outsourcing, cloud, ICT, BCM, resilience. | **Indirectly** (banks only; reaches EAMs via custodian flow-down clauses) | When the EAM's custodian is a bank, the custodian's contractual requirements typically pass Circular 2023/1 obligations downstream. CRI's architecture must survive this flow-down. |
| **SBA Cloud Guidelines, 3rd ed.** (4 Nov 2025) | Non-binding SBA recommendations. Data classification (bank-client data + critical data), risk-based approach, audit rights, exit strategy, foreign-lawful-access (CLOUD Act) section. **No AI-specific provisions**. | **Indirectly** (banks; EAMs via flow-down) | Custodian-driven flow-down; CRI's compliance pack addresses the same principles even for non-bank EAMs. |

### Is the pseudonymization approach legally defensible?

**Under nFADP:** Yes, but with nuance. Pseudonymized data where the mapping key stays with the controller **remains personal data** (Swiss and European consensus, consistent with GDPR Recital 26 and CJEU Breyer C-582/14). The CRI architecture therefore does not take the processing out of nFADP scope. It does materially reduce risk, because the recipient (Anthropic) is in a position where practical re-identification is unavailable — the CJEU's "relative approach" (SRB v EDPS, 2023) suggests such data may be effectively anonymous in the recipient's hands while remaining personal in the controller's. Swiss regulators have not explicitly adopted this doctrine but are expected to follow the European line.

**Under FinIA Art. 69 / Art. 47 BA:** Banking and professional secrecy protect information that identifies or is linked to a specific client. Robust pseudonymization where the mapping key stays inside the EAM perimeter **substantially mitigates** (but does not categorically eliminate) secrecy risk. The 2019 SBA/LLAG legal opinion on bank secrecy and cloud recognises that when a cloud provider cannot practically re-identify clients, secrecy exposure is materially reduced. **No FINMA primary guidance explicitly endorses pseudonymization as a safe harbour.** We do not claim that it is one; we position it as a defensible, layered control under a broader governance regime.

**The bottom line for CRI's compliance narrative:** the pseudonymization-at-source architecture is defensible, but not a magic shield. Its defensibility comes from being one layer in a stack: (a) pseudonymize at source, (b) Swiss-US DPF or SCCs, (c) DPIA (likely required under Art. 22 nFADP given AI + financial data + cross-border transfer), (d) FINMA Guidance 08/2024 governance (inventory, risk classification, vendor contract, monitoring), (e) Anthropic commercial contract (no training on inputs, ZDR option). Present this as a layered defence, not a single silver bullet. It survives a 10-minute DPO review because every layer is documented.

### The architectural answer: pseudonymization firewall

Cleartext identifiers never leave the advisor's perimeter. The pipeline is:

```
Advisor workstation  →  Local pseudonymization  →  Claude API  →  Local re-personalization
     (full data)            (by the advisor)          (tokens)           (by the advisor)
```

Fields tokenized: name, spouse, children, residence (to canton level), portfolio size (to bracket), custody account IDs, dates of birth (to age bracket), AHV / Steuer-Nr / any tax identifier (never transmitted at all). The advisor owns the mapping file. CRI never receives pseudonymization keys.

### Anthropic (the downstream processor) — verified terms

The commercial API tier governs CRI's use of Claude:

- **Training:** verbatim Anthropic Privacy Center, *"By default, we will not use your inputs or outputs from our commercial products (e.g. Claude for Work, Anthropic API, Claude Gov, etc.) to train our models."* Opt-in required for training use.
- **Retention:** default 30 days for inputs/outputs at the backend. **API logs specifically reduced to 7 days since 15 September 2025** (per public reporting). Exceptions: services with longer customer-controlled retention (Files API), enterprise ZDR contracts, Usage Policy enforcement (up to 2 years for inputs, up to 7 years for trust-and-safety classifier scores).
- **Zero Data Retention (ZDR):** available on enterprise contract and security addendum for qualifying customers. Under ZDR, customer data is not stored at rest after the API response is returned. **For Swiss EAM handling client data, ZDR is the version to contractually require.**
- **DPA:** Anthropic's Data Processing Addendum incorporates EU Standard Contractual Clauses (Modules 2 and 3) plus UK and **Switzerland addenda**. Auto-incorporated in Commercial Terms of Service — signing ToS = signing DPA. Customer is controller; Anthropic is processor; Anthropic commits not to sell or share personal data.
- **Encryption:** AES-256 at rest, TLS 1.2+ in transit. MFA and least-privilege access controls.
- **Certifications:** SOC 2 Type I and Type II, ISO 27001:2022, **ISO/IEC 42001:2023** (AI management systems — the first dedicated AI-governance standard), HIPAA-ready (BAA on qualifying contracts). Reports obtainable via Trust Portal under NDA.
- **Sub-processors:** primary AWS, plus Google Cloud and Microsoft Azure. Published at `trust.anthropic.com/subprocessors`.
- **Swiss-US DPF certification status:** **to be verified before each pilot** at Anthropic's Trust Center. If certified, adequacy covers the transfer. If not, Swiss SCCs apply.
- **Liability:** limited to fees paid in the 12 months preceding a claim, with IP indemnity carve-outs. Enterprise tier can negotiate stronger terms.

(All Anthropic facts from Anthropic Privacy Center and Trust Portal, access 2026-04-22. See `audit-sources.md`.)

### Regions and the "Swiss-hosted" narrative — honest version

A precision that corrects our earlier drafts. **Anthropic does not today offer a native Switzerland region for Claude.** The closest EU-resident options for a Swiss customer are:

- **AWS Bedrock Frankfurt** (eu-central-1, with cross-region inference)
- **Google Vertex AI Frankfurt** (direct in-region processing)
- **Azure AI Sweden Central** (the unique EU region for Claude on Azure)

None of these three is physically in Switzerland. For firms with absolute Swiss-residency requirements, the options are: (a) accept EU-region hosting with the pseudonymization layer as primary control, (b) use an open-weights model (Mistral, Llama) hosted on Swiss infrastructure (Infomaniak, Exoscale) with a voice-calibration penalty and quality trade-off, or (c) wait for Claude on Azure Switzerland when Microsoft and Anthropic bring it to the region.

**What we communicate in sales:**
- Pilot phase: pseudonymization-first + EU-region inference via Frankfurt or Sweden + commercial API + ZDR on request.
- Full deployment: same, with the option to migrate to Swiss-hosted open-weights if the firm's internal policy mandates Swiss-only processing.
- We do not promise "Swiss-hosted Claude" today. It would be technically inaccurate.

### What I commit, what I don't

**I commit:** pilot services agreement, DPA with Swiss FADP addendum (auto-incorporated in Anthropic's Commercial ToS; mirrored in CRI's own processor agreement to the EAM), pseudonymization SOP + advisor template, mutual NDA, Anthropic commercial tier with no training on inputs and 30-day default retention (7-day for API logs), ZDR on enterprise contract.

**I don't commit:** FINMA authorization (not required for an advisory tool used inside the EAM); Swiss-hosted Claude infrastructure (does not exist today); persistent storage of client data on my infrastructure (inputs are processed and discarded); safe-harbour under FINMA for pseudonymization (no such safe harbour is on offer — we position the architecture as a layered control, not a silver bullet).

Clarity on what the product is and is not **pre-empts** the tough compliance questions. The compliance pack is designed to survive a focused DPO review without friction.

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

- Ralph's **eight course corrections** in a row on positioning and substance (no landing site, no CRI experience on LinkedIn, no Skills section, no over-promise in outreach, Part 1 pedagogical clarity triggered by father's feedback, voice-layer reframe beyond quarterly-only, compliance-as-product, three-horizon competitive framing that replaced a fabricated "30-50%" statistic) have consistently outperformed the default BOS recommendations. The operating rule is now explicit: at the first Ralph pushback on a positioning or factual claim, do not defend — investigate and restructure.
- Network-first approach: warm intros + Dubai family + future IE cohort = three acquisition waves in 12 months that most solo founders do not have. Exploit systematically.
- Sourced knowledge base: as of dossier v2.0 (audit 2026-04-22/23), every empirical claim in the canonical artefacts is either directly sourced (regulatory instruments, market stats, Anthropic terms) or explicitly flagged "industry estimate" with reasoning. This is a defensive moat when a compliance officer or a prospect's CFO interrogates a figure.

---

## Part 9. The 30-Day Execution Plan

### Done (April 20-23)

- Direction locked: AI × Swiss wealth, single module, Ralph-first brand architecture.
- Market validated: **1,532 FINMA-approved portfolio managers + trustees (of 1,864 applications, 28 Feb 2025)**, industry-estimated 1,300-1,500 genuine EAMs. AUM: **~CHF 500 bn SAM members / ~CHF 887 bn full IAM sector extrapolation** (previous internal CHF 400 bn figure corrected upward in audit). Whitespace confirmed at the boutique-EAM tier; PMS-vendor AI features (WealthArc, Masttro) exist but are Q&A/data-structuring, not quarterly-letter drafting. Pricing defensible against a Swiss advisor loaded cost of CHF 200-400/hour.
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

## Part 10. Key Numbers (Appendix — sourced)

Every figure in this appendix is sourced in `audit-sources.md`. Where no source exists, the value is flagged "industry estimate" with reasoning.

### Pricing

| Format | Price | Scope |
|---|---|---|
| Pilot 30 days | **CHF 2,400** | 1 advisor, 20 real clients (pseudonymized inputs), quarterly-review use case |
| Full Deployment | **CHF 7,900 setup + CHF 499 / month** | Voice layer calibrated for whole firm, EU-region hosting (Frankfurt or Sweden), all year-round use cases progressively unlocked |
| Dubai pilot (summer 2026) | USD 2,600 | Mirror of Swiss pilot |
| Dubai full deploy | USD 6,900 + USD 499 / month | Mirror of Swiss deployment |

### Conversion benchmarks — sourced to B2B public data, adjusted for Swiss DACH

| Channel | Open → Respond | Respond → Meeting | Meeting → Pilot | Source notes |
|---|---|---|---|---|
| Warm intro (Swiss DACH adjusted) | **28-48%** | **11-20%** (meeting conv. on respondent pool) | **15-25%** | US baseline 40-60% / 15-25% / 15-30% × 0.7-0.8 DACH factor (Fluum, Optifai) |
| Cold LinkedIn (accept → reply) | 18-23% accept × 8-11% reply | 30-40% of replies | 5-15% | Belkins, Alsona benchmarks × DACH factor |
| Cold email financial services | **~2.5-3.4%** (FS industry benchmark, DACH-adjusted) | 30-50% of respondents | 3-10% | RemoteReps FS benchmark; SalesCaptain |

Realistic funnel for 30 qualified messages (warm-led): **~10 responses → 3-5 meetings → 1-2 pilots by end of May**. Funnel math holds only with disciplined cadence: max 2-3 LinkedIn touches per day, 5 emails/day per domain, follow-ups on D+3 / D+7 / D+14 strictly.

### Market sizing — sourced

- **1,532 FINMA-approved** portfolio managers + trustees (of 1,864 applications, at 28 Feb 2025) — FINMA press release 11 Mar 2025. Pure trustees bundled into the count; industry-estimated **1,300-1,500 genuine EAMs**.
- **~CHF 500 bn** AUM — SAM / VSV / ASG members only (2,500+ members) — VSV/ASG official.
- **~CHF 887 bn** AUM — full Swiss IAM sector extrapolation — FIN21 / finews. **Preferred single headline number for pitching Swiss EAM TAM.**
- **~200-300** firms in CRI's target segment (3-30 FTE, French-speaking CH, HNWI book) — derived from industry distribution (>80% of firms ≤10 employees; Geneva + Vaud clusters).
- **AI adoption among Swiss FIs: ~50% in use, +25% planning within 3 years** — FINMA AI Survey April 2025 of ~400 institutions. **Not EAM-specific**; EAMs are in the underweighted "other institutions" slice of the survey.
- **Advisor book size: 50 clients** per "real relationship" is the Kitces benchmark; Swiss EAM partners often carry 30-60 — consistent.
- **Time per quarterly review: 3-4 hours**, derived from Kitces meeting-prep data (5.3 hrs/week prep × 3.8 quarterly meetings/week → ~1.4h prep + 2h meeting). Swiss HNWI clients likely at the upper end of this range. No Swiss-primary industry statistic on this exact figure; flagged as a defensible derivation.
- **Workdays/year recoverable per advisor: 75-100** (50 clients × 3-4h × 4 quarters ÷ 8h/day).
- **Loaded cost per hour for Swiss senior EAM advisor: CHF 200-400/hour** — derived from Glassdoor / PayScale / WealthBriefing EAM compensation data × Swiss employer-loading factor (15-25%) × firm-overhead factor (~50%).
- **CRI pilot ROI — worked case:** 5-advisor firm × 100 workdays/year × 8 h/day × CHF 250/h midpoint = **CHF 1 million / year in recoverable qualified time vs CHF 5,988 subscription/year = ROI ~165×** on quarterly-review use case alone. Adding year-round use cases brings this to the CHF 1.3-1.6 million / year range (ROI 220-270×).

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

# Client Review Intelligence — Compliance & Data Handling One-Pager

**Audience :** EAM compliance officers, CIOs, data protection officers (DPOs).
**Purpose :** answer compliance objections at the first serious call, with sources traceable to primary instruments.
**Version :** 2.0 (2026-04-23, post-audit refactor). Source list : `audit-sources.md`.

---

## 1. The regulatory framework that applies to a Swiss EAM deploying CRI

One important precision up-front. **Article 47 of the Swiss Banking Act (BA) does not apply directly to EAMs** — it binds banks and securities firms. EAMs licensed under the Financial Institutions Act (FinIA, 2020) are subject to a **parallel professional secrecy regime under Art. 69 FinIA**, with penalties broadly similar (custodial up to 3 years or a monetary penalty for intentional unauthorised disclosure). Art. 47 BA reaches the EAM **indirectly**, via flow-down from custodian banks.

The full stack a Swiss EAM compliance officer applies to a vendor like CRI :

| Instrument | What it says | Applies to EAM directly? |
|---|---|---|
| **FinIA Art. 69** — professional secrecy for portfolio managers and trustees | Criminalises intentional unauthorised disclosure of client-identifying data by EAM directors, employees, agents, liquidators. Parallels Art. 47 BA. | **Yes — primary instrument for EAMs.** |
| **FINMA Guidance 08/2024** — Governance and risk management when using AI (published 18 Dec 2024) | Four pillars : governance & AI inventory, data quality, testing / explainability / bias, documentation / independent review. Explicitly extends to third-party AI. | **Yes — addressed to all FINMA-supervised institutions including EAMs.** |
| **Revised FADP (nFADP)** — in force 1 September 2023 | Pseudonymized data remains personal data when re-identification is possible. Cross-border transfer rules. DPIA mandatory for high-risk processing (Art. 22). Criminal sanctions up to CHF 250,000 on individuals for intentional violations. | **Yes — directly.** |
| **Swiss-US Data Privacy Framework (DPF)** — adequacy list addition, 15 September 2024 | Transfers to DPF-certified US recipients covered by adequacy. Non-certified recipients require SCCs or derogation. | **Yes — applies to the Anthropic transfer pathway.** |
| **FINMA Circular 2023/1** — Operational Risks and Resilience, Banks (in force 1 Jan 2024) | Principle-based operational risk regime. Introduces the broader "critical data" concept. Addresses outsourcing, cloud, ICT, BCM. | **Indirectly — applies to banks, reaches EAMs via custodian flow-down.** |
| **SBA Cloud Guidelines, 3rd edition** — published 4 November 2025 | Non-binding SBA recommendations on cloud use by banks. Data classification, risk-based approach, audit rights, exit strategy, new foreign-lawful-access section. **No AI-specific provisions.** | **Indirectly — via custodian flow-down.** |

Sources for every instrument above : primary FINMA / admin.ch / SBA documents plus Lenz & Staehelin, MLL News, PwC Switzerland, DLA Piper commentary. Full URL list in `audit-sources.md`.

---

## 2. Data flow (pilot phase)

```
┌─────────────────────┐     ┌──────────────────────────┐     ┌───────────────────┐
│ Advisor workstation │ →  │   PSEUDONYMIZATION         │ →  │ Anthropic Claude  │
│ (full client data)  │     │   local, by the advisor  │     │ commercial API    │
│                     │     │   BEFORE any paste        │     │ (EU region)       │
└─────────────────────┘     └──────────────────────────┘     └───────────────────┘
          ↑                                                            │
          │                   ┌──────────────────────────┐             │
          └────────────────── │   Re-personalization     │ ←──────────┘
                              │   local, by the advisor  │
                              └──────────────────────────┘
```

**Key principle :** direct client identifiers never leave the advisor's perimeter. Only structured, non-identifying portfolio and market data reach Claude. The pseudonymization mapping file stays on the advisor's workstation. CRI does not receive the mapping keys.

---

## 3. Fields pseudonymized before processing

| Field | Original (illustrative) | Tokenized |
|---|---|---|
| Client name | Dr. Marc Perrin | Client_A |
| Spouse, children | Sylvie, 3 children (28/32/35) | Spouse_A, Child_A_1..3 (age bracket only) |
| Residence | Cologny | Canton of Geneva |
| Portfolio size | CHF 4 250 000 | CHF 4.0–4.5M |
| Custody account ID | IBAN / Account reference | Internal ref only |
| Dates of birth | 1963-05-12 | Age bracket 60-65 |
| Taxpayer identifiers | AHV, Steuer-Nr | **Never transmitted** |

Tokenization is performed by the advisor in their local tooling. CRI provides a CLI (`pseudonymize.py`) and a JSON mapping template. CRI never collects the mapping keys. The advisor owns both the forward and reverse transforms.

---

## 4. Is the pseudonymization approach legally defensible?

**Under nFADP — defensible, with nuance.** Pseudonymized data where the mapping key stays with the controller **remains personal data** under Swiss law (consistent with GDPR Recital 26). The processing therefore remains in nFADP scope. What the architecture achieves is substantial risk mitigation: the recipient (Anthropic) is in a position where practical re-identification is unavailable, bringing it closer to the CJEU's "relative-anonymity-to-the-recipient" approach (SRB v EDPS, 2023). DPIA under Art. 22 nFADP is still required. SCCs or DPF adequacy cover the US transfer.

**Under FinIA Art. 69 / Art. 47 BA (indirect) — defensible, not a safe harbour.** Banking and professional secrecy protect information identifying a specific client. Robust pseudonymization where the mapping key stays inside the EAM perimeter materially mitigates secrecy risk. The 2019 SBA / LLAG legal opinion on cloud recognises that when a cloud provider cannot practically re-identify clients, secrecy exposure is materially reduced — but that is an industry legal opinion, not FINMA doctrine. **No FINMA primary guidance explicitly endorses pseudonymization as a safe harbour.** We do not claim that it is one ; we position it as one layer in a broader governance framework.

The layered defence CRI actually offers :
1. Pseudonymization at source (this document, section 2–3)
2. Swiss-US DPF adequacy or Swiss SCCs as the cross-border transfer mechanism
3. DPIA support (template provided)
4. FINMA Guidance 08/2024 alignment : vendor contract, documentation, risk classification (section 6 below)
5. Anthropic commercial contract with no-training-on-inputs and ZDR available (section 5)
6. Advisor-operated, under the EAM's direct supervision — CRI is a tool, not a data intermediary at scale

---

## 5. Anthropic (the downstream processor) — verified terms

Commercial API tier. Sourced to Anthropic Privacy Center, Trust Portal, and Services Agreement (April 2026, see `audit-sources.md`).

- **Training :** Anthropic Privacy Center verbatim — *"By default, we will not use your inputs or outputs from our commercial products (e.g. Claude for Work, Anthropic API, Claude Gov, etc.) to train our models."* Opt-in required for training use.
- **Retention :** default 30 days at backend for inputs / outputs. **API logs specifically : 7 days since 15 September 2025.** Exceptions : Files API (customer-controlled), enterprise Zero Data Retention contracts, Usage Policy enforcement (up to 2 years for inputs, 7 years for trust-and-safety classifier scores).
- **Zero Data Retention (ZDR) :** available on enterprise contract with security addendum. Under ZDR, customer data is not stored at rest after the API response is returned. **CRI recommends ZDR for every pilot before any real client data is processed.**
- **DPA :** Anthropic's Data Processing Addendum incorporates EU Standard Contractual Clauses (Modules 2 and 3), UK addendum, and **Switzerland addendum**. Auto-incorporated into Commercial Terms of Service — signing ToS = signing DPA. Customer is controller ; Anthropic is processor. Anthropic commits not to sell or share personal data.
- **Encryption :** AES-256 at rest, TLS 1.2+ in transit. MFA and least-privilege access controls.
- **Certifications :** SOC 2 Type I and Type II, ISO 27001:2022, **ISO/IEC 42001:2023** (AI Management Systems — the first dedicated AI-governance standard), HIPAA-ready (BAA on qualifying contracts). Reports obtainable via Trust Portal under NDA.
- **Sub-processors :** primary AWS, plus Google Cloud and Microsoft Azure. Published at `trust.anthropic.com/subprocessors`.
- **Swiss-US DPF certification status :** verify on Anthropic's Trust Center before each pilot contract. If certified, adequacy covers the transfer ; if not, Swiss SCCs apply in the DPA package.

---

## 6. FINMA Guidance 08/2024 — alignment with CRI

| FINMA requirement | CRI's provision |
|---|---|
| Clear accountability and governance for AI use | EAM-side : AI owner designated (usually the senior partner or CIO). CRI-side : Ralph Chidiac is named processor contact. |
| AI inventory with risk classification | CRI is added as an entry. Risk classification template provided. |
| Data quality | Inputs come from the EAM's own PMS / custodian export and pseudonymization layer ; output is advisor-reviewed before sending. |
| Testing, explainability, bias monitoring | Master prompt documented (v1.1 with 3 non-negotiable rules : addressee-scope register, discretion firewall, attribution rigour). Output format fixed and auditable. Manual review step before client delivery. |
| Documentation and independent review | CRI provides SOP, DPA, measurement protocol. Independent review is the EAM's compliance function, with full access to our documentation. |
| Vendor contract : data protection, output accuracy, confidentiality, audit rights | Provided in the Pilot Services Agreement + DPA. |

Result : an EAM compliance officer performing the 08/2024 checklist can close the CRI vendor file in one pass.

---

## 7. Hosting and regions — honest version

Anthropic does not offer a native Switzerland region for Claude today. The EU-resident options available for a Swiss customer are :

- **Google Vertex AI Frankfurt** — direct in-region processing (the cleanest EU residency story today).
- **AWS Bedrock Frankfurt** (eu-central-1, with cross-region inference).
- **Azure AI Sweden Central** — the unique EU region for Claude on Azure.

For firms with strict Swiss-only residency requirements, the options are (a) accept EU-region inference with the pseudonymization layer as the primary control, or (b) use an open-weights model (Mistral, Llama) hosted on Swiss infrastructure (Infomaniak, Exoscale) with a voice-calibration quality trade-off, or (c) wait for Claude on Azure Switzerland to be offered (when Microsoft and Anthropic bring it to the region).

**What CRI commits :** EU-region inference via Frankfurt or Sweden in pilot and full deployment, pseudonymization-at-source, ZDR on enterprise contract, DPF or SCC transfer mechanism. **CRI does not commit "Swiss-hosted Claude" today — it would be technically inaccurate.**

---

## 8. Contractual instruments (pilot phase)

Provided to every pilot :

1. **Pilot Services Agreement** — scope, price, measurement protocol (see `pilot-measurement-protocol.md`), refund trigger.
2. **Data Processing Addendum** — EAM = controller, Ralph Chidiac = processor. Sub-processor list (Anthropic, plus hosting infra for EU region). Mirrors Anthropic's own Swiss FADP-addendum DPA language.
3. **Pseudonymization SOP + CLI tool (`pseudonymize.py`)** — how the advisor tokenizes before processing, how outputs are re-personalized, audit trail template.
4. **DPIA template** — pre-filled covering CRI as AI + financial data + cross-border processor.
5. **Mutual NDA.**
6. **Change-of-control clause** — protections carry forward when CRI structures a legal entity (Sàrl or similar) between pilot and full deployment.

---

## 9. What CRI does NOT claim

- **Not FINMA-authorized.** CRI is an advisory tool used inside the EAM, not a regulated financial service. No authorisation requirement.
- **No Swiss-hosted Claude today.** EU-region inference + pseudonymization is the architecture.
- **No safe harbour under FINMA for pseudonymization.** We present it as a layered control, one piece of a governance stack.
- **No storage of pilot inputs beyond processing.** No database of client portfolios on CRI's side. ZDR available on enterprise contract removes even transient storage.
- **Not a FINMA-supervised institution.** CRI is a processor under the nFADP and a vendor under FINMA Guidance 08/2024 — the EAM remains the regulated entity.

Clarity on what CRI is and is not is the pre-emptive answer to the hard compliance questions.

---

## 10. Contact

Ralph Chidiac — `ralph@ralphchidiac.ch` — +41 [phone]
Compliance questions answered within 24h. Happy to walk through this with your DPO, or their external legal adviser, before signature.

**Document version history :**
- v2.0 (2026-04-23) — audit refactor. Corrected Art. 47 BA / FinIA Art. 69 framing, removed inaccurate "Azure Switzerland with Claude in-region" claim, added sourced Anthropic terms (ZDR, ISO 42001, DPF), added pseudonymization legal defensibility section.
- v1.0 (2026-04-21) — initial version.

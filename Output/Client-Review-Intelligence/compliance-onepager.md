# Client Review Intelligence — Compliance & Data Handling One-Pager

**Audience :** EAM compliance officers, CIOs, data protection officers.
**Purpose :** répondre aux objections compliance au premier call. Alignement sur les exigences FINMA + art. 47 LB + FADP.
**Version :** 1.0 (2026-04-21).

---

## 1. Regulatory context we operate under

- **Swiss Banking Act (art. 47 BA / art. 47 LB)** — banking secrecy. Direct client identifiers cannot be transmitted to foreign cloud processors without explicit legal basis.
- **FINMA Circular 2023/1 — Operational Risks & Resilience** — introduces the "critical data" concept. Cloud AI processing of client data falls under this scope.
- **FINMA Guidance 08/2024 — Governance and risk management in the use of AI** — institutions must understand outsourced AI solutions, manage data protection risks, and impose contractual clauses governing responsibilities.
- **Swiss FADP (Federal Act on Data Protection, revised 2023)** — consent, data minimization, cross-border transfer restrictions.
- **SBA Guidelines on Cloud Computing (3rd ed., Nov 2025)** — applicable framework for cloud-based processing in Swiss banking.

We have read these materials. Our architecture is designed to keep the pilot inside the permissible envelope.

---

## 2. Data flow (pilot phase)

```
┌─────────────────────┐     ┌─────────────────────────┐     ┌──────────────────┐
│ Advisor workstation │ →  │  PSEUDONYMIZATION        │ →  │ Claude API       │
│ (full client data)  │     │  local, by the advisor  │     │ (Anthropic,      │
│                     │     │  BEFORE paste            │     │  commercial tier)│
└─────────────────────┘     └─────────────────────────┘     └──────────────────┘
          ↑                                                          │
          │                  ┌─────────────────────────┐              │
          └──────────────── │  Re-personalization     │ ← ─ ─ ─ ─ ─ ─┘
                             │  local, by the advisor   │
                             └─────────────────────────┘
```

**Key principle :** direct client identifiers never leave the advisor's perimeter. Only structured, non-identifying portfolio and market data reach Claude.

---

## 3. Fields pseudonymized before processing

| Field | Original | Tokenized |
|---|---|---|
| Client name | Dr. Marc Perrin | Client_A |
| Spouse, children | Sylvie, 3 children (28/32/35) | Spouse_A, Child_A_1..3 (age bracket only) |
| Residence | Cologny | Canton of Geneva |
| Portfolio size | CHF 4 250 000 | CHF 4.0–4.5M |
| Custody account ID | IBAN/Account reference | Internal ref only |
| Dates of birth | 1963-05-12 | Age bracket 60-65 |
| Taxpayer IDs | AHV / Steuer-Nr | Never transmitted |

**Tokenization is performed by the advisor in their local tooling.** We provide a template (Excel / Notion / internal script) but do not collect pseudonymization keys.

---

## 4. What Anthropic does (and does not) with inputs

- **Commercial tier (Claude Pro, Team, Enterprise, API) :** Anthropic does NOT use customer inputs or outputs to train models.
- Data retention: inputs retained for abuse monitoring for up to 30 days, then deleted, unless the account is under specific enterprise retention terms.
- Sub-processors: AWS (compute), with DPAs in place.
- Anthropic is not a Swiss-domiciled entity. This is why pseudonymization is the mitigating control for the pilot phase.

**Reference :** Anthropic Commercial Terms + Data Processing Addendum, available on request.

---

## 5. Post-pilot : Swiss-hosted path

For full deployment (`CHF 7 900 setup + CHF 499/month`), we offer migration to a Swiss-hosted LLM infrastructure:

- **Option A :** Azure Switzerland (Claude available via Azure in-region endpoints as of 2025).
- **Option B :** Swiss-hosted open-weights model on Infomaniak / Exoscale (performance trade-off, evaluated case-by-case).

At that point the pseudonymization constraint can be relaxed or dropped, since the processing stays within Swiss territory.

---

## 6. Contractual instruments (pilot phase)

Provided to every pilot:

1. **Pilot Services Agreement** — scope, price, measurement protocol (see `pilot-measurement-protocol.md`), refund trigger.
2. **DPA (Data Processing Addendum)** — roles: EAM = controller, Ralph Chidiac = processor. Sub-processor list (Anthropic, hosting infra).
3. **Pseudonymization SOP** — how the advisor tokenizes before processing, how outputs are re-personalized, audit trail template.
4. **Confidentiality undertaking (NDA)** — mutual.

**Ralph Chidiac is the contracting counterparty in the pilot phase.** Legal entity (Sàrl or equivalent) will be structured before the first full deployment; pilot NDAs include a change-of-control clause to carry the protections forward.

---

## 7. What we do NOT claim

- We are **not** FINMA-authorized — our service is an advisory tool used by the EAM, not a regulated financial service.
- We do **not** host client data on Swiss infrastructure during the pilot — pseudonymization is the mitigating control.
- We do **not** store pilot inputs beyond the run itself — no database of client portfolios on our side.

Clarity on what we are and are not pre-empts the tough questions.

---

## 8. Contact

Ralph Chidiac — ralph@ralphchidiac.ch — +41 [number]
Compliance questions answered within 24h. Happy to walk through this with your DPO before signature.

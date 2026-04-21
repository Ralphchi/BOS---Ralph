# Dataset fictif — Marc Perrin (démo Q1 2026)

**Usage :** Dataset de démo pour tester Client Review Intelligence. Tous les chiffres sont fictifs. Aucune donnée client réelle.

**Deux versions dans ce fichier :**
1. **Version nominale** (ci-dessous) — pour la démo vidéo et les sales calls où aucune donnée client réelle n'est en jeu.
2. **Version pseudonymisée** (en bas du fichier) — pour démontrer le protocole d'utilisation sur des données EAM RÉELLES pendant le pilote.

**Changelog :**
- v1.1 (2026-04-21, après-midi) : voice samples passés en register 1:1 (`Cher Dr. Perrin`) ; gift CHF 300k flaggé `[discreet]` ; ajout section pseudonymisée.
- v1.0 (2026-04-21, matin) : version initiale.

---

## Version nominale (démo)

### Bloc 1/5 — Client Profile

```
<client_profile>
Name: Dr. Marc Perrin
Age: 62, retired orthopedic surgeon
Residence: Cologny, Geneva
Base currency: CHF
Portfolio size: CHF 4 250 000
Addressee scope: single named individual (review is addressed 1:1 to Dr. Perrin, not to the household)
Investment objectives: Capital preservation + modest real growth (+2-3% real/year); liquidity for philanthropy CHF 200k/year; legacy for 3 adult children
Risk tolerance: Moderate-conservative
Target allocation: 60% fixed income & cash, 35% equities, 5% alternatives
Constraints: Swiss tax resident; ESG preferences (no tobacco, no armaments, no thermal coal); existing loyalty to Nestlé and Roche holdings (emotional, not strategic)
Personal notes:
- spouse Sylvie, 3 children (28/32/35), first grandchild due May 2026
- [discreet] considering a CHF 300k gift to eldest daughter for property down-payment this summer — must NOT appear in any circulated material (agenda, printouts). Advisor-only briefing.
</client_profile>
```

### Bloc 2/5 — Portfolio Snapshot

```
<portfolio_snapshot>
Q1 2026 closing snapshot (31.03.2026), base CHF:

FIXED INCOME (58.2%, CHF 2 473 500):
- Swiss Confederation bonds 2031: CHF 850 000 (20.0%)
- European IG corporate bond fund: CHF 620 000 (14.6%)
- US Treasuries 2029 (CHF-hedged): CHF 510 000 (12.0%)
- Swiss corporate bond fund (IG): CHF 493 500 (11.6%)

EQUITIES (34.6%, CHF 1 470 000):
- Nestlé (direct): CHF 310 000 (7.3%)
- Roche (direct): CHF 245 000 (5.8%)
- MSCI World ESG-screened ETF: CHF 410 000 (9.6%)
- Swiss Market Index ESG ETF: CHF 260 000 (6.1%)
- European luxury basket (LVMH, Richemont, Kering): CHF 245 000 (5.8%)

ALTERNATIVES (5.1%, CHF 218 000):
- Gold ETF (CHF-hedged): CHF 138 000 (3.2%)
- Swiss real estate fund: CHF 80 000 (1.9%)

CASH (2.1%, CHF 88 500): CHF current account

Custodian: Banque Pictet
</portfolio_snapshot>
```

### Bloc 3/5 — Quarterly Performance

```
<quarterly_performance>
Quarter: Q1 2026 (01.01.2026 – 31.03.2026)

Performance (net of fees, CHF base):
- Q1 return: +1.8%
- YTD: +1.8%
- Benchmark (60/35/5 custom blend, CHF): +2.1%
- 12-month rolling: +6.4%

Top contributors:
- European luxury basket: +8.2% (Richemont watch demand recovery + LVMH China rebound)
- US Treasuries 2029: +1.4% (Fed rate-cut expectations repriced dovish)
- Swiss Market Index ESG ETF: +3.1% (Nestlé + Roche + Novartis carried the index)

Top detractors:
- Nestlé direct: -2.4% (softer water segment, China pressure). Contribution to portfolio gap: position_weight 7.3% × -2.4% ≈ -17.5 bps.
- Gold ETF: -0.8% (USD weakness vs CHF erased gains). Contribution: 3.2% × -0.8% ≈ -2.6 bps.
- Swiss real estate fund: -1.1% (rate uncertainty weighing). Contribution: 1.9% × -1.1% ≈ -2.1 bps.

Allocation drift: equities now at 34.6% (vs 35% target), fixed income 58.2% (vs 60%), alts and cash slightly above target. Within bands.
</quarterly_performance>
```

### Bloc 4/5 — Market Context

```
<market_context>
Q1 2026 themes relevant to this portfolio:
- SNB held rates at 0.75% in March; inflation expectations anchored at 1.1%. Supportive for Swiss bonds and CHF stability.
- ECB cut 25bp mid-February, signaling more easing later in 2026. Helped European credit and luxury consumer names.
- Fed held but minutes turned dovish; 2-year Treasury yields fell 35bp, boosting bond prices.
- Luxury sector strong rebound after weak 2025: Chinese affluent consumer re-engagement, US resilience. LVMH +11%, Richemont +9%, Kering +3%.
- Nestlé continued underperformance (-2-3%) on Perrier scandal follow-up and softer volumes in emerging markets.
- Gold flat in USD, -1% in CHF terms. No risk-off catalyst strong enough to move it.
- Swiss real estate sector sideways; rate cut expectations being repriced later than hoped.
</market_context>
```

### Bloc 5/5 — Firm Voice Sample

```
<firm_voice_sample>
Sample 1 (previous quarter commentary written by the EAM's advisors, addressed 1:1 to Dr. Perrin):
« Cher Dr. Perrin, le trimestre écoulé s'est inscrit dans une continuité prudente pour votre portefeuille. Nous avons maintenu votre surpondération en obligations souveraines suisses, convaincus que le mouvement de détente monétaire européen demeure votre meilleur allié dans la préservation du capital. Nous restons attentifs au positionnement défensif de votre allocation, et n'apporterons que des ajustements mineurs tant que la visibilité macroéconomique reste celle d'aujourd'hui. »

Sample 2:
« Votre exposition aux valeurs de consommation européenne continue de porter ses fruits, en particulier dans le segment du luxe, où nous identifions une reprise structurelle plutôt que cyclique. Néanmoins, nous vous recommandons de ne pas augmenter cette poche au-delà du niveau actuel — la discipline de l'allocation reste plus créatrice de valeur que les convictions sectorielles isolées. »

Observations: Register 1:1 formel (`Cher Dr. Perrin`, `Votre portefeuille`, `Votre allocation`). Geneva boutique understated. Signature phrases: "continuité prudente", "créateur de valeur", "discipline de l'allocation", "attentifs au positionnement". Hedging verbs: "restons", "n'apporterons que", "vous recommandons de ne pas". Never uses plural when addressing a single named individual. Ouverture toujours `Cher [Titre Nom]`.
</firm_voice_sample>
```

---

## Version pseudonymisée (protocole pilote)

**Usage critique :** pendant le pilote, on tourne l'agent sur les vrais portfolios EAM. Swiss Banking Act (art. 47 BA) + FINMA Circular 2023/1 + FINMA Guidance 08/2024 imposent que les identifiants directs du client ne quittent pas la juridiction suisse. Anthropic (Claude API) étant US-cloud, l'advisor pseudonymise les inputs AVANT de les coller dans l'agent. L'output revient tokenisé, l'advisor re-personnalise localement.

**Champs à tokeniser systématiquement :**
- `Name` → `Client_[token]` (ex. `Client_A`, `Client_042`)
- `Spouse name`, noms des enfants → `Spouse_A`, `Child_A_1`, `Child_A_2`, etc.
- `Residence` (adresse précise) → ville ou canton uniquement
- `Portfolio size` exact → fourchette (ex. `CHF 4.0–4.5M`)
- `Account IDs`, numéros custodiens → références internes anonymes
- Dates de naissance → année ou fourchette d'âge

**Ce qu'on garde :**
- Objectifs d'investissement, risk tolerance, contraintes (ESG, sectorielles), base currency
- Toutes les données de marché et de performance (non-identifiantes par nature)
- Voice samples (le ton, pas l'identité)

### Bloc 1/5 pseudonymisé — exemple

```
<client_profile>
Name: Client_A (internal ref: CLIENT-CH-2026-0001)
Age bracket: 60-65, retired medical professional
Residence: Canton of Geneva
Base currency: CHF
Portfolio size: CHF 4.0-4.5M
Addressee scope: single named individual
Investment objectives: Capital preservation + modest real growth (+2-3% real/year); recurring philanthropic liquidity ~5% of AUM/year; legacy for 3 adult children
Risk tolerance: Moderate-conservative
Target allocation: 60% fixed income & cash, 35% equities, 5% alternatives
Constraints: Swiss tax resident; ESG preferences (no tobacco, no armaments, no thermal coal); sentimental position in 2 large Swiss-cap consumer and pharma names (not to be touched without explicit mandate)
Personal notes:
- Spouse_A, 3 adult children, first grandchild arriving Q2 2026
- [discreet] gift of ~7% of AUM planned summer 2026 to Child_A_1 for property purchase — advisor-only briefing, not to circulate.
</client_profile>
```

Les 4 autres blocs sont déjà anonymes par nature (portfolio composition par asset class, performance, market context, voice samples avec `[CLIENT_TITLE CLIENT_SURNAME]` tokenized).

**Protocole advisor (1 page) :** voir `compliance-onepager.md`.

---

## Profil du client (meta)

- **Persona :** HNWI suisse retraité, Cologny (Genève), conservateur
- **Complexité :** moyenne — 4 asset classes, 13 positions, contraintes ESG, événements personnels (petit-enfant, gift fille aînée flaggé discreet)
- **Objectif démo :** montrer la personnalisation ET le respect de la discrétion (gift CHF 300k ne doit JAMAIS apparaître en Section 5 du review)
- **Durée de run attendue :** ~2 min dans Claude

# Business

**Stade :** Pré-lancement — direction finale validée le 2026-04-21
**Brand stratégie :** Personnelle jour 1, company name punté à plus tard (décision Ralph 21 avril). Ralph vend sous son nom + credentials EPFL/IE. Modèle Hormozi / Yomi Denzel / Gadzhi : le founder AVANT la company.

**Architecture brand :**

| Couche | Nom | Quand activé |
|---|---|---|
| **Brand perso principale** | **Ralph Chidiac** (EPFL + IE Madrid FinTech) | Jour 1 |
| **Duo visible** | **Ralph & [prénom frère] Chidiac** | Dès que frère formalise l'engagement |
| **Personal brand endgame** | *The Chidiac Brothers* (podcast + contenu + communauté) | Mois 6-9 |
| **Product name** | *Client Review Intelligence* (descriptif pour l'instant) | Verrouillé si productisation à 3+ clients |
| **Company légale** | PUNTED | Décidée à 3 clients / 6 mois / clarté produit |

**Domaines et handles réservés (jour 1) :**
- `ralphchidiac.com` + `ralphchidiac.ch` (hub perso, landing, CV/credentials/offre)
- `@ralphchidiac` sur LinkedIn / Instagram / X / YouTube / TikTok
- Réserve pour plus tard : `thechidiacbrothers.com` (quand podcast lance)

## Offre

**Flagship unique : *Client Review Intelligence* — an AI system for Swiss wealth managers, built by Ralph Chidiac (EPFL) and his brother.**

- **Positioning reframe (2026-04-23 soir) :** **compliance is the product, not a constraint.** CRI n'est pas « AI tool for quarterly reviews ». CRI est *« the compliant, audited path to the productivity gain that an estimated 30-50% of Swiss advisors are already grabbing silently with ChatGPT »*. Ce framing change la conversation : on ne vend pas de l'IA à un marché sans IA, on vend la version contrôlée à un marché qui improvise dans l'ombre.
- **Le vrai moat (4 couches indissociables) :** voice-calibration expertise + compliance architecture + measurement rigor + ongoing service. Pas le prompt (copiable). Les 4 ensemble.
- **Positionnement :** « An AI commentary layer that sits on top of your existing PMS. Works with Assetmax, WealthArc, WIZE, Expersoft, or custodian PDFs. **Pilot phase: pseudonymized inputs — no direct client identifiers leave your perimeter.** Full deployment: Swiss-hosted (Azure Switzerland), FINMA 08/2024-aligned governance, tone-trained on your firm's voice. »
- **Compliance posture (révisée 2026-04-21) :** le pilote tourne sur des inputs pseudonymisés côté advisor AVANT envoi à Claude (US cloud). Les identifiants clients ne sortent jamais du périmètre de l'EAM. Migration Swiss-hosted (Azure Switzerland) = feature du full deployment, argument d'upsell naturel. Voir `Output/Client-Review-Intelligence/compliance-onepager.md`.
- **Architecture produit (reframe 2026-04-22 nuit) :** deux couches.
  - **Voice layer** — calibré une fois en week-0 setup (tone, register, signature phrases de la firme). C'est l'asset pérenne et le moat. Il dure toute la vie du contrat.
  - **Use case layer** — templates plugés sur le voice layer. Chaque template = un type de communication écrite client-facing. 30-60 min de setup par nouveau use case, pas de nouvelle calibration.
- **Entry use case (livré dans le pilote et le premier mois du full deployment) :** quarterly client review. L'agent ingère portfolio snapshot + market context + client profile + 2 commentaires passés de la firme, et sort le package 6 sections (executive summary, performance review avec attribution math, market themes, outlook, meeting agenda, advisor-only talking points) dans la voix de la firme. 3-4h → 15 min par review.
- **Year-round use cases débloqués progressivement post-pilote (mois 2+) :**
  1. Ad-hoc market letters (Fed move, géopolitique, etc.)
  2. Proposal drafts pour prospects HNWI
  3. Meeting prep briefs (pre-meeting research + agenda)
  4. Response drafts (email client inquiet, question spécifique)
  5. Post-meeting follow-up letters
  6. Annual reviews (plus élaborés que quarterly)
  7. Event-driven client alerts (drawdown, drift d'allocation)
  8. Monthly firm newsletter
- **ROI démontrable (recalculé avec year-round scope) :**
  - Quarterly reviews : 100 workdays/year/advisor libérés (ROI pilote confirmé)
  - Autres use cases (ad-hoc + meeting prep + follow-ups + proposals) : +60-100 workdays/year/advisor additionnels
  - **Firme 5 advisors : 800-1 000 qualified workdays/year libérés ≈ CHF 1.3-1.6M de temps qualifié vs CHF 5 988 de subscription/an → ROI 220-270×**
- **Modules 2 (Prospect Intelligence standalone) et 3 (Compliance Prep) :** roadmap externe, distincts du voice layer CRI. Upsell post-3-clients signés uniquement.

### Formats

| Format | Prix | Scope |
|---|---|---|
| **Pilot 30 jours** | **CHF 2 400** | 1 advisor, 20 clients test pseudonymisés, quarterly review use case uniquement, crédité à 100% si conversion |
| **Full Deployment** | **CHF 7 900 setup + CHF 499/mois** | Voice layer calibré pour toute la firme + use case #1 (quarterly reviews) + déblocage progressif des 8 use cases year-round (ad-hoc letters, proposals, meeting prep, follow-ups, etc.) au rythme de l'EAM |

**Garantie :** remboursement intégral si économie de temps <50% sur le scope mesuré. Protocole de mesure documenté et annexé au contrat (baseline self-loggué par l'advisor en semaine 0, remeasure en semaine 4). Voir `Output/Client-Review-Intelligence/pilot-measurement-protocol.md`.

**Paiement :** CHF phase 1 (Suisse). USD ajouté pour Dubai phase 2.

## Persona

**Wealth managers indépendants / EAMs FINMA-licensed 3-30 FTE**, Suisse romande (Genève/Lausanne) en priorité.

Contexte :
- 1 532 EAMs licenciés FINMA (post-FinIA 2020), ~CHF 400 mds AUM
- Pain : 4-6h/RM/semaine en commentary + reporting manuel
- Culture achat relationnelle, sales cycle 6-12 mois
- Vénèrent les credentials (EPFL + IE = billet d'entrée)

**Phase 2 (été 2026) :** family offices Dubai (via père pointeur passif).
**Phase 3 (sept 2026+) :** expansion Europe + Madrid via réseau IE.

## Paysage concurrentiel

- **Masttro** (Zurich) : closest adjacent, all-in-one family office stack — pas add-on
- **Unique.ch** (Zurich, 30M$ levés) : vise banques privées, pas EAMs
- **WealthArc / Assetmax / WIZE / Expersoft** : PMS sans AI commentary avancée
- **Apiax / Indigita** : RegTech — on ne les concurrence pas
- **Whitespace confirmé :** « AI commentary layer, PMS-agnostic, tone-trained, Swiss-hosted » inoccupé

## Produit / Service

Done-for-you. Ralph + frère + ami backbone :
1. Audit workflow client + accès sécurisés (NDA + DPA Swiss FADP-compliant)
2. Build prompt + intégration PMS existant / exports custodiens
3. Tone-training sur 3-5 commentaries existants
4. Formation advisors (2h) + documentation
5. Support 4 semaines + maintenance continue

## Marketing

### Phase 1 — Suisse romande (mois 1-6)

**Outreach sortant EN signé Ralph Chidiac :**
- Message type : *« I'm Ralph Chidiac — EPFL engineering (finishing my Bachelor), heading to IE Madrid for a Master in FinTech this September. With my brother, we build AI systems for Swiss wealth managers that save RMs 4-6 hours per week on client review preparation. 30-day pilot at CHF 2 400 on 20 of your real clients — no PMS migration, plugs on your existing setup. Would 15 minutes next week work? »*
- Activation réseau direct Ralph + events VSV/ASG + desks EAM custodiens (Julius Baer, UBP, Sygnum, Maerki Baumann)

**Sales stack phase pilote (pas de site web — décision 2026-04-21 soir) :**
- **LinkedIn profil optimisé** (hub credibilité) : headline + about + Featured section avec vidéo démo embedded + lien Calendly + experience CRI + education. Framework de révision dans `Output/Client-Review-Intelligence/linkedin-optimization-framework.md`.
- **YouTube `@ralphchidiac`** pour héberger la vidéo démo 90s en **unlisted** (visible seulement avec le lien).
- **Calendly `calendly.com/ralphchidiac`** — 15-min Client Review Intelligence Discovery Call. Free tier suffit.
- **PDF leave-behind pack** (2-3 pages A4) envoyé en email post-call aux EAMs intéressés. Source MD dans `Output/Client-Review-Intelligence/leave-behind-pack.md`.
- **Domaines réservés en insurance :** `ralphchidiac.com/.ch` + `chidiacbrothers.com`. Sites vides phase 1 — pas d'overbuild.
- **Ton :** intello-premium, EPFL-backed, pas bombast. Silence observable sur LinkedIn (pas de posts) = signal premium pour marché wealth management suisse.
- **Raison :** Swiss EAM = culture ultra-relationnelle, 3 premiers pilotes viendront des warm intros (réseau direct Ralph + liste père Dubai + futur IE Madrid). Un advisor ne signe jamais parce qu'il a vu une landing page — il signe parce que quelqu'un de confiance a dit ton nom.
- **Phase 2 (post-pilote #1) :** landing page + contenu EN régulier sur LinkedIn/YouTube réévalués selon besoin réel.

### Phase 2 — Dubai (été 2026)
- Pack 1-pager EN + démo vidéo + case study Swiss (si dispo)
- Activation liste noms père
- Rencontres physiques pendant la fenêtre

### Phase 3 — Madrid + Europe (sept 2026+)
- Réseau IE activé (cohort FinTech, founders, VCs, guest lectures)
- Opération remote, EUR ajouté, contenu EN scalé

## Finances

- Revenue actuel : 0 CHF
- Budget initial : 500-1 000 CHF (domaines persos CHF ~40, outils, design)
- Stack outils cible : Claude (agents + tone-training), n8n / Make (workflows), Notion / Linear, Stripe multi-devises, Infomaniak (hébergement .ch), Swiss-hosted LLM ou Azure Switzerland (FINMA 08/2024)

## Équipe

- **Ralph Chidiac** — founder visible, sales, construction IA, caméra
- **[Frère] Chidiac** — co-founder, co-visage, construction IA, contenu (engagement à formaliser semaine du 21 avril)
- **[Ami]** — backbone ops : relation client, delivery, PM (à briefer semaine du 21 avril)

## Vision 18-36 mois

- **Mois 1-6** : *Client Review Intelligence* packagé, 1-2 pilots signés, 1 full deploy, première case study, 2-5k EN followers sur Ralph + frère
- **Mois 6-12** : 3-5 clients Suisse + Dubai, MRR CHF 2-5k/mois, podcast *The Chidiac Brothers* lancé, 10k+ abonnés qualifiés
- **Mois 12-18** : Modules 2 + 3 upsell validés, premier lancement cohort premium *AI Wealth Program* (sous *The Chidiac Brothers*) → 200-350k CHF/USD, company légale fondée avec clarté produit
- **Année 2-3** : Company AI établie avec CA 7 chiffres · *The Chidiac Brothers* = communauté premium internationale, events Lausanne + Madrid + Dubai

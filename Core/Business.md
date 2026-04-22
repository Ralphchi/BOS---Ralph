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
- **Positionnement (v2.0, post-audit 2026-04-23) :** « An AI commentary layer that sits on top of your existing PMS. Works with Assetmax, WealthArc, WIZE, Expersoft, or custodian PDFs. **Pilot phase: pseudonymized inputs — no direct client identifiers leave your perimeter. EU-region inference (Frankfurt or Sweden), Anthropic commercial API with Zero Data Retention available on enterprise contract.** Full deployment: same architecture + voice layer calibrated for the firm + progressive unlock of year-round use cases. FinIA Art. 69-aligned for EAMs ; FINMA Guidance 08/2024 governance checklist complete ; Anthropic DPA with Swiss FADP addendum ; tone-trained on your firm's voice. »
- **Compliance posture (v2.0, post-audit 2026-04-23) :** le régime principal qui s'applique aux EAMs est **FinIA Art. 69** (secret professionnel), pas Art. 47 BA directement (qui couvre les banques). Art. 47 BA reaches EAMs indirectly via flow-down des custodians. Le pilote tourne sur des inputs pseudonymisés AVANT envoi à Claude (EU-region hosting : Frankfurt ou Sweden, pas Swiss). **Anthropic n'offre pas de région Swiss native pour Claude aujourd'hui** — narratif « Swiss-hosted deployment » retiré comme techniquement inexact. Options pour firmes strict Swiss-only : open-weights sur Infomaniak/Exoscale (voice-calibration trade-off), ou attendre Claude on Azure Switzerland. Voir `Output/Client-Review-Intelligence/compliance-onepager.md` v2.0 pour le détail complet sourcé.
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
- **1 532 portfolio managers + trustees** FINMA-approved (de 1 864 demandes, au 28 février 2025 ; source : FINMA press release 11 mars 2025). Industry-estimated **~1 300-1 500 genuine EAMs** (hors pure trustees). AUM : **~CHF 500 mds** (membres SAM/VSV/ASG) ou **~CHF 887 mds** (secteur IAM extrapolation finews/FIN21) — **pas CHF 400 mds** comme précédemment cité (correction audit 2026-04-23)
- Pain : 4-6h/RM/semaine en commentary + reporting manuel
- Culture achat relationnelle, sales cycle 6-12 mois
- Vénèrent les credentials (EPFL + IE = billet d'entrée)

**Phase 2 (été 2026) :** family offices Dubai (via père pointeur passif).
**Phase 3 (sept 2026+) :** expansion Europe + Madrid via réseau IE.

## Paysage concurrentiel — cadrage 3 horizons (refactored 2026-04-23 nuit)

### Horizon 1 — compétition directe aujourd'hui (à déplacer au pilote)

Dans une firme EAM donnée, le quarterly review s'écrit aujourd'hui en 4 modes :
- **Hand-written from scratch** (senior advisors sceptiques IA) — ~55-65% du marché, la vraie majorité
- **Internal improvisation naked ChatGPT** (advisor qui a trouvé le shortcut sans le framework compliance) — ~15-25%, pile où CRI pitche le plus fort
- **Junior analyst / intern** drafting sous supervision senior — ~10-15%
- **Offshore drafting** (Asia) — ~5-10%, compliance nightmare, niche

Le pilote CRI cible surtout les modes 2 et 3 — pain aigu + advisor déjà prêt à utiliser un outil.

### Horizon 2 — menace structurelle 12-24 mois (la vraie bataille)

**PMS vendors ajoutant AI commentary natively :** Assetmax, WealthArc, WIZE, Expersoft. Ils possèdent déjà la donnée cleartext, ajouter un bouton « Generate Q review » est une extension naturelle. Certains y travaillent probablement.

**Moat CRI forward-looking :**
- **PMS-agnostic** — l'EAM déploie CRI indépendamment de son PMS
- **Pseudonymization enforced by design** — tokenization côté advisor workstation AVANT que quoi que ce soit quitte le périmètre. Le PMS vendor a la cleartext in-hand et la refile au LLM — même problème compliance qu'un advisor qui pastes dans ChatGPT
- **Compliance contractuelle directe** — DPA EAM ↔ CRI, pas via le PMS qui a ses propres SLAs opaques

### Horizon 3 — 24+ mois

Consolidation du marché. Survie CRI via : (a) expansion multi-use-case voice agent (en cours avec v1.2), (b) acquisition par un PMS vendor comme leur compliance-grade AI layer (exit option), (c) positioning leader compliance-first AI pour private wealth Swiss (v1.3).

### Acteurs connus à surveiller

- **Masttro** (Zurich) : all-in-one family office stack, closest adjacent — pas add-on, pas menace pilote directe
- **Unique.ch** (Zurich, ~USD 30M levés) : vise banques privées, pas EAMs — marché différent mais preuve que les budgets IA existent
- **WealthArc / Assetmax / WIZE / Expersoft** (PMS) : l'Horizon 2 vrai — à documenter en profondeur dans l'audit
- **Apiax / Indigita** (RegTech) : on ne les concurrence pas, potentiel partenariat
- **Whitespace confirmé (phase 1) :** « AI commentary layer, PMS-agnostic, pseudonymization-first, tone-trained » inoccupé aujourd'hui. Fenêtre = 12-18 mois avant PMS-native catch-up.

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
- Stack outils cible : Claude via EU-region (AWS Bedrock Frankfurt ou Google Vertex Frankfurt) — **pas de Swiss-hosted Claude aujourd'hui**, Azure Switzerland n'offre pas Claude. Open-weights sur Infomaniak/Exoscale comme option pour firmes strict Swiss-residency. Outils annexes : n8n / Make (workflows), Notion / Linear, Stripe multi-devises, Infomaniak (hébergement .ch des sites vitrines personnels).

## Équipe

- **Ralph Chidiac** — founder visible, sales, construction IA, caméra
- **[Frère] Chidiac** — co-founder, co-visage, construction IA, contenu (engagement à formaliser semaine du 21 avril)
- **[Ami]** — backbone ops : relation client, delivery, PM (à briefer semaine du 21 avril)

## Vision 18-36 mois

- **Mois 1-6** : *Client Review Intelligence* packagé, 1-2 pilots signés, 1 full deploy, première case study, 2-5k EN followers sur Ralph + frère
- **Mois 6-12** : 3-5 clients Suisse + Dubai, MRR CHF 2-5k/mois, podcast *The Chidiac Brothers* lancé, 10k+ abonnés qualifiés
- **Mois 12-18** : Modules 2 + 3 upsell validés, premier lancement cohort premium *AI Wealth Program* (sous *The Chidiac Brothers*) → 200-350k CHF/USD, company légale fondée avec clarté produit
- **Année 2-3** : Company AI établie avec CA 7 chiffres · *The Chidiac Brothers* = communauté premium internationale, events Lausanne + Madrid + Dubai

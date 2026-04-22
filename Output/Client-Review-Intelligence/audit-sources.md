# Audit Sources — Client Review Intelligence v2.0

**Date d'audit :** 2026-04-22 / 2026-04-23
**Objectif :** toutes les affirmations dans les artefacts CRI doivent être sourcées ou explicitement flaggées « industry estimate ». Ce fichier liste toutes les sources consultées lors de l'audit web, avec URL et date d'accès. Chaque artefact qui cite une stat ou un claim régulatoire pointe vers ce fichier pour la validation.

---

## 1. Régulations Swiss (banking secrecy, FINMA, nFADP, SBA)

### Art. 47 Banking Act + Art. 69 FinIA (secret bancaire / secret professionnel)

**Finding clé :** Art. 47 BA s'applique aux **banques et securities firms**, PAS directement aux EAMs. Les EAMs post-FinIA (2020) sont soumis à **Art. 69 FinIA** (secret professionnel) — régime parallèle avec pénalités similaires (custodial jusqu'à 3 ans ou amende pécuniaire).

- FINMA licence list (vvtr.pdf) — https://www.finma.ch/en/~/media/finma/dokumente/bewilligungstraeger/pdf/vvtr.pdf (accès 2026-04-22)
- Wikipedia, Federal Act on Banks and Savings Banks — https://en.wikipedia.org/wiki/Federal_Act_on_Banks_and_Savings_Banks (accès 2026-04-22)
- LauxLawyers, Bank Secrecy Laws (Switzerland) — https://www.lauxlawyers.ch/wp-content/uploads/2019/11/Bank-Secrecy-Laws.pdf (accès 2026-04-22)
- CapLaw, Supervision of Portfolio Managers and Trustees — https://caplaw.ch/2019/supervision-of-portfolio-managers-and-trustees-3/ (accès 2026-04-22)
- Global Investigations Review, Switzerland Securities Enforcement — https://globalinvestigationsreview.com/guide/the-guide-international-enforcement-of-the-securities-laws/third-edition/ (accès 2026-04-22)
- Mondaq, Evolution of Swiss Banking Secrecy — https://www.mondaq.com/finance-and-banking/12118/the-evolution-of-swiss-banking-secrecy-and-current-trends-in-enforcement (accès 2026-04-22)
- SBA/LLAG 2019 legal opinion (bank secrecy + cloud) — https://www.swissbanking.ch/_Resources/Persistent/0/e/5/d/0e5da24c4b6b15d1758a408b304bf4d36ced1b17/SBA_Bank_Secrecy_and_Cloud_Legal_Opinion_LLAG_2019_EN.pdf (accès 2026-04-22)

### FINMA Circular 2023/1 (Operational Risks — Banks)

**Finding clé :** S'applique aux **banques et securities firms uniquement**. Entrée en vigueur 1er janvier 2024, pleine conformité attendue 1er janvier 2026. S'étend aux EAMs **indirectement** via flow-down contractuel des banques custodiennes.

- FINMA press release (13 Dec 2022) — https://www.finma.ch/en/news/2022/12/20221213-mm-anh-rs-op-risks/ (accès 2026-04-22)
- MME commentary — https://www.mme.ch/en/magazine/articles/total-revision-of-finma-circular-2023-1-operational-risks-and-resilience-banks (accès 2026-04-22)
- KPMG briefing PDF — https://assets.kpmg.com/content/dam/kpmgsites/ch/pdf/finma-circular-2023.pdf (accès 2026-04-22)
- Grant Thornton commentary — https://www.grantthornton.ch/en/insights/finma-circular-operational-risks-resilience/ (accès 2026-04-22)
- Lexology — https://www.lexology.com/library/detail.aspx?g=dfedc094-8865-46ce-a68c-1aaa44ade496 (accès 2026-04-22)

### FINMA Guidance 08/2024 (AI Governance)

**Finding clé :** Titre exact « FINMA Guidance 08/2024: Governance and risk management when using artificial intelligence ». Publiée **18 décembre 2024**. Applicable à **tous les institutions supervisées FINMA, EAMs inclus**. 4 piliers : governance, data quality, testing/explainability/bias, documentation.

- FINMA press release (18 Dec 2024) — https://www.finma.ch/en/news/2024/12/20241218-mm-finma-am-08-24/ (accès 2026-04-22)
- Lenz & Staehelin commentary — https://www.lenzstaehelin.com/news-and-insights/browse-thought-leadership-insights/insights-detail/finma-issues-guidance-on-ai-use-in-financial-institutions/ (accès 2026-04-22)
- MLL News — https://www.mll-news.com/finma-guidance-08-2024-governance-and-risk-management-when-using-artificial-intelligence/?lang=en (accès 2026-04-22)
- PwC Switzerland — https://www.pwc.ch/en/insights/fs/ai-in-the-financial-industry.html (accès 2026-04-22)

### Revised FADP (nFADP, 2023)

**Finding clé :** Entrée en vigueur **1er septembre 2023**, pas de grace period. Pseudonymized data reste « personal data » si re-identification reste possible. Sanctions pénales jusqu'à CHF 250,000 sur les individus pour violations volontaires.

- admin.ch KMU — https://www.kmu.admin.ch/kmu/en/home/facts-and-trends/digitization/data-protection/new-federal-act-on-data-protection-nfadp.html (accès 2026-04-22)
- DLA Piper data protection Switzerland — https://www.dlapiperdataprotection.com/?t=law&c=CH (accès 2026-04-22)
- FDPIC (edoeb) cross-border transfer — https://www.edoeb.admin.ch/en/cross-border-transfer-of-personal-data (accès 2026-04-22)

### Swiss-US Data Privacy Framework (DPF) — adéquation transferts US

**Finding clé :** **15 septembre 2024** — le Swiss Federal Council a ajouté les US à la liste d'adéquation via le Swiss-US DPF. Transferts aux entreprises US **DPF-certified** = pas de garanties additionnelles requises. Transferts aux entreprises non-certifiées = SCCs, BCRs, ou statutory derogation requis.

- FDPIC cross-border — https://www.edoeb.admin.ch/en/cross-border-transfer-of-personal-data (accès 2026-04-22)

### SBA Cloud Guidelines 3rd Edition

**Finding clé :** Publiée **4 novembre 2025**. Recommendations non-contraignantes adressées aux banques et securities firms. **Pas d'AI-specific provisions** (pour l'AI → FINMA 08/2024).

- Lenz & Staehelin — https://www.lenzstaehelin.com/news-and-insights/browse-thought-leadership-insights/insights-detail/third-edition-of-the-sba-cloud-guidelines/ (accès 2026-04-22)
- SBA PDF — https://www.swissbanking.ch/_Resources/Persistent/c/3/7/8/c378dbe9e1dafa45f4e4f8783cacddf7436cd1e6/Cloud%20Guidelines%20(2025).pdf (accès 2026-04-22)

---

## 2. Marché Swiss EAM

### Nombre d'EAMs FINMA-licensed

**Finding clé :** Au **28 février 2025**, FINMA avait approuvé **1,532 licences sur 1,864 demandes** (portfolio managers + trustees combinés, pas de split public). Industrie estime ~1,300-1,500 **genuine EAMs** (hors pure trustees).

- FINMA press release (11 Mar 2025) — https://www.finma.ch/en/news/2025/03/20250311-mm-abschluss-uvv/ (accès 2026-04-22)
- FINMA liste publique des portfolio managers et trustees — https://www.finma.ch/en/~/media/finma/dokumente/bewilligungstraeger/pdf/vvtr.pdf (accès 2026-04-22)

### AUM du secteur EAM Swiss

**Finding clé :** Deux chiffres défendables, **pas CHF 400bn** comme je citais :
- **CHF 500 bn** — AUM des membres SAM (VSV/ASG) uniquement
- **CHF 887 bn** — extrapolation du secteur IAM complet (études FIN21/finews)

- finews, « 887 Billion Francs: Independent Asset Managers Rival UBS » — https://www.finews.com/news/english-news/71580-independent-asset-managers-switzerland-eam-study-chris-kuenzle-juerg-furrer-aquila-patrick-stauber-marcuard-heritage (accès 2026-04-22)
- SAM — https://www.vsv-asg.ch/en/verband/ueber-uns (accès 2026-04-22)

### Structure du marché par taille

**Finding clé :** **>80% des Swiss IAM firms emploient ≤10 personnes**. AUM : deux-tiers dans CHF 100m-2bn. Deux-tiers des managing directors sont >50 ans (succession risk).

- finews, EAM sector study — https://www.finews.com/news/english-news/71580-... (accès 2026-04-22)
- KPMG Clarity on Swiss Private Banks 2024 — https://assets.kpmg.com/content/dam/kpmgsites/ch/pdf/clarity-on-swiss-private-banks-2024.pdf (accès 2026-04-22)
- KPMG Clarity on Swiss Private Banks 2025 — https://assets.kpmg.com/content/dam/kpmgsites/ch/pdf/KPMG-CH-Swiss-Private-Banks-2025.pdf.coredownload.pdf (accès 2026-04-22)
- KPMG Swiss Asset Management Insights 2025 — https://assets.kpmg.com/content/dam/kpmgsites/ch/pdf/swiss-asset-management-insights-2025.pdf (accès 2026-04-22)
- zeb Swiss Asset Management Study 2025 — https://zeb-consulting.com/en-DE/node/12912 (accès 2026-04-22)

### Supervisory Organisations (5 SOs post-FinIA)

**Finding clé :** FINMA a licensé **5 SOs** supervisant FinIA/FinSA/AMLA compliance :
- **AOOS** (Zurich, fondée par SAM/VSV, 27 Oct 2020, la plus grande)
- **OSIF** (Genève, 6 Jul 2020)
- **SO-FIT** (Genève)
- **OSFIN** (Neuchâtel)
- **FINcontrol Suisse AG** (Bern, 100% VQF-owned)

Pas de split officiel FINMA des parts de marché par SO.

- FINMA SO authorisations — https://www.finma.ch/en/news/2020/07/20200707-mm-ao-bewilligung/ (accès 2026-04-22)
- FINMA liste des SOs — https://www.finma.ch/en/~/media/finma/dokumente/bewilligungstraeger/pdf/ao.pdf (accès 2026-04-22)

### VSV / ASG / SAM (Swiss Association of Wealth Managers)

**Finding clé :** **>2,500 membres**. Représente « plus de la moitié » des ~1,500 wealth et portfolio management firms Swiss. Membres gèrent collectivement **~CHF 500 bn**. Frais annuels : **CHF 5,000 + VAT**. A fondé AOOS comme SO supervision.

- VSV/ASG about — https://www.vsv-asg.ch/en/verband/ueber-uns (accès 2026-04-22)
- VSV/ASG membership — https://www.vsv-asg.ch/en/verband/mitgliedschaft (accès 2026-04-22)

### ASWM (Alliance of Swiss Wealth Managers)

**Finding clé :** Association concurrente VSV, groupe des EAMs plus larges. Prime Partners est membre déclaré.

- asv-aswm.ch

---

## 3. Paysage compétitif PMS + AI vendors Swiss

### Assetmax (Zurich)

**Finding clé :** Multi-custody PM / CRM / invoicing / reporting, on-prem ou cloud. Target : independent asset managers, family offices, banks. **Pricing privé. Pas de feature AI commentary générative publiquement annoncée.**

- SaaSworthy — https://www.saasworthy.com/product/assetmax-ch (accès 2026-04-22)
- AndSimple — https://andsimple.co/companies/assetmax/ (accès 2026-04-22)
- Avaloq ecosystem (Assetmax partner) — https://www.avaloq.com/platform/ecosystem/assetmax (accès 2026-04-22)

### WealthArc

**Finding clé :** « Global data infrastructure for AI-ready portfolio data ». **140+ custodian bank feeds**. En 2025 a lancé : **AI Agent** qui convertit documents financiers en données structurées ; **« Chat with your Data »** (Q&A). **Pas encore un générateur de quarterly review letter** en public.

- WealthArc expands custodian + AI agents — https://itbrief.co.uk/story/wealtharc-expands-custodian-network-builds-ai-agents (accès 2026-04-22)
- WealthArc launches AI Agent — https://cfotech.co.uk/story/wealtharc-launches-ai-agent-to-structure-portfolio-data (accès 2026-04-22)
- Financial IT coverage — https://financialit.net/news/financial/wealtharc-now-connects-over-140-custodian-banks-worldwide-ai-agents-launched-to-automate-advisor-workflows-leverage-chat-with-your-data (accès 2026-04-22)

### WIZE by TeamWork

**Finding clé :** **100+ clients, ~3,000 users in 23 countries, 200+ custodian feeds**. Partnership avec Bank Syz pour EAM distribution. **Pas de feature AI publique trouvée.**

- WIZE — https://www.wize.net/en (accès 2026-04-22)
- Bank Syz + WIZE partnership — https://www.syzgroup.com/en/news/bank-syz-and-wize-teamwork-... (accès 2026-04-22)

### Expersoft

**Finding clé :** Plateforme **PM1**. Utilisé par des privates banks + EAMs. Hosted in Switzerland or Oracle Cloud. **Pas de feature AI commentary publique.**

- Expersoft — https://www.expersoft.com (accès 2026-04-22)
- Expersoft IAM page — https://www.expersoft.com/independent-wealth-asset-manager (accès 2026-04-22)

### Masttro (HQ NYC, offices Zurich + Monterrey)

**Finding clé :** Primarily family offices. **10,000+ users, 35 countries, 650+ custodian feeds**. **Marketing AI le plus aggressive du peer set** : « Masttro Intelligence » (Q&A natural language sur portfolio data), agentic AI pour capital calls / distributions. Messaging « data never leaves Masttro platform » (isolated deployment). **Pas un « draft the review letter » product.** Closest adjacent narrative-wise, mais target FO pas boutique EAM 5-30 FTE.

- Masttro AI for family offices — https://masttro.com/insights/ai-for-family-offices (accès 2026-04-22)
- Masttro agentic AI — https://masttro.com/insights/agentic-ai-family-offices (accès 2026-04-22)

### Unique.ai (Zurich)

**Finding clé :** **Series A USD 30M** annoncée **27 février 2025**, lead **CommerzVentures + DN Capital**, with **VI Partners + Pictet Group**. Total raised since 2021 = **USD 53M**. Customers : **Pictet, UBP, SIX, LGT, Partners Group**. **30,000 financial professionals users**. **Target : private banks, pas EAMs.**

- Unique.ai Series A press — https://www.unique.ai/en/blog/unique-secures-usd-30-million-series-a-to-pioneer-agentic-ai-workforce-in-financial-services-2 (accès 2026-04-22)
- FintechNews.ch — https://fintechnews.ch/aifintech/switzerlands-unique-raises-30m-series-a-to-advance-financial-ai-solutions/74883/ (accès 2026-04-22)
- AI Insider coverage — https://theaiinsider.tech/2025/02/28/unique-secures-30m-in-series-a-funding-to-accelerate-ai-innovation-in-financial-services/ (accès 2026-04-22)

### Apiax, Indigita (RegTech — non-competitors)

- Apiax — https://www.apiax.com (accès 2026-04-22)
- Indigita — https://www.indigita.ch/company/ (accès 2026-04-22)

---

## 4. Anthropic terms (Claude API commercial tier)

### Training sur inputs (default)

**Finding clé :** **« By default, we will not use your inputs or outputs from our commercial products (e.g. Claude for Work, Anthropic API, Claude Gov, etc.) to train our models »** (verbatim). Différence critique vs consumer tier où l'opt-out est requis depuis Sept 2025.

- Anthropic — is my data used for model training — https://privacy.claude.com/en/articles/7996868-is-my-data-used-for-model-training (accès 2026-04-22)

### Rétention

**Finding clé :** **30 jours par défaut** pour inputs/outputs backend. **7 jours pour API logs** depuis 15 septembre 2025 (reporting tiers). Exceptions pour (a) services avec longer retention (Files API), (b) ZDR contractuel, (c) Usage Policy enforcement (jusqu'à 2 ans inputs, 7 ans trust & safety scores).

- Anthropic retention — https://privacy.claude.com/en/articles/7996866-how-long-do-you-store-my-organization-s-data (accès 2026-04-22)

### Zero Data Retention (ZDR)

**Finding clé :** Disponible pour qualifying enterprise API customers sous contrat signé. Sous ZDR : **« customer data is not stored at rest after the API response is returned »**. Applique uniquement à Enterprise/Team API keys. **Pour un Swiss EAM avec client data, ZDR est la version à demander.**

- Anthropic ZDR scope — https://privacy.claude.com/en/articles/8956058-i-have-a-zero-data-retention-agreement-with-anthropic-what-products-does-it-apply-to (accès 2026-04-22)

### DPA (avec Swiss FADP addendum)

**Finding clé :** DPA Anthropic inclut **EU Standard Contractual Clauses (Modules 2 & 3) + UK + Switzerland addenda**. **Auto-incorporé dans Commercial ToS** — signer ToS = signer DPA. Customer = data controller, Anthropic = processor. Encryption AES-256 at rest, TLS 1.2+ in transit.

- Anthropic DPA viewing/signing — https://privacy.claude.com/en/articles/7996862-how-do-i-view-and-sign-your-data-processing-addendum-dpa (accès 2026-04-22)
- Anthropic DPA PDF (Sep 2023 version) — https://assets-global.website-files.com/6548404a216c2e42eb79648b/65680354f8f4425cc8a8110c_Toothless-Anthropic_DPA_Sep-22-2023.pdf (accès 2026-04-22)

### Certifications

**Finding clé :** **SOC 2 Type I & II, ISO 27001:2022, ISO/IEC 42001:2023 (AI Management Systems), HIPAA-ready (BAA available)**. Reports via Trust Portal sous NDA.

- Anthropic certifications — https://privacy.claude.com/en/articles/10015870-what-certifications-has-anthropic-obtained (accès 2026-04-22)
- Anthropic Trust Portal — https://trust.anthropic.com (accès 2026-04-22)

### Régions disponibles pour Swiss customers

**Finding clé important :** **Pas de région Swiss native pour Claude.** Options GDPR-friendly pour Swiss customers :
- AWS Bedrock Frankfurt (eu-central-1, cross-region inference)
- Google Vertex AI Frankfurt (direct in-region processing) — **cleanest residency story today**
- Azure AI Sweden Central (unique EU region de Claude sur Azure)

**Implication CRI :** notre narratif « Swiss-hosted (Azure Switzerland) post-pilot » était imprécis. Il n'existe pas de Claude on Azure Switzerland aujourd'hui. À reformuler : « EU-region hosting (Frankfurt ou Sweden) pour full deployment, avec pseudonymization layer enforced. Open-weights Swiss-hosted option disponible sur demande (Mistral/Llama sur Infomaniak/Exoscale). »

- Gerloff, Claude regions comparison — https://www.gerloff.dev/writing/claude-aws-azure-google-gdpr (accès 2026-04-22)

### Sub-processors

**Finding clé :** AWS = primary cloud provider (Apr 2026 : expanded deal up to USD 25B entre Amazon et Anthropic). Google Cloud + Microsoft Azure aussi utilisés. Liste publique sur trust.anthropic.com/subprocessors.

- CNBC AWS-Anthropic deal (Apr 2026) — https://www.cnbc.com/2026/04/20/amazon-invest-up-to-25-billion-in-anthropic-part-of-ai-infrastructure.html (accès 2026-04-22)
- Anthropic sub-processors — https://trust.anthropic.com/subprocessors (accès 2026-04-22)

### Liability

**Finding clé :** Limited à fees paid in 12 months preceding claim, with IP indemnity carve-outs. Enterprise peut négocier stronger terms.

- Anthropic Services Agreement — https://aiby.mobi/chat_ios/anthropic/ai-services-agreement.pdf (accès 2026-04-22)

---

## 5. AI adoption Swiss financial services

### FINMA 2025 AI Survey

**Finding clé :** Survey de **~400 licensed institutions**, conduite end-Nov 2024 to mid-Jan 2025. **~50% already use AI or initial applications in development**, +25% plan within 3 years. **91% of AI-using institutions also use GenAI. ~50% have explicit AI strategy.** Distribution : 100 banks/securities firms, 75 insurers, 12 fund managers — **les EAMs sont dans le petit bucket « other institutions »**, stat pas EAM-specific.

- FINMA AI Survey press release (24 Apr 2025) — https://www.finma.ch/en/news/2025/04/20250424-mm-umfrage-ki/ (accès 2026-04-22)
- Charltons Quantum summary — https://charltonsquantum.com/finma-ai-survey-2025/ (accès 2026-04-22)
- FinanceMagnates — https://www.financemagnates.com/forex/50-of-swiss-financial-firms-use-ai-finma-survey-of-400-institutions-shows/ (accès 2026-04-22)

### KPMG / Deloitte context

- KPMG Swiss Asset Management Insights 2025 — https://assets.kpmg.com/content/dam/kpmgsites/ch/pdf/swiss-asset-management-insights-2025.pdf (accès 2026-04-22)
- Deloitte on Swiss EAM consolidation — https://blogs.deloitte.ch/banking/2022/06/accelerating-consolidation-dynamic-among-swiss-external-asset-managers-amid-regulatory-and-profitabi.html (accès 2026-04-22)

### McKinsey global wealth / AI

- McKinsey US Wealth Management 2035 — https://www.mckinsey.com/industries/financial-services/our-insights/us-wealth-management-in-2035-a-transformative-decade-begins (accès 2026-04-22)

---

## 6. Swiss advisor / RM compensation benchmarks

**Finding clé :**
- Wealth Management Switzerland avg : **CHF 105,000/year** (P25-P75 : CHF 87,500-135,000)
- Geneva WM avg : CHF 125,000 ; Zurich avg : CHF 98,000
- Senior Wealth Manager Geneva : **CHF 300,000-500,000** (avg CHF 385,000)
- Relationship Manager Swiss : CHF 105,000 avg, P75 CHF 160,000
- EAM RM : souvent revenue-share >80% gross. Senior book-carrying : **CHF 200,000-400,000 total comp**
- Swiss employer loading : **+15-25% sur brut** (AHV/IV/ALV, BVG, UVG, family allowances, admin)

**Derived loaded hourly cost (défendable) :**
- Mid-career EAM RM : CHF 216k fully loaded / 1,800 productive hours = **CHF 120/hr**. Avec overhead firm +50% = **CHF 180/hr**.
- Senior EAM RM / Partner : CHF 420k / 1,800h = **CHF 233/hr**. Avec overhead = **CHF 350/hr**.
- **Range CRI défendable : CHF 200-400/hr loaded pour senior Swiss EAM advisor.**

**Pilot savings math :** 100 workdays/yr × 8h/jr = 800h. × CHF 250/hr midpoint = **CHF 200,000/yr de valeur par advisor**. À CHF 2,400 pilot = **ROI ~65-85×**.

- Glassdoor WM Switzerland — https://www.glassdoor.com/Salaries/switzerland-wealth-management-salary-SRCH_IL.0,11_IN226_KO12,29.htm (accès 2026-04-22)
- Glassdoor Geneva senior WM — https://www.glassdoor.com/Salaries/geneva-switzerland-wealth-manager-salary-SRCH_IL.0,18_IM1141_KO19,33.htm (accès 2026-04-22)
- PayScale Swiss WM — https://www.payscale.com/research/CH/Industry=Wealth_Management/Salary (accès 2026-04-22)
- WealthBriefing EAM RM comp — https://www.wealthbriefing.com/html/article.php/Compensation-Models-For-Wealth-Manager-RMs:-A-Look-At-Switzerland's-EAMs (accès 2026-04-22)
- Deel Swiss employer cost — https://www.deel.com/blog/employer-costs-for-an-employee-in-switzerland/ (accès 2026-04-22)

---

## 7. B2B outreach conversion benchmarks

**Finding clé :**
- Cold email financial services : **~3.39% response rate** (B2B general : 3-5.1% avg, >5% « good », top quartile 10%+, elite 15-25%)
- Follow-ups (2-3 more, start day 3) : +65.8% reply rate
- Cold LinkedIn connect acceptance : **26-29% baseline**, 30-40%+ avec personalisation/2nd degree. Personalised msg reply rate 9.36% vs 5.44% sans
- Post-connection reply rate : ~11% (7-15%)
- Warm intros : **40-60% response**, **15-25% convert to meeting** (vs 1.5-2% cold)
- **Swiss/DACH adjustment : 0.7-0.8× US numbers** (stricter data protection culture)
- Sales cycle B2B avg 60-120 jours ; Swiss wealth vendor 6-12 mois (industry estimate)

- SalesCaptain cold email stats — https://www.salescaptain.io/blog/cold-email-statistics (accès 2026-04-22)
- RemoteReps B2B cold email benchmarks by industry — https://remotereps247.com/b2b-cold-email-benchmarks-2025-response-rates-by-industry/ (accès 2026-04-22)
- Digital Bloom reply-rate — https://thedigitalbloom.com/learn/cold-outbound-reply-rate-benchmarks/ (accès 2026-04-22)
- Belkins LinkedIn outreach study — https://belkins.io/blog/linkedin-outreach-study (accès 2026-04-22)
- Alsona LinkedIn acceptance benchmarks — https://www.alsona.com/blog/linkedin-connection-request-benchmarks-healthy-acceptance-rate-in-2025 (accès 2026-04-22)
- Fluum warm-intro guide — https://fluum.ai/journal/the-complete-guide-to-b2b-warm-introductions-in-2026 (accès 2026-04-22)
- Optifai cold-to-meeting — https://optif.ai/learn/questions/cold-call-to-meeting-conversion-rate/ (accès 2026-04-22)
- Focus Digital B2B sales cycle by industry — https://focus-digital.co/average-sales-cycle-length-by-industry/ (accès 2026-04-22)

---

## 8. Advisor workflow benchmarks (Kitces Research)

**Finding clé :**
- Advisor spends **5.3 hrs/wk meeting preparation**, 8.8 hrs in meetings (Kitces)
- Si 50 clients × quarterly → ~3.8 meetings/wk → **~1.4h prep + 2h meeting = ~3.4h per quarterly touchpoint** → **« 3-4 hours per quarterly review » VALIDATED** pour US context, défendable pour Swiss (probably upper-end for HNWI)
- **« 50-client book per advisor » VALIDATED** : Kitces `« 50 great clients »` model, 50-100 upper bound par RM pour relationships
- « 4-6 hrs/wk commentary+reporting » : Kitces donne 5.3h prep + 5.5h investment mgmt + 4.2h admin = 15h envelope. **Isolating commentary ~4-6h/wk défendable mais pas source directe Swiss-specific.**

- Kitces — How advisors spend time — https://www.kitces.com/blog/how-do-financial-advisors-spend-time-research-study-productivity-capacity-efficiency/ (accès 2026-04-22)
- Kitces — 50 great clients — https://www.kitces.com/blog/50-great-clients-how-many-clients-does-a-financial-advisor-need/ (accès 2026-04-22)

---

## 9. Validation EAMs cibles spécifiques (pipeline hygiene)

**Corrections requises dans `eam-pipeline.md` v1.1 :**

| Firme | Problème identifié | Correction |
|---|---|---|
| **Fairway Asset Management** | Listée comme Lausanne — **en réalité Zurich** | Fix location |
| **Lakefield Partners** | Listée comme Geneva — **en réalité Zurich** | Fix location |
| **Heritage Financial Services (Geneva)** | Nom introuvable tel quel. Probablement Banque Heritage (une banque, pas un EAM) ou 47Heritage | Re-verify legal name |
| **Geneva Management Group** | Au moins une entité GMG en liquidation (finews : « a returned its license »). Autre entité sister active. | Confirm quelle entité cible |

**Firmes validées FINMA-licensed :**
- MFM Mirante Fund Management (Lausanne) — https://mirante.ch/en/asset-management/about-us/
- The Forum Finance Group SA (Geneva) — ~25 employees, ~CHF 2 bn AUM — https://www.ffgg.com/en/about-us-global-wealth-management-geneva/
- 1875 Finance (Geneva + Zurich + Luxembourg + HK) — >CHF 13 bn AUM — https://1875.ch/company/affiliations/
- Pleion SA / Probus Pleion (Geneva + Bern + Nyon + Sion + Verbier + Zurich) — >USD 5 bn AUM — https://www.probuspleion.ch/en/
- Elypse Partners SA (Lausanne) — https://www.elypse-partners.com/en/about/
- TBH Global Family Office SA (Geneva) — https://tbh-gfo.com/
- Vector Gestion (Nyon HQ + Lausanne + Morges + Geneva) — ~30 professionals — https://vectorgestion.ch/en/
- EMC Gestion de Fortune SA (Geneva) — founded 1982 — https://emcge.com/en/gerants-de-fortune
- Prime Partners SA (Geneva) — FINMA since May 2022, ASWM member, >CHF 3.5 bn AUM — https://www.prime-partners.com/en/home-page/
- Diamond Capital Management Switzerland (Geneva) — ASG/VSV member — https://www.diamondcapital.ch

---

## 10. Caveats et données non-trouvées publiquement

Les claims suivants **n'ont pas été trouvés en source publique** et doivent être marqués « industry estimate » ou retirés :

- Canton-breakdown des EAMs FINMA-licensed (FINMA ne publie pas la table directement)
- Roadmap interne AI des PMS vendors au-delà du marketing public
- Parts de marché par Supervisory Organisation (vendor-declared seulement)
- Pricing exact des PMS vendors (tous privés)
- « 30-50% of advisors using ChatGPT silently » — **claim retiré v1.4** comme invérifiable
- FINMA enforcement cases sous Art. 47 BA derniers 5 ans — aucun cas public trouvé
- FINMA primary guidance explicite sur pseudonymization as safe harbour sous Art. 47 BA — **pas de statement FINMA direct**. Le positioning est défendable via nFADP + FinIA art. 69, pas un safe harbour explicite.

---

**Version de l'audit :** 1.0 (2026-04-23)
**Maintenance :** ce fichier est re-accessé à chaque update d'artefact canonique. Chaque claim dans un artefact doit soit pointer ici, soit être flaggé « industry estimate » explicitement.

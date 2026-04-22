# Script vidéo démo — 90s (v1.2 solo)

**Objectif :** un asset sales à intégrer dans chaque email/DM outreach. Un email EN avec démo = 3× taux de réponse vs sans.

**Format :** screen recording + webcam simple (Ralph solo, centered)
**Durée cible :** 60-90 secondes
**Langue :** EN (brand phase 1 = 100% EN)
**Tournage :** 2 prises maximum, pas de sur-production

**Changelog :**
- **v1.2 (2026-04-22, PM)** : reformulation solo (frère sur autre projet). Simplification : plus de picture-in-picture duo, structure face cam → screen → face cam. Remplacement systématique `we / my brother` → `I / my`. Zéro mention duo retirée côté credentials (toujours EPFL + IE comme angle unique).
- v1.1 (2026-04-21) : math corrigée (100 workdays/an) + CTA compliance.
- v1.0 (2026-04-21) : version initiale.

---

## Setup technique simplifié (solo)

- **Screen recording Mac** (QuickTime gratuit ou Loom si sous-titres auto)
- **Webcam** : Ralph centré, cadrage épaules (pas visage-seul), fond neutre (mur blanc ou plante discrète)
- **Lumière** : face à la fenêtre entre 10h et 15h — pas de lampe de bureau qui écrase
- **Audio** : AirPods ou micro lavalier — pas le micro intégré du Mac
- **Tenue** : chemise sobre ou pull col rond sombre, pas de t-shirt, pas de logo visible
- **Enregistrement séparé :** face cam et screen recording dans 2 fichiers distincts puis montés ensemble (DaVinci Resolve ou CapCut, 30 min max de montage)

**Pourquoi c'est plus simple en solo :** plus de picture-in-picture à caler, plus de coordination jumeau. Juste 3 prises face cam (hook, pain, CTA) + 1 prise screen recording. Si une prise rate, tu refais juste elle.

---

## Script (90s)

### [0:00–0:10] Hook — face cam

> « Hi, I'm Ralph Chidiac. EPFL engineering, moving to IE Madrid for a Master in FinTech this September. I've built an AI system for Swiss wealth managers. Let me show you in 90 seconds. »

**Note de jeu :** direct, calme, pas souriant-commercial. Swiss register = understated. Une respiration entre les phrases.

---

### [0:10–0:25] Le pain — face cam, ton posé

> « A Swiss EAM advisor spends three to four hours preparing each quarterly client review. For a fifty-client book, that's about one hundred workdays a year lost to manual commentary — five months of full-time work. »

**Note de jeu :** regarde la caméra sur « one hundred workdays a year ». Chiffre qui doit rester une seconde en l'air.

---

### [0:25–1:15] Demo — screen recording + voiceover (tu ne parles pas face cam ici)

**À l'écran :** Claude Project ouvert. Le dataset Perrin (pseudonymisé) apparaît collé. L'output se génère en direct, scroll lent.

**Voiceover (par-dessus le screen recording) :**

> « Here it's running on a fictional four-million Swiss franc client portfolio. It ingests a pseudonymized portfolio snapshot, the quarter's news context, and two commentary samples to learn the firm's tone. »

*[Pause 2-3 secondes pendant que l'output commence à se générer]*

> « In under two minutes, the advisor gets an executive summary, a performance review with proper attribution math, market themes tied to the client's actual holdings, an outlook section, a meeting agenda — and, critically, advisor-only talking points the client never sees. Everything in the firm's own voice. »

**Note tournage :** pour le screen recording, pré-charger le dataset dans le Claude Project AVANT d'enregistrer. Lancer la run au début du screen recording. Tu as ~60s d'output en live pour remplir 50s de voiceover — large.

---

### [1:15–1:30] CTA — retour face cam

> « I'm running a thirty-day pilot at two thousand four hundred Swiss francs with three EAMs this quarter. Inputs are pseudonymized before processing — no client identifiers leave your perimeter. Time savings are measured against a baseline you log in week one, remeasured in week four. If they don't hit fifty percent, full refund. Link below for a fifteen-minute call. Thanks. »

**Note de jeu :** regarde la caméra sur « full refund ». C'est le mot qui vend le pilote.

---

## Deux règles de jeu importantes

1. **Pas de « we » ou « my team ».** Tu es seul phase 1 — assume-le. « I've built », « I'm running ». Plus honnête, plus cohérent avec le solo register Hormozi/Yomi/Gadzhi. Si un EAM demande « vous êtes combien ? » en call, tu réponds « I'm leading this myself, with a delivery partner on ops. That's why I'm only onboarding three EAMs this quarter. » C'est une FORCE (scarcity + boutique register), pas un manque.

2. **Pas de sourire commercial.** Swiss EAM register = sobre, factuel. Pense private banker, pas founder LinkedIn. Sourcils détendus, pas de « Hi guys! », pas de « So today we're gonna talk about… ». Juste « Voici ce que j'ai construit, voici ce que ça coûte, voici la garantie ». Fin.

---

## Checklist avant tournage

- [ ] Master prompt **v1.1** chargé dans le Claude Project (pas la v1.0)
- [ ] Dataset **Perrin révisé** dans le Project (`[discreet]` sur gift, register 1:1)
- [ ] Run test réalisé pour vérifier que l'output génère proprement en live (ouverture `Cher Dr. Perrin`, gift en Section 6 only)
- [ ] Screen recording test — le Claude Project génère bien en 50-60s
- [ ] Lumière naturelle OK (entre 10h et 15h)
- [ ] Calendly prêt avec 15-min slot « Client Review Intelligence — Discovery Call »
- [ ] Compliance one-pager PDF prêt à envoyer en follow-up
- [ ] Pilot measurement protocol prêt en annexe contractuelle

---

## Post-production

- Trim intro/outro (pas de « alors voilà », pas de hésitations)
- Sous-titres EN burn-in (40% des wealth managers regardent sans son sur mobile/LinkedIn)
- Transition discrète face cam → screen recording (cross-fade 0.3s, pas de wipe spectacle)
- Watermark `ralphchidiac.com` bottom-right petit et discret à partir du screen recording
- Export : 1080p, MP4, <50 MB
- **Upload YouTube `@ralphchidiac` en `Unlisted`** — pas Public. Le lien est partagé manuellement dans chaque DM/email, tu gardes le contrôle.

---

## Vérification math (référence)

- 3h × 50 clients = 150h/quarter (bas de la fourchette)
- 4h × 50 clients = 200h/quarter (haut)
- 150–200h ÷ 8h/jour = 18.75–25 workdays/quarter
- × 4 quarters = 75–100 workdays/an
- Arrondi vidéo : « about one hundred workdays a year »
- Image parlante : « five months of full-time work » (100 ÷ 20 workdays/mois)

---

## Deadline révisée

- **2026-04-23 soir** — final prep : run test Claude Project validé (Cher Dr. Perrin + gift Section 6 only), script relu à voix haute 3 fois.
- **2026-04-24 ou 2026-04-25** — enregistrement solo (face cam + screen recording). Plus besoin de synchroniser avec le frère → tu peux tourner samedi matin tranquille.
- **2026-04-26 soir** — version finale exportée (YouTube Unlisted) + lien prêt pour le premier batch outreach du 28/04.

---

## Deux prises de face cam à tourner séparément

**Prise 1 (hook + pain) :** 0:00-0:25. Tu enregistres d'une traite les 25 premières secondes face cam. Si tu te trompes, tu recommences.

**Prise 2 (CTA) :** 0:15s seulement. Plus facile, tu peux la refaire 5 fois pour avoir la bonne.

**Prise 3 (screen recording avec voiceover) :** tu peux enregistrer le voiceover séparément après, en regardant le screen recording. Ça te permet de doubler la voix plus posée sans être stressé par le timing du Claude Project.

Cette décomposition = 3 mini-tâches faciles au lieu d'une grosse tâche stressante. Si une prise rate, tu refais juste elle.

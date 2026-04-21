# Script vidéo démo — 90s (v1.1 post-hardening)

**Objectif :** un asset sales à intégrer dans chaque email/DM outreach. Un email EN avec démo = 3× taux de réponse vs sans.

**Format :** screen recording + webcam picture-in-picture (Ralph + frère, bottom-right)
**Durée cible :** 60-90 secondes
**Langue :** EN (brand phase 1 = 100% EN)
**Tournage :** 2 prises maximum, pas de sur-production

**Changelog :**
- v1.1 (2026-04-21, après-midi) : math corrigée (100 workdays/an vs « almost 30 » erroné v1.0) ; CTA révisé avec compliance framing (pseudonymized inputs) + protocole de mesure du refund.
- v1.0 (2026-04-21, matin) : version initiale.

---

## Setup technique

- Screen recording Mac (QuickTime ou Loom)
- Webcam : Ralph au centre, frère à côté ou derrière
- Lumière naturelle (face à la fenêtre)
- Fond : neutre et propre, pas de bibliothèque cliché
- Audio : AirPods ou micro externe (pas le micro intégré)

---

## Script (90s)

### [0:00–0:08] Hook

**À l'écran :** Ralph + frère en face caméra

> « Hi, I'm Ralph Chidiac. I'm an EPFL engineering student and with my brother, we build AI for Swiss wealth managers. In 90 seconds, here's what we've built. »

---

### [0:08–0:22] Le pain (math corrigée)

**À l'écran :** toujours face caméra

> « A Swiss EAM advisor spends 3 to 4 hours preparing each quarterly client review. For a 50-client book, that's 150 to 200 hours every quarter — up to 25 full workdays per quarter, 100 workdays a year. That's five months of one advisor's full-time work, every year, lost to manual commentary. »

---

### [0:22–1:05] Demo (screen recording prend le dessus)

**À l'écran :** Claude Project avec le master prompt + le dataset Perrin qui apparaît.

> « Here's our system running on a fictional 4-million Swiss franc client portfolio. It ingests a pseudonymized portfolio snapshot, the quarter's news context, and two commentary samples to learn the firm's tone. »

*[Pause pendant que l'output se génère à l'écran — scroll lentement]*

> « In under two minutes, the advisor gets an executive summary, a detailed performance review with proper attribution math, market themes tied to the client's actual holdings, the outlook section, a meeting agenda — and, critically, advisor-only talking points the client never sees. Everything in the firm's own voice, in the register the firm uses. »

---

### [1:05–1:30] CTA (compliance + measured refund)

**À l'écran :** retour face caméra, Ralph parle

> « We're running a 30-day pilot at CHF 2,400 with 3 Swiss EAMs in Q2. Inputs are pseudonymized before processing — no client identifiers leave your perimeter. Time savings are measured against a baseline you log in week one, remeasured in week four. If they don't hit 50%, full refund. If you're curious, 15 minutes next week. Link below. Ralph. »

---

## Checklist avant tournage

- [ ] Master prompt **v1.1** chargé dans le Claude Project (pas la v1.0)
- [ ] Dataset **Perrin révisé** dans le Project (`[discreet]` sur gift, register 1:1)
- [ ] Run test réalisé pour vérifier que l'output génère proprement en live (ouverture `Cher Dr. Perrin`, gift en Section 6 only)
- [ ] Lumière naturelle OK (tourner entre 10h et 15h)
- [ ] Chemises/tenues alignées (duo — effet jumeaux à leverager)
- [ ] Calendly prêt avec 15-min slot « Client Review Intelligence — Discovery Call »
- [ ] Landing page `ralphchidiac.com` live avec embed vidéo
- [ ] Compliance one-pager PDF prêt à envoyer en follow-up (`compliance-onepager.md` mis en forme)
- [ ] Pilot measurement protocol prêt en annexe contractuelle (`pilot-measurement-protocol.md`)

## Post-production

- Trim intro/outro (pas de hésitation)
- Sous-titres EN burn-in (40% des wealth managers regardent sans son sur mobile/LinkedIn)
- Watermark discret `ralphchidiac.com` bottom-right après la démo
- Export : 1080p, MP4, <50 MB pour intégration email/LinkedIn

## Vérification math (référence)

- 3h × 50 clients = 150h/quarter (bas de la fourchette)
- 4h × 50 clients = 200h/quarter (haut)
- 150–200h ÷ 8h/jour = 18.75–25 workdays/quarter
- × 4 quarters = 75–100 workdays/an
- Arrondi vidéo : « up to 25 workdays/quarter, 100 workdays a year »
- Image parlante : « five months of full-time work » (100 ÷ 20 workdays/mois)

## Deadline

**2026-04-23 soir** — master prompt v1.1 + dataset révisé + run test dans Project validé.
**2026-04-24 (vendredi)** — enregistrement avec frère.
**2026-04-26** — version finale exportée + embed landing page.

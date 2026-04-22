# CRI Outreach — Daily Scoreboard

**Le seul fichier à ouvrir chaque matin.** Ralph, c'est ta page d'accueil.

---

## Ritual matin (90 secondes, tous les jours de semaine)

1. Ouvrir LinkedIn + checker les notifs (response? accept? profile view?).
2. Mettre à jour la tracking table dans `outreach-wave-1-drafts.md` — colonne par colonne, date de l'événement.
3. Lancer le dashboard :
   ```
   cd Output/Client-Review-Intelligence/tools
   source .venv/bin/activate
   python outreach_status.py
   ```
4. Exécuter les « TODAY'S ACTIONS » du dashboard.
5. Si c'est fait, fermer. Rouvrir demain matin. C'est tout.

**Règle absolue :** pas de trading, pas de Twitter, pas de nouvelles features, pas de nouvelles idées de business **tant que le dashboard du jour n'est pas à zéro action**. La discipline quotidienne casse le pattern d'abandon. Le reste = distraction.

---

## P1 — Où on va

**Objectif :** 1 pilote signé à CHF 2 400 avant le 30 juin 2026.

```
Aujourd'hui                                                     P1 target
      │                                                              │
  ────┼──────────────────────────────────────────────────────────────┤
      │                                                              │
 2026-04-22                                                      2026-06-30
```

10 semaines. 6 cibles prio A déjà drafted. 23 prio B/C en backlog. **Un seul oui suffit pour atteindre P1.**

---

## Cadence hebdo (jusqu'à premier pilote signé)

| Jour | Action par défaut |
|------|-------------------|
| **Lundi** | Envoi : wave du lundi (3 nouveaux connect notes, espacés 2-3h) — cible prio A suivante dans la file |
| **Mardi** | D+3 follow-ups sur les cibles acceptées la semaine précédente |
| **Mercredi** | Ritual matin seul. Après-midi : prep de la wave suivante (research + personnalisation si nouveau target) |
| **Jeudi** | D+7 value-add sur les cibles qui ont ouvert le D+3 mais pas répondu |
| **Vendredi** | D+14 close sur les silences totaux. Review hebdo en 10 min : taux de réponse, apprentissages, ajustement message |
| **Week-end** | Off. Si tu touches LinkedIn, c'est pour du contenu perso, pas de l'outreach. |

**Diagnostic hebdo (vendredi fin de journée) :**
- Combien envoyés cette semaine ?
- Combien acceptés ? (target warm-ish cold : ≥ 40%)
- Combien répondu ? (target : ≥ 10% des acceptés)
- Si < target 2 semaines de suite → pause, re-challenge le message avec BOS avant d'envoyer plus.

---

## Stack de fichiers (pour ne pas se perdre)

| Fichier | À quoi ça sert |
|---------|----------------|
| **`outreach-scoreboard.md`** (ce fichier) | Page d'accueil daily |
| **`outreach-wave-1-drafts.md`** | Les 6 messages wave 1 + wave 2, la tracking table (source de vérité) |
| **`eam-pipeline.md`** | Les 30 cibles et la méthodologie — pour piocher les prochaines après wave 1/2 |
| **`outreach-pack-en.md`** | Templates génériques pour si tu dois drafter en urgence sans BOS |
| **`strategy-dossier-v1.pdf`** | Relire avant chaque discovery call pour bien avoir la narrative en tête |
| **`compliance-onepager.md`** | À envoyer en follow-up post-call pour le DPO/CIO |
| **`leave-behind-pack.md`** | À envoyer en follow-up post-call aux decision-makers |
| **`pilot-measurement-protocol.md`** | Annexe du pilot services agreement — à sortir si le prospect demande le cadre contractuel |
| **`master-prompt-v1.md`** | Le prompt de l'agent. À sortir uniquement pour un prospect tech-savvy (Bolko Hohaus type) qui demande à voir |
| **`tools/outreach_status.py`** | Le dashboard CLI lu tous les matins |

---

## Les 3 métriques qui comptent

**Métrique 1 — Taux d'acceptation connect note (proxy de la qualité du message d'intro)**
- Target : ≥ 40% des connect notes envoyés acceptés dans les 72h
- Si < 30% : le hook d'ouverture ne marche pas. Re-drafter avec BOS.

**Métrique 2 — Taux de réponse après D+3 (proxy de la qualité du pitch)**
- Target : ≥ 20% des acceptés répondent au D+3 follow-up
- Si < 10% : le pitch est trop long, trop commercial, ou mal cadré. Re-drafter.

**Métrique 3 — Meeting booked / réponse positive (proxy du credibility stack)**
- Target : ≥ 50% des réponses positives aboutissent à un meeting
- Si < 30% : ta Calendly / tes options de créneaux sont un frein, OU tu parais pas assez sérieux dans le back-and-forth. Fix le handling.

**Le funnel idéal sur 6 messages :** 6 sent → 3 accepted → 1 replied → 1 meeting → 0-1 pilote.
**Le funnel réaliste :** 6 sent → 2-3 accepted → 0-1 replied → 0-1 meeting. Il faudra probablement 15-20 messages pour un pilote sur ce marché froid. Pas de panique à 6 messages = 0 réponse. C'est normal.

---

## Règle d'engagement émotionnelle

**Silence complet sur 6 messages = pas un drame.** 3-8% de réponse en cold est normal sur ce marché.

**Si tu commences à te dire :**
- « mon produit est nul » → **faux**, le produit est solide, le marché est lent
- « je devrais pivoter » → **non**, 6 messages est trop tôt pour juger
- « je vais arrêter » → **c'est exactement ce que le pattern veut**, tu ouvres BOS pour une conversation à la place

**Si une réponse négative :** garde la politesse, remercie, archive. **Tu n'as rien à défendre.** Un « no » est un data point, pas un rejet personnel. Le register Swiss EAM attend justement ça — pas d'insistance.

**Si une réponse positive :** tu respires, tu réponds dans les 2h, tu offres 3 créneaux précis dans les 5 jours qui suivent, tu envoies le Calendly. **Tu ne survends pas dans le back-and-forth.** Le call vendra, pas le texte.

---

## Le scoreboard en une ligne

```
$ python outreach_status.py
```

Run cette commande. Lis le dashboard. Exécute les actions du jour. Point.

---

*Document v1.0 — 2026-04-22 soir. Version vivante : tu le modifies quand tu trouves une meilleure routine matin.*

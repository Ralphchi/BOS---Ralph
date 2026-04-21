# Journal

## 2026-04-20 — Onboarding
- Onboarding complet.
- Profil : Ralph, étudiant EPFL (fin Bachelor ~juin 2026) → Master FinTech à IE Madrid (septembre 2026). Jumeau identique enthousiaste pour co-founder + co-visage. Ami « travailleur » comme backbone ops (relation client + delivery).
- Stade : pré-lancement.
- Première intuition (coaching santé/performance) rejetée par Ralph comme « pas assez stimulante, pas envie de m'exposer sur la santé ». Vrai signal : il veut être vu en **démonstration de maîtrise d'un craft**, pas en démonstration de lifestyle. Pattern d'abandon lié à l'invisibilité, pas à la discipline.
- Direction validée : **AI-for-FinTech services, niche wealth managers**. Plan hybride : services (cash + substance) → marque perso jumeaux (audience) → communauté premium (empire).
- Endgame : communauté premium type Real World / Ecom Empire — inspiration Tate brothers (version européenne clean, intello-premium) et parcours Yomi Denzel.
- Bottleneck : aucun livrable existant.

## 2026-04-20 (update) — Intégration réseau international + pivot brand EN
- Famille basée à Dubai depuis ~10 ans, père avec connexions wealth management local. Footprint familial Dubai/Tokyo/LA/Genève/Riyadh.
- Clarifications : père = pointeur passif. Priorité Suisse mois 1-2, Dubai en backup. Présence physique Dubai été 2026.
- Plan : **séquencement 3 phases** — Suisse → Dubai → Madrid. Brand 100% anglais.

## 2026-04-20 (update) — Recherche marché Swiss EAM + pivot offre
- Marché validé : 1 532 EAMs FINMA-licensed, ~CHF 400 mds AUM, IA adoption 50%, Unique.ch levé 30M$.
- **Pivot offre :** single-module (*Client Review Intelligence*) au lancement, bundles Pro/Elite tués. Positionnement « AI commentary layer on top of existing PMS, PMS-agnostic, tone-trained, Swiss-hosted, FINMA 08/2024 compliant ». Pricing CHF only phase 1 : pilot CHF 2 400 / deploy CHF 7 900 + 499/mois.
- **Sales cycle réalité :** 6-12 mois EAM Swiss. P1 ajusté fin août/septembre 2026 pour premier full deployment.
- Whitespace confirmé. Masttro = closest adjacent.

## 2026-04-20 (update) — Naming exploration
- Stratum, Quill, Fulcrum, Caelus, Kairos, Argentum : tous RED (collisions).
- Helvio : GREEN sur domaines et registry, mais Ralph dit **« ces noms abstraits me parlent pas »**.

## 2026-04-21 — Pivot brand : Ralph Chidiac first, company name punté
- Ralph fait la bonne call : vendre sous **son nom + credentials EPFL/IE** au lieu d'un nom de company abstrait.
- Raisonnement validé : tous les modèles admirés (Hormozi, Yomi, Gadzhi, Tate) ont fait exactement ce move — personal brand d'abord, company name ensuite quand le produit et la clarté sont là.
- Bonus : Swiss wealth management = culture achat ultra-relationnelle, les EAMs signent avec des personnes, pas avec des brands abstraites. Ralph + EPFL + IE = billet d'entrée direct.
- **Architecture brand verrouillée :**
  - Ralph Chidiac (seul puis + frère) = brand de vente
  - The Chidiac Brothers = personal brand long terme (podcast + contenu + communauté)
  - Product = *Client Review Intelligence* (descriptif)
  - Company légale = punté à 3 clients / 6 mois / clarté
- Domaines à réserver : `ralphchidiac.com` + `.ch` + handles `@ralphchidiac` partout. CHF ~40.
- Règle BOS ajoutée à CLAUDE.md pour ne plus insister sur un company name prématurément.
- **Prochaine étape session (aujourd'hui) :** construction de *Client Review Intelligence* en live, sortie attendue = prompt-agent fonctionnel + dataset fictif + démo output + script vidéo 60-90s.

## 2026-04-21 (après-midi) — Client Review Intelligence v1 livrée
- Action #1 de la semaine accomplie. Pattern d'abandon cassé — premier livrable tangible existe avant fin J1.
- **Output produits** dans `Output/Client-Review-Intelligence/` :
  - `master-prompt-v1.md` — system prompt complet pour l'agent (6 sections structurées, tone matching, règles non-négociables)
  - `dataset-perrin-fictif.md` — client test HNWI genevois, CHF 4.25M, conservative, portfolio 13 positions
  - `sample-output-q1-2026.md` — exemple indicatif du review package (v0 BOS-généré) + emplacement pour v1 après run réel
  - `script-demo-90s.md` — script vidéo EN pour l'outreach (hook/pain/demo/CTA, deadline tournage 24 avril)
- **Choix d'architecture expliqué à Ralph :** le repo BOS-Ralph stocke les livrables (version control, diff, IP). Le Claude Project sur claude.ai = runtime d'exécution pour les clients EAM. Les deux coexistent, rôles séparés.
- **Confusion résolue :** Ralph pensait initialement qu'il fallait créer un 2e repo. Non — tout vit dans `Output/` du repo BOS-Ralph existant.
- **Restant aujourd'hui côté Ralph :**
  1. Créer Claude Project `Client Review Intelligence v1` sur claude.ai, coller master prompt en instructions, uploader dataset + samples en knowledge, inviter frère
  2. Run réel sur Perrin, coller output dans `sample-output-q1-2026.md`, commit
- **Prochaine action post-validation :** enchaîner sur action #2 (réservation domaines `ralphchidiac.com/.ch` + handles, deadline demain 22 avril).

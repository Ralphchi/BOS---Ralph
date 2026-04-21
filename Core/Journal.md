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

## 2026-04-21 (fin d'après-midi) — Hardening Module 1 post-critique agent
- Ralph a créé le Claude Project `Client Review Intelligence v1` et a tenté le run. L'agent a **refusé de runner immédiatement** et a produit de lui-même une critique senior-grade de 5 issues matérielles + 2 secondaires avant même de recevoir les 5 blocs.
- **Issues flaggées :** (1) FINMA/Swiss banking secrecy dealbreaker sur pilote `real clients` → cloud US ; (2) refund trigger `<50%` non mesurable = risque juridique ; (3) voice register `Chers clients` incohérent avec destinataire 1 personne ; (4) gift CHF 300k `discreet` apparaît en Section 5 Agenda qui circule ; (5) math vidéo fausse (30 workdays/an au lieu de 100). Deux secondaires : pricing vs valeur non cadré, attribution math hand-wavy.
- **Décision stratégique :** Chemin A (pseudonymisation + positionnement aligné) retenu sur Chemin B (overbuild Azure Switzerland). Logique : le pilote est un proof of value, pas une production-grade platform. Swiss-hosted devient un argument d'upsell du full deployment, pas un prérequis pilote.
- **Artefacts livrés (9 fichiers touchés) :**
  - Master prompt v1.1 — 3 nouvelles règles non-négociables (addressee scope & register, discretion handling, attribution rigour)
  - Dataset Perrin v1.1 — voice samples en 1:1 `Cher Dr. Perrin`, flag `[discreet]` sur gift, section « version pseudonymisée » pour le protocole pilote
  - Sample output v0.1 — ouverture `Cher Dr. Perrin`, gift en Section 6 uniquement, attribution Nestlé phrasée en bps (≈60% du gap, plus « principalement »)
  - Script vidéo v1.1 — math corrigée (100 workdays/an, « five months of full-time work »), CTA compliance (pseudonymized inputs), CTA refund avec baseline/remeasure
  - **compliance-onepager.md (NEW)** — cadre juridique Swiss (art. 47 LB, FINMA 2023/1, FINMA 08/2024, SBA Cloud Guidelines, FADP), data flow, champs pseudonymisés, Anthropic commercial-tier no-training policy, migration Swiss-hosted post-pilote
  - **pilot-measurement-protocol.md (NEW)** — baseline 3 reviews W0 self-loggué par advisor, intervention 28 jours, remeasure 3 reviews W4, formule `(baseline - intervention) / baseline < 0.50 → refund`
  - `Core/Business.md` — positionnement revu (pilot pseudonymized, full deployment Swiss-hosted)
  - `Core/Diagnosis.md` — problème #6 ajouté (compliance layer), bottleneck mis à jour, historique updated
  - `Core/Actions.md` — action 1.5 (hardening) ajoutée et marquée terminée, action 3 (vidéo) updated pour référencer le script v1.1
- **Enseignement stratégique :** le fait que l'agent ait produit une critique senior AVANT d'accepter de runner est un signal puissant que Claude Sonnet/Opus sur ce genre de prompt se comporte comme un analyste senior, pas un exécutant aveugle. À garder pour le pitch : « our system pushes back before it runs — it won't let an advisor ship a compromised review ».
- **Prochaine étape immédiate Ralph :**
  1. Recharger le master prompt **v1.1** dans le Claude Project (écraser l'ancien)
  2. Re-uploader dataset Perrin v1.1 + sample output v0.1 en knowledge (écraser)
  3. Re-run sur Perrin → vérifier checklist validation dans `sample-output-q1-2026.md`
  4. Coller l'output v1 réel dans le fichier sample → BOS commit final
- **Deadline vendredi 24 avril inchangée** — tournage vidéo avec frère, artefacts désormais solides.

## 2026-04-21 (soir) — Run v1 validé, pack Module 1 complet
- Ralph a run le Claude Project avec le master prompt v1.1 + dataset Perrin v1.1. Output v1 généré en ~90 secondes. **Toutes les 9 checkboxes de validation passent.**
- **Qualité observée supérieure à la v0.1 BOS-générée :**
  - Tone matching impeccable, l'agent a même inventé une tournure (« appeler notre vigilance ») parfaitement dans le register sans être dans les samples
  - Talking point #4 dépasse la discrétion : l'agent propose une tactique concrète (sources de liquidité : cash + Swiss corporate IG pour préserver Treasuries) + procédure de note écrite en main propre à Dr. Perrin
  - Section 5 élégante : « transmission et succession — souhaits de révision éventuels » évoque le cycle familial sans trahir le gift
  - Attribution math explicite (58%, -17.5 bps) — rigueur vérifiable
- **Enseignement produit :** la v1.1 du master prompt est déployable sur un premier pilote réel. Risque résiduel = tone matching sur une firm voice réelle (à valider au pilote), pas le prompt lui-même.
- **Pattern d'abandon définitivement cassé pour la semaine 1 :** Ralph a un pack Module 1 complet, versionné, testé et documenté en J+1 du lancement effectif du business. Premier livrable tangible de l'histoire des projets Ralph.
- **Prochaine action :** action #2 — réservation domaines `ralphchidiac.com/.ch` + handles `@ralphchidiac`. Deadline 2026-04-22 (demain). ~10 min chez Infomaniak ou Gandi (domaines) + 5 min par handle.

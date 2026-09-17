# Forge — Lancement d'une marque, de la data au déploiement IA

**Projet fictif** démontrant une compétence transverse : data analyse, SEO/GEO augmenté par l'IA, direction créative, production vidéo, tracking analytics et automatisation — appliqués au lancement d'une marque de compléments et accessoires street workout / calisthenics.

> Ce README documente la démarche end-to-end. Chaque section renvoie vers les livrables du dépôt.

---

## Sommaire

1. [Contexte & positionnement](#contexte--positionnement)
2. [Data — audience & mots-clés](#1--data--audience--mots-clés)
3. [SEO/IA — stratégie éditoriale](#2--seoia--stratégie-éditoriale)
4. [Direction créative — identité visuelle](#3--direction-créative--identité-visuelle)
5. [Vidéo — brief de production](#4--vidéo--brief-de-production)
6. [Analytics — tracking & dashboard](#5--analytics--tracking--dashboard)
7. [Automatisation — reporting IA](#6--automatisation--reporting-ia)
8. [Stack technique](#stack-technique)
9. [Structure du dépôt](#structure-du-dépôt)

---

## Contexte & positionnement

**Forge** est une marque fictive de compléments alimentaires et d'accessoires pour le street workout / calisthenics, conçue comme projet portfolio pour démontrer une double compétence **data + marketing digital + IA appliquée**.

- **Persona principal** : pratiquant sérieux, méfiant du marketing fitness classique, valorise l'effort, la régularité et la discipline
- **Positionnement** : anti-influenceur, performance brute, zéro bullshit marketing
- **Différenciateur méthodologique** : chaque décision créative (couleurs, contenu, ton) découle d'une recherche data en amont, jamais d'une intuition seule

---

## 1 — Data : audience & mots-clés

**Objectif** : construire des personas et une liste de mots-clés priorisés à partir de signaux réels (Reddit, Google Autocomplete, forums spécialisés) plutôt que d'hypothèses.

**Méthode** :
- Recherche qualitative sur les communautés street workout (r/streetworkout, r/bodyweightfitness, forums FR spécialisés) pour identifier vocabulaire, pain points et objections
- Construction de 3 personas différenciés par niveau de pratique (débutant anxieux / intermédiaire en plateau / discipliné identitaire)
- Clustering sémantique des mots-clés collectés, automatisable via script Python (embeddings + clustering hiérarchique)

**Livrables** :
- `clustering_motscles_forge.py` — script de clustering sémantique (sentence-transformers + scikit-learn)

---

## 2 — SEO/IA : stratégie éditoriale

**Objectif** : traduire les clusters de mots-clés en calendrier éditorial structuré, et documenter une méthode reproductible de génération de contenu assistée par IA — pas juste "utiliser ChatGPT".

**Cocons éditoriaux** (issus du clustering) :

| Cocon | Persona ciblé | Objectif SEO |
|---|---|---|
| Débuter sans se blesser | Débutant anxieux | Capter les recherches informationnelles d'entrée |
| Débloquer sa progression | Intermédiaire en plateau | Capter les recherches de résolution de problème |
| Nutrition & récupération | Tous | Pont entre contenu et produit |
| Discipline & mode de vie | Discipliné identitaire | Contenu de marque, réseaux sociaux |

**Méthodologie IA documentée** : chaque article suit un brief structuré (mot-clé, persona, angle, structure Hn, contraintes de marque) transformé en **prompt template réutilisable** — le prompt encode le brief plutôt que de laisser l'IA improviser. C'est ce processus, pas le texte généré, qui constitue la compétence démontrée.

**Livrables** :
- `brief_editorial_forge_musclup.md` — brief complet + template de prompt structuré pour un article pilier

---

## 3 — Direction créative : identité visuelle

**Objectif** : une identité visuelle cohérente cross-canal (web, réseaux sociaux, vidéo), construite à partir du positionnement de marque et produite avec Affinity (scripting SDK).

**Système de marque** :
- **Palette** : anthracite `#1A1A1A`, gris béton `#3A3A3A`, orange brûlé `#C4491D`, blanc cassé `#F2EDE7`
- **Typographie** : Archivo Black (titres/logo) + Inter (texte courant)
- **Logo** : monogramme géométrique "F" construit par script (formes vectorielles unionnées), décliné en 3 variantes (couleur / mono noir / mono blanc)

**Livrables** :
- `brief_creatif_forge.md` — brief créatif complet (specs couleurs, typo, direction)
- `Forge_logo_variantes.afdesign` / `.png` — logo et ses 3 variantes
- `Forge_post_instagram.afdesign` / `.png` — template réseaux sociaux
- `Forge_banniere_web.afdesign` / `.png` — bannière web 1920×600

---

## 4 — Vidéo : brief de production

**Objectif** : une vidéo promotionnelle courte (30-45s) appliquant l'identité visuelle définie à l'étape précédente, montée dans DaVinci Resolve.

**Structure narrative** : accroche → problème (plateau/frustration) → transition marque (logo) → preuve (discipline/régularité) → CTA. Étalonnage sélectif : désaturation générale, orange brûlé comme seule touche saturée — cohérent avec la palette de marque.

**Livrables** :
- `script_video_forge.md` — script détaillé plan par plan (timecodes, cadrage, texte à l'écran, notes d'étalonnage et de montage DaVinci Resolve)

---

## 5 — Analytics : tracking & dashboard

**Objectif** : mesurer la performance éditoriale par cocon (pas juste le trafic global), et relier contenu → intérêt produit.

**Points clés** :
- Variable `cocon` injectée dans le dataLayer GTM sur chaque article — permet de segmenter tous les rapports GA4 par cocon éditorial
- Funnel simple : vue article → scroll 75% → clic CTA produit
- Dashboard Looker Studio en 4 pages : vue d'ensemble, performance éditoriale, SEO (Search Console), acquisition & réseaux sociaux

**Livrables** :
- `plan_tracking_dashboard_forge.md` — plan de tracking GA4/GTM complet + structure du dashboard

---

## 6 — Automatisation : reporting IA

**Objectif** : automatiser la remontée d'insights actionnables (pas juste des chiffres) à partir des données GA4 + Search Console, via un workflow n8n qui appelle l'API Claude pour transformer la donnée brute en synthèse exploitable.

**Workflow** : déclencheur hebdomadaire → appels parallèles GA4 Data API + Search Console API → fusion → analyse par l'API Claude (prompt contraint : 150-200 mots, 3 points d'action) → publication automatique sur Slack.

**Livrables** :
- `forge_workflow_reporting_n8n.json` — workflow n8n complet, importable directement

---

## Stack technique

| Domaine | Outils |
|---|---|
| Data & clustering | Python, pandas, sentence-transformers, scikit-learn |
| SEO & contenu | Recherche manuelle + API Claude (prompts structurés) |
| Design | Affinity Designer (scripting SDK JavaScript) |
| Vidéo | DaVinci Resolve |
| Analytics | Google Analytics 4, Google Tag Manager, Search Console, Looker Studio |
| Automatisation | n8n, API Anthropic (Claude), Slack |

---

## Structure du dépôt

```
forge/
├── README.md
├── data/
│   └── clustering_motscles_forge.py
├── editorial/
│   └── brief_editorial_forge_musclup.md
├── design/
│   ├── brief_creatif_forge.md
│   ├── Forge_logo_variantes.afdesign / .png
│   ├── Forge_post_instagram.afdesign / .png
│   └── Forge_banniere_web.afdesign / .png
├── video/
│   └── script_video_forge.md
├── analytics/
│   └── plan_tracking_dashboard_forge.md
└── automation/
    └── forge_workflow_reporting_n8n.json
```

---

*Projet réalisé dans le cadre d'un portfolio Data/Marketing Analyst — chaque étape est documentée pour montrer la méthode autant que le résultat.*

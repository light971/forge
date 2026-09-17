# Plan de tracking & dashboard — Projet Forge

---

## 1. Architecture GA4

### Propriété & flux de données
- Une propriété GA4 unique : "Forge — Site web"
- Un flux de données Web pointant vers le domaine forge.fr
- Google Signals désactivé si non pertinent pour un projet portfolio (évite le bruit dans les rapports démographiques)

### Événements à suivre (au-delà des événements automatiques GA4)

| Événement | Déclencheur | Paramètres associés | Pourquoi |
|---|---|---|---|
| `article_view` | Vue d'une page article (auto via page_view + paramètre) | `cocon` (débuter / progression / nutrition / discipline), `titre_article` | Mesurer quel cocon éditorial performe |
| `scroll_75` | Scroll à 75% d'un article | `titre_article` | Distinguer trafic qui lit vraiment du trafic qui rebondit |
| `cta_produit_click` | Clic sur un lien/bouton produit depuis un article | `produit`, `emplacement_cta` (fin d'article / bannière) | Mesurer la conversion contenu → intérêt produit |
| `newsletter_signup` | Soumission formulaire newsletter | `emplacement` (footer / popup / article) | KPI d'engagement principal pour un site sans e-commerce actif |
| `social_click` | Clic vers Instagram/réseaux depuis le site | `réseau` | Mesurer le pont site ↔ réseaux sociaux |
| `outbound_click` | Clic vers une boutique externe (si affiliation) | `destination` | Si le produit n'est pas vendu en direct sur le site |

### Configuration GTM

- **Déclencheurs** : Trigger "Scroll Depth" natif GTM pour `scroll_75` ; Click Trigger avec filtre CSS class pour les CTA produits
- **Variables personnalisées** : Data Layer variable `cocon` injectée dans le HTML de chaque template d'article (`<script>dataLayer.push({cocon: "debuter"})</script>`) — c'est ce qui permet de segmenter les rapports par cocon éditorial dans GA4
- **Paramètres UTM** : structure standardisée pour tous les liens sortants du site vers les réseaux
  - `utm_source` = instagram / newsletter / direct
  - `utm_medium` = social / email
  - `utm_campaign` = nom du cocon ou de la campagne (ex : `cocon_progression`)

---

## 2. Structure du dashboard Looker Studio

### Page 1 — Vue d'ensemble
- **Cartes KPI** (en haut, format "scorecard") : Sessions, Utilisateurs, Taux d'engagement, Impressions organiques (connecté via Search Console)
- **Graphique courbe** : Évolution du trafic sur 90 jours, avec annotation aux dates de publication d'articles
- **Répartition des sources de trafic** (camembert) : Organique / Direct / Social / Referral

### Page 2 — Performance éditoriale (le cœur du dashboard)
- **Tableau** : Articles classés par vues, temps moyen, taux de scroll 75%, filtrable par `cocon`
- **Barres comparatives** : Performance des 4 cocons (Débuter / Progression / Nutrition / Discipline) sur trafic + engagement
- **Funnel simple** : Vue article → scroll 75% → clic CTA produit (visualise la déperdition à chaque étape)

### Page 3 — SEO (connecté à Search Console)
- Impressions, clics, CTR moyen, position moyenne — évolution dans le temps
- Tableau des requêtes principales générant du trafic
- Comparaison avant/après optimisation pour les articles retravaillés

### Page 4 — Acquisition & réseaux sociaux
- Clics `social_click` par réseau
- Sessions par `utm_campaign` (mesure l'impact de chaque post Instagram sur le trafic site)
- Taux de conversion newsletter par source

---

## 3. Ce qui rend ce dashboard crédible pour un recruteur

- Il ne se contente pas d'afficher du trafic brut : il **relie la donnée à la stratégie éditoriale** (segmentation par cocon, funnel contenu → produit)
- Il croise **deux sources** (GA4 + Search Console), ce qui montre une maîtrise du tracking cross-outil plutôt qu'un simple export de rapport
- Le funnel simple (vue → scroll → clic CTA) est la preuve que tu penses en termes de **parcours utilisateur**, pas juste de volumétrie

## 4. Prochaine étape concrète

1. Créer la propriété GA4 (5 min)
2. Configurer GTM avec les événements ci-dessus (variable `cocon` en priorité, c'est elle qui structure tout le reste)
3. Publier au moins 2-3 articles avec du vrai trafic (même faible) pour avoir de la donnée à afficher
4. Construire le dashboard Looker Studio en connectant GA4 + Search Console
5. Capturer des screenshots du dashboard pour le portfolio — même avec peu de données, la structure et la logique de segmentation sont ce qui compte

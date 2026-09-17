# Script vidéo — Forge (30-45s, format 9:16)

---

## Découpage plan par plan

| # | Timecode | Plan | Cadrage / mouvement | Texte à l'écran | Son / voix |
|---|---|---|---|---|---|
| 1 | 0:00–0:03 | Gros plan mains qui appliquent de la magnésie, prise de barre | Macro, statique, léger grain | — | Silence, puis un souffle net |
| 2 | 0:03–0:05 | Plan large : silhouette qui s'élance vers une barre de traction, parc urbain | Grand angle, caméra fixe | "Pas de raccourci." | Percussion sèche, un seul coup |
| 3 | 0:05–0:08 | Tentative de muscle-up ratée — chute, frustration visible | Caméra épaule, légèrement tremblante | — | Rien, juste le bruit du corps qui retombe |
| 4 | 0:08–0:11 | Gros plan visage, respiration, regard déterminé | Portrait serré, statique | — | Silence tendu |
| 5 | 0:11–0:15 | Montage rapide (0.5-0.8s/plan) : 3-4 essais successifs, échecs | Coupes cut, caméra à l'épaule | "La plupart abandonnent au premier plateau." | Percussion qui monte en intensité |
| 6 | 0:15–0:20 | Cut sec sur noir, puis apparition du logo F (monogramme) qui se dessine trait par trait | Statique, fond anthracite | "FORGE" (Archivo Black, blanc cassé) | Silence total 0.3s, puis impact sourd |
| 7 | 0:20–0:26 | Montage dynamique : répétitions d'entraînement, sueur, mains sur la barre, gros plans techniques | Coupes rapides (0.6-1s), mix macro/plan large | — | Percussion rythmée, régulière |
| 8 | 0:26–0:32 | Enchaînement de progression : la même personne réussit enfin le mouvement qui la bloquait au plan 3 | Plan large stabilisé, léger ralenti sur la réussite | "La régularité bat le talent." | Percussion qui s'apaise, une note tenue |
| 9 | 0:32–0:38 | Plan large environnement urbain (parc, barres, béton), lumière dorée | Grand angle, léger travelling si possible | — | Silence, respiration calme |
| 10 | 0:38–0:44 | Logo Forge + packaging produit (si mockup dispo) + site web | Statique, fond anthracite, composition centrée | "forge.fr — sans excuses." | Impact final, coupure nette |

---

## Notes de montage DaVinci Resolve

### Rythme
- Plans 1-4 : lents, contemplatifs (1-3s chacun) — installer la tension
- Plan 5 : accélération marquée (cuts de 0.5-0.8s) — créer l'énergie du désarroi
- Plan 6 : rupture totale — silence + noir avant le logo, effet de respiration
- Plans 7-8 : rythme soutenu mais moins haché que le plan 5 (0.6-1s) — énergie positive, pas chaotique
- Plans 9-10 : ralentissement final — laisser respirer avant le CTA

### Étalonnage (Color page)
1. **Désaturation globale** : -15 à -20% de saturation sur l'ensemble du montage (nœud de base)
2. **Poussée des noirs** : Lift légèrement negatif sur le canal luminance pour renforcer l'anthracite
3. **Isolation de l'orange** : nœud de qualification secondaire (HSL Qualifier) ciblant la teinte orange brûlé `#C4491D` — tout le reste reste désaturé, seul l'accent (logo, éventuel élément vestimentaire) ressort
4. **Contraste** : courbe en S modérée, pas agressive — cohérent avec le ton "sérieux, pas criard" de la marque

### Typographie à l'écran
- Toujours Archivo Black (ou Arial Black en substitut), blanc cassé `#F2EDE7`
- Apparition : fade-in simple 0.2s, jamais d'animation "bounce" ou "glitch" — cohérent avec le positionnement anti-tape-à-l'œil
- Position : toujours dans le tiers inférieur ou centré, jamais en haut (format 9:16, zone de sécurité pour les réseaux sociaux)

### Musique / son
- Pas de musique "motivation Instagram" générique (piano épique, montée orchestrale)
- Percussion sèche seule (djembé, clap, ou percussion électronique minimaliste) — cherche sur une bibliothèque libre de droits (Epidemic Sound, Artlist, ou YouTube Audio Library en filtrant "percussion minimal")
- Le silence est un outil : les plans 1, 4 et 6 utilisent l'absence de son comme respiration dramatique

### Format d'export
- Export principal : 1080×1920 (9:16) pour Reels/TikTok/Stories
- Décliner en 1080×1080 (1:1) pour le feed Instagram en recadrant les plans centraux (éviter les plans 2 et 9 qui ont besoin du cadre large)

---

## Ce que tu peux filmer concrètement

- Plans 1, 3, 4, 5, 7, 8 : filmables avec un téléphone, toi-même en street workout (cohérent avec ta pratique réelle mentionnée dans ton CV)
- Plan 2, 9 : plan large environnement — facile à obtenir dans un parc avec structures de street workout
- Plan 6, 10 : purement montage/graphisme, pas de tournage — utilise le logo qu'on a construit dans Affinity

**Astuce tournage** : filme large et varié (plusieurs angles, plusieurs tentatives, plusieurs échecs ET réussites) puis sélectionne au montage — c'est plus simple que d'essayer de tourner exactement dans l'ordre du script.

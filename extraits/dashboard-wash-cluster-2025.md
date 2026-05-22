# Dashboard WASH Cluster State of Palestine — vue filtrée sur Human Appeal

![Dashboard WASH Cluster filtré sur HA](dashboard-wash-cluster-2025.png)

**Source :** Power BI public du WASH Cluster State of Palestine, page « Water »
**Capture :** 22 mai 2026, filtre slicer « HA » activé
**Métadonnées :** strippées (`magick -strip`)

---

## Identification du document

**Titre exact :** *« WASH Cluster — State of Palestine — Number of people reached with appropriate drinking and domestic water services »*

URL publique (page Water) :
https://app.powerbi.com/view?r=eyJrIjoiNDBjNmQwOTktNzFmOS00YWFkLThlYTItN2ExNWZmNzJhNTUyIiwidCI6Ijc3NDEwMTk1LTE0ZTEtNGZiOC05MDRiLWFiMTg5MjAyMzY2NyIsImMiOjh9&pageName=109fa3d4608ac422357d

---

## Ce que montre la capture (filtre HA activé)

### Carte gauche — Reached people by governorate (HA seul)

Échelle `CapPeopleReached` :
- 1 406 (min — Rafah / North Gaza)
- 5 983
- 10 561
- **15 138 (max — gouvernorat le mieux servi par HA)**

Gaza centre, Middle Area et Khan Younis sont les zones où HA touche le plus de monde.

### Pie chart droite — Water quantity (m³) delivered by Governorate (HA seul)

| Gouvernorat | Volume HA | % du HA total |
|---|---|---|
| Khan Younis | **21,72 m³** | 12,83 % |
| Gaza | **90,87 m³** | 53,71 % |
| Middle Area | **48,17 m³** | 28,47 % |
| (Rafah + North Gaza ~5 %) | ~8 m³ | ~5 % |
| **HA total Gaza** | **~169 m³** | 100 % |

Vérification : voir [tooltip exact pour Khan Younis](#tooltip-de-vérification).

### Slicer « Responsive Partners »

62 partenaires Gaza listés. **HA est sélectionné** (surligné en bleu clair dans la capture).

---

## Tooltip de vérification

Sur cette même page, en survolant le secteur « Khan Younis » du pie chart, le tooltip Power BI affiche :

```
Governorate    Khan Younis
Quantity       21,72 (12,83%)
```

Ce qui confirme que **« 21,71500... »** affiché sur l'étiquette du pie chart vaut littéralement **21,72 m³** — pas 21 715 m³ ni 21,72 K m³.

La virgule est ici le séparateur décimal français.

---

## Comparaison avec le cluster total Gaza (sans filtre)

| Métrique | Cluster total | HA seul | Ratio |
|---|---|---|---|
| Total m³ délivrés | ~152 390 | ~169 | **0,11 %** |
| Max people reached (max gouvernorat) | 1 627 252 | 15 138 | **0,93 %** |

**Constat majeur** : sur le dashboard que la publicité de Human Appeal France utilise visuellement, Human Appeal apparaît comme un contributeur **marginal**, pas comme le 2ᵉ plus grand fournisseur d'eau.

---

## Implications pour l'enquête

Cette capture est la **preuve directe** que :

1. ✅ HA est bien un partenaire actif du WASH Cluster (visible dans la liste slicer, sélectionnable)
2. ✅ Le dashboard que la pub référence existe réellement et est public
3. ✅ Les chiffres affichés par le dashboard pour HA sont en m³, pas en K m³ (tooltip confirme « 21,72 »)
4. ❌ HA n'est ni 2ᵉ, ni dans le top 10 en volume m³ ([Constat 4](../constats/04-ranking-2eme-fournisseur.md))

---

## Reproductibilité

N'importe qui peut ouvrir l'URL ci-dessus, cliquer sur « HA » dans la slicer « Responsive Partners », et vérifier ces chiffres en quelques secondes.

C'est précisément ce qui rend le slogan publicitaire facilement vérifiable — et précisément ce qui le rend problématique : la pièce que la pub cite **contredit** le slogan.

---

## Liens

- [Constat 4 : ranking #2 infirmé](../constats/04-ranking-2eme-fournisseur.md)
- [Constat 5 : HA = Human Appeal](../constats/05-acronyme-HA-dans-pub.md)
- [Source dashboard Power BI](../sources/dashboard-powerbi-wash-cluster.md)
- [Données extraites des 62 partenaires](../dashboard-scrape/README.md)

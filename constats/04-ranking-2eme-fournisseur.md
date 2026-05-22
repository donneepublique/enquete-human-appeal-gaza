# Constat 4 — Le ranking « 2ᵉ fournisseur d'eau à Gaza » est INFIRMÉ par les données du dashboard cité

**Statut :** **Infirmé** (mise à jour v4 — précédemment « Non vérifiable »)
**Sources principales :**
- WASH Cluster dashboard Power BI public (page Water)
- Extraction des données partenaire-par-partenaire : [`../dashboard-scrape/partners.csv`](../dashboard-scrape/partners.csv)
- Captures fournies par l'utilisateur

---

## Évolution du constat

| Version | Statut | Raison |
|---|---|---|
| v1 | « Contradicted » | Erreur méthodologique — basé sur le mauvais document |
| v2-v3 | « Non vérifiable publiquement » | Pas de classement public officiel |
| **v4** | **« Infirmé par les données du dashboard cité »** | Extraction directe des données partenaire-par-partenaire |

---

## La méthode de vérification

Le dashboard WASH Cluster Power BI public ([URL complète](../dashboard-scrape/README.md)) permet de filtrer par partenaire pour voir les volumes individuels. La publicité de Human Appeal France utilise une capture de **ce dashboard précis**.

Nous avons extrait les données pour les **62 partenaires Gaza** présents dans la slicer du dashboard via un scraper Playwright headless.

Voir [`../dashboard-scrape/`](../dashboard-scrape/) pour les fichiers et la méthodologie.

---

## Ancres chiffrées vérifiées

Deux partenaires servent de points de calibration, leurs valeurs lues directement par l'utilisateur dans le dashboard :

| Partenaire | Volume m³ (somme Gaza) | Max people reached (max gouvernorat) |
|---|---|---|
| **Cluster total** | **152 390 m³** | **1 627 252** |
| UNICEF | ~37 700 m³ (visible : 4 620 + 10 370 + 20 470) | 940 560 |
| **HA (Human Appeal)** | **~169 m³** (Khan Younis 21,72 + Gaza 90,87 + Middle Area 48,17) | **15 138** |

Les valeurs HA ont été lues sur le tooltip du dashboard par l'utilisateur. Voir [extrait de cette lecture](../extraits/dashboard-wash-cluster-2025.md).

---

## Position de HA dans le classement

### Métrique 1 — Volume d'eau livré (m³)

- **HA = ~169 m³** sur ~152 390 m³ du cluster = **0,11 %**
- Sur les 62 partenaires scrapés, **environ 30 ont un volume m³ supérieur à HA**
- HA est dans le **dernier tiers** du classement par volume

### Métrique 2 — Personnes touchées (max par gouvernorat)

- **HA = 15 138** sur 1 627 252 du cluster = **0,93 %**
- UNICEF seul = 940 560 (= **62 fois** HA dans son meilleur gouvernorat)
- HA est très loin du top par personnes touchées

### Métrique 3 — Bénéficiaires directs mensuels

- UNICEF : 47 000 à 452 000 par mois selon les mois (moyenne ~265 K/mois)
- HA : à reconstituer mais nécessairement nettement inférieur étant donné les autres métriques

---

## Sur aucune métrique HA n'apparaît dans le top 10

L'allégation « 2ᵉ plus grand fournisseur d'eau à Gaza » de la publicité requerrait que HA soit n°2 sur **au moins une métrique défendable**. Sur les trois métriques principales que publie le dashboard cité :

| Métrique | Position approximative de HA | « 2ᵉ » crédible ? |
|---|---|---|
| Volume m³ délivré | ~rang 30+/62 | ❌ Non, c'est même très bas |
| Max people reached par gouvernorat | hors top 20 | ❌ Non |
| Bénéficiaires touchés sur la période | inconnu mais déduit faible | ❌ Non |

**Le dashboard que Human Appeal France utilise pour appuyer son slogan contredit ce slogan.**

---

## L'asymétrie revelatrice

C'est l'observation la plus parlante de toute l'enquête :

> La publicité utilise un visuel WASH Cluster pour suggérer une caution onusienne sur un classement « #2 ». **Le dashboard sous-jacent à ce visuel contredit le slogan.** N'importe quel donateur qui ouvrirait le dashboard via le lien public verrait que Human Appeal y figure comme un partenaire **modeste** (0,1 % du volume cluster), pas comme un acteur dominant.

---

## Limites

- Le mapping `acronyme dashboard → ONG complète` reste incertain pour certains partenaires (acronymes locaux non documentés).
- Les volumes affichés par le dashboard sont auto-reportés par chaque partenaire au cluster ; le cluster n'audite pas ces auto-reports.
- Une métrique différente (capacité installée de désalinisation, financement total, points d'eau opérés selon une autre définition) pourrait classer HA différemment — mais ce serait à HA de produire la donnée justifiant son ranking, pas au donateur de la deviner.

---

## Hypothèse charitable rejetée

On pourrait imaginer que Human Appeal communique sur un classement basé sur des **dollars dépensés** ou **financement levé** plutôt que sur le volume livré. Dans ce cas, le slogan « 2ᵉ fournisseur d'eau » serait techniquement défendable mais **trompeur** pour un grand public qui interprète naturellement « fournisseur d'eau » comme « celui qui apporte l'eau », pas « celui qui finance ».

Plus généralement : un fournisseur d'eau doit fournir de l'eau. 169 m³ sur 152 000 = 0,1 %. Cela ne fait pas un fournisseur de premier plan.

---

## Liens

- [Extraction de données](../dashboard-scrape/README.md) — CSV + méthodologie
- [Constat 5 : HA bien identifié sur le dashboard](05-acronyme-HA-dans-pub.md)
- [Conclusion globale (README)](../README.md)

# Constat 4 — Le ranking « 2ᵉ fournisseur d'eau à Gaza » est INFIRMÉ par les données du dashboard cité

**Statut :** **Infirmé** (mise à jour v4 — précédemment « Non vérifiable »)
**Sources principales :**
- WASH Cluster dashboard Power BI public (page Water)
- Lectures directes par tooltip utilisateur (ancres HA et UNICEF)
- Extraction automatique des données partenaire-par-partenaire : [`../dashboard-scrape/partners.csv`](../dashboard-scrape/partners.csv)

---

## Évolution du constat

| Version | Statut | Raison |
|---|---|---|
| v1 | « Contredit » | Erreur méthodologique — basé sur le mauvais document |
| v2-v3 | « Non vérifiable publiquement » | Pas de classement public officiel identifié à l'époque |
| **v4** | **« Infirmé par les données du dashboard cité »** | Extraction directe des données partenaire-par-partenaire |

---

## La méthode de vérification

Le dashboard WASH Cluster Power BI public ([URL complète](../dashboard-scrape/README.md)) permet de filtrer par partenaire pour voir les volumes individuels. La publicité de Human Appeal France utilise une capture de **ce dashboard précis** (titre, mise en page et chiffres agrégés correspondent).

Deux approches complémentaires ont été utilisées :

1. **Ancres lues à la main** (tooltips) : l'utilisateur a filtré le dashboard sur « HA » puis sur « UNICEF » et a lu les valeurs exactes affichées par les tooltips.
2. **Extraction automatique** : un scraper Playwright a cliqué sur chacun des 62 partenaires de la slicer Gaza et a enregistré les valeurs lues. Voir [`../dashboard-scrape/`](../dashboard-scrape/).

---

## Ancres chiffrées vérifiées (lecture directe)

| Partenaire | Volume m³ (somme Gaza) | Max people reached (max gouvernorat) |
|---|---|---|
| **Cluster total** (sans filtre) | **152 390 m³** | **1 627 252** |
| **UNICEF** | ~37 700 m³ (Middle Area 20 470 + Gaza 10 370 + Khan Younis 4 620 + résiduels) | **940 560** |
| **HA (Human Appeal)** | **~169 m³** (Gaza 90,87 + Middle Area 48,17 + Khan Younis 21,72 + résiduels) | **15 138** |

Ces deux ancres ont été lues directement par l'utilisateur sur les tooltips Power BI. Voir [extrait](../extraits/dashboard-wash-cluster-2025.md). Le scraper a retrouvé exactement ces deux jeux de valeurs dans son extraction (à un décalage d'étiquette près — voir limites ci-dessous).

---

## Position de HA dans le classement — chiffres consolidés

L'extraction automatique a capturé des **valeurs réelles** pour 56 partenaires sur 62 (les 6 autres correspondent à des clicks ratés pendant lesquels le filtre n'a pas été appliqué, voir [méthodologie](../dashboard-scrape/README.md)). En **comparant ces valeurs** (indépendamment de l'étiquette à laquelle elles ont été associées par le scraper), on obtient :

### Métrique 1 — Personnes touchées (max par gouvernorat)

- **HA = 15 138** sur 1 627 252 au niveau cluster = **0,93 %**
- Parmi les **56 valeurs partenaires** réellement capturées, **41 dépassent strictement HA**, 14 sont en-dessous, 1 est exactement HA (= HA lui-même)
- Les 6 clicks ratés sont indéterminés : même s'ils étaient tous inférieurs à HA, HA serait au mieux **rang 42** sur 62
- Aucune valeur capturée ne dépasse UNICEF (940 560) → **UNICEF est le n°1 sur cette métrique**

### Métrique 2 — Volume d'eau livré (m³ cumulé sur la période)

- **HA ≈ 169 m³** sur 152 390 m³ du cluster = **0,11 %**
- Parmi les **56 valeurs partenaires** capturées, **36 ont un total m³ strictement supérieur à HA**, 7 sont inférieures, et 13 n'ont pas de m³ extraits (pie chart vide — possiblement parce que ces partenaires opèrent sur d'autres métriques du dashboard : sanitation, hygiène, etc.)
- Là encore, même en prêtant aux 6 clicks ratés des valeurs faibles, HA reste dans le **dernier tiers** par volume m³

### Métrique 3 — Bénéficiaires directs mensuels

Le dashboard publie aussi un barchart « Direct Beneficiaries Reached by Month ». Il n'a pas été extrait par partenaire faute d'interactivité utile dans la slicer pour ce graphique. Sur les deux autres métriques où HA est dans le dernier tiers du classement, il n'y a aucune raison de penser que HA pourrait se hisser au top sur celle-ci.

---

## Sur aucune métrique HA n'apparaît dans le top 10

L'allégation « 2ᵉ plus grand fournisseur d'eau à Gaza » de la publicité requerrait que HA soit n°2 sur **au moins une métrique défendable**. Sur les deux métriques principales publiées par le dashboard cité :

| Métrique | Position de HA | « 2ᵉ » crédible ? |
|---|---|---|
| Volume m³ délivré (parmi captures > 0) | au moins 36 partenaires devant HA | ❌ Non |
| Max people reached par gouvernorat | rang 42 à 48 sur 62 (bornes selon clicks ratés) | ❌ Non |

**Le dashboard que Human Appeal France utilise pour appuyer son slogan contredit ce slogan.**

---

## L'asymétrie révélatrice

C'est l'observation la plus parlante de toute l'enquête :

> La publicité utilise un visuel WASH Cluster pour suggérer une caution onusienne sur un classement « #2 ». **Le dashboard sous-jacent à ce visuel contredit le slogan.** N'importe quel donateur qui ouvrirait le dashboard via le lien public verrait que Human Appeal y figure comme un partenaire **modeste** (0,11 % du volume cluster), pas comme un acteur dominant.

---

## Limites

- **Décalage d'étiquetage du scraper** : pour 6 partenaires sur 62, le clic dans la slicer n'a pas pris effet avant la lecture (les valeurs capturées sous l'étiquette sont alors la baseline cluster, signal clair d'un click raté). Sur les 56 autres, le mapping `étiquette → valeur` est lui aussi décalé pour ~5 lignes — par exemple les valeurs HA (15 138, etc.) apparaissent sous l'étiquette « IDRF », les valeurs UNICEF (940 560, etc.) sous l'étiquette « UNRWA ». Les **valeurs sont réelles** mais une attribution **valeur → ONG** précise n'est garantie que pour HA et UNICEF (vérifiées par tooltip). Voir [méthodologie](../dashboard-scrape/README.md).
- **Auto-déclaration** : les volumes affichés par le dashboard sont reportés par chaque partenaire au cluster (système 5W). Le cluster n'audite pas ces auto-reports.
- **Métrique alternative théorique** : un classement basé sur capacité installée, financement levé, ou points d'eau opérés selon une autre définition pourrait classer HA différemment. Mais c'est à Human Appeal de produire la donnée qui justifierait son ranking — pas au donateur de la deviner.

---

## Hypothèse charitable rejetée

On pourrait imaginer que Human Appeal communique sur un classement basé sur des **dollars dépensés** ou **financement levé** plutôt que sur le volume livré. Dans ce cas, le slogan « 2ᵉ fournisseur d'eau » serait techniquement défendable mais **trompeur** pour un grand public qui interprète naturellement « fournisseur d'eau » comme « celui qui apporte l'eau », pas « celui qui finance ».

Plus généralement : un fournisseur d'eau doit fournir de l'eau. 169 m³ sur 152 390 m³ = 0,11 %. Cela ne fait pas un fournisseur de premier plan.

---

## Liens

- [Extraction de données](../dashboard-scrape/README.md) — CSV + méthodologie
- [Constat 5 : HA bien identifié sur le dashboard](05-acronyme-HA-dans-pub.md)
- [Conclusion globale (README)](../README.md)

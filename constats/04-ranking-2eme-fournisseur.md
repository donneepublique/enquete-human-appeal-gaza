# Constat 4 — Le ranking « 2ᵉ fournisseur d'eau à Gaza » est INFIRMÉ par les données du dashboard cité

**Statut :** **Infirmé**
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
| v4 | « Infirmé par les données du dashboard cité » | Extraction directe — mais étiquetage scraper buggé |
| **v5** | **« Infirmé par les données du dashboard cité »** | Scraper corrigé (JS-click direct), 62/62 attributions fiables |

---

## La méthode de vérification

Le dashboard WASH Cluster Power BI public ([URL complète](../dashboard-scrape/README.md)) permet de filtrer par partenaire pour voir les volumes individuels. La publicité de Human Appeal France utilise une capture de **ce dashboard précis** (titre, mise en page et chiffres agrégés correspondent).

Deux approches complémentaires :

1. **Ancres lues à la main** (tooltips) : l'utilisateur a filtré le dashboard sur « HA » puis sur « UNICEF » et a lu les valeurs exactes affichées par les tooltips.
2. **Extraction automatique** : un scraper Playwright a cliqué sur chacun des 62 partenaires de la slicer Gaza et a enregistré les valeurs lues. Voir [`../dashboard-scrape/`](../dashboard-scrape/).

Le scrape v2 (JS-click direct par index, vérification stricte et confirmation par double ancre) attribue **62 partenaires sur 62** à leurs vraies valeurs. La fiabilité du mapping `étiquette ↔ ONG` est confirmée par concordance exacte avec les deux ancres lues à la main.

---

## Ancres chiffrées vérifiées (lecture directe)

| Partenaire | Volume m³ (somme Gaza) | Max people reached (max gouvernorat) |
|---|---|---|
| **Cluster total** (sans filtre) | **152 390 m³** | **1 627 252** |
| **UNICEF** | **~35 460 m³** (Middle Area 20 470 + Gaza 10 370 + Khan Younis 4 620 + résiduels) | **940 560** |
| **HA (Human Appeal)** | **~169 m³** (Gaza 90,87 + Middle Area 48,17 + Khan Younis 21,72 + résiduels) | **15 138** |

Ces deux ancres ont été lues directement par l'utilisateur sur les tooltips Power BI. Voir [extrait](../extraits/dashboard-wash-cluster-2025.md). Le scrape automatique retrouve **exactement** ces valeurs sous les bonnes étiquettes.

---

## Position de HA dans le classement — chiffres consolidés

### Métrique 1 — Personnes touchées (max par gouvernorat)

- **HA = 15 138** sur 1 627 252 au niveau cluster = **0,93 %**
- **Rang HA : 48 sur 62 partenaires** — dernier tiers
- UNICEF est n°1 (940 560) — **62× HA**

Top 10 par max_people :

| Rang | Partenaire | max_people |
|---|---|---|
| 1 | UNICEF | 940 560 |
| 2 | PALSTD | 481 495 |
| 3 | AAH | 371 688 |
| 4 | AIOCP | 351 983 |
| 5 | HF | 288 153 |
| 6 | MAAN | 248 896 |
| 7 | CARE | 225 565 |
| 8 | QRCS | 222 015 |
| 9 | MECA | 215 465 |
| 10 | PCRF | 193 116 |
| … | | |
| **48** | **HA** | **15 138** |

### Métrique 2 — Volume d'eau livré (m³ cumulé sur la période)

- **HA ≈ 169 m³** sur 152 390 m³ cluster = **0,11 %**
- **Rang HA : 42 sur 62 partenaires** (49 ont des m³ extraits ; les 13 autres ont un pie vide — partenaires actifs sur d'autres métriques du dashboard : sanitation, hygiène, etc.)
- UNICEF n°1 avec ~35 460 m³ — **210× HA**

Top 10 par total m³ :

| Rang | Partenaire | total m³ |
|---|---|---|
| 1 | UNICEF | ~35 460 |
| 2 | PCRF | ~17 440 |
| 3 | OCK3 | ~15 560 |
| 4 | AAH | ~10 500 |
| 5 | MECA | ~7 640 |
| 6 | UNRWA | ~6 080 |
| 7 | PALSTD | ~4 240 |
| 8 | MSF-F | ~4 200 |
| 9 | GDD | ~3 860 |
| 10 | SCI | ~3 840 |
| … | | |
| **42** | **HA** | **~169** |

### Métrique 3 — Bénéficiaires directs mensuels

Le dashboard publie aussi un barchart « Direct Beneficiaries Reached by Month ». Il n'a pas été extrait par partenaire faute d'interactivité utile dans la slicer pour ce graphique. Sur les deux autres métriques où HA est dans le dernier tiers du classement, il n'y a aucune raison de penser que HA pourrait se hisser au top sur celle-ci.

---

## Sur aucune métrique HA n'apparaît dans le top 10

L'allégation « 2ᵉ plus grand fournisseur d'eau à Gaza » de la publicité requerrait que HA soit n°2 sur **au moins une métrique défendable**. Sur les deux métriques principales publiées par le dashboard cité :

| Métrique | Rang de HA | « 2ᵉ » crédible ? |
|---|---|---|
| Volume m³ délivré | **42 sur 62** | ❌ Non |
| Max people reached par gouvernorat | **48 sur 62** | ❌ Non |

**Le dashboard que Human Appeal France utilise pour appuyer son slogan contredit ce slogan.**

---

## L'asymétrie révélatrice

C'est l'observation la plus parlante de toute l'enquête :

> La publicité utilise un visuel WASH Cluster pour suggérer une caution onusienne sur un classement « #2 ». **Le dashboard sous-jacent à ce visuel contredit le slogan.** N'importe quel donateur qui ouvrirait le dashboard via le lien public verrait que Human Appeal y figure comme un partenaire **modeste** (0,11 % du volume cluster), pas comme un acteur dominant.

---

## Limites

- **Auto-déclaration** : les volumes affichés par le dashboard sont reportés par chaque partenaire au cluster (système 5W). Le cluster n'audite pas ces auto-reports.
- **Période d'observation** : les chiffres reflètent les déclarations cumulées sur la période couverte par le dashboard public à la date de capture (mai 2026). Une fenêtre différente pourrait donner d'autres ratios — mais c'est précisément le dashboard qu'utilise visuellement la publicité.
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

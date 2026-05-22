# Source : Dashboard Power BI public — WASH Cluster State of Palestine

**Type :** dashboard interactif Power BI hébergé publiquement
**Émetteur :** WASH Cluster State of Palestine (équipe de coordination UNICEF)
**Mise à jour observée :** 23 septembre 2025 (date affichée dans la pub) — données toujours accessibles en mai 2026
**Hébergement :** Microsoft Power BI public (`app.powerbi.com/view`)

---

## URLs

- Page **Water** (celle citée par la pub Human Appeal France) :
  https://app.powerbi.com/view?r=eyJrIjoiNDBjNmQwOTktNzFmOS00YWFkLThlYTItN2ExNWZmNzJhNTUyIiwidCI6Ijc3NDEwMTk1LTE0ZTEtNGZiOC05MDRiLWFiMTg5MjAyMzY2NyIsImMiOjh9&pageName=109fa3d4608ac422357d

- Dashboard parent (7 pages : Flash Appeal, Water, Sanitation, SWM, Hygiene, Supplies, WASH in institutions) :
  https://app.powerbi.com/view?r=eyJrIjoiNDBjNmQwOTktNzFmOS00YWFkLThlYTItN2ExNWZmNzJhNTUyIiwidCI6Ijc3NDEwMTk1LTE0ZTEtNGZiOC05MDRiLWFiMTg5MjAyMzY2NyIsImMiOjh9

---

## Pourquoi cette source est centrale

C'est la **source primaire** que la publicité de Human Appeal France utilise comme caution visuelle. Le visuel zoomé dans la pub est une capture de ce dashboard précis (titre exact « WASH Cluster — State of Palestine — Number of people reached with appropriate drinking and domestic water services », page « Water »).

Cette source permet ce qu'aucune autre source publique n'autorise : **lire les chiffres individuels par partenaire** via le filtre slicer. Sans cette source, le ranking « #2 » n'aurait pas pu être directement infirmé — seulement marqué « non vérifiable ».

---

## Force probante

| Aspect | Force probante |
|---|---|
| Authorship | UNICEF (équipe de coordination WASH Cluster State of Palestine) |
| Hébergement | Microsoft Power BI public — donc lecture par n'importe qui sans authentification |
| Données affichées | Auto-déclarées par les partenaires au cluster (système 5W), agrégées et publiées sans audit indépendant |
| Mise à jour | Régulière (la date « 23 September 2025 » dans la pub est la date de la dernière mise à jour à ce moment-là) |

⚠ **Limite essentielle** : les chiffres sont auto-déclarés par les partenaires. Le cluster ne les audite pas. Mais ce sont les chiffres que le cluster lui-même retient et publie, donc ils représentent la **vérité institutionnelle reconnue** sur la question.

---

## Métriques principales (page Water)

1. **Number of water points** (Gaza) — type de point d'eau par gouvernorat
2. **Daily drinking water delivery (m³)** — volumes en m³ par jour
3. **Daily domestic water delivery (m³)** — autre catégorie de volume
4. **Number of partners** — nombre de partenaires actifs (41 au 23 sept 2025)
5. **Water quantity (m³) delivered by Governorate** — pie chart, ventilation par gouvernorat
6. **Reached people by governorate** — carte choroplèthe, échelle `CapPeopleReached`
7. **Direct Beneficiaries Reached by Month** — barchart historique mensuel
8. Slicer **Responsive Partners** — liste des 62 partenaires Gaza et 14 Cisjordanie, cliquables pour filtrer

---

## Données extraites pour cette enquête

Voir [`../dashboard-scrape/`](../dashboard-scrape/) :

- `partners.csv` — 62 partenaires × données par gouvernorat (volume m³, % du total partenaire, max people reached)
- `partners_raw.json` — sortie brute du scraper
- Code source : `../scripts/scrape-dashboard.py`

### Données baseline (cluster entier Gaza, sans filtre)

| Métrique | Valeur |
|---|---|
| Total m³ délivrés (somme 4 gouvernorats) | **152 390 m³** |
| Max people reached (max gouvernorat) | **1 627 252** |
| Répartition par gouvernorat (m³) | Middle Area 49 030 (31,28 %) · Khan Younis 46 330 (29,55 %) · Gaza 44 120 (28,14 %) · North Gaza 12 910 (8,24 %) |

### Données pour Human Appeal (HA) — vérifiées via tooltip user

| Gouvernorat | Volume m³ HA | % du total HA |
|---|---|---|
| Khan Younis | 21,72 | 12,83 % |
| Gaza | 90,87 | 53,71 % |
| Middle Area | 48,17 | 28,47 % |
| (Rafah + North Gaza résiduels) | ~8 | ~5 % |
| **HA total Gaza** | **~169 m³** | 100 % |
| Max people reached HA (max gouvernorat) | **15 138** | — |

**HA = 0,11 % du volume cluster Gaza et 0,93 % du max people reached.**

### Données pour UNICEF — vérifiées via screenshot user

| Gouvernorat | Volume m³ UNICEF | % |
|---|---|---|
| Khan Younis | 4 620 | 12,19 % |
| Gaza | 10 370 | 27,36 % |
| Middle Area | 20 470 | 54,01 % |
| (résiduel) | ~2 200 | ~6 % |
| **UNICEF total Gaza** | **~37 700 m³** | 100 % |
| Max people reached UNICEF | **940 560** | — |

---

## Limites de la source

1. **Auto-déclaration** : aucun audit indépendant des volumes reportés par chaque partenaire.
2. **Mapping acronyme → ONG** : pour ~6-10 partenaires sur 62, l'acronyme local n'est pas documenté ailleurs (OCK3, GDD, GEM, PAEEP, etc.).
3. **Périodicité** : la date affichée (23 sept 2025) est la dernière mise à jour mais le dashboard est cumulatif sur 2025, pas une situation instantanée.
4. **Données potentiellement contestées** : un partenaire peut sous-déclarer (pour ne pas attirer l'attention sur ses livraisons en zone sensible) ou sur-déclarer (pour valoriser son rôle auprès des bailleurs).

---

## Voir aussi

- [Méthodologie de l'extraction](../dashboard-scrape/README.md)
- [Constat 4 (la conclusion principale, basée sur cette source)](../constats/04-ranking-2eme-fournisseur.md)
- [Extrait visuel](../extraits/dashboard-wash-cluster-2025.md)

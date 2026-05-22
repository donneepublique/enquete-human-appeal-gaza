# Extraction des données du dashboard WASH Cluster

## Source

Dashboard Power BI public du WASH Cluster State of Palestine, page « Water » :

https://app.powerbi.com/view?r=eyJrIjoiNDBjNmQwOTktNzFmOS00YWFkLThlYTItN2ExNWZmNzJhNTUyIiwidCI6Ijc3NDEwMTk1LTE0ZTEtNGZiOC05MDRiLWFiMTg5MjAyMzY2NyIsImMiOjh9&pageName=109fa3d4608ac422357d

C'est précisément le dashboard dont la publicité de Human Appeal France utilise une capture (titre exact, mise en page et chiffres agrégés correspondent).

## Méthode

Scraper Playwright + Chrome headless qui, pour chacun des 62 partenaires Gaza listés dans la slicer du dashboard, applique le filtre et lit les valeurs affichées sur :

- La carte choroplèthe « Reached people by governorate » (échelle `CapPeopleReached`)
- Le pie chart « Water quantity (m³) delivered by Governorate »

Code : [`../scripts/scrape-dashboard.py`](../scripts/scrape-dashboard.py)
Analyse : [`../scripts/analyze-partners.py`](../scripts/analyze-partners.py)

## Fichiers

| Fichier | Contenu |
|---|---|
| `partners.csv` | Un partenaire par ligne, avec les m³ par gouvernorat, pourcentages et max people reached |
| `partners_raw.json` | Sortie brute du scraper (mêmes données, format JSON détaillé) |

## ⚠️ Avertissement sur les étiquettes (limite connue)

Le scraper clique sur chaque partenaire séquentiellement et lit ensuite les valeurs affichées. Deux limites :

1. **6 clicks « ratés » sur 62** : pour 6 partenaires de la slicer (AH, HF, IWWAA, PALSTD, PSCF, WCK dans notre run), le clic n'a pas pris effet avant la lecture — les valeurs enregistrées sous ces étiquettes sont **identiques à la baseline cluster** (152 390 m³ total et 1 627 252 max people). C'est le signal clair que le filtre n'a pas été appliqué.

2. **Décalage d'étiquetage pour ~5 lignes** : sur les 56 captures « réussies » (= valeurs différentes de la baseline), pour ~5 lignes le mapping `étiquette → valeur` est décalé. Exemples vérifiables :
   - Les valeurs HA réelles (max_people 15 138, m³ 90,87 / 48,17 / 21,72) apparaissent dans le CSV **sous l'étiquette « IDRF »**
   - Les valeurs UNICEF réelles (max_people 940 560, m³ 20 470 / 10 370 / 4 620) apparaissent **sous l'étiquette « UNRWA »**

**Conséquence :** les **valeurs sont réelles** (elles correspondent bien à un partenaire réel du cluster) ; le **mapping `étiquette → ONG` est garanti uniquement pour HA et UNICEF**, par double vérification via les tooltips lus à la main.

### Vérification par ancres

| Partenaire | Valeur attendue (tooltip user) | Valeur trouvée dans le scrape | Étiquette dans le CSV |
|---|---|---|---|
| HA | max_people = 15 138 ; m³ : 21,72 / 90,87 / 48,17 | Identique | « IDRF » (décalage) |
| UNICEF | max_people = 940 560 ; m³ : 4,62K / 10,37K / 20,47K | Identique | « UNRWA » (décalage) |

Ces deux ancres confirment que les **valeurs sont fiables** et que l'**étiquetage n'est pas fiable** pour les lignes concernées.

## Données baseline (cluster total Gaza)

- Total m³ délivrés (somme 4 gouvernorats) : **152 390 m³**
- Max people reached (max gouvernorat) : **1 627 252**
- Répartition par gouvernorat :
  - Middle Area : 49 030 m³ (31,28 %)
  - Khan Younis : 46 330 m³ (29,55 %)
  - Gaza : 44 120 m³ (28,14 %)
  - North Gaza : 12 910 m³ (8,24 %)

## Position de HA dans la distribution — chiffres value-based

L'extraction ayant 6 clicks ratés (= 6 valeurs inconnues) et ~5 décalages d'étiquette mais des **valeurs réelles**, la comparaison se fait par **valeurs**, pas par étiquettes :

- **56 captures « réussies »** sur 62 (valeurs distinctes de la baseline)
- **HA = 15 138** max people, **~169 m³** total Gaza (lus par tooltip)

| Métrique | Captures > HA | Captures = HA | Captures < HA | Captures sans donnée m³ |
|---|---|---|---|---|
| max_people | **41 / 56** | 1 (= HA lui-même) | 14 | — |
| total m³ | **36 / 56** | 1 (= HA lui-même) | 7 | 13 (pie vide) |

**Borne :** même si les 6 clicks ratés correspondaient tous à des partenaires plus petits que HA (hypothèse la plus favorable), HA serait au **rang 42 sur 62** par max_people. C'est largement hors du top 10 et **incompatible avec un classement « 2ᵉ »**.

UNICEF est confirmé n°1 par max_people : aucune valeur capturée ne dépasse 940 560.

Voir [`../constats/04-ranking-2eme-fournisseur.md`](../constats/04-ranking-2eme-fournisseur.md) pour l'analyse complète.

## Reproductibilité

```bash
# Installer playwright avec Chrome système
pip install playwright
playwright install chrome  # ou utiliser /Applications/Google Chrome.app

# Lancer le scrape (~5 min)
python scripts/scrape-dashboard.py

# Analyser
python scripts/analyze-partners.py
```

Le dashboard étant public, n'importe qui peut reproduire cette extraction. Une exécution alternative qui voudrait éliminer le problème de décalage d'étiquetage devrait ajouter une vérification après chaque clic (par exemple : attendre que la baseline change vraiment, ou re-cliquer si la valeur lue est identique à la précédente). Cette amélioration n'est pas nécessaire pour la conclusion principale, qui repose sur des comparaisons de **valeurs** indépendantes des étiquettes.

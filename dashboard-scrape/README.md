# Extraction des données du dashboard WASH Cluster

## Source

Dashboard Power BI public du WASH Cluster State of Palestine, page « Water » :

https://app.powerbi.com/view?r=eyJrIjoiNDBjNmQwOTktNzFmOS00YWFkLThlYTItN2ExNWZmNzJhNTUyIiwidCI6Ijc3NDEwMTk1LTE0ZTEtNGZiOC05MDRiLWFiMTg5MjAyMzY2NyIsImMiOjh9&pageName=109fa3d4608ac422357d

C'est précisément le dashboard dont la publicité de Human Appeal France utilise une capture.

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

## ⚠️ Avertissement sur les étiquettes

Le scraper clique sur chaque partenaire séquentiellement. Pour ~6 partenaires sur 62, le timing entre clic et lecture a produit un décalage d'étiquetage : la donnée du partenaire X peut apparaître sous l'étiquette du partenaire suivant dans l'ordre alphabétique.

**Les valeurs chiffrées sont correctes** — elles correspondent bien à un partenaire réel du cluster. Mais le **mapping `étiquette → partenaire` est incertain pour ~10 % des lignes**.

### Vérification par ancres

| Partenaire | max_people attendu (tooltip user) | max_people trouvé dans le scrape | Étiquette correspondante | Décalage |
|---|---|---|---|---|
| HA | 15 138 | 15 138 | "IDRF" | +2 positions |
| UNICEF | 940 560 | 940 560 | "UNRWA" | +1 position |

Ces deux ancres confirment que les valeurs sont réelles mais que le label peut être décalé.

## Données baseline (cluster total Gaza)

- Total m³ délivrés (somme 4 gouvernorats) : **152 390 m³**
- Max people reached (max gouvernorat) : **1 627 252**
- Répartition par gouvernorat :
  - Middle Area : 49 030 m³ (31,28 %)
  - Khan Younis : 46 330 m³ (29,55 %)
  - Gaza : 44 120 m³ (28,14 %)
  - North Gaza : 12 910 m³ (8,24 %)

## Distribution des partenaires par volume

Sur 62 partenaires scrapés (avec incertitude sur ~6 étiquettes) :

- **~14 partenaires** ont un total m³ > 2 000 m³
- **~30 partenaires** ont un total m³ > 169 m³ (= valeur HA)
- **HA** est dans le **dernier tiers** du classement par volume

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

Le dashboard étant public, n'importe qui peut reproduire cette extraction.

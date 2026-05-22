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

### Cycle de vérification par partenaire

Une version antérieure du scraper enregistrait des données mal attribuées (par exemple les valeurs HA stockées sous l'étiquette « IDRF »). La cause : les méthodes de clic Playwright (`.get_by_text().click()`, `.locator().click()`, `page.mouse.click(x,y)`) ratent d'une ligne sur ce slicer Power BI virtualisé et sélectionnent l'item juste au-dessus de celui visé.

La version actuelle :

1. **Click par JavaScript direct** : on identifie le `.slicerItemContainer` dont le `textContent` exact matche le partenaire, on appelle `element.click()` en JS depuis l'iframe. C'est la seule stratégie qui sélectionne fiablement le bon item (vérifié par diagnostic).
2. **Reset à la baseline avant chaque clic** : on confirme que le dashboard est en état non-filtré (max = 1 627 252) avant d'appliquer un nouveau filtre.
3. **Attente active jusqu'à filtre appliqué + stable** : on poll l'état du dashboard jusqu'à ce qu'il diffère de la baseline ET que deux lectures consécutives soient identiques.
4. **Toggle off + confirmation retour baseline** après chaque partenaire.
5. **Vérification d'ancre** en fin de run : on compare les valeurs scrapées pour HA et UNICEF aux valeurs lues à la main par tooltip dans le dashboard. Le run actuel passe les deux ancres.

### Diagnostic

Le script `../scripts/diagnose-slicer.py` teste plusieurs stratégies de click sur l'entrée « HA » du slicer et vérifie laquelle sélectionne réellement HA (et pas un voisin). Sortie typique :

```
=== Strategy: js_click_by_index ===
  ✓ After click 'HA': selected = ['HA']
=== Strategy: playwright_get_by_text ===
  ✗ After click 'HA': selected = ['GEM']
=== Strategy: playwright_coordinate ===
  ✗ After click 'HA': selected = []
=== Strategy: playwright_locator_by_index ===
  ✗ After click 'HA': selected = ['GEM']
```

## Fichiers

| Fichier | Contenu |
|---|---|
| `partners_raw.json` | Sortie brute du scraper, format JSON détaillé |
| `partners.csv` | Format **long** (un partenaire × gouvernorat par ligne) — valeurs au format PowerBI (« 2,92K », virgule décimale française) |
| `partners_wide.csv` | Format **wide** (un partenaire par ligne) — valeurs numériques parsées, m³ par gouvernorat, totaux, % cluster, rangs |

Le `partners_wide.csv` est généré par [`../scripts/build-wide-csv.py`](../scripts/build-wide-csv.py) à partir du JSON brut.

## Vérification par ancres

| Partenaire | Valeur attendue (tooltip user) | Valeur scrapée | Statut |
|---|---|---|---|
| HA | max_people = 15 138 ; m³ : 21,72 / 90,87 / 48,17 | Identique | ✓ |
| UNICEF | max_people = 940 560 ; m³ : 4,62K / 10,37K / 20,47K | Identique | ✓ |

**62 captures sur 62 réussies. Aucune erreur d'attribution.**

## Données baseline (cluster total Gaza, filtre vide)

- Total m³ délivrés (somme 4 gouvernorats) : **152 390 m³**
- Max people reached (max gouvernorat) : **1 627 252**
- Répartition par gouvernorat :
  - Middle Area : 49 030 m³ (31,28 %)
  - Khan Younis : 46 330 m³ (29,55 %)
  - Gaza : 44 120 m³ (28,14 %)
  - North Gaza : 12 910 m³ (8,24 %)

## Position de HA dans la distribution

Données partenaire-par-partenaire (62/62 captures valides) :

| Métrique | Valeur HA | Rang HA | UNICEF (n°1 sur max_people) |
|---|---|---|---|
| max_people (max gouvernorat) | **15 138** | **48 / 62** | 940 560 |
| total m³ délivrés | **~169 m³** | **42 / 62** | 35 460 m³ |

**HA contribue 0,11 % du volume m³ du cluster et 0,93 % du max_people cluster.** UNICEF apporte à lui seul 210× plus de m³ que HA et 62× plus de max_people. Le slogan « 2ᵉ fournisseur d'eau à Gaza » est incompatible avec ces deux classements.

Voir [`../constats/04-ranking-2eme-fournisseur.md`](../constats/04-ranking-2eme-fournisseur.md) pour l'analyse complète.

## Reproductibilité

```bash
# Installer playwright avec Chrome système
pip install playwright
playwright install chrome  # ou utiliser /Applications/Google Chrome.app

# Lancer le scrape (~10-12 min)
python scripts/scrape-dashboard.py

# Vérifier les ancres dans la sortie ; passer l'analyse
python scripts/analyze-partners.py
```

Le dashboard étant public, n'importe qui peut reproduire cette extraction. Le script `scrape-dashboard.py` imprime une section « ANCRES DE VÉRIFICATION » en fin de run qui doit afficher ✓ pour HA et UNICEF — sinon les données ne sont pas fiables et il faut investiguer (typiquement avec `scripts/diagnose-slicer.py`).

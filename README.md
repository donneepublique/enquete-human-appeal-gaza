# Enquête : Human Appeal est-il vraiment le « 2ᵉ fournisseur d'eau à Gaza » ?

> Vérification factuelle d'une publicité Instagram de Human Appeal France affirmant que l'ONG est le « 2ᵉ plus grand fournisseur d'eau à Gaza » selon le WASH Cluster (UN-OCHA).

**Période :** 22-23 mai 2026.

---

## Synthèse en une page

La publicité fait deux affirmations distinctes :

| Affirmation | Statut | Pourquoi |
|---|---|---|
| Human Appeal est partenaire du WASH Cluster ONU pour Gaza | ✅ **Vrai** | Profil officiel page 35 du *WASH Cluster Partners' Profile, juillet 2022* (UNICEF / UN-OCHA) |
| Human Appeal est le **2ᵉ plus grand fournisseur d'eau** à Gaza | ❌ **Infirmé** | Les données du dashboard cité par la pub elle-même contredisent ce ranking |

**Le chiffre qui tue le slogan :** sur le dashboard WASH Cluster (page Water), Human Appeal a livré **~169 m³ d'eau** sur **152 390 m³** au total du cluster Gaza. C'est **0,11 %**. Sur les 62 partenaires Gaza extraits du dashboard avec une attribution fiable (62/62), HA est :

- **rang 48 sur 62 par max_people** (personnes touchées dans le gouvernorat le mieux servi par HA)
- **rang 42 sur 62 par volume m³** délivré

UNICEF, n°1 sur les deux métriques, fait **62× plus** de personnes touchées et **210× plus** de m³ que HA.

---

## Index des constats

### Claims publicitaires vérifiés

Les affirmations factuelles précises que la publicité avance pour justifier le don.

| # | Claim | Statut |
|---|---|---|
| 4 | [« 2ᵉ plus grand fournisseur d'eau à Gaza »](constats/04-ranking-2eme-fournisseur.md) | ❌ **Infirmé** — rang 48/62 par personnes touchées, rang 42/62 par m³ |
| 7 | [« Plus de 100 millions de litres d'eau » livrés](constats/07-volume-cumule-100M-litres.md) | ❌ **Non démontré** — impliquerait 4-10 % du desal cluster 2024 ; HA jamais nommée dans les newsletters cluster 2024 |
| 8 | [« Largest desalination plant in southern Gaza »](constats/08-plant-desalinisation-claims.md) | ❌ **Faux** — South Gaza Plant (EU/UNICEF) ~9-12× plus grande ; HA dit elle-même que sa plant est fermée depuis mai 2024 |
| 9 | [« In Gaza since 1991 » / « 35 years in Palestine »](constats/09-dates-presence-gaza.md) | ❌ **Trompeur** — HA déclare à l'ONU (WASH Cluster 2022) « operational in Palestine since 2018 » ; bureau Gaza ouvert en 2016 |

### Contexte et questionnements

Les éléments de contexte qui encadrent les claims et permettent de les évaluer (HA est-elle membre du cluster ? à quel niveau d'engagement ? l'acronyme « HA » désigne-t-il bien Human Appeal ?).

| # | Question | Réponse |
|---|---|---|
| 1 | [HA est-elle partenaire du WASH Cluster ?](constats/01-partenariat-cluster.md) | ✅ Oui, profil officiel 2022 |
| 2 | [À quel niveau d'instance de coordination ?](constats/02-instances-coordination.md) | Membre simple, pas SAG / TWiG |
| 3 | [Évolution du cluster 2022 → 2025 ?](constats/03-evolution-cluster-2022-2025.md) | 61 → 77 partenaires |
| 5 | [L'acronyme « HA » du dashboard = Human Appeal ?](constats/05-acronyme-HA-dans-pub.md) | ✅ Confirmé par tooltip + standard onusien |

> La numérotation saute le 6 : le Constat 6 (statut juridique) a été retiré comme hors-sujet en v6 — voir [`corrections.md`](corrections.md).

---

## Démarche

1. **Identifier la source citée par la pub** : la pub utilise un visuel du dashboard public WASH Cluster (page Water) du Power BI de UNICEF / UN-OCHA.
2. **Lire ce que dit le dashboard sur HA** : tooltip user montre HA Khan Younis = 21,72 m³ ; HA Gaza = 90,87 m³ ; HA Middle Area = 48,17 m³ ; max people reached (max gouvernorat) = 15 138.
3. **Comparer HA aux 61 autres partenaires** : scraping Playwright du slicer Power BI (JS-click direct, vérification d'ancre par double tooltip HA + UNICEF). Voir [`dashboard-scrape/`](dashboard-scrape/).
4. **Conclure** : HA est un contributeur **marginal** (0,11 % du volume cluster, 0,93 % du max people reached du cluster) — pas un acteur de premier plan.

---

## Conclusion journalistique

**Sur le statut institutionnel** : Human Appeal *est* effectivement reconnu comme partenaire du WASH Cluster par les Nations Unies depuis 2022. C'est documenté et vérifiable. La première version de cette enquête a contesté ce statut à tort ; voir [`corrections.md`](corrections.md).

**Sur le ranking « #2 »** : il est **infirmé par les données mêmes que la publicité référence visuellement**. Le dashboard Power BI du WASH Cluster montre Human Appeal comme un contributeur modeste (~0,1 % du volume d'eau du cluster), pas comme un acteur dominant.

**Sur la transparence publicitaire** : la pub crée une impression de caution onusienne en utilisant le visuel d'un tableau de bord ONU. Cette impression est **partiellement justifiée** (HA *est* membre du cluster) et **partiellement trompeuse** (le tableau de bord ne dit pas ce que la pub lui fait dire — au contraire, il le contredit).

**Pour le donateur** :
- ✅ Human Appeal est bien une ONG humanitaire reconnue par l'ONU pour Gaza
- ❌ Le chiffre « #2 » qui justifie le ton de la collecte n'est pas démontré, et le dashboard cité indique le contraire

---

## Structure du dossier

```
enquete-human-appeal-gaza/
├── README.md                   ← ce fichier (synthèse + index)
├── methodologie.md             démarche, limites, biais
├── corrections.md              historique des erreurs (v1 → v6)
│
├── constats/                   les constats détaillés
│   ├── 01-partenariat-cluster.md             ✅ Confirmé
│   ├── 02-instances-coordination.md          Membre simple
│   ├── 03-evolution-cluster-2022-2025.md     61 → 77 partenaires
│   ├── 04-ranking-2eme-fournisseur.md        ❌ INFIRMÉ
│   ├── 05-acronyme-HA-dans-pub.md            ✅ HA = Human Appeal
│   ├── 07-volume-cumule-100M-litres.md       ❌ « 100M+ litres » positionné comme leading provider ; cluster dit l'inverse
│   ├── 08-plant-desalinisation-claims.md     ❌ « Largest in southern Gaza » faux ; plant fermée depuis mai 2024
│   └── 09-dates-presence-gaza.md             ❌ « Since 1991 in Gaza » trompeur — HA déclare « since 2018 » à l'ONU
│
├── sources/                    description critique des sources primaires et tierces
│   ├── README.md
│   ├── wash-cluster-partners-profile-2022.md
│   ├── wash-cluster-contingency-plan-2022.md
│   ├── ocha-rapports-2025.md
│   ├── dashboard-powerbi-wash-cluster.md
│   ├── wash-cluster-newsletters-2024.md
│   └── sources-tierces.md
│
├── extraits/                   reproductions verbatim
│   ├── dashboard-wash-cluster-2025.md
│   ├── dashboard-wash-cluster-2025.png
│   ├── dashboard-water-page-unfiltered-2025.png
│   ├── page-35-profil-human-appeal.md
│   ├── page-74-lettre-adhesion.md
│   ├── page-75-coordination-team-unicef.md
│   ├── pages-8-10-instances-coordination.md
│   ├── liste-partenaires-2022.md
│   ├── HA-feedback-feb2024.md           ← HA self-report Feb 2024 (avant le claim 100M)
│   ├── HA-gaza-emergency-feedback-feb2024.pdf
│   ├── claims-water-cumulatif-2026.md   ← claims « 100M+ litres » mai 2026
│   ├── HA-palestine-country-page.md     ← page pays HA (admet plant shut down mai 2024)
│   └── claims-dates-presence-gaza.md    ← toutes les variantes de dates de présence Gaza
│
├── dashboard-scrape/           données extraites du dashboard Power BI
│   ├── README.md               méthodologie de l'extraction
│   ├── partners_raw.json       sortie brute du scraper (JSON)
│   ├── partners.csv            format long (partenaire × gouvernorat par ligne)
│   └── partners_wide.csv       format wide (partenaire par ligne, valeurs parsées + rangs)
│
└── scripts/                    code source de l'extraction
    ├── scrape-dashboard.py     scraper Playwright (JS-click direct)
    ├── analyze-partners.py     calcul de classements
    ├── build-wide-csv.py       génère partners_wide.csv depuis le JSON
    └── diagnose-slicer.py      diagnostic des stratégies de click sur le slicer
```

---

## Reproductibilité

Tout le matériel est public. Les sources primaires, le code de scraping et les données brutes sont dans ce repo. N'importe qui peut, en quelques minutes :

1. Ouvrir le dashboard WASH Cluster ([URL](dashboard-scrape/README.md))
2. Cliquer sur « HA » dans la slicer « Responsive Partners »
3. Lire les chiffres affichés (tooltip ou directement sur le pie chart / la carte)
4. Comparer aux autres partenaires en cliquant tour à tour
5. Reproduire les constats

Pour reproduire l'extraction automatique des 62 partenaires :

```bash
pip install playwright
playwright install chrome
python scripts/scrape-dashboard.py    # ~10 min
python scripts/build-wide-csv.py      # génère partners_wide.csv
python scripts/analyze-partners.py    # imprime les rangs
```

Le scraper imprime en fin de run une section « ANCRES DE VÉRIFICATION » qui doit afficher `✓ HA` et `✓ UNICEF` — sinon les données ne sont pas fiables.

---

## Avertissement

Travail de vérification factuelle indépendant, conduit du 22 au 23 mai 2026 à partir de sources publiquement accessibles. Aucun lien avec Human Appeal, le WASH Cluster, l'UNICEF, OCHA, ni avec aucune organisation politique ou religieuse. Toute correction documentée sera intégrée — voir [`corrections.md`](corrections.md) pour l'historique des erreurs déjà corrigées.

L'enquête traite **uniquement** de l'affirmation « 2ᵉ plus grand fournisseur d'eau ». Le statut juridique de Human Appeal (charity UK n° 1154288, sans enquête statutaire ouverte au moment de cette enquête) et les controverses politiques qui l'entourent sont **hors-sujet** pour cette question précise. Voir [`sources/sources-tierces.md`](sources/sources-tierces.md) pour le traitement de ces éléments.

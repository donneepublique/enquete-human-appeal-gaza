# Enquête : Human Appeal est-il vraiment le « 2ᵉ fournisseur d'eau à Gaza » ?

> Vérification factuelle d'une publicité Instagram de Human Appeal France affirmant que l'ONG est le « 2ᵉ plus grand fournisseur d'eau à Gaza » selon le WASH Cluster (UN-OCHA).

**Date :** 22 mai 2026
**Statut :** v4 — conclusion confirmée par extraction directe des données du dashboard cité par la pub.

---

## Synthèse en une page

La publicité fait deux affirmations distinctes :

| Affirmation | Statut | Pourquoi |
|---|---|---|
| Human Appeal est partenaire du WASH Cluster ONU pour Gaza | ✅ **Vrai** | Profil officiel page 35 du *WASH Cluster Partners' Profile, juillet 2022* (UNICEF / UN-OCHA) |
| Human Appeal est le **2ᵉ plus grand fournisseur d'eau** à Gaza | ❌ **Infirmé** | Les données du dashboard cité par la pub elle-même contredisent ce ranking |

**Le chiffre qui tue le slogan :** sur le dashboard WASH Cluster (page Water), Human Appeal a livré **~169 m³ d'eau** sur **152 390 m³** au total du cluster Gaza. C'est **0,11 %**. Sur 62 partenaires scrapés, environ 30 dépassent HA en volume.

---

## Démarche

1. **Identifier la source citée par la pub** : la pub utilise un visuel du dashboard public WASH Cluster (page Water).
2. **Lire ce que dit le dashboard sur HA** : tooltip user montre HA Khan Younis = 21,72 m³, HA Gaza = 90,87 m³, HA Middle Area = 48,17 m³.
3. **Comparer HA aux autres partenaires** : extraction par scraping Playwright des 62 partenaires Gaza. Voir [`dashboard-scrape/`](dashboard-scrape/).
4. **Conclure** : HA est un contributeur **marginal** (~0,1 % du volume cluster), pas un acteur de premier plan.

---

## Structure du dossier

```
enquete-human-appeal-gaza/
├── README.md                   ← ce fichier (synthèse + index)
├── methodologie.md             démarche, limites, biais
├── corrections.md              historique des erreurs (v1 → v4)
│
├── constats/                   les 6 constats détaillés
│   ├── 01-partenariat-cluster.md             ✅ Confirmé
│   ├── 02-instances-coordination.md          Membre simple
│   ├── 03-evolution-cluster-2022-2025.md     61 → 77 partenaires
│   ├── 04-ranking-2eme-fournisseur.md        ❌ INFIRMÉ
│   ├── 05-acronyme-HA-dans-pub.md            ✅ HA = Human Appeal
│   └── 06-contexte-juridique.md              Contesté
│
├── sources/                    description critique des sources
│   ├── README.md
│   ├── wash-cluster-partners-profile-2022.md
│   ├── wash-cluster-contingency-plan-2022.md
│   ├── ocha-rapports-2025.md
│   └── sources-tierces.md
│
├── extraits/                   reproductions verbatim
│   ├── dashboard-wash-cluster-2025.md
│   ├── dashboard-wash-cluster-2025.png
│   ├── page-35-profil-human-appeal.md
│   ├── page-74-lettre-adhesion.md
│   ├── page-75-coordination-team-unicef.md
│   ├── pages-8-10-instances-coordination.md
│   └── liste-partenaires-2022.md
│
├── dashboard-scrape/           extraction des données du dashboard PowerBI
│   ├── README.md               méthodologie de l'extraction
│   ├── partners.csv            62 partenaires × données par gouvernorat
│   └── partners_raw.json       sortie brute du scraper
│
└── scripts/                    code source de l'extraction
    ├── scrape-dashboard.py     scraper Playwright
    └── analyze-partners.py     calcul de classements
```

---

## Conclusion journalistique

**Sur le statut institutionnel** : Human Appeal *est* effectivement reconnu comme partenaire du WASH Cluster par les Nations Unies depuis 2022. Cela est documenté et vérifiable. La première version de cette enquête a contesté ce statut à tort ; voir [`corrections.md`](corrections.md).

**Sur le ranking « #2 »** : il est **infirmé par les données mêmes que la publicité référence visuellement**. Le dashboard Power BI du WASH Cluster montre Human Appeal comme un contributeur modeste (~0,1 % du volume d'eau du cluster), pas comme un acteur dominant.

**Sur la transparence publicitaire** : la pub crée une impression de caution onusienne en utilisant le visuel d'un tableau de bord ONU. Cette impression est **partiellement justifiée** (HA *est* membre du cluster) et **partiellement trompeuse** (le tableau de bord ne dit pas ce que la pub lui fait dire — au contraire, il le contredit).

**Pour le donateur** :
- ✅ Human Appeal est bien une ONG humanitaire reconnue par l'ONU pour Gaza
- ❌ Le chiffre « #2 » qui justifie le ton de la collecte n'est pas démontré, et le dashboard cité indique le contraire
- ❓ Les fonds passent partiellement via des partenaires intermédiaires locaux dont certains sont controversés (voir [Constat 6](constats/06-contexte-juridique.md))

---

## Reproductibilité

Tout le matériel est public. Les sources primaires, le code de scraping et les données brutes sont dans ce repo. N'importe qui peut :

1. Ouvrir le dashboard WASH Cluster ([lien](dashboard-scrape/README.md))
2. Cliquer sur "HA" dans la slicer
3. Lire les chiffres
4. Comparer aux autres partenaires
5. Reproduire les constats

C'est le principe de la vérification factuelle : pas asséner une vérité, mais documenter une démarche reproductible.

---

## Avertissement

Travail de vérification factuelle indépendant, conduit le 22 mai 2026 à partir de sources publiquement accessibles. Aucun lien avec Human Appeal, le WASH Cluster, l'UNICEF, OCHA, ni avec aucune organisation politique ou religieuse. Toute correction documentée sera intégrée.

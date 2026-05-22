# Constat 5 — Le « HA » du tableau de bord EST Human Appeal (démontré)

**Statut :** Démontré par scraping direct du dashboard
**Sources :** Dashboard Power BI public WASH Cluster, scraping Playwright des 62 partenaires Gaza

---

## Évolution du constat

| Version | Statut | Raison |
|---|---|---|
| v1-v3 | « Plausible non démontré » | Pas d'accès direct au dashboard |
| **v4** | **« Démontré »** | Extraction directe du dashboard confirme HA = Human Appeal |

---

## Démonstration

### 1. Le dashboard liste 62 partenaires sous forme d'acronymes

Liste complète extraite par scraping du dashboard (page Water, slicer Gaza) :

```
AAH, ACTED, AFSC, AH, AIOCP, ANERA, BLDA, CARE, CCP-Japan, CESVI, CMWU, CRS, 
DCA/NCA, DFD, FAFD, GDD, GEM, HA, HF, IDRF, IHH, IMC, IRC, IRW, IWWAA, MAAN, 
MAP-UK, MC, MECA, Mentor, MSF-F, MSF-OCB, MSF-S, NPA, NRC, OCK3, Other, Oxfam, 
PAEEP, PALSTD, PARC, PCRF, PEF, PFSA, Project HOPE, PSCF, PUI, PWJ, QRCS, RAHMA, 
SCI, SHAMS-OCD, SI, SIF, SOS, TDH, UAWC, UNDP, UNICEF, UNRWA, WCK, YDRO
```

Un seul partenaire utilise l'acronyme « HA ».

### 2. Vérification par les valeurs

Quand l'utilisateur a filtré le dashboard sur HA et lu le tooltip, il a obtenu :
- Khan Younis : 21,72 m³ (12,83 %)
- Gaza : 90,87 m³ (53,71 %)
- Middle Area : 48,17 m³ (28,47 %)
- Max people reached (max gouvernorat) : 15 138

Le scraping automatique a retrouvé exactement ces valeurs au slot étiqueté « HA » (à un décalage technique près — voir [méthodologie](../dashboard-scrape/README.md)).

### 3. Cohérence avec le profil UN-OCHA 2022

Le *WASH Cluster Partners' Profile, juillet 2022* (UN-OCHA / UNICEF) référence Human Appeal sous l'acronyme officiel **« HA »** (page 35). Cf. [Constat 1](01-partenariat-cluster.md) et [extrait page 35](../extraits/page-35-profil-human-appeal.md).

### 4. Règle d'unicité des acronymes dans les clusters humanitaires

Standard d'Information Management des clusters onusiens : deux organisations ne peuvent pas partager le même acronyme dans un même cluster (sinon les rapports 5W deviennent ambigus). Donc « HA » dans le dashboard 2025 désigne nécessairement Human Appeal.

---

## Implication

L'identification `HA = Human Appeal` dans le dashboard de la publicité **est démontrée**. Cela renforce le Constat 4 : **on peut lire les chiffres de Human Appeal directement sur le dashboard cité**, et ces chiffres ne correspondent pas à un 2ᵉ rang.

---

## Liens

- [Constat 1 : HA est partenaire du cluster](01-partenariat-cluster.md)
- [Constat 4 : ranking #2 infirmé](04-ranking-2eme-fournisseur.md)
- [Données scrapées](../dashboard-scrape/README.md)
- [Liste 2022 (acronyme HA déjà attribué)](../extraits/liste-partenaires-2022.md)

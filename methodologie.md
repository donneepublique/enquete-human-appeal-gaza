# Méthodologie de l'enquête

---

## Démarche

L'enquête répond à une question précise : *la publicité Instagram de Human Appeal France qui affirme que l'ONG est le « 2ᵉ plus grand fournisseur d'eau à Gaza » est-elle factuellement étayée ?*

Démarche en quatre temps :

1. **Identifier les sources qui pourraient valider ou invalider l'affirmation** : autorités onusiennes (OCHA, UNICEF, WASH Cluster), autorités réglementaires (UK Charity Commission), tiers indépendants (reporting journalistique).

2. **Récupérer les documents primaires** : Partners' Profile WASH Cluster, plans de contingence, OCHA updates.

3. **Lire chaque document en distinguant** ce qui est factuel (validé par l'auteur du document) de ce qui est auto-déclaré (transcrit sans validation).

4. **Conclure** sur la vérifiabilité de chaque sous-affirmation, en distinguant :
   - Ce qui est démontré
   - Ce qui est plausible mais non démontré
   - Ce qui est non vérifiable publiquement

---

## Hiérarchie d'autorité des sources utilisées

```
Force probante décroissante :

1. Documents primaires UN-OCHA / WASH Cluster
   (compilés et publiés sous responsabilité UNICEF ou OCHA)
   ↓
2. Filings publics auprès d'autorités statutaires
   (Charity Commission UK)
   ↓
3. Publications officielles UNICEF / WFP / UNRWA sur leurs propres sites
   ↓
4. Reporting journalistique indépendant
   (presse généraliste vérifiée)
   ↓
5. Communications NGO auto-publiées
   (qu'elles soient sur le site de l'ONG ou hébergées sur ReliefWeb)
   ↓
6. Think tanks et publications militantes
   (sources politiquement orientées : non reprises comme faits
    dans cette enquête ; mentionnées seulement pour signaler
    leur existence quand un débat public le justifie)
```

---

## Distinction clé : autorité institutionnelle vs auto-déclaration

C'est la distinction la plus importante de cette enquête.

Un document peut être **publié par une autorité institutionnelle** (UNICEF dans le cas du WASH Cluster Partners' Profile) tout en contenant des **contenus auto-déclarés** par des tiers (chaque profil partenaire est rédigé par l'ONG elle-même).

L'erreur fréquente — et celle que la pub de Human Appeal France semble exploiter — est de confondre :
- **« Publié par l'ONU »** (le document a une autorité institutionnelle)
- **« Validé par l'ONU »** (le contenu particulier de telle ou telle assertion a été audité par l'ONU)

Tout au long de l'enquête, j'ai cherché à expliciter quel niveau d'autorité s'applique à chaque assertion.

---

## Limites de l'enquête

### Limite 1 — Aucun contact avec les acteurs concernés

L'enquête s'appuie uniquement sur des sources publiquement accessibles en ligne. Aucune demande de commentaire n'a été adressée à :

- Human Appeal France
- Le focal point Gaza Human Appeal (fahmi.abushaaban@humanappeal.org.ps)
- Le WASH Cluster Coordination Team (mamro@unicef.org, ynassar@unicef.org)

Pour une enquête plus approfondie, ces contacts seraient l'étape suivante.

### Limite 2 — Pas d'accès aux données 5W brutes internes

Le WASH Cluster utilise un système 5W (Who-does-What-Where) pour collecter les contributions de chaque partenaire. Les **rapports 5W détaillés** (séries temporelles complètes, ventilation par activité) ne sont pas publics.

En revanche, le **dashboard Power BI public** du cluster (page Water) publie une **ventilation par partenaire** des deux métriques principales — volume d'eau (m³) délivré par gouvernorat et personnes touchées par gouvernorat. C'est cette ventilation publique qui permet à la v4 d'infirmer le ranking « 2ᵉ ». Voir [`constats/04`](constats/04-ranking-2eme-fournisseur.md).

### Limite 3 — Documents primaires datés

Le WASH Cluster Partners' Profile date de juillet 2022. Le plan de contingence date de novembre 2022. Les rapports OCHA de 2025 mentionnent l'existence d'un nouveau Partners' Profile mais celui-ci n'est pas accessible publiquement (au 22 mai 2026, recherches web).

### Limite 4 — Pas de vérification terrain

Cette enquête n'inclut aucune vérification terrain à Gaza, ce qui serait impossible sans accréditation humanitaire et accès au territoire.

### Limite 5 — Biais possibles de l'enquêteur

- Biais initial vers la défiance, qui a conduit à une **erreur factuelle dans la v1** (conclure trop vite que Human Appeal n'était pas dans la liste du cluster). Corrigée en v2.
- Cadre journalistique (« vérification factuelle ») qui privilégie le doute par défaut.
- Sources consultées principalement en anglais et en français — pas de presse arabophone consultée.

---

## Critères de la vérité factuelle utilisés

Une affirmation est considérée :

- **Confirmée** quand au moins une source primaire d'autorité (niveau 1-3 ci-dessus) l'établit explicitement.
- **Plausible non démontrée** quand des éléments la rendent crédible mais aucune source primaire ne l'établit explicitement.
- **Non vérifiable publiquement** quand aucune source publique ne permet de la confirmer ou de l'infirmer.
- **Contestée** quand des sources fiables se contredisent.
- **Infirmée** quand une source primaire d'autorité l'écarte explicitement.

---

## Reproductibilité

L'ensemble des sources est listé avec URL dans [`sources/README.md`](sources/README.md). Toute personne ayant accès à Internet peut, en quelques heures, refaire le parcours de cette enquête et soit confirmer les constats, soit en formuler une critique documentée.

C'est le principe de la vérification factuelle : non pas asséner une vérité, mais documenter une démarche que d'autres peuvent reproduire et challenger.

---

## Voir aussi

- [Sources](sources/)
- [Corrections](corrections.md)

# Constat 7 — Le claim « Over 100 million litres of clean drinking water delivered » est non démontré et incompatible avec le record officiel du WASH Cluster

**Statut :** Non démontré ; structurellement incompatible avec l'enregistrement officiel du WASH Cluster pour HA en 2025 (facteur ~180×).
**Sources principales :**
- Pages publiques Human Appeal UK / USA (mai 2026) — voir [extraits/claims-water-cumulatif-2026.md](../extraits/claims-water-cumulatif-2026.md)
- Rapport Human Appeal *Gaza Emergency Appeal Update*, février 2024 — voir [extraits/HA-feedback-feb2024.md](../extraits/HA-feedback-feb2024.md)
- Rapport Human Appeal *One Year On Gaza Humanitarian Impact Report*, octobre 2024
- Dashboard Power BI WASH Cluster State of Palestine, **Flash Appeal Indicators 2025**, *« As of 04 November »* — voir [extraits/dashboard-water-page-unfiltered-2025.png](../extraits/dashboard-water-page-unfiltered-2025.png)

---

## Le claim revendiqué publiquement

Trois pages Human Appeal portent un volume cumulé d'eau livrée à Gaza depuis octobre 2023. Les chiffres diffèrent selon le site :

| Source HA | Chiffre | Période |
|---|---|---|
| UK — appeals/gaza-emergency-appeal | **« Over 102 million litres of clean drinking water delivered »** | « since October 2023 » |
| USA — donate/projects/.../gaza-water | **« 114 068 000 liters of clean water delivered »** | « Since 2023 » |
| USA — news 13 mai 2026 | **« More than 100 million litres of clean water have been delivered »** | « since October 2023 » |

Voir [reproduction verbatim](../extraits/claims-water-cumulatif-2026.md).

L'écart entre les versions UK et USA pour la même période = **~12 millions de litres**. Ce désaccord interne est déjà un signal.

---

## Ce que le WASH Cluster enregistre pour HA

Le **dashboard officiel du WASH Cluster State of Palestine**, intitulé *« Flash Appeal Indicators 2025 »*, daté *« As of 04 November »*, indique en pied de page :

> *« Creation date: February 2025 — Sources: Partners reporting — Feedback : mohahussein@unicef.org »*

(Mohammad Hussein est le *WASH Cluster Information Management Officer* identifié page 75 du *WASH Cluster Partners' Profile 2022* — c'est l'autorité officielle qui compile les 5W partenaire-par-partenaire pour le cluster.)

**Période couverte par le dashboard** : du 1ᵉʳ janvier 2025 au 4 novembre 2025 = **277 jours ≈ 9,1 mois**. Le barchart « New Direct Beneficiaries Reached by Month » confirme cette plage (Jan → Oct visibles).

**Pour Human Appeal, le dashboard enregistre** (lecture tooltip + scraping confirmés) :

| Métrique | Valeur HA |
|---|---|
| Volume m³ d'eau délivré (somme gouvernorats) | **~169 m³** |
| Volume m³ d'eau délivré, en litres | **~169 000 litres** |
| Part de HA dans le cluster | **0,11 %** |
| Rang de HA dans le cluster (62 partenaires) | **#42 par m³, #48 par max_people** |

---

## Confrontation du claim public au record cluster

Pour comparer les deux chiffres dans la même fenêtre temporelle, on normalise le claim public par mois :

| | Volume | Période | Rate mensuel |
|---|---|---|---|
| Claim HA UK | 102 000 000 L | Oct 2023 → mai 2026 (≈ 31 mois) | **3 290 000 L/mois** |
| Claim HA USA | 114 068 000 L | Idem | **3 680 000 L/mois** |
| Record WASH Cluster 2025 | 169 000 L | Jan → 4 nov 2025 (≈ 9,1 mois) | **18 300 L/mois** |

**Ratio claim public / record cluster** : **180× (UK) à 200× (USA)**.

Autre formulation, prêté à HA la même rate que son claim revendique sur 31 mois :
- Si HA livrait au rythme implicite de son claim (≈ 29 940 m³ pour 9,1 mois), cela représenterait **20 % du volume total que le cluster entier (62 partenaires) déclare avoir délivré en 2025**. C'est-à-dire que HA, seul, aurait livré un cinquième de ce que les 62 partenaires (dont UNICEF, UNRWA, Oxfam, etc.) reportent ensemble. **Le dashboard cité par la pub elle-même contredit cette projection.**

---

## Évolution des claims dans le temps

Le claim « 100M+ litres » n'apparaît dans aucune communication HA antérieure. Comparaison de trois moments :

### Février 2024 — *Gaza Emergency Appeal Update*

Le rapport HA compte des **bénéficiaires**, pas des volumes (voir [extrait](../extraits/HA-feedback-feb2024.md)) :

| Métrique | Valeur |
|---|---|
| Bénéficiaires « tanks of clean water » | 19 660 personnes |
| Bénéficiaires « water from our desalination plant » | 30 000 personnes |
| Capacité plant | 52 000 L/h (inchangé jusqu'à 2026) |
| Volume cumulé eau livrée | **absent du document** |

### Octobre 2024 — *One Year On Gaza Humanitarian Impact Report*

Conçu pour célébrer 12 mois d'action depuis le début de la guerre. Seule métrique eau citée :

> *« Ongoing clean water distribution using water tanker trucks with a capacity of 36,500 litres per day »*

**Aucun volume cumulé n'y est revendiqué.** Capacité quotidienne uniquement.

### Mai 2026 — claim cumulé apparaît

Sur les trois pages mentionnées en début de constat : « Over 102 million litres » / « 114 068 000 liters » / « More than 100 million litres ».

**Le saut narratif est notable** : passage de comptes de bénéficiaires (Feb 2024) puis de capacité quotidienne (Oct 2024) à un volume cumulé exprimé en millions de litres (May 2026), sans publication intermédiaire qui documenterait la progression du chiffre.

---

## Borne physique théorique

La capacité **stated** de HA pour Gaza est :
- **Plant de désalinisation** : 52 000 L/h
- **Water tanker trucks** : 36 500 L/jour

Sur 31 mois (Oct 2023 → mai 2026) :

| Source | Production max (24/7) | Uptime nécessaire pour 102M L |
|---|---|---|
| Plant 24/7 sur 31 mois | ~1 178 000 000 L (1,18 milliard) | **~8,7 %** (soit ~2 h/jour) |
| Trucks 24/7 sur 31 mois | ~34 400 000 L | n'atteint pas 102M L même à 100 % |

Le claim « 102M+ litres » est donc **physiquement plausible** si la plant fonctionne ne serait-ce que ~2 heures/jour en moyenne sur 31 mois. Il n'est **pas physiquement impossible**.

Cependant : la plant est explicitement décrite (Feb 2024) comme dépendante du **fuel UNRWA** et OCHA documente que les partenaires WASH ont reçu en décembre 2024 seulement **12 % du carburant minimum nécessaire**. Le taux d'uptime de 8,7 % requis pour atteindre 102M L est donc à confronter à une contrainte d'approvisionnement énergétique sévère, dont aucune source publique ne permet de mesurer l'effet net.

---

## Pourquoi le cluster ne « voit » pas ces volumes

Le rapport Feb 2024 fournit la clé probable :

> *« This sustainable source of water is delivered to the local water network »*

Une fois injectée dans le réseau municipal, l'eau n'est plus attribuée à HA dans le **5W (Who-does-What-Where)** du WASH Cluster — elle est comptabilisée par le PWA / CMWU (opérateur réseau). Le 5W partenaire-par-partenaire compte principalement les **livraisons directes** par camions, points d'eau opérés, etc.

C'est une **hypothèse plausible** qui réconcilierait :
- une production effective de la plant dans la fourchette physiquement plausible,
- le record cluster de 169 m³ pour HA en 2025 (qui ne couvre que les livraisons directement attribuables à HA).

Mais cette réconciliation est précisément ce qui invalide l'argument promotionnel : **HA invoque l'autorité du WASH Cluster pour étayer son ranking (« 2ᵉ fournisseur ») et son volume (« 100M+ litres »), alors que la métrique du cluster ne comptabilise pas ces volumes injectés en réseau**. HA ne peut pas avoir le beurre et l'argent du beurre.

---

## Statut du claim

| Question | Réponse |
|---|---|
| Le chiffre « 100M+ litres » est-il indépendamment vérifiable ? | **Non.** Aucun audit, aucun document tiers, aucun rapport ONU ne le confirme. |
| Est-il physiquement plausible ? | **Oui, ~9 % d'uptime suffit.** Mais non démontré. |
| Le WASH Cluster (que HA invoque) atteste-t-il ce volume ? | **Non.** Le record cluster pour HA en 2025 est 169 m³ (~0,17M L), soit ~180× moins que le rate impliqué par le claim. |
| Le claim était-il présent dans la communication initiale ? | **Non.** Absent en Feb 2024 et en Oct 2024 (« One Year On »). Apparaît à partir de 2025-2026. |
| Le claim est-il interne cohérent ? | **Non.** Trois pages HA en mai 2026 donnent trois chiffres différents (102M, 114M, « more than 100M »). |

---

## Implication pour le donateur

Quand HA présente un visuel du dashboard WASH Cluster pour étayer sa communication sur Gaza :
- ✅ HA est bien membre du cluster (Constat 1)
- ❌ Le dashboard ne contient ni le ranking « 2ᵉ » (Constat 4) ni le volume « 100M+ litres » (ce Constat 7)
- ❓ La production réelle de la plant + tanks n'a aucune attestation indépendante

Le visuel WASH Cluster est utilisé pour donner une caution institutionnelle à des chiffres que cette même source ne soutient pas. C'est le même mécanisme rhétorique que celui identifié dans le Constat 4, appliqué à une autre métrique.

---

## Liens

- [Extrait — claims cumulés mai 2026](../extraits/claims-water-cumulatif-2026.md)
- [Extrait — rapport HA Feb 2024](../extraits/HA-feedback-feb2024.md)
- [Source — dashboard Power BI WASH Cluster](../sources/dashboard-powerbi-wash-cluster.md)
- [Constat 4 — ranking « 2ᵉ » infirmé](04-ranking-2eme-fournisseur.md)

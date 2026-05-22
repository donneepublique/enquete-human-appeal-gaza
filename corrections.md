# Corrections — historique des erreurs identifiées et corrigées

Ce fichier documente les erreurs factuelles présentes dans les versions antérieures de l'enquête, par souci de transparence méthodologique.

---

## v1 → v2 (22 mai 2026)

### Erreur identifiée

**v1 affirmait :** « Human Appeal n'apparaît pas dans la liste officielle des partenaires WASH Cluster ».

**Cette affirmation était fausse.**

### Source de l'erreur

La v1 s'appuyait uniquement sur le *Gaza WASH Contingency Plan* de novembre 2022 (annexe 9.3 « WASH Implementing Partners » qui liste 26 organisations). Human Appeal n'y figure pas → conclusion (à tort) que HA n'est pas membre du cluster.

**Pourquoi cette source ne suffisait pas :** l'annexe 9.3 est une **liste opérationnelle restreinte** des partenaires budgétisés pour les scénarios de contingence. Pas le registre des membres.

### Source correcte

Le document de référence est le **WASH Cluster Partners' Profile, juillet 2022** (UN-OCHA / UNICEF). Page 35 : profil officiel de Human Appeal.

### Identification

Par une question du user : *« mais 2022 ils peuvent dire que c'est dans la rapport plus recents? existent ils ? »* — qui m'a poussé à élargir au-delà du seul plan de contingence.

---

## v2 → v3 (22 mai 2026, même jour)

### Évolution structurelle

Passage d'un seul README à un dossier journalistique multi-fichiers (constats/, sources/, extraits/, méthodologie, corrections).

Aucun constat factuel modifié — uniquement approfondissement.

---

## v5 → v6 (23 mai 2026)

### Scraper corrigé — attribution fiable, 62/62 partenaires

**v5 affirmait :** « ~5 lignes du scrape ont une étiquette décalée ; on raisonne par valeurs pour rester robuste à ce décalage. »

**v6 corrige la cause** : le décalage ne venait pas d'un timing PowerBI mais des méthodes de click Playwright (`.get_by_text().click()`, `.locator().click()`, `page.mouse.click(x,y)`) qui ratent toutes d'une ligne sur ce slicer Power BI virtualisé et sélectionnent l'item juste au-dessus de celui visé. Seul un `element.click()` JavaScript direct sur le `.slicerItemContainer` exact donne la bonne sélection.

### Identification

Une objection du user : *« non mais c'est quoi c'est connerie de decalage encore? les valeurs HA réelles (15 138) apparaissent sous l'étiquette IDRF, les valeurs UNICEF sous UNRWA »*. Le constat correct : on ne peut pas publier un ranking dont l'attribution est buggée et se cacher derrière un raisonnement value-based.

### Méthode du fix

1. Un script `diagnose-slicer.py` qui clique « HA » par 4 stratégies et vérifie laquelle sélectionne réellement HA (via aria/classes/bg du DOM du slicer).
2. Résultat : seul `js_click_by_index` (= `document.querySelectorAll('.slicerItemContainer')[idx].click()`) sélectionne le bon item. Toutes les méthodes Playwright sélectionnent l'item juste au-dessus.
3. Réécriture du scraper avec cette stratégie + vérification des ancres HA et UNICEF en fin de run.
4. Run final : 62/62 captures valides, les deux ancres matchent exactement.

### Chiffres mis à jour

- Avant (v5) : HA entre rang 42 et 48 sur 62 (intervalle dû aux clicks ratés)
- Maintenant (v6) : **HA rang 48 sur 62 par max_people**, **rang 42 sur 62 par total m³** (valeurs exactes)
- UNICEF n°1 confirmé sur les deux métriques (940 560 max_people, ~35 460 m³)

La conclusion principale (« infirmé ») est inchangée — mais les chiffres sont maintenant tirés d'une attribution fiable et non d'un raisonnement contournant le bug.

### Principe en jeu

Une analyse value-based qui contourne un bug d'attribution est moins défendable qu'une analyse standard sur des données dont l'attribution est correcte. Quand on peut corriger le bug, on corrige le bug.

### Constat 6 supprimé

Le Constat 6 (« Statut juridique et modèle opérationnel ») a été **retiré de l'enquête**. Raison : il était hors-sujet par rapport à la question précise traitée — le statut administratif de Human Appeal (charity UK n° 1154288, sans enquête statutaire) et son recours à des partenaires locaux **n'invalident ni ne valident** le ranking « 2ᵉ fournisseur d'eau ». Le fichier précisait d'ailleurs lui-même cette absence de pertinence.

Les éléments factuels utiles (numéro de charity, absence d'enquête, traitement des sources partisanes) restent référencés dans [`sources/sources-tierces.md`](sources/sources-tierces.md). Conserver un constat hors-sujet — même soigneusement neutre — affaiblissait la lisibilité de l'enquête en suggérant que le statut juridique faisait partie des éléments à charge contre HA. Il ne l'a jamais été.

---

## v4 → v5 (22 mai 2026, même jour)

### Révision de cohérence

Trois types de corrections ont été apportées en v5 sans changer la conclusion principale :

**1. Contradictions internes résolues**

- `methodologie.md` Limite 2 indiquait que la position « 2ᵉ » de HA n'est « ni vérifiable ni infirmable » à défaut des données 5W, ce qui contredisait la conclusion v4. Reformulée : les rapports 5W bruts ne sont pas publics, mais la ventilation par partenaire **est** publiée sur le dashboard Power BI (qui suffit à infirmer le ranking).
- `constats/03` affirmait que la ventilation par partenaire « n'est pas publiée », ce qui contredisait également la v4. Reformulée pour pointer vers le dashboard.

**2. Allégations non strictement assurées retirées (Constat 6)**

Le Constat 6 reprenait des allégations du **Middle East Forum** (transferts vers l'« Islamic Zakat Society », caractérisation « proxy Hamas », réseau « Union of Good »). Ces allégations émanent d'une **source partisane**, ne sont **pas confirmées** par une autorité judiciaire ou réglementaire, et la Charity Commission UK n'a pas ouvert d'enquête statutaire.

La règle « ne reprendre que des faits strictement assurés » impose de ne **pas** les reproduire comme faits. Le Constat 6 a été réécrit pour conserver uniquement :
- le statut juridique vérifié (charity UK n° 1154288, enregistrée en mai 2014, absence d'enquête statutaire),
- le modèle opérationnel via partenaires locaux (documenté dans le profil WASH Cluster lui-même),
- la mention que des controverses existent, sans les reprendre comme faits.

Les chiffres précis (« 4,7 M£ depuis 2020 », « ~90 M£ revenus FY 2024 ») ont aussi été retirés faute de pouvoir les vérifier ligne-à-ligne dans les comptes annuels — le renvoi vers le registre Charity Commission est plus honnête.

**3. Classement consolidé par valeur (Constat 4)**

Le classement précédent disait « environ 30 partenaires dépassent HA en volume ». Cette formulation reposait sur les étiquettes du scraper, dont la fiabilité est imparfaite (~5 lignes décalées). Une analyse par **valeurs capturées** (indépendante des étiquettes) donne un chiffre plus précis et plus robuste :
- **41 sur 56 captures réussies dépassent HA** en max people reached
- **36 sur 56 captures réussies dépassent HA** en m³ délivré
- HA est entre le **rang 42 et 48 sur 62** (selon ce que sont les 6 clicks ratés)
- UNICEF est confirmé n°1 (aucune capture ne dépasse 940 560)

La conclusion reste la même mais avec une borne précise. La méthode est aussi plus défendable car elle ne dépend pas du mapping étiquette → ONG.

---

## v3 → v4 (22 mai 2026, même jour)

### Mise à jour majeure du Constat 4 — ranking « #2 »

**v3 statuait :** « Non vérifiable publiquement » (le WASH Cluster ne publie pas de ranking par partenaire).

**v4 statue :** « **Infirmé par les données du dashboard cité par la pub elle-même** ».

### Pourquoi cette mise à jour

Le user a trouvé que le dashboard cité dans la pub est public et permet de filtrer par partenaire. Il a lu un tooltip qui confirme que Human Appeal délivre seulement **~169 m³** sur **152 390 m³** du cluster (= 0,11 %).

Pour confirmer que HA n'est pas le 2ᵉ sur la métrique m³, j'ai écrit un scraper Playwright qui clique sur chaque partenaire dans la slicer du dashboard et lit les valeurs. Résultat : sur 62 partenaires, environ 30 dépassent HA en volume.

### Erreur intermédiaire

Dans mon analyse, j'ai d'abord lu les chiffres HA comme « 160 000 m³ » au lieu de « 160 m³ » (mauvaise interprétation du format de nombre français : la virgule est décimale, pas séparateur de milliers). Le user m'a corrigé : *« c'est 21,72 a khan younis pas 21K »*. Sans cette correction, je serais arrivé à une conclusion fausse.

### Limites résiduelles de la v4

- Le scraper a un problème de timing pour ~6 partenaires sur 62 (étiquettes décalées d'une ou deux positions). **Les valeurs sont réelles**, les labels parfois bancals.
- Le mapping `acronyme dashboard → nom complet` reste incertain pour certains partenaires (OCK3, GDD, GEM, PAEEP, etc.).
- Une métrique alternative (capacité installée, financement levé, etc.) pourrait classer HA différemment — mais ce serait à HA de produire cette pièce.

---

## Principe méthodologique

> Une enquête factuelle qui se corrige publiquement est plus fiable qu'une enquête qui défend ses premières conclusions. La transparence sur les erreurs n'invalide pas le travail — elle le valide.

Cette enquête a vu trois inversions de conclusion notables et une révision de cohérence :
- v1 → v2 : « HA pas dans cluster » devient « HA est dans le cluster »
- v3 → v4 : « ranking #2 non vérifiable » devient « ranking #2 infirmé »
- Lecture de chiffres : « HA = 160K m³ » devient « HA = 160 m³ »
- v4 → v5 : retrait des allégations partisanes non strictement assurées ; classement value-based plus précis

Les trois premières ont été déclenchées par une **objection du user**. La quatrième par une **demande explicite de relecture critique** de tous les points. C'est précieux à noter : un enquêteur seul aurait probablement maintenu ses premières conclusions et conservé des points faiblement étayés au nom de « la nuance ».

---

## Voir aussi

- [Méthodologie](methodologie.md)
- [Constat 4 (la conclusion principale, mise à jour)](constats/04-ranking-2eme-fournisseur.md)
- [Extraction du dashboard](dashboard-scrape/README.md)

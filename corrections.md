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

Cette enquête a vu trois inversions de conclusion notables :
- v1 → v2 : « HA pas dans cluster » devient « HA est dans le cluster »
- v3 → v4 : « ranking #2 non vérifiable » devient « ranking #2 infirmé »
- Lecture de chiffres : « HA = 160K m³ » devient « HA = 160 m³ »

Chaque correction a été déclenchée par une **objection du user**, pas par une introspection. C'est précieux à noter : un enquêteur seul aurait probablement maintenu les premières conclusions.

---

## Voir aussi

- [Méthodologie](methodologie.md)
- [Constat 4 (la conclusion principale, mise à jour)](constats/04-ranking-2eme-fournisseur.md)
- [Extraction du dashboard](dashboard-scrape/README.md)

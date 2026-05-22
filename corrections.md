# Corrections — historique des erreurs identifiées et corrigées

Ce fichier documente les erreurs factuelles présentes dans les versions antérieures de l'enquête, par souci de transparence méthodologique.

---

## v1 → v2 (22 mai 2026)

### Erreur identifiée

**v1 affirmait :** « Human Appeal n'apparaît pas dans la liste officielle des partenaires WASH Cluster ».

**Cette affirmation était fausse.**

### Source de l'erreur

La v1 s'appuyait uniquement sur le *Gaza WASH Contingency Plan* de novembre 2022, dont l'annexe 9.3 « WASH Implementing Partners » liste 26 organisations. Human Appeal n'y figure pas, ce qui a conduit (à tort) à la conclusion que Human Appeal n'était pas membre du cluster.

**Pourquoi cette source ne suffisait pas :**
L'annexe 9.3 du plan de contingence est une **liste opérationnelle restreinte** des partenaires qui ont déclaré disposer de capacités budgétisées pour les 4 scénarios de contingence (eau, hygiène, latrines, etc.). Ce n'est **pas** le registre des membres du cluster.

### Source correcte

Le document de référence pour la liste des membres du cluster est le **WASH Cluster Partners' Profile, juillet 2022** (UN-OCHA / UNICEF). Dans ce document :

- Page 35 : profil officiel de Human Appeal (HA) avec adresse Gaza, focal point, et programme WASH déclaré
- Page 6 : logo Human Appeal sur la planche visuelle des 61 partenaires 2022

### Comment l'erreur a été identifiée

Par une question méthodologique de l'interlocuteur de cette enquête :

> *« mais 2022 ils peuvent dire que c'est dans la rapport plus recents? existent ils ? »*

Cette question a conduit à élargir la recherche au-delà du seul plan de contingence, à découvrir le Partners' Profile (publié au même moment, juillet/août 2022, mais à un autre endroit), et à identifier la véritable position de Human Appeal.

### Corrections appliquées

Tous les constats de la v2 prennent en compte le fait que Human Appeal est bien un partenaire reconnu du cluster.

Le constat principal a été **inversé** : passe de *« Human Appeal n'est pas dans la liste officielle »* (faux) à *« Human Appeal est un partenaire officiel du WASH Cluster »* (vrai).

Le constat secondaire est **renforcé** : *« Le ranking #2 n'est pas vérifiable publiquement »* reste valable, et c'est désormais le cœur de l'enquête.

### Commit GitHub

Voir le commit `fa3d013` sur https://github.com/donneepublique/enquete-human-appeal-gaza qui matérialise cette correction.

---

## v2 → v3 (22 mai 2026, même jour)

### Évolution structurelle

La v2 tenait dans un seul fichier README.md. La v3 restructure l'enquête en dossier journalistique :

- Un README synthèse + index
- Un dossier `constats/` avec 6 constats détaillés
- Un dossier `sources/` avec description critique de chaque source
- Un dossier `extraits/` avec reproductions verbatim des passages clés
- Des fichiers `methodologie.md` et `corrections.md`

### Ce qui change

Les constats sont approfondis (plus de citations verbatim, plus de comparaisons inter-partenaires, plus de distinction entre statut institutionnel et auto-déclaration).

Aucun constat factuel n'a été modifié — seule la mise en forme évolue.

---

## Principe méthodologique

> Une enquête factuelle qui se corrige publiquement est plus fiable qu'une enquête qui défend ses premières conclusions. La transparence sur les erreurs n'invalide pas le travail — elle le valide.

---

## Voir aussi

- [Méthodologie](methodologie.md)

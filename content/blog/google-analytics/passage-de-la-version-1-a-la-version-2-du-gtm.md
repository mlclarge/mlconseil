---
title: "Gestionnaire de balises Google : l'essentiel sur la dernière version (2)"
date: 2015-01-12
author: "admin"
categories: ["Google Analytics"]
tags: []
slug: "passage-de-la-version-1-a-la-version-2-du-gtm"
---

Après cette avoir évoqué brièvement dans la [revue google analytics de la semaine dernière](https://www.mauricelargeron.com/les-principaux-changements-de-google-analytics-en-2014/) l’évolution du **gestionnaire de balise**, j’y reviens plus dans le détail aujourd’hui, vu la nette amélioration de cet l’outil de tracking. Je rappelle que ce **TMS** (tag management system)   permet de centraliser l’ensemble des  marqueurs pour un site internet afin d’assurer  un suivi d’audience simplifié et donc accessible aux  développeurs web bien sûr mais aussi aux **professionnels du webmarketing** (marketeurs, chef de projet...).  Depuis mi-octobre dernier, la version google tag manager s’est paré de nouveaux apparats ! Alors n’attendons plus et examinons ses spécificités, les éléments pour une migration V1 vers V2,  et la pose d’une balise en 4 clics !

## **Nouveautés de la version V2**

Tout d’abord, sachez que courant janvier 2015, les possesseurs d’un compte tag manager verront leur compte migrer d’office vers le nouvelle version. Pour les plus pressés, le chapitre suivant indique comment migrer un compte v1 vers v2. Notons également que le GTM V2 n’est disponible qu’ en Anglais à ce jour...

[![nouvelle-version-310x205.jpg](/images/blog/nouvelle-version-310x205.jpg) Interface GTM V2 épurée..

	- **Interface intuitive** : ok, facile à dire, mais c’est vraiment le cas. Pour avoir tester la V1, cette dernière apparaît désormais comme vraiment pas pratique pour le non développeur. La V2 adopte le design des workflows que l’on peut retrouver dans google adwords ou analytics, avec ce principe de chemins visuel, marqué par des étapes validées.

	- **Intitulés** : la notion de règle est remplacée par trigger (déclencheurs) et celle de macro par variables. Ici, la logique reste la même seulement ce nommage colle davantage à la réalité.

### *Fonctionnalités*

[![variables-integrees-gtm-310x189.jpg](/images/blog/variables-integrees-gtm-310x189.jpg) Variables pré-installées gtm v2

	- **Déclencheur** : tout  "trigger" est muni d’un “event” (sur page vue ou clic sur un lien par ex.) .Ne pas confondre  cette notion d’évènement,  avec celui du modèle de data  de GA pour installer un évènement sur objet particulier (catégorie, action,libellé, valeur).

	- **Variables intégrées** : Une nouveau choix de catégorie est embarqué muni de  variables pré-activées, non modiables. Ce qui n’empêche pas la création de variables personnalisées bien sûr. Le bénéfice de cette amélioration est double, moins de configuration basique à faire, et disponibilité transversale une fois une variable cochée : Plus d’infos ici [https://support.google.com/tagmanager/answer/6106965](https://support.google.com/tagmanager/answer/6106965)

	- **Auto-event tracking** : grandement simplifié ! Plus besoin de construire une balise “gtm.Click” en amont lors de la pause d’un écouteur de clic, il suffit simplement d’ajouter le “trigger” du genre “Click” est le tour est joué !

	- **Api** : une interface de programmation pour les développeurs est accessible désormais.

## **Migration d’un compte GTM v1 vers Version 2**

L’objectif ici est de migrer un compte muni d’un container GTM-XXXX v1 vers la nouvelle interface.

[![processus-310x210.jpg](/images/blog/processus-310x210.jpg) Migration V1 vers V2

Rien de compliquer ici, il suffit d’utiliser depuis l’ancienne interface le lien du menu de gauche export  :

	- Se loguer sur la V2

	- Créer un compte sur la V2 pour accueillir l’import du code du container de la V1

	- Télécharger au format Json en local le code V1.

	- Basculer à  nouveau vers la nouvelle interface (grâce à un lien situé en haut à droite)

	- Importer depuis la V2 le fichier précédemment downloadé depuis le menu haut “Admin”

	- Écraser (tout basculer sur les nouveaux modèles de variables) ou fusionner (conserver les anciens paramétrages v1) : au choix, je suis conservateur, j’ai fait le choix de fusionner.

	- Confirmer le choix  précédent (donc on ne peut pas se tromper)

[![migratin-tag-manager-v1-v2-310x151.jpg](/images/blog/migratin-tag-manager-v1-v2-310x151.jpg) Processus de Migration

***Avertissements ***

	- Ne pas oublier de changer le numéro du container V2 et de publier cette nouvelle version.

	- Des erreurs à l’importation peuvent subvenir, cela est dû bien souvent à la variable existante “tableau de conversion” non mise à jour dans la V1.

## **Exemple de Marquage dans la nouvelle version GTM V2**

L ‘idée ici de faire un petit tour rapide sur un paramétrage lambda comme celui d’une balise de remarketing adwords. Ce qui frappe ici  c’est vraiment la simplicité d’utilisation par le chemin tracé par le didacticiel de configuration

[![marquage-pas-à-pas-goolge-tag-manager-v2-158x300.jpg](/images/blog/marquage-pas-à-pas-goolge-tag-manager-v2-158x300.jpg) Marquage pas à pas google tag manager v2

En 4 clics, ou presque pour créer une balise (illustration : le marquage d’une balise de remarketing  sur un site web)

	- 1-Choisir la balise Google Adwords  prête à l’emploi (template)

	- 2-Opter pour la version (conversion ou remarketing)

	- 3-Indiquer les conditions du déclenchement le tag (filtre de choix : toutes pages, 1 page en particulier ) avec exceptions possibles (blocage si...)

	- 4-Paramétrer l'identification de la balise (Id donné par Adwords) avec éventuellement ajout de paramétrages d’intégration avancé pour le codage dans la page (dataLayer personnalisé, extraction de data :clé -valeurs)

	- 5-Valider et publier

	- Merci à [http://www.tatvic.com/webinars/](http://www.tatvic.com/webinars/) pour leur série de webinars sur Google analytics et en particulier sur GTM

https://www.youtube.com/watch?v=wwEXxpXsmoE
## **Sources annexes d’informations**

**Api : ****[https://support.google.com/tagmanager/answer/4605576?hl=fr](https://support.google.com/tagmanager/answer/4605576?hl=fr)**
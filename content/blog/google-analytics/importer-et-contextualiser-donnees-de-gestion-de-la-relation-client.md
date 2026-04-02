---
title: "Analyse d'audience  & Crm dans Google analytics"
date: 2015-11-23
author: "admin"
categories: ["Google Analytics"]
tags: []
slug: "importer-et-contextualiser-donnees-de-gestion-de-la-relation-client"
image: "/images/blog/google-analytics-et-connais.jpg"
---

En quoi **Google analytics** peut aider le marketing manager à enrichir [la relation client](https://fr.wikipedia.org/wiki/Gestion_de_la_relation_client) et faire d’une donnée d’audience une valeur transversale qui participe à la construction d’un profil 360 ? Quelle fonctionnalité  permet  d’enrichir une donnée anonyme collectée par GA ? Sur quel indicateur se baser ? Avec quelle méthode ? Pour produire quel type de rapport **webmarketing**  ?

## **Principes d’élaboration d’un suivi d’audience orienté client**

Un petit schéma d'ensemble pour se situer le contexte de la **collecte orientée client.**

 	- Définir  le choix de la variable représentative de l'userid à intégrer dans GA

 	- Développement web sur la méthode pour pousser cette variable pour Ga

 	- Paramétrages de la vue dédiée G. Analytics

 	- Création de dimensions personnalisées afin d'améliorer le suivi comportemental centrée sur l'utilisateur (vs visiteur).

 	- Collecte et remontée dans Ga des appels

 	- Importation des Métadonnées Crm liées à l'[userid ](https://www.mauricelargeron.com/parametrer-un-suivi-d-audience-multi-appareils/)(dim. perso.)

 	- Création des rapports personnalisés

[![Image](/images/blog/schema-processus-de-collecte-userId-310x33.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2015/11/schema-processus-de-collecte-userId.jpg) Processus de collecte data client
## **Eliminer les biais du marquage natif de GA sur la notion de  « visiteur »**

### *Représentation d’un utilisateur unique (au lieu d’un device)*

Notez que nativement, le script analytics.js dépose  lors d’une visite un  cid (clientid)  attaché à un navigateur, d’où les biais dans le comptage de visiteurs (même device avec 3 navigateurs = 3 visiteurs différents).

Alors comment avoir une vue plus proche de la réalité ? L’intégration d’une variable transversale attachée au visiteur , puis portée au moment de son authentification.

[![Image](/images/blog/userId-et-cid-310x201.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2015/11/userId-et-cid.jpg) UserId (uid ) et cid

Google  a donc tout prévu même s’il interdit la collecte de donnée personnalisée au sein de son application avec la fonctionnalité Uid autrement dénommée d’userId. Cette dernière  a pour finalité  de faire du suivi cross devices,  au lieu d’un tracking unique par appareil, malin  :) .

Je rappelle que les conditions de ce suivi réclament que **le client soit logué sur le site de l’éditeur** et que la génération de cet userid soit générée par le système d’information de la propriété (domaine).

En termes de développement, plusieurs choix sont envisageables pour créer cette variable d’identification.

 	- Récupérer l’id du client depuis la base de données du site ecommerce disponible pour GA comme uid.

 	- Générer un id à la volée, à chaque connexion authentifiée qui se met à jour selon une fonction conditionnelle basé sur un cookie (si existant alors ,Vs si pas existant alors)

 	- Utiliser une variable issue d’une base crm qui sera poussée lors d’une authentification de session par le visiteur (api).

Le résultat de cette collecte s’effectue  dans une vue dédiée « userId »  prévue à cet effet. Les chemins de conversion d’un utilisateur qui utiliserait plusieurs appareils pour enfin convertir deviennent lisibles mais agrégés et anonymes.

[![Image](/images/blog/chevauchement-vue-userId-289x300.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2015/11/chevauchement-vue-userId.jpg) Chemin conversion et Chevauchement Devices

Si une partie de la connexion se passe hors authentification, **l’unification de session** définit par défaut lors de l’élaboration de la vue UserId permettra d’intégrer le suivi d’audience précédent le login visiteur.

[![Image](/images/blog/session-unifiée-310x154.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2015/11/session-unifiée.jpg) Session unifiée dans vue UserId
## **Optimiser un suivi visiteur par la personnalisation sur un ensemble de session sur un même appareil.**

Associer Cid  de GA et UserId afin d’avoir un suivi plus précis de l’utilisateur (client),  tout au long de ses sessions , qu’il soit authentifié ou pas,  est  le but de la manœuvre.

Pourquoi faire cette association ? Dans le premier cas exposé plus avant, avant l’authentification , point de salut sur ce qu’à bien pu faire le visiteur sur des sessions non loguées. L’idée donc est de la manœuvre ici est de  passer par la maitrise du **cid de google** (avant login) et de l’ **userId** (authentification) en les associant et les matchant   on obtient ainsi a totalité du comportement utilisateur pendant une série de sessions,  logué ou pas.

Techniquement, il va falloir stocker la valeur du Cid et la faire « matcher » avec celle de l’userId. Cette intégration pourra passer par la création d’une dimension personnalisée pour son stockage comme dimension.

Les limites de cette manipulation sont celles du bon sens , en sachant qu’un seul cid sera associé a un userId donc si plusieurs consultations se font depuis différents devices, point de salut.

Une fois la collecte effectuée, ces **2 dimensions personnalisées** sont disponibles au sein des rapports personnalisés , mais aussi dans la segmentation. Le référentiel de cet userId est propre à chaque entreprise et devra être signifiant pour donner un sens plus prononcé aux rapports. Sinon, pour qualifier plus avant la **connaissance visiteur**, reste de nouer autour ces dimensions personnalisées des métadonnées réservées à la qualification client. Le site e-nor.com explicite cela très bien au travers de ce schéma …

[![Image](/images/blog/cid-et-userid-285x300.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2015/11/cid-et-userid.jpg) Cid et userid sur une session
## **Suivi avancé :  multi-devices, mono-utilisateur, logué ou non ! **

Je reprends le scénario  de l’**agence e-nor*** (super articles en passant) .*

**Scénario :** le visiteur procède à une série de session dont les 2 premières proviennent de 2 appareils différents sans authentification. La troisième visite est authentifiée sur l’un des deux devices. L’userId généré va suivre l’utilisateur lors des sessions suivantes (sert ici de liant) où le cid existant sur le device précédent va rencontrer l’userId généré lors de cette 3ème visite…Simple non ?

[![Image](/images/blog/stitiching-avancé-239x300.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2015/11/stitiching-avancé.jpg) Stitching avancé pour unifier suivi utilisateur logué ou non

Techniquement,  la création de 2 dimensions personnalisées  va récupérer le cid du cookie de analytics.js  et le stocker dans un cookie et l’userId ,  cela dynamiquement sur l’ensemble des  sessions d’un même utilisateur. Ce principe-là s’intitule dans le jargon d’expert **session « stitching ».**  Ne pas confondre ce cette manipulation avec l’**unification de session** bien que très proche néanmoins, qui , comme son nom l’indique, permet d’associer pendant une même session, les hits avant login /userId.   Code "officiel" pour la collecte  (à  adapter selon le cas) :

ga('create', 'UA-XXXXXX-Y);  
ga(‘set’, ‘&uid’, {{USER_ID}}); // a placer avant l'envoi de la page vue pour alimenter la vue cross devices
ga('set', 'dimension1', UserId); // Configure un userid au niveau de l'utlisateur pour le matching de meta data crm
ga('set', 'dimension2', cid); // pour l'envoi le cid au niveau de la session
ga('send', 'pageview'); // envoi de la page vue  

***Elargir ces données utilisateurs via l’importation de meta- données Crm dans GA***

Afin de donner un **contexte «profil client » plus étendu** à sa collecte de clics avec google analytics , il faut passer par l’importation de métadonnées. La porte d’entrée import  passe par la dimension personnalisée UserId déjà collecté par GA.

Ce processus s’effectue au niveau de la propriété via la définition d’un « **schéma de données** ». Chaque métadonnée fera l’objet d’un ajout d’une nouvelle dimension en plus de celle pivot UserId. Ces métadonnées peuvent être relatives aux personas, à la valeur client,  à un référentiel spécifique de la relation client lié au **SI de l’organisation**.

[![Image](/images/blog/importation-dans-ga-310x273.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2015/11/importation-dans-ga.jpg) Schema Importation dans ga

 	- Etape 1 : Choisir la dimension UserId

 	- Etape 2 : Définir et créer les nouvelles dimensions liées aux Méta Crm

 	- Etape 3 : Procéder à la qualification du schéma d’importation (clé : userId ódonnées importées)

 	- Etape 4 : Télécharger un modèle ou accéder à la clé API

 	- Etape 5 : Compléter les données et les importer via fichier.csv ou via programmation dans GA (API)

Exemple de Meta Donnée  Crm :

 	- -> Persona : Curieux, Professionnel, Donneur d'Ordre

 	- -> Valeur Client : Basse, Moyenne, Haute

[![Image](/images/blog/extrait-data-a-importer-dans-ga-310x124.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2015/11/extrait-data-a-importer-dans-ga.jpg) Extrait data csv a importer dans ga

 	- Etape 6 : Attendre la validation

 	- Etape 7 : Procéder au reporting personnalisé

Sur l’étape 7, il faudra donc croiser les dimensions apportées avec d’autres éventuellement (events…) avec des statistiques classiques natives google analytics (sessions..).

[![Image](/images/blog/rapport-crm-dans-ga-310x106.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2015/11/rapport-crm-dans-ga.jpg) Rapport Meta crm et Data GA

Comprenons les réticences des propriétaires de sites  à divulguer des données clientèles même anonymisées. Mais on est sur un marché du gagnant-gagnant , où les 2 parties y trouvent leur compte dans la valeur ajoutée apportée au final à la data.
***Des articles utiles pour comprendre la donnée client ***

Un **grand merci aux auteurs** de ces posts vulgarisateurs sur la thématique Crm et Google analytics

 	- https://www.e-nor.com/blog/google-analytics/advanced-session-stitching-and-cross-device-attribution-using-custom-dimensions-in-google-analytics

 	- https://www.optimizesmart.com/complete-guide-cross-device-tracking-user-id-google-analytics/

 	- http://www.simoahava.com/gtm-tips/once-userid-always-userid/

 	- https://productforums.google.com/forum/m/#!topic/analytics/2J_Ud3Lx1L8
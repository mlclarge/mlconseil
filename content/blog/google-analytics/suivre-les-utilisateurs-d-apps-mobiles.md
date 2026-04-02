---
title: "Firebase analytics un outil d'analyse d'audience pour applications"
date: 2016-11-14
author: "admin"
categories: ["Google Analytics"]
tags: []
slug: "suivre-les-utilisateurs-d-apps-mobiles"
image: "/images/blog/firebase-analytics-presenta.jpg"
---

La sortie d’une version démonstration d’un compte firebase analytics est une bonne nouvelle pour vulgariser les pratiques autour du développement des apps.  Les revenus via les apps mobile auront doublé d’ici 2020 selon le dernier rapport d’[AppAnnie ](https://www.appannie.com/fr/)(fournisseur de Business intelligence) , il est donc temps de parfaire ses connaissances webmarketing sur l’ecosystème des applications !  Mais à quoi sert Firebase analytics précisemment ?   Quelle différence avec Google analytics ? A quoi ressemble la data qui est collectée par une application mobile et restituée par FIrebase ?

## **Firebase  analytics pourquoi faire ?**

### ***Qu’est-ce que firebase ?***

Firebase tout seul, est une application de développement  pour smartphones Android, Ios et autres os.  et firebase analytics un module à l’intérieur qui permet de mesurer l’audience d’une application comme à l’instar de ses  aspects démographiques, de la mesure de l’engagement, de la rétention des utilisateurs sans oublier sa monétisation.
Cette petite vidéo explique parfaitement ce que fournit firebase analytics comme data.

https://youtu.be/fgT6r4f9Apc

## **Firebase Analytics ou Google analytics quelle solution choisir* ?***

On pourrait se demander effectivement quel choix faire pour son suivi d’audience après tout ? De toute manière, si l’on souhaite mesurer quoique ce soit dans une application mobile, cela passe par l’ajout d’un SDK  GA ou Firebase, équivalent d’un tag JavaScript pour une page web.  Mais voici la préconisation de Google sur le sujet :

 	- Organisation avec une seule application ->  Firebase Analytics fera l’affaire

 	- Entreprise ne disposant que d'un site Web -> installer Google Analytics

 	- Structure disposant à la fois d'une application et d'un site Web ->  faire usage de  Firebase Analytics plus Google Analytics L’avantage effectivement pour GA est de tout réunir dans une seule interface avec le suivi d’une application configurée comme une propriété classique, comme l’est un site web.

[![Image](/images/blog/firebase-vs-google-analytics-363x300.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2016/11/firebase-vs-google-analytics.jpg) Firebase Vs Google Analytics
## **Focus sur "FloodIt" une version pour s’entraîner à firebase analytics**

### ***Quel type de data cela produit-il ?***

Ah enfin, Google se bouge pour vulgariser ses plateformes et ouvre une  version démo.  ouverte à tout utilisateur muni d’un compte Google après  inscription à la communauté firebase, Les rapports  sont de vraies données, oui oui !  . L’audience d’une véritable application, celle de Floodit , un jeu de labyrinthe américain permet de rentrer au cœur de ce qui se passe dans une application mobile à savoir des données d’attribution, évènements clés, cohortes, entonnoirs de conversions,  d’audience, les premières ouverture de l’App. (Installations), l'achat in-App etc.. A partir du menu de gauche, on accède à une première vue sous forme à partir du menu horizontal qui donne un joli tableau de bord out of the box présenté sous forme de widgets avec les** kpi** suivants :

 	- Utilisateurs actifs

 	- Chiffres d’affaires

 	- Provenance des installations

 	- Cohortes de fidélisation

 	- Intérêts et interactions des visiteurs

 	- Achat via une application

 	- Version de l’App

 	- Appareils des joueurs

 	- Provenance géographique

 	- Données démographiques

 	- Centre d’intérêts

[![Image](/images/blog/menu-firebase-analytics-422x300.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2016/11/menu-firebase-analytics.jpg) Menu firebase Analytics

Si on rentre dans les détails du menu analytics on peut retrouver :

 	- B/ les performances sur les évènements (clics sur les publicités, reset, désinstallation, mise à jour, achats..)

 	- c/  le type d ‘audience : utilisateurs, crash users, les experts, les différents niveaux de joueurs, les acheteurs.

 	- D/ Des données d’attribution sur les conversions : les atteintes à niveaux de jeux,  volume des installations.

 	- E/ Entonnoirs de conversion : les indicateurs sur atteinte des différentes étapes d’un entonnoir (exemple : passer du niveau de base vers l’utilisation du processus vers les niveaux supérieurs.

 	- F/ Cohortes : Mesure la fidélisation des joueurs par ensembles au travers de 5 semaines ici.

[![Image](/images/blog/cohortes-utilisateurs-application-mobile-310x230.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2016/11/cohortes-utilisateurs-application-mobile.jpg) Cohortes Utilisateurs
### ***Au delà de l'audience, Firebase est aussi une technologie au service du developpeur.***

Sous le menu de gauche, on peut retrouver des fonctionnalités pures  "dev".

 	- Un module de test sur l’installation ou virtualisation à travers différents Os  pour assurer une qualité uniforme.

 	- Plantages : détails sur l’origine des bugs, les différentes étapes qui ont amené au crash.

 	- Notification de campagne : un reporting sur les différents messages pour engager les utilisateurs, volumes, ouverture. Quelles sont les campagnes les plus rentables en termes de gain par utilisateur.

 	- Configuration distante : avec les paramètres de ciblage basés sur une paire clés/valeurs et guidés par une segmentation d’audience, cette fonctionnalité cloud permet de délivrer une UX selon son type d’audience afin d’optimiser les performances de l’application. Elle permet de construire une présentation différente selon le type de visiteur pour résumer.

https://youtu.be/_CXXVFPO6f0

Cette offre de démonstration sera bien utile aux formateurs web marketing pour le plus grand bonheur des étudiants et apprenants :) . Pour accéder à la démo c'est par ici : [https://analytics.googleblog.com/2016/11/introducing-firebase-demo-project.html](https://analytics.googleblog.com/2016/11/introducing-firebase-demo-project.html)
---
title: "5 dernières améliorations de Google Analytics"
date: 2017-06-19
author: "admin"
categories: ["Google Analytics"]
tags: []
slug: "5-dernieres-ameliorations-de-google-analytics"
image: "/images/blog/5-nouveaute-google-analytic.jpg"
---

J’ai pu présenter la nouvelle interface ux/ui de [Google Analytics](https://analytics.googleblog.com/search/label/Analytics)  il y a quelques semaines [ici](https://www.mauricelargeron.com/nouvelle-ux-design-pour-google-analytics/) mais sans mentionner les nouveautés. Examinons 5  améliorations tant au niveau des fonctionnalités que des rapports qui enrichissent plus que jamais cette application d’analyse d’audience.

## **Fraicheur de la données et Intégration du format AMP**

### ***AMP plus lisibles dans GA***

L’idée ici c’est d’avoir une vue de l’audience sur le contenu d’une page qu’elle soit AMP pas AMP. Je rappelle que le format AMP est un format adapté aux appareils mobiles standards imposés par Google pour améliorer l’expérience utilisateur et alléger les data Center de Google.

Le problème c’est que dans Google Analytics il est possible d’ isoler les pages vues en tant qu’AMP et additionner les pages non AMP,  mais pas d’avoir une vue réelle « utilisateur ». Les effets également de cette collecte dissociée entraine une inflation du nombre de visites et d’utilisateurs considérés comme différents par rapport à un même type de contenu.

[![google-analytics-freshness-310x82.jpg](/images/blog/google-analytics-freshness-310x82.jpg) 10 minutes et hop voila la data !

Google donc remédie à cela par agrégation NON AMP ET AMP. Les indicateurs comme le nombre de  pages par session et les taux de rebond augmenteront vu que le nombre de sessions baissera. Ces effets statistiques vont se lisser au cours du temps au fur et à mesure  de l’unification des visiteurs. Dans un premier temps uniquement les pages servies par le domaine seront concernées, précise Google, les pages servies sur les plates-formes déportées en cache ou autres ne seront pas concernées en revanche pour l’instant.

### ***Fréquence d’actualisation : de la matière Fraiche pour les clients 360* !**

Pour les geeks de la data en temps réel, on s’en rapproche grandement du temps réel !  Que ce soit sur n’importe quel support, depuis l’application Google Analytics, ou via l’API et bientôt via Big Query (infrastructure de traitement Big data de Google, pour des traitements de gros  volumes de données), l’information est collectée en 10 minutes, jusqu’à présent il fallait attendre quelques heures pour avoir les data traitées. Un indicateur visuel est présent dans GA

[![amp-google-analytics-310x128.jpg](/images/blog/amp-google-analytics-310x128.jpg) amp google analytics

 	- Les limites au niveau des vues où ces 10 min. de collecte ne s’appliquent pas sont  :

 	- Traitement des données provenant des plates-formes publicitaires Adwords et DoubleClick en revanche restent toujours dans le créneau habituel de quelques heures.

 	- Certaines vues  filtrées : imports, source et support

 	- UserId

## **Valeur des utilisateurs**

Attention on n’a  pas le nom de l’utilisateur en clair (données anonymisées), mais d’une manière agrégée  Google rapporte dans le cadre transactions e-commerce  chaque canal par rapport à la dimension « Utilisateur »  selon les indicateurs statistiques  de Revenu, durée, objectifs, pages vues,  transactions avec une segmentation possible par canal sources support et campagne d’acquisition sur une durée de 90 jours maximum.

[![valeur-client-google-analytics-310x193.jpg](/images/blog/valeur-client-google-analytics-310x193.jpg) Valeur du client
## **Qualité de la session (visite)**

Merci à [Enrico Pavan](http://www.enricopavan.com/)  pour le partage de cette illustration, annoncée il y a six mois déjà  sur la qualité de sessions des visiteurs. Les prérequis pour ce rapport sont d’avoir :

 	- Un suivi des transactions ecommerce intégré a GA

 	- Un minimum de 1000 transactions par mois

 	- Un  historique de 30 jours avec ce seuil des 1000 transactions

Ce dernier est présenté par tranche  ce qui permet une segmentation facile pour analyse. Il est calculé lors de chaque session avec un scoring allant de 1 à 100.  Sur l’illustration  ventile les moyennes qualitatives par type  de canal d’acquisition.

Le but de ce rapport est de pouvoir analyser le potentiel des utilisateurs proches de la conversion,  d’actionner des leviers complémentaires et de répondre aux questions :

 	- Quel type d’action  apporte la marque une audience la plus  ou la moins propice aux ventes ?

 	- Quels sont les contenus,  les mots clés engagent plus ou moins mes visiteurs ?

[![session-quality-google-analytics-310x138.jpg](/images/blog/session-quality-google-analytics-310x138.jpg) Qualité de la session

Comme les objectifs intelligents, listes intelligentes, ce type de rapport peut être utilisé pour engager des actions de remarketing (c’est sans doute la volonté de Google qui par une politique data driven grâce au machine Learning, génère un surplus d’investissements des annonceurs).

## **Une page d’accueil au  Top !**

La page d’accueil reste vraiment ce qui surprend le plus dans cette nouvelle interface Google Analytics, full matériel design ! Elle donne l’essentiel de ce qui est en train de se passer .Elle est de bonne augure sur ce que vont devenir les autres rapports qui restent encore inchangés (temps réel, tableaux de bord)

[![page-accueil-google-analytics-310x236.jpg](/images/blog/page-accueil-google-analytics-310x236.jpg) Page accueil google analytics

En prime, une nouvelle page « produits Google analytics » disponible sur le menu de gauche en bas, au-dessus d’administration, une belle galerie de l’écosystème web analytics de Google.

[![decouvrir-google-analytics-310x214.jpg](/images/blog/decouvrir-google-analytics-310x214.jpg) Galerie marchande de GA :)
## **Plus d’informations nouveautés GA**

 	- [https://support.google.com/analytics/answer/7084038](https://support.google.com/analytics/answer/7084038)

 	- https://support.google.com/analytics/answer/6182550
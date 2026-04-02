---
title: "Comprendre l'analyse visiteur,visite et page vue."
date: 2011-12-08
author: "admin"
categories: ["Google Analytics"]
tags: []
slug: "analyser-les-clics-visiteurs-de-son-site"
---

Ce billet s’intéresse aujourd’hui  à l’interface de l’application d’analyse du** flot de clics sur un site internet** et notamment de Google Analytics. Aujourd’hui je parlerai du principe de remontée des données depuis votre site vers Google. J’ai déjà ébauché ces notions lors d’un article sur le sens des données  dans Google analytics  il y a quelques semaines. Comment peut-on  connaître le nombre de visites, de visiteurs, de pages vues  (uniques ou pas) ?  Je m'attacherai ici à la méthode du marqueur javascript (tag) , d'autres systèmes existent néanmoins (logs,web beacons, sniffeur de packets) . Le principe est simple :

[![GAFonctionnement0-300x200.jpg](/images/blog/GAFonctionnement0-300x200.jpg) Fig1. Principes des cookies

Rien ne se passe avant (depuis le site de recherche Google par exemple) , seulement dès  le site web visité (1), se télécharge sur le navigateur de l’internaute un petit fichier texte appelé cookie qui va être ensuite manipulé par un programme (JavaScript)  qui s’exécutera  sur l’ordinateur de l’internaute à chaque visite en tâche fond et d'une manière asynchrone afin de ne pas ralentir le chargement des pages. Les données remontées via l’appel d'un petit programme Javascript sont ensuite stockées (2), puis analysées (3) et enfin présentées (4) dans l’interface de GA.

Le cœur de cette machine à statistiques sont les cookies, petits fichiers textes  qui se trouvent  dans chaque navigateurs internet (pc, tablette, mobile..). Ils contiennent une chaîne alphanumérique persistente et peuvent identifier une url, un tampon de temps (pour calcul durée), un ID, une résolution d'écran, une profondeur de couleur...

Prenons le cas d’une présentation de données  que j’ai évoqué en introduction : pages vues, visites et visiteurs.  A chaque type, 1 cookie dédié, il est nommé sous la forme  soit _utma, _utmb ou _utmc…et à une vertu particulière. Par exemple le cookie qui représente la donnée « visiteur » a une durée de 2 ans.

[![GAparamétrages7cookie1-310x216.jpg](/images/blog/GAparamétrages7cookie1-310x216.jpg) GA paramétrages

Ainsi, une fréquentation d’un internaute sur un site peut se démontrer par le fait qu’1 visiteur peut représenter 2 visites s’il reste plus de 30 minutes, et 5 pages vues  (1 page vue 3 fois représente 3 pages vues *. Le nombre de pages vues uniques est un critère pertinent car il rassemble sur 1 visite le nombre de pages uniques, donc différentes, qui ont été consultées. Cela  peut souligner l’intérêt du visiteur ou bien témoigner de son papillonnage. Il faudra corréler ces chiffres avec le temps passé global lors d’une visite (contextualisation).

[![GAparamétrages7cookie2-310x237.jpg](/images/blog/GAparamétrages7cookie2-310x237.jpg)

Pour  aller plus loin dans la compréhension des cookies,  le lexique complet de la société américaine [Cardinal path,](http://www.cardinalpath.com/) apporte des précisons sur les appels JavaScript dédiés aux pages vues, aux sources de trafic, et à l’e-commerce.

[![GAparamétrages7cookie3-310x226.jpg](/images/blog/GAparamétrages7cookie3-310x226.jpg)

Cette technologie  de remontée de données a cependant ses limites. En effet, un navigateur = un visiteur, mais  le visiteur  qui navigue avec plusieurs « browsers », ou qui efface ces cookies après chaque session,  ou,  qui, tout simplement, désactive l’installation de ces petits fichiers sur son ordinateur, troublera  les analyses statistiques des clics effectués sur une interface web. De plus, qui est derrière l'écran pour certifier que ce visiteur soit effectivement la même personne ? Il conviendra donc de prendre ces données pour ce qu'elles sont, des indicateurs, à croiser avec d'autres sources (op marketing, panels, enquêtes).*

@Source  images : [Google University](http://support.google.com/conversionuniversity/bin/request.py?hl=en&contact_type=indexSplash&rd=1)
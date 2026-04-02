---
title: "Mesurer les interactions sociales de son site web"
date: 2012-01-11
author: "admin"
categories: ["Google Analytics"]
tags: []
slug: "analyse-engagement-social-dans-google-analytics"
---

Après un dernier article sur l'audit de site web consacré à la mesure des clics visiteurs et pages vues dans Google analytics et  à l’heure  où Google amplifie dans son **moteur de recherche sur les [interactions sociales](http://googlefrance.blogspot.com/2012/01/la-recherche-votre-univers-en-plus.html)**, je me suis posé la question de la mesure des différentes intéractions sociales menées par les visiteurs sur un site.  Quelle solution adopter pour **analyser  les « j’aime », « partage » et autres  « Google +1 »** que peuvent engager mes lecteurs   avec Google Analytics* (centralisation des données)* ?

Postulat de départ : le code de Google analytics est déjà intégré  sur le  site. En natif, ce code assure le suivi automatique du bouton Google plus, un peu normal :) . Là  où les choses se corsent,  c’est lorsque l’on souhaite suivre l’interaction de réseaux sociaux comme Facebook, Twitter, LinkedIn.

Alors comment intégrer donc ces** boutons de partage  sociaux** et assurer leurs suivis dans GA ?

Tout dépend de la solution avec laquelle vous produisez votre contenu au départ. Il peut s'agir d’un site fait sur mesure *(élaborer à l’aide d’un éditeur comme Dreamweaver)*, d’un cms *(type joomla !, drupal etc. )*  ,  d’un blog *(comme ici WordPress)*.  Sinon, il existe aussi des plugins génériques *(adaptables sur toutes plateformes de contenus)*  prêts à l’emploi  mais qui ne possèdent pas forcément toutes les fonctionnalités d'analyse attendues pour suivre les intéractions d'internautes.

## Site sur mesure

Il convient de suivre cette aide [ici](http://code.google.com/intl/fr-FR/apis/analytics/docs/tracking/gaTrackingSocial.html) et notamment d’ajouter cette ligne de code  dans la partie  de la page web et de la paramétrer selon le réseau et l’interaction que l’on souhaite mesurer :

_gaq.push();

	- Network : Twitter, Facebook, LinkedIn

	- Social action : j’aime, partager, tweet)

	- Opt-target l’url de la page concernée (option)

	- opt_pagePath : une chaine de caractères qui représente le chemin par lequel l’action arrive. Le plus souvent le chemin de la page est la source d’interaction, cette option est utilisée dans le cadre de pages virtuelles dont les urls sont générées dynamiquement et donc pas traçable facilement.

Le moyen le plus simple ensuite  est de récupérer sur les plates-formes sociales, les boutons à intégrer sur votre site et d’y ajouter les codes correspondants. Attention aux boutons Facebook générés dans une iframe, le code de suivi GA de fonctionnera pas. Par ailleurs, il conviendra aussi d’utiliser le JS-SDK async de FB afin d’assurer une parfaite intégration.

**FaceBook (bouton "j'aime")**

[![Image](/images/blog/facebook-300x254.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2012/01/facebook.jpg) Integration sociale plugin Facebook

**FaceBook (bouton "j'aime" + "j'aime plus" et "envoyé") **Code plus complexe qui apporte plus de choix dans la mesure de l'intéraction.

[![Image](/images/blog/jsfbcorpspage-300x213.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2012/01/jsfbcorpspage.jpg) Code corps de page "J'aime, j'aime plus, envoyé"
### **Extensions sociales  pour logiciels éditeurs (ici Dreamweaver)**

Sinon, il existe des extensions qui permettent de rajouter sans rentrer trop dans le code des boutons de partage vers réseaux sociaux.  Par exemple la société Webassist  fournit un « addon » pour Dreamweaver qui  permet d’intégrer  aisément à l’ensemble d’un site les boutons sociaux et de l’interfacer avec Google analytics ensuite.

FIchier manaquant : rechercher webassist sur archive.org

**Cms (Joomla !)**
Les solutions pour cms, blogs ou plugins dédiés « standalone » (addThis)  sont des solutions intégrées  où les boutons sont fournis, ainsi que le tracking (analytics).

Dans un Cms, l’avantage est d’avoir un Framework qui produit en quelques clics une plateforme de gestion de contenu, son inconvénient par rapport à une solution développée sur mesure est que pour l’ajout d’une fonctionnalité précise, comme ici, trouver une solution de partage social pouvant être monitorée  par une application externe comme Google analytics , n’est pas sans difficulté.

J’en ai trouvé 1 ! Elle ne réclame vraisemblablement pas de hack sur le code natif de Joomla ! et peut s’interfacer avec GA.

[![Image](/images/blog/joomla-300x190.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2012/01/joomla.jpg) Solution partage social Joomla!Plus d’infos : http://www.wijiti.com/projects/jsharethis

** Additif du 13/01/2012 ! **

****Une autre solution, qui,  je dois l'avouer, m'a été souflée par son **développeur Yannick Gaultier**  et  la plus pratique me semble t-il, est l'adoption du composant **sh404 Sef** qui permet non seulement *(et c'est sa vocation de base)* de re-écrire les urls optimisées pour l'internaute et les moteurs de recherche,et  qui dernièrement, s'est vu enrichir d'une fonctionnalité qui permet l'ajout de **boutons de partage vers les réseaux sociaux**. Le tableau de bord  est visible depuis l'administration du site, mais également,depuis l'interface de google analytics.

[![Image](/images/blog/404sef-300x245.png)](https://www.mauricelargeron.com/wp-content/uploads/2012/01/404sef.png) Configuration composant Sh404Sef                              & des boutons sociaux

[![Image](/images/blog/sh404sef-254x300.png)](https://www.mauricelargeron.com/wp-content/uploads/2012/01/sh404sef.png) Tableau de bord analytics dans Joomla!

[![Image](/images/blog/s404-300x135.png)](https://www.mauricelargeron.com/wp-content/uploads/2012/01/s404.png) Boutons de partage social Article Joomla!
**Blog (WordPress) **

Là aussi, il faut faire son marché. Le plus souvent, les plugins proposent  de monitorer  dans le back-end automatiquement les interactions sociales comme par exemple le plugin "social metrics" mais sans ouverture sur le suivi de Google Analytics, et  rares sont ceux reliés directement à  GA.

Cependant j’ai  trouvé  [Social Media Tracking](http://wordpress.org/extend/plugins/social-media-tracking/),  merci au développeur, un plugin dédié GA, que j’ai installé ici sur ce blog pour l’occasion ! Sans aucune manipulation de code, je le laisse tourner en test en ce moment.

[![Image](/images/blog/socialTracking-300x157.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2012/01/socialTracking.jpg) Partage social "trackable" avec GA

**Additif du 16/01/2012**

La solution de ce plugin après vérification dans GA , est malheureusement obsolète, il traque les intéractions mais les fait remonter au niveau de GA dans la section Contenu>évènements :( et non dans audience>Réseaux sociaux>interet et interaction

[![Image](/images/blog/social-interaction-300x159.png)](https://www.mauricelargeron.com/wp-content/uploads/2012/01/social-interaction.png) Remontées données plugin obsolètes

J'ai fait une recherche nouvelle ([forum DIY](http://diythemes.com/) ) et suis arrivé sur ce [tutorial ](http://creersitepro.com/2011/ultimate-share-buttons-code-for-thesis/)qui offre l'intégration complète pour le thème Thésis (celui de ce blog) fait par serge (Un grand merci pour lui) ! Il intègre les 4 plateformes (google +, twitter, facebook et linkeIn) , et normalement est relié à Google Analytics (à tester donc).

Enfin, une solution que je trouve vraiment passe partout et aboutie est celle de AddThis . Non seulement ce plugin est universelle (editeur,cms , blogs)possède  un backEnd de monitoring réussi ainsi que la possibilité via leur api de l'intégrer très facilement dans GA.

[![Image](/images/blog/addThis1-300x297.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2012/01/addThis1.jpg) AddThis & GA integration

Une fois la solution choisie , les données sociales sont ensuite visualisables dans l’interface Analytics de Google.

[![Image](/images/blog/ga1-300x231.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2012/01/ga1.jpg) Rapport des partages sociaux dans GA

Plus d'infos : [Analyse du plugin réseaux sociaux](http://support.google.com/analytics/bin/answer.py?hl=fr&topic=1316551&answer=1316556)
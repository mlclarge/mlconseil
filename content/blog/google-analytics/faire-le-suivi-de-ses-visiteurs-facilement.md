---
title: "Autotrack : un plugin qui facilite Google analytics !"
date: 2016-04-25
author: "admin"
categories: ["Google Analytics"]
tags: []
slug: "faire-le-suivi-de-ses-visiteurs-facilement"
image: "/images/blog/autotrack.jpg"
---

Voilà une fonctionnalité **Google analytics** qui va séduire les utilisateurs non geek de l'analyse d'audience. [Autotrack ](http://analytics.blogspot.fr/2016/02/introducing-autotrack-for-analyticsjs.html)permet d'enrichir le tracking de base standard et évite d'aller sur le gestionnaire de balises (GTM) pour faire court. Comme son nom l'indique, ce plugin automatise la pose de marqueurs sur un site. Alors essayons de voir les aspects essentiels.

## **Pourquoi utiliser l'autotracking ?**

Ceux qui utilisent la version standard de GA et qui n'utilisent pas **google tag manager** (peut être trop complexe à certains égards) sont les premiers concernés par cette nouveauté. Elle n'est pas disponible pour la version premium, et le code est open-source disponible sur github.

[![autotrack-google-analytics-310x153.jpg](/images/blog/autotrack-google-analytics-310x153.jpg) Principes d'autotrack

**Les 6 types de suivi simplifiés d'autotrack**  :

 	- les clics sur les liens sortants

 	- un formulaire situé sur un domaine externe ou sous domaine.

 	- des intéractions sur historique d'urls d'une même page (ajax)

 	- des changements de disposition d'appareils (détection des résolutions de devices )

 	- Tracking de boutons sociaux natifs officiels twitter et facebook

 	- Suivi d évènements (clics spécifiques à identifier)

Il n'est donc pas destiné à ceux qui déjà font un suivi avancé par le gestionnaire de balises, ou qui possèdent déjà un suivi classique avec des marqueurs installés. Il est cependant possible dans [GTM](https://www.mauricelargeron.com/google-tag-manager-un-outil-webmarketin-bien-utile/) d'installer via un html personnalisé le script de base en y incluant le plugin autotrack.

## **Comment implémenter autotrack ?**

En 2 temps : intégration du **code source autotrack.js** et pose du script sur le template du site.
Il faut intégrer ce code donc sur les fichiers Js du site dans un répertoire dédié, ou alors sur un cdn externe bref, c'est lui qui va faire fonctionner le marqueur , inséré dans le script natif de GA standard déjà placé dans le header.

[![autotracker-310x104.jpg](/images/blog/autotracker-310x104.jpg) Insertion du plugin
## **Quels types de rapports donnent autotrack ?**

Normalement, dans la catégorie **[évènements de GA](https://www.mauricelargeron.com/mesurer-les-interactions-visiteurs/)**, ou alors pour le suivi de résolution, il faudra passer par l'installation de dimensions personnalisées et créér des rapports personnalisés. Pour avoir une idée de [type de graphique](https://www.mauricelargeron.com/les-rapports-graphiques-dans-ga/) de données ou d'insights comme le disent les geeks anglophones , allez sur le site de démo , sinon, voici un aperçu de ce que l'on peut tirer de ce plugin autotrack :

[![exemple-rapport-autotrack-310x140.jpg](/images/blog/exemple-rapport-autotrack-310x140.jpg) Exemple rapport autotrack

Documentation sur autotrack :

 	- [http://analytics.blogspot.fr/2016/02/introducing-autotrack-for-analyticsjs.html](http://www.blastam.com/blog/index.php/2016/03/google-analytics-autotrack-should-you-use-it)

 	- [https://github.com/googleanalytics/autotrack](https://github.com/googleanalytics/autotrack)
---
title: "Le gestionnaire de balise enfin dévoilé..en Français !"
date: 2015-07-15
author: "admin"
categories: ["Google Analytics"]
tags: []
slug: "se-documenter-sur-le-gestionnaire-de-tag-de-google"
---

[**Google tag manager**](https://www.google.fr/tagmanager/) vous connaissez ? Non, ou un peu.. Ou alors vous en avez entendu parler  sans doute… si vous oeuvrez dans le webmarketing .. Malgré le titre  "angloxason" tout est rédigé en Français, ouf !  Jusqu'à lors,  la littérature papier en Français  sur le sujet n'existait pas *(disponible aussi en numérique néanmoins)*, sauf, sauf... depuis l’arrivée du  bouquin de **Ronan Chardonneau*** , *qu'on de présente plus,** **multirécidiviste dans la vulgarisation web analytics :  Maître de conférences, blogueur, auteur d’ouvrages sur le webmarketing, conférencier bref..j’arrête là. Soulignons que ce bouquin arrive à point nommé vu l' utilisation grandissante du GTM aussi bien auprès de développeurs que des web marketeurs.   Bon, que nous racontes-tu Ronan  dans ce livre ?

## **S’initier au monde des gestionnaires de balises**

### ***Les parties prenantes du marché des TMS***

L’approche de l’auteur se veut très englobante et linéaire. Il se met à la place du **néophyte, non développeur** , avec une posture de marketeur curieux. Il nous raconte dès les premières lignes la place de cet outil Google  parmi les différents acteurs du marché.  Sans renier son côté franchouillard, Ronan nous  fait découvrir d'abord un  pionnier du "tag management",   la solution payante Française « **TagCommander** » bien implantée mondialement et en France bien sûr *(auprès de grands comptes principalement)*. et ensuite des solutions propriétaires ou open source *(adobe dynamic tag management, tagman, opentag, tealium les derniers chiffres de ce « vendor » : 25% de part de marché sur les 100 premiers sites mondiaux).*

[![Image](/images/blog/chapitres-du-livre-google-tag-manager-310x62.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2015/07/chapitres-du-livre-google-tag-manager.jpg) Grandes Parties du livre gTm

Puis on rentre dans le vif du sujet avec focus sur le **Google Tag Manager**,  présentation « all-in-one » j’aurais envie de dire. R. Chardonneau  rentre directement dans le concret avec des explications sur ce qui constitue le cœur de ce système de tracking : **le datalayer**. Cette dernière est une pièce maitresse  qui va servir d’interface pour pousser des **données standard ou métiers** du site web vers une solution d’analyse d’audience. Attention ! Pas forcément Google analytics, même si parfois cela prête à confusion pour les néophytes, Google tag manager est une solution adaptable  à  tout système de  tracking** ** (At internet, adobe, Google, piwik…). Je propose ici une illustration non tirée du livre  issue d’un cours sur le site  Lynda.com consacré à GTM.

[![Image](/images/blog/illustration-cours-Lynda.com-sur-GTM-310x172.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2015/07/illustration-cours-Lynda.com-sur-GTM.jpg) Illustration Personnelle (pas dans le manuel)
### ***Méthodologie d’implémentation d'un projet de tracking***

Une fois que l’on connait ce dont on parle, il faut se retrousser les manches et se poser les bonnes questions lors du projet d’installation du gestionnaire de balises dans une optique ex-nihilo ou alors dans le cadre d’une migration. Comme toute stratégie, et ici, la web analyse n’est pas en reste, il faut agir avec méthode , en prenant pour principes de procéder par étapes,  dans une manière agile sans oublier les facteurs humains (RH), conditions essentielles de la réussite d’un projet (compétences, services, implication, formation).

	- Expression des **besoins de trackin**g : métiers, audience, acquisition, comportements, conversions

	- Fixation des **objectifs et suivi par l’installation de kpi** : référentiel et indicateurs de performances

	- **Plan de marquage** : traduction technique des données à collecter sur le site (variables, tag, solutions)

	- **Développement et production**:  solution de tracking, univers pré-prod, livrables, recette

	- **Surveillance** : monitoring, maintenance (mise à jour)

	- **Analyse** : reporting, tableaux de bord

	- **Optimisation** : corrections , améliorations (itératif)

## **Description de la plateforme Google Tag  Manager**

L’auteur s’attache à expliquer le fonctionnement de la plateforme sur sa dernière version (plus d’infos ici : la V2)  en l’étayant d’exemples concrets à chaque description. On retient  les possibilités  de l’outil en terme de :

	- Gestion des accès utilisateurs

	- D’insertion de plusieurs comptes GTM à l’intérieur de la plateforme (reprenant le principe d’un compte Google analytics intégrant plusieurs comptes UA-XXXXXX)

	- D’intégration de solution de balises de façon native, c’est-à-dire sous forme de « template » , formulaires simples à compléter selon les trackers des fournisseurs  (Google analytics et adwords ;)  linkedin, ClickTale, DoubleClick) ou personnalisée (html, javascript)

	- Enfin, les 3 jalons des principes de tracking sont ensuite détaillés dans la pratique : balises, déclencheurs et variables (intégrées ou à personnaliser)  sans oublier l’étape débugage avant de passer à celle de la mise en ligne et toujours illustrés de cas concrets.

## **Cas pratiques et carnet d’adresses  en web analytics**

### ***14 tutoriaux gtm pour expliquer comment cela marche***

Il  n’y plus qu’à se retrousser les manches et à s’y coller. Ronan Chardonneau s’attache essentiellement à des exercices pour les solutions Google, mais pas que vu qu’on retrouve des cas d’intégration pour Piwik, Microsoft Bing, tracking spécifique Seo (et oui, quand tout se rejoint, c’est chouette) :

	- Google analytics : suivi universal standard, conversion adwords,  evènements, erreurs Js, vidéos, roll-over, historique, données tierces via api (météo)

	- Divers : Piwik, Msn Bing Ads, Seo

### *Pour aller plus loin avec le gestionnaire de balises*

Listing des outils pour se simplifier la vie, networking web analytics, et documentation  ponctue ce livre qui , sans douter la moindre seconde, fera gagner du temps à son lecteur. Merci à toi Ronan pour ce boulot de rédaction.

Liens pour se procurer le livre aux editions ENI : [http://bit.ly/LivreFrancaisGoogleTagManager](http://bit.ly/LivreFrancaisGoogleTagManager)
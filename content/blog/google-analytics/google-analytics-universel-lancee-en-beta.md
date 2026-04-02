---
title: "Récapitulatif des dernières des 12 améliorations dans GA"
date: 2013-04-17
author: "admin"
categories: ["Google Analytics"]
tags: []
slug: "google-analytics-universel-lancee-en-beta"
---

C’est le grand déballage de printemps depuis le point effectué en décembre sur les dernières améliorations de [Google analytics](https://www.mauricelargeron.com/google-analytics-devient-universel/). Depuis donc mi-janvier 2013,  j’ai regroupé les principaux changements  sur l’interface de l’application sous 3 catégories : le code et le compte GA, l’e-commerce *(panier et adwords)* et les sources de trafic *(social)*. Certains changements sont anecdotiques, d’autres sont plus fondamentaux, commençons par les plus importants alors..

## Paramétrage du code et gestion des données

### Google analytics universel version bêta

On y est ! Lorsque vous ouvrez un compte GA vous avez le choix d’opter pour le nouveau code de tracking Google analytics , faites vos jeux…Le principe au fond, est de choisir la bêta, elle vous offre des possibilités plus étendues dans la collecte des données :

	- 20 variables (+15)  et **statistiques personnalisées** ,.

	- Configuration plus simple des sessions, source de trafic, exclusion de sites référents et termes de recherche.

	- Importation par l’intermédiaire d’un nouveau protocole, des données externes à Google analytics liées à votre propre système d’information.

[![Image](https://www.mauricelargeron.com/wp-content/uploads/2013/04/1-nouveau-code-ga-310x258.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2013/04/1-nouveau-code-ga.jpg) Version  GATC Universelle disponible
### Droits des utilisateurs

Trois niveaux d’accès au lieu de 2 auparavant (admin et utilisateurs)  vont être disponible sous peu, me concernant, je n’ai encore rien vu venir :( . Ces 3 types de droits d'accès s’établissent au niveau du compte, de la propriété *(blog, application, mobile)* ou des profils avec un principe d’héritage classique *(parent, enfant)*. Un utilisateur pourra donc accéder ou pas à certains niveaux, et cela d’une manière combinée dans le cas de plusieurs comptes.

	- 1er niveau : tout le compte

	- 2eme  niveau : un type de  propriété

	- 3eme niveau : un jeu de profils

[![Image](https://www.mauricelargeron.com/wp-content/uploads/2013/04/2-droits-et-acces-google-analytics-310x144.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2013/04/2-droits-et-acces-google-analytics.jpg) Droits accès plus fonctionnels - Source Google
### Historique des modifications

Ah celle-ci, cela faisait un bout de temps qu’elle s’annonçait. Qui a fait quoi sur le compte ? Les différents ajouts, suppressions ou autres sont désormais accessibles depuis le niveau de l’administration du compte.

[![Image](https://www.mauricelargeron.com/wp-content/uploads/2013/04/3-historique-310x108.png)](https://www.mauricelargeron.com/wp-content/uploads/2013/04/3-historique.png) Historique des modifications
### Export des données

Un changement mineur mais néanmoins, à l’heure du cloud, il fallait le souligner. Si vous souhaitez rester dans l’écosystème de Google, un export vers Google drive et son application **tableur** est possible.

[![Image](https://www.mauricelargeron.com/wp-content/uploads/2013/04/4-exports-295x300.png)](https://www.mauricelargeron.com/wp-content/uploads/2013/04/4-exports.png) Export vers Google Docs
### Moteur de navigation

Un champ de recherche « assistée » permet très rapidement de retrouver le rapport égaré. Google nous habitue désormais à ce type de fonctionnalité, ce qu’il y a de pratique, c’est la visualisation du chemin qui amène au reporting.

[![Image](https://www.mauricelargeron.com/wp-content/uploads/2013/04/5-recherche-assistee-310x248.png)](https://www.mauricelargeron.com/wp-content/uploads/2013/04/5-recherche-assistee.png) Recherche rapide et visuelle
### A la recherche ..du Temps réel !

L’**analyse en temps réel** n’est plus un gadget comme je l’entends dire souvent ! Certes, il faut une  équipe sur le pont pour suivre l’outil et en déduire des correctifs sur le champ, mais l’outil est fiable et utile pour les impatients de la donnée,  lors par exemple d’un  lancement d’une  campagne pour juger s’il y a buzz..ou pas !  La configuration de widgets "temps réel" selon des indicateurs liés aux **visiteurs actifs** selon leur nombre, le labs de  temps, la géolocalisation, ou autres variables selon ses besoins. Les  possibilités nouvelles par le temps réel permettent donc la :

	- Distinction du trafic par appareil (tablette, mobile, bureau)

	- Création de raccourcis sur les segments personnalisés

	- Comparaison des données triées des données d’ensemble

	- Création de Tableaux de bord « widgetisables » en temps réel

[![Image](https://www.mauricelargeron.com/wp-content/uploads/2013/04/6-widgetsTempsReel-310x165.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2013/04/6-widgetsTempsReel.jpg) Tableau de Bord : widgets temps réel

Sans oublier, c'est en bêta,  la mesure des **évènements** (clics, téléchagements..) aussi en temps réel* (Chemin d'accès : Temps réel > Evènement).*
### Extension pour navigateur Chrome *(mise à jour 24/04/13)*

Voilà un outil pratique qui permet de vérifier si un code est bien implanté. Donc au menu un indicateur écrit en vert 'working" donc cela est bon, le type de code, sa syntaxe et eventuellement les variables personnalisées installées.

[![Image](https://www.mauricelargeron.com/wp-content/uploads/2013/04/extension-chrome-215x300.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2013/04/extension-chrome.jpg)
### Mise à jour pour applications mobile Android et IOS

Les ingénieurs chez GA ont remanié les SDK afin de rendre plus simples l'installation du code de suivi. Les rapports donnent des informations sur le nombre des acquisitions téléchargées, leurs utilisateurs (le type d'appareils, géolocalisations, régularité d'utilisations), les différentes intéractions avec l'interface de l'apps, et enfin les résultats une fois en amont paramétré objectifs et ecommerce électronique (ventes, formulaires). Plus d'informations en fin d'article.
[![Image](https://www.mauricelargeron.com/wp-content/uploads/2013/04/google-analytics-sdk-mobiles-310x204.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2013/04/google-analytics-sdk-mobiles.jpg)
## E-commerce et Adwords

### Chiffre d’affaire local

Pour les commerçants **multidevises**, le paramétrage du code e-commerce avec multiples monnaies est validé. Pratique et ne remet pas en cause la donnée globale de CA calculé automatiquement par un service Google de conversion de devises.

[![Image](https://www.mauricelargeron.com/wp-content/uploads/2013/04/9-chiffrelocalDevise-310x254.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2013/04/9-chiffrelocalDevise.jpg) Devises multiples sur e-commerce
### Plusieurs comptes pour 1 client

Ce cas est remonté d’une demande récente sur le **forum adwords**. Il arrive parfois de gérer plusieurs comptes adwords pour un seul client, comment s’y retrouver ? Une variable est à ce propos disponible dans les rapports standards  mais malheureusement pas dans les « personnalisés ».

[![Image](https://www.mauricelargeron.com/wp-content/uploads/2013/04/10-client-adwords-310x96.png)](https://www.mauricelargeron.com/wp-content/uploads/2013/04/10-client-adwords.png) Identification des comptes adwords
## Sources de trafic « social »

2 types de rapports prêts à l’emploi sont consultables depuis source de trafic > réseaux sociaux.
### Hub social et intéraction

Le premier rapport, autrefois disponible indirectement dans l’interface GA, concerne sur ce qui se dit au sujet d’une page web et sur son partage sur les **plateformes sociales** (ceux appartement au Hub social comme l’entend Google).

[![Image](https://www.mauricelargeron.com/wp-content/uploads/2013/04/7-centre-de-donnees-sociales-310x151.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2013/04/7-centre-de-donnees-sociales.jpg) Données du Hub Social
### Liens retours

Enfin, ce dernier tableau « tout fait » de « **rétroliens** » ou backlinks, ceux qui pointent vers un site avec les propriétés du lien, le titre de la page pointée et le nombre de visites dues à ce lien retour. Le référenceur aurait plutôt placé ce rapport dans « optimisation pour du référencement », mais on sait que Google tente de faire comprendre que la popularité d’un site doit provenir du social, et non  de la pose de liens ..optimisés pour le référencement dans une optique d’audience.

[![Image](https://www.mauricelargeron.com/wp-content/uploads/2013/04/8-retroliens-310x51.png)](https://www.mauricelargeron.com/wp-content/uploads/2013/04/8-retroliens.png) Trafic des rétroliens

Voilà donc pour l’essentiel des nouveautés dans Google analytics, reste le challenge maintenant à relever par le web marketer sur le premier point évoqué, celui de l’**analyse multi-plateformes universelle**.
 Infos mobiles : [http://support.google.com/analytics/answer/2568871?hl=fr](http://support.google.com/analytics/answer/2568871?hl=fr)
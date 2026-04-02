---
title: "Annonces Textuelles Contextualisées"
date: 2014-12-15
author: "admin"
categories: ["annonces google ads"]
tags: []
slug: "personnaliser-les-annonces-adwords"
---

**Google Adwords** se veut de plus en plus dynamique avec l’arrivée de cette nouvelle fonctionnalité « ads customizer » .  Il semble que la plateforme publicitaire de Google  veuille conduire l’annonceur vers un pilotage des campagnes de plus en plus orienté par des flux de données**.** Les données entreprises situées au sein de la bibliothèque partagée marquent ce phénomène de **campagnes pilotées par les flux ***(google merchant center  pour google shopping fut le premier à utiliser cette technique !)* où le site web à promouvoir est décomposé en  « feeds » d’application, de liens, de téléphone, d’offres, de remarketing graphique…

[*](https://www.mauricelargeron.com/wp-content/uploads/2014/12/flux-feed-adwords.jpg) Les flux dans Adwords
## **Atouts du constructeur **personnalisé **d’annonces **

La création d’annonces incitatrices et  contextualisées est intrinsèquement liée  à l’**e-commerce**, bien que  le** btob** puisse aussi l’utiliser à bon escient..

L’objectif annoncé de cette fonctionnalité est de permettre de générer un message pertinent , incitant au clic bien  sûr mais adapté en temps réel à la requête de l’internaute avec la possibilité d’annoncer à terme sur :

 	- un message adapté selon le **contexte du visiteur** (sa géolocalisation, historique, la météo, une date d’évènement)

 	- une promotion limitée dans le temps (début et fin d’une opération).

L’exemple d’une campagne dont les enchères soient pilotées par un script lié aux conditions météo et personnalisées selon un évènement saisonnier est désormais possible.

Cette fonctionnalité va pouvoir  être utilisée à 2  niveaux dans un compte :

Au sein d’une structure de campagne existante à l’intérieur de groupes existants, donc sans modification particulière de l’arborescence d’une campagne

Ou alors d’une manière transversale pour une campagne vu que les paramètres du flux permettent de récupérer des éléments liés :

 	- A la campagne

 	- Aux groupes d’annonces

 	- Aux mots clés

 	- A la localisation (à venir)

[![ads-customizer-310x197.jpg](/images/blog/ads-customizer-310x197.jpg) Transversalité annonces à l'aide du flux

Avec un choix de combinaisons entre ces  entités avec une condition « ET » et ainsi  permettre ainsi un ciblage équivalent à une structure hiérarchisée traditionnelle.

## Mise en Œuvre et fonctionnement des annonces "customisable"

### **Processus de création***

Un flux n’est ni plus ni moins qu’une feuille de calcul. Il faut construire d’abord la construire avec les attributs (entête de colonnes)  personnalisés au métier  et procéder à l’appel des attributs indiqués dans son flux lors de la [construction de l’annonce](https://www.mauricelargeron.com/des-annonces-toujours-plus-automatisees-par-google/).

[*](https://www.mauricelargeron.com/wp-content/uploads/2014/12/processus-de-creation.jpg) Processus de creation

Pour l’instant, l’annonce peut être circonscrite uniquement dans un groupe d’annonces existant. Il est fortement conseillé d’avoir donc une annonce textuelle standard en cas de non déclenchement de l’annonce dynamique.

[![construction-flux-adwords-310x154.jpg](/images/blog/construction-flux-adwords-310x154.jpg) Construction d'une annonce

Les mises à jours sont possibles directement depuis l’interface adwords ou par update du flux dans sa totalité ou alors par mise à jour partielle avec adjonction d’un attribut « ad or remove » au niveau du feed (sans doute plus favorable à la conservation de l’historique des performances).

### **Possibilité de ce type d’annonces***

***Compatibilité :***

 	- Balise dynamique mot clés

 	- Extensions d’annonces

 	- Texte et nombre

 	- Correspondance des KW

 	- Ouvert sur l’API adwords

 	- Disponible sur le search et le display et sur du remarketing dynamique

 	- Parution programmé possible (ads scheduling)

***Incompatibilité  :***

 	- Campagnes dynamiques ( dsa)

 	- Mobiles prefered ads mais choix du device « mobile » autorisé dans le flux

 	- Google shopping et flux personnalisé d'annonces

 	- Ads Parameters

 	- Modification les urls de destination

### ***A venir courant 2015***

 	- La géolocalisation dans les attributs ! Pas mal :)

### ***Fonctionnement de l’impression***

Le déclenchement de l’annonce se fait ensuite sur la requête vis-à-vis du flux, pour illustration…

[![annonce-personnalisee-310x142.jpg](/images/blog/annonce-personnalisee-310x142.jpg) Impression dans Google
## **Ressources - Liens **

 	- Webinar en français : https://www.youtube.com/watch?v=GgJ2H5FrUqE

 	- Documentation Google :  https://support.google.com/adwords/answer/6093368?hl=fr#types
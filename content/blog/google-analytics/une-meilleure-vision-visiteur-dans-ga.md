---
title: "La vue utilisateur débarque enfin dans Google Analytics."
date: 2016-05-02
author: "admin"
categories: ["Google Analytics"]
tags: []
slug: "une-meilleure-vision-visiteur-dans-ga"
---

2016 sera sans doute une année ultra-riche pour **Google analytics** en nouvelles fonctionnalités. Il en devient difficile  de mettre à jour mes formations analytics :( . En vedette aujourd’hui, le tout nouveau rapport : **[explorateur d’utilisateurs](http://marketingland.com/google-analytics-new-user-explorer-report-shows-individual-anonymized-website-interactions-172998)**, centré sur le visiteur, du jamais vu !  C’est une révolution dans l’esprit de GA, toujours orienté sur des agrégats de données, segmentables certes, mais jamais encore ramené à l'individu. Alors que nous fournit ce rapport révolutionnaire ?

## **Explorateur d’utilisateurs : mieux comprendre son visiteur**

L’objectif ici est bien de dresser des profils, donc de rapprocher sa loupe de ce que peut faire un utilisateur. Alors vraiment utile ? Soyons critique..  Quand on a des milliers voir des millions de visiteurs, peut-on réellement étudier chaque "potentiel" client ? Pas vraiment, la web analyse s’attache  à donner des **tendances, des flux** qui permettent la décision et l’optimisation d’une application, d’un site web.  Mais quand on peut extrapoler cette data à des ensembles, cela peut devenir judicieux.

Un des atouts de ce rapport explorateur d'utilisateurs, est sans doute la possibilité de l' **élargir  par de la data captée sur site et hors site**, via  des dimensions personnalisées , un **CRM** ou autres solutions de marketing automatisé.  Chacun des profils se voient enrichis dans des segments à forte valeur ajoutée. J’ai essayé ici d’en parler dans cet [article ](https://www.mauricelargeron.com/importer-et-contextualiser-donnees-de-gestion-de-la-relation-client/) il y a quelques semaines.

L’enrichissement concrètement c’est une adresse email, de la data nominative collectée lors de l’envoi d’un formulaire, lors d’un appel téléphonique, d’une visite en magasin, une donnée métier collectée sur le site. Il suffit ensuite de les associer à cet client id fournit par GA  (cid), et le tour est joué. Google est content car aucune information personnelle n’est affichée, sa plateforme devient un **outil de reciblage publicitaire** plus précis (la finalité est tout de même là ! ) et l’utilisateur quant à lui, améliore sa stratégie data-driven. C’est du gagnant gagnant dans ce monde froid numérique :).

L’import de cet enrichissement de data « **user centric** »  peut donc se faire plus lisiblement dans GA, via ce rapport, avec la fonctionnalité des dimensions personnalisées. Dans l’illustration ci-dessous, je fais un zoning pour expliquer ce nouveau rapport :

 	- **Acquisition **: la source, la provenance du visiteur avec la date et le device utilisé

 	- **Connaissance client **: avec l’importation de dimensions personnalisée, ici, elles sont libellées mais pas encore activées.

 	- **Comportemental avec 4 données** : pages consultées, les objectifs réalisés, les données ecommerce (transaction ecommerce)  et les évènements (clics sur pdt, libellé moyen de paiement, lecture vidéo..).

[![Image](https://www.mauricelargeron.com/wp-content/uploads/2016/04/explorateur-prospects-310x170.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2016/04/explorateur-prospects.jpg) La rapport explorateur d'utilisateurs
## **Les plus et les moins de ce nouveau rapport ?**

### ***Les aspects positifs de cette fonctionnalité d'audience***

 	- Une vue micro pour améliorer un ensemble , c'est bien !

 	- La création de segment selon les insights recherchés : évènements, chiffre affaires, pages vues.. Pour illustration, je pars d’un utilisateur et je créé un segment à partir de ce persona « prospect prudent » qui a la particularité d’avoir rempli ces 2 micro-conversions :

-> Segment = Avoir vu ma page « qui suis-je » du blog +  avoir cliqué sur le logo « Google partners »

[![Image](https://www.mauricelargeron.com/wp-content/uploads/2016/04/CREATION-SEGMENT-310x300.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2016/04/CREATION-SEGMENT.jpg) Création de'une segmentation basée sur l'utilisateur

Ensuite dans Google adwords, si l’audience est suffisante (100 pour le display et 1000 pour le moteur de recherche Google) je pourrai lancer une campagne de reciblage. Bon, ici, avec 3 utilisateurs, je vais pas aller bien loin..

[![Image](https://www.mauricelargeron.com/wp-content/uploads/2016/05/tri-sur-segment-google-analytics-310x133.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2016/05/tri-sur-segment-google-analytics.jpg) Résultat du filtre après segmentation
### ***Les points à améliorer sur ce reporting centré utilisateur***

 	- Il n’y a pas de champ de recherche sur le rapport, pas très pratique quand on cherche une référence précise manuellement

 	- Pour l’instant les rapports personnalisés n’intègrent pas la dimension client Id

 	- On ne peut remonter qu’environ 2 mois en arrière, pas plus.

 	- Une segmentation native par genre « habitués, récents » ou par durée (plus de 3 mn par ex.)

## **Comment est produit ce rapport pour le comprendre ?**

On peut faire du reverse engineering à la papa !  Il suffit pour cela d’aller sur chrome et de télécharger wasp, une extension qui va visualiser le cookie et son contenu dans le navigateur,  pour faire au plus simple *(mais  c’est possible  sans addons aussi)*. Ensuite  Tapez F12, charger la page du site, et lire les informations.  En effet, suis à la pose du **script de suivi standard de google analytics**, toutes les pages web du site animent un cookie lié au domaine visité. Le **client ID**, cid dans le jargon, est composé de 2 série de  suite de chiffres qui identifient un même visiteur au fil de ses visites, il a une durée maximale de 2 ans. Cette information ainsi que la page vues, le device , l’heure, et d’autres dont les dimensions personnalisées, sont récupérées à chaque session (visite).

Pour l’exemple, je me suis auto-traqué, cela fait mal, mais je me suis dévoué :) .

[![Image](https://www.mauricelargeron.com/wp-content/uploads/2016/04/client-id-google-analtytics-310x195.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2016/04/client-id-google-analtytics.jpg) Fonctionnement du client Id - cookie de GA

Bon Google analytics a  visiblement des ambitions de conquérir de nouveaux adeptes cette année,  et avec cette nouveauté, cela semble bien parti.
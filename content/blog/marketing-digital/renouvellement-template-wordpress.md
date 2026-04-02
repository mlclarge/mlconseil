---
title: "Changer le template de son site web"
date: 2017-08-14
author: "admin"
categories: ["Marketing Digital"]
tags: []
slug: "renouvellement-template-wordpress"
image: "/images/blog/templating.jpg"
---

Révision de vacances pour ceux qui pensent **refaire le look** de leur site web à la rentrée ! Le contexte est celui ici de la petite entreprise, l’auto-entrepreneur, l'indépendant qui souhaite rafraîchir son site,  à partir d’un **CMS du marché, WordPress** pour ne pas le citer. Donc ne pas concevoir mais seulement **changer le Template** avec quelques mises à jour (nouvelle page, visuels) que l’on repousse toujours au lendemain.

## **Faire appel à un prestataire web**

Bon, si on n’est pas de la partie, autant faire-faire si on en a les moyens.  Bon il faudra compter quelques deniers, mais cela dépendra toujours du genre de site. Un site vitrine, ou B2B de présentation d’un service n’aura pas les mêmes contraintes d’un site e-commerce.  Le nombre de pages à retravailler, de contenus à manipuler pourra passer du simple en termes de prix à  presque l’infini !

Faire faire un Template personnalisé par un intégrateur-développeur qui connait bien le cms, du « sur mesure »  pourra coûter entre 1000 et 2000 euros  selon ses fonctionnalités, le type de prestataire (agence, indépendant, stagiaire  :)  )

[![Image](/images/blog/tariftemplate-502x231.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2017/07/tariftemplate.jpg) Exemples de tarifs de prestations

 

Allez voir un site spécialisé sur ce sujet ici : [https://wpformation.com/combien-coute-un-site-wordpress/](https://wpformation.com/combien-coute-un-site-wordpress/) qui reprend les coûts globaux de prestation

## **Changer le Template soi-même, va on y va**

### ***Contexte et compromis***

C’est ce que j’ai fait ici, j’ai abandonné la proie pour l’ombre, je savais que le site précédent était adapté pour du blog pur (template DIYTheme ), mais un peu moins pour de la prospection ou de l’acquisition et nécessitait un relookage plus "up to date" !

J’ai donc fait le tour des vendeurs de Template, me suis documenté sur les plus et les moins de chacun d’entre eux.

En gros,  il existe des Templates prêts à l’emploi, souvent gratuits, rien à faire ou presque rien. Ensuite il y a les premiums, plus sexy, plus riche en fonctionnalités, et puis les Template WISIWIG, gourmand en ressources lors de l’édition d’une page, pas forcément optimisé nativement pour le Seo (balisage et performance d’affichage), parfois lourd dans le codage avec trop de balise de style en ligne mais bon je souhaitais tester moi même ce genre de produit, alors…

### ***Sources intéressantes sur le sujet des Templates***

Guide : [https://bulledev.com/optimiser-wordpress/](https://bulledev.com/optimiser-wordpress/)

 	- 13 plugins Editeur : [https://www.icegram.com/wordpress-plugins/best-editor-plugins-for-wordpress-in-2016/2/](https://www.icegram.com/wordpress-plugins/best-editor-plugins-for-wordpress-in-2016/2/)

 	- Liste de 50 fournisseurs de Template : [https://www.premiumwp.com/the-complete-list-of-premium-wordpress-theme-shops/](https://www.premiumwp.com/the-complete-list-of-premium-wordpress-theme-shops/)

 	- Benchmark Thème WordPress : [https://docs.google.com/spreadsheets/d/195q80B3bJQmGxcwXOmomPNOO1OaFBxsyM0xnUeJ-nmk/edit#gid=901323818](https://docs.google.com/spreadsheets/d/195q80B3bJQmGxcwXOmomPNOO1OaFBxsyM0xnUeJ-nmk/edit#gid=901323818)

On se laissera séduire par les Template aux atours  les plus beaux, mais ensuite c’est une autre histoire….il va falloir passer à l’intégration.

[![Image](/images/blog/tarif-comparateur-template-502x206.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2017/07/tarif-comparateur-template.jpg) Comparatif/Benchmark de fournisseurs de template
## **Mise en œuvre, va on se retrousse les manches**

***Travail à faire de préparationi avant le basculement ***

Dans l’idéal, on travaille sur un **serveur pré-prod**, pour travailler en off, soit de manière distante soit en local, c’est justement l’occasion, une fois que l’on a fait son choix de Template, de pouvoir tester en condition réelle avec les données du site actuel. Donc on peut utiliser un plugin comme .**All-in-One WP Migration **pour installer à l'identique son site web actuel. Il fait une copie complète de la base, des fichiers et de l'ensemble des plugins sur une coquille vide d'un WP en modifiant tout les chemins selon la plateforme utilisée.

Je n’ai sans doute pas fait le meilleur choix, mais en tout cas, pour pouvoir m’en servir comme support de cours pour des thématiques de création de sites, j’ai fait le choix d’un éditeur de Template populaire  de la maison elegantthemes qui donne rapidement de bons résultats. Si l’on souhaite le personnaliser, le support est disponible pour répondre aux questions.  Mais même si tout semble simple avec ce genre de produit, il faudra tout de même toucher :

 	- Aux CSS : Adaptation des formulaires + Customisation des modules + Calage des visuels

 	- Au Seo : Essayer d’exporter via un plugin  «data seo importé », les titres, Méta description de l’ancien Template pour les préparer pour le nouveau plugin dans le cas précis ici, Yoast Seo. Pour des optimisations plus fines (nature des liens), l’intervention d’un développeur sera utile ultérieurement.

 	- A la traduction :Template en anglais, donc traduction via un petit soft poedit qui génère les fichiers de langues standards (po, mo)

 	- Au design :Gabarits de pages selon ses souhaits de départ. Personnaliser les couleurs et fonts au couleur du business.

Dans l’idéal, sur la version off, tous ces réglages devront être exportables pour ensuite avoir juste à les réimporter sur le site live.
***Mise en ligne du nouveau Template***

Phase un peu critique, à faire plutôt le soir ou le week end pour éviter des désagréments visiteurs, cela doit prendre le minimum de temps (30 minutes maxi)

 	- Télécharger les nouveaux plugins et Template

 	- Désactiver les anciens plugins et thème inutiles

 	- Faire une sauvegarde complète de la base et des fichiers

 	- Activer le nouveau thème (et thème enfant)

 	- Régler la navigation des menus et la position des widgets

 	- Importer les réglages du nouveau thème :  Css, Seo, Langues, Design.

Bon voilà les principales étapes, sans toucher au code, ou presque dans ce changement de Template prêt à l’emploi du marché !
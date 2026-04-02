---
title: "12 étapes pour démarrer un test A/B avec Google Optimize"
date: 2017-05-09
author: "admin"
categories: ["Google Analytics"]
tags: []
slug: "premiers-pas-avec-google-optimize"
image: "/images/blog/optimize.jpg"
---

**Google optimize** fait partie de la suite Analytics 360. Elle est en ce moment déployée de manière gratuite mais limitée à 3 expérimentations. Son  avantage c’est qu’elle s’intègre directement la Google Analytics > comportement > test. Voyons comment démarrer l’intégration de cette solution d’optimisation User Expérience et   un premier test

## **Quelle utilisation pour  la solution Google optimize ?**

### ***Principales caractéristiques de la version gratuite par rapport à celle de la suite 360 payante.***

[![Image](/images/blog/comparatifs-versions-299x300.png)](https://www.mauricelargeron.com/wp-content/uploads/2017/05/comparatifs-versions.png)
### *Quoi analyser au final ?*

 	- Type de Pages : accueil, contact, produit, panier, remerciement, résultat de recherche, destination

 	- Objets du la page à tester : navigation, recherche, champs de formulaires, boutons les fameux « call to action », fenêtres pop-up, vidéos, images, les aplats de couleurs, bref, y’a du boulot !

[![Image](/images/blog/test-ab-abn-502x234.png)](https://www.mauricelargeron.com/wp-content/uploads/2017/05/test-ab-abn.png) Tests dans Google Optimize

Quoiqu’il en soit, son intégration avec Google analytics en fait vraiment un outil puissant relié à l’audience que l’on souhaite ciblée. Il est tout à fait possible de pouvoir faire des tests uniquement sur un groupe de visiteurs préalablement segmenté suite à un critère de ciblage comme le montant dépensé, la provenance géographique, le type de produit recherché sur un site etc…
https://www.youtube.com/watch?v=qUEfEXuDtkI&
Aide en ligne Google optimize :

 	- [https://support.google.com/360suite/optimize#topic=6314903](https://support.google.com/360suite/optimize#topic=6314903)

## **12 étapes principales pour démarrer un test A/B  **

 	- 1 Avoir un accès et se connecter à la plateforme  optimize

 	- 2 Intégrer Google Optimize avec Google Tag Manager : récupérer id pour gtm depuis optimise sous la forme gtm-XXXXXX

 	- 3 Se rendre sur gtm et intégration la balise Optimize via le Template prévu dans GTM

 	- 4 installer id optimize dans gtm dans les champs appropriés

 	- 5 Debugger dans chrome pour vérifier si le code est installé

 	- 6 Choisir une alternative  à Gtm avec une intégration classique du code (copier-coller le code en dur dans le site ou la page à tester

 	- 7  Ne pas oublier d’intégrer le second snippet «anti-effet de bord » dans la page pour le test.

 	- 8 Aller dans G Optimize et commencer la   création d’un test

 	- 9 installer l’extension optimize , outil de création de variante de page, obligatoire.

 	- 10 Finaliser les objectifs de trafic (répartition de la charge des  impressions sur page A ou B pour Google optimize)  et de conversions (objectifs GA)

 	- 11 Collecter le Traffic ()

 	- 12 Reporting : Analyser depuis GOptimize et depuis GA pour  valider les optimisations.

Il est recommandé d’attendre au moins 15 jours et un trafic représentatif et significatif du site ou de la page consulté avant de tirer des conclusions.
## **Google optimize : avis d’un data scientist chez ab tasty**

Je vous renvoie sur cette article :

 	- [https://www.abtasty.com/fr/blog/google-optimize-un-avis-de-data-scientist/](https://www.abtasty.com/fr/blog/google-optimize-un-avis-de-data-scientist/)
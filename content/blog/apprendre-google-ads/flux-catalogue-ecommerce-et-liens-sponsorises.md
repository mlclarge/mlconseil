---
title: "Tutoriel campagne adwords pour les offres produits"
date: 2013-04-03
author: "admin"
categories: ["Apprendre Google Ads"]
tags: []
slug: "flux-catalogue-ecommerce-et-liens-sponsorises"
---

Après avoir vu que les campagnes universelles constituent le nouvel horizon du modèle **Google adwords**, regardons de plus près un type de campagne qui fait de plus en plus parler les annonceurs : les **annonces pour offres de produits ***(Product Listing Ads)*** **. Ce style de campagne rassemble  différents acteurs de la tribu Google : Google Merchant center *(arrière-boutique)*, shopping *(vitrine comparateur produit/prix)*, Google adwords sur le moteur de recherche (avec des annonces + images). Autrefois, avant février 2013, le fait d’être sur Google shopping pouvait améliorer sa visibilité dans Google, vu que les annonces s’affichaient comme résultats organiques, gratuitement. Maintenant, elles s’affichent sous forme de liens payants sur la colonne de droite ou juste en dessous du champ de recherche* (position top*) sous forme de **liens sponsorisés**. Les commerçants qui commercialisent des produits à prix fixes sont concernés  au détriment des entreprises de services *(pas de prestations style séjours, voyages, consulting..).*

[![Image](/images/blog/acteurs-adwords-shopping_1-310x238.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2013/04/acteurs-adwords-shopping_1.jpg) Vitrine des offres produits
## **Création d’une première campagne offre de produit (PLA) **

Les ingrédients pour monter ce genre de campagne sont donc :

	- Un catalogue produit matérialisé sous forme de flux (fichier formats txt, xml)

	- Un compte Google Merchant center (bien identifier son domaine)

	- Un compte adwords

	- Une association à opérer depuis son compte adwords avec Google Merchant center (via l’extension).

En effet, cela semble simple ! Pas de texte d’annonces à faire, pas de mots clés à chercher, tout ce fait automatiquement, une seule enchère à choisir. Par défaut, une cible automatique "tout produit" est créée. Le  problème, c’est qu’ici,  on crée une campagne « **tout produit **» sans distinction aucune sur les enchères, les messages de promotion, les produits. On se retrouve dans un modèle monolithique qui ne permet pas de distinguer les produits des uns des autres. Les marges de manœuvre sont réduites,  voici ci dessous schématisé le résultat de ce modèle.

[![Image](/images/blog/structure-campagne_1_1-310x224.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2013/04/structure-campagne_1_1.jpg) Campagne PLA "Tout venant en 5 clics"
## Créer une campagne avancée pour offre de produit 

**Rappel sur l’exclusion de termes **: N’oublions pas que les **mots clés à exclure** sont disponibles au niveau campagne et groupe d’annonces qui permet de restreindre des impressions sur des requêtes non ciblées. Un **attribut booléen** existe aussi pour le flux  « adwords_publish ».  Les  supports de diffusion sont par défaut tous les terminaux (pc, tablettes, mobiles) via les campagnes universelles.

### Les filtres au niveau des paramètres de campagne

Afin d'affiner une parution, il faudra faire appel aux  attributs dédiés adwords* (voir dessous définition : source google).*

[![Image](/images/blog/attributs-adwords_1-310x74.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2013/04/attributs-adwords_1.jpg) Définition attributs dédiés Adw

Bien heureusement, adwords donne ces cartouches pour les annonceurs soucieux de **segmenter leur publicité**. Au niveau de la campagne, cela va se traduire par des filtres qui vont reprendre ces attributs,  l'objectif  est ici  d’agir sur un sous ensemble de produits *(différents des cibles)*.  Pour ceux qui sont familiers des filtres dans google analytics, l'idée en est la même. Une fois votre flux bien catégorisé en amont dans GMC, il est possible de ne laisser passer donc que la catégorie de produits voulue, par exemple, par l’attribut « product type » .

[![Image](/images/blog/filtres-extensions_1-310x169.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2013/04/filtres-extensions_1.jpg) Filtres "product type" extension niv. campagne
### Les "cibles produits" à l’échelle.. des produits.. logique !

Ces dernières permettent de sélectionner les produits susceptibles de s’afficher et se situe en aval par rapport aux filtres *(qui excluent le reste du flux). *Il convient dans ce cadre-là, d’utiliser les attributs de flux adwords mis à disposition du flux dans GMC afin de pouvoir mieux segmenter ces cibles. Notons que l’**attribut « étiquette **» ou « labels » permet de jouer sur les CPC, alors que l’ « **adwords grouping** » permet des regroupements de produits *(un peu comme les libellés de campagne)* comme par exemple la saisonnalité, la gamme, le modèle, le fabricant.

[![Image](/images/blog/cibles-produits_1_1-310x146.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2013/04/cibles-produits_1_1.jpg) Cibles produits selon attributs Adw
### Une structure de campagne orientée avec pour condition «l' id » du produit

[![Image](/images/blog/granularite-campagne_1-310x174.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2013/04/granularite-campagne_1.jpg) Structurer une campagne PLA

Afin de jouer sur la granularité de la campagne offre produit, ***Martin Roettgerding***, suggère une méthode qui va individualiser chaque entité de la campagne. La mise en œuvre, pour gagner du temps,  se fera via **adwords editor** et s’appuira  sur le flux produit. Objectif encore, individualiser les groupes d’annonces, les conditions de ciblage produit sur la base de l’ « id ».

[![Image](/images/blog/cible-automatiques_1-310x175.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2013/04/cible-automatiques_1.jpg) Structure selon "id" du produit

Le grand désavantage de cette méthode est le fait qu’il faille refaire cette manipulation à chaque nouvelle mise à jour du catalogue. En revanche, les avantages sont d’une part une plus grande **flexibilité des enchères**, des textes de promo, et d'autre part, l’usage des **règles automatique**s et des scripts qui  deviennent possible avec un  reporting sur les **termes de recherche** plus lisible vu l’adjonction du nom du groupe à côté des mots de recherche. Un dernier conseil est de rajouter une campagne "tout produit" *(celle par défaut évoqué plus haut)* avec des cpcs inférieurs à ceux ciblés, afin de toucher les nouveaux produits pas encore mis à jour.

## Analyse du ROI de ces PLA

Comme à l’accoutumée, selon la stratégie d’enchères définie et le modèle éco. du site , les indicateurs comme les **CPC**,  le nombre de **conversions**,  leur coût sont à comparer avec des campagnes plus traditionnelles. De plus  l’outil de tracking « **[url de suivi dynamique ](https://support.google.com/adwords/answer/2549100?ctx=tltp)**»  *(niv. Campagne)* ou l’ajout d’**urls de destination** *(des cibles de produits)* permettent de suivre les performances de chaque clic.  Il semblerait cependant que ces statistiques démontrent une rentabilité qui restent à prouver.  Alors est-ce dû à des effets du marché qui surévalue les cpc, à des structures de campagne inadéquates, à une certaine latence liée à l’historique dans le cadre de récentes campagnes ?  Les commentaires "**Roistes"** sont les bienvenus !
** Infos pratiques**

	- [Démarrer sa campagne](http://support.google.com/merchants/bin/answer.py?hl=fr&answer=188479)

	- [Classification produits ](http://support.google.com/merchants/bin/answer.py?hl=fr&answer=1705911)

	- [Modèle amazon Vs Google Shopping ](http://searchenginewatch.com/article/2249526/Google-Shopping-Beats-Amazon-Product-Ads-on-Costs-Traffic-Not-Conversion-Rate-Study)

	- [Suivi du ROI (rsi)](http://support.google.com/adwords/answer/2456108)
---
title: "Optimisation du chemin de conversion"
date: 2017-08-21
author: "admin"
categories: ["Google Analytics"]
tags: []
slug: "analyse-parcours-client"
image: "/images/blog/OPTIMISATION-DU-PARCOURS-CL.jpg"
---

L’analyse des **chemins de conversion** en ligne est quelque chose de complexe, voilà pour fixer le niveau du sujet :) . Cela tient à la nature même de celui qui en est maître du jeu : l’internaute.  Il y a de nombreux comportements dans ce monde qui se numérise à vitesse grand V et autant d’usages liés. Les **points de contacts** sont matérialisés par les smartphones, objets connectés, bornes, site web, applications, tv  où l’internaute est soumis aux messages publicitaires de l’annonceur via des leviers comme l’email, display, SEM. Comment définir et analyser le chemin de conversion dans ce contexte riche et varié ? J’expose ici à grands traits les 3 concepts à connaître pour devenir un geek de l’analyse du parcours client : **parcours visiteur, attribution, contribution, déduplication.**

[![multidevice-502x209.jpg](/images/blog/multidevice-502x209.jpg) Points de contacts du parcours visiteur
## **Construire, baliser le parcours de l’internaute**

Tout est mesurable en ligne, et même hors ligne maintenant quasiment. Bref, pour analyser le chemin du visiteur/client, il faut collecter, et pour collecter il faut ‘marquer’ tout le trafic qui arrive sur le site pour optimiser le parcours client.

Illustrons par ce propos par la représentation d’un chemin de conversion établit par le CPA dans un de  ses livres blanc, ou la métaphore d’une chaîne de production est utilisée pour représenter la réalisation d’une conversion : seo, blog affilié, email, display, brand SEM, coupon.cashback.

[![chemin-de-conversion-502x168.jpg](/images/blog/chemin-de-conversion-502x168.jpg) Chemin "type" de conversion

La représentation de ce parcours  est réalisée via l’intégration d’une solution d’analyse d’audience qui va automatiquement relever  les canaux apporteurs de trafic mais qui faudra ensuite personnaliser selon les campagnes menées. La pose de variable « UTM » par exemple pour l’application Google analytics est un moyen pratique et facile.

[![chemin-de-conversion-classique-dans-google-analytics-502x123.jpg](/images/blog/chemin-de-conversion-classique-dans-google-analytics-502x123.jpg) Chemin classique vu dans Google analytics
## **Attribuer la conversion **

### ***A qui « attribuer »  la conversion  une fois le chemin balisé ?***

Je reprends la définition simple que donne Mazeberry, une de nos start-ups Française **: « L’attribution est une méthode d’analyse de la performance des canaux marketing. ». **Donc, premier élément à retenir, l’attribution, n’est pas obligatoire ! En effet, si un seul levier est impliqué dans une vente, rien ne sert de s’en préoccuper. Bon, en clair, celui qui fait qu’uniquement de l’Adwords, n’a pas besoin d’attribution. L’étude de Mazeberry indiquait d’ailleurs que plus de 54% les taux de conversion étaient multitouche et 45% monotouche (tou de même !).

Dans Google analytics, nous sommes par défaut, dans un modèle last clic , donc le dernier dans le chemin analysé remporte la timbale. Prenons ici un extrait et au final analysons le canal le plus apporteur en volume de conversions.

[![chemins-de-conversion-502x170.jpg](/images/blog/chemins-de-conversion-502x170.jpg) Last clic dans GA
### ***Quelle méthode ou "modèle" utiliser ?***

Principalement, au-delà du Last click, la traditionnelle, il existe d’autres méthodes basées sur des règles, que l’on peut d’ailleurs appliquer  dans Google analytics. Ces méthodes vont dépendre du modèle de business :

 	- Leader sur le marché : Bien faire la part des choses entre les leviers naturels directs et ceux issus de campagne hors marque en début de chemin.

 	- Cycle long ou court : les leviers inbound pour les cycles longs seront récompensés,  en revanche pour les campagnes SEM pour de la décision d’achat à court terme seront priorisés.

 	- Clientèle volatile : le facteur prix est-il déterminant, alors les leviers à la performance seront valorisés comme le couponing/cash Back.

 	- Puis de plus en plus, et google le fait pour Adwords, l’attribution peut être traitée algorithmiquement ! On appelle cela , data driven attribution.

[![attribution-502x181.jpg](/images/blog/attribution-502x181.jpg)

## **Analyser finement la contribution de chaque levier pour la conversion**

L’idée ici est de ce dire, au-delà de la présence des leviers et de l’affectation des budgets selon            le modèle de business, quels sont les rôles intrinsèques de chacun des leviers ?  Cela devient intéressant dans l’analyse du ROI, de déterminer comment s’enchainent le plus favorablement les différents canaux dans le ou les  parcours les plus rentables. La solution mazeberry  intègre parfaitement dans sa plateforme cette analyse avec une typologie composée de 4 rôles :

 	- Initiateur : attention dans le tunnel de vente

 	- Passeur :  met en avant l’Intérêt du visiteur

 	- Buteur : finalise à souhait la conversion

 	- Autonome : peut se débrouiller tout seul

[![contribution-analytse-502x292.jpg](/images/blog/contribution-analytse-502x292.jpg)

Ainsi, la contribution sert à optimiser son mix marketing et à arbitrer selon les résultats des leviers engagés dans une stratégie d’acquisition. Les performances projetées sur les canaux sont elles au rendez vous ?

## **Rétribuer les canaux à la performance : la déduplication**

La déduplication sert à éviter de payer 2 fois pour une seule acquisition. C’est une négociation qui s’engage avec les apporteurs d’affaires qui travaillent dans un modèle à la performance. Si tu vends, je te paye. Oui mais le problème se pose, lorsque le modèle de rétribution est mal défini et où parfois, 2 affiliés remontent l’attribution d’une conversion.  Le commissionnement basé sur des règles claires doit être mise en place, pour rétribuer chacun, selon son rôle dans le déclenchement de la conversion. Alors pourquoi la déduplication ne s’applique pas au modèle cpm ou cpc ? Question piège…tout simplement le fait que ce levier ne soit pas à la performance, ou prépayé en quelque sorte, ne nécessite pas de calcul de rétribution J .

[![deduplication-502x236.jpg](/images/blog/deduplication-502x236.jpg)

## **Par où commencer  alors l’optimisation du parcours client ?**

Rien est obligatoire au final, que ce soit l’attribution ou la déduplication , cela est fonction de sa problématique. Je reprends ce tableau synthétique qui résume bien les choix selon son cas.

[![presentation-attribution-deduplication-mazeberry--502x282.jpg](/images/blog/presentation-attribution-deduplication-mazeberry--502x282.jpg)

Alors au final nous pouvons avoir un modèle complexe, où les chemins de conversion cumulent à la fois du CPC/CPM + CPA pour établir un Cout final d’acquisition. C’est dans ce contexte où ces notions concepts d’attribution, contribution, déduplication prennent tout leur sens.
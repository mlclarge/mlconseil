---
title: "Dessine-moi un graphique"
date: 2015-05-26
author: "admin"
categories: ["Google Analytics"]
tags: []
slug: "les-rapports-graphiques-dans-ga"
---

Le reporting visuel au service de l'analyse d'audience et du pilotage d'une stratégie **webmarketing**. Vaste sujet que je ne vais qu’effleurer dans l’article d’aujourd’hui au travers de **Google Analytics **et de ses graphiques. Pour les geeks de la **Business Intelligence **au sens large, je conseille la visite du site-blog  de [Stephen Few ](http://www.perceptualedge.com/examples.php) *(US, merci à B. Arson pour cette ressource)* .  Pour illustrer ce thème,  j'utiliserai 2 axes d'approche : Chronologie et de comparaison. **Chronologie** pour avoir une tendance,  et **comparaison **pour apporter  du recul dans la reflexion . Pour fil rouge une collecte basique de data  sera utilisée provenant des sources d’acquisition de trafic sur un trimestre. A vos graphiques ! Petite révision à suivre , avec ensite des exemples de reporting graphique...

## ***Recette pour créer un graphique dans GA ***

Petits rappels fondamentaux sur la **notion de graphique.** Quels sont les ingrédients pour bâtir une  simple courbe par exemple ? Quelques éléments de méthode...

Un graphe est constitué issu du  croisement de 2 types de données tabulaire : une statistique (nombre, %, taux de couleur bleue dans GA)  et une variable , unité insécable  (appelée dimension dans google analytics de couleur verte) .  Le but est de synthétiser une idée et la rendre  « communicable » d’une manière visuelle au détriment d’une exhaustivité rendue par un tableau en lignes et colonnes. Avant de faire un graphique, il faudrait se poser ce genre de questions :

	- Quel est le sujet ? de quoi parle-t-on ? : ex : progression des visites sur une trimestre

	- Objectif de la représentation : Le but de la démonstration ? -> Soulignez un regain de trafic

	- Destinataire  ? Pour quel type de public  ? -> Trafic manager

	- Comment ? Type de graphique ? -> Courbe, Bâtons, Camembert

	- Avec quoi ? -> Quel couple de  statistique et dimension -> Sessions (statistiques) et Mois (variable temporelle). Le 5ème élément :) est sans doute celui le plus délicat à choisir.

[![elements-graphique.jpg](/images/blog/elements-graphique.jpg) graphique : elements de fond.

Gardons l’exemple d’une représentation simple trimestrielle . Dans google analytics, pour avoir un graphique personnalisé il faut utiliser la fonctionnalité  calendrier soit dans les rapports standards,  soit dans les tableaux de bord. Dans ces derniers, Google analytics ne fournit ici qu’un graphique à courbes journalier, donc difficile de **dégager une tendance de fond**. mais uniquement une série de vagues pas très parlantes. En tout cas, gardons à l’esprit que GA ne garde rien en sauvegarde !

[![evolution-trimestrielle-visites-310x168.jpg](/images/blog/evolution-trimestrielle-visites-310x168.jpg) Evolution trimestrielle vu par Tab. Bord

Il faut allors passer par un rapport personnalisé  mais…c’ est qu’il n’y a pas de graphique au bout , seulement la fourniture d’un tableau !

[![rapport-simple-GA-310x115.jpg](/images/blog/rapport-simple-GA-310x115.jpg) Rapport perso. GA : raw data

Solution ? Passer par l’**export depuis le rapport personnalisé** vers des tableurs externes, prenons ici celui du cloud google : G. Sheets. ..Il faudra ensuite convertir le chiffre du mois sous format texte.  En effet, l'exportation de donnée calendaire se fait sous format  numérique  dans GA :  : ex -> "01" pour "Janvier" , il faudra donc utiliser cette petite formule :

=TEXT(DATE( 2015 ; VALUE( RIGHT( A1 ; 2 ) ) ; 2 ) ; "MMMM" )

[![google-sheet-et-g-analytics-310x185.jpg](/images/blog/google-sheet-et-g-analytics-310x185.jpg) G Sheet pour VIsualiser et conserver

Voyons maintenant quelques cas de graphiques  pour analyser des tendances...
## ***Rapports évolution 2014 – 2015 trimestriel***

### *Tendance générale*

Plusieurs méthodes dans Google analytics peuvent amenées des rendus équivalents.  L’analyse se fait sur le cumul de sessions sur une durée de 3 mois. On observe sur la période 36 % de trafic supplémentaire.

[![evolution-visites-sur-trimestre-comparés-310x197.jpg](/images/blog/evolution-visites-sur-trimestre-comparés-310x197.jpg) Evolution Comparée Trafic total
### *Focus sur un canal*

Il est possible ensuite d’aller cherche l’analyse sur un seul canal, par exemple celui issu des résultats naturels.  L’usage de l’outil segmentation permet d’arriver  à nos fins. Ici  l’augmentation observée atteint  65 %. Le graphique par courbes par année souligne cette tendance, et les données de détails sont sous forme de table.

[![evolution-trimestirelle-sur-le-canal-organique-310x253.jpg](/images/blog/evolution-trimestirelle-sur-le-canal-organique-310x253.jpg) Focus Canal Organique 2014 - 2015
### ***Détail sur l’évolution dans la période comparée***

Ensuite si l’analyse veut porter sur le détail à l’intérieur d’une période donnée, ici le trimestre, il est alors possible d’y adjoindre une donnée secondaire correspondant à une sous période, le mois. L’inconvénient de GA, c’est que données mensuels sont numérique avec par exemple 1 pour janvier, 2 pour février etc..

[![evolutio-ncomparée-trimestrielle-avec-détail-par-mois-310x256.jpg](/images/blog/evolutio-ncomparée-trimestrielle-avec-détail-par-mois-310x256.jpg) Détail mensuel par trimestre
## ***Dessiner des courbes et des Bâtons pour mesurer la performance***

### ***2 façons de Tracer des courbes dans GA !***

Pour tracer des courbes au niveau du graphique, en dehors du fait que dans ce rapport personnalisé, il faut être en mode explorer et non statique (tableau), il faut utiliser le bouton « tracer les lignes », il plutôt donc « courbes »

[![courbes-repot-ga-310x177.jpg](/images/blog/courbes-repot-ga-310x177.jpg) Tirer des courbas dans GA

Il est aussi possible d’utiliser les graphiques dynamiques et notamment celle dédiée aux courbes. C’est une autre façon, plus rapide de dessiner des tendances d’évolution. A tester sans tarder…

[![tendances-par-courbes-evolutioin-seo-310x294.jpg](/images/blog/tendances-par-courbes-evolutioin-seo-310x294.jpg) Des courbes par différents chemins
### ***Les histogrammes dans GA***

Le choix n’est pas trop varié en terme d’histogramme  dans GA. Si  l’on reste dans les rapports personnalisés, ils existent  les graphiques dynamiques qui permettent en 2 dates d’avoir un graphique à bâtons animé. Attention c'est de la dynamite !

[![grahipues-dynamiques-310x200.jpg](/images/blog/grahipues-dynamiques-310x200.jpg) Graphipue dynamiques à Bâtons

Cet outil qui anime la **data ne donne pas la possibilité de comparer des période**s. Pour cela il faudra recourir à des tableaux de bord. Par exemple, une comparaison de dimensions comme celles reliées aux supports : organic, referral, direct (none),  .  Le visuel est tricolore, une couleur pour chaque période, avec hachurée en grisée la période antérieure.

[![graphique-barre-couchée-comparée-310x241.jpg](/images/blog/graphique-barre-couchée-comparée-310x241.jpg) WIdget de tableau de Bord Comparatif à Barres

Bon voilà pour ce petit tour rapide de la visualisation des données dans GA.

### ** Ressources de la semaine**

	- Tutoriels pour faire un graphique : http://www.mdf-xlpages.com/modules/publisher/item.php?itemid=178

	- Rapports perso. dans GoogleSheets: http://bit.ly/RapPersoExportTrimestre2015
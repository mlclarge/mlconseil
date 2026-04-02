---
title: "Focus sur le \"RSI\" des sources de trafic"
date: 2013-10-23
author: "admin"
categories: ["Google Analytics"]
tags: []
slug: "analyse-roiste-du-mix-marketing-avec-mazeberry"
---

La  dernière **conférence sur Google Analytics** qui s’est tenue à Mountain View  en ce début d’octobre fut riche en informations et cela tous azimuts *(api, premium, Ua)* . Les products managers annonçaient de nouvelles fonctionnalités dont notamment le déploiement sur la version de GA  gratuite :

	- D’une segmentation plus élaborée, centrée visites et visiteurs

	- D’une rubrique refondue orientée sur l’analyse des leviers  de trafic (acquisition, comportement, conversion)

	- De nouvelles données sociales démographiques (âge, sexe)

	- Du tagage automatique d’évènements depuis Google tag manager

	- De l’amélioration sur la gestion du balisage remarketing  doubleclick

Je  reviendrai  sur certains points plus  précisément dans un prochain billet, mais ces annonces peuvent en cacher aussi d’autres, moins visibles mais tout aussi utile pour parfaire son analyse d’audience  comme **la sortie de la version 2.5 de Mazeberry Express**.  J’ai pu présenter dans un précèdent article la présence de cet outil dans l’écosystème de Google analytics.  Je profite donc  du lancement des dernières fonctionnalités  comme les **rapports de fréquence**,  la  refonte de** la segmentation**   pour en parler aujourd’hui.  Voyons dès à preésent  l’ intérêt de l’outil, son  installation,  son interface et fonctionnalités, et  enfin la production de son reporting au travers un cas d’usage *(les  illustrations sont basées sur la version démo de MBY).*

## **L’intérêt de cette application**

### *Petit rappel sur le produit*

**Mazeberry** est une application complémentaire à Google analytics. Elle permet une "**analyse ROIste**" que ne peut pas faire la version brute de Google analytics. Comme le dit si bien Fabien Dutrieux, cet outil  fait du reporting  complet, alors que GA.  Est une apps de pilotage.  Son focus porte sur une **analyse des leviers web marketing** *(affiliation, liens sponsorisés, seo etc..)* : trace leur rentabilité, leur performance dans le** mix-marketing**.

### *Méthode PASID : une analyse complète de l’impact des sources de trafic. *

Il convient avant de se lancer dans la lecture des tableaux, de prendre quelques minutes pour identifier et qualifier les statistiques de MBY basées sur 5 modules  axés sur les leviers d’acquisition dont :

	- La **P**résence (Canal  visible au moins 1 fois de la source du trafic)

	- Son **A**ttribution (le poids de ce levier dans la transformation, la vente)

	- Sa  **S**egmentation (dans le cadre d’une conversion multicanal, le moment de l’apparition du levier dans le chemin : début, milieu, fin)

	- Son **I**nteraction (les combinaisons de leviers)

	- **D**écision (matrice d’aide à la décision qui synthétise les 4 items précédents)

## **Installation de Mazeberry**

### *Mise en œuvre de l'application*

MB est une solution Saas, donc pas d’installation en local, un simple login et password suffisent pour avoir l’accès aux rapports. L’importation des statistiques de Google analytics se fait depuis la plateforme MBY,  il faut connecter votre compte Google Analytics  à analyser, en choisir le principal profil/vue  (si vous en possédez plusieurs), et Mazeberry se charge ensuite d’importer vos données de GA en toute confidentialité grâce à  son API.
Il suffit ensuite d’intégrer les 3  données  qui permettront l’analyse Roiste  :

	- les **dépense**s des différents leviers

	- les **visites** par levier *(automatique pour l’appli. AT Internet)*

	- le** taux** de marge si possible. Et that’s it !

[![mazeberry-couts-visites-310x176.jpg](/images/blog/mazeberry-couts-visites-310x176.jpg) Importation des données de couts dans MBY
## **Interface et fonctionnalités**

### ***3 entrées : Infographie, Rapports et Leviers***

Un reporting qui peut se faire selon 3 types de visualisation selon la  cible des destinataires *(décideurs, marketeur, analyste)* .

**1/** **Infographie** : avec pas moins de 5 tableaux  dont 1 synthèse globale (utile au dirigeant avec des Kpi comme le CA, dépenses,  Cpa, Audience) qui résume l’essentiel plus  une vision cumulée sur les différents leviers présentés par modules  (Attribution, Présence, Interactions, Segmentation)

[![interface1-310x124.jpg](/images/blog/interface1-310x124.jpg) Extrait présentation 1 :  Infographique M.

**2/** **Focus sur les rapports** : Avec un menu qui donne accès à des **rapports standards & à des rapports avancés**. L’idée ici, est de rentrer dans les variables du mix marketing par la méthode PASID et de donner du contexte sur l’apport de chaque levier entre eux et dans les chemins d’accès multicanaux vers le graal de la conversion.

-> 21/ les  Rapports analytics recensent

	- l’**Attribution multitouch** (la rentabilité et taux de conversion,  des données tabulaires assorties d’un graphique)

	- Une vision sur la **Segmentation** (identification du potentiel des leviers)

	- Une vue sur le degré de **Présence des leviers** (présent, absent ?)

	- Une entrée sur la pondération des modèles d’Attribution (**derniers clics Vs Exponentiel** croissant par exemple)

	- Une **Synthèse globale** (matrice Décision, analyse SWOT): une des nouveautés de ce printemps 2013.

[![interface-mazeberry-25-310x253.jpg](/images/blog/interface-mazeberry-25-310x253.jpg) Screenshot Interface 2 :  "rapports"

-> 22/ Les rapports avancés

	- **Contribution** (évaluation des leviers dans leur aptitude à finaliser une conversion)

	- Plus des **ratios d’assistance** (qui donnent en 1 clin d’œil la part de l’apport de chacun des leviers entre eux).

	- **Intéraction** et le mix marketing (identification de couples de leviers pertinents dans l’obtention de la conversion)

	- **Fréquence** (exposition du visiteur aux différents canaux et identification du nombre de visites nécessaire à la conversion : nouveauté 2.5 ! )

	- Comparaison de l’attribution (**synthèse médiane des différents modèles d’attribution**).

**3/ Loupe sur les leviers**

Ici, MazeBerry propose une entrée directe non pas par les piliers de PASID, mais tout simplement directement par les leviers, accessible depuis le menu latéral gauche. C’est une vision rapprochée d’un levier précis  sans comparatif concurrentiel direct avec d’autres canaux. Cela peut compléter  la présentation  des rapports standards vue plus haut.

[![focus-leviers-310x143.jpg](/images/blog/focus-leviers-310x143.jpg) Vue 3 :  "Focus leviers"

Pas moins de 13 leviers  (cashback, Seo, AdExchange..) ont été paramétrés dans l’illustration avec pour chacun d’eux des indicateurs comme :

	- Kpi globaux de rentabilité (CA, Conv, Tx de C., Panier Moyen, Tx d’exclu.)

	- les dépenses (globale, cpa, roas, Roi, Tx de Pub)

	- les visites (nombre, segmentation, présence)

	- Mix Marketing (identification des couples de leviers dominants)

	- Matrice Swot

## **Cas pratique : Analyse d’un levier -> Adwords**

Prenons un cas pratique et rentrons sur la plateforme MBY avec un objectif précis, l’analyse du levier de trafic adwords.

### *Entrée par l’interface sur le focus des rapports *

Cela rapporte adwords ?

Comme tout bon professionnel du web marketing, je me focalise avant tout sur **la rentabilité** de mes dernières dépenses en **campagne adwords** (non marque). Je consulte le **rapport sur la rentabilité** dans les "focus sur les rapports" ! Une des nouveautés de la version 2.5 est l'intégration de la variable "**taux de marge**" qui sépare  le **ROAS** (return on advertising spending: analyse sur le retour des couts de pub.) du **ROI** (profitabilité avec intégration du taux de marge après déduction des dépenses publicaires).

[![adwords-rentabilite-310x248.jpg](/images/blog/adwords-rentabilite-310x248.jpg) Focus sur les rapports : "Rentabilité"

Bien que le CPA soit satisfaisant, le ROAS  est faible et l’impact sur le ROI (RSI)  laisse apparaitre un indicateur dans le rouge :(  .
Essayons d’aller voir plus loin..

Je consulte le reporting sur la **segmentation pour identifier la valeur de ce canal**, et je m’aperçois que MazeBerry attribue ce levier comme étant « passeur » donc sans doute utile dans la chaîne de valeur  !

[![adwords-segmentation-310x111.jpg](/images/blog/adwords-segmentation-310x111.jpg) Quelle influence  a le canal  étudié ?
Que vaut réellement cette source de trafic ?

Je fais confiance à Mazeberry :) , avec ces ratios et notamment ceux qui évaluent**  l’exclusivité et l’assistance**. J’en déduis que seul, (0.18) adwords n’apporte pas grand-chose, mais contribue fortement (0.82) dans la construction des  chemins multicanaux de conversion.

[![adwords-assistance-conversioin-310x140.jpg](/images/blog/adwords-assistance-conversioin-310x140.jpg) Quelle efficacité  levier dans la chaine de valeur ?
Matrice de décision, que vais-je faire avec cet outil  ?

Je décide, pour me rassurer, de corréler 2 variables (**Chiffre d’affaires et CPA**), pour situer Adwords vis-à-vis de ces camarades.  Finalement, pas premier, certes, mais en milieu de tableau, il contribue concrètement au CA, en ayant un **CPA  moyen à l’acquisition**.

[![adwords-matrice-decision-310x178.jpg](/images/blog/adwords-matrice-decision-310x178.jpg) Graphe "customizable" : ici C. Affaires / CPA
Alors efficace ce levier ADW ?

Le** détail par levier** peut m'indiquer son efficacité  dans l'obtention d'une vente. Faut-il réellement beaucoup de visites pour convertir ? Apparemment non, puisque ici, il se positionne comme second en "nombre moyen de visites"  avant la conversion et efficace vu le "nombre de visites" après son intervention.

### *Entrée par les focus sur les leviers*

Quels sont les meilleures recettes nuptiales du Mix ?

Cette fois - ci, il faut aller sur « focus sur leviers » pour avoir l’essentiel des combinaisons avec lesquelles adwords s’encanaille.

[![focus-levier-adwords-310x140.jpg](/images/blog/focus-levier-adwords-310x140.jpg) Quels sont les couples de canaux dominants ?

Finalement, bien qu’apparemment pas d’une rentabilité extraordinaire, sa **contribution positive** avec le reste de l’écosystème des leviers e-marketing, m’incite à lui donner encore quelques budgets mais en essayant sans doute d’optimiser les annonces de mes campagnes ;) .

## Mazeberry une éclaircie pour l'analyse multicanal ?

Sans doute,** Mazeberry** est l'outil pratique pour les organisations qui souhaitent rapidement, sans développer des tableurs dédiés,  analyser tous leurs leviers de trafic. Cette application permet d’**importer ces données GA et donc de les conserver** ! Google analytics en version gratuite reste limitée aux derniers 24 mois ne l'oublions pas !
Plus d'informations : [http://www.multitouchanalytics.fr/](http://www.multitouchanalytics.fr/)
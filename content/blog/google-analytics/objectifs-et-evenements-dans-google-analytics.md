---
title: "Analyse des actions visiteurs avec Google analytics"
date: 2012-02-01
author: "admin"
categories: ["Google Analytics"]
tags: []
slug: "objectifs-et-evenements-dans-google-analytics"
---

L’article de la semaine dernière portait sur l’analyse de l’audience selon des indicateurs liés au référencement d’un site. Allons plus loin dans l’analyse cette fois-ci et intéressons-nous  au « **comment puis-je mesurer les interactions visiteurs par rapport à mes formulaires, panier e-commerce, vidéos, téléchargements mis à disposition " **? . Les termes  « ** d’objectifs **»  et  « **d’évènements** » entrent en jeu ici. Dans un premier temps, je m’attacherai à décrire ce qu’est un « objectif », puis dans un deuxième chapitre, parlerai des « évènements ». Cet article est inspiré de [ce billet](http://www.hmtweb.com/imd/?p=56), de lectures diverses, de témoignages  venus de  propriétaires de sites.

[![Image](https://www.mauricelargeron.com/wp-content/uploads/2012/02/menu-google-analytics-148x300.png)](https://www.mauricelargeron.com/wp-content/uploads/2012/02/menu-google-analytics.png) Fig 1 Menu Google Analytics
## **Objectifs (conversion)**

Les objectifs correspondent à l'atteinte d'un but précis.  Il est **le résultat d’une action.** Vous pouvez mesurer cette action de 4 façons  différentes et lui attribuer une valeur personnalisée.

[
![Image](https://www.mauricelargeron.com/wp-content/uploads/2012/02/objectif1-300x178.png)](https://www.mauricelargeron.com/wp-content/uploads/2012/02/objectif1.png)Fig. 2 Paramétrage objectif "page" en 3 étapes

Si  vos pages ne sont pas « distinctes », il y a moyen de créer des **pages virtuelles**, cet article décrit pas à pas la procédure  de [création de pages virtuelles dans Google analytics](http://www.adviso.ca/blog/2008/08/15/pages-vues-virtuelles-google-analytics/) . Voici des exemples d'objectifs :

	- Temps passé sur le site

	- Pages consultées  par visite

	- Atteinte page de téléchargement d’un document

	- Atteinte page de remerciement lors du remplissage d’un formulaire d’inscription à une newsletter.

	- Une page précise de destination*** (création possible d’un entonnoir de conversion)*** comme la page de remerciement après achat avec  le suivi du cheminement via différentes pages (voir fig. 2 et fig 3).

[![Image](https://www.mauricelargeron.com/wp-content/uploads/2012/02/entonnoir2-300x157.png)](https://www.mauricelargeron.com/wp-content/uploads/2012/02/entonnoir2.png) Fig. 3 Paramétrage entonnoir conversion et rapport

 Le suivi des 5 premiers objectifs cités ci-dessus ne nécessite **aucun ajout de code de suivi**, seulement, connaître le chemin exact de chaque page *(ou URI).*
       6. Un Evènement ***(j’y reviens dans le détail dans la seconde partie de l’article)***

**Macro et micro conversion** : Il est intéressant de  pouvoir distinguer des macro-conversions *(achat par exemple)* des micro-conversions *(téléchargement gratuit)* cela donne de la graduation dans l'importance des indicateurs. Elles devront cependant être pensées en amont du projet d’analyse  afin de n’avoir qu’à définir logiquement une typologie de conversions (ou objectifs) lors de la mise en place du suivi d'audience. Le nombre de conversion par profils est **20 maximum par tranche de  5**, si un besoin plus important se fait sentir, il faudra démultiplier le nombre de profils.

### **Evènements **

Dans l’ancienne version d’analytics, les évènements étaient traités à part, en effet, ils nécessitent l’ajout** d’une portion de code au code analytics** existant avec  un paramétrage de la méthode de collecte des données. La nouvelle version 5 permet donc un paramétrage centralisé des objectifs dont les" évènements" font partis.

[![Image](https://www.mauricelargeron.com/wp-content/uploads/2012/02/evenement-300x206.png)](https://www.mauricelargeron.com/wp-content/uploads/2012/02/evenement.png) Fig 4. Paramétrage Evènement (théorie & pratique) 

Un évènement par rapport à un objectif peut se distinguer dans le but poursuivi par chacun. Un objectif a** souvent comme dessein une url**, alors qu’un **évènement s’intéressent à l’action faite** sur ...

	- Des éléments de page intégrés

	- Des Gadgets

	- Des téléchargements de fichiers (bouton soumettre)

	- Des Temps de chargement

	- Des Eléments en flash

	- Des Lectures de vidéos

Lecture dans Google analytics du rapport « Evènements » (fig. 3)

[![Image](https://www.mauricelargeron.com/wp-content/uploads/2012/02/rapport-evènements-google-analytics.png)](https://www.mauricelargeron.com/wp-content/uploads/2012/02/rapport-evènements-google-analytics.png) nouveautésAdwords2012
**Paramétrages avancés sur les évènements **

Pour mémoire, la limite du nombre d’évènements est 500 par session !

Les événements « uniques » sont ceux qui se déroulent lors d’une même session par un visiteur.

La lecture des évènements est indépendante du nombre de pages vues. En revanche**, si vous usez des pages virtuelles** afin de suivre des clics d’internautes sur une vidéo, cela faussera le nombre de pages vues, à chaque clic, 1 page vue sera incrémentée car google analytics ne fait pas la différence entre pages réelles et pages virtuelles.

Pour améliorer donc le reporting, il sera possible  :  :

1/  De créer un **segment avancé** : la catégorie  ou l’action de l’évènement  est égal au nombre de vidéo vues sur l’ensemble des visiteurs.

2/  D’établir un **rapport personnalisé** qui croisera le critère de l’événement avec le nombre de visites.

Plus d'infos : [http://support.google.com/analytics/bin/answer.py?hl=fr&answer=1033068](http://support.google.com/analytics/bin/answer.py?hl=fr&answer=1033068)
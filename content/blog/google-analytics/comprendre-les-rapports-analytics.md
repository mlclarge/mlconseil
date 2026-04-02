---
title: "Tutoriel sur les rapports personnalisés google analytics"
date: 2012-02-15
author: "admin"
categories: ["Google Analytics"]
tags: []
slug: "comprendre-les-rapports-analytics"
---

Ce billet sur les rapports personnalisés clôture la série de 4 articles sur l’audit de site démarrée en janvier,  dont le sujet dernier avait  pour thème les [variables personnalisées dans Google analytics.](https://www.mauricelargeron.com/analyse-avancee-du-suivi-internaute-de-son-site/) Cette fois-ci  intéressons-nous aux rapports entièrement personnalisables,  fonctionnalité disponible  dans GA depuis avril 2008, elle s’est considérablement améliorée depuis avec notamment avec la possibilité de créer des rapports plus puissants (présentation, sous ensemble de données). Mais quels sont les avantages des rapports personnalisés par rapport aux rapports habituels ?

[![Image](https://www.mauricelargeron.com/wp-content/uploads/2012/02/fig1-interface-300x110.png)](https://www.mauricelargeron.com/wp-content/uploads/2012/02/fig1-interface.png)
## **Pourquoi utiliser des rapports personnalisés par rapports aux rapports standards ?**

	- Pour Organiser ses propres rapports (cela va de soi mais bon :) ) selon ses besoins et ainsi ne pas avoir forcément les données standards *(avec donc ajout  et/ou suppression de variables et/ou de statistiques)*

	- Pour les liens personnalisés  qu'ils génèrent (fig1-2), accessibles depuis le tableau de bord général de GA

	- Afin de pouvoir partager (fig2) avec ses collaborateurs des rapports sur des données précises permettant de se focaliser sur un sujet (indicateur, contexte, tendance…).

[![Image](https://www.mauricelargeron.com/wp-content/uploads/2012/02/fig2-partage-300x92.png)](https://www.mauricelargeron.com/wp-content/uploads/2012/02/fig2-partage.png)

	- Pour avoir l’opportunité d’utiliser la fonctionnalité « explorateur » : elle permet de créer des rapports avec des groupes de données* (fig-3 : cette illustration permet de connaitre le type de contenu le plus consulté selon le trafic) .*

[![Image](https://www.mauricelargeron.com/wp-content/uploads/2012/02/fig3-groupe-300x206.png)](https://www.mauricelargeron.com/wp-content/uploads/2012/02/fig3-groupe.png)
## **Les ingrédients des rapports personnalisés  (définition et combinaison)**

Je reviens sur quelques rappels sur le [sens des données](https://www.mauricelargeron.com/explications-flots-de-clics-google-analytics/) de la plateforme Google analytics à savoir principalement les 2 pièces maitresse qu’utilisent les rapports : variable et statistique. Prenons le terme de  « variable » (en vert), parfois appelée  critère, ou dimension, c’est une donnée « bloc » unique, elle signifie par exemple un visiteur, une provenance, un aspect technique (navigateur). La notion de « statistique » (en bleue)  quant à elle, est beaucoup parlante, dénommée aussi  « métrique », elle quantifie une interaction en %, nombres, c’est une donnée de mesure.

Ces 2 indicateurs sont ensuite combinés selon ses propres besoins. Il est à noter que cette combinatoire à ces limites. Cet [article](http://support.google.com/analytics/bin/answer.py?hl=fr&answer=1033062) du support Google détaille bien cet aspect.

Donc l’intérêt pour ces rapports, est de croiser ces 2 éléments (variable et statistique) afin de faire ressortir une analyse adaptée à sa problématique. Exemple ici avec le cas de la Fig4 qui tente de répondre au souhait de savoir :  quel type de contenu  *(variable  type : titre de page = ici articles d’un blog)  * est le plus relayé selon les différents canaux  en nombre de visites ?  *(variable :  type "trafic"  =  organique, référent, direct)*.

[![Image](https://www.mauricelargeron.com/wp-content/uploads/2012/02/fig4-tableau-statique-300x248.png)](https://www.mauricelargeron.com/wp-content/uploads/2012/02/fig4-tableau-statique.png)

**Interface et mis en œuvre d’un rapport personnalisé**

L’illustration en fig-5 résume ce qui a été vu précédemment et souligne la possibilité avec "**l’ajout d’onglet"** de complexifier les rapports, avec le **champ filtre **de soustraire selon un mot clé ou par expression régulière un indicateur particulier, et enfin avec le **champ profil **de démultiplier les rapports dans un même compte (vers des profils ou comptes individuels).

[![Image](https://www.mauricelargeron.com/wp-content/uploads/2012/02/fig5-misenoeuvre-300x201.png)](https://www.mauricelargeron.com/wp-content/uploads/2012/02/fig5-misenoeuvre.png)

**Analyse d’un rapport personnalisé : Analyse sur l’efficacité des pages**

Je reprends l’article en le personnalisant de [Mr Kaushik](http://www.kaushik.net/avinash/best-downloadable-custom-web-analytics-reports/#page) sur l’analyse de page où nous avons en variable principale (en vert)  le titre de chaque page et en statistiques des données personnalisées que l’on souhaite mettre en avant :

	- Entrées, rebonds : qui mesure la première impression visiteur

	- Visiteurs uniques, pages vues, et temps moyen passé sur la page : qui chiffre le profil et l’attitude visiteur.

	- J’aurai pu rajouter en supplément une donnée de « valeur » (attribué sur un objectif fixé sur une url par exemple).

[![Image](https://www.mauricelargeron.com/wp-content/uploads/2012/02/fig6-lecturDashBoard-300x131.png)](https://www.mauricelargeron.com/wp-content/uploads/2012/02/fig6-lecturDashBoard.png)
---
title: "Créer ses propres indicateurs d'audience dans GA"
date: 2016-04-18
author: "admin"
categories: ["Google Analytics"]
tags: []
slug: "statistiques-sur-mesure-dans-google-analytics"
image: "/images/blog/statistiques-calculees-ga.jpg"
---

Attardons-nous sur une fonctionnalité qui donne un grand pouvoir dans la **[personnalisation de statistiques de google analytics](https://support.google.com/analytics/answer/2709829?hl=fr&ref_topic=2709827)**. Out of the box, ga affiche des données dans ses rapports standards selon un schema classique comme par exemple : le croisement d'une dimension, valeur insécable (comme un utilisateur) avec une statistique, valeur quantifiable (nombre de pages vues). Jusqu'à présent il était impossible de pouvoir créer de toute pièce ses propres indicateurs de suivi, désormais, c'est possible, ce qui apporte plus de flexibilité dans la connaissance de son audience et évite d'aller bidouiller dans un tableur externe !

[![Image](/images/blog/statifisques-calculees-ga-310x227.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2016/04/statifisques-calculees-ga.jpg) Principes statistiques calculees
## **Ingrédients pour monter ses propres indicateurs statistiques**

L'interface est simplicime dans son usage : nommage du ratio, type de variable souhaitée, et indicateurs à associer.
### ***Type de variables ***

 	- entier (with customizable decimal places)

 	- Devises (Decimal)

 	- Duree

 	- Flottant

 	- Percentage (avec personnalisation après la virgule)

[![Image](/images/blog/fonctionnalité-statistique-calculée-analytics-1-276x300.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2016/04/fonctionnalité-statistique-calculée-analytics-1.jpg) Statistiques calculées dans GA
### ***Formulation et opérateurs disponibles***

 	- Plus (+)

 	- Moins (-)

 	- Divisé par (/)

 	- Multiplié par (*)

 	- Parentheses

 	- Nombre cardinaux positifs (0-9), peut inclure des décimaux

### ***Indicateurs à croiser ***

Ceux Standards de GA et personnalisés issus des objectifs, des dimensions personnalisées, nombre et valeurs des évènements.
## **Paramétrages et reporting  des statistiques calculées**

L'intérêt de cette fonctionnalité nouvelle est de pouvoir ramener certains indicateurs globaux d'une part à une échelle user centric (utilisateurs : atteinte des **micro-conversions**) et d'autre part à mieux appréhender certaines entités liées aux [sources de trafic](https://www.mauricelargeron.com/deduplication-au-service-de-lannonceur/) comme le Roi d'une campagne adwords par visite.

[![Image](/images/blog/rapport-personnalisés-310x204.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2016/04/rapport-personnalisés.jpg) DIsponibilité des SC

A noter qu'il est possible pour ces statistiques "maison" :

 	- de les modifier une fois créées

 	- de les paramétrer uniquement au niveau d'une vue (pas de la propriété).

 	- d'avoir un quota de 5 statistiques calculées par vue (contre 50 sur ga premium/analytics suite 360)

 	- de les supprimer (attention une fois modifié dans l'admin, de les supprimer )

[![Image](/images/blog/rapport-personnalisés-2-310x94.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2016/04/rapport-personnalisés-2.jpg) Lecture des rapports perso. dans GA avec Stat. Calc.
## **Exemples d'indicateurs de performances**

### ***Acquisition (campagne)***

 	- Cout Moyen par session ok
Calcul = {{Cout}} / {{Sessions}}
Format Type = Devise

 	- Sessions / Clics – Visites moyennes par clic (tracking est-il correct, le visiteur procède t-il à plusieurs visites suite à 1 clics ?)
Calcul = {{Sessions}} / {{Clics}}
Format = Flottant

### ***Comportement du visiteur ***

***=> focus contenus***

 	- Nombre de Pages par visite ok

 	- Durée moyenne de la visite ok

 	- Taux de visite d'une section du site (blog, pro.) ok

***=> focus contenus  (Micro conversions : : selon la personnalisation des évènements (lecture de vidéos, )***

 	- Nbre d'objectifs total accomplis

 	- Nombre et valeur moyen d 'évènements par utilisateurs (ou par session)
exemple : Calcul = {{nombre total evenements}} / {{Utilisateurs}} ou {{Sessions}}
Format = Flottant

 	- Taux de lecture, de partage de contenus vidéos, diaporama etc (il faut avoir traqué bien sûr les boutons dédiés au suivi sur les players comme events) et les positionner comme objectifs.

### ***Conversions : tunnel, visiteur, session***

**=> Par visites (sessions)**

 	- Analyse du tunnel de conversion , en vue horizontale(voir article l3): ok
Ici l'idée est d'analyser d'une manière tabulaire les phases d'accomplissement avec leur taux de conversion sur chaque étape d'un tunnel de vente et segmenté par utilisateur, session avec des dimensions secondaires comme les appareils, canaux, ville etc..
User Type. Cela complète la vue graphique du tunnel de conversion traditionnelle. Je vous renvoie sur un article en bas de page qui détaille le processus.

 	- Total des objectifs  : l'idée ici est d'additionner des objectifs par thématique (pdfs, pages vues...)

 	- Chiffre d'affaire moyen par Session
Calcul = {{CA}} / {{Sessions}}
Format Type = Devises

 	- CA après remboursement : l'idée ici est tout simplement d'avoir à disposition le chiffre d'affaires net de tout remboursement (après avoir importé les données de remboursement).

 	- Chiffre d'affaire par session

**=> Par utilisateurs**

 	- Taux de conversion : {{Transactions}} / {{Utilisateurs}}

 	- CA ramené sur le total visiteurs

## **Liens utiles pour les statistiques calculées**

 	- Tunnel de conversion :[http://www.l3analytics.com/2015/11/03/a-powerful-use-case-for-ga-calculated-metrics/](http://www.l3analytics.com/2015/11/03/a-powerful-use-case-for-ga-calculated-metrics/)

 	- 25 Différents types de stats : [https://www.analyticspros.com/blog/google-analytics/25-calculated-metrics-for-google-analytics/](https://www.analyticspros.com/blog/google-analytics/25-calculated-metrics-for-google-analytics/)
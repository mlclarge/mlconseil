---
title: "Les cohortes, l'art de la Segmentation !"
date: 2015-03-23
author: "admin"
categories: ["Google Analytics"]
tags: []
slug: "analyse-daudience-facilitee-avec-les-cohortes"
---

Focus sur une nouvelle mesure d’audience cette semaine. Un nouveau rapport  intitulé « **cohorte analysis**  » vient fleurir avec l’arrivée du printemps le parterre de la data **Google analytics**. Oh, me direz-vous,  pour paraphraser la Fontaine, un de plus, pas de quoi faire un joli camembert !  Ceci dit , je me sentis de joie d’avoir une idée d’article , sur un sujet de choix , celui de la sacro-sainte **segmentation**, domaine de prédilection de l’analyse web.  Alors d’où provient l’origine de ce style de rapport ? Comment le construire, donner une interprétation ?

## **Origine et définition de la notion de cohortes**

Plusieurs origines dessinent cette appellation…

### ***Sens Historique de l’époque Antique..***

Cette notion proviendrait du 2eme siècle avant notre ère, elle qualifiait une tactique militaire romaine, celle de constituer des groupes de soldats ayant des traits communs : cohors praetoria (garde prétorienne : préteurs) , urbana (sécurité en journée) ; vigilum (de nuit)etc..

### ***Statistiquement vôtre***

Dans le sens démographique, les cohortes sont assimilées à des échantillonnages de populations qui ont vécu des évènements similaires dans le domaine de la santé par exemple, ceux qui ont été soumis à une exposition prolongée à une pandémie.

### ***Marketing quand tu nous tiens***

C’est le domaine qui nous intéresse ici tout de même ! C’est l’américain Kotler, professeur en stratégie marketing, qui en parle le 1er dans les années 70 dans son best seller « marketing management » (14eme édition en 2012) . Il parle de cohortes générationnelles soit de groupes d’individus nés dans une même période temporelle .

[![Image](/images/blog/definition-kotler-cohortes-310x124.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2015/03/definition-kotler-cohortes.jpg) Phillip kotler et ses cohortes générationnelles
### ***WebAnalytics ? ***

Peut-on parler de cohortes numériques ? Comment les  qualifier ? Je n’ai pas de définition en particulier. Que pourrait on dire ? Elles représentent  des  groupes de visiteurs constitués par un attribut commun (ici dans Google analytics , item de base  « date acquisition de la 1ere session »), à partir de laquelle  une segmentation plus fine  par  dimensions et statistiques  (rétention, transaction ..) permettra de  mieux cerner certains usages . L’objectif est  de mieux cibler les actions digitales à venir. Bon à voir dans le concret…

Retenons pour l’essentiel le facteur « temps » (date) donnée fondatrice pour bâtir une cohorte.

## **Créer des cohortes "maison" dans GA **

Jusqu’à présent, dans GA, faire une segmentation de telle sorte n’allait pas de soi ! L’application a souvent était critiquée pour cela, pour ce manque de fonctionnalité permettant une segmentation out of the box complète, segmentable par statistiques variées.

Bon, jusqu’à présent, en restant dans l’application GA, ce genre de cohortes (segmentation)  reste possible  à fabriquer :

	- par  donnée d’entrée la date de "1ere session". Pour l’exemple ici  : segmentons , suite à une campagne seo, le canal éponyme.. Donc, constitution d’un groupe d’utilisateurs depuis le 1er mars  2015 au 7 mars comme date de 1ere session,  de provenance  du canal d’acquisition « seo ». Il est bien sur possible d’affiner cette cohorte par d’autres dimensions personnalisées et par d’autres périodes, mais pas très pratique ni lisible.

[![Image](/images/blog/segment-cohortes-google-analytics-310x219.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2015/03/segment-cohortes-google-analytics.jpg) Segment cohortes "maison"

[https://www.google.com/analytics/web/template?uid=07QZW6hVQbaQP_37YsvaHQ](https://www.google.com/analytics/web/template?uid=07QZW6hVQbaQP_37YsvaHQ)

	- par marquage par variables/dimensions  personnalisée : ga('set', 'yyyymmdd',1);

	- par la pose d’évènements : ga('send', 'event', 'cohorte', 'premierAchat', ' yyyymmdd’);

Dans GA, le reporting n’est cependant  pas très « parlant » pour lui donner du sens.  Seule  l’ exportation des données pour tableur ou autre  soft de business intelligence fait l’affaire .Sinon,  des solutions  proposent des compléments pratiques pour gagner du temps dans l’export de la data vers son traitement dans un tableur :  La solution du addons d’analystics edge + feuille de calcul fait bien l’affaire

[![Image](/images/blog/analytics-edge-cohort-excel-sheet-310x233.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2015/03/analytics-edge-cohort-excel-sheet.jpg) Analytics edge addons & tab excel
## **Cohort analysis en Bêta est arrivée , ouf !**

### ***Quelles sont les composantes d’une cohorte pour GA ?***

Cette cohorte se présente sous forme tabulaire .  L’intérêt majeur de ce nouveau rapport réside dans sa construction standard toute prête à l’emploi ! Les composants de cette représentation sont pour l’instant (va évoluer prochainement) :

	- la date d’acquisition du trafic (point de départ, 1ere visite) : data prioritaire

	- La taille : par jour, semaine ou mois

	- La statistique étudiée : par utilisateur, par rétention (fidélité), par volume de données (objectifs, page vues, chiffre d’affaires, durée de session, transactions.)

	- **Chaque ligne correspond à 1 cohorte par date**

	- **Les colonnes indiquent la progression de chaque groupe par périod*e***

[![Image](/images/blog/details-cohortes-227x300.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2015/03/details-cohortes.jpg) Ingrédients des cohortes
### ***Que peut-on faire avec ce genre de reporting ?***

SI  l’on souhaite allez plus loin dans le « qui fait quoi » de l’analyse, on peut par exemple s’amuser à segmenter une cohorte par canal d’acquisition, comme ici pour l’exemple, le levier « seo ». Les visiteurs de ce canal sont-ils plus  fidèles (analyse de la rétention)  ?

[![Image](/images/blog/segmentation-cohortes-par-trafic-organique-276x300.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2015/03/segmentation-cohortes-par-trafic-organique.jpg) Segmentation cohortes par trafic organique
## **Quelques ressources** 

	- Complément WIkipedia : [http://en.wikipedia.org/wiki/Cohort_analysis](http://en.wikipedia.org/wiki/Cohort_analysis)

	- Atinternet cohorte & ebusiness :  [*http://blog.atinternet.com/fr/cohorte-buzz-performance/*](http://blog.atinternet.com/fr/cohorte-buzz-performance/)

	- Complément Excel + template : [http://help.analyticsedge.com/googleanalytics/building-a-cohort-analysis/](http://help.analyticsedge.com/googleanalytics/building-a-cohort-analysis/)
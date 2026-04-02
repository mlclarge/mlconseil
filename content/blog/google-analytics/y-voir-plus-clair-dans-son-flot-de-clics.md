---
title: "Segmenter c'est un peu trier pour mieux cibler !"
date: 2013-11-13
author: "admin"
categories: ["Google Analytics"]
tags: []
slug: "y-voir-plus-clair-dans-son-flot-de-clics"
---

Abordons le sujet de la segmentation avec Google analytics qui  vient d’améliorer son outil , de le perfectionner  tout au moins, avec la possibilité d’aller plus loin dans l’analyse d’audience, au-delà de la simple visite (plus techniquement appelée la session). La notion de visiteur rentre dans le bal, avec l’analyse multi-sessions.  Rappelons les vertus de la segmentation, puis la prise en main de l’outil, et des cas d’utilisation.

## **L’art de la segmentation **

### **La segmentation, pourquoi faire ?**

Tout simplement pour avoir une vision plus précise de qui fait quoi sur le site.  Google analytics nous donne déjà des une poignée de données mais agrégées, sans distinction précise, un flot de clics qu’il va falloir distinguer.

[*](https://www.mauricelargeron.com/wp-content/uploads/2013/11/segmenter.jpg) L'art du Tri !

Prenons un petit exemple simple, la catégorie audience nous donne des données démographiques et notamment  par tranches d’âges (18-24/25-34/35-44/45-54)  pour 5,71 % des visites,  certes ce n’est pas représentatif, mais c’est un début,  36,9 % sont des hommes et 63,1% des femmes.

[![Image](https://www.mauricelargeron.com/wp-content/uploads/2013/11/demographie-310x153.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2013/11/demographie.jpg)

Si je considère que mon cœur de cible sont les  femmes de 25-44 ans comment connaître  sa proportion ici ?  Un segment personnalisé va me permettre de le découvrir

[![Image](https://www.mauricelargeron.com/wp-content/uploads/2013/11/demographie-segmentation-femmes-310x255.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2013/11/demographie-segmentation-femmes.jpg) Avec un segment ciblé sur 1 cible précise
### **3 niveaux de segmentation ***

Jusqu’à peu de temps, Google analytics ne permettait que de segmenter sur 2 niveaux de la visite ou session, représentée par un cookie de 30mn. Dorénavant, il est possible de représenter un ensemble de visiteurs au travers leur différente visite. Donc 3 niveaux de mesures pour analyser son trafic.

	- La **session**: temps limité qui représente une visite est une collection de hits.

	- Le **visiteur** : ensemble de visites (ou sessions).

	- *Les **appels de fichiers** (hits) : temps par page,  taux de rebond, clics, évènements, variables personnalisées (accessibles depuis les filtres avancés dans l’outil)*

[*](https://www.mauricelargeron.com/wp-content/uploads/2013/11/echelle-segment.jpg) 2 niveaux d'interprétation dans GA
### **Les données segmentables, 2 grandes familles ..***

***Les variables ou données indivisibles  identifiées en vert dans GA, comme par exemple :***

	- Démographie : Age, sexe, langue, géographie

	- Technologie : système exploitation, navigateur, marque et modèle mobile

	- Source de trafic : campagnes, support, sources de trafic

	- Comportement : page de sortie, type de visiteur.

***Des statistiques ou données chiffrées (taux, quantités/nombres, durée d’ensemble) marquées  en bleu.. :***

	- Comportement : visites, jours, durée en minutes, pages vues, visites avec recherche

	- Conversions : achats, transactions, objectifs

	- Publicité : impressions...

## ***Prise en main du nouvel outil ***

### **Intuitif cet outil d'analytics..**

Le nouvel outil donc ne change pas la donne sur l’essentiel, l’interface est plus intuitive, plus puissante avec la venue multi-sessions visiteurs.

[*](https://www.mauricelargeron.com/wp-content/uploads/2013/11/interface-opti.jpg) Interface de l'outil segmentation

Survoler les champs du formulaire avec la souris,  les variables vous seront suggérées automatiquement par le système, pratique quand on veut tester l’outil sans objectif de départ précis.

### **Puissant avec la création de séquences**

Permet de fixer des conditions au segment étudié, soit par exemple trier les utilisateurs qui ont pu visiter telle ou telle page sur le chemin de la conversion , ou alors ceux qui ont été exposé à une campagne publicitaire, ou alors ceux dont le taux de rebond est supérieur à « x » % etc….Cet outil est similaire à ce que l’on peut retrouver dans les combinaisons dans l’établissement de listes de remarketing.

### **Petite vidéo d’ensemble **

Pour les anglophones, désolés  :( , mais donne néanmoins un petit aperçu.

**http://youtu.be/dD-j9dgWF98***

### Pas illimité en revanche !

	- Les données disponibles à l’échelle visiteur peut remonter jusqu’ à 90 jours

	- La possibilité de constituer des ensembles (cohortes) n’est possible que sur une durée maximale de 31 jours.

	- 100 segments par utilisateur et par vue sont autorisés.

### **Attention tout n’est pas segmentable**

Tout d’abord, gardons aussi à l’esprit que cette segmentation est transversale aux  catégories consultées  (audience, acquisition, comportement…) . Précisions : Il peut arriver que l’on veuille  « isoler »  un contenu, comme par exemple une url, pour avoir une vue uniquement  sur cette page, on va donc utiliser un filtre « par page », mais cela ne  marchera pas, car nous sommes dans un segment, au niveau utilisateur et toutes les pages vues seront scindées sans distinction.

[*](https://www.mauricelargeron.com/wp-content/uploads/2013/11/mauvais-segment.jpg) Une info pas disponible dans un segment

Il faudra passer par un rapport personnalisé avec un filtre plus  adapter  un éventuel segment sur ce nouveau rapport, comme par exemple la part de trafic venant de facebook.

[![Image](https://www.mauricelargeron.com/wp-content/uploads/2013/11/detail-page-analytics-310x177.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2013/11/detail-page-analytics.jpg) Page dans rapport personnalisé + 1 segment
## **Cas d’usages**

### **RFM***

Les anglo saxons appellent récence, (recensy)  fréquence (fréquency), et revenus (money)

Déterminer le profil visiteur de ceux qui viennent récemment et  une cadence régulière avec un panier d’achat minimum. Ici les leviers actionnables sont ceux du comportement et des achats dans l’outil.

[![Image](https://www.mauricelargeron.com/wp-content/uploads/2013/11/frm-analytics-310x256.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2013/11/frm-analytics.jpg) Récence-Fréquence-Revenus
### **Cohortes**

L’usage ancien de ce terme marketing est revenu d’actualité ! La sélection sur une période donnée (1 mois maxi pour l’instant) permet d’avoir une vue d’ensemble sur un groupe de visiteurs, ici 33 % des utilisateurs proviennent du trafic organique ou direct entre le 1 et 31 octobre  représentant 33 % du trafic d’ensemble.

[![Image](https://www.mauricelargeron.com/wp-content/uploads/2013/11/cohortes-310x236.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2013/11/cohortes.jpg) Création de cohortes (ensembles homogênes)

Les cas d’usages sont à adapter en fonction des problématiques de chacun et selon son propre modèle économique.

## Webographie
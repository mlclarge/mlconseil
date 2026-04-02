---
title: "10 rapports Google analytics pour qualifier une audience"
date: 2015-12-07
author: "admin"
categories: ["Google Analytics"]
tags: []
slug: "10-rapports-google-analytics-pour-qualifier-une-audience"
image: "/images/blog/rapports-google-analytics.jpg"
---

Un des exercices sur [Google Analytics](https://www.google.com/analytics/) lors de **formations webmarketing** consiste à faire chercher aux étudiants dans les rapports de l’application, des réponses à des questions fondamentales que tout possesseur de sites web est amené à se poser un jour ou l’autre pour mesurer certains indicateurs d’audience. J’ai synthétisé 10 questions qui amènent à produire 10 rapports dans GA avec comme exemple ce blog et un site ecommerce, le tout regroupé dans 3 catégorie : profils **utilisateurs, comportements et conversions**.

## **Profils d’utilisateurs du site**

### *1/ A quoi ressemblent les visiteurs du blog ?*

En toute logique, avant le lancement d’un site web, blog ou autre, on tente de se faire une idée de son lectorat potentiel, alors on dresse dans le jargon des « personas », des profils susceptibles d’être intéressés par les contenus  produits.

**Chemin :** Audience>Données démographiques>Présentation avec 4 segments

J’apprends avec ce rapport que **segmenté** par : rebond, notoriété (accès direct), fidélité que les visiteurs et temps par visite (sessions). J’observe donc une audience  plutôt masculine, avec un accès direct d’env. 15% qui souligne  une notoriété timide, un  volume du temps moyen passé sur l’ensemble des sessions  supérieur à 2mn faible mais pas surprenant,  et enfin, qu’un quart des visiteurs semblent fidèles (déjà venus certainement d’ailleurs par accès direct).

[![rapport-1-381x300.jpg](/images/blog/rapport-1-381x300.jpg) 4 Segments pour une audience
### *2/ Quel type d'appareils  utilisent-ils ?*

**Chemin :** Audience>Mobile>Vue d’ensemble

Bon ici, dans un monde multi-appareils, il peut être intéressant d’observer les visites par type d’appareils et de faire un rapprochement avec les **conversions**.

Les devices mobiles semblent avoir un taux de conversion autour de 10% alors que celui issu d’une consultation desktop se rapproche de 15% . Faut-il en déduire une UX à optimiser sur les devices plus mobiles où tout simplement le contexte (mobilité) est-il peu propice à la conversion ?

[![appareils-et-conversions-304x300.jpg](/images/blog/appareils-et-conversions-304x300.jpg) Types d appareils et conversions
### *3/ Le site est-il optimisé pour tous les navigateurs qu’ils utilisent ?*

**Chemin :** Audience>Technologie>Navigateur et OS (option : Version système exploitation)

Une certaine homogénéité qui semble correspondre à la cible des visiteurs, early adopté de chrome et Firefox principalement sous Windows (si on active la dimension secondaire).

[![optimisation-navigateurs-310x141.jpg](/images/blog/optimisation-navigateurs-310x141.jpg) Optimisation navigateurs
## **Comportements des visiteurs**

### *4/ Quels sont les requêtes tapées par les visiteurs depuis Google ?*

 	- **Chemin :** Acquisition>Optimisation du référencement > Requêtes

J’ai fait un tri par nombre de clics. Ces données sont rapportées depuis l’association du service « **Search Console **», bien sûr ce n’est qu’une portion congrue de la réalité (non définie).

[![mots-clés-principayx-310x61.jpg](/images/blog/mots-clés-principayx-310x61.jpg) Mots clés principaux
### ***5/ Quels contenus consultent-ils ?***

 	- **Chemin :** Comportement>Contenu du site > Toutes les pages

La page d’accueil, pour la période choisie, n' est pas leader, normal pour un blog,  en revanche la homepage s'attire les meilleurs kpi comportementaux (rebond, temps passé, durée) et de conversions. En outre, un bon marquage Seo des mots clés par page, peut donner une idée des mots clés tapés par les internautes provenant des moteurs de recherche sur ces contenus principaux (lié au rapport précédent).

[![contenus-plus-consultés-310x95.jpg](/images/blog/contenus-plus-consultés-310x95.jpg) pages les plus consultées
### *6/ Quels sont les pages les plus partagées depuis les réseaux sociaux ?*

 	- **Chemin :** Comportement>Contenu du site > Toutes les pages

Bon pas trop au top, mais il y a un début à tout ! Vu la cible, ces résultats me semblent cohérents.

[![url-plus-partagee-310x66.jpg](/images/blog/url-plus-partagee-310x66.jpg) url plus partagees sur les Rs
### *7/ Quels sont les vues uniques consultées par  page (avec une déclinaison par villes) ?*

 	- **Chemin :** Comportement>Contenu du site > Toutes les pages > **Tableau croisé dynamique** : support et ville comme dimensions + vues uniques et temps passé comme statistiques.Et oui, même GA fait des TCD, le seul endroit ou le **croisement de dimensions** est possible !

[![tableau-croise-dynamique-par-contenus-310x97.jpg](/images/blog/tableau-croise-dynamique-par-contenus-310x97.jpg) Tableau croise dynamique par contenus
## **Chemins d’acquisition & Attribution - conversions**

### *8/ Quel podium pour les canaux en terme de volumes de conversions ?*

 	- **Chemin :** Acquisition>Tout le trafic>Canaux>Conversions : tous les objectifs

Une fois les profils plus ou moins identifiés, par quels chemins principaux empruntés pour la conversion ?

On  note l’importance du SEO ici, avec la première position pour la recherche organique, et la troisième pour les référents, la deuxième place loin derrière pour le trafic direct (notoriété). Peu se poser ici la question ici de la Google dépendance !

[![leviers-acquisitions-310x82.jpg](/images/blog/leviers-acquisitions-310x82.jpg) Leviers acquisitions
### *9/ Quels chemins les plus fréquents les clients empruntent-ils pour convertir (volume) ?*

 	- **Chemin :** Conversion>Entonnoirs multicanaux>Chemins de conversions

Le trio de tête ici laisse une large place au référencement naturel encore, le plus pérenne des canaux d’acquisition d’ailleurs.  Notons la place prépondérante des liens sponsorisés, mais ce rapport est à prendre avec précaution, car il est trié par volume et non par valeur d’une part et selon un modèle d’attribution au dernier clic.

[![groupe-de-chemins-les-plus-importants-310x54.jpg](/images/blog/groupe-de-chemins-les-plus-importants-310x54.jpg) Groupe de chemins les plus importants
### ***10/ Quels poids pour chaque levier ?***

 	- **Chemin :** Conversion>Attribution>Outil de comparaison de modèles

Le classement des groupes de canaux  est donc au dernier clic, mais si l’on souhaite mettre en avant plutôt le 1er contact avec le visiteur et y affecter la valeur et volume de conversion ? Ce type de modèle 1er clic cette fois –ci  fait changer le poids des leviers. Sur la seconde position, les liens sponsorisés se voient affectés le 2eme rang et l’accès direct en 3eme place.

[![attribution-au-premier-clic-310x174.jpg](/images/blog/attribution-au-premier-clic-310x174.jpg) Modèle d'attribution au premier clic Vs last clic

Ensuite de ces rapports il suffira de tirer des **tableaux de bord** selon les objectifs prioritaire définis dans l'acquisition de trafic et  ainsi permettre  un pilotage décisionnel.
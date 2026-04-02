---
title: "Tout savoir sur l'outil de B.I. \" Data Studio\" de google"
date: 2016-07-25
author: "admin"
categories: ["Outils Web et Marketing"]
tags: []
slug: "data-studio-360-pour-visualiser-ses-statistiques"
image: "/images/blog/data-studio-tutoriel.jpg"
---

Google est en train de déployer un de ses derniers **[outils de Business intelligence ‘Data studio »](https://www.google.com/analytics/360-suite/data-studio/).** Même si l’outil n’est disponible qu’en lecture seule actuellement en France, il est possible déjà d’en prendre la mesure dès aujourd’hui, en se rendant sur l’interface via une recherche dans Google (il faut avoir un compte Google bien sûr). Quoi qu’il en soit, voyons à quoi sert la solution, ses limites, atouts, et enfin son interface.

[![Image](/images/blog/google-studio-gratuit-310x228.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2016/07/google-studio-gratuit.jpg) Ou trouver Data Studio ?
## **Les deux principales caractéristiques de Data Studio**

N’oublions pas que cette version qui fait partie de la [suite  Analytics 360](https://www.mauricelargeron.com/une-suite-6-etoiles-pour-une-galaxie-de-donnees/) est une version bêta donc perfectible et qu’elle va sans doute s’enrichir de fonctionnalités. Comme son nom l’indique, cet **outil produit des rapports sous forme graphique** à partir de données sources existantes (data = statistiques et dimensions)  comme  Google Adwords, Google analytics, Big query (le big data de Google), feuilles de calcul Google.

[![Image](/images/blog/connecteurs-data-studio-210x300.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2016/07/connecteurs-data-studio.jpg) Connecteurs Data Studio

L’objectif de cet outil est double :

 	- **Donner du sens **à l’analyse de data, dont les sources sont souvent nombreuses sous forme tabulaires (lignes et de colonnes).  D’un ensemble de rapports (comme ceux de Google analytics), ces données deviennent  plus claires et compréhensibles au sein d'un tableau de bord.

[![Image](/images/blog/exemple-de-rapport-310x282.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2016/07/exemple-de-rapport.jpg) Exemple de rapport graphique

 	- **D’apporter de l’interactivité**  au destinataire du rapport : manager, marketeur, client avec une possibilité d’avoir des données actualisées en permanence, modifiables « live » sur la partie calendrier/période étudiée et enfin doté d’une fonctionnalité de tri qui permet d’engager son lecteur s’il souhaite trier certains rapport chiffrés par les entêtes de colonnes.

Je remercie vivement **Ben Collins** pour cette petite animation qui donne un exemple des interactions possibles.
[![Image](/images/blog/mobile_dashboard-310x238.gif)](https://www.mauricelargeron.com/wp-content/uploads/2016/07/mobile_dashboard.gif)
## **Les plus, limites et bonnes pratiques de Data Studio 360.**

### ***Les plus de l’outil Data Studio 360***

 	- Une interface très user friendly, rapide, intuitive pré-chargée de Template graphique standard.

 	- Sa gratuité ! Certes limitée à 5 rapports par compte Google mais totalement illimitée en partage et édition (modification).

 	- Les valeurs peuvent être restituées en pourcentage (utiliser l’aide sur les fonctions qui élargissent les manipulations des statistiques).

 	- DS360 supporte les fonctions de requêtes SQL mais pas toutes ! Consultez donc l’aide technique ponctuellement.

 	- Mélange de plusieurs sources de data au sein d’un même rapport (Adwords et Google analytics par exemple).

 	- Les rapports graphiques sont responsive.

[![Image](/images/blog/datastudio-360-sur-mobile-310x204.png)](https://www.mauricelargeron.com/wp-content/uploads/2016/07/datastudio-360-sur-mobile.png) Affichage Data studio 360 sur mobile
### ***Les limites de DS 360***

 	- Pas d’export sous format pdf

 	- Pas d’intégration (embedding) dans une page web. Donc le partage est celui déjà disponible sur Google sheet, via un lien direct.

 	- Le scheduling de rapport par email  n’est pas prévu (la data étant updatée automatiquement donc mise à jour facile :) ).

 	- Les données de la search console intégrées dans GA par association des 2 plateformes ne sont pas accessibles via DS 360  il faudra passer par un export sous feuille de calcul Google et ensuite la relier à DS360.

 	- Les différentes feuilles de calcul d’un Google sheets ne sont pas intégrable tel quel sur un appel de data. Il faudra les traiter individuellement.

 	- Différentes parties situées sur une même feuille ne sont pas intégrable dans un appel de data source.

 	- Les filtres sur des sous-ensembles de data ne sont pas disponible. Avoir par exemple des conversions pour un traffic supérieur à 2500 pages vues n’est pas configurable.

 	- Attention au conflits probable sur l’édition de graphique, re dimensionner un graphe sous Microsoft edge n’est pas possible.

 	- La segmentation de données n’est pas gérée (data source ou nativement).

 	- Pas d’agrégation par mois, semaines, uniquement par jour.

 	- Pas d’agrégation de la data sous des formats de type percentile, médian.

### ***Bonnes pratiques de Data Studio 360***

 	- Ne pas oublier que les manipulations de data sur BigQuery via DS360 sont facturées comme un usage direct (normal) de BQ.

 	- Utiliser la fonction « Case » , la fonction « if » n’étant pas disponible.

 	- Faire usage des regroupements de composants sur l’éditeur graphique (sélection via souris) lors de la création de filtres de contrôle afin d’éviter un blocage navigateur.

 	- Pour s’initier à la construction de rapports, faire une copie des exemples « sample data » donnés en page d’accueil.

 	- Rendre complémentaire l’usage d’addons comme supermetrics en amont pour fournir de la data, et connecter ensuite DS.

## **L’interface de data studio (en français ) **

J’avoue, google m’a copié, l’aide est particulièrement bien faîte, j’ai donc récupéré et traduit leur screenshot pour une fois !  :)

[![Image](/images/blog/page-accueil-google-studio-490x300.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2016/07/page-accueil-google-studio.jpg) Page accueil google studio

***Descriptif de la page accueil :***

 	- **Créer** un **nouveau bouton de rapport.**

 	- **Liste** des **rapports.** Cliquez sur un rapport pour la voir.

 	- **Outil sélecteur.** Basculer entre les rapports et sources de données.

 	- **Catégorie onglets.** Préciser la liste des rapports ou des sources de données.

 	- **Plus menu.** Partager, renommer ou supprimer le rapport sélectionné ou d'une source de données.

 	- **Recherche.** Trouver des rapports ou des sources de données rapidement.

 	- **Liste Trier.**

 	- **Google Analytics 360 Sélecteur de produit Suite** (Analytics 360 utilisateurs Suite uniquement).

 	- **Google icône** de **profil.** Gérez votre compte Google.

[![Image](/images/blog/createur-de-rapport-google-studio-449x300.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2016/07/createur-de-rapport-google-studio.jpg)

***Description de l'éditeur de rapport :***

 	- **Page de travail pour créer un rapport.** Construisez votre rapport ici.

 	- **Barre d'outils du graphique.** Cliquez sur l’outil graphique, puis dessiner une boîte sur la page pour ajouter ce graphique à votre rapport.

 	- **Graphique.** Charts visualiser les dimensions et les statistiques de vos sources de données. Sélectionnez un graphique pour afficher le panneau de propriétés de ce tableau. Google studio crée automatiquement un graphique par défaut.

 	- **Panneau Propriétés.** Configurez les paramètres et propriétés pour le composant sélectionné de la page de travail (ici voir N°3)

 	- **Barre de menus.** De nombreuses fonctions de menu peuvent également être consultées en cliquant droit sur un composant.

 	- **Modifier bascule.** Basculer entre les éditer et mode d’affichage.

 	- (De droite à gauche:)

 	- **Bouton Partager.** Partagez ce rapport avec d'autres personnes.

 	- **Suite organisation icône.** (Suite Google Analytics 360 utilisateurs uniquement) Basculer entre les organisations

 	- **Google icône** de **profil.** Gérez votre compte Google.

 	- **Texte, image, et** la **forme** des **outils.** Ajouter des annotations, des graphiques et des formes géométriques à votre rapport.

 	- **Date** de **contrôle de** la **plage |** **Filtrez** le **contrôle.** Ajouter des contrôles interactifs pour permettre aux utilisateurs d’affiner le rapport.

 	- **Mode de sélection |** **Annuler |** **Refaire.**

 	- Le **contrôle du cache.** Mettre à jour le cache.

 	- **Contrôles Page.** Ajouter les pages à supprimer et pages du rapport. Recherchez et renommez pages.

 	- **Logo.** Cliquez pour revenir à la page d'accueil RAPPORT.

 	- **Signaler nom.** Cliquez pour changer le nom.

## Sources utiles pour Data studio 

Documentation  (en) : [https://support.google.com/360suite/datastudio?hl=en#topic=6267740](https://support.google.com/360suite/datastudio?hl=en#topic=6267740)

https://www.youtube.com/watch?v=6FTUpceqWnc

***A lire Article US :***

 	- [http://www.benlcollins.com/dashboard/google-data-studio-tips/](http://www.benlcollins.com/dashboard/google-data-studio-tips/)

 	- [http://online-behavior.com/analytics/google-data-studio](http://online-behavior.com/analytics/google-data-studio)

 	- Intégration avec supermetrics : [https://analytics.googleblog.com/2016/06/get-facebook-bing-twitter-more-into.html](https://analytics.googleblog.com/2016/06/get-facebook-bing-twitter-more-into.html)
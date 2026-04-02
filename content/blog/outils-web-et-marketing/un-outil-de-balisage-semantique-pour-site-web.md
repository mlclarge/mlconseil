---
title: "Balisage Schema.org facilité avec SemanticMarker !"
date: 2015-04-13
author: "admin"
categories: ["Outils Web et Marketing"]
tags: []
slug: "un-outil-de-balisage-semantique-pour-site-web"
---

Revenons dans l’univers du **web sémantique** cette semaine avec la présentation d’un outil de balisage de page web. Pour son concepteur Fred Laurent , cet outil arrive  comme une étape nouvelle mais également comme un aboutissement dans le  développement d’outils d’aide à la [sémantisation](http://fr.wikipedia.org/wiki/Projet:Web_s%C3%A9mantique) pour les  éditeurs de site web.  Pousser l’élaboration de contenus ayant du sens pour les moteurs, robots et autres crawlers est  un souhait développé par bon nombres d’acteurs.  Sa société **SémanticMarker** s’y adonne depuis fin 2010.  Posons dans un premier temps le décor, et rentrons ensuite  dans l’outil.

## **Pourquoi baliser les données pour les moteurs ?**

### ***Pour les machines, apporter de l’intelligence***

Et ainsi donner plus de sens et permettre aux moteurs de lire entre les lignes le message de son émetteur mais aussi créer des liens relationnels entre les différents documents. En effet, le langage Html ne fait que représenter pour un navigateur, la corpulence d’un contenu (titre, paragraphe, gras..) mais en aucun cas n’en « signifie » le sens. Comment indiquer  ce que recouvre le mot « Fraise » par exemple dans un titre ? Indique t-il  le fruit ?  l’outil du chaudronnier ? , l’artifice vestimentaire ?  , une tête en argot ?  . Depuis la naissance du web, les moteurs se sont fait une raison.  Le Page rank de Google, pilier fondamental du moteur,  épaulé par des technologies d’analyse de textes, comparaisons,  lecture de graphes réussissent néanmoins à classer l’information. Mais cela reste parfois approximatif . Ici , ci-dessous, cette illustration sur le mot "Bercy" selon le contexte ..

[![Image](https://www.mauricelargeron.com/wp-content/uploads/2015/04/desanbiguite-310x92.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2015/04/desanbiguite.jpg) "Désamgiguiser" les termes* (source: semanticmarker)*

Baliser sert aussi à  donner de la cohérence à ce graphe de liens sans cesse grandissant de l’internet, où le codage  donne naissance à des **entités** palpables pour la machine : **personnes, choses, évènements** mais aussi  objets comme la vidéo, les images, le son.

Pour lire ces **microdatas,** il faut que ces mêmes moteurs puissent inclure dans leur algorithme, des technologies capables de « lire » ces balises. Le projet Schema.org est allé dans ce sens depuis 2011 . Créer  un standard  plus simple que le RDFa (complexe  à coder ),  pour les plus gros acteurs de la recherche (Google, bing, yahoo,Yandex). Soulignons que  des passerelles   existent pour aller d’un simple html vers des microdatas plus poussées  comme le RDFa. La dernière version Schéma.org   est la 1.93 annoncé le  4 février dernier, et à chaque nouvelle sortie, des améliorations sont ajoutés sur la richesse, la profondeur du vocabulaire des balises.

[![Image](https://www.mauricelargeron.com/wp-content/uploads/2015/04/marqueurs-semantiques-203x300.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2015/04/marqueurs-semantiques.jpg) Principaux Marqueurs sémantiques
### ***Le Seo, améliorer ses positions !***

La relation cause à effet n’est apparemment pas si simple  à établir au niveau des résultats des urls dans le classement des  moteurs de recherche comme Google..L’étude de SearchMetrics *(voir étude complète en fin d'article)* démontre une corrélation entre un balisage shema.org et un meilleur **positionnement dans les serp**, mais attention aux conclusions rapides car la relation de cause à effet n’est pas  démontrée. En tous cas, notons que cela ne peut faire que du bien à son [webmarketing](https://www.mauricelargeron.com/definir-le-terme-webmarketing/) !

[![Image](https://www.mauricelargeron.com/wp-content/uploads/2015/04/entites-et-serp-google-277x300.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2015/04/entites-et-serp-google.jpg) **Efficacité du balisage selon SearchMetrics**
## SemanticMarker facilitateur Seo** !**

### **Que représente le développement de cet outil  par [SemanticMarker](http://semanticmarker.com/) ?**

	- 4 ans de développement

	- 2.2 millions d'entités gérées

	- 197 catégories d'entités (dont modèles de voiture, Smartphones, films, événements, thèmes économiques, ...)

	- 262 millions d'éléments pour l'analyse du contexte et la désambiguïsation des entités

### ***Objectifs et fonctionnalités  de SM***

But : Dixit son développeur à qui j’ai posé la question, la réponse est claire :  « SemanticMarker optimise le référencement naturel des contenus Web, en leur ajoutant des données structurées détaillées, conformément aux consignes émises par les principaux moteurs de recherche (Google, Bing, Yahoo).
Ces **données structurées** identifient et désambiguïsent les entités contenues dans les articles (personnes, organisations, événements, thèmes d'actualités) et les connectent aux Knowledge Graphs des moteurs de recherche, ce qui améliore la qualité de leur indexation.

Placées dans le corps du texte, ces données sont invisibles pour le lecteur et complémentaires des stratégies SEO existantes. Leur mise en place est automatisée. »
***Exemple pour une url d'un blog***

L’interface est très simple d’usage. Il suffit de copier-coller dans le champ approprié l’url que l’on souhaite voir balisée et hop ! La page est scannée et restitue à l’écran 4 grandes volets  : la page codée, les entités détectées (34), les marqueurs insérés (87) et les connexions sémantiques (93). Voici la première partie de l’interface..(Scindée dans l’illustration pour raison pratique)

[![Image](https://www.mauricelargeron.com/wp-content/uploads/2015/04/schema-tool-310x296.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2015/04/schema-tool.jpg) Interface de l'outil

Un tableau agrégé précise les principaux termes associés à leur entité, leur type et la catégorie thématique respective. Une indication de fréquence indique la proportion des termes similaires (répétition en quelque sorte). La dernière colonne  « valider » donne le choix du balisage final pour chaque entité. L’algo. de l’outil filtre selon la sémantique du texte, des entités non justifiées. Le code source de la page est également rendu. Enfin, mais c’est juste pour l’anecdote ici car cette indicateur va disparaître, les **connexions sémantiques** sont représentées (proviennent du **knowledge graph** (un outil interne dont les sources sont : Wikipédia FR, Wikipédia EN, Wikidata et d'un graphe d'actualités actualisé en temps réels (articles/post parus sur le Web, analysés par Knowly, autre outil, qui construit le graphe d'actus ).

[![Image](https://www.mauricelargeron.com/wp-content/uploads/2015/04/connexions-semantiques-223x300.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2015/04/connexions-semantiques.jpg) Fonctionnalités de l'outil
### ***Intégration dans les CMS du marché***

	- Pour Wordpress,  selon Fred Laurent,  il suffit de modifier le fichier kses.php et copier le code HTML. Normalement, le code HTML d'origine incluant la mise en page est préservé.  Je n’ai pas testé personnellement, mais il ne pense pas que la désactivation de plugins soit nécessaire.

	- Pour Joomla, à priori aucun problème à partir de la version 3.3, c'est inclut nativement.

	- Pour Drupal, à priori ça ne pose pas de problème à partir de la version 7, à tester.

### ***Tester au final***

On peut aussi s’amuser à tester la page avec l’outil Google mise à jour récemment sur la lecture des microdatas. Ici, pour la même url testée ci-dessus,  il distingue bien 4 types d’entités : thing (chose), Corporation (enseigne), Organization, et Person. L’indication des filtres personnalisés est à l’usage du service de Google «moteur de recherche personnalisé », afin d’utiliser les entités de son choix pour guider le moteur selon la thématique sur lequel il est installé.

[![Image](https://www.mauricelargeron.com/wp-content/uploads/2015/04/testing-tool-page-310x182.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2015/04/testing-tool-page.jpg) Google testing tool page
## **Des liens qui complètent le sujet**

	- Seo et sémantique outil d’aide à l’optimisation : [http://www.knowly.net/](http://www.knowly.net/)

	- Knowlegde graph tool : [http://www.saciol.com/welcome](http://www.saciol.com/welcome)

	- Google Testing Tool : https://developers.google.com/structured-data/testing-tool/

	- Cas d’usage : http://semanticmarker.com/mark?url=www.mauricelargeron.com/concept-et-balisage-semantique-pour-un-site-web/#graphe

	- Balisage RichSnippet et Positionnement Srp : [Searchmetrics](https://www.mauricelargeron.com/wp-content/uploads/2015/04/Searchmetrics_Schemaorg_Study_2014.pdf)
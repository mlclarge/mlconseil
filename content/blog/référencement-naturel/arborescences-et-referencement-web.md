---
title: "Sept Architectures Web et Seo"
date: 2013-01-31
author: "admin"
categories: ["Référencement naturel"]
tags: []
slug: "arborescences-et-referencement-web"
---

Après avoir parlé de web stratégie la semaine dernière, c’est à l’architecture web d’être à l’honneur cette semaine. J’introduis le sujet par un angle métier qui élargit le débat. Dans le monde du référencement de site internet, un poste à fait apparition relativement récemment, celui d’architecte Seo. Parmi ces fonctions, outre celles liées aux compétences de chef de projet (coordination des parties prenantes, formation, stratégie), l’une d’entre elles sert la conception et la mise en place de l’architecture de sites web. Tant il vrai que le référencement, fait partie de l’ADN de toute présence web.  J’ai dénombré pas moins de 7** types d’architectures** avec un peu d’imagination. Ces six architectures démontrent  une structure, une organisation  à un ensemble de données, les voici en partant de la base en allant vers le visiteur : Plateforme Web, Modèle de programmation, Systeme d'information (catégorisation, taxonomie), Navigation (chemins-Menus), Structuration (Ex :Orga. plate, organigramme), Ossature des urls, Forme du contenu (sa rédaction).

Ces dernières sont regroupées en 2 catégories, je  parlerais donc dans une première partie des l’**architectures  techniques**, et dans un second temps de celles qui intéressent l'**organisation des contenus** dans une optique d'optimisation pour les moteurs de recherche (seo), ah, enfin !

[![architectures-web-287x300.gif](/images/blog/architectures-web-287x300.gif) 7 Architectures web
## **Architectures Techniques d'une présence web **

### Plateforme web

Celle -ci intéresse l’**ossature physique des fichiers** sur un serveur web. Elle peut être est le résultat d’une organisation personnelle ou imposée dans le cadre de l’utilisation d’un code open source.

[![1-architecture-fichier-physiques-310x288.gif](/images/blog/1-architecture-fichier-physiques-310x288.gif) Arborescence des fichiers d'un site web
### Programmation web

Reprenons le cas de l’utilisation d’un CMS, type Joomla. Le modèle de **conception type MVC**, va s’appuyer sur l’organisation des fichiers du Framework (vu ci-dessus) au travers de son processus de scripts.

[![2-architecture-Technique-cms1-310x139.gif](/images/blog/2-architecture-Technique-cms1-310x139.gif) Processus programmation objet web d'une page
## **Architectures d’organisation de contenus (pour une meilleure indexation web)**

### Structure du système d’information

Selon son **système d’information** et son **articulation**, il va falloir prêter attention, avant de faire son choix de plateforme de diffusion, aux possibilités  offertes par le système de gestion de contenu (blog, ecommerce, cms). Exemple, pour ceux qui ont connu Joomla !, jusqu’à la version 1.6, l’opportunité de faire nativement du multi catégoriel était tout simplement impossible.Heureusement qu’avec l’adjonction de composants tierces, des parades furent possibles. L'objectif ici, est de **construire une suite logique** à la granularité de son contenu, et donc de la fluidité dans la "lecture" du site.

[![3-sous-categorie-310x138.gif](/images/blog/3-sous-categorie-310x138.gif) Agencement Multi-catégorie faisable ?

Je rajoute cet article , visuel, en anglais sur une méthode pour[ élaborer une stratégie interne de liens](http://www.seomoz.org/blog/internal-linking-strategies-for-2012-and-beyond)
### Structuration  de l'info et SEO

Niveaux et profondeur de liens

Il est fortement conseillé d’avoir une profondeur maximale de 4 clics sur les pages les plus profondes. Cela aussi bien pour les crawlers de moteurs de recherche, que pour faciliter la visite de l’internaute.

Ce schéma ci-dessous essaie de démontrer néanmoins l’opportunité des pages profondes, face au concept de longue traine. En outre, il est conseillé de réactualiser les pages anciennes (profondes ou pas)  afin d’envoyer un signal de fraicheur aux moteurs.

[![4-profondeur-navigation-310x206.jpg](/images/blog/4-profondeur-navigation-310x206.jpg) Profondeur de navigation et Longue traine

Le principe  traditionnel veut que l’articulation de l’information se fasse donc sur 4 niveaux pour une diffusion du page rank, à partir  de la page d’accueil  puis transmission sur le reste des pages.  Les moteurs, donc Google, attribue selon le degré d’autorité et de confiance au site, un certain seuil de crawlabitité au-delà duquel, les pages ne sont plus crawlées et encore moins indexées. De plus, il est conseillé de ne pas dépasser plus de 100 liens par page. Je reprends ici les schémas de seogadget qui font référence sur le sujet. Pour les sites ou le nombre de pages est conséquent, introduire au niveau de la page d’accueil, un plan de site de nature html qui permettra d’accéder aux sous catégories du site. Un sitemap de type xml, répertoriant les pages prioritaires, peut aussi servir de guide aux spiders.

[![5-siloisation-310x161.gif](/images/blog/5-siloisation-310x161.gif) Architecture plate and jus de lien (link juice)

Ce schéma en dit plus sur l’idée que pour donner de la force, du poids à un contenu, ce dernier doit être compartimenté. Cela se comprend finalement et le vieil adage fait foi « chaque chose à sa place, et une place pour chaque chose » (siloing).  Le cross-linking est aussi à recommander pour faire un maillage interne optimal d’une page à l’autre, mais ceci est à faire de manière logique et en lien, c’est le cas de le dire,  avec la thématique du contenu (sémantique).

[![6-architectureNavigation-310x147.jpg](/images/blog/6-architectureNavigation-310x147.jpg) "Siloisation" des contenus
**Menus de Navigation**

Comment atteindre ce(s) contenu(s) ? Les menus de navigation doivent si possible être explicite, là aussi, cela est directement relié aux fonctionnalités natives de la solution web adoptée. Une logique standard  marketing préconise une catégorisation de l’information (et ses  sous catégories éventuelles) qui achemine le visiteur vers la fiche produit ou service. Si pagination (donc liste d’urls), il faudra veiller à utiliser les tagages prévus à cet effet (rel= « next » and rel= « previous ») ou d’user du « rel »=canonical, afin d’éviter une pénalisation pour  plusieurs urls qui amènent au même contenu.

[![7-navigation-310x228.gif](/images/blog/7-navigation-310x228.gif) Tunnel de navigation

Cette méthode sera reprise pour nommer les interfaces (boutons, liens) de navigation sur le site. Attention à ne pas utiliser des menus javascripts, illisible pour les moteurs, ils sont souvents agréables à l'oeil mais sans pertinence pour les search engines.

[![8-navigation-278x300.jpg](/images/blog/8-navigation-278x300.jpg) Architecture de navigation
Configuration des liens hypertexte.

Sans rentrer dans les détails de la réécriture d’urls, cela tombe sous le sens de pouvoir avoir une plateforme qui génère une url par page (éviter ainsi le duplicate content), et que cette dernière reflète les menus de navigation.

[![9-construction-urls-310x20.gif](/images/blog/9-construction-urls-310x20.gif) Ossature des Urls
**Forme du contenu rédactionnel**

La pyramide inversée, une autre forme d’architecture,  a pour objectif d’attirer l’œil du lecteur. D’abord elle présente le primordial, ce qui est d’actualité, ce qui intéresse celui qui lit,  puis  continue vers le moins en moins important *(Désolé pour l'auteur de cette illustration ci dessous, j'ai oublié son nom).*
Très anglo-saxons, les premières lignes résument l’information en s’appuyant sur les 5W  (qui ? quoi ? quand ? où ? pourquoi ?) et le 2 H (how, how much, comment, combien ?).  Voilà le jargon que tout bon journaliste connait par cœur !

[![10-redaction-web-310x173.jpg](/images/blog/10-redaction-web-310x173.jpg) Archi. du contenu rédactionnel

Ces architectures doivent baigner dans une expérience utilisateur optimale, on parlera alors d’ergonomie web ! CQFD
---
title: "Wordpress et le Gestionnaire de Balises"
date: 2014-07-11
author: "admin"
categories: ["Google Analytics"]
tags: []
slug: "gtm-et-le-cms-wp"
---

Le dernier article portait sur les avantages d’utiliser un système de marquage comme le **tag manager** pour suivre ce qui se passe sur un site web. Maintenant, intéressons-nous plus à  la pratique et à sa mise en place de ce GTM.  Principes d’installation, intégration manuelle dans WordPress, et enfin à travers **un plugin prêt à l’emploi**.

## **Principes d’installation du google tag manager**

Dans le cadre d’un suivi via** Google analytics**, mais ce n’est pas obligatoire, voici les 3 grandes étapes à suivre pour installer le GTM :

	- Créer un compte Google analytics, récupérer l’id

	- Ouvrir un compte sur la plateforme GTM

	- Copier-coller sur le site le code fourni

	- Installer, selon besoin, un datalayer (pour des besoins de personnalisation, pour collecter des données non disponibles sur la page visitée (ecommerce sur la page de remerciement)

[![mise-en-place-gtm-analytics-310x209.jpg](/images/blog/mise-en-place-gtm-analytics-310x209.jpg) Position du GTM dans la page
## **Exemple d’intégration dans un WordPress sans plugin**

	- Faire les étapes 1 et 2 du chapitre précédent

	- Mise en place du **container** : Intégrer dans le header de WordPress (voir selon les templates le bon fichier (sous thème du Template dit child theme) ,ici sous  le modèle de Thesis de diythemes il faut aller sur : /wp-content/thesis/skins/classic-r sur le fichier nommé custom.php dans lequel je vais coller le code du container.

	- **Datalaye**r : même chemin que précédemment (2), et là cela se Corse (n’est pas Julien), car oui, Mr Coquet nous mâche le travail et nous divulgue un datalayer tout prêt à l’emploi qui permet de récupérer des variables comme :

	- Le type de document consulté

	- Le nom de l’auteur

	- La catégorie visitée

	- La page

	- Le libéllé

	- Le nombre de commentaires

Ce datalayer est donc un objet JavaScript qui crée un tableau avec à l’intérieur des cases avec des données noms + valeurs présentent dans le Framework de WP, mais pas accessible nativement sur la page consulté par le container « out of the box ».

Ce script techniquement collecte les variables :

a)  De l’url (doc, chemin, référent)
b)  Le N° UA si pas renseigné au préalable sous forme de macro dans le GTM basique
c)  Les 404 (url non disponible)
d)  Les attributs de la page d’accueil (type de  post et catégorie si non renseigné dans le gtm au départ), le contenu des pages web de WordPress (voir liste ci-dessus)

[![datalayer-gtm-310x275.jpg](/images/blog/datalayer-gtm-310x275.jpg) Extrait du code d'un Datalayer pour WP
## **Les Plugins WP pour le GTM**

### Offres de la communauté WP

J’ai pu repérer quelques  plugins pour intégrer d’une manière simple ce sacré container.  Les plugins s’installent par défaut dans le footer de WP. Il faudra donc, comme pour l’installation manuelle, si l’on souhaite le container dans le body, hacké le header du thème d’une petite ligne de code prêt à copier (ou presque). Selon Phil Pearce qui édite un guide très complet sur le sujet, 3 plugins sortent du lot dont :

	- Wp Google tag manager (fonctionnalité basique, pas mise à jour depuis Janv 2013)

	- Metronet Tag Manager (plus puissant et customizable mais pas à jour Juillet 2013)

	- [Duracell Tomi Google Tag Manager](http://wordpress.org/plugins/duracelltomi-google-tag-manager/) (à jour, avec le support du développeur et un micro site dédié)

Le dernier reste mon préféré. Il est vrai que j’ai rencontré son développeur, **Thomas Geiger** (programmeur de formation),  lors d’un sommet Adwords à San Francisco (Ca le fait non ?) car il est aussi « Top Contributor »  comme votre serviteur.  Thomas vit à Budapest et travaille pour l’une des plus grosses agences de Hongrie.  Il a créé ce plugin pour GTM ors de l’été 2013, il devient celui le plus téléchargé depuis quelque temps. Hormis ce fait, il est fait réellement pour les non-développeurs (comme moi), et cependant retire l’essentiel de la richesse de WordPress.
### Fonctionnalités GTM apportées par le plugin de Thomas

	- Pages et articles : titres, dates, nom de catégorie, libellé, nom de l’auteur, type d’article

	- Utilisateur loggué, son rôle

	- Recherche sur site

	- Données navigateur et système d’exploitation et appareil

	- Suivi des clics (sortant, téléchargements, email)

	- Tracking de formulaire (entre les champs)

	- Social plugins

	- Scrolling de souris

	- Intégration sur Contact form 7 et Woo Commerce

	- Flexible : désactivation depuis wp de certaines balises, macros du container.

[![plugin-gtm-analytics-310x154.jpg](/images/blog/plugin-gtm-analytics-310x154.jpg) Interface du Plugin duracelltomi.com

C’est tout de même pas mal non ?
### **Lecture des rapports : Evènements avec Clics et Scrolling**

Trop de données, tuent celles dont on a cruellement besoin, mais bon, pour le fun dirons-nous, le scrolling de la page est amusant, cela fait partie des évènements à lire dans les rapports standards.

[![scrolling-site-310x189.jpg](/images/blog/scrolling-site-310x189.jpg) Rapport Evènements issu du GTM
## Infos supplémentaires sur le gestionnaire

	- MicroSite dédié [http://duracelltomi.com/](http://duracelltomi.com/)

	- [Guide Technique complet du GTM](http://superweek.hu/files/phil-pearce-gtm-guide-v3_7.pdf)

	- Datalayer dans WP : [http://juliencoquet.com/en/2014/01/22/data-layer-google-tag-manager-for-wordpress/](http://juliencoquet.com/en/2014/01/22/data-layer-google-tag-manager-for-wordpress/)
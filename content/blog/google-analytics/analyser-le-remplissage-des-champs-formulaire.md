---
title: "Solutions pour taguer les pages de formulaires"
date: 2013-09-04
author: "admin"
categories: ["Google Analytics"]
tags: []
slug: "analyser-le-remplissage-des-champs-formulaire"
---

Cette rentrée est partie sur les chapeaux de roues, passons sans plus attendre à la façon de pouvoir ** tracer  le succès des formulaires **(et leur conversion)** **. Cet  outil est indispensable, il est la base du contact prospect dans une stratégie de  génération de leads en ligne (en terme savant) ou alors suivi de panier (succession de formulaires) . L'idée m’est venue lors d’une question sur la communauté française Google analytics. Bref, les formulaires sont partout dans notre monde numérique, pas une seconde ou connexion sans remplissage d’**un champ  login ou mot de passe**. Nous verrons donc le **suivi des formulaires** **pour Google analytics**, comme d’habitude me dirait vous ? .. mais bon, cela reste, avec Piwik une des solutions accessibles pour le grand public, alors... Quatre chapitres au programme, la méthode classique,  celle des plugins,  les scripts du marché puis enfin, le principe d'un tracking externe (FBook).

## **Méthodes de tracking de formulaire classiques**

Le contexte ici est celui d’un site développé sur mesure hors des Framework de cms  (WordPress, drupal, Joomla).

### La fameuse « Page de remerciement »

Traquer par la page de remerciement : sur le bouton envoyer une redirection JavaScript  est faites vers une page avec un petit message sympathique, ex : /merci.html cette page est ensuite traquée comme objectif dans GAanalytics.

Code : 

	- Aucun moyen d’avoir une analyse de champs des formulaires

	- Fiable (vis-à-vis  d’un enregistrement par méthodes de pages vues virtuelles ou évènements peut traîner la patte)

[![form0-310x186.jpg](/images/blog/form0-310x186.jpg) Principe Redirection Page de remerciement

L’analyse des abandons sur un formulaire. L’idée ici est d’aller identifier les goulots d’étranglements du formulaire, en identifiant chacun des champs et de mesurer leur taux de remplissage.

### Le Duo de Tracking Javascript de google analytics

1/ Traquer par la méthode des **pages vues virtuelles**   comme pour un panier e-commerce à l’aide de la syntaxe Jus de GA.                         Code :  "_gaq.push();"
Inconvénients de cette formule

	- Augmenter artificiellement le nombre de pages par visites

	- Diminue le temps passé sur la page

	- Influence la profondeur des rapports

	- Affectera les rapports sur flux d’objectifs

Donc des parades existent dans GA pour ne pas polluer les rapports standards

	- Utiliser un profil séparé distinct

	- Intégrer un filtre pour ne pas polluer dans votre profil standard les  pages générées par la consultation des champs.

[![principe-suivi-champ-formulaire-310x157.jpg](/images/blog/principe-suivi-champ-formulaire-310x157.jpg) Schéma de principe suivi abandons de champs

L’avantage de la page vue est la possibilité d’assigner plusieurs étapes avant l’objectif final sans compter qu'elle s'adapte mieux au contexte de la page.

2/ Tagguer avec la méthode de l’**évènement basique.**

21.**  **Code : "_gaq.push();"

La fonctionnalité  enregistre l’action visiteur comme pour la méthode _pagesview mais le désavantage ici, outre le fait que cette méthode soit plus dédiée à l’échelle du site et non d’une page,   c’est que l’évènement ne permet pas d’établir des objectifs fixes, et la schématisation dans GA n’est donc pas possible (entonnoir visuel). Ici, on ne traque que le fait que le formulaire ait été complété.

22. Pour un suivi des champs de formulaire individuellement ([méthode lunametrics](http://www.lunametrics.com/blog/2012/11/13/track-form-abandonment-google-analytics/#sr=gp&m=r&cp=(sfgfssbm)&ct=/vsm-tmc&ts=1377704193) plus sophistiquée)

Basé sur la même méthode d’évènement, mais à base d’une librairie JS Jquery idéale pour écouter les évènements qui se passe sur ces champs de formulaire. Le tracking se fait sur l’ensemble des champs, avec soit un remplissage soit un non remplissage.

[![evenementjpg-310x142.jpg](/images/blog/evenementjpg-310x142.jpg) Processus de suivi à base d'évènements (Sce Lunametrics)
## **Taguer son formulaire dans le cadre de plateformes de gestion de contenus**

Les éditeurs et bloggeurs sur des plateformes prêtes à l’emploi  sont plus chanceux quant à la mise en place de solutions de tracking formulaire.

### WordPress et le plugin contact 7 form

Tracking formulaire classique au travers d'un CMS

Pas très original comme choix de plugin mais efficace si l’on souhaite suivre ses conversions dans Google analytics. Le terrible avantage avec  ce plugin de formulaire  est son intégration facile  avec WordPress et Google analytics. Il suffit de rajouter une ligne de code dans le champ prévu à cet effet, situé en base de sa configuration.

[![contactform-310x211.jpg](/images/blog/contactform-310x211.jpg) Configuration d'un suivi de redirection avec d'un pluging

Les codes : Redirection, pagesvues ou évènement , c’est au choix selon critères indiqués plus haut ) :

	- on_sent_ok: "location = 'https://www.mauricelargeron.com/merci-pour-votre-interet/';"

	- on_sent_ok: “

	- on_sent_ok: "

Pour plus d’infomation à ce sujet consultez la fin de cette page avec notamment un article de Ronan Chardonneau ainsi que celui du concepteur du plugin.

Tracking du marketeur Geek !

Je résume l’idée ici seulement de Julien Coquet, qui permet toujours via ce  plugin de formulaire de collecter dans une base donnée  (grâce  à un ajout de plugin dédié) les données de GA et notamment un de ces fameux cookies de **suivi  de campagne _utmz** . Pourquoi  faire ? Eh bien pour étoffer son crm d’information utile  comme par exemple collecter la provenance de l’envoyeur du formulaire. Pour en savoir plus, consultez en fin d’article le lien sur le sujet !

## Scripts  du marché pour Joomla, drupal, tumblr

Pour aller plus loin sans toucher au code, ces formules sont intégrables sur des sites sur mesure ou sur des plateformes web , des scripts prêt à l’emploi d’analyse visiteurs possèdent des fonctionnalités spécifiques pour traquer les conversions de formulaires. Je prends ici 2 exemples « clicktale »  et « sessioncam » pour illustrer ce propos. Il suffit de télécharger leur code source respectif puis de spécifier les pages à suivre et le tour est joué ! Attention cependant aux éventuels conflits de scripts qui peuvent ralentir le chargement des pages.

Clicktale avec un tableau de bord évolué qui permet d’avoir les indicateurs d’abandon agrégés sur l’ensemble des formulaires, des rapports de conversion sous forme d’entonnoir semblable à Google analytics.

[![scripts-217x300.jpg](/images/blog/scripts-217x300.jpg) Tracking et Reporting avec script Clicktale

SessionCam offre une plateforme semblable avec aussi la possibilité de suivre de près ces formulaires. L’interface est plus sobre mais semble aussi efficace !

[![wordpress-310x248.jpg](/images/blog/wordpress-310x248.jpg) Reporting de la plateforme/script SessionCam
## **Tracking Externe de formulaire : cas facebook**

Pour un tracking adapté, il conviendra d’utiliser une solution serveur qui va permettre d’installer un code de suivi Google analytics [avec cette méthode ](http://www.webdigi.co.uk/blog/2010/google-analytics-for-facebook-fan-pages/)  (code open source de tracking d’image  pouvant être installé sur son propre serveur) sur une page Fbml codée pour l’occasion avec cette outil [http://french.jotform.com/](http://french.jotform.com/) . En effet, le fbml n’accepte pas nativement le code javascript de Google analytics (GATC) , donc ce système est une parade possible, pas testé mais semble avoir une bonne notoriété.

Sinon, autre solution mais plus basique, avec  le cas du formulaire doté d’un  bouton « envoyer » (tagué des variables utm de suivi de campagne GA),  sur une page de remerciement hors Fbook (lien sortant).

## Webographie formulairienne !

	- Principes de bases  [http://www.converteo.com/blog/web-analytics/google-analytics-tagger-le-remplissage-dun-formulaire-astuce-n%C2%B06/](http://www.converteo.com/blog/web-analytics/google-analytics-tagger-le-remplissage-dun-formulaire-astuce-n%C2%B06/)

WordPress

	- Méthode  pour le plugin [contact 7 par Ronan Chardonneau](http://blog.inextcom.fr/2012/02/tracker-contact-form-7-pour-wordpress-dans-google-analytics/)

	- [Formulaire et crm par Julien coquet](http://juliencoquet.com/2012/07/19/formulaires-de-contact-wordpress-et-google-analytics-contact-form-7/) (suivi de provenance)

Analyse qualitative (en) :

	- [Mesure de la qualité d’un formulaire](http://analytics.blogspot.fr/2010/04/how-to-measure-quality-of-online-form.html) en ligne par bluerank sur blog GA
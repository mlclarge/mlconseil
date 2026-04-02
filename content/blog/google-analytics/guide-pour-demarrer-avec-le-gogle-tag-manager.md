---
title: "Tutoriel Gestionnaire de balises Google"
date: 2012-12-26
author: "admin"
categories: ["Google Analytics"]
tags: []
slug: "guide-pour-demarrer-avec-le-gogle-tag-manager"
---

Google Tag manager est un service gratuit offert depuis quelques semaines qui aide bien pour faciliter son suivi dans [google analytics](https://www.mauricelargeron.com/google-analytics-devient-universel/). C’est un endroit unique, centralisé, qui permet de gérer les balises d’un site web. Je rappelle qu’une balise est constituée  par un bout de code qui permet  la collecte de statistiques  dont l’analyse des pages vues, le suivi e-commerce,  l’analyse des différentes conversions, le tracking social, démographiques etc…

Certains sites peuvent recueillir jusqu’à 20 balises ! Sans la plateforme GTManager, il faut à chaque nouvelle balise, modifier le code source du site. Google tag manager vient simplifier le process de tracking (suivi) en y ajoutant des fonctionnalités de personnalisation (macros, règles).

[![Image](/images/blog/1-avant-apres-tag-manage-310x260.gif)](https://www.mauricelargeron.com/wp-content/uploads/2012/12/1-avant-apres-tag-manage.gif) Fig. 1 Avant & APres le Tag manager

Gtm fournit par défaut le paramétrage de balises dont bien sûr Google analytics.

[![Image](/images/blog/2-balises-tags.gif)](/images/blog/2-balises-tags.gif) Fig.2 Les differentes balises (ou tags) dans GTM
## **Principes de base et tagage Google analytics**

S’il s’agit d’utiliser le GTManager sur un site déjà tagué, il conviendra bien sûr de nettoyer en amont tous les tags existants. Donc se connecter sur la plateforme GTM, et créer un container à rajouter sur toutes les pages du site, et c’est tout (fig.3).

[![Image](/images/blog/3-container-tag-manager-310x201.gif)](https://www.mauricelargeron.com/wp-content/uploads/2012/12/3-container-tag-manager.gif) Fig. 3 Le container a installer sur son site

Ensuite, selon ce que l’on souhaite acquérir comme données sur le trafic de son site, il conviendra de rajouter les balises de son choix depuis l’interface de GTM. Prenons ici, un exemple basique, celui du code de suivi de Google analytics (GATC). Trois étapes sont indispensables pour « marquer » un site web d’une balise (fig.21)

[![Image](/images/blog/4-ga-et-gtm-310x172.png)](https://www.mauricelargeron.com/wp-content/uploads/2012/12/4-ga-et-gtm.png) Fig. 4 Installation d'1 balise

Concrètement sur Google tag manager, je choisis la nature de la balise (ici GA), une règle (sur toutes les pages) (éventuellement (facultatif)  une restriction selon mon plan de tagage) et enfin  une publication (version).

[![Image](/images/blog/5-balises-ga-310x228.png)](https://www.mauricelargeron.com/wp-content/uploads/2012/12/5-balises-ga.png) Fig. 5 Balisage Google Analytics

Donc pour toutes balises, il faut obligatoirement assigner une règle qui régit leurs déclenchements. Une règle est composée d'une ou plusieurs conditions, chacune se présentant sous la forme d’une macro. Trois macros par défaut sont définies dans GTM *(URL", "URL de provenance" &  "événement***)**,  elles permettent généralement le paramétrage de règles les plus fréquentes. La publication peut être faite globalement sur un ensemble de balises en une seule fois.

[![Image](/images/blog/6-regles-gtm-230x300.png)](https://www.mauricelargeron.com/wp-content/uploads/2012/12/6-regles-gtm.png) Fig. 6 Regles depuis les Macros GTM
## **Utilisation des macros**

Les macros permettent donc la personnalisation des déclenchements de balises, elles sont capables d’aller chercher des variables de balises spécifiques *(paire nom – valeur)*  qui vont donner naissance aux futures règles de tagage.

[![Image](/images/blog/7-macros-gtm-279x300.png)](https://www.mauricelargeron.com/wp-content/uploads/2012/12/7-macros-gtm.png) Fig.7 Types de Macros GTM

On peut, à titre d’exemple, utiliser une macro qui va se déclencher selon une valeur déterminée par une balise de suivi. Pour illustration, pour  le suivi d’un [évènement](https://www.mauricelargeron.com/objectifs-et-evenements-dans-google-analytics/) la macro récupère une variable personnalisée (custom var) d’une balise sur une page d’un blog. Toute chose étant égal par ailleurs, il faudra éditer une règle de restriction dans le suivi de base de GA, pour ne pas avoir de doublon sur cette page spécifiquement.

[![Image](/images/blog/8-evenement-310x287.gif)](https://www.mauricelargeron.com/wp-content/uploads/2012/12/8-evenement.gif) Fig.8 Evènement dans GA
## **Suivi e-commerce  avec le tag manager**

Il existe plusieurs méthodes pour assurer le suivi e-commerce d’un panier. En voici une en 4 étapes. Le script et le tag sont à placer sur la page de confirmation d’achat.
1 – Formater avec les [variables couches de données](https://developers.google.com/tag-manager/reference#varnames) de Google analytics, un script à insérer avant le container tag manager sur la page de confirmation de commande.

[![Image](/images/blog/9-ecommerce-couche-donnee-310x292.png)](https://www.mauricelargeron.com/wp-content/uploads/2012/12/9-ecommerce-couche-donnee.png) Fig. 9 Couche de données pour Tag Ecommerce

2 –Faire autant de macros que de variables dans Tag manager

[![Image](/images/blog/10-ecommerce-macro-1-310x160.png)](https://www.mauricelargeron.com/wp-content/uploads/2012/12/10-ecommerce-macro-1.png) Fig. 10 1 des Macros ecommerce (data layer)

3 – Créer ensuite la balise à l’aide d’un « html personnalisé »

[![Image](/images/blog/11-ecommerce-balise-310x202.png)](https://www.mauricelargeron.com/wp-content/uploads/2012/12/11-ecommerce-balise.png) Fig.11 Balisage dans GA

4 –Faire une règle pour déclencher la balise.

[![Image](/images/blog/12-ecommerce-regles-310x129.png)](https://www.mauricelargeron.com/wp-content/uploads/2012/12/12-ecommerce-regles.png) Fig. 11 Règle Déclenchement balise

Il existe aussi une autre manière , décrite ici par Pavel , son developpeur,* (avec bibliothèque Jquery)* : [http://www.ga-script.org/en/posts/2012/12/gtm-tracking-ecommerce-transactions-with-tag-manager](http://www.ga-script.org/en/posts/2012/12/gtm-tracking-ecommerce-transactions-with-tag-manager). Pour résumer, elle consiste à rajouter au Tag GA existant, la fonctionnalité "transaction" avec une règle basée sur un évènement 'trackTrans" (on aura pris le soin préalablement dans la config. GAnalytics de permettre le suivi ecommerce ;) )

## **Ce que ne fait pas le Gestionnaire de balises**

Les **balises synchrones** ne sont pas pris en charge, celles qui utilisent la fonction « **document.write **», ou celles liées à la structure de la page (widget sociaux par ex.).

Pas de tableaux de bord de suivi des déclenchements de balises. Tag manager n’est pas compatible avec le** test A/B**.

## Compléments d'informations sur la gestion de tags

Je remercie les articles suivants qui m'ont permis de débroussailler le sujet :

 	- Couche de données : [Aide developpeurs Google](https://developers.google.com/tag-manager/devguide#datalayer)

 	- Suivi e-commerce : Article de Lothaire Ruellan sur le [tracking ecommerce dans GA](http://www.chaoticinflation.com/93-tips-and-tricks-for-implementing-google-analytics-tags-via-google-tag-manager)

 	- Généralités sur techniques de tagage avec le post de [Marc Pantoliano sur Seomoz.org](http://www.seomoz.org/blog/what-is-tag-management)

**Bonne année 2013 à tous ! **
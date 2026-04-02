---
title: "Comment débugguer l'AMP avec WordPress"
date: 2018-06-04
author: "admin"
categories: ["Marketing Digital"]
tags: []
slug: "comment-debugguer-lamp-avec-wordpress"
image: "/images/blog/smart-adwords.jpg"
---

Accelerated mobile page reste la technologie de pointe pour mettre en avant des contenus rapidement chargés sur les appareils mobiles. Mais je profite de partager une petite expérience avec l’AMP sur mon  site WordPress, sans prétention technique mais destiné au non dev.  par excellence  !  Installé avec le plugin classique de Wordpress.com, mes pages se sont mises tout d’un coup à ne plus fonctionner d’après la search console. Comme c’est elle qui fait foi pour son indexation dans Google il a fallu donc trouver la parade.

[![search-console-google-310x119.jpg](/images/blog/search-console-google-310x119.jpg) search console googlee et amp
## **La solution changez de plugin !**

Bon ok  pas très originale la combine,  mais sans connaître la cause réelle, c’est vrai, j’ai pu réparer à court terme ce bug, c’est après tout l’essentiel. J’ai avant de désactivé, vérifié aussi les mises à jour, ré-activé, sans succès.

[![desactivee-310x171.jpg](/images/blog/desactivee-310x171.jpg) Désactivation de l'AMP de Wordpress.com

J’ai donc eu recourt à ce plugin, dont l’installation est simplissime et fonctionne sans réfléchir. De plus, la customisation des  pages offertes par ce plugin est sans commune mesure plus complète que celle de la maison mère de WordPress !

[![plugin-amp-310x177.jpg](/images/blog/plugin-amp-310x177.jpg) Plugin amp de remplacement

La validation si on veut être rassuré peut se faire à l’aide d’une extension AMP validator.

[![amp-plugin-183x300.jpg](/images/blog/amp-plugin-183x300.jpg) Validation à l'aide d'une extension navigateur
## **Reconfigurer le tracking des pages AMP**

Là aussi, avec ce nouveau  plugin, il faut repenser au mode de tracking. J'utilisais  celui de Yoast (amp glue) mais j'en ai profité pour en changer du coup.   Ainsi je centralise dans un seul plugin, génération et suivi de pages AMP. Il suffit d’avoir une propriété Google analytics dédiée et renseigner l’Id dans les paramètres du plugin. Encore, cela fonctionne sans attendre, sans bug.

[![amp-google-analytics-310x175.jpg](/images/blog/amp-google-analytics-310x175.jpg) amp google analytics

Il existe aussi d’autres solutions, sans passer par une autre propriété GA, comme celle de passer par l’ajout en dur de bout de code, ou par Google tag manager.

[![amp-julien-coquet-310x241.jpg](/images/blog/amp-julien-coquet-310x241.jpg) Autres solutions : code et GTM

L’avantage ici, est d’avoir tout regroupé dans une même propriété, restera ensuite à filtrer ou segmenter selon son choix au niveau des vues, pour avoir des rapports dédiés d’audience de ses pages AMP.

## **Point du projet AMP vu par Eric Enge au  SMX 18 **

Terminons avec  Éric Enge, un gourou US du net, sur  sa vision de l'AMP.  Non ! ce n'est pas seulement un format pour les médias, mais aussi pour du lead, de l’ecommerce. Les internautes comment réagissent-ils au symbole l’éclair dans les serp de Google ? Les possibilités de rendre ces pages dynamiques et attrayantes existent.  Les parallèles avec les PWA, la problématique du tracking, bref voici la prez :

Alors bon débuggage !
---
title: "Gtag.js vers une nouvelle méthode de tracking Google ?"
date: 2017-09-04
author: "admin"
categories: ["Google Analytics"]
tags: []
slug: "vers-une-unification-des-tags-de-tracking"
---

Google vient de créer une nouvelle méthode globale de tracking. Avant que cela soit déployé sur tous les comptes, il va encore se passer un peu de temps ! Mais pas d’affolement à avoir, apparemment aucun changement ou migration à terme n’est à prévoir dans les comptes de Google analytics par exemple.

## ***Historique dans les librairies de suivi JS***

Profitons-en pour faire un petit historique sur les différents librairies qui collectent la data et produisent les rapports d’analyse d’audience.

[![Image](https://www.mauricelargeron.com/wp-content/uploads/2017/09/histoire-librairies-js-502x263.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2017/09/histoire-librairies-js.jpg) Histoire librairies js de google
## ***Comment installer Gtag.js sur un site web ?***

Ne faites rien pour l’instant, sauf des tests éventuels, rien d’obligatoire du tout et loin de là. Sinon, sur toutes les pages du site, il faudra pose ce tag, la base pour collecter les pages vues, les évènements, voir plus bas pour les nouveautés, les pages d’écrans d’applications (rapprochement avec firebase), les temps de chargement, des exceptions (crash ou erreurs du site).

window.dataLayer = window.dataLayer || ;
function gtag(){dataLayer.push(arguments)};
gtag('js', new Date());

gtag('config', 'GA_TRACKING_ID');

## ***Objectifs de Gtag.js : unification et simplification***

### ***Unifier les méthodes de suivi***

L’objectif de cette nouvelle méthode, serait d’unifier les différents modes utilisées sur les différents objets de tracking de Google et principalement sur son protocole de mesure,  les conversions, le remarketing. Cela toucherait  donc les produits comme **Google analytics** (analyse d’audience), ** adwords** (petites annonces liens sponsorisés et display), **firebase** (application mobile). A suivre donc !
### ***Simplifier par un data model par défaut, exemple des évènements***

Le Suivi d’évènement (clics, scrolling, téléchargement)  par exemple est taggué par défaut dans son modèle de data où la catégorie, action et libellé sont automatiquement renseignés, sauf personnalisation. Par exemple, un event comme une authentification nommé « login » taggué comme tel :

gtag('event', 'login');

Aura pour résultat de lecture dans GA

 	- Catégorisation : « engagement »

 	- Action : « login »

 	- Libellé : «not set », ou « monsiteweb » si renseigné comme ci-dessous

gtag('event', 'login', {'method': 'nomdemonsite'});

La syntaxe complète pour personnaliser sera :

gtag('event', 'login', {
'event_category': 'acces_au_site',
'event_label': 'nomdemonsite'
});

Liste des events nommés par défaut : [https://developers.google.com/analytics/devguides/collection/gtagjs/events#send-events](https://developers.google.com/analytics/devguides/collection/gtagjs/events#send-events)

Voilà pour cette information fortement inspirée de l’aide en ligne de Google developper, du post sur Google + de Stéphane Hamel, et de l’article de Traa Dunn [d’enor](https://www.e-nor.com/blog/google-analytics/google-analytics-new-global-site-tag-offers-unified-google-product-tracking) . Merci à eux !
---
title: "Les Cookies Démasqués !"
date: 2015-10-26
author: "admin"
categories: ["Google Analytics"]
tags: []
slug: "les-cookies-demasques"
image: "/images/blog/cookies-et-mouchards.jpg"
---

Tout savoir sur les traces.. ou presque ! Mine de rien, dernière ces petits scripts et fichiers textes qui ne pèsent pas grand-chose sur nos interfaces (pc, mobile, tablette) , repose une lourde industrie publicitaire à plusieurs milliards d’euros. Mais, à quoi ressemblent-t-ils, comment se les représenter ?  Un sujet pour les marketeurs, « visuels »  qui souhaitent en savoir plus sur l’écosystème de cette technologie sans rentrer dans la syntaxe du code .

## **A quoi servent les cookies ? **

Les cookies,  constitue la mémoire des usages du visiteur de l’internet sur un site web. En effet, entre 2 pages visitées sur un même site, sans cookie, aucun  lien n’est effectué entre la consultation de ces 2 pages. Le navigateur reconstruit de A à Z chaque page lors de tout nouvel appel. Vous allez me dire que non, et que le cache, cela sert aussi à accélérer une page ! Oui c’est un atout technique mais pas n’apporte rien sur l’historique d’un ensemble de pages. Après tout, le parcours d’un visiteur, c’est cela qui est intéressant non ?

### ***Constitution et Fonctionnalités des mouchards***

Oui, on peut aussi les appeler comme cela.  Ils sont constitués  de scripts et de cookies. Les scripts (JavaScript par exemple mais d’autres méthodes existent..) servent à  installer les cookies et à leur donner du sens.

Il existe différentes vocations à ces traces . Les objectifs sont multiples : reconnaissance des visiteurs (cookies de 1ere partie) dans le cadre d’un CRM, et partenariats avec des tiers (enrichissement du site, partage de données). Exemples :

**Performance du site visité pour le visiteur**

 	- préférence d’un lecteur vidéo : sportif, Sound cloud

 	- affichage rapide de contenus via les cdn

 	- garder des préférences d’accès utilisateurs en mémoire

**Objets fonctionnels d’affichage (police)**

 	- Fonts.com

 	- typekit.net

 	- fonts.googleapis.com

**Statistiques de visites (anonymes)**

 	- google-analytics.com

 	- scorecardresearch.com

 	- Omniture

 	- ScoreCard Research Beacon

 	- Webtrends

**Engagement (commentaires, chat)**

 	- Disqus

 	- Viafoura

 	- Zopim

**Réseaux sociaux**

 	- Twitter / Facebook Connect

**Géolocalisation**

 	- Adapter le contenu aux réglages régionaux de chaque pays

**Publicité**

 	- Serveurs publicitaires : affiliation, retargeting  (Critéo, adwords) , SSP : Teads (vidéo)

**Optimisation des ventes, conversions**

 	- A/B testing (kameleoon, a/b Tasty) , analyse comportementale  (eloqua, kenshoo, salesforce)

## **Comment repérer ces mouchards ?**

Bon, le plus simple, faire F12 depuis son navigateur chrome par exemple, puis allez dans l’onglet Network, dans la colonne de gauche, voir les différents appels de fichiers qui constituent la page. Souvent les cookies sont appelés via des pixels, images comme support pour les acheminer sur les serveurs.. (.jpg) , donc depuis la colonne de gauche, naviguez jusqu’à qu’un tableau affiche le détail par colonnes..

[![Image](/images/blog/localisation-des-cookies-310x213.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2015/10/localisation-des-cookies.jpg) Depuis un navigateur

Ensuite dans ce même navigateur, il sont aussi accessible par là..

[![Image](/images/blog/visualisation-cookies-310x287.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2015/10/visualisation-cookies.jpg) Paramètres des cookies
## **Comme se  représenter ces trackers ?**

La Cnil a pu livrer voilà quelque temps déjà, un navigateur proxy qui intercepte et représente dans un navigateur chromnium **les cookies déposés et leur relation entre sites ou domaines différents**. Super l’idée…On comprend mieux le fonctionnement de la publicité, du display lors de la visualisation de relations communes entre 2 sites distinctes.

[![Image](/images/blog/mariage-sud-ouest-et-ouest-france-310x223.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2015/10/mariage-sud-ouest-et-ouest-france.jpg) Représentation Graphiques par CookieViz

En live l'affichage ..

https://www.youtube.com/watch?v=f_20J4BksSs

Cnil : http://www.cnil.fr/vos-droits/vos-traces/les-cookies/telechargez-cookieviz
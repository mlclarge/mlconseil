---
title: "Optimiser et Analyser l'audience des vidéos"
date: 2014-04-22
author: "admin"
categories: ["Google Analytics"]
tags: []
slug: "analytics-et-video-marketing"
---

Savoir présenter et **mesurer les retombées d’une vidéo,**  avant de penser directement à son contenu fait partie prenante de la réussite  ce type de **levier webmarketing** en tant qu’apporteur de trafic. Revenons sur l’état actuel de ce marché, sur quelques principes d’optimisation pour la mise en ligne,  et enfin, sur focalisons-nous sur « comment mesurer »  l’audience de ce type de support.

## Le marché de la vidéo 2014

La **vidéo**, l’avenir de l’internet ? Ben voyons !  Alors que certains chiffres annoncent une bande passante consacrée aux flux vidéos à plus de **50 % du trafic de l’internet** en 2014, les FAI, fournisseurs de tuyaux, ont des soucis à suivre et le revendiquent (polémique Free et Google en 2013).  Mais l’avenir leur réserve aussi de beaux jours  face aux défis à relever. Les fournisseurs de services qu’ils soient  Google (Ytube , Chrome Cast) , Facebook (videos ads) , Twitter (micro-blogging Vine) et bientôt Netflix (Vod) sont constamment en évolution et poussent ce marché florissant.

Les **services marketing**, selon la dernière étude de Régalix (société californienne fondée en 1998)  auprès d’acteurs important du marché US (ok c'est pas pareil chez nous mais bon) , donne  une tendance sur les projections d’investissements sur les différents **leviers marketing**. L’année 2014 est l’année où la vidéo sera un **principal support de communication**, pas moins de 94% des interrogés prévoient une croissance dans les dépenses vidéos !

[![Image](/images/blog/etude-regalix-prevision-investissemen-video-310x261.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2014/04/etude-regalix-prevision-investissemen-video.jpg) Investissements 2014 dans différents leviers online

En France, quasiment 1 internaute sur 2 a consulté  en moyenne une **vidéo par jour** d’après Médiamétrie/Netratings et 15 plateformes dominent le marché avec sur le podium Google (largement dominant), Dailymotion, et TF1.

[![Image](/images/blog/plateforme-videos-310x294.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2014/04/plateforme-videos.jpg) Principales Audiences Vidéos en France
## Optimisation  vidéo pour les moteurs de recherche (seo :) )

### **Information pour une Indexation optimale **

Rien d’extraordinaire, sinon, prendre soin au nommage de la vidéo soit 4 critères principaux :

	- **Titre**, description, mots clés, url

	- Afficher le texte (**script**) de la vidéo (si incluse dans une page externe)

	- Prévoir les **partages sociaux** sur le player

	- **Robots.txt ou sitemap**  : prévoir un sitemap dédié ou inclure dans son fichier robots.txt une ligne sur l’url de la vidéo (ici elle renvoie sur le serveur qui abrite la vidéo: wistia)

User-agent: *
Disallow: /wp-admin/
Disallow: /wp-includes/
Sitemap: https://www.mauricelargeron.com/sitemap.xml.gz
# exemple de déclaration pour la plateforme wistia
Sitemap: http://app.wistia.com/sitemaps/38945.xml

	- **Snippet schema.org** : baliser le contenu avec des balises standards de reconnaissance de l’objet, ici celui de la vidéo.

## Encheres temps réel pour le display

Processus de  mise en enchères sur le réseau display.  Merci pour la production  de cette animation par le CMSummit et BattelleMédia sous l'égide D'Adobe et developpé par the office for creative ...

	- Plus d’infos "**seo**"  ici : [https://www.mauricelargeron.com/22-criteres-seo-pour-referencer-une-video-sur-le-net/](https://www.mauricelargeron.com/22-criteres-seo-pour-referencer-une-video-sur-le-net/) et voir ici un test comparatif Google & Yt search Yooda : [un test comparatif Google & Yt search Yooda](http://blog.yooda.com/2014/04/17/3096-test-seo-videos-youtube/)

### **Oser faire des vidéos selon ces moyens**

Les requêtes « comment + verbe d’action » déclenchent souvent des résultats sur des vidéos. Prenons exemple « **comment déguster du vin **», l’avantage est que le snippet vidéo s’affiche et incite au clic. A ce sujet, les Taux de clics sur des vidéos, même placés en dehors du Top 3 sont bien meilleures que les résultats de liens organiques traditionnels.

[![Image](/images/blog/video-et-seo-310x226.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2014/04/video-et-seo.jpg) Des Serp Google sur Vidéos souvent en haut de page..
### **Test provisoire de Google sur les Serp vidéos ?**

Lu dans le très sérieux site « search engine land », il rapporte l’apparition d’un résultat avec abandon de la mignature vidéo. Espérons que ce n’est qu’un test  :) .

[![Image](/images/blog/snippets-videos-test-310x161.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2014/04/snippets-videos-test.jpg) Test de Snippet sans mignatures !
### **Choix de sa plateforme de diffusion**

Selon le type de budget alloué à la création d’une vidéo, et ses objectifs, 2 alternatives peuvent se présenter.

La plus "simple et publique",  gratuite, est celle de choisir une grosse plateforme de diffusion type **Dailymotion, Viméo, Youtube** au risque de noyer son message et son trafic. Mais cela se juge au cas par cas et selon les cibles.

La plus "propriétaire", est de choisir une plateforme spécialisée, payante mais qui offre des services personnalisés et qui ne renvoie pas  une partie de l’audience sur la plateforme mère.

Le mieux, est de **multi-diffuser,** c’est-à-dire d’envoyer son contenu sur les big players en verrouillant au maximum sur ces plateformes publiques mais aussi en intégrant un** player plus personnel** sur le site web.

**La vidéo ci-dessous** utilise un de ces services payant, celui de **wistia**, avec une première formule, gratuite avec 3 vidéos (avec en échange le nom du fournisseur sur le  player, normal..).

http://mauricelargeron.wistia.com/medias/zupnfi2c5j?embedType=popover&popoverHeight=84&popoverWidth=150&videoWidth=430

## Mesurer les retombées de visionnages

### **Avec Google Analytics et YT **Suivre les pages de sa chaîne YT

Il est possible d’affecter une UA-xxxxxx de tracking dédié à une chaine Youtube dans GA, mais ce n’est pas extraordinaire car, seul les clics sur les pages de la chaîne sont remontés, pas les interactions sur les vidéos. Néanmoins, pour que cela fonctionne, il suffit d’aller dans sa chaine YT, puis « Options avancées » et de copier-coller le numéro UA préalablement créé pour l’occasion.

[![Image](/images/blog/youtube-et-ga-310x220.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2014/04/youtube-et-ga.jpg) Intégration GA dans YT

Le résultat des clics , observés ici en temps réel..

[![Image](/images/blog/youtube-et-analytics-310x166.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2014/04/youtube-et-analytics.jpg) Chaine/Pages YT dans GAnalytics
### **Analyser ses campagnes de pub  vidéo**

Alors que le not provided apparait dans les résultats de campagne payante de Google analytics (info JvWeb), voici un nouveau reporting des **campagnes vidéos adwords** dans Google analytics.  Pratique pour avoir tout de centralisé dans un seul et même endroit.

[![Image](/images/blog/video-campagne-adwords-310x227.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2014/04/video-campagne-adwords.jpg) Nouveau rapport GA  pour les Vidéos
### **Obtenir des éléments plus poussés sur l’engagement du « visionneur »**

Ou alors configurer selon sa plateforme, un **écouteur de clics** sur les boutons du **player vidéo.** Ici les résultats d’un tracking , dans Google analytics,  avec l’aide de cette méthode élaborée par [stéphane Hamel](http://www.cardinalpath.com/youtube-video-tracking-with-gtm-and-ua-a-step-by-step-guide/). Pour lire ce rapport, il faut se rendre dans Comportement > Principaux évènements > et cela rend compte :

	- Pause, play, taux de lecture (de 25 à 100 %)

[![Image](/images/blog/google-analytics-evenements-video-310x151.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2014/04/google-analytics-evenements-video.jpg) Reporting par "évènements" GA
### **Ou alors dans Google adwords..**

[![Image](/images/blog/adwords-rapport-video-310x52.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2014/04/adwords-rapport-video.jpg) Rapport Natif dans Adwords
### **Dans le reporting de la plateforme Youtube Analytics**

Cette plateforme sait attirer le chaland avec son « analytics » très riche en données d’audience, avec 2 parties :
Vue globale :

	- **Vues**: Nombre, minutes regardées, moyenne visionnage

	- **Démographique** : hommes, femmes, âges

	- **Contextuelle**:  pages, lecture intégrée, mobiles

	- **Sources de trafic**: publicité, recherche YT, site externe, recherche google, suggestion youtube

	- **Appareils**: ordinateur, tablette, mobiles, console de jeux

Participation (engagement):

	- **Abonnés**

	- Like ou pas

	- Favoris, commentaires, partages et annotations.

[![Image](/images/blog/youtube-analytics-310x148.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2014/04/youtube-analytics.jpg) Analytics de Youtube

Voir cet article complet qui en décrit les [fonctionnalités](http://fr.shopify.com/blog/10472577-youtube-analytics-10-facons-de-suivre-la-performance)
## **Outils pratiques vidéos**

	- Télécharger des vidéos YT : [http://www.telechargervideoyoutube.com/](http://www.telechargervideoyoutube.com/)

	- Générateur de code schema pour vidéo : [http://www.sistrix.com/video-rich-snippets/](http://www.sistrix.com/video-rich-snippets/)

	- Plateforme personnalisable : [http://wistia.com/](http://wistia.com/)

	- Vidéos prêt à l'emploi: [http://www.pitchy.fr](http://www.pitchy.fr/)
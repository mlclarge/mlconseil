---
title: "Comment suivre ses sources de trafic dans google ads"
date: 2019-05-27
author: "admin"
categories: ["Campagne google ads"]
tags: []
slug: "comment-suivre-ses-sources-de-trafic-dans-google-ads"
image: "/images/blog/urls-tracking.jpg"
---

Le suivi des canaux d’acquisition revêt un caractère prépondérant par temps de RGPD. Connaître la source de ses audiences est un minimum même s’il devient plus difficile d’avoir des données personnelles.  Les plateformes publicitaires d’acquisition ont toujours mis à disposition des outils de suivi. Ces derniers consistent la plupart du temps par l’ajout de paramètres à la fin des urls de destination. Donc toutes les sources, selon l’application de mesure qui les recevra, ici Google analytics, devront être « tagguées » avec des paramètres reconnus par l’App. de web analytics. Voyons donc les spécificités d’un modèle de suivi dans un contexte classique de plateformes où les parties prenantes sont : le site web, Google ads (adwords), Google analytics, Crm (zoho), Attribution (Facebook).

[![suivi-des-urls-dans-google-ads.jpg](/images/blog/suivi-des-urls-dans-google-ads.jpg) Suivi des urls dans google ads
## **Conserver la valeur des utms sur le site Web**

Le site web, plateforme d’atterrissage, reçoit le trafic qui provient de Google ads, Facebook, twitter doit reconnaître et conserver les paramètres des urls entrantes venant de ces sources d’acquisition entrantes. C’est souvent là que réside le problème de la transmission des valeurs de ces variables « UTM » qui littéralement signifie « urchin tracking module ». Urchin étant le nom d’une ancienne startup créatrice de ce modèle avant Google analytics.  Le visiteur rempli un formulaire donc, valide un panier d’achat,  et lors du clic, il est redirigé ou reste sur la même page avec un message de remerciement à la fin. Ces paramètres UTM doivent être transmis jusqu’au bout du parcours. Pour cela,  un petit script récupère les valeurs de ces balises  qui sont alors stockées sous forme de cookies. Chaque fois qu'un utilisateur soumet un formulaire donné, les valeurs de cookie sont ensuite transmises dans des champs cachés du formulaire en question.

A savoir : Pour des questions de référentiel du système d’information, certains développeurs font des scripts qui réécrivent les variables UTM selon la provenance du trafic.

Sinon, des solutions standard d’intégration de formulaire sont prêt à l’emploi et fournisse en plus des codes de créas. de formulaires des scripts d’intégration pour récupérer, cookéifier et restituer lors de conversion les sources d’acquisition « parsées »  depuis les urls. Exemple ici d’intégration pour WordPress avec un plugin dédié :

## **Installer le suivi depuis les plateformes qui amènent du trafic**

Tout ce trafic qui vient des publicités, affiliés, référents, emailing divers considéré  comme campagnes d’acquisition d’audiences devra être taggué. Toutes les urls qui pointent vers le site web devront être décorées de variables ces « UTM » destinées à porter la source de trafic entrant.

***Modèle de données UTM***

 	- Campagne: (obligatoire) Quel est le nom de la campagne? À quelle campagne envoyez-vous le trafic? Quel est le principal domaine dans lequel vous souhaitez que les internautes qui cliquent sur vos liens ou vos annonces choisissent de participer?

 	- Source principale: (Obligatoire) Sur quelle plate-forme ou site Web ce lien est-il placé? D'où viennent ces pistes? Facebook, Google, email, blog, etc.?

 	- Moyen: (Obligatoire) Sur quelle plate-forme ou quel site web ce lien est-il placé? D'où viennent ces pistes? Facebook, Google, email, blog, etc.?

 	- Contenu: (Facultatif) Cette variable doit inclure des informations d'identification sur le contenu spécifique sur lequel ils ont cliqué. Quelle version d'une annonce était-ce? Quel était le titre? Quelle image avait-il? Quel CTA avait-il? Cette variable doit être complètement unique pour chaque lien.

 	- Terme: (Facultatif) Cette variable est généralement utilisée par les plates-formes de recherche et permet de placer les informations sur les termes pour lesquels vous enchérissez. Dans Google, il peut s’agir du terme de recherche spécifique ou des mots-clés qu’un responsable utiliserait pour trouver votre campagne Adwords. Vous pouvez également l'utiliser pour identifier le public que vous avez utilisé pour une publicité sur Facebook.

### ***Outils de création d’url  UTM ***

Il faut avoir son url de destination et suivre ensuite le formulaire de création. Le classique de Google ici : [https://ga-dev-tools.appspot.com/campaign-url-builder/](https://ga-dev-tools.appspot.com/campaign-url-builder/) .C’est un outil adhoc il ne garde pas les urls, donc le mieux est de sauvegarder les urls pour les retrouver par la suite.

Exemple d’Url tagguée :

[www.monsiteweb.fr?utm_source=Facebook.com&utm_medium=social&utm_campaign=FbPrintemps19&utm_content=bannierevidéo](http://www.monsiteweb.fr?utm_source=Facebook.com&utm_medium=social&utm_campaign=FbPrintemps19&utm_content=bannierevidéo)

Ou alors un simple tableur peut suffire comme celui-ci , que j’ai récupéré quelque part et Franchisé pour l’occasion : [https://docs.google.com/spreadsheets/d/1BMJ6B-NG8e03GSgGBHtpV7UoQR3SeqFGs79ZRwsjswQ/edit?usp=sharing](https://docs.google.com/spreadsheets/d/1BMJ6B-NG8e03GSgGBHtpV7UoQR3SeqFGs79ZRwsjswQ/edit?usp=sharing)

[![outil-utm-gratuit.gif](/images/blog/outil-utm-gratuit.gif) outil utm gratuit

Bon à savoir : Quand à la syntaxe , il est classique de séparer l’url des variables « utm » par un « ? » mais cela fonctionne aussi avec un « # » qui serait mieux d’un point de vue « seo » afin parfois d’éviter des scénarios de duplicate content. Mais bon, c’est déjà ici un niveau avancé dans la conception pour moi ! Mieux vaut, selon les urls présentes sur le site, faire appel à un expert qui maitrisera le sujet.

## **Faire un suivi personnalisé simple avec  Utm et paramètres perso. pour une campagne de pub.**

Le cas d’usage peut être la transmission toute simple d’une identification d’un produit, service, transmis dans l’url entrante et ensuite traitée par le site web via un script.

Les paramètres d'URL permettent de transférer donc  des données sur un clic via l'URL. Ces paramètres d'URL comprennent  une clé et une valeur, séparées par le signe "=". Vous pouvez ajouter  plusieurs paramètres avec une liaison à l’aide d’une esperluette (&).  Le point d'interrogation séparant l’url du 1er paramètre suivi d’UTM, les 2 valeurs sont compatibles. Exemple : http://example.com?product=1234&utm_source=google

Il existe deux types de paramètres d'URL que vous pouvez utiliser dans le modèle de suivi ou dans les paramètres personnalisés d’une  annonce :

 	- Les paramètres modifiant le contenu transmettent des informations à la page de destination. Ils doivent obligatoirement et exclusivement être définis dans l'URL finale. Par exemple, l'URL http://example.com?productid=1234 permet de rediriger l'utilisateur vers la page de votre site Web relative au produit 1234.

 	- Les paramètres de suivi transmettent des informations au sujet du clic pour votre compte, votre campagne ou votre groupe d'annonces au sein du modèle de suivi. Il existe deux types de paramètres de suivi :

 	- Les paramètres personnalisés correspondent à une valeur définie par l'annonceur dans le modèle de suivi. Par exemple, vous pouvez définir {_campaign}=branding ou {_campaign}=leads dans les paramètres personnalisés de votre campagne, et régler le modèle de suivi de votre compte sur {lpurl}?source_campaign={_campaign}. En savoir plus

## **Suivi avancé  depuis Google Ads à l’aide de Gclid et Utm**

le suivi automatisé Classique  proposé par le système

[![gclid-vs-utm.jpg](/images/blog/gclid-vs-utm.jpg)

 	- Le marquage automatique associe un paramètre GCLID (ID de clic Google) à l'URL sur laquelle cliquent vos clients. Cela vous permet de savoir quelle annonce a reçu un clic pour chaque visite effectuée sur votre site Web.

 	- Google Analytics et des programmes similaires peuvent utiliser les informations des URL marquées automatiquement pour indiquer le mot clé Google Ads ayant généré une visite sur votre site, la campagne dont il provient et le coût du clic correspondant.

 	- Ces informations peuvent vous aider à importer des [conversions](https://www.mauricelargeron.com/formation-google-ads/google-ads-et-le-suivi-avance-des-conversions/) complexes dans Google Ads, en ligne ou hors connexion.

A noter que ce paramétrage est aussi compatible avec un marquage manuel pour Google analytics. Cela permet d’avoir à la fois les données détaillés depuis Acquisition > Google ads dans GA mais aussi d’avoir des données plus « propriétaires » de suivi dans Acquisition > campagnes

[![glcid-et-utm-dans-google-analytics.jpg](/images/blog/glcid-et-utm-dans-google-analytics.jpg) glcid et utm dans google analytics
## **Suivi avancé  depuis Google Ads à l’aide de Gclid et Value Track**

Un Template de suivi personnalisé, avec Value Track, permet de transférer des données de clics d’une annonce pour un système de suivi tiers comme un CRM par exemple. Les 2 systèmes de suivi sont donc compatibles. Le CRM peut recueillir ensuite ce genre de statistiques comme le suivi gclid, le mot clé, le cpc, la date, le coût d’acquisition total.

[![crm-et-gclid.jpg](/images/blog/crm-et-gclid.jpg) crm et suivi gclid

Les paramètres ValueTrack sont un type de paramètre d'URL. Chaque paramètre d'URL est constitué d'un texte entre accolades ({}), comme : {matchtype}. Vous pouvez insérer ces paramètres dans l'URL finale, le modèle de suivi ou le paramètre personnalisé de votre annonce.

Lorsqu'un utilisateur clique sur votre annonce, le système AdWords remplace le paramètre ValueTrack par une valeur calculée à partir des informations associées à l'annonce au moment de l'enregistrement du clic. Par exemple, le paramètre {matchtype} sert à spécifier le type de correspondance du mot clé ayant déclenché la diffusion de l'annonce. Lorsque vous examinez vos données, au lieu de voir {matchtype}, c'est la valeur enregistrée par ValueTrack qui s'affiche : b pour une requête large, p pour une expression exacte ou e pour un mot clé exact. Si aucune valeur ne peut être insérée, le paramètre ValueTrack est remplacé par un espace vide.

Img gif

Plus d’infos ici : [https://support.google.com/google-ads/answer/6305529](https://support.google.com/google-ads/answer/6305529)

## **Suivi avancé  d’une campagne Google ads pour une solution tierce d’attribution marketing**

Admettons ici qu’en plus d’un suivi Gclid et Utm, nous souhaitons aussi transférer des données de clics et de conversions à une solution tierce d’analyse d’attribution de sources de trafic. Prenons ici celle de Facebook. Il faudra donc partir du mode de tracking de Fbook récupérer les éléments et les inclure dans un modèle de suivi, ici que nous placerons au niveau du compte de toutes les sources d’acquisition comme Bing, Google, etc..

[![google-adwords-parallel-tracking.gif](/images/blog/google-adwords-parallel-tracking.gif)

Fbook attrib img

Img config

Faire un test selon toutes les situations, et afin de ne pas trop alourdi le temps entre le clic et l’arrivée sur le site, un traitement en parallèle des redirections.

[![test-des-urls-de-redirection.jpg](/images/blog/test-des-urls-de-redirection.jpg) Test des urls de redirection

Cela peut donner ensuite des rapports comme ceci

[![attibution-fbook.png](/images/blog/attibution-fbook.png) attribution fbook
## Et le suivi dans un écosystème d’application mobile  (Vs web/user centric) ?

C’est un sujet super intéressant que je propose d’aborder lors d’un prochain article !
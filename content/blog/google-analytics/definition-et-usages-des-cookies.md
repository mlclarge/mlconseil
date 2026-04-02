---
title: "Anatomie d'un cookie pour l'analyse web"
date: 2013-08-22
author: "admin"
categories: ["Google Analytics"]
tags: []
slug: "definition-et-usages-des-cookies"
---

De fils en aiguilles, filons ;)  cette semaine  sans plus tarder sur la thématique de l’**analyse web avec** **le sujet des cookies**. La semaine dernière, nous avons discuté de l’alternative au marqueur JavaScript de Google analytics où le cookie prend toute sa place.  Après tout, l’essentiel des données collectées par les éditeurs de site part  de ce petit fichier texte !  Des parades existent pour les navigateurs qui interdisent le JavaScript et l’installation de ces « témoins de connexion » comme les requêtes urls, Ip tracking, champs de formulaires, mais bon, ils restent encore bien utiles pour tous les usages de tracking. Explorons les sous 3 angles : leur création et usages, leur anatomie au travers du marqueur google analytics et leur carrière marketing.

## **Naissance, raison d’être et typologie des cookies**

### Historique

Il faut remonter à 1994 pour voir l’utilisation de ces petits fichiers texte dans le monde de l’internet. Ils étaient déjà utilisés dans le milieu informatique.

**Le cookie ** tire son utilité dans le fait qu’il apporte une « mémoire » tant au navigateur qu’au serveur web lorsqu’ils discutent entre eux. Ils sont créés à partir de langages de scripts comme JavaScript, PHP, ou autres et sont insérés dans la ou les pages du site. Ils comportent généralement 4 parties : une paire nom/valeur ; une date d’expiration ; un domaine / arborescence , un chemin auxquels ils sont liés.

Leurs fonctions sont principalement de 3 ordres

	- Conserver les **données de session** : pour les sites marchands par exemple pour la conservation des produits dans le panier, pour l’enregistrement de statistiques de visites par exemple avec Google analytics.

	- Garder des **informations pérennes** : comme l’identifiant d’un visiteur pour éviter de le retaper à chaque visite. Ces cookies peuvent être lus depuis le navigateur Chrome (suivre ce chemin : outils, paramètres, paramètres avancés, confidentialité, cookies, ouf !).

[![lecture-cookie-310x177.gif](/images/blog/lecture-cookie-310x177.gif) Lecture d'un cookie depuis son navigateur Chrome

	- Collecter des **informations pour des tiers** : c’est le cas des cookies posés par des régies publicitaires afin de déterminer certains comportements de visiteurs.

### Gamme des cookies

	- First partie : autrement de 1ere partie, ce sont ceux édités par le domaine sur lequel le serveur vous renvoie la page web.

	- Tierce partie : ceux qui sont posés par des domaines qui ne sont pas liés au domaine visité.

## **La Vie  des cookies, focus sur le marqueur GA**

### **Cas Google analytics, des cookies de confiance ?**

Les cookies de Google analytics sont de première partie, cela déjà enlève une épine du pied du domaine qui le dépose, car il est possible de paramétrer son navigateur de n’utiliser que des cookies de première partie, considérés comme moins intrusif.

Google A. Classique et les cookies natifs

Cinq types de cookies sont utilisés dont 4 vraiment sont en vigueur, nom du cookie, durée, et description sont utiles pour permettre de mieux comprendre les remontées dans Google analytics, voici le document du site google pour les developpeurs traduit de l'anglais , of course.

[![cookies-ga-310x138.jpg](/images/blog/cookies-ga-310x138.jpg) Cookies du marqueur G. Analytics

On s’aperçoit donc que le cookie né, vit et meurt et tout cela en silence ! :(

Vous remarquerez que le **cookie _utmz** **est le cookie du marketeur **! C’est lui en effet qui renferme les différentes variables utm de campagnes accolées au tag des annonces et bannières publicitaires, mailing  pour en assurer le suivi. Cette chaîne de caractères contient la Source, le nom de la campagne, son support, le terme (mot clé), son contenu, bref, tout y passe.

Nouveauté dans Google Universel

Le **tracking de session** ne se passe plus côté client mais coté serveur, ce qui explique les fonctionnalités sur le paramétrage de la gestion de la durée de session, de l’ajout de moteurs supplémentaires, de la reclassification sur la nature de sites référents. Donc, 1 seul cookie par défaut dans le navigateur ! On passe de ga.js qui orchestre le tracking classique à analytics.js qui change la donne.

Plus d’infos précises ici : [https://developers.google.com/analytics/devguides/collection/analyticsjs/domains](https://developers.google.com/analytics/devguides/collection/analyticsjs/domains)

### **Voyage de  ces  témoins de connexion avec le vaisseau _utm.gif !**

**L’utm.gif** appelé à chaque chargement de la page web par l’internaute, emporte avec lui depuis le navigateur, un ensemble de données dont ces cookies mais pas seulement eux ! Comment repérer ce départ vers la planète Google analytics ? On peut utiliser **son navigateur (voir illustration ci dessus avec chrome) **, ou une **extension dédiée** comme **ga debug** ou alors une application comme **fiddler** qui intercepte ce qui se trame entre les serveurs et le navigateur. L’_utm.gif (historique voulant dire Urchin Tracking Monitor) transporte les  trames de transaction (ip), les requêtes http  (nom d’hôte, référent, langue utilisée), des éléments du navigateur (résolution écran..) mais aussi les données des cookies de 1ere et de tierce partie (régie pub doubleclick).

[![requete-utm-293x300.gif](/images/blog/requete-utm-293x300.gif) Lecture de la requete -utm.gif , collecteur de données pour GA à l'aide de Fiddler
## **Cookies et Web Marketing il n'y a qu'un pas !**

Dans le modèle classique, il est possible de récupérer les valeurs des cookies pour les intégrer dans des champs cachés d’un formulaire de souscription par exemple. Cette collecte alimentera une application de gestion de clientèle (crm).  Le faire au niveau client (browser) est plus intéressant en terme de traçabilité du visiteur que de les extraire depuis GA. Utiliser l’**API de GA** est donc possible mais déjà trop tard vu que les données sont rendues anonymes. Enfin, un  développeur chevronné sera sans doute capable de placer un identifiant unique afin d’étoffer un CRM des données de GA ;) .

### Fini l’utm_gif  ? Oui un peu..

Dans le nouveau suivi de Google analytics (universel) , l’intérêt est l’apparition du protocole de mesure l’objectif est  de suivre non plus un navigateur, mais **différents appareils tous reliés sur le même protocole**.  Un "objet tracker"  dénommé "**collect**" remplace l'UTM gif. Il est nécessaire d’envoyer ces données directement sur les serveurs GA,  pour cela 3 types de valeurs sont requises :  le tid (compte ga), le cid (client id anonyme), le t (type de hit : pages vues, event, transaction, timing) .

[![analyse-cookie-universal-287x300.gif](/images/blog/analyse-cookie-universal-287x300.gif) Valeurs et cookie du nouveau traqueur GA Universel

Ici on récupère le client ID lors d’un formulaire (lead) et l’on envoie cela dans un **CRM** (même principe).  Il reste néanmoins la présence des cookies GA classique.  Le monde du online et du offline (magasin) peuvent enfin se rejoindre. Donc le **principe de la collecte  à base de cookies** existe toujours mais les objectifs sont plus ambitieux, plus large, plus ubiquitaire.

L’implémentation de l’User ID (à)   permettra de réaliser un rapport **User centric** en ayant une vue sur les usages d’un seul visiteur au travers de son cheminement sur plusieurs devices.

[![protocol-de-mesure-310x110.gif](/images/blog/protocol-de-mesure-310x110.gif) Un nouveau mode de tracking UA :cookies/protocole

Bon, finalement, ces cookies nous amènent à prévoir de nouveaux développements techniques afin de déployer ces nouveaux marqueurs pour le plus grand plaisir du service marketing !

Finalement, les cookies, vous les préférez  comment ?

##  Webographie 

	- Histoire du cookie : http://fr.wikipedia.org/wiki/Cookie_(informatique)

	- Principe codage (ga et universal) : https://developers.google.com/analytics/devguides/collection/analyticsjs/cookie-usage

	- Customisation du nouveau cookie universal : https://developers.google.com/analytics/devguides/collection/analyticsjs/domains#getClientId

	- Page / Test d'exercice : [http://www.enhanceie.com/test/cookie/](http://www.enhanceie.com/test/cookie/) & [http://www.w3schools.com/js/js_cookies.asp](http://www.w3schools.com/js/js_cookies.asp)
---
title: "Alternative au code d'implémentation GATC classique "
date: 2013-08-14
author: "admin"
categories: ["Google Analytics"]
tags: []
slug: "tracking-sans-cookies-ni-javascript"
---

Le sujet de  la semaine dernière sur l’IP tracking finalement m’inspire  celui de cette semaine.  A l’heure ou l’on parle de modifier à nouveau la législation européenne sur la façon dont on recueille les données visiteurs sur un site web (selon l’usage des cookies et leur degré d’intrusion *(connexion, transactionnel, publicitaire, statistiques…)* , un consentement de la part de l’internaute  doit être clairement mentionné sur le site et validé par son visiteur, [infos](http://www.ico.org.uk/for_organisations/privacy_and_electronic_communications/the_guide/cookies), les cordonniers ne sont pas les mieux chaussés d’ailleurs ici :( . Quoi penser du devenir de la méthode de collecte via le marqueur JavaScript de Google analytics *(à l’aide de cookies)* ? **Existe-t-il une alternative **? Je vais essayer de répondre à cette question ! Voyons donc le système actuel de GA, les raisons d’en changer et passons en revue quelques méthodes alternatives.

## **Principes de fonctionnement du suivi Google analytics **

Je tire cette information entre autre  de la documentation officielle de Google analytics pour les développeurs. Les sources d’informations proviennent :

	- Des **entêtes http** du visiteur

	- Du **navigateur** de l’internaute

	- Des **cookies** propriétaire de GA

### *JavaScript et  cookies *

[![principes-collecte-cookie-ga-1-310x159.jpg](/images/blog/principes-collecte-cookie-ga-1-310x159.jpg) Processus de collecte Javascript Classique GA

Ces petits fichiers texte qui contiennent les données visiteurs, sont créés par l’appel de la page web **(1)** qui contient le GATC (script JavaScript (js) ) qui va déclencher des appels sur les serveurs de Google** (2)** analytics.  Un mécanisme de collecte **(3) ** va ensuite être pérennisé au fur et à mesure des visites grâce à  l’appel du GIF-image posé par le GATC (mise à jour des cookies).  Une fois sur les serveurs de GA un processus de parsing (tri)  sera effectué **(6 à 9)** sur le fichiers journaux des serveurs google , une mise en base de données effectuée **(10)** et enfin, une présentation via navigateur des données aggrégées et échantillonnées selon les volumes traités.

## **Pourquoi envisager une autre méthode de tracking ?**

J’ai pu recenser 5 raisons principales pour penser un autre suivi GATC (Google analytics tracking code)

	- Lutter contre la **politique de confidentialité** sur les cookies incertaine (évoquée dans l’introduction)

	- Parer à la **désactivation de la fonctionnalité** JavaScript de la part du visiteur

	- Assurer une **continuité dans le suivi** des données *(suite effacement du cache navigateur)*

	- **Tracer des documents** (pdf, excel, images)  qui sortent du champ classique de la visite *(accès directe fichier, provenance d’un lien sur serveur messagerie par ex.) *et où GA n’a pas la main.

	- **Extraire et envoyer** d’autres  données  d’une manière confidentielle *(pas dans le code source)*

## **Une méthode sans cookies ou presque !**

### *Principe et usage du modèle Client / serveur *

[![principes-environnement-php-ga-310x131.jpg](/images/blog/principes-environnement-php-ga-310x131.jpg) Contexte triangulaire du suivi côté serveur

Ce modèle classique d’architecture web peut être utilisé aussi pour collecter les données visiteurs sans pose de cookies  ni JavaScript. Donc, on quitte un code qui s’exécute sur le poste de l’internaute dans son navigateur, pour une syntaxe qui s’opère sur le **serveur web du site.**  Par quel moyen démarrer ? Il suffit d’utiliser une des 2 classes php SSGA ou PHP-GA  exitantes (le travail a déjà été effectué ou presque donc)  qui vont  s’interfacer avec les serveurs de Google analytics.  A noter que celle qu’il est préférable d’employer est PHP-GA (entretenue et mise à jour).  Pour certains objets à tracer, ce moyen client-serveur peut avoir recourt aussi aux cookies.

### *Ingrédients  pour que cela fonctionne *

	- Avoir un fichier serveur apache

	- Installer la librairie **php-ga** sur le serveur web.

	- Installer sur les pages suivies les  méthodes php  selon les objectifs analytics poursuivis (tracking de pages, évènements etc..) qui font appel à php-ga

	- Customiser éventuellement selon ses besoins un fichier .htaccess pour les directives assignées au serveur

### *Cas d’usages *

	- Suivi de pages

[![example-code-10-310x205.jpg](/images/blog/example-code-10-310x205.jpg) Extrait code de base Source Google

	- Evènements

	- Ecommerce

	- Visiteurs

	- Valeur personnalisées (mais avec cookies)

	- Suivi de Mobile (qui n’exécute pas le Js avec une librairie dédiée voir ici)

### *Les inconvénients pour sa mise en œuvre*

Toute médaille a son revers . Les principaux désavantages sont :

	- le temps de codage (ici php mais peuvent se faire dans d’autres langages web de script)

	- la librairie telle décrite ici ne prend pas en compte les visites récurrentes

	- Selon ces objectifs, l’usage des cookies restent incontournables

	- Solution qui donne moins de fonctionnalités donc moins complète que celle des cookies (pas de géolocalisation par exemple)

	- Fiabilité en terme de qualité de service par rapport aux services Google ?

	- Enregistrement des sessions moins fiable que GATC

### *Autres moyens possibles plus rudimentaires mais sans cookies, client / serveur*

**Solution serveur tiers**

**Principe : **sur la page web, suivie qui lance  un appel http sur un serveur tiers qui héberge une librairie dédié à GA, qui va stocké et envoyé ensuite les données sur les serveurs GA. Plus d’infos ici [http://nojsstats.blogspot.fr/](http://nojsstats.blogspot.fr/)

Solution pour serveurs ms ou apache (asp.net et php)

**Méthode** : Dénommé CFA (cookie free analytics), cette solution n’apporte pas non plus ce que donne le « vrai GATC » mais peut être une parade dans des situations contraintes. Elle utilise 2 façons pour traquer les données. D’une manière visible avec le principe précédent d’un appel d’image via html, et d’une manière invisible grâce à l’installation d’un module http dédié, pas de Js ni d’image ici. Lien : [http://www.cookiefreeanalytics.co.uk/](http://www.cookiefreeanalytics.co.uk/)

Voilà donc des alternatives à la pose du GATC classique, qui peuvent constituer une parade si un jour la loi européenne venait à imposer des restrictions. A suivre…

Webographie :

	- Code source php-GA : https://code.google.com/p/php-ga/

	- Cas pratique tracking Pdf par php : http://www.lunametrics.com/blog/2013/06/04/tracking-pdfs-google-analytics-server-side

	- Suivi par Jquery une librairie js alternative : http://www.shamasis.net/projects/ga/
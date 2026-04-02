---
title: "Optimisations de son hébergement  et de son site"
date: 2011-12-15
author: "admin"
categories: ["Référencement naturel"]
tags: []
slug: "ameliorer-les-performances-techniques-de-son-site"
---

L'objet de ce billet ici tentera de répondre à une question récurrente :  "Comment faire pour que mon site soit facilement lu par Google ?". Une partie de la réponse revient aux **performances techniques de l'hébergement** d'une part, d'autre part,  du **codage intrinsèque du site** web .

Je reviens donc ici sur les performances techniques d'un hébergement et d'un serveur web. Une fois n'est pas coutume, alors ce matin, je ne vais pas réinventer la roue !  J'ai gardé dans mes archives 2 présentations slideshare dont 1 effectuée  par la société **Résonéo lors du SeoCampus 2010** et l'autre par la société **CleverAge** lors d'une conférence lors des Microsoft TechDays 2011. Ces 2 présentations se complètent bien.

Je voudrais rajouter néanmoins ces quelques lignes  inspirées par l'article du [blog de Google du 6 décembre dernie](http://googlewebmastercentral.blogspot.com/2011/12/tips-for-hosting-providers-and.html)r. En effet, le moteur de recherche met l'accent les points essentiels à observer et notamment :

## Serveurs de Nom et Hébergement

- **Blocage du robot de Google** : Protection de l'hébergement (pare-feu/Protection Dos) ou du Cms en lui-même qui empêche le robot de bien visiter le site. Pour y remédier Google offre des outils (Webmaster tool) et une aide en ligne à ce sujet  ([http://support.google.com/webmasters/bin/answer.py?hl=fr&hlrm=en&answer=158587](http://support.google.com/webmasters/bin/answer.py?hl=fr&hlrm=en&answer=158587))

-**Indisponibilité du site** (problème de DNS, serveurs saturés..).Aide:[http://support.google.com/webmasters/bin/answer.py?hl=fr&hlrm=en&answer=35120](http://support.google.com/webmasters/bin/answer.py?hl=fr&hlrm=en&answer=35120)

- **Certificat SSL** : Ces certificats qui authentifient un site web (domaines et sous domaines) sont parfois obsolètes et ainsi génèrent des conflits de navigation avec l'internaute.

- **Couverture DNS** : les sites internet peuvent être configurés pour répondre aux requêtes effectuées non seulement sur le domaine principal monsite.com mais aussi sur d'autres sous domaines lui appartenant exemple.monsite.com; Afin d'éviter le contenu dupliqué, craint par les webmasters (même contenu disponible sous divers noms de domaines) il est possible de configurer le serveur web afin de générer soit une page d'erreur 404, soit un refus de connexion.

- **Contenu dupliqué dû à des urls spécifiques** : il est possible parfois d'accéder à son serveur via des urls spécifiques offerte par son hébergeur comme  http://ovh.com/~monsite.com/, les recommandations sont de ne pas avoir ces urls accessibles (avec mots de passe par exemple).

- **Pages d'erreur "soft"** : Certains hébergeurs répondent par des erreurs http 2000 au lieu d'erreur 404. Cela peut affecter le positionnement de certaines pages. Ce problème est expliquez ici : [http://support.google.com/webmasters/bin/answer.py?hl=fr&topic=20985&hlrm=en&answer=1716747](http://support.google.com/webmasters/bin/answer.py?hl=fr&topic=20985&hlrm=en&answer=1716747)

- **Contenu modifié et jeux de cadres** : Des hébergeurs selon le type d'hébergement choisi, peuvent injecter des scripts ou des images, ou des modules d'optimisation de code (comme mod_pagespeed d'apache), c'est tant mieux

- **Spam et Malware** : Google tente depuis septembre 2010 d'avertir certains hébergeurs qui accueillent d'innombrables sites web dont certains s'avèrent nuisibles.

## Audit technique et performance d'un site 

Mais revenons sur l'aspect spécifique de l'optimisation technique du code d'un site web. Ce diaporama  met l'accent sur** l'optimisation du code html** : Balises Méta, code html, optimisation temps de chargements, scripts utilisés.

Ce second diaporama, met l'accent sur l'audit des performances en utilisant des **outils (plugins/extensions) embarqués sur les navigateurs comme firebug** pour FFox et Yslow, et souligne  aussi l'existence d’outils disponibles en ligne. On rejoint dans ces slides, les propos évoqués dans le premier chapitre de cet article.
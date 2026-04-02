---
title: "L' Api Adwords pour apprenti développeur (part. 1)"
date: 2014-11-17
author: "admin"
categories: ["Apprendre Google Ads"]
tags: []
slug: "a-quoi-sert-l-api-google-adwords"
---

Explorons cette semaine une des fonctionnalités  techniques de la **plateforme publicitaire de google adwords,** son **API**. Ne partez pas de suite, le post de la semaine sera toujours dans la ligne éditoriale du blog, vulgarisatrice , de toute façon, je ne peux pas faire mieux  !  Cette **Application Programming Interface** (API) permet de dialoguer avec les différentes entités  que composent la [plateforme Adwords](https://www.mauricelargeron.com/utiliser-simplement-le-code-js/) : création de comptes, de campagnes, routines de gestion, reporting afin d’intégrer des données dans une application entreprise ou de créer des applications pour des utilisateurs finaux.  Que faut-il comme outils pour démarrer et se familiariser avec l’API sans prendre de risque ?  Je fais le choix ici donc de  présenter l’installation d’un environnement de type « SandBox » dans lequel l’apprenti développeur va pouvoir évoluer dans ce  mode « test » sans toucher aux campagnes en production.

## **Construction d’un environnement de travail SandBox pour Adwords**

### ***A quoi cela sert l 'api ? Cas d’usages ***

Plantons le décor. Le gestionnaire de campagne en agence, manager d' un centre multicompte  souhaite créer un **outil de reporting simple de campagnes adwords  qui sera disponible dans le cloud**   à destination de ses clients  annonceurs. En effet, adwords étant une interface trop touffue, un accès direct à quelques  tableaux de bord stratégiques   et opérationnels suffiront à l’annonceur pour suivre d’un œil le travail de l’agence.  Le développeur débutant va devoir se coller à la tâche et pour se faire la main sur l’Api, dans un contexte sandBox qui va être créé pour l’occasion.

Autre cas d’utilisation de l’Api adwords  illustré ci-dessous, le service cloud que propose la plateforme Optimizr et qui facilite la gestion et l’optimisation de campagnes.

[*](https://www.mauricelargeron.com/wp-content/uploads/2014/11/exemple-application-optimizr.jpg) Exemple d'outil développé depuis l'api adwords
### **Environnement de Test Adwords (côté serveur adwords)***

Le process général de mise en place de l’environnement du développeur*.*

[![Mcc-test-adwords-310x260.jpg](/images/blog/Mcc-test-adwords-310x260.jpg) Mise en place "Mcc test " adwords

Pour avoir **accès  à l’api**, il faut demander une autorisation d’accès via un centre multicompte existant.  La fonctionnalité est disponible depuis les paramètres du compte en haut à droite dans l’interface. Dans le cadre d’une utilisation de l’api en mode « test », une clé temporaire fonctionnera,  sans attendre l’approbation de Google  et l’acceptation des conditions d’utilisation et de facturation, exigée dans le cadre d’un usage en mode  production (réel).


Il faut ensuite créer un centre multicompte de « test » dédié à fournir de la data aux tests de développement. Il suffira ensuite de copier-coller des comptes de campagnes existant depuis adwords éditor par exemple et de les importer dans le centre multicompte test.


Voilà notre environnement de adwords « bac à sable » est terminé.

## **Environnement développeur Adwords (côté client)**

### ***Processus global ***

Pour communiquer avec cette plateforme MCC serveur,  il va falloir créer en local (mais pourrait être aussi fait depuis un serveur externe) un contexte « client » qui va dialoguer à l’aide d’un langage web, choisi par le développeur selon ses affinités avec tel ou tel type de syntaxe  (python, php, .net ..)et  basée sur une librairie consacrée pour adwords (api) . Cette dernière sera téléchargée et interfacée sur une plateforme de développement liée au langage de programmation installé sur l’ordinateur du développeur (ici pour illustration c’est du php, plus abordable dès le départ).

[![environnement-developpement-310x132.jpg](/images/blog/environnement-developpement-310x132.jpg) Environnement de développement

Les tâches du développeur seront principalement :

 	- De configurer son environnement de  développement

 	- D’installer les  librairies et autres packages nécessaires à la construction de l’application

 	- De maitriser la librairie choisie bien sûr

 	- D’avoir une connaissance métier de l’application adwords et de traduire en fonctionnalités les problématiques d’un gestionnaire de campagne. Rappelons que l’intérêt de l’api réside dans le traitement de masse importante de données et de manière dynamique si besoin (par exemple pour l’ecommerce activation ou non d’annonces selon disponibilité du stock)  : création de comptes, des paramètres de  campagne (enchères, budget ..), des annonces (texte dynamique),  production automatisée de rapports, optimisation…

### ***Mise en œuvre des outils de développement***

Le plus simple, sera d’utiliser un serveur Xampp et de passer par la console cmd.exe pour utiliser pour démarrer la libraire google adwords api. Donc à télécharger :

 	- Xampp (en local pour initier du php)

 	- Télécharger la** librairie dédiée php** pour adwords dans le dossier de Xampp : httpDocs

 	- Paramétrer le fichier auth.ini avec les « crédentials » du Mcc test (client Id, secret)  mais avec l’api key du serveur de production.

 	- Les accès à l’api sont gratuits avec un premier pallier à 10 000 hits/jours

[![fichierConfig-310x147.jpg](/images/blog/fichierConfig-310x147.jpg) Paramétrer les fichiers config.                                                            pour communiquer avec le MCC test

Lancer les script php dans la console : cmd.exe  *(paramétrer les variables système  dans windows voir liens fin d'article)* puis la commande php  + nom du fichier.php que l’on souhaite (ici dans l’illustration, récupérer les mots clés de la campagne). Ici, les fichiers php de la librairie contiennent des exemples d'utilisation, prêt à l'emploi , je prends ici le cas de l'un d'entre eux qui s'intitule "GetKeywords.php" qui va récupérer des mots clés d'une campagne (dans le but de faire un rapport par exemple à insérer dans un Crm).

[![commande-api-adwords-310x254.jpg](/images/blog/commande-api-adwords-310x254.jpg) Communication depuis via l'api avec le MCC

Bon, j’arrête là,  je ne saurais aller plus loin pour l’instant….je beugue sur validation d'Oauth. ...la suite donc dans un prochain article avec la [partie 2](https://www.mauricelargeron.com/les-bases-du-fonctionnement-de-l-api-adwords/)  !

## **Quelques ressources pour démarrer**

 	- Doc Adwords  : [https://support.google.com/adwords/answer/15235?hl=fr](https://support.google.com/adwords/answer/15235?hl=fr)

 	- Developpeurs : [https://developers.google.com/adwords/api/docs/guides/reporting](https://developers.google.com/adwords/api/docs/guides/reporting)

 	- Youtube : [3 tutos vidéos sur php ](https://www.youtube.com/watch?v=-VNhsA2Tv-A)

 	- Article utile détaillé : [http://www.sagerock.com/blog/setting-google-adwords-api-access-first-time/](http://www.sagerock.com/blog/setting-google-adwords-api-access-first-time/)

 	- APi Sea diverses : [http://www.ewanheming.com/adwords-api-offline-conversion-import](http://www.ewanheming.com/adwords-api-offline-conversion-import)
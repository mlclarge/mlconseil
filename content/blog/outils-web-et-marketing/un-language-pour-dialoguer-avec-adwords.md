---
title: "AWQL.me, un utilitaire Adwords à découvrir !"
date: 2014-05-17
author: "admin"
categories: ["Outils Web et Marketing"]
tags: []
slug: "un-language-pour-dialoguer-avec-adwords"
---

Un  petit outil aujourd’hui, à  l’honneur d’Adwords,  va être  passé en revue. C’est Bastien Rabaute, développeur et originaire de Toulouse,  qui a apporté à ma connaissance cette petite plateforme, disponible en ligne et gratuite.  Elle permet de dialoguer à distance, via un console reliée à l’**API d’Adwords**.  Pourquoi cet outil ? Quelle utilité ? Comment cela marche ? Et pour terminer quelques cas d’usages…

## **AWQL et origine de l’outil awql.me**

### AdWords Query Language Quésaquo  ?

C’est un langage semblable à SQL qui permet d’interroger la base de données Adwords, avec les traditionnels « questionneurs » sur les tables d’une base, voici un exemple type d'une requête :

SELECT     CampaignId, CampaignName
 WHERE      Ctr &gt; 0.05
 AND Impressions &lt; 100
 DURING     20120201,20120228
 ORDER BY   CampaignName DESC

Ce langage n’est pas nouveau, je n’ai pas réussi à retrouver sa date de naissance, mais cela fait déjà plusieurs années qu’il existe.

### Origine de awql.me

Bastien de Toulouse et son associé (basé à San Francisco) en développant des outils de reporting ont cherché ce genre d’utilitaire pour leur process.  Ne le trouvant pas,  et comme on est toujours mieux chaussé que par soi-même, ils l’ont donc développé et mise à disposition gratuitement.

## **A quoi sert-il vraiment ce AWQL ?**

### **Interroger Adwords et élaborer du reporting sur mesure**

Dixit ses concepteurs, awql.me permet :

	- d'écrire facilement des requêtes AWQL (une fois le compte adwords choisi),

	- une auto-complétion et une aide en ligne contextuelle,

	- de retourner les erreurs de syntaxe de la requête s'il y a un problème,

	- de renvoyer les résultats sous forme de tableau avec possibilité de recherche et de classement colonne par colonne,

	- d'exporter les résultats en CSV ou XML,

	- l’accès à une aide en ligne avec toutes les tables et les champs: [https://www.awql.me/adwords-awql-help/](https://t.yesware.com/tl/880cde7bec076c4a98ec4d04f3d712a7dc5bc0ae/8bffec61b63208f8b802f62152895fb1/d8abad2e19d16942b5660f6e4313b6b8?ytl=https%3A%2F%2Fwww.awql.me%2Fadwords-awql-help%2F)

### **Aide à mieux comprendre les données de la plateforme publicitaire..sans être développeur !**

Au-delà  de ces attributs techniques, et de son usage, le fait de fouiller dans les tables et les champs, permet d’avoir une approche différente par rapport aux indicateurs Adwords. C’est une autre façon ou manière de voir l’accès aux rapports que l’on peut élaborer.

L’accès à l’API Adwords est souvent réservé aux développeurs lorsqu'ils veulent construire des applications, des routines de gestion de campagnes, des rapports. Cela se fait  via un process complexe au départ comprenant : autorisation,  jeton (gestion des accès) , installation de librairie et autre client distant (python, php..)  pour réussir à dialoguer (**envoyer des requêtes**), cet outil raccourcit  la procédure en quelque sorte..et rend accessible au néophyte la base de donnée adwords.

## **Comment cela marche ?**

### **Permettre l’accès de son compte adwords  au service awql.me**

Création d’un compte en 2 clics et autorisation d’accès de la plateforme AWQL.me au compte Adwords via le compte Google.

### **Elaborer sa première requête**

Bien évidemment, la base de départ c’est déjà savoir ce que l’on cherche ! Pour exemple ici, j’ai fait une requête sur une petite campagne display, ciblée par thèmes dont je veux connaître le nombre de  clics et la moyenne du  cout par mille impressions (cpm).

L’aide sur la table « display par thème » supporte 50 champs dont ceux des « clics » et des « cpm moyen »

[![etape1-310x179.jpg](/images/blog/etape1-310x179.jpg) Table et champ"display" de la base Adwords

Je vais donc pouvoir m’en inspirer lors de la requête depuis la console de l’outil.

[![tutoriel-awql-304x300.jpg](/images/blog/tutoriel-awql-304x300.jpg) Console Awql.me et principe de requêtage
### **Rapprocher Adwords et AWQL.me**

Autre exemple où cette fois-ci, je souhaite avoir depuis la table « campaign performance report » accès au** numéro de campagne et à ses clics**, j’obtiens un tableau qui me donne sur 2 colonnes les items demandés.

[![parIddeCampagne-les-clicks-310x282.jpg](/images/blog/parIddeCampagne-les-clicks-310x282.jpg) Requête depuis la console

Je vérifie dans Adwords pour être sûr de mon coup.., je suis comme Saint Thomas, je veux être sûr que cet outil me restitue les vraies données source ..

[![dans-adwords-310x236.jpg](/images/blog/dans-adwords-310x236.jpg) Le même rapport dans Adwords

Un grand merci donc aux concepteurs et une longue vie à leur outil de reporting [Sunnyreports](https://www.sunnyreports.com/).

Source google pour Awql : https://developers.google.com/adwords/api/docs/guides/awql
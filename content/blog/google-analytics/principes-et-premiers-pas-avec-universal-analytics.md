---
title: "Principes et premiers paramétrages avec Universal analytics"
date: 2013-02-20
author: "admin"
categories: ["Google Analytics"]
tags: []
slug: "principes-et-premiers-pas-avec-universal-analytics"
---

Qu'apporte la nouvelle version **universelle de Google analytics** par rapport à la version actuelle ?  Je rappelle que cette version a pour but de collecter plus précisément les données des visiteurs avec un nouveau protocole multiplateformes / appareils. L’intérêt ici est bien donc, à terme, de faire du multi-devices, multicanal centré sur l’utilisateur et d’étudier la profitabilité des leviers marketing engagés dans l’obtention des conversions.

Trois parties traitées : les  **principes de base** de ce suivi d'audience,  l'**aspect  technique** pour son paramétrage,  et enfin quelques **vues de l'interface** . L'accès à cette version est disponible  via ce [formulaire](https://services.google.com/fb/forms/analyticspreview/). Je tiens à remercie [Matt Clarke pour son article](http://techpad.co.uk/content.php?sid=248) *(qui m'a aidé à rédiger ce billet) * ainsi que pour sa collaboration .

## **Principes de base de ce  nouveau protocole de suivi**

**Code** : analytics.js remplace ga.js et tous les anciens cookies par celui ci :  _ga

La **syntaxe** est entièrement nouvelle mais l’ensemble  des entités *(évènements etc..)* est conservé. La personnalisation des données et statistiques remplacent les anciennes variables personnalisées. Un **user-id** sera bientôt supporté.

Sur les pages produits, les **variables personnalisées** seront déclenchées sur les produits,  la marque, le fabricant, le fournisseur par exemple. Des **statistiques** comme  la marge, le bénéfice, en plus de celles sur les campagnes extérieures à adwords *(disponible d’ailleurs déjà dans la version actuelle de GA) * relatives aux coûts pourront y être incorporées.

Le but donc est d'envoyer ces données  à GA et de les rapprocher  des items de la conversion (transaction) afin d'avoir une** analyse plus fine** dans Google analytics du retour sur investissement (rsi).

## **JavaScript et PHP une solution technique hybrique pour un suivi personnalisé.**

Techniquement, 1 méthode  pour faire remonter les données. En effet, il peut sembler délicat d’envoyer des données commerciales lisibles dans le code source. Il est donc possible d’utiliser le **script coté client** (*analytics.js)* pour les données traditionnelles et d’employer un** langage côté serveur** *(PHP-ga)* par exemple pour pousser les données sensibles sur les serveurs de GA via la page de paiement.
A la source du tracking  :  **coté serveur**, un codage maison basé sur  une couche de données sera créé, en respectant [le protocole de référence](https://developers.google.com/analytics/devguides/collection/protocol/v1/devguide)  plus  l’adjonction du nouveau tag GA, **côte client**.

[![Image](https://www.mauricelargeron.com/wp-content/uploads/2013/02/analytics-js-310x232.gif)](https://www.mauricelargeron.com/wp-content/uploads/2013/02/analytics-js.gif) Code GATC Universal : analytics-js
## **Interface : informations de suivi dans l’interface  Google Analytics Universal**

**Six fonctionnalités** sont proposées en dur dans l'interface, cela évite donc l'ajout d'appels de méthodes js dans le GATC standard comme on peut le faire habituellement.

### **Durée de session**

30 minutes par défaut et 6 mois pour une campagne. Cela peut varier selon la problématique de l'entreprise.

[![Image](https://www.mauricelargeron.com/wp-content/uploads/2013/02/analytics-js-session-310x271.gif)](https://www.mauricelargeron.com/wp-content/uploads/2013/02/analytics-js-session.gif) Paramétrage des sessions
### **Paramétrage des sources de recherche naturelle**

Ex :qwant ! (le pauvre, encourageons le ! co co ri co !).Ici, on rajoute des moteurs de recherche non répertorié dans le listing par défaut de GA.

[![Image](https://www.mauricelargeron.com/wp-content/uploads/2013/02/filtre-moteurs-recherche-310x226.gif)](https://www.mauricelargeron.com/wp-content/uploads/2013/02/filtre-moteurs-recherche.gif) Ajout d'un moteur de recherche
### **Site référents **

L’objectif est d’exclure certains domaines pour qu'ils ne soient pas reconnus comme des sources de trafic en tant que sites. Sortit son propre domaine du trafic, c’est fortement recommander afin d’éviter que votre site soit vu comme une source lorsque des visiteurs de ce dernier cliquent sur un lien interne (lien vers un autre répertoire ou de retour vers le page d'accueil).

### **Exclusion des termes de recherche**

Pratique aussi pour tous les internautes qui tapent dans le moteur un nom qu'ils connaissent déjà, le nom de l'entreprise ou la marque. Ainsi, le trafic n'est plus considéré comme du direct.

[![Image](https://www.mauricelargeron.com/wp-content/uploads/2013/02/universal-interface-4-310x220.gif)](https://www.mauricelargeron.com/wp-content/uploads/2013/02/universal-interface-4.gif) Extraction de certaines requetes
### **Définitions personnalisées variables et statistiques, ces 2 Onglets supplémentaires font leur apparition.**

Comment cela marche ?

Il faudra d’abord  les  définir, puis les envoyer via une page vue ou un évènement du genre  : _ga('send'n'pageview'', {dimension1:'decatlhon modèle survet'});

[![Image](https://www.mauricelargeron.com/wp-content/uploads/2013/02/universal-variables-personnalisées-5-310x230.gif)](https://www.mauricelargeron.com/wp-content/uploads/2013/02/universal-variables-personnalisées-5.gif) universal-variables-personnalisées

Infos pour leurs paramétrages sur le [site des developpeurs google](https://developers.google.com/analytics/devguides/platform/features/customdimsmets#scope).

Le protocole de mesure et l'UA utilise un visiteur ID appelé l'iD client (cid) ne pas confondre avec l'user id qui n'existe pas encore. Pour utiliser le **protocole de mesure et L'UA ensemble**, il faudra utiliser les mêmes id client.  Autrement pas de connexion GA avec le visiteur.
Plus d'infos sur l'extraction de données du cookie ga Matt Clarke de la société Tchad en dit plus ici [https://plus.google.com/u/0/110147996971766876369/posts/Mz1ksPoBGHx](https://plus.google.com/u/0/110147996971766876369/posts/Mz1ksPoBGHx)
### **Rapports dans l'interface**

Il n'y a pour l'instant aucun changement particulier à noter  mise à part bien sûr  les nouvelles dimensions et statistiques personnalisées.

[![Image](https://www.mauricelargeron.com/wp-content/uploads/2013/02/ga-universal-rapport-310x300.gif)](https://www.mauricelargeron.com/wp-content/uploads/2013/02/ga-universal-rapport.gif) Rapport GA Universal  & variable perso : "Manufacturer"
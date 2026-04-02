---
title: "Le navigateur, cet outil Multitâche"
date: 2014-04-11
author: "admin"
categories: ["Outils Web et Marketing"]
tags: []
slug: "fonctionnalites-des-browsers"
---

**Le navigateur internet** est devenu tellement intuitif à l’usage du web, que l'on y prête quasiment plus attention. Pour les initiés (développeurs, analyste), il constitue un outil quotidien de travail, mais pour l’utilisateur lambda ou le** webmarketeur**, découvrir ses trésors cachés peut être un défi, vu la complexité de cette application. Essayons de passer en revue **les caractéristiques de cette utilitaire** indispensable à nos vies numériques. **Historique, fonctionnement et usages spécifiques** (sécurité, seo et pratiques insolites ! ) seront les principales parties de ce post. Je prendrai comme toile de fond, souvent le **navigateur Chrome**, car il faut bien en choisir 1 !

## **Histoire des navigateurs**

### **Historique des sésames du net**

Rien ne sert de refaire, ce qui est très bien fait, donc, je reprends le travail effectué par cette timeline depuis 1991 jusqu’à nos jours..avec notamment :

 	- 1991 : Naissance du protocole « http »

 	- 1992 : Html « 1 » !

 	- Mars 1993 : 1er navigateur Mosaïc

 	- Octobre 1994 : Nescape + Html 2

 	- Avril 1995 : Opéra + Apparition des cookies + Internet Explorer + SSL (norme de sécurité) et entrée de Javascript

 	- 1996 : Arrivée des Applets Java (petit programme embarqué sur Navigateur) + html 3

 	- 1997 : Flash arrive sur le marché (programme adapté pour animations, effets..)

 	-  1998 : html 4 + CSS 2 (language de style)

 	- 1999 : AJAX (méthodes côté client apportant de l’intéractivité)

 	- Juin 2003 : Naissance du Browser Safari

 	- Novembre 2004 : Entrée du renard …Firefox

 	- 2006 : xmlHttprequest2 (requête http ou https directement dans le script serveur)

 	- Depuis 2008 : Beaucoup d’améliorations dans les possibilités Html 5 (rendu dynamique), le CSS 3, Applications Web, API

[![timeline-310x100.jpg](/images/blog/timeline-310x100.jpg) Chronologie des navigateurs 1991 à nos jours

Cette **Timeline "live"** de la navigation web est visible ici :  [http://www.evolutionoftheweb.com/?hl=fr#/evolution/day](http://www.evolutionoftheweb.com/?hl=fr#/evolution/day)
### **Parts de Marché du surfing ...**

Le petit dernier se taille la part du lion, son secret ? Certainement sa rapidité avec son cousin moteur de recherche Google. Qui aurait pu penser qu’internet explorer continue sa chute ? Il est vrai que l’abus de position dominante de Microsoft , a su plomber sa domination.

## **Fonctionnement des navigateurs web**

### **Navigateur = principale interface graphique pour se connecter au web (via http)**

Le navigateur fait le lien entre la machine de l’internaute et celle du site web (serveur). C'est un "client" du protocole   "**http:// client-serveur". **D'autres protocoles peuvent passer par un navigateur comme le **FTP** (plus ancien), ou le **WEBDAV** (extension du http) ou **Gopher** *(via Firefox, mais confidentiel)*.** ** En fait, c’est en quelque sorte l’interprète entre le sreveur du site web et le visiteur ! Pour que le serveur du site et la page demandée puisse s’afficher, des **variables d’environnements**, puisées dans les **couches réseaux du modèle OSI**, doivent être déclarées et transmises et cela avant toute discussion (envoi d’images, pages etc..). Le Modèle réseau OSI (**7 couches**) représente les différentes strates de ce qui est nécessaire pour établir connexion et communication entre machines sur un réseau.

[![osi-et-html-310x156.jpg](/images/blog/osi-et-html-310x156.jpg) Le navigateur : application intégrée du modèle OSI
### **Les discussions entre un Browser et un Serveur web**

Diverses applications, conçues pour tracer les différents appels entre le navigateur et le serveur, permettent de mieux comprendre les allers et venues de l’information. Fidler fait partie d’un de ses outils bien utiles pour voir et mesurer les différents appels de part et d’autre :

 	- Statut  des appels : 200 (ok) - 404 (page  non trouvée) - 500 (erreur serveur)

 	- Scripts

 	- Cookies

 	- Images

 	- Code Html

 	- Img fidler

[![fiddler-debug-310x250.jpg](/images/blog/fiddler-debug-310x250.jpg) Les appels de fichiers intercepté par Fiddler

**Comment le navigateur traduit et affiche-t-il  le contenu envoyé par le serveur web ?**

Sans rentrer dans les détails techniques, je donne ici brièvement les grandes lignes dont est fait un navigateur. Je tire ces infos d’un document technique mais vulgarisateur en français sur developpez.com (voir lien fin d’article) basé sur les travaux de Tali Garsiel. 7 composants le constitue..

 	- L’interface utilisateur :  Barre d'adresse, les boutons avant et arrière

 	- Moteur du navigateur : Gère les actions entre l'interface et le moteur de rendu

 	- **Moteur de rendu : Analyse le code HTML et CSS**

 	- Réseaux : requêtes d’entêtes http

 	- Interpréteur Js : Exécute le code  Js !

 	- Backend : Console, Api interface qu’utilise le développeur ou l’analyste

 	- **Données stockées par le Browser : cookies** ..

[![composants-navigateurs-310x212.jpg](/images/blog/composants-navigateurs-310x212.jpg) Composants d'un navigateur
### **Focus sur le moteur de rendu : analyse Html**

Le moteur de rendu analyse les données du serveur via un process élaboré selon le type de language et de documents qu’il doit afficher pour l’utilisateur.  Principalement de l’Html, xml, images, css, doc pdf ou autres (animations flash etc..).

Voici schématisé ci-dessous ce que le** moteur webkit** (safari, chrome)  utilise comme  flux de traitement.

[![moteur-webkit-310x226.png](/images/blog/moteur-webkit-310x226.png) Etapes du traitement d'un document web

Un des aspects de ce processus est l’utilisation du Document Object Model, qui utilise **2 types d’analyses : lexicale** (vocabulaire, string)  et s**yntaxique** (règles du langage).

### **Rôle du DOM dans la restitution d’un document**

Le Dom est une API embarquée sur les navigateurs qui est utile aux langages  web de scripts (Js) afin de  manipuler dynamiquement les contenus html et xml plus communément appelé documents. Son architecture est structurée et orientée objet.  Le développeur peut ainsi faire appel à cette hiérarchie pour élaborer des pages web.

[![dom-et-analytics-310x190.jpg](/images/blog/dom-et-analytics-310x190.jpg) Hierarchie d'un document traité par un navigateur
## **Usages spécifiques  du navigateur**

### **Chrome et ses attributs**

 	- En tapant dans Chrome : **chrome://about/** une liste d’urls donne accès à des informations sur ce que renferme le navigateur, voici quelques fonctionnalités :

 	- chrome://bookmarks : Ouvre le gestionnaire de signets du navigateur

 	- chrome://cache : Affiche tous les éléments mis en cache , les sites Web , les images et les scripts

 	- chrome://credits : Technologies qui sont inclus dans le navigateur , de leurs licences , et qui les a créé

 	- chrome://extensions : Affiche les extensions installées

 	- chrome://flags :  affiche les fonctions expérimentales qui peuvent ou ne peuvent pas être intégrés dans le navigateur à un moment ou l'autre.

 	- chrome://inspect : Option pour inspecter des éléments , tels que des pages ou des extensions dans Chrome

 	- chrome://memory : Affiche les processus de navigateurs, et l’utilisation de la mémoire de tous les navigateurs web ouvert sur ​​l'ordinateur

[![dialoguer-avec-chrome-250x300.jpg](/images/blog/dialoguer-avec-chrome-250x300.jpg) Attributs de Chrome

**Bonus** : Si vous souhaitez manipuler votre **historique navigateur** avec doigté suivre un des liens en fin de page !
### **Chrome comme explorateur de votre OS**

Il suffit de taper :**file:///C://** et cela ouvre l’accès aux dossiers et autres fichiers du disque dur. Utile

[![navigateur-disque-dur-310x209.jpg](/images/blog/navigateur-disque-dur-310x209.jpg) Explorateur Chrome
### **Navigateur et Seo : Cloaking **

Exemple d'entête navigateur :

![Image](/images/blog/ebtetenav.jpg) en tete navigateur

Etant donné que les **variables d’en tête de session** véhiculent des données intéressantes comme les « user - agent » ou autre « l’adresse ip » de connexion, il suffira pour le serveur web, munit d’un script de détection de « qui l’interroge ? » , de lui** servir un contenu variable selon le demandeur**. Par exemple une page différente pour l’utilisateur, et une autre un moteur de recherche lambda ;)

### **Référencement : manipulation du référant**

Le navigateur d’une page à l’autre ou d’un domaine à l’autre, en cliquant sur un lien, enregistre la page de provenance. Là encore, le navigateur et ce champ « référent » peut être falsifié pour indiquer le domaine que l’on souhaite et récupérer ainsi le  bénéfice de la visite et en espérer d’éventuelles retombées.

### **Sécurité : attention aux failles !**

Le navigateur est une plateforme de prédilection pour accueillir des scripts malveillants venus de sites web non protégés, ou alors volontairement malicieux, ou bien d’extensions douteuses.

 	- **Cross-site Scripting** : Chaque fois qu’un serveur web accepte des données non fiables et les envoie à un navigateur, des scripts malveillants peuvent détourner des sessions utilisateurs, faire des redirections vers des sites malveillants.

 	- Exposition de données sensibles : Là encore, il est possible d’intercepter ce qui transite entre le navigateur et le serveur web, surtout lors de session transactionnelles (cartes de crédit, données d’authentification..) , passer par **un chiffrement** est indispensable (https + ssl) pour crypter les échanges entre Browser et serveur.

 	- Falsification de la requête : C’est l’**attaque CSRF** (cross site request forgery) , elle force le navigateur d’une victime connue à envoyer une requête http, avec cookie de session et autres informations utiles vers une application web. Le hacker force le navigateur à effectuer des requêtes sous le sceau de sa victime.

**Le navigateur, outil de travail du développeur et de l'analyste web**

En tapant Ctrl+Maj+J , on accède à la console à l’**api Javascript de Chrome** qui permet de discuter avec ce qui se passe sur la page (scripts, objets du DOM). Un exemple de commande Xpath (langage utilisé pour interroger des éléments, mais aussi pour scraper des données) : $x(« //p « ) qui permet de rechercher dans les différents paragraphes, la présence de lien muni d’ une balise « a ». Lors de débuggage sur des marqueurs Js pour google analytics, les fonctionnalités sont aussi utilisées.

[![console_js-api-310x162.jpg](/images/blog/console_js-api-310x162.jpg) Console Js pour dialoguer avec la page
## **Liens sur le sujet des navigateurs web**

 	- Document technique sur l'analyse et l'interprétation des N.: [developpez.com](http://web.developpez.com/tutoriels/web/how-browsers-work/)

 	- Site sur les traces numériques : [http://assiste.com.free.fr/p/qui_etes_vous/qui_etes_vous_vos_traces.php](http://assiste.com.free.fr/p/qui_etes_vous/qui_etes_vous_vos_traces.php)

 	- Outils : [analyse entre serveur et browser](http://www.telerik.com/fiddler) + [manipulation d'users agent](http://www.wannabrowser.com/)

 	- Article intéressant sur une[ expérience de Cloaking](http://blog.unmaskparasites.com/2013/03/11/cloaking-think-outside-of-your-box/)

 	- Astuce utile par Julien Coquet sur une [suppression d'historique dans Chrome](http://juliencoquet.com/2013/09/10/nettoyer-son-historique-de-google-chrome/)
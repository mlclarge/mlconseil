---
title: "Google tag Manager un outil précieux pour un suivi d'audience"
date: 2015-12-14
author: "admin"
categories: ["Google Analytics"]
tags: []
slug: "google-tag-manager-un-outil-webmarketin-bien-utile"
image: "/images/blog/gtm-et-suivi-de-lien.jpg"
---

Il faut se mettre au **[Google tag manager ](https://tagmanager.google.com/)** (avec bien sûr Google analytics en toile de fond) ! Prenons le cas ici  d'un suivi d'engagement visiteur (clic)  sur une page web.   C’est tout de même devenu un jeu d’enfant vis-à-vis du tracking traditionnel. Essayons d’argumenter …

## **Sans Google tag manager ?**

Il faut savoir un petit peu comprendre le langage JavaScript

 	- Récupérer la syntaxe ou le bon script pour coder son objet

 	- Avoir accès au code source du site

 	- Identifier la page où l'on souhaite poser un marqueur **d'évènement** pour GA, ou alors appliquer  un suivi global dans le Template du site via un Js qui va « écouter » ce qui se passe sur toutes les pages. Plus raisonnable si l’on souhaite par exemple suivre les 150 liens sortants du site :s.

 	- Vérifier, tester

[![Image](/images/blog/coder.jpg)](/images/blog/coder.jpg) Dur dur de coder pour un marketeur

Entretemps, le code selon les cms a été modifié par l’éditeur natif (Joomla, WordPress..) et commence la galère. Le développeur qui peut vous aider n’a pas que cela à faire, et votre contenu, tout neuf, tout beau sur la page, reste seul, vierge de tout marquage, face aux éventuelles interactions des visiteurs !

## **Avec Google Tag Manager**

 GTM est composé de bouts de Js (listeners) et d'un conteneur de données (dataLayer) automatisé.

[![Image](/images/blog/automatiser-310x149.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2015/12/automatiser.jpg) Tracking assisté avec GTM

Si on détaille, un temps d’apprentissage est nécessaire pour comprendre la logique de la plateforme certes ! Mais ensuite c’est tout bénéfice pour la suite des tâches de marquage. En effet, GTM embarque dans sa librairie JS nativement des **écouteurs prêts à   l’emploi** qui couvrent l’essentiel des besoins en

 	- Attributs de page ; url, http, réfèrent

 	- Identification des clics  : class, url, texte, Id, élément

 	- Formulaires : caractéristiques identiques aux clics

 	- Historique : écoute les états liés à une navigation dynamique (Ajax), ancres de texte sur la page

 	- Erreurs sur une page : serveur 404, mais aussi clients Js

 	- Utilitaires : récupères des données contenues dans le container (events, ID, version)

### Que fait ce gestionnaire de balises  ?

 	- Scanne nativement tout un ensemble d'objets situés sur la page  ( variables)

 	- Utilise des déclencheurs pour cibler les objets à collecter (events) : étape la plus délicate..

 	- Pousse la data dans son conteneur

 	- Envoie ensuite à des solutions d'optimation de marketing online la data (balises).

[![Image](/images/blog/collecteur-gtm-310x106.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2015/12/collecteur-gtm.jpg) Processus GTM

Ce qu’impose GTM par rapport à la méthode « traditionnelle » manuelle,  est dû à sa nature (pilotage distant du marquage),  donc il faut lui replacer tous les éléments dans le bon ordre.  GTM demande à se poser 3 questions :

[![Image](/images/blog/processus-marquage-Gtm-310x144.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2015/12/processus-marquage-Gtm.jpg) Raisonnement marquage d'un lien sortant

***LA VARIABLE*  c’est lui indiquer ce que l’on veut suivre !** Le QUOI en résumé. Cela  correspondant à l’objet que je souhaite suivre, dans le cadre d’un suivi de lien sortant, c’est **l’identification de l’image**  qui pointe vers un site tiers. Le débogueur du gestionnaire de balise nous aide à identifier cela. Exemple avec ce clic sur le l’image vers Apple store. C’est automatiquement tracé !

[![Image](/images/blog/identification-de-la-vairiable-310x107.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2015/12/identification-de-la-vairiable.jpg) Identification de la variable : objet à cliquer

 	- Variable : click élément

***LE DECLENCHEUR* , c’est le  comment de l’action liée à la variable à cibler.**

 	- Comment : suite à un clic (event : à ne pas confondre avec l’event de GA !) et lorsque qu’un élément de type variable ‘click élément » comporte « iTunes

[![Image](/images/blog/declencheur-gtm-310x172.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2015/12/declencheur-gtm.jpg) **Declencheur gtm**
### **NOTER A CE STADE QUE CETTE CONFIGURATION NE CONCERNE EN RIEN GOOGLE ANALYTICS !**

***LA BALISE ***Reste ensuite à relier Variable et Déclencheur à l’application de tracking ici donc GA avec le modèle de data habituel des évènements (catégorie, action, libellé)  sur l’ordre du déclencheur préalablement défini.

[![Image](/images/blog/balise-GA-310x273.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2015/12/balise-GA.jpg) Balise - Tag GA

Puis à contrôler le résultat…

[![Image](/images/blog/google-analytics-evenement-310x199.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2015/12/google-analytics-evenement.jpg) Control dans GA temps réel
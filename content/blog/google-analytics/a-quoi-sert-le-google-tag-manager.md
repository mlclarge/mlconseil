---
title: "Atouts du gestionnaire de balise"
date: 2014-06-27
author: "admin"
categories: ["Google Analytics"]
tags: []
slug: "a-quoi-sert-le-google-tag-manager"
---

Il est temps de revenir sur le Google Tag Manager. Ce dernier fait partie des TMS (Tag Management Systemes) du marché qui compte pas mal d'acteurs déjà *(Signal, nsighten, Tealium)*  !  L’interface de GTM évolue, les fonctionnalités embarquées sont plus riches, et les développeurs produisent des plugins dédiés au gestionnaire de balises de plus en plus. Rappelons l’utilité de cette application,  ce dont elle a besoin pour fonctionner, et ce que contient "Out of the box"  le GTM bien utile aux non codeurs.

## **Quoi faire avec le Google Tag manager ?**

	- **Marquer** de site web et d’applications web (mobile)

	- Suivre les **paniers e-commerce **(Ventes et bientôt suivi panier)

	- Taguer  les **conversions & Marquage Remarketing**  (Adwords, doubleClick)

	- Baliser pour identifier les** audiences** (bizo, comscore)

	- Marquages **dynamiques spéciaux**  (à base d’ajax, html dynamique)

	- **Suivre les clics** sur un site (internes, externes) et de formulaires

	- Tracer les **téléchargement**s (pdf, images..)

	- Monitorer son **activité sociale**

	- Déceler les **comportements sur le site** (scrolling, temps passé, parcours souris)

	- Etre plus précis sur l’**engagement sur les contenus (**ex sur player vidéo)

[![tag-manager-caractéristiques-310x212.jpg](/images/blog/tag-manager-caractéristiques-310x212.jpg) tag manager caractéristiques
## **A quoi le GTM roule t-il ? **

### **Trois ressources sont nécessaires**

	- Une balise (Marqueur : script de base comme le code de GA : Ua-xxxxxx-x ou Adwords)

	- Une règle (condition basée sur la ou les  macro(s)  pour définir l’étendue du suivi, exemple :  « égal  à »  toutes les pages )

	- Une macro (variable à collecter , ex : les urls des pages du site), ces valeurs d’éxécution sont collectées soit par l’intermédiaire d’une couche de données rajoutée en amont du container sur le site, soit par collecte des éléments de la page (DOM) , soit par par l’ajout de script personnalisés (via Javascript encapsulé dans du html personnalisé) .

[![configuration-tag-manager-310x151.jpg](/images/blog/configuration-tag-manager-310x151.jpg) 3 piliers de la plateforme
## **Qui a-t-il de fourni out of the box ?**

### **Des fonctionnalités de base mais déjà bien utiles **

Je ne mentionne pas le fait qu’au départ, il faut récupérer le code du container (GTM-QZ88)  et l’installer dans le body de son template. Ensuite, plus besoin de se rendre dans le code de son site, ou presque !

J’entends par « out of the box” le fait ne pas toucher à l’élaboration d’un script spécifique. Il convient néanmoins pour les fonctionnalités ci-dessous de remplir les formulaires du GTM avec les données mentionnées dans l’aide de la plateforme.  Donc, sans codage on peut :

	- Opérer au suivi des pages du site en rentrant simplement le  No UA-XXXXXX-X de GA

	- Suivre tous les clics du site (à l’intérieur du site, sortants, downloads)  en créant 1 tag d’évènements avec la bonne règle  d’exécution ((ex :gtm.click) pré-machée.

	- Traquer  les envois de formulaire

	- Enregistrer la circulation des pages du navigateur (utile pour les urls dynamiques : ajax..)

[![interface-google-tag-manager-310x243.jpg](/images/blog/interface-google-tag-manager-310x243.jpg) Possibilités 'out of the box' du Gestionnaire
### **Des paramétrages avancés**

16 macros préconfigurées

	- Utiles pour les paramétrages out of the box, mais aussi pour l’investigation avancée donc

	- Variables d’évènements automatique génériques (6): ces macros récupères les entités de la page web qui peuvent provenir du DOM, des classes du code html, des balises de page, d’éléments constitutifs de l’url.

	- Evènement personnalisé (1)** **: à utiliser sans modération

	- Variable d’historique (5) : Mesure les allers et venus sur le navigateur, les balises dynamiques sur les menus et autres fenêtres ajax

	- Référent (1): simple, c’est l’url de provenance qui pointe sur la page d’arrivée du site

	- Items d’urls (3) : port, nom d’hôte, tagage d’url (utm par ex) , protocole

[![macros-tag-manager-310x264.jpg](/images/blog/macros-tag-manager-310x264.jpg) Macros livrés avec le GTM

Dans un prochain post, je parlerai de l’intégration  du gtm avec  les développements inhérents (plugins) développés pour le GTM.
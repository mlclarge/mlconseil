---
title: "Créér un test AB avec Google Optimize pour Adwords"
date: 2018-04-30
author: "admin"
categories: ["Conversion google ads"]
tags: []
slug: "test-ab-avec-google-optimize-pour-adwords"
image: "/images/blog/page-de-destination-adwords.jpg"
---

Google a pensé à tout lors de son déploiement de sa plateforme d’optimisation de contenu [Google optimize](https://support.google.com/optimize#topic=6314903). En effet, depuis quelques mois, il est possible de la synchroniser avec **Google Adwords** pour optimiser ses campagnes au travers des  pages de destination. Abordons les 3 principales phases dans un **projet d’ AB testing **(un levier webmarketing efficace !) : le  marketing, la technique, la mise en œuvre sur une landing page à soumettre à un test A/B ciblé  (sur une image de tête pour ce petit tuto.).

## **Phase marketing, quel est le contexte du test A/B ? **

Avant de rentrer dans l’outil Google optimize il convient de définir l’environnement global qui va entourer ce projet d’[optimisation des conversions.](https://www.mauricelargeron.com/formation-google-ads/google-ads-et-le-suivi-avance-des-conversions/)  Ici il s’agira de tester une page avec 1 variante (une image) personnalisée sur la zone géographique, bon ok, pas top en design mais on fait avec ses moyens !

[![test-ab-google-optimize-310x231.jpg](/images/blog/test-ab-google-optimize-310x231.jpg) Test ab google optimize

 	- Quelle cible Adwords tester : campagne adwords, groupes d’annonces, mots clés ? Je prendrai ici le niveau campagne. Précision que ce n’est possible que sur des campagnes évoluant sur le moteur Google donc : shopping, recherche (et display sélectif mais Gdn sera ignoré). Noter une réserve du système sur un impact sur le score de qualité, si les landing observent des temps de changements avec des redirections mal maitrisées suite aux clics. (Voir plus bas sur le chapitre technique)

 	- Quel type de test sur la page : A/B (changement d’une seule variable), Redirection (2 pages différentes), Multi variables (plusieurs objets), choix d’un A/B test.

 	- Quelle sera la (les) page(s) que l’on souhaite traiter ! Une page classique avec formulaire de demande de renseignements.

 	- Quel objet variant  choisir : images ? couleurs ? texte ? Dans le test ici, je ne change qu’une image, celle de la bannière haute.

 	- Faire la création graphique de l’objet

 	- Charger la création sur le site web et noter son adresse url (https//www.mondomaine.com/mavarianteimage.jpg), utile lors de la création de la variante de page.

 	- Quel trafic  des visiteurs, sur quelle zone géographique ?  100% , 80%, 50 % ? Ici 100% des clics

 	- Quelle pondération de l’exposition de chacune des versions de la  page : ici je prends  50/50 (soit une répartition équilibrée)

 	- Quel nombre de test à faire : en version gratuite, 3 tests sont possibles par vues dans Google analytics, je ferai qu’un seul test.

 	- A noter : Audience : pas de possibilité de cibler un segment d’audience depuis GAnalytics.

## **Phase technique, mettre en place les outils et les relier**

Il va falloir vers discuter plusieurs plateformes dont la  majorité bien sûr proviennent de la planète Google (optimize, tag manager, analytics, adwords, extension chrome tag assistant), et celle de gestion de contenu, ici le cms WordPress. Tout d’abord il va falloir dans l’ordre

 	- **Créer un compte Google optimize**, plusieurs choix possible : installer le plugin dans le code GA existant (analytics.js ou gtag.js selon l’ancienneté de votre code de suivi), mais en tout cas il est conseillé pour éviter des mauvais effets UX visiteurs, d’installer en dur  dans le head un snippet qui stabilise l’affichage aléatoire selon les visiteurs. Pour ma part je passe par Google Tag Manager, il faudra , si vous utiliser un champ « allow linker » dans votre tracking traditionnel GA de faire ce même choix dans le paramétrage d’optimize pour utiliser à son plein potentiel l’outil de création de variante en mode GUI.

[![zllow-linker-310x231.jpg](/images/blog/zllow-linker-310x231.jpg) Bug éventuel sur paramètre Allow Linker

 	- Insérer le plugin  dans via Google Tag manager (si vous n’avez pas fait le choix précédent en dur dans le Template header.php de votre site). J’ai fait ce choix car je trouve très pratique le choix des déclencheurs, ici, ce test ne sera enclenché que sur la landing précisément. Vérifiez tout de même sur la page en question, si tout est en place correctement avec l’extension navigateur Tag assistant.

[![tag-assistant-google-optimize-310x155.jpg](/images/blog/tag-assistant-google-optimize-310x155.jpg) Tag assistant et Google optimize

 	- Associer le compte  Google optimize définit dans la phase marketing depuis le compte adwords, le marquage du suivi automatique est obligatoire.

 	- Relier Google analytics pour avoir  les rapports des tests obtenus avec l’intégration de Google tag manager et d’optimize  (association).

[![optimize-278x300.jpg](/images/blog/optimize-278x300.jpg) Association des comptes GA et ADW
## **Mise en Œuvre depuis Google Optimize**

Si la phase marketing est complète, l’étape opérationnelle est un jeu d’enfants :) ,  **3 volets** à compléter : objectifs, ciblage et création variante de page.

Il n’est pas obligatoire de travailler avec l’extension browser d’édition de Google optimize mais c’est un outil facilitateur pour intégrer ses créations, où faire des modifications de dernière minuter ou avoir un mode de prévisualisation facile.
Les étapes à suivre ….suivre le wizard !

 	- Connexion au compte Google optimize et création un test (bouton bleu) avec choix du type de test (a/b par exemple)

 	- La plateforme Optimize vous amène sur les **objectifs** dans le contexte de Google analytics : 2 items à remplir ->  Sur quelle vue vue de la propriété, avec quel but, ici je pointe  la page de remerciement une fois le formulaire soumis, elle est proposé automatiquement dans l’interface. L’intérêt aussi est d’ajouter en temps que faire se peut des objectifs supplémentaires au-delà de la simple conversion comme les nombres de pages vues.

[![objectifs-supplémentaires-310x158.jpg](/images/blog/objectifs-supplémentaires-310x158.jpg) Objectifs du test

 	- Second volet du paramétrage avec 3 parties dans **le ciblage** pour ce test

 	- Qui / combien : vue dans la phase visiteur et répartition de l’exposition des variantes de pages.

 	- Quoi : avec les « Règles »  qui pointent sur le compte, campagne, groupe d’annonces, mots clés, pas moins d’une dizaine d’ajustements sont possibles. Je choisis 3 filtres une campagne search  sur une ville : Bordeaux et sur l’url de la landing page.

[![regles-google-optimmize-310x242.jpg](/images/blog/regles-google-optimmize-310x242.jpg) Regles Google Optimize

https://www.youtube.com/watch?v=BlLmOk9q9IU

[![ciblage-optimize-310x218.jpg](/images/blog/ciblage-optimize-310x218.jpg) Ciblages Google optimize

 	- Troisième volet : **Création des variantes** depuis le navigateur à l'aide du plugin Chrome à l'aide de la souris et des éléments définis dans la phase marketing, par  survol des objets html de la page. Pour des changements simples comme les couleurs, les dimensions des blocs, les textes (titre, rédactionnel), les images pas besoin de savoir coder. Pour des élements plus dynamiques , des alternatives basées sur l'utilisateur par exemple , il faudra faire appel à un developpeur Javascript.

[![vairante-optimize-bordeaux-310x214.jpg](/images/blog/vairante-optimize-bordeaux-310x214.jpg) Interface editeur variante depuis chrome
### **Aperçu des résultats sur un petit test « atelier »**

J'illustre ici ce cas pour démontrer que même sur un volume de conversions restreint, Optimize apporte de la donnée.  Ce reporting concerne un test sur une **redirection de page** avec des blocs inversés de contenus. La variante observe 84% en probabilité d’être la meilleure mais à prendre avec des pincettes vu que cette dernière a observé néanmoins quasiment plus du double de sessions.

[![reporting-310x277.jpg](/images/blog/reporting-310x277.jpg) Petit reporting dans Optimize

[![reporting-optimize-ga-310x188.jpg](/images/blog/reporting-optimize-ga-310x188.jpg) Reporting optimize dans ga

J’ai arrêté cette expérience où aucune variante optimale ne s’est détachée, sur le **test A/B** sur l'objet image, je ferai un compte rendu prochainement !
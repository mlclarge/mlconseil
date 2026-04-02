---
title: "Webographie sur le Google Tag Manager (GTM)"
date: 2014-09-08
author: "admin"
categories: ["Google Analytics"]
tags: []
slug: "tutoriaux-liens-pour-comprendre-le-gestionnaire-de-balises"
---

Voici  une liste de **50  ressources  pour Google Tag Manager** dédiée au suivi d’audience avec  **Google Analytics**. J’attends aussi avec impatience  la sortie du bouquin de Ronan Chardonneau sur la thématique du Gestionnaire de balises ! Le dernier article sur ce sujet portait sur l'intégration du container avec un [plugin GTM pour Wordpress](https://www.mauricelargeron.com/gtm-et-le-cms-wp/). Sinon, avant d’énumérer une liste de liens**,** je vais revenir quelque  peu sur les nouveautés du GTM depuis ce mois de juin et ensuite proposerai  différentes sources à partir desquelles  j’ai pu avancer dans la connaissance de ce TMS (Tag Managerment System). Même si certaines d’entre elles sont reliées au tracking classique, elles gardent leur intérêt pédagogique pour la qualité du raisonnement des articles.

## **Principales améliorations et fonctionnalités nouvelles depuis cet été **

### **Pour les Développeurs **

 	- la prévisualisation et mode débogage a été amélioré

 	- La priorité de déclenchement des balises selon une échelle de 0 défaut à 3  (haute priorité)

 	- Amélioration pour IOS du dispatching réseau

 	- Disponibilité de l’affichage du numéro de version du container pour les mobiles

### **E-commerce **

Le plug-in du tracking de panier avancé devient configurable (IOS compris)

### **Adwords **

La valeur de conversion pour le tag de conversion est devenue facultative, et un nouveau champ pour le code monnaie est instauré.
**Présentation et Généralités ou spécificités du  GTM**

Afin d'y voir plus clair dans cette énumération, rien ne vaut mieux qu'un bon schéma !

[*](https://www.mauricelargeron.com/wp-content/uploads/2014/09/organisation-classement-des-ressources.jpg) Classement des ressources GTM

Même si tout le monde le connaît je suis sûr qu’au moins 100% des personnes n’y reviennent pas s’ils n’ont pas trouvé 1 fois la solution à leur problème. Il faut savoir que ce centre d’aide vit, et s’enrichit comme son application : [http://bit.ly/AideTagManager](http://bit.ly/AideTagManager)

**Le blog de Simo Ahava** :   « Google développer expert », blogueur, contributeur actif sur les communautés Google + dans ce post, il énumère différentes sources d’informations sur la thématique, on peut  reconnaître « cocorico » Julien Coquet, lui aussi, très actif sur le sujet parmi tant d’autres et depuis des années (hello, Julien !) : [http://bit.ly/Simo-Ahava-A](http://bit.ly/Simo-Ahava-A)

**Le guide « ultime » sur le GTM, de Phil Pearce** comme le nomme les anglo-saxons :   Quasiment 100 pages sur sujet  qui parle de tous les aspects du gestionnaire de balise, lisible pour un non développeur  comme moi, que par un initié du javascript, à mettre entre toutes les mains pour les curieux , merci à son auteur ! : [http://bit.ly/Phil-Pearce-Guide-A](http://bit.ly/Phil-Pearce-Guide-A)

**Container**  (à placer dans le ** du site au départ)

 	- Les Bases :  [http://bit.ly/Cutroni-Container-C](http://bit.ly/Cutroni-Container-C)

 	- Description ligne par ligne du snippet : [http://bit.ly/Simo-Ahava-Container-E](http://bit.ly/Simo-Ahava-Container-E)

**Datalayer**

Comprendre l’utilité du Datalayer, des articles riches en exemples  sur l’usage de cette couche de données :

 	- Bases implémentation : [http://bit.ly/Getdelve-datalayer-A](http://bit.ly/Getdelve-datalayer-A)

 	- Potentiel  du snippet : [http://bit.ly/Padicode-datalayer-A](http://bit.ly/Padicode-datalayer-A)

 	- Ecommerce : [http://bit.ly/Lunametrics-Datalayer-G](http://bit.ly/Lunametrics-Datalayer-G)

 	- WordPress (julien coquet) : [http://bit.ly/JulienCoquet-datalayerWp-A](http://bit.ly/JulienCoquet-datalayerWp-A)

### **Application Mobile**

 	- Intégration du GTM sur Apps : [http://bit.ly/GoogleIO2013-MobApps-A](http://bit.ly/GoogleIO2013-MobApps-A)

## Suivi globaux à l’échelle du site web**

### **Suivi multidomaines**

 	- Par lunametrics :[ http://bit.ly/Lunametrics-A]( http://bit.ly/Lunametrics-A)

 	- Avec un code muni d’Iframes, un casse-tête bien souvent : [http://bit.ly/Knewledge-cross-iframes-A](http://bit.ly/Knewledge-cross-iframes-A)

 	- Sous l’ancien code classique (démarche intéressante même si obsolète multi et sous domaine) : [http://bit.ly/margari-net](http://bit.ly/margari-net)

### **Catégorisation - Segmentation personnalisée**

***GA Classique :***

Instauration d’une variable personnalisée (appelée aujourd’hui sous UA dimension) pour suivre les visiteurs qui se sont logués : [http://bit.ly/Conversionrepublic-A](http://bit.ly/Conversionrepublic-A)

Migration d’un  mode de tracking traditionnel à base de CustomsVars vers  le gestionnaire de balise Google,   sur un  forum développeurs, même si la procédure est « deprecated » la démonstration est utile et peut être reporté sur la  nouvelle syntaxe UA : [http://bit.ly/StackOverFlow-A](http://bit.ly/StackOverFlow-A)

***Universal :***

 	- Implémentation par une dimension personnalisée d’un tracking pour faire remonter le nom des auteurs des pages consultées : [http://bit.ly/CommunautéGplus-A](http://bit.ly/CommunautéGplus-A)

 	- Configuration d’un regroupement de contenus par code de suivi  (différent de l’extraction par règles ou par urls).  Mehdi Oudjida un des modérateurs de la communauté France Google Analytics, aide au paramétrage : [http://bit.ly/Communauté-GA-GPlus-Fr-A](http://bit.ly/Communauté-GA-GPlus-Fr-A)

 	- Tutoriel en images pas à pas du regroupement par thèmes et débogage  par S. Ahova  : [http://bit.ly/Simo-Ahava-B](http://bit.ly/Simo-Ahava-B)

***WordPress :***

 	- Installer le Tag Manager pour le CMS WP : J’ai pu parler dans un article précédent du plugin pour Gtm de Thomas Duracell : [http://bit.ly/GTMetWPress](http://bit.ly/GTMetWPress)

 	- Plus technique, un article sur les Hack possibles sur des templates WordPress assez populaires : [http://bit.ly/WordPress-Templates-et-GTM](http://bit.ly/WordPress-Templates-et-GTM)

## **Marqueurs analytics au niveau de la page web**

### **Contenus de la page**

**AB Testing **

 	- Intégration d’une plateforme de test A/B comme Optimizely et Google analytics via le GTM, cela passe par une portion de code Html maison, mais la démonstration est simple à suivre, intéressant : [http://bit.ly/VerticalNerve-A](http://bit.ly/VerticalNerve-A)

**Evènements **

Sont des interactions autres que les simples pages vues et qui peuvent servir à déceler des comportements (clics, téléchargements, survols..) sont aussi configurables via le GTM,  voici quelques ressources :

 	- Source Officielle : [http://bit.ly/Blog-Analytics-Event-A](http://bit.ly/Blog-Analytics-Event-A)

2 vidéos et articles très pédagogiques en anglais mais qui résume bien l’utilité des évents  (liens sortants, pdf, mailto, Ajax, vidéo player, formulaires) *et  du Google tag manager  :

 	- [http://bit.ly/KissMetrics-A](http://bit.ly/KissMetrics-A)

 	- [http://bit.ly/Youtube-event-GTM-A](http://bit.ly/Youtube-event-GTM-A)

 	- [http://bit.ly/Cutroni-events-A](http://bit.ly/Cutroni-events-A)

 	- Event  tracking via le gestionnaire, mais vu dans la console du navigateur cette fois ci, son auteur est réactif et  répond aux commentaires sur des interrogations nouvelles : [http://bit.ly/SwellPath-eventsConsoleJs-A](http://bit.ly/SwellPath-eventsConsoleJs-A)

 	- En français, mais pour le code GA Classique, donc mérite d’être mentionné ! Le processus est bien expliqué, reste à le transposer pour Universal : [http://bit.ly/Optim-Conversions-events-A](http://bit.ly/Optim-Conversions-events-A)

 	- Un débogage d’un problème sur un suivi d’évènement, la progression est intéressante, le problème venait d’une option par défaut du gestionnaire qui bloquait le déclenchement des tags : [http://bit.ly/Communauté-GA-GPlus-Fr-B](http://bit.ly/Communauté-GA-GPlus-Fr-B)

**Téléchargement de Pdfs**

Au-delà du simple tracking d’évents, Jonathan Weber  de lunametrics nous démontre comment il est simple de cibler son marqueur sur une url de téléchargement qui contient à la fin « .pdf » :

 	- [http://bit.ly/Lunametrics-pdf-B](http://bit.ly/Lunametrics-pdf-B)

 	- Une  variante cette fois-ci mais sur un paramètre de l’url via une /Regex/et le paramétrage des attributs de l’évènement (catégorie, action, libellé) : [http://bit.ly/Provenance-Pdf-A](http://bit.ly/Provenance-Pdf-A)

 	- Ronan Chardonneau s’y est collé aussi, donc, en Français et d’une manière très claire, après cette lecture, le tracking de pdf n’a plus de secret : [http://bit.ly/Ronan-Chardonneau-pdf-A](http://bit.ly/Ronan-Chardonneau-pdf-A)

**Scrolling du navigateur**

 	- Comment se comporte ici encore, le visiteur, zappe-t-il directement vers le bas de l’article, a - t-til un cheminement progressif, bref, le contenu est-il lu réellement ?  L’écoute des mouvements de l’ascenseur peut aider à répondre à cette interrogation :[ http://bit.ly/Cutroni-scrolling-B]( http://bit.ly/Cutroni-scrolling-B)

**Survols de liens**

 	- La bannière, le widget, bref, les « call to action » sont-ils vraiment efficaces ? Comment mesurer une pré-interaction ?  Le suivi des  Roll-Over peut constituer un marqueur utile. Est-il fiable et maitrisé ? Alors là, bonne question, à tester. : [http://bit.ly/Lunametrics-RollOver-C](http://bit.ly/Lunametrics-RollOver-C)

**Lecture de Vidéos**

 	- Trop fort Stéphane Hamel, ici, pour Cardinal Path, il nous livre tous les ingrédients pour suivre les comportements visiteurs sur un player Youtube, merci ! : [http://bit.ly/CardinalPath-video-A](http://bit.ly/CardinalPath-video-A)

[![video-player-gtm-310x250.jpg](/images/blog/video-player-gtm-310x250.jpg) Suivi du Player YT via Appel Api
**Formulaires**

 	- SImo nous livre un de ces articles fameux, il déroule la façon dont traquer tout ou pratiquement tout sur un formulaire : les champs, les listes déroulantes, les cases à cocher, boutons radio .. : [http://bit.ly/Simo-Ahava-form-C](http://bit.ly/Simo-Ahava-form-C)

 	- Abandon de champs : Cette discussion apporte des éléments sur les abandons de remplissage de  formulaires, si des infos plus précises existent, je suis preneur : [http://bit.ly/Forum-Google-Tag-Manager-A](http://bit.ly/Forum-Google-Tag-Manager-A)

## **Tag Manager & SEA**

### **Suivi de campagnes**

 	- **Lunametrics**, eh oui, encore eux, nous partage leur savoir sur le suivi de campagne à base de variables utm ..dynamiques ! Soit en fait, suivi l’apport de trafic provenant d’un même canal par exemple mais dont les acteurs sont pluriels (affiliation par exemple), le problème à résoudre est le paramétrage de cet « utm source » qui, si elle est ignorée, Google ne la traquera pas..La solution, prévoir ce paramètre utm : source  mais lui affecter une valeur au moment de la session en capturant la provenance du référant  (un bout de Js  accomplit cette tâche, et va chercher dans l’URI, la variable referrer) : [http://bit.ly/Lunametrics-UtmDyn-D](http://bit.ly/Lunametrics-UtmDyn-D)

### **Pose du tag de conversion Adwords**

 	- Suivre les conversions de formulaires suite à une campagne Adwords. Le conseil est donné par Theniks sur la communauté  anglaise : [http://bit.ly/Communauté-Anglaise-Adw-TagConversion-A](http://bit.ly/Communauté-Anglaise-Adw-TagConversion-A)

### **Remarketing**

Le principe est d’alimenter une liste visiteurs passés sur un site web  « a » via un tag et ensuite de proposer à ces visiteurs à nouveau un contenu publicitaire  lié à sa visite sur ce site « a ». Doc pdf d’andré mafei : [http://bit.ly/AndreMafei-rmktg-A](http://bit.ly/AndreMafei-rmktg-A)

### **Suivi e-commerce**

 	- Notez le [guide complet  sur GTM et Prestashop](http://www.chablais-web.fr/google-tag-manager-ecommerce-prestashop.php) édité par Bruno Guyot.

 	- Eviter les doublons  des transactions, avec le GTM, c’est possible !  Ce problème est fréquent lors de redirections hasardeuses où les pages de remerciements sont doublées : [http://bit.ly/Lunametrics-dédupConv-E](http://bit.ly/Lunametrics-dédupConv-E)

 	- Enhanced Ecommerce (commerce amélioré ?)  : C’est un ajout au tracking de base ecommerce existant. Ici, Impressions, abandons et  suppression de paniers, usage de coupons sont balisés. Source officielle des développeurs, mais avec le tag manager, c’est possible oui, depuis ce mois d’août :  [http://bit.ly/GoogleDevelop-enhancedEcom-A](http://bit.ly/GoogleDevelop-enhancedEcom-A)

 	- Pour continuer sur la vente, Brian O' Sullivan nous démontre l’utilisation de variables perso. pour segmenter le comportement visiteur par le type de catégorie de produit qu’il visite. Dynamiquement, il affecte une  macro  qui va récupérer  certains paramètres distinctifs de la page vue, puis dans un second temps, les affecter ensuite aux urls de pages de conversions.  Ainsi, il crée  un lien direct entre un  chemin probable de conversion  et la vente finale.  Il fallait y penser : [http://bit.ly/Conversionrepublic-conv-B](http://bit.ly/Conversionrepublic-conv-B)

 	- **Magento** : Pas évident lorsque l’on parle de tracking sur un Framework comme Magento, bon, merci à Ludismédia de s’y être penché : [http://bit.ly/LudisMedia-magento-A](http://bit.ly/LudisMedia-magento-A)

### **Social**

 	- Pas évident de suivre qui clique sur les boutons de partage, nativement dans GA, les données sur les plugins sociaux sont pas top, Simo ici nous démontre qu’avec le gestionnaire de balises , rien n’est compliqué :[ http://bit.ly/Simo-Ahava-SocialBout-D]( http://bit.ly/Simo-Ahava-SocialBout-D)

### **Google Analytics et ses filtres**

 	- Comment le GTM peut permettre d’éviter d’utiliser les filtres contenus dans l’interface de Google Analytics ? L’intérêt est de diminuer à la source, le flux de clics et ainsi, de restreindre l’échantillonnage, cela démontre la puissance de ce TMS  :[ http://bit.ly/Lunametrics-Filters-F]( http://bit.ly/Lunametrics-Filters-F)

## **Astuces techniques pour non développeurs ou dev. Confirmés !**

### **Pages Virtuelles**

 	- Affiner son tunnel de conversion : [http://bit.ly/RepriseMedia-pagesVirtu-A](http://bit.ly/RepriseMedia-pagesVirtu-A)

 	- Se débarrasser des urls compliquées :[ http://bit.ly/OnlineBehavior-PagesVirtu-A]( http://bit.ly/OnlineBehavior-PagesVirtu-A)

### **Debugging Avancé**

 	- Debugging révélé, malgré un lien disparu dans ce post ! Une astuce pour faire lâcher des infos de la console JS  du mode debug de GTM : [http://bit.ly/GooglePlusCty-debugTips-A](http://bit.ly/GooglePlusCty-debugTips-A)

Voilà un extrait  de ce que peut faire ce TMS, toutes nouvelles sources sont les bienvenues ! Merci d'avance..
## **Quelques tutos sur ce blog pour démarrer ...**

 	- [https://www.mauricelargeron.com/chrome-pour-decrypter-le-gtm-de-google-analytics/](https://www.mauricelargeron.com/chrome-pour-decrypter-le-gtm-de-google-analytics/)

 	- [https://www.mauricelargeron.com/suivi-des-clics-en-2-clics-avec-le-tag-manager/](https://www.mauricelargeron.com/suivi-des-clics-en-2-clics-avec-le-tag-manager/)

 	- [https://www.mauricelargeron.com/guide-pour-demarrer-avec-le-gogle-tag-manager/](https://www.mauricelargeron.com/guide-pour-demarrer-avec-le-gogle-tag-manager/)
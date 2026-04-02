---
title: "Javascript un language presque familier pour Google"
date: 2016-01-11
author: "admin"
categories: ["Référencement naturel"]
tags: []
slug: "js-et-les-moteurs-de-recherche"
image: "/images/blog/seo-et-js.jpg"
---

Depuis l’invention du [JavaScript](https://fr.wikipedia.org/wiki/JavaScript) par **Brendan Eich ***(ex CEO  évincé pour la petite histoire de la direction de FIrefox en 2014 à laquelle il a contribué depuis 1998)*** ** en 1995  lorsqu’il était Développeur chez Netscape   ex-leader en son temps des navigateurs (l’équivalent de l’actuel navigateur le plus prisé Chrome) ce** langage de programmation côté client** (cad qui s’exécute depuis la machine du visiteur) a subit de multiples évolutions. Mesurons aujourd’hui son impact sur les contenus et notamment en matière de pratiques seo.

## **Google et JS**

Google l’annonçait fin **octobre 2015**, les recommandations datant de **2008/2009** sur les possibilités de lecture du JS et sur les recommandations de codage Ajax ne sont plus d’actualité. Un élément de plus qui témoigne de la vélocité du moteur à pouvoir comprendre et restituer les contenus codés en JS.

**2013** marque une étape du moteur dans sa capacité à lire le JS des pages Web. Sans penser à tromper le moteur par des pratiques malveillantes, le fait d’utiliser un JS traditionnel ou Asynchrone (Ajax qui permet des effets de présentation selon l’interaction du visiteur) est désormais plus une contrainte car le moteur  peut lire  assez bien (G) le  JS d'une page et par ricochet donc du **DOM**  (rendu html JS par le moteur JS du navigateur pour faire  court), et ainsi indexer les contenus encartés dans des objets purs Html et JavaScript (menus, contenus déroulants, liens hypertextes, les objets de formulaires).

Précisons également qu’il existe globalement 2 façons de générer du contenu dynamiquement sans appel à un rechargement de la page par le Browser :

 	- Via **JavaScript et CSS** côté client : ou le contenu est chargé dans la page mais pas en visuel, c’est sur un roll-over ou via un scroll que celui-ci sera présenté au visiteur

 	- Via **Ajax côté serveur** : où le contenu est généré dynamiquement aussi mais après des requêtes de type XHR (xmlHttpRequest) ou Json selon interaction de l’utilisateur avec le contenu.

Il y a quelques mois SEL a mené quelques test sur ce que voit **Google lors du crawl d’une page web**, bilan : les balises [Seo](https://www.mauricelargeron.com/seo-local-et-traces-du-pigeon/) (titre, méta, canonique, Hn) sont respectés, et les contenus à l’intérieur aussi. Great ! **Search Engine Land** remarque tout particulièrement son efficacité depuis une grosse année.
Cinq grandes catégories furent passées en revue :

 	- Redirection : window.location function

 	- Liens JS : onChange (déroulant), avec ancres » # » , Href=javascript :void(0) ; concaténation

 	- Balises dynamique : tire, méta, méta robot,

 	- Contenu dynamique : interne et externe (texte, image, liens, navigation)

 	- Attribut rel= »no follow » : exception !

En général, Google bot lie et assimilerait  le contenu de la page web  (statique ou dynamique) sauf cas particulier lors de la manipulation d’un attribut not=nofollow poussé via le Dom sur le href, le bot n’attend pas le chargement final du Dom, le codage traditionnel lui est fonctionnel  où  Google ne suit pas l’attribut du lien comme prévu.

Pour résumer, les  **Google bots** (il y en a[ 9](https://support.google.com/webmasters/answer/1061943?hl=en) pour simplifier)  fait le job de charger la page, de lire les scripts Js, de simuler certains  « events » (clics par exemple) pour aller chercher au plus profond les contenus à indexer. Le fait-il d’une manière systématique et sur tous les sites ?  Bon tout cela c'est de la  théorie, mais le fait-il vraiment ? Selon John Mueller dans un hangout ici  https://plus.google.com/events/c37bs2o8a413c0aqnh05jteb7ek indique que le **Crawler Google ne sait pas manager les events** du genre survol de souris, alors  qui croire  *(merci à Mathieu Chartier pour cette info.)* ? Les plus pointus des SEO actuels ont déjà la réponse par une pratique quotidienne.  Il ne faut pas trop donner de pouvoir non plus à César, mais le temps de crawl et petites mains algorithmiques dépendent aussi du budget temps qu’alloue le grand Google au site web scanné.

## **Utilisation de Framework Js modernes (MVC, MVP, MVVM) : Focus sur angularJs le Framework G. !**

[![seo-et-javascript-310x277.jpg](/images/blog/seo-et-javascript-310x277.jpg) Web Serveur VS Client

**AngularJs,**  Ember.js,  backbone.js etc…sont des solutions qui optimisent l’expérience utilisateur et la gestion des ressources. AngularJS est poussé par Google, il permet de construire des applications web mais peut également servir à créer de site web de toute pièce. C’est un manipulateur du DOM comme le sont ces confrères. Malgré les possibilités de Google Bot, certains conservateurs indiquent que pour être Seo friendly l’utilisation d’une version « flat » pilotée via des « vues »  coté serveur  reste néanmoins d’actualité ! A l’aide d’urls dédiés, de middlewares comme prerender.io  ou brombone facilitent la gestion des crawls pour les « spiders ». Tous les crawlers ne sont pas JS  friendly made, donc il faut aussi penser aux autres !

**Particularité à savoir** pour les pages Web sous ce framework : les sites fait en AngularJS ne sont pas visible sur le cache de Google. Il faut passer par la Search Console de Google pour avoir un aperçu *(merci à Olivier Andrieu pour ce relais d'information issue du Forum webmaster anglais)* .

Voici ici **une source de sites**   web construit en AngularJS : https://www.madewithangular.com/#/. Sinon **exemple de site : http://jobfoundry.com/** faire clic droit pour lecture du code source, il n'y a pas grand chose !

[![fait-avec-angularJs-310x185.jpg](/images/blog/fait-avec-angularJs-310x185.jpg) https://www.madewithangular.com

**Des scripts à optimiser  JS et autres manipulations du DOM**

Une fois briefé sur les capacités des spiders du marché, il faut bien se mettre à la tâche et ne pas faire n’importe quoi !

Le Search engine optimisation passe aussi par :

 	- **Optimisation du poids des pages **: prenons l’information du JDN qui relate l’étude de Dareboost pour le site Edf je cite : «*EDF ne compresse pas certains de ses fichiers JavaScript, ce qui pourrait pourtant faire gagner près de 15% du poids total de ce type de ressources. On remarque d’ailleurs d’autres efforts intéressants pour ces contenus, puisque près de **500ko de JavaScript** sont nécessaires pour permettre le début de l’affichage de la page. »*

[![jdn-classement-dareboost-310x220.jpg](/images/blog/jdn-classement-dareboost-310x220.jpg) jdn classement Dareboost

 	- **Parallax et balisages Urls** : marquage des principales balises de la page : peu importe comment est généré le contenu d’une page, il faut que les différents états de cette page soit marqués entre l’entête statique et le footer. Voici un exemple avec cette url ou sans changer de page, les 3 urls qui défilent dans la barre d’adresse seront indexées individuellement dans Google : http://parallax.iprospectcontent.co.uk/the-jquery-engine

[![contenu-et-js-256x300.jpg](/images/blog/contenu-et-js-256x300.jpg) Technos Onpage pour pousser du contenu

L’ingénierie de cette page s’articule autour de 2 piliers : l’écoute  du scrolling et la génération dynamique des urls (3) via Jquery.

Donc on constate que JavaScript ne rime pas avec magique ! Les développeurs web  spécialisés dans les frameworks modernes sont recherchés selon certains Geeks observateurs car nécessitent une bonne maîtrise de l’écosystème global Client/serveur.

**A savoir !**  : Pour faire simple, depuis la fin de la première décennie (2009), une  techno.  Javascript existe côté serveur comme **Node.Js.**

## **Quelques Pratiques JavaScript reliées au Seo**

**Offuscation de liens : **le principe est de dissimuler pour le moteur les liens sortant d’une page, cela favorisant sa puissance  d’un point de fut scoring de PR (linkjuice pour les experts). Je renvoie en fin d’article sur les 2 techniques JS de Mathieu Chartier à ce sujet (merci !) : liens cachés sur le front de page(overflow) et l’autre qui dissimule au niveau du code source  que son auteur nomme **jQueryRank Sculpting.**

**Dissimulation de contenu **: présenter une page pour le lecteur (celle avec de la pub, affiliation par exemple), une autre pour le moteur (sans intérêt particulier, propre). Technique JS appelé cloaking (peut aussi s’appuyer sur d’autres techniques coté serveur).

**Personnalisation de contenu **: construire une page personnalisée selon la provenance du trafic (référent par exemple), selon le lien cliqué, un script est placé sur la page de destination écoute la provenance du lien et affiche un contenu adapté. Des script sur mesure ou alors du commerce sont à la mode utile autant en seo qu’en sea, emailing etc …

**Redirections temporisée** : Une page redirige vers une autre au bout d’un certain temps. Bon pas très fin comme manipulation, le visiteur se fait balader une fois mais pas deux, mais cette fois-là, même qu’une fois, le but est atteint.

**Rafraichissement automatique** : Au bout d’un temps déterminé, la page se recharge toute seule, pas mal ou augmenter les métriques de consultations de pages, bannières…

**Détournement de navigateur** : un site infecté contamine un navigateur et le système d’exploitation (base de registre), un des plus connu actuellement est delta homes , cette pratique est plus communément appelé « browser hijacker ». Une bonne alternative au MFA (made for adsense) plus trop en vogue chez Google. La page d’accueil d’accueil de son moteur préféré est redirige sur des sites pleins de pub. Bon cela se voit de suite, et rend quasiment son browser.

### **Quelques liens **

 	- AngularJS : [https://angularjs.org/](https://angularjs.org/)

 	- Facilitateur  de lecture Js pour Search engine : [https://prerender.io/](https://prerender.io/)

 	- Google Bots :

 	- JrSculpting par Mathier Chartier : [http://blog.internet-formation.fr/2013/05/jqueryrank-sculpting-modifier-les-balises-en-liens-elementtoa/](http://blog.internet-formation.fr/2013/05/jqueryrank-sculpting-modifier-les-balises-en-liens-elementtoa/)

 	- Guide google : https://google.github.io/styleguide/javascriptguide.xml#JavaScript_Style_Rules
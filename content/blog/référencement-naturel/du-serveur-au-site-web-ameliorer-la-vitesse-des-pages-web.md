---
title: "Du Serveur aux pages web améliorer la vitesse d'un site"
date: 2018-02-12
author: "admin"
categories: ["Référencement naturel"]
tags: []
slug: "du-serveur-au-site-web-ameliorer-la-vitesse-des-pages-web"
image: "/images/blog/ameliorer-la-vitesse-du-sit.jpg"
---

Et si soudainement, les vulnérabilités  des processeurs d'Intel qui ouvrent des attaques malveillantes comme [**MeltDown et Spectre**](https://meltdownattack.com/) affectaient tous mes efforts** webmarketing** que je fais pour le SEM, display etc. ? Certains observateurs indiquent que les patchs pour combler ces intrusions sont encore pas au point, mais en tout cas, ralentissent les machines sur lesquelles tournent les serveurs web, donc les sites web par répercussions ! J’ai donc appelé mon hébergeur préféré (Yoorshop) pour prévenir éventuellement d’une telle  menace. Bon cela c’est pour le storytelling, mais au final, j’ai gagné en **vitesse**,  et l'ont sait que le **Seo** aime çà depuis 2010, et  juillet 2018 marquera sans doute un nouveau challenge avec le Speed Update  pour les mobiles !

## ***Améliorer la vitesse d'un site web côté hébergement***

### ***Perfuser son site sous SSD Intel sur interface NMVe***

Bon, quand Johann m’indique que justement qu’il souhaitait changer la  machine sur lequel était hébergé mon site !  De toute façon, MeltDown/Spectre ou pas, si les disques sont très performants à la base, les incidences de ralentissement sur d’éventuels patches à venir n’y seraient pas perceptibles. Alors passons au disques durs SSD NMVe !

Alors banco, cela a pris 10 minutes chrono, avec interdiction d’écrire sur la base de données pendant ce temps, le site restant disponible en lecture et donc disponible aux visiteurs.

Résultat ? Prenons comme étalon, la page d’accueil sur un site WordPress. Sans aller rentrer dans les outils de Benchmark dans un premier temps. Les pages s’affichent plus vite, après bien sûr vidage de cache au préalable en partant d’une session toute neuve. Je dirai au doigt mouillé que j’ai pu gagner, selon les pages une grosse demi-seconde soit 500 ms tout de même ! Si vous êtes curieux sur l'histoire des processeurs, cette infographie vaut le détour...

[![histoire-des-processeurs-intel-502x233.jpg](/images/blog/histoire-des-processeurs-intel-502x233.jpg) histoire des processeurs intel
### ***Comment vraiment vérifier la vitesse réelle d’un site web ?***

Il y a de nombreux outils, mais cela dépend vraiment du contexte utilisateur, dans l’idéal aujourd’hui, il faut faire confronter  différents outils  en mode 3G pour être au fait de la mobilité et de l’affichage sur les smartphones.
***Analyser la vitesse avec les crawlers distants***

 	- Certains sont flatteurs comme Pingdom  qui me donne moins  de bons résultats,   je passe sous la barre de 1 seconde …hum hum...

[![temps-de-chargement-pingdom-449x300.jpg](/images/blog/temps-de-chargement-pingdom-449x300.jpg) temps de chargement pingdom

 	- D’autres, moins flexibles pour paramétrages donnent des performances moins flatteuses comme DareBoost, GtMetrix, GooglePage Speed, WebpageTest.

[![temps-de-chargement-site-web-502x226.jpg](/images/blog/temps-de-chargement-site-web-502x226.jpg) temps de chargement site web aec Gt Métrix
### ***Des  outils côté « client »***

 	- Plugins natifs de chrome ou lightHouse, mais encore [a](https://www.apptelemetry.com/)pptelemetry.com qui semblent plus proche de la vérité, la vôtre sur le moment uniquement ! Je suis sans doute plus proche de la réalité ici qu'avec les 2 outils précédents., entre 1 et 2 secondes sur la page d'accueil.

[![temps-de-chargement-reel-coté-client-453x300.jpg](/images/blog/temps-de-chargement-reel-coté-client-453x300.jpg) Temps de chargement reel coté client
### ***Des Services tiers de test utilisateurs***

 	- Des plateformes  comme [https://www.userlynx.com/](https://www.userlynx.com/) permettent de prendre du recul et d’avoir une vision utilisateurs plus exhaustive  et en plus de travailler sur l’expérience utilisateur (UX)

## **Optimiser avec les  logiciels serveurs ! **

 	- **Optimisation du PHP** du site grâce à la gestion des connections, des caches avec** Nginx ou Varnish** comme Reverse Proxy. Cela consiste à utiliser via ces logiciels principalement des modes de compressions comme brotli (pas reconnu par des outils de test de vitesse d’ailleurs), gzip, http2. Le but étant d’optimiser le chargement du code source du site web. Bon je ne m’aventure pas trop là-dedans, trop technique et je pourrais raconter n’importe quoi. Ci-dessous les principaux apports des techniques du marché.

## **Optimiser aussi son Seo côté site web**

 	- Un **langage optimisé** : dans le cas de WordPress, depuis 2015 les versions sont compatibles php7 une sacré évolution sur la 5.6 (2 fois plus performant en gros en vitesse d’exécution).

 	- Une **solution de cache pour Cms** comme WP-rocket qui permet de bien s’articuler avec les logiciels serveurs avec ces principaux atouts :

 	- Mise en cache de toutes les pages pour une visualisation rapide

 	- Pré chargement du cache de fichiers à l'aide de deux robots en Python

 	- Réduction du nombre de requêtes HTTP pour réduire le temps de chargement

 	- Diminuer l'utilisation de la bande passante avec la compression GZIP

 	- Gestion des en-têtes (expire, etags ...)

 	- Minification et concaténation des fichiers JS et CSS Chargement différé d'images (LazyLoad) Chargement différé de fichiers JavaScript

 	- Le  **Choix d’un Template** et des modules annxees optimisés. Là encore, cet aspect est super important. Celui que j’utilise ici (eleganttheme) n’est pas forcément le meilleur mais c’est une bonne base, l’idéal, c’est celui maison, sur mesure, adapté à ses besoins, mais le sur-mesure coûte toujours un peu plus !

 	- **Alléger les pages**, que ce soit en terme :

 	- de liens (netlinking, siloing),

 	- de présence de scripts externes avec tous les trackeurs de web analytics, publicitaire, comportementaux, de rétention (fenêtre de chat ..)

 	- de lourdeur classique sur les images

Au final, parlons plus de **vitesse de pages que de vitesse de site**. N’oublions pas que le navigateur sans ces  optimisations, reconstruit à chaque chargement de page sur un domaine l’ensemble de l’affichage. Ici, sur le mien, les pages catégories, articles, landing, home ont toute des vitesses différentes. Le webmarketeur doit faire des choix sur chacun des objectifs des contenus affichés, c’est toute la difficulté dans cette thématique d’optimisation des performances et de la vitesse d'un site web.
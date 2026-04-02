---
title: "6 fonctionnalités et 1 application améliorent google analytics"
date: 2012-12-12
author: "admin"
categories: ["Google Analytics"]
tags: []
slug: "google-analytics-devient-universel"
---

Voici les dernières fonctionnalités de l’interface Google analytics observées depuis ce dernier trimestre 2012 pour ceux qui n'auraient pas suivi l'actualité de l'application. Il faut suivre ! Je commence sans ordre chronologique, mais plus par importance des nouveautés. Le futur de Google analytics s’oriente sur l’analyse d’audience « multi-devices » avec le programme « Universal Analytics », en version bêta et sur demande.  Cette version a pour objectif d’apporter une vision à 360° sur les différents points de contacts que chaque potentiel acheteur consulte avant de passer à l’acte d’achat. Techniquement, il s’agit d’un nouveau protocole qui permet la collecte et l’intégration de données externes provenant de tous types d’appareils  dans un compte Google analytics *(appareils numériques divers, tablettes, Smartphones, consoles de salon)* . Les données sont synchronisées offline et online, et la personnalisation qui en découle devient plus proche des données de l’entreprise. A lire sur le sujet cet article du [blog polynet](http://blog.polynet-online.fr/m-commerce-smartphone-tablette.html) en francais  et sur le [blog analytics](http://analytics.blogspot.fr/2012/10/universal-analytics.html) de G. !

[![Image](https://www.mauricelargeron.com/wp-content/uploads/2012/12/1-analytics-UNIERSAL-219x300.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2012/12/1-analytics-UNIERSAL.jpg) Fig.1 Google Analytics Universel

Revenons sur la version actuelle, qui permet elle aussi d’intégrer des **données de couts** de campagnes externes à adwords. Elle est disponible depuis le bouton « admin » via « profil » en allant sur l’onglet « **définitions personnalisée**s ». Un développeur est nécessaire pour ce genre d’intégration, cette fonctionnalité est encore en bêta. En gros, **4 étapes,** taguer les urls de la campagne externe, récupérer les données de reporting  *(mots clés, impressions, clics, cout..)* sous forme de fichier .csv, configurer une entrée (voir fig. 2)  et ensuite se connecter à l’api pour y intégrer les données.

[![Image](https://www.mauricelargeron.com/wp-content/uploads/2012/12/2-definitions-personnalisees-ga-310x133.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2012/12/2-definitions-personnalisees-ga.jpg) Fig. 2 Definitions personnalisées

Le but de cette possibilité d’incorporer à Google analytics des données de cout externe est d’améliorer l’analyse de rentabilité composée d’**indicateurs**  (automatiquement calculés) comme le **revenu par clic** (RPC), le  **ROI** (retour sur investissement) et la  **marge**.

Toujours dans la partie « profil », il est possible de monter une **liste de remarketing** *(relever les visiteurs non convertis, ou convertis d’ailleurs..)* pour un reciblage en vue d’obtenir une autre conversion.  Le paramétrage est très simple (fig. 3).

[![Image](https://www.mauricelargeron.com/wp-content/uploads/2012/12/3-remarketing-liste-310x210.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2012/12/3-remarketing-liste.jpg) Fig. 3 Liste de remarketing dans GA

Votre compte GA doit être lié  à Adwords bien sûr. Il suffira ensuite de lancer une campagne en utilisant comme cible sa liste préalablement construite via l’onglet « **display** ». (fig.4)

[![Image](https://www.mauricelargeron.com/wp-content/uploads/2012/12/4-remarketing-liste-1-310x212.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2012/12/4-remarketing-liste-1.jpg) Fig. 4 Remarketing dans Adwords

A noter, toujours dans « l’admin », l’onglet information de suivi qui intègre un outil tagage d’urls avec les **variables utm** *(nom, source, medium, term, content)*. Ce dernier est utile pour tracer les liens issus de campagne emailing, d’affiliation ou autres (fig. 5)

[![Image](https://www.mauricelargeron.com/wp-content/uploads/2012/12/5-analytics-info-suivi-310x230.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2012/12/5-analytics-info-suivi.jpg) Fig. 5 Infos de suivi dans GAnaltyics

L’onglet « paramètres du site » situé toujours au niveau administration (fig. 6), fait apparaître désormais une fonctionnalité plus poussée pour l’analyse des clics sur l’interface du site audité *(attribution améliorée des liens - ergonomie)*, l’association avec les « outils pour webmasters » est aussi piloté à cet endroit (utilise pour l’**analyse des mots clés** pour le référencement).

[![Image](https://www.mauricelargeron.com/wp-content/uploads/2012/12/6-analyse-pages-web-0-288x300.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2012/12/6-analyse-pages-web-0.jpg) Fig. 6 Analyse des clics sur la page

Voici une capture d’écran* (source: google analytics blog)*  sur l’avant et l’après activation des liens d’attribution pour l’analyse des pages web (fig. 7).

[![Image](https://www.mauricelargeron.com/wp-content/uploads/2012/12/7-analyse-pages-web-01-310x123.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2012/12/7-analyse-pages-web-01.jpg) Fig. 7 Analyse de page Web

On ne peut pas terminer ce tour des nouveautés sans parler d’un outil externe à Google analytics mais dont son existence lui est directement liée, le [gestionnaire de balises](http://www.google.com/tagmanager/). Une plateforme web gratuite, conçu par  Google,  qui centralise les différents tags à poser sur un site. Plus la peine d’aller dans le code source pour poser des bouts de code de suivi, tout au long de la vie du site. Il suffit d’un seul paramétrage (pose du conteneur) en amont,  pour ensuite n’utiliser que le tag manager (autrement appelé Fig. 8).

[![Image](https://www.mauricelargeron.com/wp-content/uploads/2012/12/8-tagManagerSuppCpte-310x202.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2012/12/8-tagManagerSuppCpte.jpg) Fig. 8 Application web "Gestionnaire de balises"

Enfin, soulignons 3  dernières possibilités dans Google analytics, le** tracking en temps réel du trafic sur les applications mobiles**, la construction de **raccourcis**, et le** partage de rapports** (segments) avec un utilisateur tiers.
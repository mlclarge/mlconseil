---
title: "Valeurs et Modèles d'attribution dans google analytics"
date: 2013-02-13
author: "admin"
categories: ["Google Analytics"]
tags: []
slug: "objectifs-et-valeurs-dans-l-analyse-daudience-web"
---

L’utilité de **Google analytics** comme outil de mesure de retour sur investissement ne se dément plus. Mais  quelles sont ces **notions de valeurs** que l’on peut retrouver au sein de cette application d’analyse d’audience ?  A la mise en route, GA est une coquille, presque vide ! En effet, souvent, l’entreprise utilise GA comme simple compteur de visites, c’est son usage basique. Mais l’analyse peut aller beaucoup plus loin ! Comment utiliser Google analytics comme outil pratique pour mesurer les efforts du service marketing fait en amont de la conversion ? Ces leviers e marketing sont nombreux, les plus souvent utilisés sont l’emailing, l’affiliation, les liens sponsorisés, le display. Je ferai quelques rappels dans une première partie sur les valeurs attachées aux micro et macro conversions, puis m’attacherai plus particulièrement ensuite à la chaine de valeur au travers des entonnoirs multicanaux et au poids de l’attribution de la conversion selon les différents canaux digitaux.

## Valeurs des Objectifs, interactions et e-commerce

En ce qui concerne les **objectifs**, Il faut indiquer à Google analytics les nœuds de **valeur d’un site** et y affecter un montant, c’est facultatif mais conseillé, sinon, comment valoriser ses résultats ? Ces objectifs, ou **micro - conversions** sont de trois ordres : une page de destination (après abonnement à une lettre newsletter), la durée de visite, le nombre de pages consultées par visite, ok.

[![parametrages-objectifs-dans-google-2-310x217.gif](/images/blog/parametrages-objectifs-dans-google-2-310x217.gif) Parametrages objectifs dans google

Au-delà de ces 3 aspects liés à la **fréquentation d’une page**, il est possible de mesurer ce qui se passe sur cette page, les **différentes interactions** de l’internaute avec le contenu par exemple : clics sur boutons, taux de remplissage d’un formulaire, téléchargements de documents, liens sortants, internes etc. On y peut y affecter également une valeur.

[![evenements-analytics-310x75.gif](/images/blog/evenements-analytics-310x75.gif) Evenements et valeurs dans GA

Pour les **valeurs de l’e-commerce**, il faut rajouter un code supplémentaire spécifique qui va récupérer les différentes valeurs du panier et les restituer sur une page de redirection (remerciement par exemple, une fois la transaction terminée). Bon, je ne m’appesantis pas sur le sujet ici. Une fois le code implémenté, notez les 2 valeurs que communique GA : le panier moyen, bon, rien à rajouter ici de particulier, tout bon commerçant connait son panier moyen (;)), la deuxième valeur indique **la valeur par visite**, un indicateur qui peut être pertinent pour l’élaboration de budget de campagnes (enchères liens sponsorisés) par exemple. Elle est calculée selon le montant des **transactions e-commerce** (CA) divisé par le nombre de visites, je préfèrerais le nombre de visiteurs uniques, plus pragmatique à mon goût. Même si un internaute ne laisse pas une valeur monétaire, cet indicateur en le segmentant (par source d'origine de  trafic)  aide à positionner ses objectifs marketing et commerciaux. Ce Kpi est aussi délivré pour les objectifs hors e-commerce pur. Quel levier apporte une valeur par visite la plus profitable finalement à mon business  ? Cette valeur répond à cette intérogation.

[![ecommerce-et-valeurs-310x111.gif](/images/blog/ecommerce-et-valeurs-310x111.gif) Valeurs :transactions et visite

**Ajout du 25/02 :** Il existe aussi une statistique intitulée **"valeur de la page**" . Cet indicateur donne la valeur d'une page  ou d'un ensemble de pages . Elle est égal à la valeur de la transaction de la page (si site ecommerce) plus la valeur totale des objectifs assignés à cette page , divisé par les nombre de page vues uniques.

## Attribution  de valeur au chemin de conversion (l’analyse multicanal)

Pour que cette catégorie de rapports fonctionne, il faut avoir défini au moins un objectif, ou alors installé le suivi de panier bien sûr.
Tout d’abord, je précise qu’ailleurs dans Google analytics, c’est-à-dire dans les rapports hors « entonnoirs multicanaux », si le dernier canal est d’origine directe, c’est le précédent qui remporte la mise. Pourquoi, et bien parce que :) . Si l’on souhaite sortir de cette logique du dernier arrivé, il conviendra de taguer les sources de trafic avec la variable _UTM : nooverride qui conservera le **cookie du premier point de contact.** Pour compliquer les choses, dans Adwords, il faut penser différemment, c’est toujours le premier clic sur une annonce adwords qui remporte le trophée même si la conversion intervient via un autre canal, plus tard,  à un autre moment. Donc surtout, ne pas mélanger les torchons et les serviettes !

Revenons à cette fonctionnalité multicanal. Elle sert à découvrir les différents points de contact qu’a eu le visiteur dans son **cheminement vers la conversion**. Précisons que cette analyse concerne les interactions avec les différents **canaux digitaux** enregistrés sur un seul appareil *(ordinateurs, tablettes ou mobiles)*. Ici, l’attribution de la conversion dans Google analytics est toujours donnée à la dernière interaction avant la conversion *(qu’elle soit d’origine directe ou pa*s).

Généralement, par défaut, les **leviers  standards** sont :

	- Résultats de recherche naturels

	- Accès directs

	- Liens commerciaux

	- Sites référents

	- Réseau social

	- Affiliation

GA donne ensuite, tous les chemins et leurs points de contacts respectifs qui ont amené à la conversion. On observera des points de contact, ou conversions indirectes, celles qui ne sont pas situées les dernières dans l’attribution, mais qui « ont contribué à ». Elles sont matérialisées par des rectangles en forme de flèches. Les attributions de la valeur de la transaction sont matérialisées par des formes rectangulaires.


L’outil de modélisation de l’attribution, fonctionnalité autrefois payante dans Google analytics, est désormais accessible sur demande. Cet outil permet justement de jouer sur l’attribution de la valeur affectée aux différents canaux. Selon sa stratégie marketing, par exemple, il est peut être utile de pondérer l’importance que chaque canal joue dans la répartition de la valeur générée par la conversion. Voici un modèle «passe partout » utilisé, celui qui donne une valeur au plus proche de la conversion.

[![modele-attribution-310x135.jpg](/images/blog/modele-attribution-310x135.jpg) Un des modèles d'attribution

Sinon, trois modèles comparés sont utilisables simultanément, dans l’illustration ci-dessous, les modèles « 1ere interaction », « Dépréciation dans le temps » et « Dernière interaction » passe la valeur des conversions de chaque canal au tamis.

[![modeles-attributions-analytics-310x136.gif](/images/blog/modeles-attributions-analytics-310x136.gif) Outil de modélisation

Voici un dernier exemple ‘imagé’ avec le chemin original ou la réflexion se fait sur une campagne de mots clés (Marque « brand » et générique « g ») , puis son affectation d’un modèle « linéaire » qui répartit uniformément le chiffre d’affaires, ou alors un modèle personnalisé ou la marque « B » est affectée d’une pondération minimale au profit des mots clés génériques ‘G’.

[![attribution-analytics-310x158.jpg](/images/blog/attribution-analytics-310x158.jpg) Attribtuion: Pondération de la marque

Pour résumer notre propos, nous avons pu donc appréhender les **différents niveaux de valeurs** possibles pour analyser un flot de clics, ceux pour les objectifs, les interactions, les transactions (of course) et enfin,  les canaux d’acquisition.
---
title: "Panel d'indicateurs d'analyse référencement pour son blog"
date: 2012-01-26
author: "admin"
categories: ["Google Analytics"]
tags: []
slug: "initiation-statistiques-referencement-dans-google-analytics"
---

Après avoir parcouru  la semaine dernière les tenants et aboutissants de [l’analyse multicanal](https://www.mauricelargeron.com/guide-entonnoirs-multicanaux/), je reste aujourd’hui dans le sujet de l’audit de site avec l’outil Google Analytics et vais aborder les principaux indicateurs (pour en savoir plus : kpi) à utiliser dans le cadre d’une optimisation pour les  moteurs de recherche. Je prendrai pour illustration ici le cas d’un site d’une association de défense contre l’excision. Son objectif est de diffuser un message et de fidéliser son audience.

Il convient au préalable de lier son compte Google webmaster tools  avec son compte analytics afin d’avoir toutes les données centralisées  sur une seule et même plateforme. Le sésame ici de l’analyse reste le « **mot clé **» car c’est la donnée que le référenceur, le propriétaire de site va pouvoir utiliser pour monitorer la thématique de sa présence web . Je vais passer en revue dans premier temps, la catégorie « **Sources de trafic** » *(depuis le menu de Google Analytics)*  avec les principales données liées au travail d’optimisation , puis donnerai **une liste de Kpi** orientée e-commerce, et finirai par énoncer d'autres **astuces** pour analyser son audience avec une optique référencement.

## Source du trafic 

Vue d'ensemble
Google analytics fait déjà tout le travail pour vous, puisque, sans aucun paramétrage, il vous donne via le menu  «  Vue d’ensemble » la provenance du trafic   avec des données axées autour de 3 critères ou dimensions :

1/ Trafic de recherche (voir  fig.1 - 1)

	- **Mots clés** (Activé par défaut), liste les 10 principaux mots clés qui amènent des visites

	- **Requête de rech. Avec correspondance** : quelle recherche enclenche l’affichage d’une de vos annonces si vous effectuez une campagne adwords (sinon « not set » est indiqué)

	- **Source** : les moteurs de recherche qui envoient le trafic  (ici Google 96% !)

2/ Site référents (voir  fig.1 - 2)

	- **Source backlinks**  : les sites qui font un lien vers votre site , ici 11 visites sont générées par Facebook, le référent le plus fort !

3/ Accès direct  (voir  fig.1 - 3)

	- **Page de destination** : les internautes accèdent directement depuis leurs navigateurs en tapant l’adresse du site ou en cliquant sur un favori. Ici, 28 % vont atterrissent directement sur la page d’accueil mentionnée avec un "/".

[![Image](/images/blog/analytics-sources-trafic1-300x195.png)](https://www.mauricelargeron.com/wp-content/uploads/2012/01/analytics-sources-trafic1.png) Fig.1 Indicateurs " Vue d'ensemble" | G. Analytics

Sources

Ce chapitre ici détaille numériquement les statistiques agrégées citées plus haut  en donnant :

	- **Tout le trafic**  que l’on peut segmenter selon ces besoins. Exemple : Je m’aperçois que le site d’information  cité en exemple ici est retrouvé par le terme « excision » un des sujets traités mais pas le seul par le blog :( , je souhaite évaluer l’impact global de ce terme sur l’ensemble des visites. Je vais donc créer un segment personnalisé sur ce mot clé qui va trier sur les mots clés celui qui contient les trois premières lettres du terme « excision » soit «** exc **» (voir Fig. 2)

[![Image](/images/blog/segment-personnalise-300x150.png)](https://www.mauricelargeron.com/wp-content/uploads/2012/01/segment-personnalise.png) Création segment personnalisé

Une fois ce segment crée, j’indique sous l’onglet** rapport standard** que je souhaite afficher le rapport « toutes les visites » avec  «** impact du mot clé excision **».

[![Image](/images/blog/segment-personnalise2-300x81.png)](https://www.mauricelargeron.com/wp-content/uploads/2012/01/segment-personnalise2.png) Affichage de 2 segments (std & perso)

Je m’aperçois que **62.5 % du total des visites est impacté par ce terme de recherche ***(Soit 475 visites sur 760)*. Je peux affiner ensuite selon les moteurs de recherche, en cliquant sur  le plus influent et j’obtiens ensuite son « poids » dans la provenance de ces visites (86%). Le taux de rebond ici est très élevé (+80 %),  corrélé au temps passé sur la page, cela indique certainement que les internautes ne trouvent pas ce qu’ils recherchent.

[![Image](/images/blog/contexte-impact-analytics-300x216.png)](https://www.mauricelargeron.com/wp-content/uploads/2012/01/contexte-impact-analytics.png) Contextualisation sur impact d'1 mot clé

**Site référent (popularité du site)**

Ce lien donne par défaut des stats.  déjà vues en agrégées depuis Source de trafic > Vue d’ensemble.  Cependant, il peut être judicieux de connaître les pages de destination que réfèrent mes sites partenaires, avec le % de chacun. Ici, seule la page d’accueil, mentionnée avec un « / »  représente l’essentiel  de mes liens entrants *(ces derniers composent  l’indice de popularité pour Google, un lien vers un site= 1 vote)*. En revanche, sur les données standard données par analytics (*visites, pages par visites=, temps moyen passé sur le site, taux de rebond)*, je constate que ces liens apportent un trafic qui semble qualitatif au regard du taux de rebond très faible (26%) et du temps passé sur le site *(187% supérieur à la moyenne)*. Dans ma stratégie Seo *(Search engine optimization ou référencement)*, il est clair que je dois renforcer mes efforts sur ce canal afin d’améliorer ce 4% du total des visites !

[![Image](/images/blog/site-referent-300x185.png)](https://www.mauricelargeron.com/wp-content/uploads/2012/01/site-referent.png) Analyse qualitative des sites référents

**Recherche **

On revient ici sur les requêtes tapées par les internautes. Il faut choisir **selon ces besoins des critères** pour aller plus loin dans l’analyse. Ci-dessous, je mets en parallèle le mot clé (sans regroupement), sa page de destination, les visites  et  le temps passé sur le site. Intéressant à noter que le second terme de recherche est celui du nom de l’association, le temps passé par ces internautes est 3 fois supérieur à celui qui tape le terme générique de sa recherche.

[![Image](/images/blog/resultatnaturels-300x205.png)](https://www.mauricelargeron.com/wp-content/uploads/2012/01/resultatnaturels.png) Perspective: Mos clés -> page destination
### Optimisation pour le référencement

Optimisation pour le référencement, rentrons dans le vif du sujet ! *(association avec Google Webmaster Tools) les 1000 et 1 nuit du référenceur ! . *Les rapports donnés sur l’optimisation du référencement utilisent **4 statistiques** issus de la recherche sur le moteur de recherche Google :** Les impressions, les clics, position moyenne de ces liens et le ctr (taux de clics /impressions) en pourcentage.**
Ce modèle est emprunté au modèle du programme adwords. Donc pour ceux qui y sont familier… ;)

	- **Requêtes**

Nous avons ici plus de profondeur que les données précédentes, puisque dans une certaine mesure *(1000 principales requêtes quotidiennes)* Google fait remonter les **termes de recherche**, et les urls du site qui se sont affichées, les clics  effectués, et la position moyenne sur la page (calcul de moyenne entre des positions différentes sur des requêtes différentes pour 1 url). Les 4 statistiques peuvent être choisies selon ces besoins. Ici, sur les requêtes effectuées, les chiffres sont plutôt bons  (CTR de 25%) !

[![Image](/images/blog/1000-requetes-analytics-300x192.png)](https://www.mauricelargeron.com/wp-content/uploads/2012/01/1000-requetes-analytics.png) 1000 principales requêtes internautes

	- **Pages de destination**

Ce rapport indique les 1000 premières pages  *(limite de 1000 urls uniques)* quotidiennes. Pour les petits sites, les pages sont comptées par impression. Il est  utile pour juger du trafic global du site et ainsi d’améliorer la position de certaines pages. Ici la page d’accueil  n’est pas celle qui obtient le plus de succès !

[![Image](/images/blog/pages-1000-300x188.png)](https://www.mauricelargeron.com/wp-content/uploads/2012/01/pages-1000.png) 1000 premières pages du Blog
Autres Suggestions segmentations et indicateurs

	- **Segmentation avancée : Travailler sa longue traîne**

Des requêtes peuvent contenir 5, 6,7 mots auxquelles il est difficile de penser, comment les retrouver dans ces rapports ? L’utilisation d’expressions régulières est là pour ça. Ici, j’ai utilisé une syntaxe qui permet de compter  5 espaces entre chaque mot soit 6 mots au total

^(+ ){5}+$

[![Image](/images/blog/regex1-300x202.png)](https://www.mauricelargeron.com/wp-content/uploads/2012/01/regex1.png) Expression régulière : tri sur longueur requêtes

	- **Segmentation avancée : Travailler les liens profonds de page**

Même cause, même effet avec cette expression :   ^/(+/){2}*$ . Elle nous donne la profondeur de la page de destination, ici, réglé à un chemin dont la profondeur est égale à 2 répertoires.

[![Image](/images/blog/profondeur-liens-Pages-300x175.png)](https://www.mauricelargeron.com/wp-content/uploads/2012/01/profondeur-liens-Pages.png) Exp. régul. : Liens sur pages pronfondes

	- **Cheminement par mots clés** : flux de visiteur par mots clés du  trafic naturel. Une autre vision du comportement des visiteurs et des interactions selon les requêtes de départ.

[![Image](/images/blog/flux-analytics-300x174.png)](https://www.mauricelargeron.com/wp-content/uploads/2012/01/flux-analytics.png) Cheminement selon mots clés entrants

	- **Liste non exhaustive de KPI** ...

A connotation commerciale, avec paramétrages de conversions/ objectifs au préalable *(panier, formulaire, inscription…).*

	- Profits générés depuis recherche naturelle

	- Trafic visites selon Mots clés de la Marque et/ou  Mots clés générique

	- Statut du visiteur (1ere visite ou visiteur fidèle) selon mots clés et conversion (avec Marque/ ou sans)

	- % Trafic naturel & trafic liens sponsorises (rapport)

	- Indicateurs (ex : progression trafic naturel)  avec comparatifs temporels (mois, année, saison.)

	- Regroupement sémantique (thématique mots clés)

	- Provenance géographique des visiteurs par mots clés (recherche locale)

	- % des mots clés cours / mots clés long (travail longue traîne)

	- Mots clés et position dans entonnoir de conversion (retargeting)

	- Nombre moyen de mots clés par page de destination

	- Tx de conversion par mots clés (page de destination) etc....

Recherche sur le site & Analyse des pages web

	- **Recherches internes au site **

Si l'on souhaite connaître ce que recherche réellement le visiteur sur ce blog, il est possible d'installer un moteur de recherche interne et ainsi récupérer une liste des requêtes. Cela permet ensuite de pouvoir adapter parfois le contenu au lecteur.

[![Image](/images/blog/termeRecherche-300x201.png)](https://www.mauricelargeron.com/wp-content/uploads/2012/01/termeRecherche.png) Recherches interne au site

	- **Analyse des pages Web**

Utile pour avoir une idée sur la **bonne ou mauvaise ergonomie de son site**. Les menus de navigation  incitent-ils les internautes à aller voir les contenus que je souhaite mettre en avant ?  Quelles sont les relations à établir avec les flux visiteurs* (précédemment évoqués avec ces "ruptures" dans les intéractions)*, les **taux de rebond** ?

[![Image](/images/blog/analyse-page-web-300x152.png)](https://www.mauricelargeron.com/wp-content/uploads/2012/01/analyse-page-web.png) Tx de clic sur page accueil

Mais il ne faut pas se méprendre sur ces Kpi, indicateurs et rapports  car  seule** la stratégie et les objectifs de départ** fixeront les données d'une bonne analyse Seo.
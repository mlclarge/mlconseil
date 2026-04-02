---
title: "Solutions pour démasquer le not provided"
date: 2012-08-29
author: "admin"
categories: ["Google Analytics"]
tags: []
slug: "not-provided-dans-google-analytics"
---

Dévoilons le «** not provided **» de Google analytics .  Petit rappel : cet item « not-provided »  figure dans  les statistiques  au niveau des **sources de trafic**, dans la rubrique **recherche naturelle**.  Cette dernière est censée  faire remonter  la liste de mots clés tapés par l’internaute dans le moteur de recherche Google. Sauf que depuis octobre 2011, le géant de la recherche ne fournit plus dans un certain quota, qui peut varier de 10% à 68%,  les mots clés  du visiteur identifié (https://)  . Donc difficile de savoir quels sont les sésames qui amènent votre trafic sous ce label « not provided ».  La  proportion des visiteurs logués ne cessent de croitre, les internautes s’identifient  de plus en plus (messagerie, réseaux sociaux..), les navigateurs implémentent par défaut le protocole sécurisé (Firefox depuis juillet 2012). Qui plus est, Google teste actuellement des listes  de résultats avec 7  liens organiques *(selon les requêtes bien sûr, au lieu de 10 voir plus parfois)*,  le monde du Seo  n’est pas à la fête et va donc devoir s’adapter !  Voici donc quelques solutions pour tenter de combler ce vide de données, dans Google analytics d’une part, puis avec l’aide d’outils complémentaires d'autre part, et enfin, en utilisant d’autres parades pour dévoiler ces sacrés mots clés.

## **Provided or not provided dans Google analytics ?**

Une première solution est de rapprocher la colonne** mot clé** avec le  « not-provided » avec la **page de destination** et ainsi avoir un champ lexical complet qui donne  la tonalité de la recherche cachée Fig .1.

[![Fig.-1-Google-Analytics-not-provided-300x216.png](/images/blog/Fig.-1-Google-Analytics-not-provided-300x216.png) Fig. 1 Correler NP et Urls de destination

Puis ensuite isoler l'url qui reçoit le plus de visites pour être représentatif en utilisant un** filtre avanc**é « Fig 2.

[![Fig.-2-GoogleAnalytics-tri-mots-cles-300x136.png](/images/blog/Fig.-2-GoogleAnalytics-tri-mots-cles-300x136.png) Fig. 2 G.A Tri des Urls principales

Cela vous donne la liste des mots clés qui ont aboutis sur cette page (url) Fig 3.

[![Fig.-3-not-provided-300x104.png](/images/blog/Fig.-3-not-provided-300x104.png) Fig 3 NP et Mots clés sur 1 même PD

Voici la même manipulation, mais effectué à partir de la page de destination, voir processus Fig 4.


Une autre façon est de procéder par élimination par **typologie de mots-clés**, les mots clés de la **marque** et les autres. Généralement, la marque aboutit à la page d’accueil, donc le but ici est de faire un tri de tous les mots clés qui amènent à la page d’accueil , le « not-provided » sera ainsi dénombré et identifié comme celui relié directement au nom de la marque, de l’enseigne Fig. 5.

[![Fig.-5-Extraction-page-accueil-300x109.png](/images/blog/Fig.-5-Extraction-page-accueil-300x109.png) Fig. 5 Extraction de la page d'accueil

Insérer un **moteur de recherche interne** sur son site est aussi une alternative.  L’idée ici d’oublier la donnée « non disponible » et de cerner ce que réellement cherche le visiteur (fig.6 ).

[![Fig.-6-moteur-de-recherche-300x287.png](/images/blog/Fig.-6-moteur-de-recherche-300x287.png) Fig. 5 Installer un moteur de recherche interne (source Havinash Kaushik)
## **Outils complémentaires pour analyser le « Not Provided »**

Votre hébergeur possède lui aussi des données de fréquentation, gratuites, il suffit d’y accéder ! Même si la précision parfois n’est pas au rendez-vous, la tendance est donnée, et c’est avant tout l’essentiel pour garder le cap sur le couple **thématique-visibilité** Fig. 7.

[![Fig.-7-LogHebergeurs-300x284.png](/images/blog/Fig.-7-LogHebergeurs-300x284.png) Fig. 7 Statistiques hébergeurs

Une nouvelle fois, sortons du sacro-saint cadre **mot-clé/url** et pensons plus large. Les moteurs Bing/Yahoo, même si peu utilisés en France, fournissent  des données en « clair », ici aussi, l’objectif est d’avoir la ** tendance des requêtes** pour lesquelles un site est positionné Fig. 8.

[![Fig.-8-bing-300x148.png](/images/blog/Fig.-8-bing-300x148.png) Fig. 8 Elargir le débat avec Bing  !

Pour finir cette partie sur les **outils gratuits**, je n’oublie pas l’interface de **Google webmaster tool**, qui est l’équivalent du suivi des fichiers d’un hébergeur mais avec des données plus précises. Je préfère consulter GWT en natif, que depuis G.A, l’analyse est plus fouillée. Les données sont ici échantillonnées et agrégées  (2000 impressions/jour) mais très pertinentes pour** saisir les intentions de recherche** du moment. On identifie les urls  les plus populaires et une liste de mots clés y est automatiquement liée, pas mal non Fig. 9 ?

[![Fig.-9-Gwt-300x225.png](/images/blog/Fig.-9-Gwt-300x225.png) Fig. 9 GWT un outil très utile
## Autres parades anti "not provided"

### Un filtre relié à la variable de campagne..

Mise à jour : je remercie Carrie Hill pour son partage d'un filtre, qui permet d'y voir plus claire quant aux urls touchées par le "not provided. Il vaut mieux isoler ce filtre dans un profil distinct  par précaution. Voilà ce que donne les données **sans filtre** :
[![not-provided-filter-310x85.gif](/images/blog/not-provided-filter-310x85.gif)

Son principe est simple, le tag 'not provided' est associé à un terme ne campagne, donc on l'isole dans un filtre de champ A "terme de campagne" puis dans un champ B on récupère l'URI et l'on construit l'url finale en précisant le np (pour not provided) à mettre devant pour distinction dans le rapport.
Récap :
Champ A -> Extrait A T Cgne : (not provided)
Champ B -> Extrait B URI de la demande : (.*)
Sortie vers -> Constructeur Valeurs personnalisées   np $B1

Les mêmes données passées au filtre...

[![not-provided-filter-1-310x165.gif](/images/blog/not-provided-filter-1-310x165.gif)

Ensuite il existe  d’autres outils de monitoring de positionnement qui permettent d’**évaluer le positionnement** d’une page par rapport à une **liste de mots clés**. Par déduction, si pour un mot clé donné, aucune page n’apparaît dans les principaux moteurs de recherche, sûr que ces derniers ne figurent pas dans le "not provided" ;) . Exemple ici avec la solution **Rank Tracker** fig. 10 .

[![Fig.-10-Seo-Tracker-300x32.png](/images/blog/Fig.-10-Seo-Tracker-300x32.png) Fig. 10 Visibilité de mots clés cibles dans les moteurs

Enfin, il est aussi possible grâce à la manipulation de liste de mots clés et à son **classement en catégories **, ou en sous-ensembles depuis une extraction de google analytics de faire des rapprochements lexicaux, lire la deuxième partie de cette article : [Keyword Research Using Categories to Make Your Process More Actionable](http://www.seomoz.org/blog/keyword-research-using-categories) (anglais) sur ce procédé.
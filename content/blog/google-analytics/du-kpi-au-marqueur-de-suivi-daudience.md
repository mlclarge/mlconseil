---
title: "Du Kpi au marqueur technique de suivi d'audience"
date: 2016-10-24
author: "admin"
categories: ["Google Analytics"]
tags: []
slug: "du-kpi-au-marqueur-de-suivi-daudience"
image: "/images/blog/PLAN-DE-MARQUAGE-TECHNIQUE.jpg"
---

Passons au **[plan de taguage "technique](https://www.1min30.com/dictionnaire-du-web/plan-de-marquage-taggage)"** consacré au marquage des différents kpis que l’on souhaite mesurer sur un site web après avoir vu le plan de [**marquage marketing**](https://www.mauricelargeron.com/pre-requis-avant-le-marquage-technique-dun-site-web/) .  J'ai scindé en 2 posts afin de marquer les 2 approches possibles. Nous prendrons en toile de fond ici, un plan qui utilise les outils de Google, soit Google analytics Universal à l'aide éventuellement de son gestionnaire de balises.

## **Préparer le(s) site(s) web et la solution de tracking à son plan marketing**

### ***Périmètre du champ de collecte***

Plusieurs domaines, sous domaines, applications font peut être parties des zones de collecte. Cela aura des répercussions sur les méthodes de tracking. Le tracker devra être paramétré pour permettre un **suivi multi domaine**, les formulaires, les iframes seront les objets à suivre de près et notamment avec le suivi des cookies inter-domaines. Les **paramètres de session** devront être passés d’un site web à l’autre appartenant à une même entité. Au-delà de cet aspect, n’oublions pas la gouvernance pour l’accès aux rapports qui impliquera fortement la configuration du compte Google analytics afin de fournir la bonne data aux parties prenantes. La gestion des utilisateurs et la fonctionnalité Rolling up (disponible sur analytics premium/360) facilite grandement les accès et  l’agrégation de différents comptes UA.

### *Choix de la solution de suivi *

Comme indiqué dans le choix d’une solution comme celle de **Google analytics** associé au gestionnaire de balises, des réglages seront nécessaires. Une  partie de ces paramétrages passera dans l’admin de l’interface de GA, et  sur la plateforme de Google Tag Manager. Pour illustrer, **les dimensions personnalisées** sont à déclarer dans ga afin d’avoir la lecture de ceux-ci dans les rapports, mais doivent aussi être déclaré dans le tag principal de GTM

### *Donnée de l’organisation et impératif de la librairie JS*

Selon le plan de marquage d’audience marketing, et le niveau de personnalisation de la mesure d’audience, une segmentation claire des besoins est toujours la bienvenue. Au-delà de Google analytics et  selon les souhaits de l’équipe marketing, de ventes, il sera nécessaire de sortir de la solution et d’utiliser des marqueurs tiers mais qui ne seront pas directement traités et collectés par GA. Exemple : les pixels de e-marketing, les collecteurs intelligents de visiteurs non logués, l’enregistrement de sessions etc…

[![plan-marquage-web-analytics-282x300.jpg](/images/blog/plan-marquage-web-analytics-282x300.jpg) plan marquage web analytics

**Data métier** : Quel est le référentiel (s’il existe) de l’organisation pour mettre en adéquation les libellés des indicateurs de la solution de tracking choisie ? Le back office donc de l’organisation doit être impérativement scanné des valeurs que l’on souhaite remonter. L’adéquation avec le service d’information interne de l’entreprise, **crm, database et la nomenclature des données** : choix, libellé, valeur devront être homogénéiser avec la solution de web analytics. La solution d’un TMS comme Google tag manager , va impliquer la pause d’un dataLayer, solution pérenne de marquage personnalisé. Ce collecteur de data servira de « zone neutre » entre l’api du site web (cms, standalone, site ecommerce prêt à l’emploi) et Google analytics.

 	- Audience : Si le cross device est nécessaire, alors une implémentation de l’**user-Id **sera obligatoire, cet id sera celui généré par le SI interne de l’organisation et non identifiable. Il pourra s’appuyer sur l’id d’une table visiteurs authentifié ou alors être aléatoire et généré lors de la session.

 	- Acquisition : Au-delà des indicateurs standards, quel référentiel pour le  **libellé des canaux** d’acquisition ? Au-delà des libellés par défaut de GA défini par le système  (organic, référents, direct..), une personnalisation utilisateur pour coller à l’exigence du service marketing est impérative.

 	- Interaction : la remontée des marqueurs sur la collecte comportementale nécessite d’utiliser les **modèles de data** de la librairie JavaScript de la solution choisie, ici, celle de GA sans oublier celles reliés aux Api externes (boutons sociaux par exemple). Exemple du suivi de clics personnalisé avec les ‘évènements ‘ :

 	- Conversion : le suivi du **tunnel de conversion**, le tunnel d’achat, les transactions vont réclamer des ajustements dans la présentation native du site web pour présenter la data aux différents collecteurs (cheminement, abandon, mise au panier, règlement sur plateforme de paiement).

 	- Automatisation/Big Data : En terme de **conquête ou de fidélisation,** les marqueurs devront ils enclencher des routines automatisées sur le visiteur (ex :si montant du panier > 100 , relance automatique). Y va-t-il des impératifs quant à la stratégie d’analyse des data ? Pour des sites à fort traffic, une liaison avec des infrastructures big data sera sans doute nécessaire.

## **Un site web bien codé au service des marqueurs **

### ***Les data métier : exemple du suivi ecommerce***

Côté solution de tracking, soit le tracker standard fera l’affaire, soit l’ajout d’un plugin dédié à ce type de data sera nécessaire. Pour illustrer, la tracking ecommerce standard requiert une phase de développement côté site pour présenter les variables produits et de transaction sur la page de destination. De même, pour le suivi améliorer du tunnel de vente, un plugin GA supplémentaire devra être intégrer dans le site.

La data à collecter est-elle présente en front sur le site web ? Sinon, prévoir une phase de développement dans l’api du CMS par exemple, ou l’usage d’un plugin prêt à l’emploi pour faire remonter et présenter la data à collecter.

Sans GTM, Une passation de la data pourra se faire traditionnellement en php pour la présenter sur la page de remerciement, avec extraction des différents attributs et intégration dans le script JS de GA. Ou alors, dans le cadre de GTM. la construction d’un dataLayer, container de variables, sera mise à disposition relié au déclenchement de ce dataLayer.

### ***Les data côté client***

C’est souvent un peu le nerf de la guerre, on s’aperçoit que le balisage html n’est pas assez explicite ou trop générique, du coup, les marqueurs ne peuvent pas  capable d’identifier la valeur des variables à remonter.  Les attributs de différents objets sur la page doivent être en rapport avec les exigences du marqueur de la solution : div, liens, images, documents, coordonnées, formulaires.

[![un-code-source-bien-propre-310x139.jpg](/images/blog/un-code-source-bien-propre-310x139.jpg) un code source bien propre

Bref dans l’idéal les objets d’une page devront avoir au moins un des ces 4 attributs :

 	- Un id

 	- Une Classe

 	- Un nom

 	- Une action

## **Un plan de marquage pour assurer un suivi pérenne**

Peu importe le format, que ce soit un powerpoint, un fichier excel, un drive Google. L’idée ici, est d’avoir un récapitulatif le plus exhaustif possible des marqueurs par grandes zones de collecte. Il n’existe pas de norme ou de standard donc chacun y va selon ses propres besoins internes.

[![plan-marquage-api-externe-310x178.jpg](/images/blog/plan-marquage-api-externe-310x178.jpg) Extrait plan marquage pour service externe

Enfin, notons que la popularité des Tag management system et leur facilité d’usage implique néanmoins une rigueur dans l’implémentation des marqueurs. Principalement notons 3 pratiques bienveillantes classiques :

 	- Prendre garde aux conflits de librairies JS

 	- Avoir conscience de l’ordre du chargement des différents écouteurs JS

 	- Eviter de s’appuyer sur les éléments du DOM, l’usage du dataLayer est agnostique des changements de design du  template et est donc à ce titre plus pérenne.
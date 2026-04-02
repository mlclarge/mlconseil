---
title: "Enrichir l'analyse digitale de ses ventes online"
date: 2013-10-03
author: "admin"
categories: ["Apprendre Google Ads"]
tags: []
slug: "offline-et-online-rassembles-dans-une-campagne-publicitaire"
---

Google Adwords joue le modèle gagnant gagnant ! Je te donne 1 donnée supplémentaire, et tu me diras ce qui se passe en dehors de la plateforme Adwords. L’idée est séduisante, et se place dans le droit fil des dernières améliorations apportées à la qualité du reporting de campagne. Je pense notamment à :

	- L’identification du positionnement des urls dans les serp naturels de Google et de leur corrélation avec les mots clés achetés (Adwords > Variables > Liens commerciaux et recherche naturelle)

	- La remontée dans Google Analytics des données de coûts Adwords  (conversion > attribution)

	- La collectée des données dîtes de campagnes universelles dans GA (Sources de trafic  > ajustement des enchères)

L’avantage est d’apporter plus de champ (« incorporer» du offline dans du « online ») et par la même d’apporter un  recul dans l’analyse des conversions  dans Adwords  afin de pouvoir arbitrer ses campagnes au plus juste.  Comment ? Par des actions menées à partir d’outils comme les stratégies d’enchères flexibles, les règles automatiques, les ajustements d’enchères par type d’appareils,  la personnalisation des formats d’annonces (via les extensions planifiées selon les horaires etc).

## **Le principe des remontées Offline vers online**

### **Processus de remontée des conversions**

Alors qu’en est-il précisément de cette nouvelle fonctionnalité ?  Comment l’intégrer dans son propre système d'information ?

Résumons le procédé. La plateforme Adwords génère un identifiant unique collecté lors du remplissage d’un formulaire de demande de contact effectué par un internaute. Cet ID est remonté via un champ caché au moment de l’envoi du message, puis collecté dans l’application de gestion de la relation client, plus communément appelé CRM (Customer Relationship Management). Un suivi commercial est opéré avec une conversion générée (ou non). Si  oui, elle est importée dans Adwords  et ainsi permet un reporting, une analyse et enfin un arbitrage pour optimiser la campagne.

[![Image](/images/blog/process-adwords_online-310x219.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2013/09/process-adwords_online.jpg) Les étapes du processus de collecte des conversions
### **Cas d’utilisations **

Les situations d’usages peuvent varier selon la situation de l’annonceur. Le cas présenté ci-dessus fait apparaître une situation commune de rappel téléphonique après un lead généré en ligne.  Mais d’autres cas peuvent se présenter.

	- Pallier à un problème technique de remontée des conversions

	- Ciblage dans le type de vente occasionnée (second achat ou  nouveau client seulement)

	- Corriger les ventes annulées

	- Elargir les conversions intervenues au-delà des 30 jours (maxi 90 jours)

## **Intégration technique pour la collecte de l’ID Adwords **

### **Elaboration de la collecte en 4 étapes **

[![Image](/images/blog/offline-to-online-310x90.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2013/09/offline-to-online.jpg) Les étapes d'intégration du tracking
**1/ Dans Adwords,  2 éléments à paramétrer : suivi et importation**

	- Il faut activer le suivi automatique des campagnes, cela va générer pour chaque clic d’annonce un paramètre Gclid (id).

	- Il faut créer les conditions pour préparer l’importation des conversions offline,  soit aller dans Adwords > conversions > créer une conversion de type « import »

[![Image](/images/blog/conversion-adwords-310x140.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2013/09/conversion-adwords.jpg) Interface adwords pour l'import des conversions
**2/ Sur le CRM  avec API sur Adwords pour intégration du Gclid**

	- Il faut créer l’environnement pour recevoir ce cookie Adwords.  Selon les éditeurs de solutions, les méthodes diffèrent, mais le principe reste identique. Les CRM doivent en amont pourvoir leur API d’une fonction qui intègrera ce cookie Adwords.  Il faut ensuite  créer un champ nouveau adapté à la fiche prospect et  lui affecter la  fonction appropriée.

	- Un mappage entre ce nouveau champ Gclid et celui du formulaire (voir ci-après) sur le site permettre l’alimentation de ce fameux Id !

**3/ Sur le site web : pose du cookie et transfert via formulaire**

	- **Taguer toute les pages d’un code Js** (exemple ici donné par Google),  côté client ici donc, qui va créer un cookie pour stocker sa valeur dans le navigateur de l’internaute.

[![Image](/images/blog/code-1.jpg)](/images/blog/code-1.jpg) Code pour créer un cookie à poser sur toute les pages

	- **Créer une page formulaire** (par exemple comme une page contact) avec un champ caché  (invisible pour le visiteur) pour recevoir la valeur du cookie stockée sur le navigateur, pour ensuite la transmettre à une application de gestion client (CRM).

[![Image](/images/blog/code-3.jpg)](/images/blog/code-3.jpg) Code pour le champ caché inséré dans le formulaire

	-  Cette collecte doit se faire par l’ajout d’un code Js qui va récupérer la valeur du cookie (Gclid).

[![Image](/images/blog/code-2.jpg)](/images/blog/code-2.jpg) Récupératioin de la valeur du cookie

**4/ Importation dans Adwords depuis une feuille .csv  dédiée**

Une fois les données remontées dans le CRM, le mapping entre gclid et le suivi de la fiche prospect  et la conversion accomplie, il conviendra de l’importer dans Adwords via un fichier .csv constitué de prévue à cette effet. Elle peut être créer manuellement ou généré par le CRM. Aucune donnée nominative et personnelle n’est concernée ici.

[![Image](/images/blog/excel-import-adwords-2-310x142.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2013/09/excel-import-adwords-2.jpg) Fichier  type ".csv"  à importer dans Adwords (fake)

Noter ces éléments importants :

	- Pas de conversion datant de plus de 90 jours

	- Si 2 conversions identiques (même gclid), 1 seule est importée (pour le même clic)

	- Si 2 conversions de même type, mais heure différentes, 2 conversions peuvent être importées.

	- Un état est généré lors de l’import : échec, nombre, réussite..

	- Attendre quelques heures (3) avant mise à jour

Cette solution n’est qu’un début assure Google adwords,  des améliorations sont à venir sous peu, alors patientons !

**Quelques petits liens **

	- Blogspot avec extraits du code : [http://adwords.blogspot.fr/2013/09/measure-optimize-for-offline-sales-with.html](http://adwords.blogspot.fr/2013/09/measure-optimize-for-offline-sales-with.html)

	- Web-to-lead Salesforce : pour l'idée [http://www.shellblack.com/salesforce/marketing/web-to-lead/](http://www.shellblack.com/salesforce/marketing/web-to-lead/)
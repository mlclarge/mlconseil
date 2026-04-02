---
title: "Regles de flux dans google merchant center (google shopping)"
date: 2019-04-29
author: "admin"
categories: ["google shopping"]
tags: []
slug: "regles-de-flux-dans-google-merchant-center"
image: "/images/blog/gestioinnaire-flux-gmc.jpg"
---

Un petit tuto sur  le gestionnaire des **règles de flux de Google Merchant center**. GMC est la plateforme qui permet de formater les catalogues produits des commerçants afin de l’adapter à sa plateforme [**Google shopping**](https://shopping.google.fr/). Bien souvent, les vendeurs en ligne optent pour des plateformes externes spécialisées dans la gestion multiple des flux sources pour leur adaptation sur des sites de Marketplace, comparateurs de prix (type shopping feed par exemple). Bon si vous souhaitez ne pas utiliser ce genre de plateforme,  qui prend bien sûr au passage un % du CA, vous pouvez directement utiliser,  dans le cas ici du levier Google shopping,  GMC. Cette plateforme possède un outil de rectification du flux source pour l’adapter à ses exigences de formats d’annonces sur son moteur de recherche.  On fait un petit focus aujourd’hui dessus, cela peut toujours dépanner….même si ce n'est pas [un cours magistral sur google ads](https://www.mauricelargeron.com/formation-google-ads/)
[![Image](/images/blog/ecosysteme-google-shopping.jpg)](/images/blog/ecosysteme-google-shopping.jpg) Ecosysteme google shopping
## **Deux sortes d’opérations  que peut faire l’outil des règles de flux**

Pour faire simple, un flux c’est ni plus ni moins qu’un tableur avec des lignes et des colonnes, les entêtes de colonne sont des attributs, chaque ligne est égal à un produit muni de ces attributs qui correspondent à des valeurs (données). Le gestionnaire par des fonctions énumérées ci-dessous va jongler avec les valeurs de chaque  attribut pour les affecter là où le souhaite le gestionnaire de campagne pour préparer le flux pour Google Ads.
[![Image](/images/blog/flux-produit.jpg)](/images/blog/flux-produit.jpg) Exemple Flux produit avec attribut (colonne) et valeurs (données par lignes)
### ***1/ Opérations relatives aux sources de données***

*Principalement je vous parle de l'option « **Définir sur**** »***   par exemple permet de renseigner un attribut cible avec une combinaison de valeurs statiques et de colonnes entrantes, depuis les flux principaux ou supplémentaires. Vous pouvez ainsi ajouter des données produits existantes et les enrichir de valeurs supplémentaires. **Exemple : ajouter une marque à un titre. **

**D’autres opérations sont possibles comme :**

- L’opérateur "Définir sur 'Multiples'"

- L’option "Extraire"

- "Sélectionner le plus récent"

### ***2/ Les modifications des données des attributs ***

Elles permettent d'ajouter des étapes et de changer des données pour un attribut spécifique. Utilisez les conditions et les opérations de modification pour optimiser des  données. Par exemple, **modifier certains mots dans le titre** de votre produit ou mettre à jour des  données pour répondre aux spécifications des données produit.

Sinon 8 modifications sont gérables comme

- "Ajouter un préfixe"

- "Ajouter"

- "Standardiser"

- "Ajouter un champ répété"

- "Rechercher et remplacer"

- "Calculer"

- "Séparer et sélectionner"

- "Effacer"

## Avantages et inconvénients de l’outil règles de flux

### ***Les points positifs***

- Une solution gratuite intégrée

- Une gamme de règles/possibilités de plus en plus puissante avec une interface qui évite de mettre la main dans des syntaxes compliquées

### ***Les points négatifs de l’outil***

- Un temps de traitement un peu long

- Incompatibilité avec  l’API shopping

- Des fonctions qui restent aussi limitées parfois lors de scénarios avancés

## **Tuto manipulation du flux **

Cas :**Modification d’un custom label**

Ou "étiquette personnalisée"pour **segmenter un flux produits** selon des valeurs business de l’entreprise) existantes (ici  #tag sur « soldes hiver/printemps »)   et la remplacer par "soldes printemps 2019" dans une catégorie produit personnalisée (type_de_produit ou product_type ou  nommé "catégorie" en vert dans GMC)

- 1 : Mon flux source, ici sur Google drive

[![Image](/images/blog/flux-produit-source.jpg)](/images/blog/flux-produit-source.jpg) flux produit source

- 2 : Dans GMC, éléments de départ, sur une fiche produit, j'identifie la catégorie (3) et l'étiquette personnalisée (4) à modifier

[![Image](/images/blog/obversation-du-flux-importé-à-modifier.jpg)](/images/blog/obversation-du-flux-importé-à-modifier.jpg) observation du flux importé à modifier

- 3 : Dans GMC, je me rends ensuite dans le gestionnaire de règles

[![Image](/images/blog/accès-au-gestionnaire-de-règles-du-flux.jpg)](/images/blog/accès-au-gestionnaire-de-règles-du-flux.jpg) Accès au gestionnaire de règles du flux

- 4 : Je sélectionne l'étiquette personnalisée que je souhaite donc modifier

[![Image](/images/blog/choix-de-lattribut-ici-un-label-personnalisé.jpg)](/images/blog/choix-de-lattribut-ici-un-label-personnalisé.jpg) Choix de lattribut ici un label personnalisé

- 5 : Cela m'amène sur l'attribut à modifier, et je créé ma règle, qui consiste à aller chercher dans l'attribut "type de produit" ceux qui contiennent "Gros livre" et affecter une nouvelle valeur

 
[![Image](/images/blog/reglages-du-filtre-conditionnel-à-appliquer.png)](/images/blog/reglages-du-filtre-conditionnel-à-appliquer.png) Reglages du filtre conditionnel à appliquer

- 6 : Je teste la modification

[![Image](/images/blog/test-des-modifications-avant-applications-sur-le-flux-source.jpg)](/images/blog/test-des-modifications-avant-applications-sur-le-flux-source.jpg) Test des modifications avant applications sur le flux source

- 7 : J’obtiens bien la modification souhaitée en test

[![Image](/images/blog/control-du-test-et-des-valeurs-des-attributs-modifiées.jpg)](/images/blog/control-du-test-et-des-valeurs-des-attributs-modifiées.jpg) Contrôle du test et des valeurs des attributs modifiées

- 8 : Il me reste plus qu'à appliquer

[![Image](/images/blog/application-des-regles-sur-le-flux.jpg)](/images/blog/application-des-regles-sur-le-flux.jpg) Application des regles sur le flux

Voilà YA PLUS KA !
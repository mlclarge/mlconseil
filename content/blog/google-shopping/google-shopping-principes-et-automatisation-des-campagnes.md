---
title: "De la gestion manuelle à l'automatisation pour une campagne shopping"
date: 2017-03-13
author: "admin"
categories: ["google shopping"]
tags: []
slug: "google-shopping-principes-et-automatisation-des-campagnes"
image: "/images/blog/shopping-intelligence.jpg"
---

Le commerce reste une convoitise  sur l ' Internet en témoigne différentes annonces dont celle Amazon qui se lance dans la livraison de petite épicerie en France !  [Critéo](http://www.criteo.com/fr/news/press-releases/2016/10/criteo-propose-une-nouvelle-approche-du-search-avec-le-lancement-de-criteo-predictive-search/) quant à lui vient de lancer sa plateforme dédiée à l'**[optimisation de Google shopping](https://www.mauricelargeron.com/regles-de-flux-dans-google-merchant-center/), ** l'occasion  de reparler de ce type de campagne du comparateur  de prix de Google pour en présenter les principales particularités : fondamentaux de gestion manuelle du flux, segmentation et optimisations avancées automatisées.

## **Gestion Manuelle des campagnes shopping**

3 ingrédients sont nécessaires pour lancer une campagne Google shopping : un site e-commerce :) , un compte Google Merchant center, un compte adwords..

[![Image](/images/blog/export-catalogue-310x55.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2017/03/export-catalogue.jpg) Exemple Catalogue prestashop natif à adapter au flux shopping

Le catalogue produit est à adapter aux exigences du flux Google shopping d'où une phase d'optimisation indispensable.

[![Image](/images/blog/optimisation-des-attributs-du-flux-shopping-310x78.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2017/03/optimisation-des-attributs-du-flux-shopping.jpg) Ligne de flux produit à optimiser pour GMC

Le flux shopping réclame 3 types d’attributs (en tête de colonnes) :

 	- Obligatoires selon les types de produits,

 	- Facultatifs pour enrichir la présentation de sa fiche

 	- Optionnels mais vivement conseillés pour segmenter son offre offre selon ses objectifs marketing dans adwords.

[![Image](/images/blog/flux-final-et-segmentation-gmc-310x135.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2017/03/flux-final-et-segmentation-gmc.jpg) Flux final avec segmentation pour gmc

Une fois le matching catalogue 《-》flux dans gmc effectué il suffit de l’importer dans gmc

[![Image](/images/blog/importation-dans-gmc-310x160.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2017/03/importation-dans-gmc.jpg) Google merchant center importation du flux

Accepté les produits peuvent être lance sur adwords. Il conviendra de matérialiser  la segmentation préparée dans gmc au sein d’une campagne au niveau de la création de groupes d'annonces segmentés selon la nature du catalogue / et produits en phase avec vos objectifs commerciaux et d’y adapter une stratégie d'enchères.

[![Image](/images/blog/segmentation-cote-adwords-310x208.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2017/03/segmentation-cote-adwords.jpg) Segmentation produits  coté adwords

Pour chaque groupes d’annonces ou alors uniquement sur celui par défaut qui est généré lors de l’ouverture d’une campagne par le système, une enchère pourra être attribuée valable sur l’ensemble des produits.
## **Gestion automatique dans Google shopping**

### *Utiliser l’api de Google et les plugins existants pour la gestion du flux*

Il est possible d’éviter le travail fastidieux de synchronisation du flux. Il suffira d’utiliser des connecteurs comme ceux existants aujourd’hui pour prestashop, magento ou bigcommerce, ou de faire développer sur mesure des plugins.

[![Image](/images/blog/ecommerce-310x39.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2017/03/ecommerce.jpg)

*Notons au passage le possibilité d' utiliser la mise a jour semi- automatique des produits à l'aide du balisage microdata  schema.org dans le cadre d'une gestion plus rudimentaire du flux. *

### *Faire travailler les optimisateurs automatiques de shopping.*

Dans adwords shopping, le pilotage automatique des enchères existe et est sans doute bien utile pour se libérer des taches chronophages d’arbitrage.

[![Image](/images/blog/stratégie-enchères-automatiques-google-shopping-306x300.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2017/03/stratégie-enchères-automatiques-google-shopping.jpg) 3 façons d'automatiser en natif  les enchères sur Shopping

 	- **Optimiser les clics** : définition des enchères automatiquement afin que d’avoir un max de clics, l’objectif ici, c’est le trafic.

 	- **Optimiseur de CPC** : on dit à Google d’aller chercher la vente en augmentant dans une certaine limite le montant de l’enchère, ici l’objectif visé c’est la conversion en volume.

 	- **Objectif de retour sur les dépenses publicitaires (ROAS)** : l’algorithme ici travail la rentabilité selon vos objectifs, exemple pour 1 euros dépensé en frais adwords,  je souhaite 3 euros de CA, soit une cible à 300 % . Shopping doit donc bien connaître la valeur des ventes et en fonction maximisera la mise en enchères à chaque opportunité.

## **Utiliser des  plateformes automatisées externes à Adwords**

### *Faire tourner l’api native de Google shopping*

Google fournit les clés de programmation (librairie) de sa plateforme de gestion de sa plateforme technique shopping, elle permet de développer dans une interface tierce, un projet de gestion automatisée des enchères

[![Image](/images/blog/api-310x167.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2017/03/api.jpg) Api Google Shopping pour automatiser

Cela m'amène à parler tout naturellement du dernier produit de critéo consacré à shopping. Criteo+Predictive+Search. Marine software, Kenshoo, Versafeed,  Whoopapp.com  et d’autres se sont lancées avant le roi français du retargeting avec pour objectif sans cesse une gestion plus fine et réactive de l’ensemble des entités d’une campagne Google shopping.

[![Image](/images/blog/criteo-predictve-search-310x231.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2017/03/criteo-predictve-search.jpg) Google Shopping Intelligent  vu par Critéo

Critéo met en avant le concept de **machine Learning** pour favoriser au sein d’une campagne shopping la meilleure visibilité du catalogue de l’annonceur.
### Documentation pour démarrer avec shopping

 	- [Créer des campagnes Shopping efficaces et les optimiser : bonnes pratiques de Google](https://support.google.com/adwords/answer/6167176?visit_id=1-636248129389832055-3004302210&rd=)

 	- [Utiliser les plugins google pour l'ecommerce](https://support.google.com/merchants/topic/6279271?hl=fr&ref_topic=3404821)
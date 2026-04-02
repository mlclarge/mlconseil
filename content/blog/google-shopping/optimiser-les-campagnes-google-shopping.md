---
title: "Google Shopping, l'Art de la Structuration"
date: 2018-12-03
author: "admin"
categories: ["google shopping"]
tags: []
slug: "optimiser-les-campagnes-google-shopping"
image: "/images/blog/comparateur-de-prix.jpg"
---

Les statistiques de [Google Shopping](https://support.google.com/google-ads/answer/9027761) s’enrichissent avec cette possibilité d’avoir un relevé des prix affichés des concurrents, Google nous fait un relevé de prix moyen ! C’est bien normal, il est toujours au milieu du gué et comme juge et partie il nous délivre la bonne parole. Bon, pour la petite histoire, Google n’a jamais caché le fait qu’il utilisait en back office, ce signal de prix « compétitif » pour décider d’afficher ou non un commerçant.

Marchand
Prix du produit
Nombre de clics (sept derniers jours)

Marchand A
100 €
9

Marchand B
120 €
1

Marchand C
125 €
0

Prix des produits de référence = (100 € x 9 + 120 € x 1 + 125 € x 0) ÷ 10 clics = 102 €.

Bientôt, car encore en version bêta, cette fonctionnalité sera a activé sous données des concurrents et [shopping](https://www.mauricelargeron.com/regles-de-flux-dans-google-merchant-center/) au niveau de la modification de colonnes. Cela donne ceci..

[![Image](/images/blog/prix-moyens-des-produits-concurrents-502x116.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2018/12/prix-moyens-des-produits-concurrents.jpg) prix moyens des produits concurrents

Sinon, parlons un peu structures de campagne shopping à l’heure ou le tout « Smart » est à l’honneur dans les comptes. Finalement, lancer une campagne shopping, standard ou intelligente n’a rien de compliqué, et dans la mesure où le ROI est au rendez-vous, pourquoi s’embêter plus ? En revanche, si ce n’est pas le cas, l’annonceur à souvent tendance à dire que le comparateur de prix de Google n’est pas pour son business. C’est à ce moment là où il faut parler de libellisation de flux, segmentation de campagnes,  filtres d’inventaire, groupes d’annonces par catégories de produits, en allant parfois même à affiner par groupes de produits. Les mots sont importants et se ressemblent, et l’amalgame créé la confusion. Voyons-en  les grandes lignes pour éclaircir le sujet.

## **Ecosystème Google Shopping**

### ***Le site ecommerce***

Au tout début, était le site web avec son catalogue à exporter sous formats divers (api, ftp, tableur, xml bref..) vers le gestionnaire de catalogue de Google, Google Merchant Center.

### ***Google Merchant Center***

Une fois importé, ce flux devra être optimisé au travers 6 attributs principaux qui sont en fait des entêtes de colonnes d’un tableur classique, on y retrouve :

La catégorie de produit Google : obligatoire, inchangeable

Le type de produit : personnalisable ! Sous forme de fil d’ariane, c’est un atout très important car on retrouve cette catégorisation produit ‘maison’ dans les filtres d’inventaire pour cibler les produits à mettre particulièrement en avant.

[![Image](/images/blog/ecosysteme-google-shopping-502x273.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2018/11/ecosysteme-google-shopping.jpg) Ecosysteme google shopping

->Libellés personnalisés : alors eux ils permettent de rajouter une couche d’intelligence supplémentaire par rapport à la stratégie du marchand. Mes chaussettes d’équitation sont-elles sèches, bon ok, c’est relou comme dirait l’autre, sérieusement ce produit chaussette doit-il être mise en avant :

 	- A l’occasion d’un évènement spécial ? : Noël, fête des célibataires (pour les chinois le 11 novembre !)

 	- Par son taux de marge, faible ou fort

 	- Par le fait qu’actuellement, il est en promo ?

 	- Par son statut de produit « vache à lait » qui rapporte quel que soit la saison, les années.. ?

 	- Par le fait qu’il soit un produit de saison fortement relié à une période ?

-> Marque, Lot, Id…oui, ici  l’id est  la possibilité de ne pousser   uniquement 1 produit, dans une campagne shopping, car il est exceptionnel !

[![Image](/images/blog/google-shopping-2019.gif)](/images/blog/google-shopping-2019.gif)

### ***Google Shopping Ads***

Une fois le flux segmenté, il va falloir filtrer le bon grain selon les objectifs de ventes, ou alors selon une stratégie plus complexe qui va englober tout le tunnel de vente en travaillant la segmentation en campagnes selon l’intention de la requête.

[![Image](/images/blog/tunnel-de-vente-et-intention-de-requete-generic-marque-produit-et-reference-502x182.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2018/11/tunnel-de-vente-et-intention-de-requete-generic-marque-produit-et-reference.jpg) Tunnel de vente et intention de requete generic marque, produit et reference
## **Deux types de structure de campagne Shopping à retenir**

### ***Structures classiques Mono Campagne***

Les différents niveaux de campagnes dans shopping sont au nombre de 4. Mais à selon le niveau, les marges de manœuvre sont plus ou moins réduites…

 	- Campagne = Maitrise du budget, enchères et ajustements, mots clés négatifs

 	- Groupes annonces = enchères et ajustements, mots clés négatifs

 	- Groupe de produits = granularité fine, enchères, exclusion groupes de produits

ou de produit

Cette stratégie centrée sur « les campagnes » peut se faire bien sûr par produits, par libellés issus du flux GMC.

[![Image](/images/blog/structure-par-campagne-462x300.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2018/11/structure-par-campagne.jpg) Structures par campagne

 	- Le style de campagne 1 est le style le plus commun que l’on retrouve dans les comptes. On prend à la source tout l’inventaire, on fixe un budget, et on envoie tout le catalogue avec un cpc optimisé.

 	- Le style de campagne 2 donne plus latitude pour les enchères et la mise en veille de produits.

 	- La structure 3 ouvre  plus de champs sur le ciblage sémantique par la possibilité d’exclure des termes non pertinents et faire des économies !

### ***Structures centrées sur le tunnel de vente***

Alors là accrochez-vous, j’ai rien inventé comme toujours, mais là, cela cogite sérieux. Comme évoqué un petit peu plus haut sur la pyramide inversée, l’idée est d’aller segmenter par le champ sémantique décelé dans les requêtes qui permet de savoir si l’intention est plutôt loin , ou le plus haut possible dans le tunnel vers la conversion. Donc cela nécessite une excellente connaissance du « wording » de l’internaute par rapport au produit et qu’on retrouve souvent sous forme :

 	- Mots clés génériques

 	- Mots clés à la marque +/- nom du produit

 	- Mots clés de référence produits

Ensuite,  il faudra d’une manière classique, faire usage des listes d’exclusion pour ne pas  se « surenchérir » lors de la mise en enchère. L’articulation des campagnes  à toute son importance ici, puisque l’on va piloter par priorité dans les paramètres de campagnes. La campagne, qui se situe loin de la conversion sera prioritaire. Ah bon ! Mais  c’est contre intuitif me direz-vous ! Oui en effet, l’idée est de mettre d’abord en avant le potentiel à faible taux de conversion axé sur des termes génériques pour payer le moins cher en cpc. A l’autre bout du tunnel, le plus proche de l’acte d’achat, restera la campagne en basse priorité mais axée sur des termes à fort potentiel de conversion. Pour couronner le tout, le budget, une enveloppe globale avec la fonctionnalité des budgets partagés, pourra saupoudrer selon le niveau de requête du moment.

[![Image](/images/blog/strategie-multicampagnes-unifiée-avec-budhet-partagé-502x213.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2018/11/strategie-multicampagnes-unifiée-avec-budhet-partagé.jpg) Strategie Multicampagnes unifiée avec budhet partagé
## **Avantages et Inconvénients au sein des campagnes sur l’usage des groupes d’annonces et groupes de produits **

### ***En général ce qui en  ressort…***

***-> Avantages***

 	- Plus de contrôle sur les enchères

 	- Concentration du budget

 	- Ajustements des enchères de périphérique, d'emplacement et d'audience

***-> Inconvénients***

 	- Si ensemble diversifié de produits, créer plusieurs ensembles de deux ou trois groupes de priorités de campagne pour chaque catégorie de produit.

 	- Aucune limite de budget.

 	- Division des produits dans un groupe d'annonces reste un défi.

 	- Impossible de contrôler les requêtes de recherche au niveau du produit SKU

 	- Certains produits ne seront pas exposés en raison de regroupements de produits au sein d'un même groupe d'annonces.

 	- Les produits peu performants sont plus difficiles à exclure ou à gérer à moins que vous ne les retiriez du flux Shopping.

### ***-> Plus spécifiquement, les avantages de l'utilisation de groupes d'annonces pour diviser les campagnes Google Shopping***

 	- Réduction des gaspillages de clics et des dépenses en gérant plus efficacement les termes de recherche.

 	- une structure de groupe d'annonces plus granulaire, identification exacte des mots clés déclencheurs des clics sur vos annonces produits

 	- Ajout de mots clés à exclure dans le groupe d'annonces facilité

 	- Accédez à un niveau plus précis de requêtes de termes de recherche par mots clés qui marchent

 	- Freine les modifications de flux et de groupes de produits en amont

### ***-> Il y a aussi des inconvénients de l'utilisation de groupes d'annonces pour diviser les campagnes ***

 	- Plus de temps pour obtenir des données de clics significatives pour les ajustements d'enchères ou l'automatisation des enchères

 	- Plus difficile d’examiner, d’ajuster et de gérer les enchères lors de l’utilisation de centaines ou de milliers de groupes de produits.

 	- La séparation des produits et la création de groupes d'annonces peuvent prendre beaucoup de temps, sauf si vous utilisez des outils d'optimisation Excel ou tiers.

### ***-> En outre, les  problèmes que pose  la subdivision par groupe de produits***

 	- Diviser les catégories, les produits, les marques, les prix et les identifiants est un problème si vous avez des dizaines de milliers de produits.

 	- Si les produits changent de prix ou de catégories, vos données deviendront plus difficiles à interpréter, car les références des produits qui ont bien fonctionné disparaîtront des divisions de groupes de produits.

 	- Il n'est pas possible de voir quels mots-clés déclenchent des produits spécifiques.

 	- Il est plus difficile de contrôler les termes de recherche de produits de marque pour les marques que vous vendez que les produits que vous ne vendez pas.

 Allez, c’est sans doute le moment de faire faire  des bonnes affaires aux  commerçants qui ont la pression ! Pour la faire baisser, segmentons, filtrons, enchérissons nos campagnes …
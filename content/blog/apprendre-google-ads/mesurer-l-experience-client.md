---
title: "Données de la relation client"
date: 2015-08-24
author: "admin"
categories: ["Apprendre Google Ads"]
tags: []
slug: "mesurer-l-experience-client"
---

La [data](https://fr.wikipedia.org/wiki/Donn%C3%A9e) améliore les taux de conversion, c'est un fait.  Mais d'où  proviennent t-elles ? Passons en revue  les différents gisements d'indicateurs que l’on peut collecter  sur l**’expérience utilisateur**.  Ce dernier peut être un prospect, ou déjà un client, peu importe au final. Au menu aujourd'hui,  typologie et  sources de données au service de la relation client..pour mieux le servir !

## **Les sources de Données plutôt « grises » (invisibles)**

Je les appelle comme cela, je ne sais pas si c’est le terme officiel, mais bon, certaines d’entre elles sont invisibles pour le visiteur lambda mais bien présente sur la page si on les cherche  (clic droit : code source, F12 : console Javascript)

	- **Première partie **: ce sont celles propriétés de l’organisation qui les collecte via un site web  sur sous son nom de domaine, des données métiers, web analytics (Google analytics par exemple) de visites, pages vues, d’analyse de remplissage de formulaire, page d’application mobiles ouvertes, type d’abonnement souscrits (free, premium) ..

	- **Deuxième partie **: négociée contractuellement entre les parties (échange négocié) : segments prospects collecté par une des 2 parties prenantes moyennant transaction ou partenariat.

	- **Troisième partie :** Données issues de collecteurs de data, la contrepartie est la connaissance d’audience plus un enrichissement de profil similaire (ex : LinkedIn pulse)

	- **Open Data :** Sans être dans le big data, les données ont été libérées par les collectivités publiques,  états pour le bénéfice de tous afin de développer des services pour les visiteurs (disponibilités des infrastructures locales, transport, météo)

[![Image](/images/blog/ecosysteme-285x300.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2015/08/ecosysteme.jpg) Ecosysteme Data Site Web
**Des techniques de collecte automatisées sur page web**

Le paradis du développeur web qui va jouer  avec les différents objets de la page (code html, url, formulaire, DOM, variables de sessions navigateur) à l’aide d’outils comme les pixels, cookies et  les manipuler  (transport, collecte)  via des scripts dédiés  côté client (Javascript) ou côté serveur (php, asp, node JS)

[![Image](/images/blog/developpement-tracking-web-298x300.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2015/08/developpement-tracking-web.jpg) Sources Données sur page Web
**Mobilité**

*Web to store ou store to web,* peu importe le sens, les données via les** ibeacons** illustrent la collecte d’une donnée de proximité et propose au visiteur une offre censée être adaptée..Les applications sont multiples : validation de coupons, op de push marketing, paiement (bon enfin, pas trop encore mûr comme système), localisation..Bref, tout ce qui intéresse le géo-fencing an terme anglo-saxon.

https://www.youtube.com/watch?v=UigCpZLYg0s 

## **Les données plutôt  Blanches (visibles)**

First  party elles aussi, elles concernent les données de transactions,  achat de fichiers prospection.  d’application crm. Elles sont généralement produites lors de l’achat, pendant, et après l’acte de vente (support etc..)

	- ***La voix de l’utilisateur** *sans penser forcément big data ici, les données propriétaires collectées (1st partie donc) lors de chat, d’enquêtes en ligne, de voix (call center), d’échanges d’emails. On utilisera des techniques modélisées pour analyser le sentiment général dégagé.

	- ***Des indicateurs de satisfaction client** :*  comme le Net promoter Score ou plus récent le Customer Effort Score qui consiste à poser une simple question client  permettent de prendre le pou sur l’idée que se fait le client sur son fournisseur.

[![Image](/images/blog/enquete-nps-310x201.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2015/08/enquete-nps.jpg) Le Net Promoter Score

[![Image](/images/blog/satisfaction-client-310x300.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2015/08/satisfaction-client.jpg) 3 traditionnels Indicateurs Satisfaction et correlation prédictive

	- ***L’analyse des ventes :***  transactionnel  (panier moyen, nombre d’articles, taux de réachat) , les retours  et les réclamations et leur pondération dans des objectifs de scoring,  sont aussi de précieuses données sur lesquelles  des modèles prédictifs  guideront les objectifs de nouvelles campagnes d’acquisitions pour éviter un taux d’attrition élevé.

[![Image](/images/blog/processus-predictif-rapid-miner-310x260.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2015/08/processus-predictif-rapid-miner.jpg) Processus pour analyse prédictive taux attrition

On peut  noter des KPis "traditionnels"   marketing comme :

**- RFM** (récence, Fréquence, montant), FRAT (avec déclinaison sur la gamme d’achat)

[![Image](/images/blog/rfm-310x206.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2015/08/rfm.jpg) Indicateur RFM

**- Valeur moyenne du client***** **: *autre façon de piloter un budget de campagne, consiste à calculer la valeur moyenne d’un client. Les composantes principales sont :

Valeur moyenne d'une vente
Nombre d'achats annuel
Durée de vie de l’acheteur
Recommandations moyenne amenée par client
Vente par client et par an
Ventes par durée de vie client
Ventes potentielles liées aux recommandations 
Economie Cout par acquisition client / campagne
= **Total de la valeur client
**

Ces indicateurs  (**RFM/CLV : customer lifetime value)** sont pragmatiques dans la mesure où ils font appels uniquement à des faits statistiques de transactions, ils  n'intègrent pas des valeurs plus **émotionnelles** moins quantitatives qui peuvent influer sur le comportement d'achat (réaction suite à un bad buzz, une mauvaise expérience d'achat etc..).

## **Analyse du Bruit social**

***L’analyse sociale :*** le bruit des réseaux sociaux exprimée par la WebSphere sur les présences sociale de la marque  (pages Facebook, fil twister, autres réseau social : RSE), des plateformes  sociales sont aussi une source d’identification, le big data prend tout son sens car il faut ici déployer des modes de calculs rapides sur de gros volumes de données généralement non structurées. Remonter le tout dans les fichiers contacts pour enrichir la **donnée client ou de ses salariés sur un produit, nouvelle mesure etc **(voir ci dessous avec un outil gadget mais qui illustre l'idée)** .** L’expérience client est aussi jugée à l’aune du ressenti des salariés impliqués dans la relation commerciale. Selon une enquête, 65% des salariés manquerait d’implication dans leur travail selon un cabinet RH dont j’ai oublié le nom, cela se ressent forcément sur le client lambda…

[![Image](/images/blog/analyse-de-sentiment-produit-310x179.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2015/08/analyse-de-sentiment-produit.jpg) Analyse de sentiment produit "Apple Watch"

	- **Type de données  dit d’engagement** : like, commentaires, partage, Rt, visites de profils, chaîne vidéo.

	- **Analyse d sentiment** : positif, neutre , négatif.

### **Outils **

**Veille sociale **

	- http://www.csc.ncsu.edu/faculty/healey/tweet_viz/tweet_app/

	- http://www.visibrain.com/

**Magasin de détail**

	- http://www.onyxbeacon.com/   (Ibeacons)
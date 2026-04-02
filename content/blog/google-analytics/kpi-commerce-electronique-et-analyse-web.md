---
title: "11 indicateurs e-commerce dans google analytics"
date: 2012-03-21
author: "admin"
categories: ["Google Analytics"]
tags: []
slug: "kpi-commerce-electronique-et-analyse-web"
---

Cette semaine, j’aborde les indicateurs e-commerce ou kpi dans Google analytics. Les   conditions indispensables bien évidemment sont d’avoir installé le code de suivi standard (GATC) sur le site internet puis d’avoir interfacé le [code suivi complémentaire](http://code.google.com/intl/fr-FR/apis/analytics/docs/tracking/gaTrackingEcommerce.html) avec celui du panier e-commerce du site marchand. Cette implémentation n’est pas intuitive et réclame selon le langage de programmation du site un développement spécifique afin d’intégrer le suivi du panier. Cet article est tiré en partie du livre de Brian Clifton « [advanced web metrics](http://www.advanced-web-metrics.com/blog/) ».

## Google analytics – 11  Indicateurs e-commerce

J’indique *en italique* **au-dessous de chaque KPI** la façon de les retrouver dans Google analytics (version v5).

	- **Taux de conversion global**   : c’est le  rapport  entre nombre de conversion (achat, téléchargements..) et le nombre de clics

       *Conversion  > Commerce électronique >  Vue ensemble -> Taux de conversion du commerce électronique*

	- **Taux moyen par commande** : ou plus communément appelé le panier moyen soit le chiffre d’affaire divisé par le nombre de transaction, facile à trouver !

            *Conversion  > Commerce électronique >  Vue ensemble -> valeur moyenne*

	- **Conversion du réseau de recherche par rapport cpc (publicité)** : utile pour juger de l’impact de ces 2 canaux sur les ventes.

     *Source du trafic > Sources > Recherche > vue ensemble -> onglet « commerce électronique »*

	- **Valeur par visite et valeur par objectif** : utile pour prendre de la distance entre la valeur d’un objectif (divisé par le nombre de visite) et la valeur d’une visite (chiffre d’affaire divisé par le nombre de visites)

       *Source de trafic > Source > Tout le trafic   -> choisir statistique « valeur de l’objectif » (graphique) &  Statistique « valeur de visite » (graphique)*

	- **ROI** (adw) Le retour sur investissement  (profit divisé par le cout) d’une campagne pour 1 euro dépensé, si cela me rapporte 2 euro mon Rsi sera de 100 %.

             * Publicité> Adwords > Campagnes -> onglet « clic »*

[![Image](/images/blog/roi-300x114.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2012/03/roi.jpg)

	- **CA par Nouveau visiteur  & visiteur connu** ?  Utile pour juger si la nature du visiteur influe sur le montant de ses achats, selon le rapport, des actions peuvent être menées pour améliorer les performances de l’un ou l’autre profil.

              *Audience >comportement >  Nouveau vs Connus ->  onglet « commerce électronique »*

	- **Ratio du Ca du nouveau visiteur**

[![Image](/images/blog/ratio-ca-nouv-visiteur.jpg)](/images/blog/ratio-ca-nouv-visiteur.jpg)

	- *Si ratio = 1.0 indique visiteur peut convertir à même égalité avec 1 visiteur connu*

	- *Si > 1 Plus susceptible de devenir client qu’un visiteur « connu »*

	- *Si 

	- **Engagement de la marque** (le ratio s’explique tout seul)

[![Image](/images/blog/engagement-marque-300x39.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2012/03/engagement-marque.jpg)

                            Ex = 45 % *(taux moyen d'intéraction)*

	- **CQI  Index de qualité de conversion** : quelle valeur est apportée par un trafic issue d’un lien qui pointe vers la boutique ?

[![Image](/images/blog/index-qualité-conversion.jpg)](/images/blog/index-qualité-conversion.jpg)

	- **Taux de rebond** *(internautes qui quittent le site dès la 1ère page)*

**Interprétation : **Rouge :  50 % -  Orange :  25/50 %  -  Vert 
 

	- **% d’interaction** *(engagement visiteurs)*

% visites avec interaction =  [![Image](/images/blog/pourcentage-interaction.jpg)](/images/blog/pourcentage-interaction.jpg)
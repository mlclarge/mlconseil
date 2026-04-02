---
title: "Attribution des conversions depuis GA4 dans Google Ads"
date: 2023-03-27
author: "admin"
categories: ["Non classé"]
tags: []
slug: "attribution-des-conversions-depuis-ga4-dans-google-ads"
---

Une intégration de plus en plus aboutie de l'**attribution des conversions** entre google ads et google Analytics est en train de s'opérer depuis quelques temps. Aujourd'hui on parle d'affection du crédit de la conversion . Cela concerne les comptes qui suivent les conversions depuis l'[importation des données de google Analytics](https://support.google.com/analytics/answer/10632359#zippy=%2Chow-are-conversion-credits-imported-to-google-ads-from-google-analytics).
## **Principe de suivi des conversions depuis GA4 (rappel)**

C'es  celui du [dernier clic multicanal ](https://www.mauricelargeron.com/attribution-dans-google-ads-fonctionnalite-pret-a-lemploi/)par défaut pour les conversions web (et le dernier clic ads pour les applications mobiles). Ce type de modélisation du crédit affecté à la conversion ignore les accès directs et attribue 100 % de la conversion au dernier canal avec lequel l'internaute a interagi (soit par un clic, soit par une vue sur YouTube) avant d'effectuer la conversion.

Cas d'usages pratiques du dernier clic  :

 	- 1/ Display > Réseaux sociaux > Liens commerciaux > Recherche naturelle → 100 % à la recherche naturelle
 	- 2/ Display > Réseaux sociaux > Liens commerciaux > E-mail → 100 % à l'e-mail
 	- 3/ Display > Réseaux sociaux > Liens commerciaux > Accès directs → 100 % aux liens commerciaux

## **Attribuer les conversions à Google ads d'une façon plus large**

Jusqu'à présent, les conversions importées depuis Google Analytics 4 sur la base du **dernier clic multicanal** donc.  Elles sont attribuées ensuite dans Google Ads en fonction du modèle d'attribution sélectionné (du premier click au data Driven).

*

Cela signifie que si le dernier click avant conversion ne provient pas de Google ads aucune conversion n'est importée dans le compte publicitaire.  Google indique que cela nuit à l'analyse du poids des différents points de contacts qui ont contribués à la conversion.

Avec cette mise à jour , même si le dernier clic non direct ne provient pas de google ads, tous les points de contact  présent dans le parcours seront importés dans google ads et ventilé selon le modèle d'attribution de google ads.  Personnellement, j'aime bien le modèle linéaire qui attribue une fraction de la conversion à tous les points de contact. Du coup, si google ads est présent dans le parcours utilisateur, sans être pour autant le dernier avant conversion, il aura une partie du crédit de cette conversion.

Selon le type de modèle d'attribution choisit,** data Driven** ou pas, cela devrait impacter le volume des conversions. A suivre donc l'évolution des remontées !
## **Les inconvénients de suivre les conversions depuis Google Analytics 4 par rapport à google ads**

 	- GA4  ne permet pas de suivre le nombre de vues pour des réseaux tels que Display ou YouTube
 	- Si les signaux google ne sont pas activés dans GA4, pas de suivi multi-appareils . Google ads peut utiliser les données des utilisateurs connectés pour identifier les utilisateurs cross devices.
 	- Le suivi des conversions avancées qui permet de capter les données de 1ère partie ne sont pas possible non plus dans GA4.
 	- Le tracking côté serveur est aussi possible depuis G ads, ce qui permet d'être plus solide dans la collecte anonyme des données utilisateurs.

## **Pour conclure sur le reporting des performances de conversions**

Enfin, là encore pour l'attribution des conversions, google tente d'apporter toujours plus de data "holistique" autour du parcours de l'internaute, pour nourrir ses algos.  Des correspondances plus large sur les mots clés, l'intégration plus complète des points de contact, nécessite aussi des budgets toujours plus importants. Mais bon, si au final, l'annonceur s'y retrouve ! Le hic, c'est le ticket d'entrée , qui prend toujours plus de la valeur pour les petits annonceurs.
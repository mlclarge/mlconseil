---
title: "Arrivée des Groupes de canaux personnalises dans google analytics 4"
date: 2024-03-25
author: "admin"
categories: ["Non classé"]
tags: []
slug: "arrivee-des-groupes-de-canaux-personnalises-dans-google-analytics-4"
---

Google Analytics 4 a  ajouté au  groupe de canaux primaires, un nouveau groupe de canaux modifiable qui peut devenir le canal de rapport par défaut pour tous les rapports de canaux. Les canaux sont des définitions basées sur des règles des sources de trafic d’un site web qui vous permettent de surveiller les performances de tous les canaux qui envoient du trafic vers un site web.

*
## **A quoi sert cette fonctionnalité de personnalisation des groupes de canaux ?**

Le groupe de canaux principal permet de contrôler le canal de rapport par défaut, en créant un enregistrement des changements de canaux personnalisés au fil du temps à des fins de rapports historiques, tout en conservant tous les groupes de canaux personnalisés qui reflètent la définition la plus récente dans toutes les données historiques.
## **Comment  accéder et créer un groupe de canaux ?**

### *Accéder à la fonctionnalité*

Avoir accès au groupe de canaux par défaut  est toujours  possible bien sûr et à tous les groupes de canaux personnalisés via le sélecteur de dimensions primaires, les rapports personnalisés et les explorations.

*
Google diffuse les catégories et les sources associées (domaines) dans un document officiel accès ici ([pdf](https://www.mauricelargeron.com/wp-content/uploads/2024/03/GA4-Source-Categories-Sheet1.pdf)).
### *Créer un groupe,  un canal et le modifier*

Il n’est pas possible de se tromper car le canal par défaut n’est pas modifiable , donc cool. On peut s’inspirer du canal par défaut pour ensuite modifier chacun d’entre eux. Cette modification ou création de canal se fait dans l’interface d’une manière assez intuitive en se basant sur les sources + les conditions (filtres d’égalité, expression régulière etc..)

*
Les critères initiaux du groupe de canaux primaires sont les mêmes que ceux du groupe de canaux par défaut, de sorte que toutes les données historiques du groupe de canaux primaires correspondent à celles du groupe de canaux par défaut jusqu'à modification des critères du groupe de canaux primaires. Il est possible alors , à tout moment, définir les critères du groupe de canaux primaires en fonction de l'une des configurations des  groupes de canaux personnalisés existants et, à partir de ce moment, les données du groupe de canaux primaires respectent les critères de ce groupe de canaux personnalisés.
## **Quelles sont les limites sur la création de groupes de canaux dans GA 4 ?**

Pas tant que çà au final ! Seulement 2 pour GA4 en gratuit et 5 pour GA4 360 (payant).

 	- Avec 25 canaux maximum pour chacun des groupes.

*
## **Pour conclure sur les groupes de canaux personnalisés dans GA4**

Il est préférable de bien maitriser toute la chaine de valeur du marquage des sources (utm, paramètres et variables autres  d’urls sur les affiliés , référents) avant de creuser sur les canaux personnalisés. Cela n’impacte pas au final les données natives, mais peut cependant fausser les analyses pendant un moment si ces canaux dédiés au business sont mal appréhendés dès le départ.
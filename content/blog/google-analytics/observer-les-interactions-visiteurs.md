---
title: "Visualisation des flux d'utilisateurs de Google analytics"
date: 2014-11-03
author: "admin"
categories: ["Google Analytics"]
tags: []
slug: "observer-les-interactions-visiteurs"
---

Une des interrogations assez récurrentes de la part des annonceurs, lors de [formations webmarketing](https://www.mauricelargeron.com/apprendre-ameliorer-le-traffic-sur-un-site/), concerne le suivi d’audience   d ’ actions menées sur le site web sur des éléments précis : pages, boutons, liens, documents, etc..Focalisons nous cette semaine sur une page précise au travers des rapports de flux que nous propose google analytics.  Pour ceux qui sont allergiques aux tableaux ingrats aux lignes et colonnes monotones, place au visuel !

## **Flux d’Audience**

Le flux visiteurs permet de visualiser le cheminent des visiteurs selon des dimensions comme  les sources (trafic organique, référent, direct), ou alors un pays, une techno etc…Si l’on veut se focaliser sur une page en particulier , comme une page biographie par exemple, il est pratique de faire un segment dédié sur la page en question (vu son faible taux de vues L ) , puis ensuite de la passer aux  filtres des différentes dimensions et d’observer le dispatch du volume des sessions.

[![flux-visiteurs-310x194.jpg](/images/blog/flux-visiteurs-310x194.jpg) Audience et Flux visiteurs dans GA
## **Flux de Comportements**

Ce rapport  agrège selon les évènements, ou regroupements de pages définis au préalable,  les interactions les plus importantes et leurs relations avec d’autres éléments au cours d’une session. Ces évents entraînent-ils aussi d’autres déclenchements vers la conversion finale ? A noter ici qu’il s’agit de segments de données et les sorties ne signifient pas des abandons pour autant comme pour un entonnoir traditionnel. Ce type de rapport peut indiquer si au cours de la même session des évènements se sont déclenchés plusieurs fois, ou alors de faire ressortir des évènements qui sont plus populaires que d’autres. Pour faire ressortir une page cible avec une faible notoriété, un tri par un segment dédié sera préférable et  affichera les éléments sur la page recherchée. Ici, le clic sur la page  « qui suis-je »  suivie fait l’objet aussi d’un suivi d’évènement (une pierre 2 coups).

[![flux-comportements-310x191.jpg](/images/blog/flux-comportements-310x191.jpg) Flux de comportements
## **Flux de l’Objectif**

Ici l’exemple est réduit à sa plus simple expression  vu qu’il n’y a pas eu d’étapes différentes vers la conversion !  L’entonnoir de l’objectif est un jalonnement imposé d’urls que l’on souhaite voir emprunter  de la part du visiteur.  Dans ce cadre-là, il diffère du flux d’audience vu plus haut. Ce rapport est pratique va directement à l’essentiel. Le rapport de sortie identifie clairement ce qu’il se passe après la conversion aboutie.

[![flux-objectif-287x300.jpg](/images/blog/flux-objectif-287x300.jpg) Flux d'objectifs Google Analytics

A noter les différences de lecture entre le flux de  l’objectifs  et le schéma de l’entonnoir de conversion avec principalement :

	- Le taux de conversion est calculé sur l’ensemble des visites du site et non par rapport aux  nombres d’entrées dans le tunnel (schéma)

	- L’échantillonnage à partir de 100000 lignes pour le flux contre  50 000

	- La segmentation avancée disponible pour le flux et pas pour le schéma.
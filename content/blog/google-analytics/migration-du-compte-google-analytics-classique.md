---
title: "Outil natif pour migrer son compte Google analytics"
date: 2013-10-30
author: "admin"
categories: ["Google Analytics"]
tags: []
slug: "migration-du-compte-google-analytics-classique"
---

On a pu déjà discuter sur l’arrivée du **nouveau code de tracking** de Google Analytics dit Universel  (UA) avec ces avantages et ses inconvénients. Rappelons principalement les 3 axes majeurs de cette évolution qui sont d’un côté  un code de tracking plus souple **moins invasif côté cookie**,  d’autre part un **protocole de mesure centré sur l’utilisateur**,  multi-appareils,  afin d’analyser les usages  au travers différents écrans (mobile, tablette, pc, console..) et enfin une **bibliothèque SDK mise à jour** (sdk v3)  pour les applications mobiles . Je continue aujourd’hui dans le droit fil des posts précédents pour faire part de l’annonce du déploiement d’une fonctionnalité qui va permettre de faire une migration toute en douceur de **Google analytics classique vers Universal Analytics**.

## **Calendrier  du déploiement et mise en œuvre de la migration vers  UA**

Du moins c’est  comme cela que présente l’équipe de développement chez GA.  Cette fonctionnalité a commencé à être déployée sur des comptes et devrait être disponible en France ces prochains jours.

### Feuille de route globale du déploiement de GA

Bien que depuis 2012, il soit possible d’utiliser GA universel, nous rentrons maintenant dans son déploiement uniformisé sur tous les comptes, standards ou premium. D’ici un an probablement, voire même avant, **Universel Analytics** sera le seul code disponible. D’ici là, 4 phases dans la feuille de route vont se succéder. De toute façon, il faudra y passer, même le transfert automatique d’ici quelques mois n’exemptera pas de faire le changement de code de suivi de base.  Donc, il faudra mettre la main à la pâte, quoiqu’il  arrive. Un petit schéma pour y voir plus clair sur le timing des opérations.

[![Image](/images/blog/timeline-deploiement-google-analytics-310x164.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2013/10/timeline-deploiement-google-analytics.jpg)

### Aujourd’hui,  c’est la phase 1 !

Etape 1 : Se rendre sur la propriété dans le compte GA à migrer, appuyé sur le bouton « transférer » .Attendre 24/48 heures pour l’achèvement du processus.

[![Image](/images/blog/transfert-ga-310x249.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2013/10/transfert-ga.jpg) Ecran 1 : Interface transfert dans ga

[![Image](/images/blog/transfert-ga-2-310x286.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2013/10/transfert-ga-2.jpg) Ecran 2 : Attention, tout n'est pas transférable !

Etape 2 : Changer le code natif classique par le nouveau. Voilà, c’est fait.
## **Les avantages et inconvénients d’utiliser l’outil  de migration dès à présent**

### Les plus…

Essayons de dresser le pour et le contre, ou du moins ce qui inciterait à utiliser cette fonctionnalité dès à présent :

	- Les plus incontestables du nouveau code (paramétrages des sessions, exclusion référents, personnalisation des sources de recherche et des termes de recherche)

	- L’historique des données , quoiqu’il en soit est sauvegardé après le transfert

	- Facile et rapide à mettre en œuvre (2 étapes)

	- Maitriser le planning de sa migration : rendu obligatoire à terme d’ici quelques mois, sans préavis, donc difficile de réagir efficacement  une fois mis devant le fait accompli !

### Les moins..

	- Une fois la migration effectuée, le tracking des pages virtuelles, des évènements, des variables personnalisées devra être calibré sur la nouvelle syntaxe du code UA.

	- Avis aux marketeurs, la librairie dc.js qui concerne **doubleClick** n’est pas encore supportée. Donc  les rapports display, les listes de remarketing, les données sociales démographiques  resteront aux abonnés absents dans GAU.

	- Toutes les propriétés du compte sont à traiter séparément. Pas de lot !

## **Le changement, c’est maintenant !**

Si vous ne touchez pas au code classique, une fois passé la phase 2, les données continueront d’être collectées avec  l’ancien suivi **pendant une durée de 2 ans**. Vous ne bénéficierez bien sûr  d’aucun des avantages du code universel.

Plus d’infos : [https://developers.google.com/analytics/devguides/collection/upgrade/](https://developers.google.com/analytics/devguides/collection/upgrade/)
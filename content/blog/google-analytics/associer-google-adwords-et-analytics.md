---
title: "Union Adwords et Analytics en 1 clic"
date: 2014-05-09
author: "admin"
categories: ["Google Analytics"]
tags: []
slug: "associer-google-adwords-et-analytics"
---

La rumeur gronde sur le fait que Google ne fournira  plus les** [mots clés](https://www.mauricelargeron.com/google-repond-a-ses-questions/)** pour ses **liens payants** qu'uniquement dans son interface Adwords,  il n'en n'est rien  pour l’instant.. Je profite de cette actu pour revenir  cette semaine sur une petite information qui n’a pas fait grand bruit, la simplification de **l’association de compte(s) entre Google Adwords et Google analytics**. Je fais le point sur le sujet  : prérequis pour cette union , intérêt  de ce mariage,   mise en œuvre depuis Adwords, et détail de la dernière fonctionnalité dans Analytics.## **Gestion des droits et autres activations  pour que cela marche**

Pour que les 2 comptes puissent discuter entre eux, et les indicateurs **GA être lues dans Adwords**,  il faut autoriser les utilisateurs de ceux-ci,  c’est simple :- Si les 2 comptes sont sur les mêmes accès (email et login semblables) , la liaison se fera sans problème et de manière intuitive, d’ailleurs GA le propose quasiment automatiquement.
- Si les deux comptes ne possèdent pas les mêmes accès, pour des raisons dues à un historique ou à une gestion déportée (cas de centre multicomptes Adwords), il faudra depuis le compte « maître » administrateur, dans ga, autoriser les accès au compte Adwords concerné sur le compte GA, dans gestion des utilisateurs par l’ajout de l’adresse email de gestion Adwords.

Pour que la lecture depuis **GA des données Adwords** il faut aussi :- Activer les partages de  données au niveau du compte GA
- Marquage automatique activé depuis  Adwords (paramètres Gclid)
[![Image](/images/blog/ajout-de-compte-310x151.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2014/05/ajout-de-compte.jpg) Gestion des droits d'accès niveau compte GA

Une fois les accès configurés, les utilisateurs qui ont accès aux vues dans Ga, pourront consulter les statistiques Adwords, de même pour Adwords, si les données sont importées dans Adwords, les utilisateurs ou gestionnaires de comptes Adwords auront accès aux données analytics,  normal.## **Avantages de l’association entre Adwords et Analytics**
### Cette union permet de contextualiser ses actions et de lire dans Adwords
- Taux de rebond
- Pages vues
- Temps passé
- Nouvelles visites
- Mais aussi d’importer  (voir chapitre après).. :
- Objectifs (appelés conversion dans Adwords)
- Liste de remarketing (si enclenchées bien sûr dans GA)
### Google Analytics, lecture des principales données de campagne(s) 
- Ajustement d’enchères
- Mots clés (pas encore not provided J )
- Requêtes de recherche
- Heure de consultation
- Url de destination
- Emplacements (sites sur le réseau displa y de Google)
- Position des mots clés sur le moteur
- Campagnes vidéo
[![Image](/images/blog/donnees-adwords-dans-ga-165x300.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2014/05/donnees-adwords-dans-ga.jpg) Lecture Adw dans GA## **Piloter son association depuis Adwords **

Depuis Adwords, dans les paramètres du compte, le pilotage des associations s’orchestre.[![Image](/images/blog/adwords-etape-1-310x111.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2014/05/adwords-etape-1.jpg) Acces au données de comptes associés

Comme il est possible d’associer plusieurs comptes Adwords sur une propriété GA, il est aussi faisable d’avoir plusieurs propriétés GA sur un même compte Adwords. Ainsi, selon les domaines que l’on gère et les annonces correspondantes, les importations des statistiques Google analytics peuvent s’intégrer dans le reporting Adwords. Il faut choisir pour cela les différentes vues GA que l’on souhaite rendre accessible. Manuellement ensuite, les données GA des différents domaines deviennent «  importables » (objectifs, audiences).[![Image](/images/blog/adwords-etape-2-310x244.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2014/05/adwords-etape-2.jpg) Pilotage des vues analytics dans Adwords

La lecture des **données d’audience** par exemple, réclame l’ajout de colonnes dans les rapports Adwords.[![Image](/images/blog/adwords-etape-3-310x150.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2014/05/adwords-etape-3.jpg) Paramétrages des indicateurs Analytics## **Enfin la nouvelle fonctionnalité d’association pratique !**
### Gestion multiple de comptes Adwords

Comme énoncé dans l’introduction,  le pilotage d’association entre Adwords et Ga devient un jeu d’enfants ..Dans GA, cela se passe au niveau de la propriété. L’exemple ci-dessous montre un compte GA dont l’accès est autorisé à un centre multicompte Adwords. Comme dans Adwords,  il est désormais plus simple d’associer plusieurs comptes Adwords sur une vue de propriété.[![Image](/images/blog/fonctionnalité-google-analytics-310x277.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2014/05/fonctionnalité-google-analytics.jpg) fonctionnalité-google-analytics### Mise en œuvre d’ un groupe de liens

C’est cette dénomination barbare qui indique cette procédure permet donc d’associer et de procéder par la même occasion au marquage automatique (ou manuel variable selon) d’un compte Adw.[![Image](/images/blog/groupe-de-liens-ga-310x192.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2014/05/groupe-de-liens-ga.jpg) Mise en oeuvre d'1 "Groupe de liens"### Dissociation des comptes

Pas forcément intuitif, la procédure de dissociation, il faut aller sur la fonctionnalité « association Adwords » bien sûr, et cliquer sur modifier  puis aller sur « supprimer le groupe d’associations.[![Image](/images/blog/dissociation-groupe-de-liens-analytics-310x183.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2014/05/dissociation-groupe-de-liens-analytics.jpg) Processus de dissociation de compte

**Pour plus d’information** sur les « how to » , rendez-vous sur : [https://support.google.com/adwords/answer/2617364?rd=1](https://support.google.com/adwords/answer/2617364?rd=1)
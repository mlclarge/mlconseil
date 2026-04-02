---
title: "Personnaliser le profil visiteur dans google analytics"
date: 2012-02-08
author: "admin"
categories: ["Google Analytics"]
tags: []
slug: "analyse-avancee-du-suivi-internaute-de-son-site"
---

Intéressons-nous cette semaine aux variables personnalisées du visiteur, une façon plus approfondie de considérer l'analyse visiteur évoquée dans l'article précédent. Le visiteur constitue une donnée que Google analytics nous restitue par défaut  avec des rapports comme ceux portant sur « l' Audience  (voir fig. 1) ».  Les  informations  dîtes « standard » du visiteur sont  ces **visites**, son type (nouveau ou non) , ses** pages vues** , sa provenance (ville, langue, région). D'autre rapports dans GA font aussi découvrir ** le canal**  par lequel il provient *(Google, un favoris, ailleurs ?)*, son cheminement dans le site* (flux , entonnoir de conversion)* . Google analytics  est  incapable cependant de faire une segmentation plus fine d’entrée de jeu, il faudra l’y aider.. Vous allez me dire, quoi savoir de plus ? Eh bien, une multitude d’autres données liées directement de ce que vous proposez dans votre site !

[![Image](/images/blog/fig1-audience-google-analytics-300x182.png)](https://www.mauricelargeron.com/wp-content/uploads/2012/02/fig1-audience-google-analytics.png)
## **Quels peuvent être les données plus avancées que celles rapportées déjà en  « standard » dans GA ?**

Par exemple, dans le cadre d’un site e-commerce, il peut être utile de connaître sur cette population de visiteurs acheteurs, ceux qui :

	- Retirent  un article de leurs paniers

	- Ne finalisent pas leurs achats (abandons)

	- Achètent entre telles ou telles valeurs (petits, moyens, gros clients)

	- Les visiteurs connectés ou non

	- Ont téléchargé un fichier (document, vidéo ..)

Ou bien dans un blog de contenu spécialisé qui nécessite authentification, ou tout simplement sur un site où un formulaire d’abonnement réclame des informations sur le sexe, la profession, hobbies, l'âge ..
Ces exemples  ci-dessus illustrent donc ces **informations qui  peuvent devenir des « critères »** dans le sens de Google analytics au même titre que sont les données standard évoquées au début de cet article.
## **Comment implémenter un suivi personnalisé ?**

Comment effectuer un tel suivi personnalisé *(paramétrages du code)* ?  Google a tout prévu :) , en effet, c’est là qu’interviennent les notions de **valeurs et variables personnalisées**. Deux termes pour effectuer la même chose, cela devient scabreux, non ? Pour comprendre, il faut remonter un peu en arrière dans l’historique de la plateforme Google analytics. Les valeurs personnalisées constituent l’ancienne méthode de paramétrage, elles apparaîssent toujours néanmoins car fonctionnent encore, même dans la dernière version de Google analytics (V5) mais depuis 2009, les **variables personnalisées** remplacent ces valeurs personnalisées *(je ne vais donc pas parler des dernières ici)*. Pourquoi ce changement ? Les variables personnalisées sont plus flexibles, et ses 3 avantages sont  : 1  champ d’application *(voir plus bas fig2 : visiteur, session, page)* comptabilisé dans plusieurs variables* (croisement des données possible)*, 1 niveau de ce même champ  invidualisé selon la variable et enfin plusieurs variables remontables dans un seul appel de fichier .GIF.

Vous l’avez donc compris, ces variables personnalisées sont donc un **moyen de segmenter le flux de visiteurs**  *(selon les besoins du propriétaire  du site)*  afin de mieux comprendre son profil.

***Le code supplémentaire : principe des variables personnalisées***

Selon donc nos souhaits de personnalisation, il conviendra de rajouter un bout de code dans l’élément suivi  *(qui qualifie le segment  « visiteur » perso. à rajouter)* par exemple : une page, un lien, un champ de formulaire, une section d’un  site *(correspondant à un répertoire de l’arborescence d‘un site).  *Ces  variables devront être paramétrées selon les 3 champs d’application (fig.2)  imposés par Google qui sont le visiteur, la session (ou visite) ou la page.

[![Image](/images/blog/Fig2-variablesPersonnalisees-300x181.png)](https://www.mauricelargeron.com/wp-content/uploads/2012/02/Fig2-variablesPersonnalisees.png)
**Installation du code de suivi**

Théorie

Le code devra être placé avant** la fonction trackPageView** dans la partie   (voir fig.3)

[![Image](/images/blog/fig3-codeSuiVariablePerso-300x23.png)](https://www.mauricelargeron.com/wp-content/uploads/2012/02/fig3-codeSuiVariablePerso.png)

**Définition d’une variable personnalisée**

	- **Index : **l'emplacement de votre variable personnalisée, de 1 à 5 : Google Analytics limite en effet le nombre de variables personnalisées à 5.

	- **Name : **le nom de la variable

	- **Value : **la valeur de la variable (sous la forme que vous voulez : chiffres ou lettres). On pourra avoir des valeurs différentes pour une même variable, en fonction de ce que fait ou ne fait pas votre visiteur.

	- **Scope : **le niveau d'analyse de la variable : s'il s'agit d'un visiteur unique (1), d'une session (2) ou d'une page vue (3). Si ce champ est vide, le niveau d'analyse par défaut sera celui de la page.

Pratique 

**Exemple -> Savoir si le visiteur s'identifie sur le site**

	- Code de suivi  :   pageTracker._setCustomVar(1, visiteurs, identifies, 2);

	- champ d’application = session

	- variable perso = lien cliqué

	- Code élément de la page : [Identifiez-vous](liendeconnection.html)

**Mise en garde lors de la configuration**

	- Ne pas combiner le même slot de variable avec différents types (la session l’emporte sur la page)

	- Pas de doublons

	- 5 variables possibles maxi dans une seule requête

	- Faire appel à _setCustomVar() avant page vue ou .gif

	- Faire une matrice de variables si complexité

	- Utiliser le suivi d’évènements au lieu de Variables personnalisées ? (voir paragraphe ci-après)

	- Suivre un comportement alors que celle au niveau page est possible

**Evènements  ou variables personnalisées ?**

Les variables personnalisées sont orientées segmentations *(profils)*  alors que les évènements jaugent plus les actions ou agissements ponctuels des visiteurs *(motivations)*. Le tableau réalisé ci-dessous par Daniel Roch, de [Seomix](http://www.seomix.fr/guide-customs-variables/),  dans son excellent article à sur ce sujet,  est très utile pour comprendre cette distinction (fig.4).

[![Image](/images/blog/fig.4-variablesPerComparatif-239x300.png)](https://www.mauricelargeron.com/wp-content/uploads/2012/02/fig.4-variablesPerComparatif.png)

Plus d’infos :

[http://support.google.com/analytics/bin/answer.py?hl=fr&answer=1144414&topic=1011345&ctx=topic](http://support.google.com/analytics/bin/answer.py?hl=fr&answer=1144414&topic=1011345&ctx=topic)
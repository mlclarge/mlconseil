---
title: "Les Graphes du webmarketing"
date: 2014-06-20
author: "admin"
categories: ["Google Analytics"]
tags: []
slug: "matrice-a-bulles-pour-comprendre-les-donnees"
---

Les **graphes du web**, qu’est-ce c’est ? A quoi servent-ils ? Quels  sont les outils (NodeXL, gephi..) qui exploitent la data ?  Dans un monde numérisé, ou tout se compte, décompte, se regroupe, s’agrège, il est parfois difficile d’avoir **une représentation globale** de tous ces bruits qui  environnent notre présence sur internet. Représenter des acteurs dans un but** analytique**, des objets, des contenus et leur interrelation pourrait être un des objectifs de ces projections graphiques, mais pas seulement, le but peut être aussi **esthétique**, avoir des bulles dessinées au lieu de barres ou autres camemberts cela peut être plus harmonieux.  Je ne vais pas ici faire un tutoriel sur le comment faire de tels graphes *(objet d’un post prochain)*, mais plutôt décrire l’**écosystème d’un graphe**,  et m’attarder sur le « à quoi cela sert » avec des petits cas pratiques au travers différents outils.

## **La production de graphes**

### **A partir de stats d’origine variées**

A la base,  il faut une source, cela peut être les **données** issues d’**API**, de **serveurs web** (fichiers logs), de statistiques diverses provenant de **Google webmaster tool**, d’outils de monitoring seo, d’Adwords, Google analytics, ou d’un texte tout simplement. Certaines données collectées pourront même subir un avant tri, avec d’être collectées (comme ceux provenant de fichier journaux d’un hébergement web) à l’aide de scripts qui vont parsés ces statistiques.

[*](https://www.mauricelargeron.com/wp-content/uploads/2014/06/ecosysteme-des-graphes-webmarketing.jpg) Process de création de graphes

Ensuite, selon les objectifs *(esthétique, analytique ou les deux)*  que l’on souhaite traiter et faire ressortir, un traitement de ces données au préalable sera nécessaire  pour **supprimer, agréger, nettoyer** les informations superflues.

La production d'un graphe ne la confrontation de plusieurs entités, les  « **nœuds** »  avec  ce qui peut les relier entre eux, **les liens**.

Les formats de fichiers à traiter seront le plus souvent sous la forme « .csv ». Il ne restera ensuite plus qu’à les passer à la  moulinette d’outils dédiés à la représentation.

Un exemple ? Tiens, prenons, le cas d’une analyse seo entre les mots clés, et les urls dominantes reliées à ces termes de recherches. Les mots clés ayant le même champ lexical seront agrégés sous forme d’un seul mot clé (nœud 1)   et les urls laissées inchangées (nœuds 2).

[![Image](/images/blog/entités-du-graphe-310x155.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2014/06/entités-du-graphe.jpg) entités-du-graphe
### **A l’aide d’outils intégrés**

Par exemple, des applications cloud comme  NameGenWeb peuvent dessiner en 1 clic de souris en se connectant via l’API Facebook, une représentation de cercles d’amis (voir ci-dessous).

## **Les Graphes appliqués à l’analyse webmarketing**

### **Des Bulles pour le Seo**

**Analyse textuelle « solaire »**

Des applications logicielles dans le domaine de l’analyse peuvent soutenir une réflexion lors de la production d’un texte. Ici, j’ai pris le corps principal d’un article au sujet de l’importance du paramétrage de la balise title lors de la rédaction d’un contenu.

Sur la représentation ci-dessous, plus une référence est répétée, plus la sphère qui la représente est importante en taille. Des entités se forment selon  leur degré de proximité, de points en commun. Ce graphique est orienté, c’est-à-dire lisible selon un ordre avec  une classe centrale, une précédente (à gauche) et une succedante (à droite).

[![Image](/images/blog/texte-graph-310x178.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2014/06/texte-graph.jpg) Analyse sémantique d'un texte
**Le portrait d’une visibilité web**

A partir d’un tableau issu de GWT qui récupère les requêtes et les urls les plus populaires (impressions et clics),  un peu d’agrégation sur les mots clés proches lexicalement permet d’avoir une matière prête à être exploitée par la fonctionnalité « graph » dans Google drive via une table de fusion.

Les nœuds en bleus (mots clés)  sont de tailles proportionnelles à leurs impressions, les « nodes » oranges sont le(s) urls qui portent cette notoriété (variable selon leur affichage).

[![Image](/images/blog/drive-310x203.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2014/06/drive.jpg) Mots clés et Urls
**Des grappes pour le SEA (Adwords)**

A l’aide de Gephi, une application open source dédiée, et de statistiques téléchargées de l’application Adwords sur les types de correspondances des mots clés achetés (large, expression, exacte), une liste de plus de 500 mots clés est passée au crible de l’algorithme  « force atlas 2 ». ..Je remercie au passage **Aurélien Berrut** du blog  [htitipi.com ](http://www.htitipi.com/blog/explorations-visuelles-reseaux.html)particulièrement pour son tutoriel sur le sujet pas piqué des vers sur le sujet.

[![Image](/images/blog/correspondance-et-mots-cles-232x300.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2014/06/correspondance-et-mots-cles.jpg) Densité Correspondance Mots clés

Qu’en ressort-il à première vue ? Tout d’abord que les trois groupes de correspondance ne sont pas de même taille, bon, ok,  pour une découverte…Mais ensuite, que certains mots clés sont employés à la fois en large et en expression (une erreur ? une stratégie ?).

**Des sphères pour Google analytics**

Une des fonctionnalités souvent oubliées de GA est celle liée aux matrices linéaires ou logarithmiques. Ici, ce sont les canaux d’acquisition apporteurs de trafic (organique, payant, référents, direct, display et social)  qui sont mis  à l’honneur au filtre des nouvelles visites (appelée sessions depuis peu). En un clic, sur l’onglet dédié (voir capture écran), la matrice est en place.  Cela change un peu des traditionnels graphiques à barres.

[![Image](/images/blog/acquisition-310x159.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2014/06/acquisition.jpg) Bulles et leviers d'acquisition dans GA
**Le social, un bon terreau pour buller..**
**Les gazoullis agrafés **!*

Comment se représenter l’écosystème d’un #hashtag sur un sujet ? Avec le plugin NodeXl bien sûr !

Ce plugin demande une autorisation d’accès à votre compte twitter depuis le tableur et rapatrie selon le hastag souhaité, ce qui s’est dit (envoyé, twitté, RT..) et en agrège les valeurs, interprété par un des algorithmes de représentation embarqués.

Une bonne dose de patience pour parer les bugs (sous Windows 7)  de ce plugin gratuit pour Excel (merci 1000 fois aux développeurs), un peu de customisation et en quelques minutes, tout devient clair (ou presque) sur le poids des twittos sur le #semainedigitale.  Il détecte 4 grandes entités par le poids des pointages et la diversité des liens.

[*](https://www.mauricelargeron.com/wp-content/uploads/2014/06/nodexl-twitter.jpg) Bruit d'un HashTag Twitter
**Facebook coloré ***

L’application TouchGraph est à l’œuvre. Elle prend la main sur les données d’un compte FB, repère les listes d’amis, les pondères selon le relationnel. Bon rien de rare, un peu égocentrique comme projection, mais bon, cela alimente le sujet. D’autres apps existent comme NameGenWeb sur le même principe.

[*](https://www.mauricelargeron.com/wp-content/uploads/2014/06/facebook-graph.jpg) Cercles et relations Fbook
**LinkedIn a tout prévu***

LinkedIn Labs n’est pas en reste, il propose via InMaps de vous générer  votre graphe relationnel ..à colorier ! Il détermine des clusters selon le niveau des relations, à vous de les qualifier par des couleurs distinctives.

[![Image](/images/blog/cluster-lindedIn-map-s-310x287.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2014/06/cluster-lindedIn-map-s.jpg) Clusters LinkedIn
***GooglePlus ne coince pas non plus la b….***

Bon, c’est la fête quand un post est partagé, ok, pas ambitieux le garçon, mais bon, 5 c’est pas « 0 » ! Et puis, c’est pas le  nombre qui compte, la valeur du partageur est plus déterminante, voilà…merci Adelino, Referenceur.be, Sylvain au passage et j’en passe.. Pour juger d’une viralité, il faut faire appel à la fonction « écho » de G+  disponible en haut et à droite de la fenêtre de post.

[![Image](/images/blog/partageDePosts-310x226.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2014/06/partageDePosts.jpg) Viralité Google Plus

Ces 8  graphes sont donc utiles  pour faire ressortir, aider à l’analyse et embellir la vie du web analyste dans son quotidien.

## **Des endroits où trouver des  outils et lectures intéressantes**

	- NodeXl : http://nodexl.codeplex.com/ + tuto ([anglais](https://blogs.k-state.edu/it-news/2013/04/06/the-nodexl-series-conducting-a-hashtag-search-of-twitter-part-5/))

	- Gephi : https://gephi.org/

	- Google Table de Fusion : [http://www.lije-creative.com/visualiser-linking-interne-tables-fusion/](http://www.lije-creative.com/visualiser-linking-interne-tables-fusion/)

	- Tropes : [analyse sémantique](http://www.tropes.fr/) de textes

	- Apps en ligne : http://box.touchgraph.com/navigator-get.php

	- Visualisation d'1,1 million de commentaires : [http://bit.ly/graphesCommentaires](http://bit.ly/graphesCommentaires)

	- Graphe de Facebook : [http://bit.ly/FacebookGraphForRanking](http://bit.ly/FacebookGraphForRanking)
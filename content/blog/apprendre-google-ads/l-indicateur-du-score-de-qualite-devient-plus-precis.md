---
title: "Evolution du quality score adwords"
date: 2013-09-18
author: "admin"
categories: ["Apprendre Google Ads"]
tags: []
slug: "l-indicateur-du-score-de-qualite-devient-plus-precis"
---

Une annonce adwords  sur le **score de qualité** est parue presque inaperçue cet été, plus exactement le 26 juillet dernier. A priori, cette information stipulait que dans les prochaines semaines, le reporting allait changer plus dans la forme que dans les fondements même  de son  mode de calcul. Les semaines se sont écoulées et les gestionnaires de campagnes  (agences, annonceurs) de la plateforme ont commencé, il y a quelques semaines, a commenter  cette évolution. Je fais un bilan ici de ce qui a pu se dire à ce sujet.  Cette indicateur est il réellement ce qu'il prétend être, soit une variable d'ajustment du montant des enchères  ? Dans ce post, je profiterai de l’occasion pour rappeler ce qu’est le **quality score**,  la façon de le suivre, et enfin, regarderai dans le détail,  les derniers changements  induits dans les campagnes.

## **Un indicateur transversal sur le compte**

Il se calcule sur l’ensemble de votre compte, donc  au-dessus des campagnes, mais n’est visible que dans l’onglet mot clé, et encore, il faut aller rajouter une colonne pour le voir apparaitre dans le reporting adwords. Voici, d’une manière séquentielle, ce que touche le QS.

### Historique de votre compte

Votre compte est-il ancien, actif, inactif, budget dépensé, qualité globale..

### Paramètres de campagne

Qualité des ciblages sur les appareils (mobile, tablette, pc) et sur les zones géographiques.

### Mots clés

Choix de ses mots par rapport à l’annonce et  à la requête de l’internaute

### Annonces

Taux de clic généré par  rapport au nombre d’impressions de l’annonce. Cette dernière est enclenchée par le mot clé bien sûr.

Url à afficher, sa popularité au sein de l’annonce.

### Page de destination

L’internaute a-t-il trouvé satisfaction après la promesse de l’annonce ? Est-elle vraiment en rapport avec le mot clé de départ ?

[![quality-score-310x129.jpg](/images/blog/quality-score-310x129.jpg) Vue globale du QS
### Objectif de cet indicateur

Motiver l’internaute à produire de belles annonces en lui faisant payer moins cher le clic (soit disant)  et ainsi faire cliquer un maximum d’annonces.  pour faire plaisir à Google ;) .

[![formule-scrore-de-qualite1-310x146.jpg](/images/blog/formule-scrore-de-qualite1-310x146.jpg) La recette officielle du QS

Une étude de la société  Click équation rapportée  en 2009, actualisée en 2013 montre des écarts en % cpcs allant de 30% entre un QS de 10 et de 7 à plus de 600% pour un score de qualité à 1 !

[![impact-quality-score-sur-cpc-310x165.jpg](/images/blog/impact-quality-score-sur-cpc-310x165.jpg) Impact du Qs sur Cpc selon Wordstream
## **Contrôler l’évolution de son score de qualité **

### De manière empirique

Au départ d’une campagne, les premiers scores de qualité tombent, 3 :(  ou 10 :) , comme les premières interrogations  à l’école. Puis, comme l’on suit sa campagne, on s’aperçoit de temps en temps que certains mots clés vont  améliorer leur QS.  Il n’y a pas possibilité de faire un historique, un come-back par tranche de dates pour avoir une évolution de son QS.  Alors comment faire ? La fonctionnalité des scripts dans adwords,  peut être utilisée à cet effet.

### Utiliser un script de suivi du quality score

Je remercie encore le blog de **Martin Roettgerding** d’où je tire les sources de ce script. Le principe est de se servir de l’api Google adwords  scripts. L’installation se fait alors en 4 étapes :

1/ Se connecter à son compte Google adwords et exporter depuis l’onglet mot clés un rapport dans Excel, ou autre tableur,  afin d’avoir sous la main campagne, groupes d’annonces et mots clés.

2/ Récupérer et renommer la feuille de  calcul (Google drive)  -> [http://bit.ly/rapportsQsAdw](http://bit.ly/rapportsQsAdw) ,  elle comprend 2 onglets ‘input keyword’ et ‘qs history’ . Remplir les 3 colonnes mots clés, campagne et  groupes d’annonces  du premier "onglet kw" par  copier-coller depuis Excel.

[![rapport-mot-cles-310x184.jpg](/images/blog/rapport-mot-cles-310x184.jpg) Feuille de calcul excel - Copier les données adwords

3/ Copier ce  script : [http://bit.ly/scriptQsAdw](http://bit.ly/scriptQsAdw)  en allant  sur la campagne Compte adwords > rubrique opération groupées>script  le Copier-coller.

[![script-adwords-310x257.jpg](/images/blog/script-adwords-310x257.jpg) Installation du script Adwords

4/ Puis, dans le début du script à l’emplacement : "INSERT_SPREADSHEET_URL_HERE";  vous  mettez l’url de la feuille de calcul Google. Enregistrez et exécuter le script. Le second onglet devrait se remplir des données recherchées soit QS et, au fil du temps, les variations du QS.

[![qs-hsitory-310x219.jpg](/images/blog/qs-hsitory-310x219.jpg) Après exec. du script Lecture dans  google Doc

Une fois cette routine installée, il sera possible de suivre les aléas des changements du QS et notamment de suivre les mises à jour de Google. J’ai installé tardivement ce script, donc n’ai pas assez de recul pour en faire une illustration personnelle ici.

## **Les changements dans les variables du scoring**

Je pense que l’on peut être unanime, que ce soit à l’Us ou en Europe, les aficionados d’adwords ont remarqué des nets changements dans le **scoring du QS**.  Des essais seraient même intervenus avant l’annonce, dès le mois de juin.

[![chutedestauxdequalite-310x160.jpg](/images/blog/chutedestauxdequalite-310x160.jpg)

### Objectifs du changement

Précision plus grande dans les sous facteurs qui impactent le score de qualité soit :

	- le taux de clics attendu

	- la pertinence de l’annonce

	- la qualité de la page de destination.

Le fait d’être dans en dessus ou en dessous de la moyenne dans les 3 paramètres ou seulement parmi l’un des trois est dorénavant plus ajusté.

[![sous-facteurs-310x183.jpg](/images/blog/sous-facteurs-310x183.jpg) 3 sous facteurs plus précis

Exemple : avoir les trois sous facteurs moyens donne un QS de 6, avoir un des trois au-dessus, donne un qs de 7.  Avoir 2 items moyens et 1 en dessous donne un 5 etc…

Ce changement confirme que cette notation plus resserrée n’est pas **corrélée à la qualité du niveau d’enchère**, ce qui est logique, cela a fait le succès du système d'enchères à la google ! Ce n'est pas parce que l'annonceur paie cher qu'il passera en premier, surtout si sa campagne est de qualité médiocre.

## **Revue de liens **

	- Annonce google : http://adwords-fr.blogspot.fr/2013/08/amelioration-des-rapports-adwords-sur.html

	- Article complet sur  évolution du Qs pour PPC : http://www.ppc-epiphany.com/2013/08/08/what-really-happened-in-the-latest-quality-score-update/

	- Commentaires et observation du QS chez  WordStream : http://www.wordstream.com/blog/ws/2013/08/26/quality-score-reporting-change
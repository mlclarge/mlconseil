---
title: "Ce que ne peut pas faire google analytics"
date: 2013-05-22
author: "admin"
categories: ["Google Analytics"]
tags: []
slug: "possibilites-maximales-de-ga"
---

Un des aspects que l’on tente à oublier souvent lors de l’ouverture d’un compte **google analytics**, est la limite imposée par la gratuité de l’outil, ou plutôt ses limites devrions nous dire. Rappelons que l'pplication google analytics est issue d’un rachat d'une société  Urchin Software Corp. Depuis son lancement en 2005, pas moins de 5 versions ont vu le jour, et en septembre 2011 , la version payante  est lancée s’intitulant PREMIUM. Cette dernière est destinée à de grands comptes, manipulant de grandes quantités de données, mais aussi à  ceux qui souhaitent un support et des fonctionnalités supplémentaires. Alors quelles sont ces limites imposées donc à cette version gratuite ?  Prenons le cas tout bête de la sauvegarde des données, la version standard les conserve 25 mois , la payante , c’est illimitée enfin ..presque 36 mois ;) . Donc pensez à constituer un historique en dehors de l’interface de GA dès à présent. Sur le fond, observer les limites d'une appli. sert aussi à mieux en comprendre ses possibilités.

Dans une première partie, nous verrons ce que ne peut pas faire GA, puis un second temps ce que Google analytics **ne fait pas par défaut**,  nous ferons ensuite un petit tour du côté des capacités de brassage de l’outil avec un comparatif entre version standard et premium et enfin terminerons sur les quotas MAX de l'application (Std).

## **Ce que Google analytics ne peut pas faire *(ou ne veut pas faire !)***

- **Customisation** de son interface (comme son concurrent Coremétrics), omniture le peut (menus).

- Pas de **rétroactivité** sur la collecte des données : les données ne peuvent être recalculées une fois le flux de données collecté à la source. En cas d’anomalie décelée sur un site à un instant « T », les données ne peuvent être corrigées.

- Les TOS (terms of service) de google interdisent officiellement la **collecte de données d’identification** des visiteurs et celles de  machines (adresses IP).

- **Exporter l’intégralité d’un compte**, ou une sous catégorie (sources de trafic, audience, conversions). Bien qu’il soit possible de procéder à un export de tous types de rapports par sous catégorie.

- **Aide à la structuration d’un compte** à la mise en service . Avec un seul domaine, pas de problème. Si vous possédez plusieurs domaines, sous domaines, rien d’intuitif  n’est encore prévu (il faut bien critiquer, non ? ).
## **GA ne le fait pas "par défaut" *(Out of the box)***

Si vous procédez à une installation simple, soit copier-coller le code de suivi tel quel, aucune donnée ne sera remontée quant aux différentes actions sur :

	- les **pages d’erreur** sur le site (code 404, 500)

	- les différentes **intéractions du visiteur** sur 1 page : clic sur un bouton, remplissage d’un formulaire, survol de souris sur un élément

	- le visionnage d’une **vidéo** Youtube

	- Une **animation** flash (si, si, cela existe encore)

	- Les **liens sortants** (vers tel ou tel partenaire, site amis de la blog roll)

	- Les **téléchargements** de documents (pdf, doc, exe..)

	- La **valeur** des conversions (je le précise pour soulever le fait que parmi les non professionnel, c’est très souvent ignoré)

	- Le suivi des **transactions** ecommerce

	- Une page ou un module avec **IFrame** (en gros, une page située à l’intérieur d’une autre page) ou du moins les indicateurs en seront faussés.

## **Les limites entre version Standard et Premium de GA**

### Pour la version premium (ce qu’il y a de plus)

**- Rétention des données :** 36 mois contre 25 pour la standard

**- Une assistance** où une équipe s’occupe de la mise en œuvre, de la gestion et de la formation avec une hotline dédiée

- **Un traitement des données** : le nombre d’accès, le nombre de lignes traitées, le non échantillonnage (critère important !) , son actualisation.

- **Une garantie de service :** une assurance d’actualisation toutes les 4 heures avec  plus de 99% de disponibilité sur la collecte, la création de rapports, et les garanties de niveau de service.

- **L’accès à partir de septembre a BigQuery** , une interface cloud google  qui permettra de lancer des requêtes sql sur les indicateurs de GA afin de générer des rapports puissants (segmentation, a/b testing) impossible à faire depuis l’interface utilisateur.

- **50 variables personnalisées** ramenées à **5** pour la Std

[![Image](/images/blog/ga-std-vs-premium-1-310x257.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2013/05/ga-std-vs-premium-1.jpg) Principales différences entre Std et Premium
## **Les quotas limites MAX standard de  GA **

Je résume ici une information rapportée par Peter Graig lors d'un post sur le site [http://www.customreportsharing.com](http://www.customreportsharing.com/) .
*Compte et profils (nombre) : *

	- 100 comptes maxi (compte premium en accepterait jusqu’à 200)

	- 50 profils

*Par Session *

	- 500 requetes par session 

	- 10 requetes par tranche de 5 secondes

	- 5 Maximum variables personnalisées par requête

*Par Rapport  (un seul))*

	- 256 caractères maxi par paramétrage de filtre

	- 5 segments avancés

	- 5 filtres maxi

	- 5 onglets maxi

	- 500 lignes à afficher (il serait possible d’amener ce chiffre à plus en jouant sur le paramètres générer par l’url de GA)

*Objectifs par profil*

	- 25 objectifs

	- 5 jeux d’objectifs

	- 10 étapes maxi par tunnel de conversion

Plus d'infos  :

- Ouvrage de **Brian Clifton**

- Maxi : [http://www.customreportsharing.com/topic/53-what-are-the-absolute-limits-for-google-analytics/](http://www.customreportsharing.com/topic/53-what-are-the-absolute-limits-for-google-analytics/)

- Google : [http://www.google.com/analytics/premium/features.html](http://www.google.com/analytics/premium/features.html)

Les retours d'expérience, corrections, commentaires  sont les bienvenus, merci d'avance..
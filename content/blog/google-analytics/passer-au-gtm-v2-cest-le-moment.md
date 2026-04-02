---
title: "Comment passer à la Version 2 du Gestionnaire de balise"
date: 2015-04-27
author: "admin"
categories: ["Google Analytics"]
tags: []
slug: "passer-au-gtm-v2-cest-le-moment"
---

Cette semaine,  repartons sur le sujet du suivi d’audience. Je tenais à partager ma petite  expérience de  migration du[ gestionnaire de balises](http://www.tagcommander.com/) V1 vers V2  autrement appelé **Google tag manager**, qui *(je le rappelle pour ceux qui n'ont pas suivi)*  gère les codes de tracking d’une manière distante via la pose unique d’un container global (script Js)  au cœur du Template du site. Il fait partie désormais  de la grande famille des TMS (tag management system) depuis 2012 auprès notamment du français **Tag commander** que je cite ici car il est de loin son aîné (2010). Voyons ici donc le mode automatique (de loin le plus simple), et la façon manuelle (par définition plus fastidieuse).

## **Migration du GTM automatique**

Depuis fin 2014, la V2 est lancée et apporte une réelle amélioration pour l’utilisateur quant  au workflow pour paramétrer une balise. Simplification des étapes, interface avec un design et visualisation améliorés. Pour plus d’information sur la présentation du potentiel de Gtm, je vous renvoie sur cet article : [https://www.mauricelargeron.com/passage-de-la-version-1-a-la-version-2-du-gtm/](https://www.mauricelargeron.com/passage-de-la-version-1-a-la-version-2-du-gtm/) .  Aujourd’hui, **2 plateformes coexisten**t car la migration n’est pas imposée pour l’instant  et sont disponible d’une manière intuitive via 2 urls différentes, mais attention, dès le 1er juin,  la migration sera automatiquement programmée.  Vous allez  me dire à quoi cela sert alors de le faire maintenant ?  Cela permet dans un premier temps, de ne pas « subir »  et de se familiariser avec  l’interface, ensuite, toute migration peut avoir des bugs dus  à certaines  incompatibilités d’une version à l’autre et être.  Travailler dans l’urgence pour régler le problème n’est pas forcément l’idéal.

[![Image](/images/blog/url-ancienne-interface-gtm-310x60.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2015/04/url-ancienne-interface-gtm.jpg) Deux Interfaces de GTM

Sinon, la procédure automatique ne prend que 15 minutes montre en main ! Il suffit de cliquer sur le bouton comme dirait l’autre, et suivre la procédure en 4 étapes.  L’avantage principal avec le mode manuel (voir plus bas), c’est bien sûr la simplicité et la commodité de ne pas avoir à créer un  ID nouveau du genre : GTM-KPX87B, l’assistant le fait  pour vous !

[![Image](/images/blog/migration-automatique-etape1-2-310x201.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2015/04/migration-automatique-etape1-2.jpg) Migration automatique etape1-2

Autre avantage de l’assistant, c’est qu’il est progressif. En effet, tous les tags ne sont pas mise à jour dans le compte de l’utilisateur, un choix est proposé, il suffit de cocher ! Et c’est tout ! Il faut ensuite attendre quelques minutes, se rendre dans l’interface V2 et constater le transfert.

[![Image](/images/blog/migration-automatique-etape-3-4-221x300.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2015/04/migration-automatique-etape-3-4.jpg)

Petite précision : A la différence d’une création « out of the box » depuis la V2, le processus de migration créé une liste des variables disponible depuis le menu de gauche  (anciennement appelées macros pour la V1)  et ne pré-coché,  pas comme  par défaut dans une installation  nouvelle,  2 catégories de variables .

## **Migration Manuelle**

Comme son nom l’indique, il va falloir faire plus de manipulations !  D’abord créer dans la V2 un nouvel espace qui va accueillir le container de la V1. Il faut donc créer un container  tout neuf pour y fusionner/intégrer celui que l’on souhaite migrer. Puis depuis la V1, exporter le container en local (pc-Apple-linux) le fichier au format Json.

[![Image](/images/blog/exportation-du-container-261x300.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2015/04/exportation-du-container.jpg) Exportation du container

Il suffira ensuite d’aller depuis la V1 chercher en local le container.json  et de l’importer, alors soit de le remplacer (efface) ou de le fusionner (conserver d’éventuels paramétrages) …S’il y a un conflit de toute façon entre V1 et V2, une notification de blocage en rouge s’affiche et invite à d’éventuels correctifs à opérer depuis la V1. J’ai pu avoir le cas notamment sur un variable « tableau » pas compatible avec la V2. Donc à tester selon ses propres  marqueurs.

[![Image](/images/blog/importation-container-format-json-310x254.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2015/04/importation-container-format-json.jpg) Importation container

Bon courage dans votre projet de migration du Google tag manager !

 	- Ce qui change avec la version deux : https://support.google.com/tagmanager/answer/4605576?hl=fr

 	- Tms Français "Tag Commander" : www.**tagcommander**.com/fr/
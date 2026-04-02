---
title: "Suivi des clics en 2 clics avec le tag manager !"
date: 2013-12-04
author: "admin"
categories: ["Google Analytics"]
tags: []
slug: "suivi-des-clics-en-2-clics-avec-le-tag-manager"
---

Voilà bientôt une année  que Google analytics annonçait la sortie de son gestionnaire de balises. Ce dernier permet de se faciliter la vie lors du balisage de son site afin de scruter son audience. Donc depuis un an, le « **tag manager** »   a fait son bout de chemin. Dernièrement, des fonctionnalités pratiques se sont rajoutées, et notamment l’écouteur d’évènements. Arrêtons-nous un petit moment dessus après un bref rappel des possibilités de ce gestionnaire de balises.

## **Un container  de plus. Mais pourquoi faire ?**

	- Eviter des allées et venues quotidiennes dans le code source du site

	- Simplifier le codage de certains marqueurs (c’est vrai, voire plus bas !)

	- Alléger le chargement de la page (constaté aussi..)

	- S’ouvrir sur d’autres sources de données (d’Audiences, de Display, Comportementales)

	- Améliorer le tracking Google Adwords (conversion + remarketing)

	- Remplacer l'existant et optimiser  les scripts vieillissants

## **Quelques petits trucs pour le tag manager**

	- Pour la compréhension d'ensemble [voir cette page](https://www.mauricelargeron.com/guide-pour-demarrer-avec-le-gogle-tag-manager/)

	- Les 3 ingrédients indispensables pour créer un suivi sur un objet dans une page web (liens, boutons, vidéo, image etc..)  : une balise (marqueur)  avec une règle (condition)   adossée à une macro (valeur).

	- Automatiquement la plateforme créée depuis quelques mois 10 macros :

	- 5 variables d’évènement automatique (élément, elm. classes, id, target, url)

	- 1 event

	- 1 referrer

	- 3 composantes d’url (url, hostname, path)

	- Le Google Tag manager  ne sait pas comptabiliser les widgets de partage sociaux

	- Pas de possibilité de lui assigner un ordre dans l’exécution des balises posées

	- Un maximum de 8 requêtes http sur un domaine en simultané est gérable par un navigateur

	- Les pages dynamiques peuvent être gérées via l’ajout d’un évènement

	- Si parfois, lors de l’ajout d’une balise, il n’est pas possible  de placer l’objet « couche de données »* (copain nécessaire du container pour certains marqueurs)* avant le container, une condition via un évènement peut en différer le chargement.

	- Dans le cas de campagne adwords avec optimiseur de conversion et  remarketing  il est fortement conseillé d’utiliser le tag manager.

## **Focus sur les évènements (clics)**

Depuis donc quelques semaines, pour le bonheur des non développeurs, Google a intégré une fonctionnalité qui permet de suivre tous **les clics sur une page** qui peuvent s'y  dérouler (boutons, liens, images, adresse email…) , soit sur **tous les liens** (internes et externes), ou alors sur l’**envoi d’un formulaire**, et enfin  l’**intégration d’un timer** pour déclencher des évènements selon une certaine fréquence de temps.

### *Suivre les clics sur une page *

Il va falloir pour cela créer  2 éléments *(au préalable, le code de suivi standard est implémenté) *:

1 balise « écouteur de clics » qui surveille les clics composée selon  1 règle « Toutes les pages » (regex .*) .  dont qui définit son étendue et dont la valeur est {{url}} (macro).  La règle et la macro sont données nativement, donc pas de code à faire (pour les containers créés depuis septembre 2013).

[*](https://www.mauricelargeron.com/wp-content/uploads/2013/12/tous-les-clics-.jpg) Mise en place 1ere balise dans GTM

1 balise « Google analytics (classique ou universelle) » dont le type sera celui d’évènement munie des 4 paramètres (catégorie, action, libellé, et valeur) pour enregistrer le clic. La règle invoquée celle de la macro {{event}}  égale à la valeur de GA « gtm.click ». Là aussi rien n’est à coder, il suffit de remplir les champs aux bons endroits.

[![evenement-310x270.jpg](/images/blog/evenement-310x270.jpg) Misen en place 2eme balise

Ensuite, directement dans la rubrique temps réel dans Google analytics, on peut observer ce que cela donne en allant sur « evènement » puis observer la colonne « action d’évèn. »  rendu par la macro paramétrée sur {{element}} dans les paramètres de la seconde balise « GA » (ci-dessus).

[![rapport-temps-réel-lien-sortant-310x184.jpg](/images/blog/rapport-temps-réel-lien-sortant-310x184.jpg) rapport-temps-réel-lien-sortant
### Suivre un clic sur un lien spécifique*

Je souhaite suivre le lien sortant dans le pied de page qui amène sur Twitter par exemple. Le principe est le même donc 2 balises à créer :

La Balise « clics sur le liens » (donnée,rien à inventer)  cette fois ci rentre en jeu, sur « toutes les pages » (regex .*).

[![clic-sur-liens-310x282.jpg](/images/blog/clic-sur-liens-310x282.jpg) 1ere balise : Clic sur Liens

La balise évènement, quant à elle,  est basée sur la règle qui observe 2 conditions dont la macro {{event}} qui doit être égale à  gtm.linkClick (donné nativement) + l’url suivie {{element url}}  qui doit contenir « twitter » par exemple. Attention aux paramétrages des suivis des évènements, afin de s'y retrouver ensuite dans ses rapports dans GA .

[![evenement-lien-sortant-310x284.jpg](/images/blog/evenement-lien-sortant-310x284.jpg) 2nde Balise évènement

Dans Google analytics, une fois son « action » et son libellé d’évènement paramétré, on peut suivre l’activité des clics sur ce type de  lien sortant.

[![temps-réel-evènement-292x300.jpg](/images/blog/temps-réel-evènement-292x300.jpg) temps-réel-evènement

Finalement pour les non codeurs, cela devient facile, attention aussi à  ne pas tomber dans un excès de données superflues en se prenant au jeu de la facilité d’implémentation !

## Petits liens entre amis

	- [Aide google sur la gestion des évènements au travers du GT](https://support.google.com/tagmanager/answer/3415369?hl=fr#TimerListener)M

	- [La Documentation Développeurs ](https://developers.google.com/tag-manager/quickstart)

	- la plateforme : https://www.google.com/tagmanager/
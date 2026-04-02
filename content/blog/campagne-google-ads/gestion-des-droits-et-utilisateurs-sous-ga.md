---
title: "Configurer un compte analytics"
date: 2014-01-10
author: "admin"
categories: ["Campagne google ads"]
tags: []
slug: "gestion-des-droits-et-utilisateurs-sous-ga"
---

Comment bien structurer et gérer les accès à son compte Google analytics ? Il arrive souvent d’avoir des demandes désespérées sur le  forum adwords - Analytics sur la perte d’accès à des comptes ou tout simplement être limité dans sa gestion quotidienne. Revenons sur quelques éléments fondamentaux sur l’architecture de compte chez GA et sur sa [gestion au quotidien](https://www.mauricelargeron.com/gestion-mode-consentement-google-ads/).

## Structure et création d’un compte Google analytics

### Architecture d’un compte GA

Il est conseillé de savoir comment est articulé l’application analytics avant de créer tête baissée un compte. 25 comptes GA sont autorisés par compte G. Dans un compte GA, les  propriétés sont illimitées (mais ne suis pas sûr à 100% !)  mais les  Vues  ne le sont pas (ancien profil), 50 maxi par compte analytics sont accordées. Par défaut, quand une propriété est créée, un vue générique est créée.

**Mise à jour 14/02/2014 :** Nous serions passés à 100 comptes GA au lieu de 25 , cela laisse du champ, mais toujours 50 vues maxi par propriété (UA-XXXXXXX). Source : [http://gatipoftheday.com/google-analytics-account-limit-raised-from-25-to-100/](http://gatipoftheday.com/google-analytics-account-limit-raised-from-25-to-100/) Tks to Eric Fettman for this news ! 

[![Image](https://www.mauricelargeron.com/wp-content/uploads/2014/01/architecture-compte-analytics-310x165.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2014/01/architecture-compte-analytics.jpg) architecture-compte-analytics

Il est conseillé de la garder comme « sauvegarde » sans filtre, puis d’en créer une seconde réservée à d’éventuels tests, puis une troisième « maître » pour l’analyse. Ainsi, vous avec un compte prêt à l’emploi et modifiable à tout moment sans risque aucun de perdre les données brutes.

[![Image](https://www.mauricelargeron.com/wp-content/uploads/2014/01/structure-compte-ga-35-310x159.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2014/01/structure-compte-ga-35.jpg) Structure de Base GA

Un compte Google analytics est constitué de 3 éléments avec un « ID » dédié

 	- Le numéro de compte en lui-même :** Account ID 12345678 **: En tant qu’administrateur, est transférable, niveau le plus élevé.

 	- Le code de suivi de la propriété web  : **ID UA-12333444-1** : pas migrable, hérite des droits de l’étage précédent.

 	- La vue : **ID 52701699** : pas transférable, liée à la propriété

[![Image](https://www.mauricelargeron.com/wp-content/uploads/2014/01/structure-compte-ga-3-310x175.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2014/01/structure-compte-ga-3.jpg) Configuration standard
### Comment créer un accès G. Analytics ?

Il faut donc avoir un compte Google à la base pour accéder à l’interface G Analytics. Un compte gmail, existant suffira pour acccéder ensuite au service analytics, sinon, il faudra en créer un pour l’occasion.

## Gestion  pour son compte GA

### A qui est destiné le compte ?

Si c’est un site personnel, pas de problème déontologique. S’il s’agit d’un  mandat, alors il sera préférable d‘utiliser un compte Google existant ou d’en créer un pour le client et lui demander  un accès en tant qu’administrateur.

### Quels sont les sites, apps, appareils  à suivre ?

Y a t-il plusieurs domaines, des sous domaines, des restrictions d’accès, des multiples accès ? Y T a-t-il des applications, des devices spécifiques ? La gestion des droits devra être pensée en amont pour pouvoir ensuite décliner une bonne gestion du compte GA et des droits utilisateurs qui lui sont liés.

### Y a-t-il différents services souhaitant avoir la même information modifiable, un siège social souhaitant un accès à toutes les propriétés ?

Dans ce cadre-là, un suivi multitracking (plusieurs : UA-xxxxxx pour un même domaine) peut être envisagé.

### Comment supprimer une propriété ?

Passer d’abord par la suppression de la vue liée à la web property.

### Comment dépasser les limites standard de GA ?

Tout simplement en n’étant pas le compte origine de la création du compte GA. Ainsi, non seulement la transparence est respectée, et les accès aux comptes tiers illimité !

### Est -il possible de transférer une propriété sur un autre compte ?

Cela revient à dire qu’il ne faut jamais créer sous un compte GA, des propriétés (UA..) pour des entités, des projets différents (clients) . Le jour ou une propriété veut voler de  ses propres ailes, le compte GA administrateur à l’origine gardera obligatoirement un accès à ce même compte (gros problème de confidentialité), à moins que cet administrateur renonce à tous ces autres comptes ;) .

## Quelques liens ressources

 	- Gestion des utilisateurs : [https://support.google.com/analytics/answer/2884495?hl=fr&utm_id=ad](https://support.google.com/analytics/answer/2884495?hl=fr&utm_id=ad)

 	- Doc google (anglais) : [https://developers.google.com/analytics/resources/concepts/gaConceptsAccounts](https://developers.google.com/analytics/resources/concepts/gaConceptsAccounts)

 	- Utiliser un suivi multitracking (rn) : [http://www.blastam.com/blog/index.php/2013/04/using-multiple-trackers-in-google-analytics/](http://www.blastam.com/blog/index.php/2013/04/using-multiple-trackers-in-google-analytics/)
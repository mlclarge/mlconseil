---
title: "Modèle d'Urls Adwords personnalisées"
date: 2015-02-23
author: "admin"
categories: ["campagnes display"]
tags: []
slug: "modele-de-suivi-urls-adwords"
---

MAJ : Première innovation 2015  fonctionnelle d'importance  pour **Google Adwords**. Elle concerne le **paramétrages des urls** pour les  annonces façon Ninja !  L’objectif de cette nouveauté est triple : apporter une simplification dans la mise à jour des urls, réduire le temps de crawl, et amener une  simplification pour la gestion des urls . Un beau programme donc, je vous propose de revenir sur le pourquoi d’un suivi personnalisé et sur ce nouveau paramétrage de ces « urls finales ». J'en profite aussi pour vous informez que je propose un cursus de formation google ads tout au long de l'année ici : [https://www.mauricelargeron.com/formation-google-ads/](https://www.mauricelargeron.com/formation-google-ads/)

## **Rappel sur les types d’urls dans les annonces adwords**

**Un clic et bien plus encore !**

Une annonce est composée  de 2 urls , une qui est visible (verte non cliquables) appelée url à afficher et une autre cliquables avec une ancre qui reprend généralement le titre de l’annonce mais dont l’adresse « technique » est cachée au visiteur mais visible dans le bas du navigateur. Cette url contient des paramètres de 2 types :

 	- Google : sécurité, tracking Google (interne et suivi Google analytics), redirection page de destination annonceur

[*](https://www.mauricelargeron.com/wp-content/uploads/2015/02/decryptage-url-annonce-adwords.jpg) Decryptage url annonce adwords

 	- Annonceur : Suivi personnalisé identifié après  l’adresse de la landing page suivi d’un caractère « ? ». Il permet de faire un tracking personnel à l’annonceur en intégrant les données de clics sur une plateforme de suivi propriétaire (crm ou autre) .

Exemples de suivis avancés  :

 	- Entités   compte adwords : groupe annonces, géo, mot clé, correspondance, device, extensions,

 	- Google shopping et DSA  (pour avoir des infos sur les urls dynamiques gérés pas le système adwords)

 	- Variables logiciel tierces  (crm , analytics)

Ce  paramétrage est facultatif et  n’a pas de lien  avec le marquage automatique des urls pour assurer un suivi dans Google analytics des campagnes ads ou adwords.  Il reste cependant des règles à respecter afin d’éviter des conflits de marqueurs.

[![urls-destination-adwords-310x135.jpg](/images/blog/urls-destination-adwords-310x135.jpg) urls destination adwords
## **Comment paramétrer traditionnellement les urls personnalisées  adwords ?**

2 façons permettent de faire un suivi plus poussé des [campagnes ads](https://www.mauricelargeron.com/campagne-display-google-ads-avec-ciblage-optimise/).

 	- **Manière « simple **»  statique en ajoutant des paramètres de variables réclamées par les applications de collecte (logiciels tierces, Custom Relationship Management).

 	- Url sans personnalisation : http://www.monsiteweb.fr/page-destination-lambda/

 	- Url ciblée sur les mots clés : http://www.monsiteweb.fr/ma-page-avec-mot-clé/ où depuis l'onglet "keywords" il suffit de créer une colonne "url destination" et indiquez la landing page dédiée au mot clé (https://support.google.com/adwords/answer/2404246?hl=fr#kw)

 	- Url de destination simple personnalisée : [http://www.monsiteweb.fr/page-destination/?crm=ann123](http://www.monsiteweb.fr/page-destination/?crm=ann123)

 	- **Façon dynamique**  à l’aide de paramètres  « Value Track »

 	- Url dynamique  customisée  avec balises dédiées  : http://www.monsiteweb.fr/page-destination/? ?keyword={keyword}&matchtype={matchtype} -> récupération pour cette url de destination du mot clé et du type de correspondance  enclenchée.

### ***Y a-t-il un rapport  avec le marquage Google analytics  ? ***

Oui ! Notez parfois des incompatibilités entre différents mode de tracking !  Voici la liste des combinaisons qui peuvent se supporter.  Donc attention de ne pas aller au-delà de ces combinaisons...

 	- Marquage simple  avec liaison **Adwords /Analytics** , reconnaissable avec le parametre  « gclid » inclus automatiquement par le système

 	- Balisage manuel seul à l’aide des  **UTM classiques** (http://www.monsiteweb.fr/page-destination?utm_source=google&utm_medium=cpc&utm_campaign=cgneprintemps)

 	- Suivi Value Track Seul

 	- Tagage double : **Value Track**  + marquage automatique  adw

 	- Duo Tracking  : Value Track  manuel  et Suivi Utm

 	- Personnalisation Simple et value track

## **Principes de la nouvelle fonctionnalité de suivi d’url : « modèle de suivi »**

### **Un template pour tout arranger..***

Pour ceux qui  n’utilisent pas Adwords éditor, on sait qu’ il est fastidieux de changer des paramètres à toutes les annonces lorsque l’url de destination change ou bien lorsque de nouveaux marqueurs font leur apparition.

 	- Y a til quelque chose à changer  pour ceux qui ne font pas de suivi ? : non

L’objectif de la nouveauté est d’offrir un **modèle de suivi** , un template dans le jargon qui va pourvoir servir de masque de personnalisation à l’échelle du compte (via la bibliothèque partagée) , des groupes d’annonces, des liens d’extensions afin de faire un changement de masse sur les urls de destination qui vont disparaître dès le 1er juillet prochaine pour laisser place à l’intitulé « url finale ».

[*](https://www.mauricelargeron.com/wp-content/uploads/2015/02/parametres-url-adwords.jpg) Avant..Maintenant !

Ce « modèle de suivi » est à  indiquer dans les ressources partagées d’ Adwords (bbliothèque).

### **Comment paramétrer ce modèle de suivi ?***

**Contexte de l’annonce** : Bannière display avec contrôle tierce des clics. Récupération des différentes composantes de l’url, ici il y aura une redirection entre l’annonce et la landing page pour assurer le  tracking externe, avec collecte d’une variable crm perso, plus une identification des annonces et des domaines ciblés dans Google analytics.

 	- **Url finale** : url =http://www.monsiteweb.fr/page-destination/ ->Balise dynamique : Value Track : **{lpurl**}

 	- **Paramètre personnalisé** : id=cgneadw2015  -> modèle **{_monIdCgne}**

 	- **Paramètres Value Track Display** : Annonce et Domaine ciblé  ->Value Track : **creative={creative}&placement={placement}**

 	- **Suivi tierce** : http://redirection.monsiteweb.fr/redirect ? (page tampon)

Cela donne :

 	- http://redirection.monsiteweb.fr/redirect?creative={creative}&placement={placement}&id=cgneadw2015&url=http://www.monsiteweb.fr/page-destination/

### *Implémentation du Modèle de suivi global*

http://redirection.monsiteweb.fr/redirect ?annonce={creative}&domaine={placement}&{_MonIdCgne}&url={lpurl}

[![url-perso-campagne-sea-310x248.jpg](/images/blog/url-perso-campagne-sea-310x248.jpg) Paramétrages de Campagne Modele suivi
## **Liens ressources à ne pas manquer **

Toutes ces ressources sont celles de la documentation Google.

 	- Utiliser les urls mises à jour : [https://support.google.com/adwords/answer/6049217?hl=fr#final](https://support.google.com/adwords/answer/6049217?hl=fr#final)

 	- Suivi des redirections : [https://support.google.com/adwords/answer/6076199?ctx=tltp#edit](https://support.google.com/adwords/answer/6076199?ctx=tltp#edit)

 	- ValueTrack : https://support.google.com/adwords/answer/2375447?hl=fr
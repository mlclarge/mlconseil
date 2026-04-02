---
title: "Suivi d'évènements pour un Site Web"
date: 2014-03-28
author: "admin"
categories: ["Google Analytics"]
tags: ["evènements"]
slug: "mesurer-les-interactions-visiteurs"
---

J’ai pu aborder le sujet du paramétrage des **évènements dans Google analytics** dans différents articles dont [celui ci](https://www.mauricelargeron.com/objectifs-et-evenements-dans-google-analytics/) en 2012, ou ceux liés au **tag manager**, mais rien de spécifique à cette mesure des interactions des visiteurs. Bon, eh bien, c’est ce que je vais tenter de faire ici, avec  pour commencer une définition et un recul historique sur le sujet, puis nous verrons les différentes façons de **coder ces « events »** et d'insérer** ce tracking  sous diverses formes  Php, As3** ,  la façon de les interpréter dans l’application de web analyse (**rapports**) et enfin les limites et  les possibilités de débugage.

## **Une fonctionnalité assez récente**

### **Définition et environnement du tracking d'évènements**

Les évènements permettent de suivre des interactions de l’internaute sur des objets tels que des liens, des images, des vidéos, des boutons, des formulaires, des documents (téléchargements), des animations (flash)  aussi bien sur des pages web, que sur des applications mobiles. Donc la pageVue n’est plus le seul objectif d’un suivi, c’est assez révolutionnaire !

[![Image](https://www.mauricelargeron.com/wp-content/uploads/2014/03/interactions-avec-site-web-248x300.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2014/03/interactions-avec-site-web.jpg) Types d'intéractions - Merci à son auteur
### **Syntaxe du code pour google analytics universel**

[![Image](https://www.mauricelargeron.com/wp-content/uploads/2014/03/syntaxe-code-310x48.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2014/03/syntaxe-code.jpg) syntaxe code
### **Historique**

	- C’est en **2007** que fut lancée cette possibilité de traquer les clics en version bêta.  Ce marquage s’effectue en Javascript, donc côté navigateur du client. Le début de ce marquage s’effectuait en 2 étapes pour le codage (création de l’objet, puis tracking des actions sur ce dernier).

	- **2008** simplifie le procédé et dans l’ancien code synchrone, cela donne (pageTracker._trackEvent("monlien", "doc", "produitA");

	- **2009 **: tracking asynchrone devenu classique GA (ga.js ) et déploiement global  des « évents » dans GA. gaq.push();

	- **2011 **: possibilité d’utiliser ce marquage comme un non évènement (pas d’incidence sur le taux de rebond) _gaq.push();

	- **2012 **: Lancement du tracking universal (analytics.js) du coup le codage des évènements deviennent dans sa version basique : ga('send', 'event', 'categorie', 'action',’libellé’, ‘nonInteraction’ : 0 ou 1)

	- **2013** : Les évènements deviennent lisibles en temps réel, pratique pour tester « live » le marquage.

	- **2014 **: l’auto event tracking est lancé sur le tag manager.

## **Différentes méthodes pour coder des évènements**

### **Implémentation classique ou universelle sur site  (ga.js)**

**Principes : **Google analytics se repose donc sur le language Javascript avec ses fonctions et méthodes pour pouvoir suivre certains comportements visiteurs comme par exemple :

	- Le clic pour un lien ou téléchargement d’un doc : fonction  « onClick »

	- La soumission ou l’activité sur un champ de formulaire : « onSubmit » ou « onBlur »

Les scripts basiques donnés ici le sont à titre **d’exemples pédagogiques**, selon le type de code de chaque site (classes Css, balisage html, librairie Js embarquée, chemins des fichiers) , il faudra les adapter. Ils sont donnés soit dans la version classique (CA)  ou alors Universel (UA)
**Méthode manuelle**

Le tracking se fait manuellement, donc sur** chaque « objet » identifié** sur la page comme un lien interne, une image précise etc . La syntaxe  déclenchera l’envoi de l’intéraction sera liée à l’objectif que l’on se fixe (clic, roll over, scrolling etc…) . Le code de base GATC est nécessaire en plus de la syntaxe de base vue précédemment dans l’historique. Ce qui change, c’est la méthode appelée selon la nature de l’intéraction que l’on souhaite analyser, que l’on soit sous le mode « classic » ou « universal » , le process reste le même, seule la syntaxe change.

	- **Clic sur un lien pdf (classique)**

Comme la page même, le pdf n’est pas traquable par lui-même de l’intérieur, il conviendra de suivre le chemin ou l’Uri de ce document pour parvenir à son suivi.

[onClick="javascript; _gaq.push(

	- **Lien sortant (UA)**

Suivez-moi](/documentation/pdfs/documentA.pdf)

	- **Sur une image (UA)**

![Image](mon-image.jpg ) 

	- **Sur un bouton (CA)**

**
	- **Sur un champ de formulaire  (CA)**

	- **Sur le bouton d’envoi d’un formulaire (CA)**

	- **Sur un email (vers un client  du genre « mailto » sur outlook) (UA)**

mailto: lien
Méthode semi - automatique Universelle sur du Javascript simple (méthode doc dev. GA)**

	- Principe : Dans le head de la page taguée, on écoute des clics liés à un téléchargement sur des objects identifiés (ids : image et div) , que l’on récupère avec une fonction JS,  avec ce petit snippet  **(UA) **:

// 

	- Ensuite, dans le body , on place les marqueurs sur les objets (ici une image et 1 balise Div)

Image :

 ![Image](bouton.jpg)

Div :

[
](http://www.monsite.fr/)

**Méthode automatique** **avancée avec Jquery (CA)**

Un script situé dans le head de la page, ou appelé par une simple syntaxe depuis l’entête de page,  va  « écouter » différents éléments interactifs qui se déroulent  et les pousser automatiquement vers Google analytics. Pratique ! Nécessite d’avoir la librairie Jquery d’embarquée.

	- Appel du fichier Js externe à la page (mettre dans le head) :

 

	- Inclusion dans le Head : monScriptExterneTracking.js

Ce script adapté à la méthode classique traque les téléchargements selon certaines extensions (mp3, pdfs, txt ..) , les liens sortants, les clics sur adresse mail, sur les num. de téléphone. Rien à placer sur les objets dans le corps de la page !

 // 
## **Variantes de tracking**

### **Pousser plusieurs events dans un seul envoi (Classic) !**

J’ai pu repérer dans un forum aussi cette possibilité d’envoyer plusieurs évènements lors d’un seul appel à la méthode, je la donne pour info. Le but était ici de récupérer les valeurs de choix d’un menu déroulant lors de l’envoi d’un formulaire (extrait) :

 _gaq.push(
,
,
,

);
### **Insérer le code GA d’évènement  au sein de  snippet php,  actionScript …**

Ici, c’est un même formulaire présent sur diverses pages, qu’il faut traquer. Le script php va scraper les urls ou le formulaire sera envoyé, le code de Google analytics y sera inséré récupèrera la valeur de cette fonction php.

**EN PHP**

?>
En ActionScript (flash)

package com.elevatelocal.model{ import com.google.analytics.AnalyticsTracker; import com.google.analytics.GATracker; import flash.display.MovieClip; import flash.events.MouseEvent; import flash.events.Event; public class AnalyticsTrackToday extends MovieClip { private var _stageAccess:MovieClip; private var _keywordTracker:String; private var tracker:AnalyticsTracker; public function AnalyticsTrackToday(getStage:MovieClip) { tracker=new GATracker(getStage,"UA-15476449-1","AS3",false); _stageAccess=getStage; } public function onQuery(getKeywords:String) { _keywordTracker=getKeywords; if (_keywordTracker!=null) { tracker.trackEvent("search queries","keywords",_keywordTracker); trace(tracker.trackEvent); } } } }

merci à Yousaf Sekander sur  http://www.rocketmill.co.uk/ pour ce partage)
### Traquer sans JavaScript le téléchargement de docs. !

**Julien Coquet** nous délivre ici une méthode avancée pour traquer vraiment les téléchargements à base d’UA  et qui se fonde sur l’**analyse de logs serveur**. En effet, il n’est pas possible de savoir réellement si le document est téléchargé dans sa totalité, sauf…en parsant les logs par un script dédié.  Ce dernier récupère les éléments nécessaires et  les envoie via  l’**url formatée pour universal analytics**  sur les serveurs de Google analytics. Il fallait y penser !

#!/bin/bash
#on dÃ©finit l'expression rÃ©guliÃ¨re servant Ã  dÃ©tecter le fichier PDF dans chaque ligne de code
pattern='GET /(.*\.pdf)'
# On rÃ©cupÃ¨re chaque nouvelle ligne de mon log Apache contenant un fichier .pdf
tail -f /var/log/apache2/access_log | grep --line-buffered .pdf | while read line; do
  echo $line
  if ]; then
	#on rÃ©cupÃ¨re la valeur entre parenthÃ¨ses dans la regex
	monfichier=${BASH_REMATCH}
  fi
  #on appelle le pixel Universal Analytics, avec les paramÃ¨tres qui vont bien
  wget -q -O  /tmp/pixel.gif "http://www.google-analytics.com/collect?v=1&t=event&tid=UA-7634164-5&cid=555&dh=juliencoquet.com&ec=Downloads&ea=PDF&el=$monfichier&ev=1"
done

Plus d'[Infos](http://juliencoquet.com/en/2013/04/05/track-pdf-downloads-with-google-universal-analytics-no-javascript/) ici

## Suivre ces évènements avec le Tag Manager**

### Deux étapes pour le procédé sans codage

J’ai pu déjà  aborder le [suivi de clics](https://www.mauricelargeron.com/suivi-des-clics-en-2-clics-avec-le-tag-manager/) par le gestionnaire de balises, donc ici focalisons nous sur le suivi sur une même page de plusieurs liens de téléchargement pdfs. Cela suppose que le container soit déjà installé dans le body du site. Je  rappelle que l’avantage ici, c’est que tout se passe sur la plateforme externe au site, sans codage particulier.

	- un  écouteur de « clics sur les liens » qui va faire office de script à l’écoute de tous les clics sur le site

[![Image](https://www.mauricelargeron.com/wp-content/uploads/2014/03/pdf-tag-manager-310x160.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2014/03/pdf-tag-manager.jpg) 2 étapes dans GTM

	- Ensuite , sur l’objet en question, un évènement sera paramétré pour fixer le déclenchement du tracking sur les urls se terminant par « .pdf » (point 5 sur capture écran ci-dessous). Je lui demande dans les attributs qui me fasse remonter le nom du lien afin de distinguer les différents pdfs (point 4 sur l’illustration).

[![Image](https://www.mauricelargeron.com/wp-content/uploads/2014/03/clics-sur-les-liens-310x138.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2014/03/clics-sur-les-liens.jpg) Etape 1 : Installation de l'écouteur de clics

[![Image](https://www.mauricelargeron.com/wp-content/uploads/2014/03/evenement-tag-manager-310x210.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2014/03/evenement-tag-manager.jpg) Etape 2 : Paramétrage de l'évènement
## **La lecture des Rapports **

### **Suivis de Pdfs**

Prenons l’exemple des liens sur les pdfs, le rapport standard ci-dessous restitue les libéllés « telechargementDoc » puis les différents intitulés des documents téléchargés (distinction par la remontée de « l’élément url »paramétré au niveau du libellé de l’évènement.

[![Image](https://www.mauricelargeron.com/wp-content/uploads/2014/03/gestionnaire-de-balises-310x142.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2014/03/gestionnaire-de-balises.jpg) Rapport Standard dans GA -Docs Pdfs

Noter l’indicateur d’évènements uniques qui rapportent sur un ensemble de visites le nombre total d’enregistrement mais aussi rapporté par type.
### **Le temps réel bien pratique**

Sinon, il est possible d’avoir aussi une vue en temps réel de toute sorte de tracking comme les liens internes, sortants, les soumissions formulaires, la profondeur du scrolling etc..

[![Image](https://www.mauricelargeron.com/wp-content/uploads/2014/03/ga-event-gtm-boutiquier-310x266.png)](https://www.mauricelargeron.com/wp-content/uploads/2014/03/ga-event-gtm-boutiquier.png) Temps réel - Pratique pour tester ses events
### **Les rapports personnalisés**

On peut par exemple segmenter toutes les visites avec celles qui observent des évènements liés aux conversions du site, pour tenter de mesurer l’impact éventuel d’un objet suivi tel qu’une bannière d’auto-promotion par exemple.

[![Image](https://www.mauricelargeron.com/wp-content/uploads/2014/03/segmentation-event-objectifs-310x216.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2014/03/segmentation-event-objectifs.jpg) Segments pour contextualiser ses Ev.
## **Limites et débogage**

### **Pas d’illimité chez Google !**

	- Les 10  1er puis toutes les secondes (classique) à 20  premiers events, puis 2 par seconde  (universal) sont traqués simultanément dirons-nous. Ensuite, c’est 1 event par seconde avec une limite de 500 par session,  200 000 hits par visiteurs par jour ou  10 millions de hits par mois par propriété (dixit Google !).

	- Si Js est désactivé dans le navigateur, pas de tracking  possible.

### **Pour trouver le bug ou avoir si l’implémentation est correcte.**

On peut aller dialoguer avec la console, mais là cela devient coton !  Non, sinon, le plus simple, sans chrome, taper F12, cela ouvre la console Js, ensuite :

	- Cliquer sur l’onglet « Source »

	- Sur la partie droite du panneau, descendre jusqu’à « Event Listener Breakpoints »

	- étendre l’arborescence et choisir le type d’évènement que l’on veut suivre

	- Interagir avec l’élément suivi (lien, image etc.)

Ou bien

	- Faire un clic droit « inspecter l’élément »

	- Aller à droite sur « event listener » et inspecter les attributs recherchés

	- Répérer les scripts liés à l’évènement (voir ci-dessous, sur un lien, le GTM y est lié par un suivi de « CLICK ».

[![Image](https://www.mauricelargeron.com/wp-content/uploads/2014/03/debuggage-event-console-310x143.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2014/03/debuggage-event-console.jpg) Debug - Console Chrome
## Webographie

**Merci aux développeurs** pour le partage de leur travail. Voici quelques sources d'informations ..

	- En: les différentes méthodes de tracking par [seer interactive ](http://www.seerinteractive.com/blog/event-tracking-explained)

	- Fr : Comprendre les évènements avec la [syntaxe Javascript](http://www.commentcamarche.net/contents/573-javascript-les-evenements)

	- Outils - Plateformes de tracking automatique : [http://www.skyglue.com/ ](http://www.skyglue.com/ )ou [http://www.analyticsengine.net/how-it-works/](http://www.analyticsengine.net/how-it-works/)

	- Suivi par [script Jquery chez Blastam](http://www.blastam.com/blog/index.php/2013/03/how-to-track-downloads-in-google-analytics-v2/) (un des scrips de l'article)

	- Outil de [débuggage visuel Wasp](http://support.webanalyticssolutionprofiler.com/knowledgebase/articles/210112-wasp-for-chrome-faq)
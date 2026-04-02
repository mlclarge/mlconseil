---
title: "Suivre les intéractions sur un document pdf avec GTM"
date: 2016-12-05
author: "admin"
categories: ["Google Analytics"]
tags: []
slug: "clics-sur-pdf-avec-tag-manager"
image: "/images/blog/pdf-trackinG-avec-gtm.jpg"
---

La semaine dernière, j'ai été questionné par une stagiaire sur le [tag manager.](http://tagmanager.google.com)  Comment puis-je suivre le téléchargement d'un document PDF spécifique sur un site ? Je me suis posé la question "il doit bien avoir un petit tuto. sur Google ?" Eh bien oui, il y a des choses, mais qui datent un peu ! Rien sur la 1er page de Google relatif à la dernière version du Google tag manager. Je prends ici un cas pratique d'un lien sur **une page du blog qui possède un document pdf** de la plateforme search metrics.

[![serp-google-411x300.jpg](/images/blog/serp-google-411x300.jpg) resultats sur tag manager dans google
## **Quelle méthode pour suivre un PDF dans Google tag manager ?**

Tout d'abord, il faut installer le container de GTM (2 bouts de code Js) sur le Template du site. Avec, une partie dans le Head et l'autre dans le body.

Pour la petite histoire, l'ancien code placé uniquement dans le body fonctionne encore. Pour le possesseur de WordPress, le [**plugin de Thomas Geiger**](https://wordpress.org/support/topic/gtm-container-in-2-parts-now-in-and/) a fait la mise à jour qui scinde le container en 2 parties : head et body. Merci encore à son developpeur ! :)
Une fois le container installé, il suffit de suivre le workflow de GTM qui est le même pour tous les marqueurs soit :

 	- Récupération d'une variable par les écouteurs par défaut préinstallé, ou création personnalisée

 	- Application d’un déclencheur, autrement dit d'une condition ou d'une règle d'exécution. Cette étape matérialise le contexte, si tu es sur cette variable à cet endroit-là de la page alors tu peux envoyer cette data.

 	- Matérialisation de cette récupération par la balise ou marqueur pour la solution d'analyse d'audience, ici Google analytics sous forme d'évènement.

[![processus-marquage-pdf-avec-tag-manager-341x300.jpg](/images/blog/processus-marquage-pdf-avec-tag-manager-341x300.jpg) Processus de marquage dans GTM

Pratiquement, une fois le container sur le site, il est conseillé de travailler en mode débogage au niveau de la console navigateur.
## **Travail sur la page web qui contient le lien PDF**

Cette étape consiste à auditer le lien que l'on souhaite suivre à l'endroit de la page. Deux outils sont nécessaires à ce stade. Tout d'abord, la console JavaScript par une sélection puis un clic droit de souris, puis "inspecter". On examine l'objet à suivre. Ensuite, le mode debug de gtm permet de vérifier quel élément le container récupère par rapport à notre problématique de lien à suivre amenant au "pdf".

[![lien-pdf-sur-la-page-search-metrics-avec-console-js-421x300.jpg](/images/blog/lien-pdf-sur-la-page-search-metrics-avec-console-js-421x300.jpg) Lien-pdf-sur-la-page-search-metrics-avec-console-js

Aperçu de la console GTM dans le navigateur

[![lien-pdf-sur-la-page-search-metrics-ecoute-par-tag-manager-310x146.jpg](/images/blog/lien-pdf-sur-la-page-search-metrics-ecoute-par-tag-manager-310x146.jpg) lien-pdf-sur-la-page-search-metrics-ecoute-par-tag-manager
## **Paramétrages sur Google tag manager**

Une fois la tache de repérage accomplie dans le navigateur, il va falloir le traduire dans le [gestionnaire de balises](https://www.mauricelargeron.com/look-de-rentree-du-tag-manager/). Suivant le process définit précédemment dans le 1er paragraphe on peut obtenir

 	- Variable : c'est  l'élément url  soit le lien du pdf

[![dans-tag-manager-ecouteur-automatique-405x300.jpg](/images/blog/dans-tag-manager-ecouteur-automatique-405x300.jpg) Dans-tag-manager-recupération-automatique de l'url à

 	- Déclencheur : sur cet élément url , soit ici un clic de souris du visiteur.

[![declencheur-sur-lien-avec-mention-436x300.jpg](/images/blog/declencheur-sur-lien-avec-mention-436x300.jpg) Declencheur-sur-lien-avec-mention

 	- Balise : récupération de la data et envoi sur Google analytics sous forme d'évènement. Le data model est constitué de 3 éléments principaux : catégorie  (pdf search metrics), action, libellé.

[![evenement-lisible-dans-google-analytics-240x300.jpg](/images/blog/evenement-lisible-dans-google-analytics-240x300.jpg) Paramétrahes de l'Evenement-lisible-dans-google-analytics

Il ne faudra pas oublier de sortir du mode debug de gtm et de publier le travail pour le rendre disponible live à tous les visiteurs.

## Résultat dans Google analytics

Chaque clic désormais  sur ce lien fera l'objet d'un évènement qui sera lisible en temps réel dans la rubrique appropriée de Google analytics. Cet évènement pourra aussi être définit comme objectif selon besoin. Il faudra attendre quelques heures supplémentaires pour voir apparaitre dans ses rapports standards de GA, au niveau de la catégorie comportement.

[![evenement-dans-google-analytics-450x300.jpg](/images/blog/evenement-dans-google-analytics-450x300.jpg) Rapport Evenements-dans-google-analytics
### ***Quelques liens supplémentaires***
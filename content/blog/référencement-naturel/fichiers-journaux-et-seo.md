---
title: "Analyses de log pour le référencement naturel"
date: 2013-03-14
author: "admin"
categories: ["Référencement naturel"]
tags: []
slug: "fichiers-journaux-et-seo"
---

L’analyse de fichiers journaux d’un serveur web  (ou logs)  peut être un complément utile  à l’analyse d’audience de Google analytics pour comprendre un problème sur le référencement naturel  d’un site internet. Ce type d’analyse peut être  effectué  par exemple suite  à un constat  de baisse  d’impressions,  ou une désindexation d’urls dans les résultats de Google.  Quelles sont les données à rechercher ? Avec quels types d’outils (existants et dédiés) ?  Les pistes d’exploration doivent se diriger sur l’analyse du crawling des robots qui parcourent le site en permanence, sur les erreurs  de serveurs,  de pages *(qui  jalonnent le parcours du visiteur mais qui passent  en apparence inaperçues lors d’une visite ponctuelle lambda)*  sans oublier  le  type de crawl que ces bots font sur le website.

## **Les données manquantes pour une analyse complète seo dans Google analytics**

### **Etat du Crawl des robots**

Par défaut, Google analytics ne donne pas de statistiques sur la fréquentation des robots et sur ce qu’ils font selon l’architecture du site. En revanche, Google webmaster tool donne une indication sur son propre robot, ce qui est déjà pas mal.

[![Image](/images/blog/googlewebmastertool-310x98.gif)](https://www.mauricelargeron.com/wp-content/uploads/2013/03/googlewebmastertool.gif) Actvitité de Google Bot sur les derniers 90 jours

Pour tenter d’avoir une exhaustivité  des robots, il faudra d’abord les recenser et ensuite demander à Google analytics de nous les montrer. Cela se complique ici, il faut  mettre les mains dans le moteur pour pouvoir tirer cette information. [Un article américain d’un site de référence, nous donne la méthode](http://www.cardinalpath.com/tracking-search-bots-in-google-analytics/) .

### **Diagnostique des Erreurs « http » de site web  et autres codes d’état. **

******Régulièrement, le site renvoie des erreurs suite à des requêtes de navigateurs de type (extrait).

	- Page web introuvable (erreur 400)

	- Le site Web a refusé d'afficher cette page Web (HTTP 403)

	- Page Web introuvable (HTTP 404) : la plus connue !

	- Le site Web ne peut pas afficher la page (HTTP 405)

	- Le site Web ne peut pas afficher la page (HTTP 500 : plus  problématique !

	- La page est redirigée (code 301) : A surveiller ;)

	- Redirection temporaire (code 302) : A surveiller

Là aussi , Google analytics nous donne pas grand-chose d’inné à son système, il faudra  rentrer à nouveau dans le **GATC** cette fois ci et y ajouter une portion de code pour lui dire d’aller déclencher un évènement qui  marquera chaque type de code d’erreur ([Voir ici pour la méthode](http://antezeta.com/news/404-errors-google-analytics)). Sinon, des astuces existent cependant, Jean-Benoît MOINGT nous en fait part dans [son blog](http://www.watussi.fr/monitorer-le-crawl-de-son-site-avec-google-analytics) , mais je n'ai pas testé sa validité actuelle, mais l'important à retenir c'est surtout le principe.
## **L’aide des Applications d’analyse de fichier journaux.**

Afin d’éviter de perdre du temps à paramétrer Google analytics des applications de lecture de fichiers log existent  déjà  et sont préinstallées par l’hébergeur et accessible depuis l’interface manager du site.  Chez ovh, c’est encore le logiciel « Urchin «  (plus suivi depuis mi  2012 mais qui fonctionne encore) de chez Google company d’ailleurs !  Elle  donne les éléments que l’on recherchait  dans le paragraphe précédent à savoir les robots, les codes d’états.  Vous allez me dire, c’est un peu tiré par les cheveux comme me disait mon prof de math, pourquoi ne pas avoir tout dans la même appli. Qui plus est, si c’est fait par la même boite ? Expliquons le simplement ainsi, leurs usage sont différents, fait pour des publics différents, plus IT, professionnels  (technos, informaticiens)  pour Urchin et plus grand public et commercial (gratuit, lié à adwords) pour GA. Plus d’information sur les différences entre [Urchin et GAnalytics ](http://www.google.com/urchin/fr-FR/features.html) chacune des solutions ici *(attention à la coquille sur les analyses de session, il faut intervertir la réponse binaire, oui/non !)*  Bref, peu importe la marque, l’intérêt est d’avoir les statistiques pertinentes.

[![Image](/images/blog/codeEtat-310x142.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2013/03/codeEtat.jpg) Ex Ovh : codes d'état donnés par Urchin

Pour connaître les robots ou autres scripts automatisés, voyons ce que donne "WebStat" la solution d’analyse de log utilisée chez 1&1

[![Image](/images/blog/robots-310x159.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2013/03/robots.jpg) 1&1 : Liste des robots par Webstat

Ce qui est gênant, si vous avez suivi jusqu’ici, c’est que l’on aucune de ces jolies statistiques corrélées avec le contenu, on sait éventuellement, la proportion d’erreurs ou de redirections mais on ne sait pas le type de catégorie  touchée par ces résultats, le niveau  du « budget de crawl » alloué par les bots et surtout ici, celui de Google.

## **L’outil saas dédié à l’analyse Seo des logs serveurs**

Jusqu’ici, pas d’information donc sur la structure du site vu par les robots et encore moins sur une éventuelle catégorisation des contenus. C’est là ou intervient l’application saas intitulée « Botify ».  Comme son nom l’indique, elle va permettre d’améliorer la perception de ce que peuvent accomplir le passage des robots et notamment celui de Google. Je n’ai pas encore le privilège de l’avoir testé, mais j’ai pu lire le blog de l’application éponyme et récupérer quelques illustrations pour démonstration. Je m’attache ici, à souligner 3 fonctionnalités qui me paraissent utiles à première vue.
Botify peut retirer des fichiers logs la structure du site par catégorisation.

[![Image](/images/blog/analysedespagespardimension-310x195.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2013/03/analysedespagespardimension.jpg) Botify : Structuration du site

Il analyse également la profondeur des pages et le corrèle avec le crawl de Google.

[![Image](/images/blog/analyse-crawl-google-310x184.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2013/03/analyse-crawl-google.jpg) Bot google selon profondeur de page

Enfin, dernier graphique, selon un critère « potentiel seo  / sans potentiel »  affecté par Botify qui correspond au moins à 1 visite organique depuis le passage de Google, met l’accent sur l’inutilité du crawl effectué sur des pages du site.

[![Image](/images/blog/url-crawlees-310x175.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2013/03/url-crawlees.jpg) Urls scannées par potentiel seo
## **L’analyse open source et celle de l’utilisateur avancé**

Il existe également cette solution open source, développée par Jean-Benoît MOINGT  et partagé ici, qui est un [analyseur de logs](http://box.watussi.fr/) . Allez sur le site watussi.fr, une vidéo explique son fonctionnement.

[![Image](/images/blog/watussiBox-310x239.gif)](https://www.mauricelargeron.com/wp-content/uploads/2013/03/watussiBox.gif) Nbre de Visites par jour de G.

François olivier , que je remercie d’avoir partagé son expérience,  nous expose  le processus d’une [méthode d’analyse de log](http://www.nicemedia.fr/blog/articles-referencement/analyses-de-logs-pour-le-seo-par-lexemple-etude-dun-cas-concret/comment-page-1#comment-12814) « pas piquée des vers » comme on dit chez nous, où par récupération des fichiers logs et un parsing avancé de ceux-ci, accomplit une analyse personnalisée du Google bot  avec un zoom sur le problème le plus saillant de l’étude de cas, le crawl sur les pages générant un code d’état « 301 » (soit une redirection).

[![Image](/images/blog/googlebot-niceMedia-310x225.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2013/03/googlebot-niceMedia.jpg) Visualisation du volume par "code état"

Retenons donc que pour aller plus loin que la simple lecture de  Google analytics standard, sans être un référenceur chevronné  *(sauf pour  la dernière démo.)*   , des solutions existent et peuvent aider à éclairer ou approfondir ses diagnostiques sur un manque de visibilité.
---
title: "Déménager son site internet précautions et usages"
date: 2013-04-10
author: "admin"
categories: ["Référencement naturel"]
tags: []
slug: "rediriger-ses-urls-pour-garder-son-referencement"
---

Les types de changements sur un site en dehors  des aménagements d'ergonomie web et les raisons pour occasionner un déménagement   peuvent être diverses.  Changer d’hébergement, de nom de domaine, de structure d’URLs  *(nouvelle taxonomie, catégorisation, organisation-arborescence)*, de migration de plateformes* (blog, ecommerce, cms)*  sont les raisons les plus fréquentes.  Ces modifications vont impacter sur **le référencement et **peuvent occasionner une chute de trafic brutale.

[![Image](/images/blog/schema-310x241.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2013/04/schema.jpg) Déménagement site : Objets, techniques et outils
## Hébergement & domaine à changement de toit , changement de loi !

### Préparer ses DNS, son adresse IP

Prenons le cas ici  d’un changement d’hébergeur et d'un nom de domaine pour un site standard. Il faut anticiper le basculement vers la nouvelle machine, le serveur qui n'est ni plus ni moins qu'un  ordinateur ! Ce dernier va accueillir les fichiers de votre site actuel. Quand on change de nom de site *(on fait appel au registrar le vendeur de domaine)* et de place  (hébergeur) , disons pour l'exemple, de l'allemand  "1 and 1" vers  le français "Ovh" , 2 paramètres sont à considérer : les DNS (domain name server),   et l'IP du serveur.  Côté DNS, la bascule entre le vieux nom de domaine et le nouveau peut prendre 24h bon poids, dont il est conseillé, de réduire le TTL (Time to Live), c’est-à-dire le cache, 1 semaine avant le basculement pour minimiser cette durée de transition. Côté data center, cela ne parait pas forcément de soit, mais optez pour un hébergeur dont les serveurs sont proches géographiquement de vos cibles visiteurs donc avec une  l’ip tricolore si vous ciblez la France  *(faîtes pas comme moi pour ce blog ;) ).*  Choisir une IP et un serveur dédié reste l’idéal, mais les mutualisés font l’affaire la plupart du temps *(et [Matt Cutts vient de le répéter pas de problème de voisinage d'Ip](http://www.abondance.com/actualites/20130410-12450-matt-cutts-et-les-sites-spammeurs-sur-un-serveur-mutualise.html), même de mauvaise réputation ! )* .

### Pensez à ses fichiers (base de données et système)

Les fichiers là aussi sont de 2 ordres, les fichiers du site, du Cms comme Joomla ! WordPress *(accessible par FTP)* et la base de données *(à synchroniser si données transactionnelles)*.  Donc faire une sauvegarde complète en cas de crash et ensuite procéder à la migration vers le nouveau serveur.  A l’installation de la base sur le serveur, il conviendra  d’adapter les paramètres du fichier configuration  à  ceux du nouvel hébergeur. Tester les scripts, et autres applications et  vérifier leur fonctionnement  dans le nouvel environnement serveur (PHP version etc..). Consulter les fichiers journaux des serveurs *(mysql/web)*  pour voir s'il n'y a pas de problème.

### Basculement du domaine

SI le nom de domaine est différent *(choix domaine : attention de ne pas opter y inclure des mots clés, le fameux [EMD](http://blog.axe-net.fr/exact-match-domain/), optez donc pour la marque, c’est plus sage),* la bascule peut se faire d’une manière transparente, en redirigeant l’ancien domaine vers le nouveau déjà installé. Dans le cas contraire, il faudra prévoir de faire cette manipulation à des heures creuses, tout en sachant qu’un délai de 24 heures est minimum bien souvent. Une **page de maintenance** pourra avertir pour  cette intervention technique *(au préalable une notification aura été diffusée  auprès de la clientèle du site dans le cadre du projet de migration). *Il est conseillé de garder le contrôle de l**’ancien domaine 6 mois** et de prévenir  Google dans l’outil webmaster tool. (choix du domaine favori).

### Migration de plateformes

Il est possible de tout changer et de passer d'un blog à un CMs, ou d'un panier vers une autre solution ecommerce. Je m'étends pas sur le sujet , mais donne comme illustration cette solution cloud de migration Add2CartMigration, ou alors des prestations sur mesure chez l'éditeur** Prestashop**.

[![Image](/images/blog/migrerunecommerce-310x244.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2013/04/migrerunecommerce.jpg) 2 Solutions de migration facile
## Lister les Urls vedettes pour le référencement organique

Concentrons-nous quelques instants sur ce qui intéresse  le référencement à proprement parlé. Un site qui possède un certain **historique chez google** , a accumulé des positions dans les moteurs de recherche en fonction des requêtes. Ses urls ont été indexées , puis classées selon un positionnement lié à la popularité des contenus qu’elles (les urls) révèlent.  Donc  au moment où l’on décide de changer quoi que ce soit dans son site, la question première que l’on doit se poser est : « **Mais que vont devenir mes urls** ? »  C’est-à-dire les adresses qui mènent à mes pages catégories, produits, articles. Le processus pour s’attacher à le moins nuire à son référencement est de faire un audit des urls indexées par Google , Bing , selon la quantité, définir des priorités, et les rediriger au bon port, soit vers leur nouvelle adresse, une par une.

### Dans Google, les urls indexées

Rien d’exceptionnel, par la commande site :monsite.com, récupérer les pages de résultats du moteur,  profitez pour vérifier les pages d’erreur 404. Selon l’importance du site, des outils de scraping seront conseillés à utiliser comme RDDZ scraper.

[![Image](/images/blog/scraper-310x223.png)](https://www.mauricelargeron.com/wp-content/uploads/2013/04/scraper.png) Extension firefox scraper
### Les adresses de pages populaires

Utiliser un outil de veille de positionnement selon les requêtes métier où l’on souhaite ne pas perdre ou du moins le moins perdre de positions.  Les urls les mieux placées devront être chouchoutées !

[![Image](/images/blog/positionnement-seo-url-310x119.png)](https://www.mauricelargeron.com/wp-content/uploads/2013/04/positionnement-seo-url.png) Les urls les mieux positionnées sur requêtes
### Avec Google Analytics aussi

Les urls qui sont le plus qualitatives en terme de fréquentation , de durée de visites. Contenu , urls de destination, nombre de visites.

[![Image](/images/blog/google-analytics-310x185.png)](https://www.mauricelargeron.com/wp-content/uploads/2013/04/google-analytics.png) Urls de destination les + fréquentées
### Les liens entrants (backlinks)

Récupérer les Urls les plus populaires, celles qui amènent du trafic récurrent. Faire un diagnostic sur plusieurs mois (un semestre donne déjà une bonne idée).

[![Image](/images/blog/majestic-seo-310x130.png)](https://www.mauricelargeron.com/wp-content/uploads/2013/04/majestic-seo.png) Les urls avec le + de backlinks

Une fois ces urls recensées  rassemblées dans une feuille de calcul , il conviendra  :

	- de faire un classement des urls  prioritaires

	- d’établir une table de correspondance (selon l’ architecture du nouveau site)

	- de sortir les doublons

	- de faire le tri des codes 200

	- de traiter les pages 404 (les regrouper thématiquement par exemple)

## **Comment faire ensuite ? La redirection 301, le sésame !**

Matt Cutts l’a dit , donc il faut suivre..Le principe est simple, à la racine du serveur, il faudra indiquer au moyen d’une syntaxe spécifique  à chaque serveur le chemin des nouvelles urls. Pas moins de 10 méthodes ont été rassemblées ci-dessous  par un développeur, bien pratique !

[![Image](/images/blog/301-syntax-310x245.png)](https://www.mauricelargeron.com/wp-content/uploads/2013/04/301-syntax.png) Syntaxes redirection 301

Je souligne ici la syntaxe la plus utilisée, spécifique au serveur apache :

Redirection 301 /connaitre-le-vocabulaire-seo/  http://www.monnouveausite.fr/vocabulaire-sur-notions-de-liens/

Si l’on ne veut pas toucher au code, des petits outils existent, limité, mais pratique si l’on sait manier le « copier-coller ». Ici, cet [outil](http://www.htaccessredirect.net/), pas dédié à la redirection 301 , mais au fichier .htaccess , qui permet de rentrer l’ancienne url et d’indiquer la nouvelle.

[![Image](/images/blog/htaccess-outil-1-310x283.png)](https://www.mauricelargeron.com/wp-content/uploads/2013/04/htaccess-outil-1.png) Outil en ligne sur 301
### Changement dans la structure interne au site

Ou alors, [celui-ci](http://seo-website-designer.com/HtAccess-301-Redirect-Generator#heading-ToolResult) , plus dédié à la redirection interne, suite par exemple à une modification de structure du site *(catégorisation, renommage des urls)*. Il génère plusieurs redirections à la fois.

[![Image](/images/blog/301-bulk-297x300.png)](https://www.mauricelargeron.com/wp-content/uploads/2013/04/301-bulk.png) Outil pour plusieurs redirections

Sinon, l’autre solution, lorsque  l’on a plusieurs dizaines de redirections, valable pour les  sites modestes, est de se servir d’une feuille de calcul , avec d’un côté les anciennes urls, de l’autre les nouvelles et de bricoler une concaténation afin de  n’avoir plus qu’à copier-coller la ligne dans le fichier htaccess. Pour des 301 plus lourdes, l'idéal est d'utiliser les expressions régulières afin de minimiser les lignes de code, et ménager ses ressources  serveur ou alors de faire développer un petit script de redirections automatiques. En outre, éviter de tout rédiriger sur la page d'accueil,  faire des regroupements thématiques.

[![Image](/images/blog/bulk-301-310x73.png)](https://www.mauricelargeron.com/wp-content/uploads/2013/04/bulk-301.png) Table Excel pour traitement multiple

Il faudra être patient et observer le **crawling du Google-bot** , mais une dizaine de jours  à  1 gros mois selon l’importance de redirections  seront nécessaires pour une re indexation, et  avant que le trafic retrouve son niveau de départ, un semestre sera pas de trop. Mais si l’accueil des nouvelles urls est fin  prêt avec un **sitemap à jour*** (xml ou html)*  des urls canoniques revues et adaptées *(attention à ne pas faire du canonical sur des redirections qu’elles soient 301 ou 302, à un moment donné il faut choisir)* ,soutenu par du contenu actualisé sur ces mêmes urls + du contenu frais, la transition devrait bien se passer. **Bon déménagement** !

**Plus d'infos sur les 301** : [http://www.annuaire-info.com/redirection-301/](http://www.annuaire-info.com/redirection-301/)
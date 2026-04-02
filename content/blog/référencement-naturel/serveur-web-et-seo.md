---
title: "Hébergement et référencement naturel"
date: 2013-03-27
author: "admin"
categories: ["Référencement naturel"]
tags: []
slug: "serveur-web-et-seo"
---

Après avoir abordé le sujet de l’analyse du crawl des robots et des erreurs rencontrées quant à l’affichage des pages d’un site, intéressons-nous cette fois-ci,  au facteur  **disponibilité d’un serveur**. Cette dernière est un des critères importants pour s’assurer d’un bon **référencement naturel**  aux yeux des moteurs, mais également pour l’**expérience utilisateur.** En effet,  en surfant sur un site, le temps de chargement s’impose comme un premier critère qualitatif pour le visiteur *(le mythe des fameuses 3 1ere secondes ! infondé !)*. Ne parlons pas  d’un éventuel crash serveur temporaire qui n’incite pas à la fidélité, sans parler d’une perte nette de chiffre d’affaires.  Les **Cms et solutions e-commerce** sont des outils bien pratiques, car leur  l’ingénierie *(mis en place en 1 clic, script, plugins, composants prêt à l’emploi)  *est séparée de leur contenu. On a donc tendance à oublier ce **socle technique** (hébergement/serveur/script), pourtant pierre angulaire d’une présence internet. Alors comment garder un œil sur un potentiel  incident ? Ou comment diagnostiquer si un site web peut tenir la charge lors d'un trafic important ?

## Surveiller le pouls de son site

Il s’agit ici de savoir si un site ou serveur observe des ralentissements ou  des petits plantages  qui passent  inaperçus mais qui, à la longue, peut faire perdre des visiteurs et des positions sur les moteurs de recherche.  Comment être alerté ? Avec l’aide de sociétés de service de  monitoring, simple à mettre en place, il suffit de s’inscrire (version gratuite ou payante), d’indiquer une url, et un agent va pinguer  le site selon des intervalles de temps que l’on peut personnaliser (tous les heurs, minutes..). Le service setuptime par exemple,  propose en gratuité un moniteur http, dans des tranches allant de 30 à 60 minutes.  D’autres services en plus du contrôle de serveur web sont proposés,  comme l’email, le ftp…

[![Image](https://www.mauricelargeron.com/wp-content/uploads/2013/03/surveillance-310x167.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2013/03/surveillance.jpg) Monitorer son serveur

Ici le mois de mars se voit pénalisé de 7 plantages, que l’on pourra peut-être recoupé avec l’analyse des fichiers logs.

Mais allons un petit peu plus loin dans la surveillance, avec le service de Monitis dont l’agent http va non seulement relever les « outages » *(voir « 1 » sur illustration)  *c’est-à-dire les plantages, mais également , les effets de latence, observés sur des hits ou requêtes effectuées sur la plateforme web  *(appels  serveur web sur des fonctionnalités du site avec réponses + ou - rapides (voir « 2 »))*.

[![Image](https://www.mauricelargeron.com/wp-content/uploads/2013/03/http-minitoring-310x264.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2013/03/http-minitoring.jpg) Surveillance avancée serveur Web
## Analyser les raisons des dysfonctionnements

Un des premiers outils, est de se référer aux **fichiers journaux**, et de repérer le moment où a eu lieu l’incident, et d’essayer de trouver l’origine du problème. Les fichiers log peuvent nous fournir les renseignements nécessaires pour identifier le ou les problèmes. Ce 26 mars, le site à mise quasiment 8 secondes pour répondre à une demande, le fichier log montre 51 hits au même moment. Quels sont les scripts incriminés, les pages concernées ?  Que donne l’analyse des fichiers log de la base de données MySQL ?

[![Image](https://www.mauricelargeron.com/wp-content/uploads/2013/03/mlc-310x208.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2013/03/mlc.jpg) Analyse des fichiers log Mysql et Accès Web

Si une page semble incriminée, une analyse de l’url avec pour but d’analyser son chargement  *(avec un outil comme par exemple http://www.webpagetest.org)*  peut apporter quelque éléments à l’analyse. On s’aperçoit que le time to first byte, le temps  de la première donnée en gros dans le header du navigateur, est de plus de 7 secondes ! D'autres outils comme [gomez ](http://www.gomeznetworks.com/custom/instant_test.html) donne des chiffres différents pour ce TTFB *(le mode de calcul est différent)*. Bref, quoiqu'il en soit, cet indicateur plus les autres, donne une idée sur la réactivité de la page portée par le serveur.

[![Image](https://www.mauricelargeron.com/wp-content/uploads/2013/03/analyse-time-to-first-byte1-310x207.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2013/03/analyse-time-to-first-byte1.jpg) Analyse de la page avec 2 outils différents
## Corriger pour éviter la répétition des problèmes

Est-ce une défaillance  du serveur ou du site ? Le « **Time to First Byte **» souligne la connexion du navigateur au serveur au travers de 5 principales étapes : Dns look up, connexion initiale, attente, réception et fermeture. C’est le temps d’attente du navigateur de l’internaute auprès du serveur. Passé 100 ms pour des données statistiques *(html, image, css, js) *est correct, 200 à 500  pour du dynamique* (script php de liaison à la base de données, requêtes..) *l'est aussi .

### **TTFB réellement important ?**

Tout dépend donc de l’application sur le site web et des capacités matérielles côté serveur *(entrée sortie disque, ram, goulot étranglement réseau hébergeur)*. De plus, il faut aussi prendre en considération l’aspect configuration logicielle du serveur *(apache/Windows, php/iris, la configuration de la base de données et la capacité de charge réseau allouée par l’hébergeur).* Selon Jeffrey Huckaby, fondateur de la société Rackaid,  si d’une part, le TTFB est important pour du contenu statique, la configuration matérielle serveur est en cause* (logique, non ?)* et si d’autre part, si le TTFB est bas pour du statique mais haut pour du « dynamique » la configuration logicielle  du serveur ou de l’application *(ici donc du  site)* est à mettre en cause. C'est donc du cas par cas :(

### **Cdn, Gzip, Etag et autre template..**

Est-on bien avancé dans tout cela ? Certains diront, que ce qui compte, c'est la possibilité de **compression** ([gzip](http://www.alsacreations.com/article/lire/914-compression-pages-html-css-gzip-deflate.html)) qui fait la différence dans le temps total de charge de la page. Quant à l'Etag, autre fonctionnalité serveur qui permet d'utiliser d'une manière optimale le cache navigateur pour afficher automatiquement la version d'un document, les avis divergent *(voir lien fin article)* .  **Le mieux c’est de tester**. Personnellement, je me suis aperçu qu’un doux mélange était de règle pour les cas évoqués plus haut, une configuration logicielle serveur à mettre à jour (version php) une base MySQL à optimiser* (1s de gagné)* , plus un **Template** à changer ou à améliorer *(gain de 2 à 3 secondes !)* . En aucun cas, la capacité (mat.)  du serveur mutualisé n’était la cause.

Alléger les sollicitation serveur passe aussi par l'usage de **Content delivery Network** (cdn) qui pallie aux appels multiples ici et là pour afficher tel ou tel widgets, plugins sociaux. Cloudfare avec une version gratuite sur des serveurs localisés sur Paris offre un panel de service.

[![Image](https://www.mauricelargeron.com/wp-content/uploads/2013/03/cloufare-310x215.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2013/03/cloufare.jpg) Un service Cdn abordable : [cloudfare](http://www.cloudflare.com/)
## Subvenir à une montée d'audience ou à un pic ponctuel de popularité.

Cependant, il peut s’avérer qu’avec le temps, et les différentes opérations d’**acquisition de popularité** *(presse, emailing de masse ciblé..bien sûr ;) )*, de campagnes de référencement naturel, plus  l'embonpoint par l'ajout de fonctionnalités *(plugins, composants)* son serveur n’encaisse **plus la charge** du à l’audience *(bon, ce n’est pas mon cas:( ).* Webserver stress est un outil qui permet d'accomplir 3 types de test (nombre de clics, charge pendant une durée ou progressive), une simulation jusqu'à 200 utilisateurs est possible. Cela couvre pas mal de besoin. Un reporting indique les défaillances à combler.

[![Image](https://www.mauricelargeron.com/wp-content/uploads/2013/03/simulation-charge-310x212.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2013/03/simulation-charge.jpg) Stress test sur serveur

Les techniques du** Cloud et de la virtualisation** sont là pour répondre à ces pics de charge ponctuels. Une société comme Gandi propose des serveurs de base à prix abordables et pouvant évoluer selon les developpements des scripts* (wordpress, prestashop, joomla!, drupal..)*. Pour des sites à grosse fréquentation, un serveur dédié pourra faire l’affaire, avec le même principe d’allocations de ressources personnalisées.

[![Image](https://www.mauricelargeron.com/wp-content/uploads/2013/03/gandi-serveur-web-310x168.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2013/03/gandi-serveur-web.jpg) Serveurs modulables chez Gandi

Finalement, le choix d'un hébergement peut aussi se faire selon l'affinité de l'hébergeur sur certains scripts :

	- Un [article intéressant au sujet de joomla! ](http://www.nosyweb.fr/outils-pour-joomla/quel-hebergeur-choisir-pour-installer-joomla.html) .

	- Le sujet (anglais) pour Wpress:  [http://www.creativedevelopment.com.au/marketing/increase-wordpress-speed-a-complete-guide/](http://www.creativedevelopment.com.au/marketing/increase-wordpress-speed-a-complete-guide/)

	- Etag : [http://w3techs.com/technologies/comparison/ce-etag,ce-gzipcompression](http://w3techs.com/technologies/comparison/ce-etag,ce-gzipcompression) +  [http://www.takeitweb.fr/blog/configurer-etags.html](http://www.takeitweb.fr/blog/configurer-etags.html)

	- Technique Msdn (GB), plus général  : [http://msdn.microsoft.com/en-us/magazine/dd188562.aspx](http://msdn.microsoft.com/en-us/magazine/dd188562.aspx)
---
title: "1001 façons de pirater un site"
date: 2014-06-13
author: "admin"
categories: ["Référencement naturel"]
tags: []
slug: "proteger-son-serveur-des-intrusions"
---

Un des aspects de l’**optimisation d’un site pour les moteurs de recherche** passe par sa sécurisation. Sans devenir  expert « sécurité », il est bon néanmoins de connaître les rudiments  sur ce que sont les différentes attaques possibles. Connaître les menaces plus courantes et essayer de s’en prémunir, faire de la prévention plutôt que de la réparation  est l’objectif de cette article ! Les affaires wikiLeaks et autre NSA  sont les témoins marquants que le numérique, par sa capacité à envahir nos vies quotidiennes,  constitue un monstre aux chevilles bien fragiles !

## **Avant tout sécuriser son serveur**

Souvent oubliée, la protection d'un site passe d'abord par celle, matérielle, des salles des centres serveurs qui abrite la machinerie des disques durs (salle blanches, protection thermique, incendie, sécurité d'accès). Ensuite, bien que transparent pour les éditeurs lambda de sites internet hébergés sur des serveurs mutualisés où la tâche de **configuration, maintenance, mise à jour** est du devoir de l’hébergeur (ovh, 1and1 pour les plus connus), les pratiques pour sécuriser une  machine sont dans l’idéal :

	- de  procéder à une veille constante sur les nouvelles menaces via l’analyse des fichiers logs

	- d’utiliser des modules dédiés à la sécurité (ex : mod_security for apache)

	- de supprimer des extensions inutiles livrées out of the box sur les serveurs apache, Microsoft

	- de monitorer tous les accès utilisateurs (supprimer ceux inutilisés) et minimiser les permissions et privilèges

	- de procéder aux mises à jour (patchs à appliquer)

	- de localiser physiquement l’application web ou les fichiers d’un site et ses scripts sur des partitions différentes de celles où résident les fichiers systèmes du système d’exploitation du serveur (risque de prise en main totale du disque). Enfin, Séparer les serveurs de productions de ceux de tests (éviter le nommage de répertoires comme /tests/ /essais/

	- de donner l’accès distant à l’admistration des serveurs uniquement via des tunnels cryptés et sécurisés et réservés uniquement à certaines adresses ips.

## **Panorama des différents types d’attaques**

### **Un vingtaine de types d’attaques !**

Les **vulnérabilités** sont nombreuses, sans devenir parano non  plus, et devenir « Hypo-Web-Driac », bien souvent, les faiblesses proviennent soit d’un code qui ne valide pas assez les entrées d’utilisateurs via les formulaires, ou avec des  urls sans protection, soit  de mécanismes d’authentification (login) défaillants ,  ou alors de parades absentes dans le traitement des erreurs, sans oublier aussi les manques de procédures pour fermer  les connexions à  la base de donnée.

L’accès le plus commun est celui par le protocole http sur les ports 80/443 et l’aire de jeu  du hacker se délimite sur l’écosystème du serveur web : **client et  serveur**.

Pour illustrer le panel de ces attaques, les infos fournit par le consortium** WASC** sont intéressantes.  Le Web Application Security Consortium  rassemble des experts internationaux, des industriels, des représentants d’organisations, son objet est de fournir des standards ‘open source’ de sécurisation basées sur les plus consensuelles bonnes pratiques en la matière.

Le schéma ci-dessous fait apparaître pas mois de 24 catégories dont les 3 principales sont le déni de service, l’injection SQL et le XSS (acronyme de Cross Site Scripting).  Je reviens sur ces trois attaques dans le paragraphe suivant. Bien sûr, la part  la plus importante néanmoins intitulée  «Inconnue» sur le graphique représente les attaques  non identifiées, une sorte d’item  « autre ». A noter qu’en 2011, elle ne représenté que 18 % ! Cela signifie-t-il une progression des techniques nouvelles de hacking ? Ou alors tout simplement un manque d’expertise des acteurs qui font remonter leur expérience lors d’incidents ? Cela mériterait plus d’investigations. Néanmoins, le principal à retenir, c’est l’éventail des moyens possible pour pénétrer sur un site ou son serveur.

[![Image](https://www.mauricelargeron.com/wp-content/uploads/2014/06/les-typologies-atttaques-site-web-2014-310x281.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2014/06/les-typologies-atttaques-site-web-2014.jpg) 23 Types d'attaques recencées
### **Quelques définitions sur ces types d’intrusions**

**Brute Force** : via des requêtes GET ou POST , avec des valeurs prédéterminées, le but est d’attaquer le système d’authentification par différents biais comme la mise en place de cookies, l’ajout d’entête http, l’utilisation d’un proxy, de tester des connexions https etc..

**Predictable Resource Location** : Analyse  les urls ou champs de formulaires et leur chemin d’accès respectifs à certaines références de  documents internes (champs de base de données, répertoires, fichiers). Le but est de récupérer des sauvegardes , des fichiers logs par exemple.

### **Des failles sur les Scripts du Marché**

SI l’on devait thématiser le type d’attaque, on peut parler de celles qui affectent  le plus les scripts du marché comme ceux sur Wordpress, Joomla !, Spip, Drupal..

[![Image](https://www.mauricelargeron.com/wp-content/uploads/2014/06/CMS-vulnerabilites-289x300.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2014/06/CMS-vulnerabilites.jpg) Failles sur les CMS par le CVE

**Des attaques thématisées : focus Seo sur serp Google**

Celle plus communément appelée «Pharma Hacks » sur des sites WordPress. Mais il y a en bien d’autres, consiste à s’introduire sur des plateformes CMS et d’y introduire des fichiers cachés, bien souvent dans des repertoires accessibles aux plugins et en lien avec la base de données.  Ils vont fabriquer des pages munis de textes, liens  ou insérer à la volée sur des contenus destinées aux moteurs, des bannières faisant la promotion d’un produit (comme le  Via..).

[![Image](https://www.mauricelargeron.com/wp-content/uploads/2014/06/pages-spam-310x224.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2014/06/pages-spam.jpg) Vue d'une Page hackée par le V.
## **Se protéger des intrusions les plus probables**

## 

### **Le Déni de service**

C’est sans doute la plus connue de toutes les attaques, car la plus simple à employer, sans matériel poussé. Elle consiste à pour but de rentre le serveur web inaccessible par une attaque ciblée sur un de ses services. Sans rentrer dans les détails techniques, c’est mettre à mal la synchronisation du serveur par une avalanche de demandes. Les procédés sont connus et touchent principalement les couches du protocole TCP/IP qui permettent le dialogue entre serveurs et machines clientes. On parle d’UDP flooding, de Syn Flood, de l’envoi de paquets fragmentés.

[![Image](https://www.mauricelargeron.com/wp-content/uploads/2014/06/ss-310x247.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2014/06/ss.jpg) Techniques DOS

 Les parades sont difficiles, l’identification et un filtrage des assaillants (adresses ips) est un moyen de refouler ces requêtes malveillantes, sinon une architecture serveurs avec plusieurs serveurs  permettent de répartir ces flux de requêtes, ou bien la présence d’un serveur « qui défend » et prévient les demandes suspectes est aussi une parade.

### **L’injection Structured Query Language**

Dû à une défaillance dans le codage d’un script , d’une application web par son développeur . Elle permet à une personne malveillante de prendre le contrôle d’une BDD via des  commandes sql par le biais de services comme :

	- un formulaire d’identification, de demande d’information..

	- les résultats d’un moteur de recherche

	- la constitution d’un panier d’articles

Pour lutter contre ses accès intempestifs, il convient :

	- de détecter et de vérifier la longueur des champs ciblés (ceux des utilisateurs par exemple : username) ,

	- de stopper l’application au bout d’un certain labs de temps d’exécution

	- de supprimer les méta-caractères  ( `, ``, \)

	- de placer un parefeu

	- de mettre en place des requêtes préparées

### **XSS ou Cross Scripting Script**

Son  exécution

Cette technique se passe côté client, donc sur un browser (firefox, chrome, Ie) et permet d’insérer une syntaxe de code sur une page web. Elle vise l’utilisateur et son navigateur,  plus que le site web en lui-même.  La page devient contaminée par un script malveillant qui va toucher la navigation et la visite du site et va, entre  autres,  pouvoir :

	- Rediriger le site

	- Collecter les cookies de la machine utilisateur

	- Afficher un formulaire pernicieux

Exemple : sur une url de type :

	- http://www.monsite.com/mon-pertoire/mon-article?id=1526

	- Rajouter un petit script qui peut ouvrir une boîte de dialogue dans le navigateur en remplaçant le chiffre de l’id .

	- http://www.monsite.com/mon-pertoire/mon-article?id=alert('eh voila une faille xss)

[![Image](https://www.mauricelargeron.com/wp-content/uploads/2014/06/xss-310x123.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2014/06/xss.jpg) Faille Xss

Deux types de faille XSS  sont répertoriées :

	- la persistente, la plus dangereuse car permanente, le code trojan est bien situé sur le serveur mais s’exécute sur le navigateur.

	- La réflexive, ou l’execution du script est conditionné par une action obligatoire de la part du visiteur.

### **Les Bot Net d'une manière générale**

Ces petits programmes spamment le web et sont introduits à l'insu des visiteurs  dans des pièces jointes  bien souvent ou sur des pages web. Ils  hackent le navigateur et agissent sur le parcours des internautes. Ils sont les auteurs des attaques mentionnées ci-dessus mais aussi de bien d'autres comme les simulation de visites, blocage sur certaines urls, récupération de données propriétaires ..mais on s'éloigne du sujet...
### **Les remèdes**

*Côté utilisateur*

	- Laisser des droits limités à son pc

	- Désactiver certaines fonctionnalités (exécution de scripts par le navigateur)

*Côté serveur*

	- Filtrer les données retournées dans le codage de l’application

	- Vérifier les syntaxes  des entrées utilisateurs par échappement de caractères ou chaîne et principalement les () . Utiliser les librairies spécialisées comme ESAPI de Owasp ou AntiXss de Microsoft évite aussi de s’auto-créer des ennuis.

## **Outils : Tests & diagnostics - Tutos et  Veille**

Dans le cadre d’un audit de sécurité, des outils  existent pour scanner les vulnérabilités.

	- Problème de sécurité : [Google webmaster tool](https://support.google.com/webmasters/answer/163635?hl=fr&ref_topic=6001942) mais bon, pas très fiable.

	- Solutions d’application Open Source de tests par [IsecPartners](https://www.isecpartners.com/tools/application-security.aspx)

	- Scanners online : [www.acunetix.com/](https://www.acunetix.com/) ou [NetSparker](https://www.netsparker.com/)

	- Modules : [mod_security sur apache ](http://www.unixgarden.com/index.php/misc/securite-avancee-du-serveur-web-apache-mod_security-et-mod_dosevasive) (un peu ancien mais pédagogique)

	- Tutoriel de [Sécurisation d’ un serveur apache](http://www.tontonfred.net/blog/?p=1401)

	- Toutes les catégories de failles par l’[OWASP](https://www.owasp.org/index.php/Category:Attack)  (Open Web Application Security Project)

	- [Plugins](http://www.acunetix.com/websitesecurity/wordpress-security-plugin/) Wordpress pour sécuriser le CMS (vérifier la version)

	- [WASC](http://projects.webappsec.org/w/page/13246995/Web-Hacking-Incident-Database) et sa base d’incidents

	- [Base de données](http://www.cvedetails.com/) de vulnérabilités

	- [Podcast de Finn Brunton ](http://www.franceculture.fr/emission-place-de-la-toile-entretien-avec-finn-brunton-auteur-de-%C2%ABspam%C2%BB-2014-05-31)auteur d'un ouvrage sur le Spam

	- Cartographie Attaque DDos : [http://www.digitalattackmap.com/](http://www.digitalattackmap.com/)
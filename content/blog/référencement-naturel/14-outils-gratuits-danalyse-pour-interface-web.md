---
title: "30 paramètres de controle pour auditer un site internet"
date: 2012-04-12
author: "admin"
categories: ["Référencement naturel"]
tags: []
slug: "14-outils-gratuits-danalyse-pour-interface-web"
---

L’audit technique en vue d**'optimiser son référencement** fait partie des incontournables lors d’un audit «seo » d’un site internet. Il est bien évidemment important de l’effectuer avant toute campagne de  liens sponsorisés ou organiques. Ces temps derniers, Google a fait remarquer qu’il apportait une importance certaine à  la vitesse de chargement de la page, à la qualité de l'hébergement du site , à  l' organisation de la structure du site sur la plateforme.

Je fais donc faire un inventaire des **principaux facteurs seo** à prendre en compte lors d’un audit de site, mais ce dernier peut être aussi utilisé comme cahier des charges technique lors d’un projet de site web.  J'ai catégorisé cette liste en 3 chapîtres : N**om de domaine**,** Hébergement** et** Site** *(et ses pages)* en soulignant en préambule l'intérêt au point de vue du référencement et en indiquant le nom de quelques outils, tous gratuits ( quand même  ), à retrouver très facilement sur votre moteur de recherche préféré. Je n'ai pas mis les liens pour que vous puissiez rester le plus longtemps sur ma page ;).

## **Nom de domaine **

-> Intérêt seo : **positionnement / visibilité** * (outil domaine : gandi.net)*

	- Présence de **multiples noms de domaine** ? les Redirections  sont –elles correctes ? , si oui, comment sont faites les redirections ? (301/302), la balise ‘canonical ‘ est-elle présente ? *( Xenu)*

	- Vérification du** pointage du répertoire** par le  nom de domaine (choix Sous répertoire / sous domaine) : l’url du domaine  est-elle bien positionnée sur le répertoire qui abrite les fichiers du site, soit généralement sur http://www.mondomaine.com et non par sur http://www.mondomaine.com/fr/accueil

	- Utilisation des **Extensions** ? (Fr ou .com) : A justifier selon la nature du site (e-commerce, blog, vitrine)

	- **Longueur du nom du  Domaine** : moyenne 11 caractères, pas de règles mais mieux vaut court que long, en général.

	- Domaining :** Protection de son domaine** (Tld),  Est-ce que les domaines autres  que le principal sont à réserver afin d’éviter une déviation frauduleuse de trafic. Généralement, les principaux sont parfois utiles à réserver (.com, .Fr)

	- Checking du domaine (Spammy ou pas) ? : présence de multiple** mots clés**, avec ou sans tirets ? Cette technique (insertion keyword) est encore utile aussi bien sur Google que sur les autres moteurs dans la mesure où la requête correspond exactement  au  nom de domaine. Voire fig-1

[![fig-1-mots-cles-domaine-300x161.jpg](/images/blog/fig-1-mots-cles-domaine-300x161.jpg) Mots clés dans domaine = requête internaute

## **Hébergement / Serveur **

-> Intérêt seo :** Crawlabilité, accessibilité** *( 404checker.com/ ; whois.domaintools.com/ )*

	- **Contrôle IP** dédiée *(class c par ex (utile pour la sécurité et stabilité))* ou  IP mutualisée ?

	- Scanning de  l’**entête http**  : Scanner les  erreurs serveurs de 1xx (information), 2xx (succès), 3xx (redirection), 4xx (erreur client) &  5xx (serveur indisponible)

	- Faire un **Reverse IP** : Connaître l’environnement de la plateforme (IP dédiée, combien de domaines si mutualisé)

	- Lancer un **Whois** : Connaître la nature de l’hébergement (lieu, nom  hébergeur), l’historique du domaine, sa validité.

	- Paramétrage d’**Etag** : Voir si optimisation du cache pour afficher le document (attention pas forcément si  clustérisation des serveurs)

	- Vérification de la **réponse du serveur** : quel temps de réponse selon différent routage (différentes requêtes depuis différentes localisation de serveurs, outil : http://www.iwebtool.com/speed_test)

	- **404 page erreur** : Si la page n’existe plus une erreur 404 doit être générée (il suffit d’appeler une page qui n’existe pas et d’examiner l’erreur affichée)

	- Y a –t-il un fichier **robot.txt **? Ce fichier permet de bloquer l’accès à des pages dont l’indexation est inutile (CGV, page de connexion..), d’indiquer le miroir principal, résultats de recherche sur le site, pages techniques..

	- Un **sitemap** a –t-il été prévu ? Ce fichier XML indique une liste d’url à crawlé pour les robots des moteurs avec indication d’une fréquence de mise à jour.

	- Listing des **liens cassés**. urls qui n’aboutissent à rien, à éliminer

	- Présence ou non d’un **taguage  statistique**  type Xiti, Google analytics

	- Enumération des **liens sortants** et **internes** de leurs balises (attributs : no follow) redirections etc.

	- Vérification pour  **sites multilingues multirégionaux des liens** (urls) adaptés de type : - 

	- **IP du serveur** est-elle** blacklistée ** (serveur mail) ? Peut s’avérer pénalisant lors d’envoi d’email avec le nom de domaine du site (classement serveur courrier destinataire comme spam).

	- Examination des différentes** composantes  d’optimisation de chargement de la page** dont 7 principales :

Code **css**, code** Javascript**, scripts divers *(**flash**..)* = vérification de leur optimisation et de leur place dans la page *(code asynchrone oui  ou différé=  ok* ). Requêtes serveur *(le moins possible)*, optimisation des images *(taille ajustée)*, jeu de caractères *(ex :utf-8)*, connexion persistante* (keep-alive : diminution latence)*..

[![fig-2-whois-300x241.jpg](/images/blog/fig-2-whois-300x241.jpg) fig-2-Outil whois
## **Site et ses pages**

-> Intérêt seo : **Indexation, positionnement, contenu** *( screaming frog seo spider , xenu, virante)*

	- Contrôle de la** pagination** :  utilisation des liens de type **rel="next"**** ****et**** ****rel="prev"**** **pour relier les URLs entre elles.

	- Présence de **contenu dupliqué** : Scan de toutes les urls du site afin de vérifier si pour chaque url aboutit à un contenu unique sinon, il y a contenu en double, erreur technique sanctionnée par Google. Utiliser comme remède pour les contenus préférés la balise  « canonical » afin d’indiquer l’url la plus pertinente à prendre en compte. (Outil Google webmaster tool)

	- **Url rewriting **: Réécriture d’urls, essentiellement pour les urls dynamiques ou il convient d’indiquer à Google de ne pas prendre en compte certains paramètres comme les Ids, session utilisateur. Le but ici est de rendre plus lisible pour les robots mais aussi pour les internautes les adresses des liens contenues dans le  navigateur.

[![fig-4-duplicate-content-300x214.jpg](/images/blog/fig-4-duplicate-content-300x214.jpg) Trouver le contenu dupliqué de son site

-> Intérêt seo : **Contenu, positionnement de page selon 1  stratégie mot clé * (****Outils : Extensions navigateur Seomoz.org ,ObservePoint, Wasp, YSlow, Seo4Firefox,kgen)*****

	- Passage en revue de ** 10 critères de balisage html** de chaque page selon l’optimisation de la thématique de la page (fameux mot clé !) et l’état de la concurrence :

Titre, Url, Meta Description, H1, H2-H4, Body, B/Gras IMG ALT, Ancre de texte (liens**), lien **canonique (indique la page principale à indexer).

Attention ici  à ne pas **sur-optimiser les pages** avec des mots clés redondants et en sur nombre.

[![fig-5-content-checking-300x225.jpg](/images/blog/fig-5-content-checking-300x225.jpg) fig-5 Vérification du balisage contenu d'une page

	- Recensement d’un formatage standard du contenu à l’aide de **rich snippets** (Méta balisage normé pour indiquer les origines d’une source (auteur, musique, livre..Outil : schema.org) . Peut aider dans la popularité d’une page, car son aspect attrayant peu encourager le lecteur à cliquer sur ce lien.

[![fig-6-schema-org-300x104.jpg](/images/blog/fig-6-schema-org-300x104.jpg) Méta données & Micro-formatage du contenu

**Intérêt seo : expérience utilisateur (ergonomie) / Popularité**

	- Présence d’un** fil d’Ariane** (breadcrumbs) utile pour aider le visiteur à se retrouver dans un site

	- **Plan du site** : même objectif que précédent (équivalent du sitemap.xml pour les robots)

	- Possibilité de** boutons sociaux de partage** (vers les plateformes sociales Fb, Twitter, Google+)

Cette liste n'est pas exhautive, et les focus d'optimisation évoluent selon l'importance (filtres) que leur accorde les moteurs de recherche.
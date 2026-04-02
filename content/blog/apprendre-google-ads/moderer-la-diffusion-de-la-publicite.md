---
title: "Brave :  navigateur web médiateur publicitaire"
date: 2016-02-01
author: "admin"
categories: ["Apprendre Google Ads"]
tags: []
slug: "moderer-la-diffusion-de-la-publicite"
---

Les [navigateurs internet](https://fr.wikipedia.org/wiki/Navigateur_web) constituent un objet bien utile pour deviner ou construire un  profil utilisateur  et **qualifier une audience**.  On peut se demander d’ailleurs comment  Google utilise Chrome pour aspirer de la data utilisateur :s . La récente actualité sur les ad-blockers est directement liée au sujet de cette semaine où  une perte  de plus de  40 milliards de dollars est évaluée côté éditeurs de sites web. Alors comment trouver un juste équilibre et garantir **un web gratuit respectueux des internautes** ? «**  Brave** »  apporte sans doute un début de réponse sur ce marché déjà bien mature.

[![Image](https://www.mauricelargeron.com/wp-content/uploads/2016/01/part-de-marche-des-navigateurs-310x178.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2016/01/part-de-marche-des-navigateurs.jpg) Part de marche des navigateurs Pc et Mobile
## **Brave, un navigateur responsable ?**

J’ai pu déjà citer le nom de * [Brendan Eich](https://www.mauricelargeron.com/js-et-les-moteurs-de-recherche/)*, créateur du JS et ex CEO de Firefox Corporation, et le revoilà à niveau dans ce projet de Navigateur durable, fondée sur le noyau open source **Chromium** crée par Google. Son origine tient sans doute sur le fait que les éditeurs, médias, sont allés trop loin dans l’intrusivité  de la publicité. Pop-ip envahissantes, vidéos imposées, impossibilité pour l’internaute que de fermer sa page ,  et d’installer  un bloqueur de pub : un** ad-block**, ou de jeter son pc par la fenêtre.

Trois arguments peuvent résumer cette initiative

 	- **Rapidité** : annoncé comme **40% plus rapide** que les principaux navigateurs du marché. La vidéo qui circule entre Safari et Brave.

https://www.youtube.com/watch?v=kHWf6hRV-GM

 	- **Liberté** : possibilité de choisir le type d’affichage publicitaire avec 3 choix possibles : le choix par défaut « replaced ads » filtrera les publicités abusives et laissera passer le nécessaire. « Block ads bloquera toutes les publicités et enfin le non filtrage où toutes les publicités sont affichées. Le MUST, c’est la fonctionnalité à venir dans les prochains mois  dont le principe est celui du **micro-paiement** pour des sites que l’on souhaite consulter sans publicité.

 	- **Sécurité **: la technologie « **https everywhere **» sera embarquée par défaut sur le navigateur, elle garantit une sécurité renforcée sur des sites vulnérables dont l’https n’est pas optimisé.

[![Image](https://www.mauricelargeron.com/wp-content/uploads/2016/01/navigation-plus-sure-310x62.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2016/01/navigation-plus-sure.jpg) Techno. "Https EveryWhere"

Selon l’équipe de conception de Brave, le modèle économique reposera sur au minimum 7 millions d’utilisateurs. Au même titre d’edge de microsoft, firefox qui imposent de plus en plus de sécurité côté utilisateur, Brave place t-il la barre plus haute ?

## **Brave et Google Chrome **

En guise de test, non scientifique :)  , j’ai téléchargé la version developer de ce nouveau navigateur qui n’offre pas de configuration personnalisée pour l’instant. J’ai souhaité me rendre compte de sa rapidité et observer le trafic envoyé entre ma machine et le serveur. J’ai fait donc la comparaison sur une requête « [formation webmarketing Bordeaux](https://www.mauricelargeron.com/ateliers-referencement-bordeaux/) » sur  Google avec Chrome (en  navigation privée, vidée des addons, cache etc..)  et sur Brave.

[![Image](https://www.mauricelargeron.com/wp-content/uploads/2016/01/web-traffic-from-brave-chromium-310x166.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2016/01/web-traffic-from-brave-chromium.jpg) Web trafic depuis Brave chromium

J’ai pu constater une vitesse de chargement sensiblement équivalente entre les 2 browsers. Pour ce qui est de la data passée par les navigateurs, la comparaison est plus nuancée.  Fiddler, un outil de développement JS qui intercepte les flux entre client et serveur démontrerai que **G. Chrome serait plus gourmand d’informations**. Sans rentrer techniquement dans les appels de données, 20 lignes sont enregistrées par G. Chrome et seulement 8 pour Brave avec aucune donnée en cache à priori stockée localement.

[![Image](https://www.mauricelargeron.com/wp-content/uploads/2016/01/web-traffic-from-google-chrome-310x215.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2016/01/web-traffic-from-google-chrome.jpg) Data Google Chrome

Mais au fait, **que se passe–t-il lors d’une connexion sur l’internet ?** Où autrement dit, quelle est la nature du dialogue entre le Browser de l’ ordinateur, pc et le serveur ?

## **Connexion à internet et informations utilisateurs **

Entre la paranoïa et l'angelisme , le navigateur, pièce maîtresse de la connaissance visiteur. reste néanmoins un outil indispensable pour relier un site (serveur) et son visiteur  (client : device)  via un protocole ouvert l’http, merci à **[Tim Berner Lee](https://www.mauricelargeron.com/historique-de-la-toile-depuis-les-annees-90/)** et équipe pour cette invention.

**8 étapes principales lors d’une visite d’une page web**

 	- Appelle de la page : http://www.siteweb.com

 	- Navigateur recherche les Dns de http://www.siteweb.com (adresse machine ou se trouve le site)

 	- Envoi d’une demande au serveur web : GET http://siteweb.com/ http/1.1 (accept, user Agent..

 	- Si redirection, serveur envoi une 301 : HHTP :1.1 301 Moved Permanently, cache control, set cookie..

 	- Génération d’une page HTML du serveur vers le client : HHTP :1.1 200 OK ? Content-Encodiing :Gzip

 	- Affichage de la page

 	- Navigateur envoi des demandes (GET) d’objets situées dans le code Html : images, css, Js

 	- Si codage AJAX, la page reste chargée mais les appels de contenus utilisateur circulent : « xml/>

Lorsqu’un internaute se connecte sur un site internet, c’est pas moins donc qu’une vingtaine d’indicateurs qui sont transmis lors d’une connexion et cela sans aucun engagement spécifique du visiteur. Voilà résumé les principales données envoyées au serveur web, lors de l’appelle de la page par le surfeur web :

 	- **Connexion** : adresse Ip, (à partir de laquelle des commandes Whois, DNS : identification du FAI : free, orange etc.., traceroute : chemin entrepris depuis le serveur jusqu’au client via les routeurs) port, format requête, chiffrement, authentification

 	- **http headers** : hôte, référent, user-agent (type de navigateur)

 	- **Cookies** : de sessions ou persistants

 	- **Langages** acceptés par le navigateur : Js, VB script, Java, plugins installés, heure locales, type d’écran et de résolution

Précisons aussi que le  navigateur est une porte d’entrée pour les malware, et pour cause, c’est l’unique porte d’entrée sur le web mise à part les applications bien sûr. Ces programmes malveillants viennent ensuite se loger dans la base de registre Windows et manipule le navigateur pour enclencher des comportements intempestifs : redirections forcées vers des pages de publicité (ex :).

Téléchargement de Brave : [https://www.brave.com/](https://www.brave.com/)
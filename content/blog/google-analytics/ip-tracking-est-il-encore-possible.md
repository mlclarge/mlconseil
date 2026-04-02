---
title: "Ip intelligence un outil web marketing en devenir ?"
date: 2013-08-07
author: "admin"
categories: ["Google Analytics"]
tags: []
slug: "ip-tracking-est-il-encore-possible"
---

Voyage et tourisme sont plutôt d’actualité ces temps-ci, donc j’en profite pour parler d’un sujet qui a défrayé la chronique récemment au sujet de « l’ **IP Tracking **» sur ces métiers. En effet, le prix de billets, des prestations  de ces sites web fournisseurs de services * (comme les agences de voyage ou transporteurs de personnes)*  seraient à même d’utiliser des techniques d’incitation à la vente plus ou moins contestée, en augmentant les tarifs selon les comportements visiteurs.

Bon sujet de **web marketing** n’est-ce pas ?  Le E-**marketing comportemental** ne date pas d’hier, mais revient au gout du jour. Servir les bonnes publicités en temps réel à la bonne cible, mettre en avant les bons produits au bon moment, recibler pour rattraper une vente échouée, tenter d'identifier les visiteurs, voilà les principales raisons des techniques de tracking.  Je ne parle pas de l’amalgame possible avec les révélations du programme prism ;) ! Bref, en étant un peu parano, on est tous fliqués, c’est un véritable complot ! D’ailleurs dans un papier du **Monde.fr**, pas moins de la moitié de nos données seraient utilisées à des fins commerciales ! Allons bon..

A des fins technico-pragmatiques, je tenterai ici de recadrer l’historique et le juridique du sujet, puis ferai un focus technique sur l’ip tracking, et parlerai des fournisseurs de service d’ip intelligence.

## **Historique et juridique**

Cela fait déjà  quelques années que des plaintes régulièrement font évoluer le législateur.  Les motifs invoqués sont l’utilisation illégales des données personnelles et la pratique commerciale trompeuse (code du commerce). Alors l’adresse IP serait considérée comme une donnée personnelle selon le contrôleur européen de protection des données et sa collecte devrait être mentionnée dans les **conditions générales de vente du site web**. Actuellement d’ailleurs,  des discussions sont en cours au niveau européen sur l’usage des données personnelles. Mais cela ressort pour l’instant de la compétence nationale  selon l’Europe ([directive 95/46/CE](http://eur-lex.europa.eu/LexUriServ/LexUriServ.do?uri=CELEX:31995L0046:fr:HTML)), donc  de l’arsenal législatif français  avec le respect de la **loi informatique et liberté de 78**,  de la **loi spécifique de 2008**, et des organismes comme celui  de la **CNIL** et de la **DGCCCRF**.  Cependant, les acteurs du secteur (fournisseurs de services, ecommercants) ont pu souffler en ce début d’été un peu car le projet de **loi relatif à la consommation** s’est vu rejeter  2 amendements dont le but visait à renforcer la législation en vigueur vis-à-vis de l’ip tracking.  Au-delà  du territoire Français, il faut faire appel aux législations compétentes des pays où sont collectées les données, normal.

En ce début d’année 2013, la députée européenne **Madame Françoise CASTEX**, a saisi la CNIL pour dénoncer cette pratique de web tracking. Une enquête est donc en cours où la [CNIL et la DGCCRF](http://www.cnil.fr/linstitution/actualite/article/article/ip-tracking-collaboration-en-cours-entre-la-cnil-et-la-dgccrf/) s’unissent pour étudier cette requête.

[![ip-tracking-etat-des-lieux-310x131.jpg](/images/blog/ip-tracking-etat-des-lieux-310x131.jpg) Etat des lieux 2013 sur l'Ip Tracking

Alors attendons voir ce qui devrait sortir en cette rentrée, tant au niveau européen que sur le territoire national. Au-delà de l’ip tracking, l’usage des cookies fait partie des préoccupations des législateurs, l’Europe en 2012  a d’ailleurs demandé à Google d’éclaircir sa  politique de confidentialité sur ces services. Fin 2012, des pas en ce sens ont été accompli de la part du moteur de recherche, et en 2013, il y a quelques semaines, l’affichage de ses Terms of Service (TOS) était mentionné avec un appel à « cliquer » pour acceptation des conditions d’usages des cookies.

## **Techniques de tracking**

Petit rappel sur la façon dont on peut collecter l’adresse IP d’un visiteur sur un site web.

### **Nativement dans une configuration client / Serveur **

Généralement les serveurs web embarquent dans leurs fichiers log les différentes connexions entre le client (via le navigateur) et le serveur. Nativement, la connexion entre 2 machines distantes utilise un protocole de transmission pour pouvoir échanger des données. Le plus communément utilisé par le http://www est TCP/IP inventé en 1983 aux USA qui d'établir une connexion pour toutes machines sur le réseau des réseaux munit d'une adresse IP (Internet Protocol).

[![client-serveur-310x141.jpg](/images/blog/client-serveur-310x141.jpg) Architecture client serveur (Sce

Les couches basses de liaison sont envoyées au serveur dès l’envoi de la requête qui retourne sa réponse aussitôt. Sans l’envoi de ce socket de connexion, point de transmission possible. Ensuite, plus haut dans les couches du  modèle OSI de communication,  les données contenues sur le serveur (pages web) vont pouvoir transiter.

[![TCP-IP-310x145.jpg](/images/blog/TCP-IP-310x145.jpg) Tcp/Ip au service des PCs - Serveurs

L’identification des adresses IP  dans les logs se font ensuite par des routines adaptées qui vont « parsées » ces fichiers textes.

[![log-serveur-310x62.jpg](/images/blog/log-serveur-310x62.jpg) Extrait fichier journal serveur web
### **Tracking via développement de scripts**

Web Beacons or Web bug

Souvent à l’aide de JavaScript, cette méthode permet d’une façon tierce (mais pas forcément), donc non associé au serveur web source, de collecter des informations. Souvent relié aux cookies, ce web beacon permet de relever, via l’insertion d’une image transparente sur la page web demandée, des données qui sont transmises au propriétaire émetteur *(via cet appel de fichier gif)* comme l’adresse IP, notre sujet du moment, mais aussi les urls visitées, le temps passé, une valeur de cookie etc…

Script php/mysql par exemple

Une autre façon  plus rudimentaire,  de collecte  d’information sur l’IP,  peut se faire aussi via différents languages dont le php, par exemple. Ce tracker peut être fait maison, relié à une base MySQL personnalisée avec une connexion sur un service de géolocalisation (via une api).

[![IPTRACKING-310x221.jpg](/images/blog/IPTRACKING-310x221.jpg) Méthodes Ide suivi adresse IP (Sce Abine.com)
## Services d’intelligence IP

### Des données ip enrichies

Les données ne sont jamais nominatives et concernent des données d’enseignes ou raisons sociales, agrégées. Concernant l’anonymat des données personnelles, Google analytics précise qu’il adopte un processus [d’anonymisation de sa collecte](https://support.google.com/analytics/answer/2763052?hl=fr).

[![google-analytics-310x81.jpg](/images/blog/google-analytics-310x81.jpg) Anonymisation de la collecte d'adresses IPs

D’autres sociétés usent de leurs **technologies propriétaires**  basées sur les techniques de scripts déjà évoquées, en se focalisant  sur l’IP  tracking. Leur valeur ajoutée vient  du data mining appliqué sur leur collecte : croisement avec données sociales, démographiques, géolocalisées.

[![service-tracking-310x279.png](/images/blog/service-tracking-310x279.png) Ip Intelligence au service du Web Marketing

Le tracking de l’adresse IP est donc une technologie bien aboutie, reste sa pérennisation dans le temps,  soumise aux évolutions des comportements des internautes  et du corpus législatif  . Cependant, les lobbys à Bruxelles défendent leur bol de soupe donc l’ip tracking n’est pas encore mort !

### Plus d'infos ...

	- La **presse** en parle : [http://www.latribune.fr/technos-medias/internet/20130717trib000776046/marketing-internet-l-ip-tracking-est-il-legal-.html](http://www.latribune.fr/technos-medias/internet/20130717trib000776046/marketing-internet-l-ip-tracking-est-il-legal-.html)

	- **Politique** / Législateur: Site du députée  Mme Castex au parlement Européen : http://www.francoisecastex.org/2013/04/ip-tracking-francoise-castex-saisit-la-cnil.html

	- **Web bug** en savoir plus : http://en.wikipedia.org/wiki/Web_bug

	- **Exemple de script** de collecte : http://ip.codehelper.io/

	- **Alternatives** au tracking via cookies : http://zawadzinski.com/2013/04/26/alternatives-to-cookie-tracking/

	- Les **parades de protection** contre l'ip tracking : [http://www.rue89.com/rue89-eco/2013/05/27/billet-train-coutait-moins-cher-matin-comment-dejouer-lip-tracking-242636](http://www.rue89.com/rue89-eco/2013/05/27/billet-train-coutait-moins-cher-matin-comment-dejouer-lip-tracking-242636)
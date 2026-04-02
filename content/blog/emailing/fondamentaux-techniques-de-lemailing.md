---
title: "Optimiser les campagnes emailing côté serveur"
date: 2016-04-04
author: "admin"
categories: ["Emailing"]
tags: []
slug: "fondamentaux-techniques-de-lemailing"
image: "/images/blog/email-delivrabilite.jpg"
---

Après un bref [historique sur l’emailing](https://www.mauricelargeron.com/les-grandes-dates-de-l-email/), il est temps de passer au plan d’action ! Avant de se lancer tête baissée dans une campagne, observons un des champs de l’**email marketing** *(autrement appelé en français , [Marketing par courriel](https://fr.wikipedia.org/wiki/Marketing_par_courriel))* **la délivrabilité ** avec focus aujourd’hui sur les aspects **techniques**.  Quels sont les atouts à mettre en oeuvre pour assurer une bonne livraison d'un message ?

## **Processus classique d’envoi des messages électroniques**

Petit rappel sur l’**acheminement  des emails**. Les clients locaux existent encore dans les entreprises, mais l’usage de clients cloud (gmail, live) devient la norme surtout en mobilité. Selon une étude récente, ce serait 40% des emails qui s’ouvriraient sur des devices mobiles.

[![Image](/images/blog/processus-achememinement-email-310x221.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2016/03/processus-achememinement-email.jpg) Processus achememinement email

MUA, MTA et MDA sont dans un …Je récupère ici la documentation fournit par la société éditrice de solutions NAS Synology :) .

### ***Mail User Agent (MUA)***

Un mail user agent, ou MUA, est une application dites lourde (per ex., Outlook, Thunderbird) qui est contrôlée par l'utilisateur. Les Mail user agents sont utilisés pour rédiger et envoyer des messages, de même que pour afficher et gérer des messages dans une boîte aux lettres d'utilisateur.

 	- ***Mail Transfer Agent (MTA) : ***Les mail transfer agents, ou MTA, servent à faire transiter les courriers électroniques entre les différents serveurs de messagerie.

 	- ***Mail Delivery Agent (MDA) : ***Les mail délivrent agents, ou MDA, servent à placer un message dans la boîte de réception d'un utilisateur local. Les protocoles Pop (transfert et effacement coté serveur) et IMAP (synchronisation) sont utilisés dans cette phase

 	- ***Simple Mail Transfer Protocol (SMTP) :***Simple Mail Transfer Protocol (SMTP) est un standard Internet utilisé dans la transmission de courriers électroniques via les réseaux Internet Protocol (IP). Alors que les mail transfer agents utilisent le SMTP pour envoyer et recevoir des messages électroniques, les mail user agents n'utilisent le SMTP que pour l'envoi de messages qui sera relayé à un autre serveur de messagerie

## **Quelle Infrastructure matérielle d’envoi  d’emails  choisir ?**

Luttons contre les idées reçues, selon ReturnPath’s 2015 Deliverability Benchmark Report :

 	- 21% des emails qualifiés comme non rebondis (bounced) seraient paisiblement logé dans la boite à spam…

### ***La  réputation commence par la technique***

Le domaine est intrinsèquement véhicule une réputation, accolé à un arobase ne change pas la donne. Il fait partie du signal « émetteur» que le serveur réceptionnaire perçoit lors l’acheminement du message.

De plus, ne nous leurrons pas dans cette histoire, le terme de technique souligne le fait que nous sommes dans un processus de machine to machine où de plus en plus, le machine Learning prends une place prépondérante sur les paramétrages d’infrastructure. La messagerie de Google, Gmail, n’est pas en reste dans ce domaine-là et apprend des **usages de l’utilisateur** (comportement) lors de réception des messages. Mais nous parlerons une autre fois de la mesure de l’engagement des destinataires par les serveurs de messagerie.

[![Image](/images/blog/solutions-emailing-310x207.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2016/03/solutions-emailing.jpg) Solutions d' emailing
### ***Utiliser les Fai du marché***

Avec un Gmail, Hotmail, Outlook, il est possible de lancer une petite campagne qui sera limitée par le serveur de messagerie (200 pour Gmail). C’est une solution souple, sans paramétrage technique mais qui sera néanmoins monitoré par votre fournisseur. Pour du publipostage, il suffira de joindre un fichier de contacts (feuille de calcul de type Google drive dans le cadre de Gmail).

***Choisir un hébergeur et construire une réputation fiable***

Utiliser un serveur web et une ip mutualisée

Tout est affaire de réputation, l’utilisation d’un domaine dont les dns sont liés à une adresse Ip mutualisée comporte un risque de mauvais voisinage.

***Utiliser un serveur mutualisé et une ip dédiée***

Une solution intermédiaire dont  une partie reste dépendante de la machine (hard) et du logiciel de messagerie (soft) mais dont le routage est estampillé par un adressage ip unique qui supporte le domaine.

Un serveur et une ip dédiée : sans doute le must pour de grosse infrastructure mais ou l’administration  la maintenance devront être à la hauteur : implémentation de l’infrastructure de routage (logiciel de messagerie, mta, protocole de routage).

***Opter pour un service spécialisé dans l’emailing***

Formule optimale : il faut rester dans les guidelines de ces fournisseurs dédiés qui font bénéficier à leurs clients des avantages de leur propre **infrastructure de routage emailing**. Citons dolist (le bordelais !),  mailjet (le nantais) la formule en mode saas, mailchimp (l’américain). Des options sont possibles dont le montage de serveurs neufs dédiés dont le rodage sera un préambule.

## **Assurer une délivrabilité par le standards d’authentification   **

Il va de soi que les enregistrements A, Ptr, Mx , accessibles et configurables au chapitre des Dns doivent être correctement déclarés.

Toute utilisation extérieure à sa propre infrastructure va nécessiter l’ajout dans l’idéal de ces 3 enregistrements. Cette procédure doit être faîte lors de l’usage d’une plateforme tierce d’envois d’email comme mailjet par exemple.

[![Image](/images/blog/spf-dkim-dmarc-310x86.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2016/03/spf-dkim-dmarc.jpg) 3 standards dans l'authentification routage

 	- **SPF **: Send policy Framework qui permet, dans le cadre d’externalisation du routage, d’indiquer que tel ou tel autre infrastructure (mailjet par exemple) est autorisée à envoyer pour le compte de…

 	- **Dkim** : Domain Key Identified  mail consiste en une signature qui garantit que le message reçu est identique au message envoyé.  Garanti qu’aucune malveillance entre l’envoi et la réception ne s’est produit.

 	- **Dmarc**   : Domain-based Message Authentication, Reporting & Conformance   encore peu implanté, elle indique au récipiendaire une consigne à adopter en cas d’absence de Spf /Dkim : autoriser, filtrer ou rejeter.

### **Décryptage  d’un code source d’un message**

L’idée ici se résume à ce cas d’envoi simple via un client léger cloud Webmail.

[![Image](/images/blog/envoi-dun-email-via-webmal-310x106.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2016/03/envoi-dun-email-via-webmal.jpg) Exemple : envoi dun email via webmal

Avant d'envoyer son message, on peut utiliser un outil pratique qui vérifie les configurations des standards d'authentification (sfp, dkim)

[![Image](/images/blog/test-mail-tester-256x300.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2016/03/test-mail-tester.jpg) Tester les parametres de configuration authentification

On peut scinder en 2 la façon dont traite un email un serveur de messagerie comme gmail.com

La partie qui concerne l’envoi depuis un ordinateur : comment le Gmail identifie l’envoyeur du message.

[![Image](/images/blog/decryptage-envoi-mail-310x158.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2016/03/decryptage-envoi-mail.jpg) Décryptage envoi mail selon récipiendaire

La partie qui concerne la réception par le serveur, comment Gmail interprète la fiabilité de l’envoyeur.

[![Image](/images/blog/delivrabilite-email-310x149.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2016/03/delivrabilite-email.jpg) Délivrabilite email perçue par recepteur gmail

Voilà pour un rapide tour d’horizon du côté de la machinerie pour assurer une **bonne délivrabilité d’un message email**. Tout reste possible en terme de configuration d’adressage, mais une fois maîtrisé, reste à se concentrer sur le message et l’engagement utilisateur (lors d’un prochain article).
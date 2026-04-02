---
title: "L'Api Adwords pour Marketeur curieux ! (part. 2)"
date: 2015-01-26
author: "admin"
categories: ["Apprendre Google Ads"]
tags: []
slug: "les-bases-du-fonctionnement-de-l-api-adwords"
---

Je continue cette semaine mon exploration newbee de l’api Adwords. Api par ici api par-là, mais comment cela marche ce truc ?

En effet, pour résumer l’étape précédente (partie 1), on se rend compte qu’il en faut des outils pour faire fonctionner une api. Le cas ici pris pour exemple est celui d’un accès et dialogue avec la Sand Box api Adwords sur un script exemple Getkeywords.php  prêt à l’emploi. Les étapes qui ont été déjà franchies :

 	- Du Kfé, et encore un peu plus.. :)

 	- Demande d'une **clé  api** depuis un centre multi compte Adwords (clé temporaire fonctionne avec bac à sable, donc pas besoin d’attendre l’obtention d’une clé finale)

 	- Création d’un compte **Sand Box** (avec compte Google tout neuf)

 	- Importation d’une **campagne** existante ou création fictive (pour avoir de la data à aller interroger)

 	- Choix d’une **plateforme de développement** : ici, basique pour l’exemple, xampp : apache - Php +  éditeur  code (notepad++)

 	- **Installation du serveur** xampp sur disque local c:\ sous windows.

 	- Téléchargement de la **librairie** et des fichiers exemples sur le serveur camp

 	- Et là. Bug ou je beugue..sur un problème d’autorisation …

J’ai demandé du secours à un developpeur  et notamment à Jean Moga  pour arriver au bout de ma démo  que je remercie ici au passage. A plusieurs on pense toujours mieux que tout seul..

## **2 problèmes en 1 pour avoir les droits d’accès à l’api !**

***J’ai tenté de lancer donc la commande depuis Windows cmd.exe sur le fichier Getkeywords.php et là..***
### **First one : Termes et conditions **

 

Apparemment mon compte MCC ne suffisait pas, étant sans doute en mode attente de clé API, il fallait signer les conditions TOS de Google *, . Bon, un peu galère pour trouver ce formulaire…mais ils sont très réactif, quelques après j’avais un document à signer et accepté dans la foulée.

[![Image](https://www.mauricelargeron.com/wp-content/uploads/2015/01/signature-tos-adwords-310x221.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2015/01/signature-tos-adwords.jpg) Signature du contrat TOS api Adwords
### **Second probleme  d'autorisation accès Api**

cela entraine ce genre de message d’erreur : redirec-uri-mismatch

[![Image](https://www.mauricelargeron.com/wp-content/uploads/2015/01/error-oauth-api-adwords-268x300.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2015/01/error-oauth-api-adwords.jpg) Erreur oauth api adwords

Le souci ici est lié au système d’identification renseigné au niveau du **fichier  auth.ini** h où il est demandé d’avoir un clientId plus une clé secrète à renseigner dans ce fichier. Il faut aller la chercher sur la console développeur de Google et surtout, ne pas se tromper dans le choix de l’application, il faut prendre le choix « application installée » et « autre ».

[![Image](https://www.mauricelargeron.com/wp-content/uploads/2015/01/processus-autorisation-adwords-310x272.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2015/01/processus-autorisation-adwords.jpg) Configuration Autorisation Accès Api
## **Récupération des données de la campagne du bac à sable !**

Bon cette fois, je pense que la configuration est bonne. J’appelle donc via le script GetKeywords, les mots clés de mon groupe d’annonces …cela marche !  Ouf !

[![Image](https://www.mauricelargeron.com/wp-content/uploads/2015/01/resulats-comande-adwords-310x43.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2015/01/resulats-comande-adwords.jpg) Resulats commande adwords via script php
## **Présentation sous forme de page Html**

Afin d’avoir une présentation plus agréable,  sous forme de page web, Jean M.  m’a inséré  dans le script,  tout simplement des balises html pour créer une  page html à l'intérieur du fichier GetKeywords.php  . C'est une méthode, mais d'autres existent...

[![Image](https://www.mauricelargeron.com/wp-content/uploads/2015/01/affichage-html-resultat-requete-via-api-310x233.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2015/01/affichage-html-resultat-requete-via-api.jpg) affichage html resultat requete via api

Dans un navigateur, cela donne cela...

[![Image](https://www.mauricelargeron.com/wp-content/uploads/2015/01/affichage-page-web-api-adwords-310x217.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2015/01/affichage-page-web-api-adwords.jpg) Affichage page web commande api adwords
## **Etapes par étapes le processus démarrer avec l'api adwords**

Une illustration vaut mieux que du blabla , donc les 7 étapes capitales du processus dans sa globalité :

[![Image](https://www.mauricelargeron.com/wp-content/uploads/2015/01/api-tutoriel-310x76.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2015/01/api-tutoriel.jpg) Process global

Eh bien "tout çà pour çà" comme dit l’autre…bon, et beh,  je serais développeur dans une autre vie sans doute…après tout, chacun son métier !

Quelques liens :

 	- Faq api adwords : [https://developers.google.com/adwords/api/faq](https://developers.google.com/adwords/api/faq)

 	- Tos Api Adw : disponible ici : [https://services.google.com/fb/forms/apicontact/](https://services.google.com/fb/forms/apicontact/)

 	- Console Developer G. : https://console.developers.google.com/

 	- Forum Api Adwords : https://groups.google.com/forum/#!forum/adwords-api
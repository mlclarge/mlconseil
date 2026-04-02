---
title: "Définition et configurations du fichier htaccess"
date: 2014-03-07
author: "admin"
categories: ["Référencement naturel"]
tags: []
slug: "parametrer-les-acces-a-son-serveur"
---

Qu’est-ce que ce fameux fichier htaccess ? Après avoir vu les aspect du [crawling de site](https://www.mauricelargeron.com/crawler-son-site-pour-son-ref-net/), essayons d’y voir plus clair sur les possibilités de ce  fichier. Je vais tenter d'en définir les contours dans un premier temps, puis ensuite ferai un listing en **5 grandes catégories regroupant 25 fonctions ** de ce couteau suisse. Je me doute bien que pour les initiés rien de neuf, qu’un bref rappel, et  pour ceux moins attachés au code,  des découvertes  sur son potentiel  peuvent se produire, c’est du moins, ce que j’espère faire passer au travers de ces quelques lignes !
## **Qu’est-ce qu’un fichier htaccess ?**

C’est un vieux vétéran du monde du web  qui sert à configurer la plupart des serveurs web de l’internet (65%) , les serveurs apache, dont il contrôle l’accès aux données du site pour faire succinct.
[![Image](https://www.mauricelargeron.com/wp-content/uploads/2014/02/repartition-serveurs-web-310x185.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2014/02/repartition-serveurs-web.jpg) Part de marché des serveurs dans le monde

Matériellement, c’est tout simplement **un fichier ASCII **(American Standard Code For Information Interchange) , soit un fichier texte lisible par un éditeur de texte comme wordpad dans windows et compréhensible par l’œil humain, au détriment d’un fichier binaire qui lui contient des codes binaires destinés aux machines.

Il peut s’exécuter  uniquement dans un environnement serveur Apache, par windows (nt).

Il n’y a pas **qu’un seul fichier htaccess** par site web, mais souvent plusieurs , ils  peuvent  s’exécuter à la racine de chaque dossier selon les directives assignées.
[![Image](https://www.mauricelargeron.com/wp-content/uploads/2014/02/htaccess-hebergement-310x196.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2014/02/htaccess-hebergement.jpg) Fichier htaccess sur hébergeur
## **Quand faut-il l’utiliser ?**

Bien souvent **le mieux c’est de ne pas l’utilise**r ! Bon alors, il ne sert à rien ? Non tout de même pas ! Quand vous avez la main sur les fichiers principaux  de configuration d’un  serveur apache (httpd.conf entre autre) et uniquement dans ce cas-là, rien ne sert à utiliser les vertus du fichier htaccess et autres directives modulaires.

En revanche, pour ceux qui n’ont pas accès via leur hébergement (comme par exemple les formules des serveurs mutualisés, virtuels etc..) , c’est un fichier incontournable ! Bon, ceci dit, pas de panique, les systèmes de CMS aujourd’hui déjà pré-paramètres les directives de leur fichier htaccess .
### Donc, nouvelle question, à quoi cela sert alors ?

Tout simplement, parfois, pour affiner des développements supplémentaires non prévus par certaines plateformes, renforcer certains paramètres de sécurité sur certaines zones de son site, optimiser certains aspects de l’hébergement (organisation personnelle)  ou du site web en lui même.

Et puis, en savoir un petit peu plus, sur comment fonctionne certains éléments, peuvent servir à appréhender des subtilités du net.
### Précision : Htaccess or Robot.txt au fait  ?

Pour clarifier, la première demande faîte au serveur du navigateur, arrive sur le fichier .htaccess , non lisible par un bot ou un navigateur, il pourra permettre ou pas la lecture de fichier ou dossier. Le robot.txt quant à lui, sert d’aiguilleur à destination des crawlers pour l’indexation ou pas d’URLs ou sections du site.
## **Panoplie des pouvoirs de l’htaccess**

Afin d’avoir une vue plus synthétique, j’ai regroupé dans** 5 catégories 25 fonctionnalités le pouvoir de l’htaccess.** Les exemples ont été récupérés de part et d’autre sur le net, ils sont prêt à l’emploi mais restent à personnalisés selon sa configuration.

- Sécurité

- Seo

- Site (performance)

- Serveur

- Expérience Utilisateur (UX)

[![Image](https://www.mauricelargeron.com/wp-content/uploads/2014/02/htaccess-310x296.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2014/02/htaccess.jpg) 5 Domaines pour l'htaccess
### **Sécurité avant tout** !

Protéger  le fichier .htaccess lui même

#htaccess file

order allow,deny
deny from all
 

Protéger  un  fichier en particulier
# protége  monfichier.php

order allow,deny
deny from all

Un fichier protégé par mot de passe

AuthType Basic
AuthName "Prompt"
AuthUserFile /home/path/.htpasswd
Require valid-user

Des fichiers protégés par mot de passe

AuthType basic
AuthName "Development"
AuthUserFile /home/path/.htpasswd
Require valid-user

Parade contre les injections via des scripts malveillants du march
Options +FollowSymLinks
RewriteEngine On
RewriteCond %{QUERY_STRING} (|%3E) 
RewriteCond %{QUERY_STRING} GLOBALS(=|{0,2}) 
RewriteCond %{QUERY_STRING} _REQUEST(=|{0,2})
RewriteRule ^(.*)$ index.php 

Désactiver la signature du serveur
# désactiver signature serveur
ServerSignature Off

Limiter la taille en upload de téléchargement
# limité à  10mb
LimitRequestBody 10240000

Blacklistage par adresse ip
#qui a accès ou pas

order allow,deny
allow from all
deny from 123.456.7xx
deny from 93.121.7xx
deny from 223.956.7xx
deny from 128.456.7xx

#Accepter l’accès à un dossier du serveur pour 1 ip
#Plusieurs adresses IP sont possibles , avec une instruction par ligne.
AuthUserFile /dev/null
AuthGroupFile /dev/null
AuthName "Example Access Control"
AuthType Basic

order deny,allow
deny from all
allow from xx.xx.xx.xx

Empêcher la navigation sur un dossier
# Stopper la navigation
Options All –Indexes

### **Experience Utilisateur**

Rediriger selon les erreurs serveurs sur des pages personnalisées
#custom error docs
ErrorDocument 404 /introuvable.php
ErrorDocument 403 /nonautorise.php
ErrorDocument 500 /erreur.php

Rediriger vers une page de maintenance

Remplacer la page dénommée maintenance.html par la page que sur laquelle vous souhaitez rediriger le visiteur avec l’adresse ip  voulue. Notez la redirection 302 pour éviter l’indexation de cette page temporaire.
RewriteEngine on
RewriteCond %{REQUEST_URI} !/maintenance.html$
RewriteCond %{REMOTE_ADDR} !^123.123.123.123
RewriteRule $ /maintenance.html 

Reécriture Url
Options +FollowSymlinks RewriteEngine on RewriteRule ^page1.html$ page2.html  RewriteRule ^page2.html$ page1.html 

### **Pure Seo**

/

 Bloquer des domaines referents.
RewriteEngine on
RewriteCond %{HTTP_REFERER} oogle.com 
RewriteRule .* – 

# Configuration d’une directive canonique
RewriteEngine On
RewriteCond %{HTTP_HOST} ^yourdomain.com$ 
RewriteRule ^(.*)$ http://www.yourdomain.com/$1 

#Refuser les connexions sans referer / Protection contre les spams de commentaires

#Le code inspecte le référent de la page sur l’accès au fichier de commentaires, si il est dénué de provenance du blog, il ne permet pas le commentaire.
Changer la ligne 4 and et spécifier l’url.
RewriteEngine On
RewriteCond %{REQUEST_METHOD} POST
RewriteCond %{REQUEST_URI} .scriptdecommentaire.php*
RewriteCond %{HTTP_REFERER} !.*votredomaine.com.* 
RewriteCond %{HTTP_USER_AGENT} ^$
RewriteRule (.*) ^http://%{REMOTE_ADDR}/$ 

# forcer la barre oblique “/” (lutter un peu contre le duplicate)

RewriteCond %{REQUEST_URI} /++$
RewriteRule ^(.+)$ %{REQUEST_URI}/ 

#Redirect Www To Non Www Or Vice Versa  (se battre contre la duplication de contenus)
RewriteEngine On
RewriteBase /
RewriteCond %{HTTP_HOST} ^www.yourblogname.com 
RewriteRule ^(.*)$ http://yourblogname.com/$1 
RewriteEngine On
RewriteBase /
RewriteCond %{HTTP_HOST} ^yourblogname.com 
RewriteRule ^(.*)$ http://www.yourblogname.com/$1 

Source: http://www.webanddesigners.com/20-htaccess-hacks-to-prevent-your-wordpress-site-from-hacking/
### **Performance serveur**

#Limiter le nombre de connexions simultanées

MaxClients 

#Configurer la timezone du serveur

SetEnv TZ America/Indianapolis

#Désactiver l’utilisation des images sur son serveur
RewriteEngine On
#Replace ?monsite.com/ avec votre url
RewriteCond %{HTTP_REFERER} !^http://(.+.)?monsite.com/ 
RewriteCond %{HTTP_REFERER} !^$
#Replace /images/pasdimage.jpg avec votre url propre
RewriteRule .*.(jpe?g|gif|bmp|png)$ /images/ pasdimage.jpg 

### **Performance site**

# Désactiver  ETAGS (permet un soulagement du serveur, mais souvent au détriment du navigateur donc à éviter, provoque des ralentissements )

FileETag none

# Permettre la compression

AddOutputFilterByType DEFLATE text/html text/plain text/xml text/css application/x-javascript
BrowserMatch ^Mozilla/4 gzip-only-text/html
BrowserMatch ^Mozilla/4\.0 no-gzip
BrowserMatch \bMSIE !no-gzip !gzip-only-text/html

#Utiliser le cache navigateur pour accélerer le chargement du site

ExpiresActive On
ExpiresByType image/jpg "access 1 year"
ExpiresByType image/jpeg "access 1 year"
ExpiresByType image/gif "access 1 year"
ExpiresByType image/png "access 1 year"
ExpiresByType text/css "access 1 month"
ExpiresByType application/pdf "access 1 month"
ExpiresByType text/x-javascript "access 1 month"
ExpiresByType application/x-shockwave-flash "access 1 month"
ExpiresByType image/x-icon "access 1 year"
ExpiresDefault "access 2 days"

Source: http://www.onextrapixel.com/2011/11/03/unleashing-htaccess-for-wordpress/

#Configurer  un site pour  HTML5 Vidéos (facultatif, si seulement cette préconfig n’existe pas dans le serveur)
RewriteCond %{REQUEST_FILENAME} !-f
RewriteCond %{REQUEST_FILENAME} !-d
RewriteCond %{REQUEST_URI} !=/favicon.ico
AddType text/xml .xml
AddType video/mp4 .mp4 .m4v
AddType video/mpeg .mpeg .mpg
AddType video/quicktime .mov
AddType video/ogg .ogv
AddType video/webm .webm
AddType audio/mp4 .m4a .m4b .m4r
AddType audio/mpeg .mp3
AddType audio/playlist .m3u
AddType audio/x-scpls .pls
AddType audio/ogg .ogg
AddType audio/wav .wav
AddType application/x-shockwave-flash swf

Source: http://snipplr.com/view.php?codeview&id=53437

http://ottopress.com/2011/howto-html5-video-that-works-almost-everywhere/
## **Webographie **

- [Bloquer certains bot par htaccess](http://www.vala-bleu.com/aide/Securite/bloquer-les-spam-bots-et-aspirateurs-de-site-web-avec-.htaccess.html)
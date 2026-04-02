---
title: " Rich Snippets seo et médias sociaux"
date: 2012-09-26
author: "admin"
categories: ["Référencement naturel"]
tags: []
slug: "maitriser-les-microdonnees-pour-son-referencement"
---

Comment améliorer le **référencement**, la visibilité d’un contenu à l’aide de **rich snippets** ? Dans cet article, je rappellerai  ce que sont les rich snippets et comment  améliorer leurs contenus.  Le grand Google y attache de l’importance puisqu’il vient de refondre son  interface pour les rich snippets. Cet  outil permet de scanner une page web afin d’en extraire le balisage provenant de ces micro-formatage. En fait, il s’agit d’une refonte de l’ancien outil avec des fonctionnalités supplémentaires quant à l’identification de chaque balise trouvé sur la page. Vous pouvez également vous servir de **Google webmaster tool ** qui lui agrège sur l’ensemble du site, toutes les pages avec des données structurées puis vous renvoie  ensuite pour identification sur le premier outil. J'avais déjà abordé brièvement le thème des rich snippets lors de l' évoquation de la [sémantique](https://www.mauricelargeron.com/la-semantique-dans-les-moteurs-de-recherche/) dans les moteurs de recherche.

Selon Paul Bruemmer (article sur Search Engine Land) ces Rich Snippets peuvent améliorer jusqu’à **30 % le trafic du référencement naturel** et normalement donc, le positionnement du contenu qui va avec ;) . Eddie JL Emmanuel, directeur de recherche chez catalyst Online, démontre aussi que sur un même contenu *(ici une recette de cuisine)* les impressions, les pages vues s’accroissent dès qu’un [balisage micro-données](http://www.catalystsearchmarketing.com/2012/01/how-rich-snippets-can-improve-your-ctr/) est utilisé (fig.1).

[![richsnippetSeo-310x204.png](/images/blog/richsnippetSeo-310x204.png) Fig.1 Rich snippets et trafic internet
## **Les Rich Snippets, quésaquo ?**

Les rich Snippets permettent d’exposer un contenu pour les moteurs de recherche et les plateformes sociales *(G+, FBook)*  d’une manière :

	- Riche

	- Ordonnée

	- Incitative et notamment dans la recherche locale

	- Renseignée  (fig.2)

[![fig.3-reultats-locaux.png](/images/blog/fig.3-reultats-locaux.png) Fig.2 Utilité des Rich Snippets

**7 types de contenus** répertoriés à ce jour

	- Avis

	- Personnes

	- Produits

	- Entreprises et organisations

	- Recettes

	- Événements

	- Musique

**3 formats** existent pour coder ce style d’information, **microdonnées**, **microformats** et **RDFa**. Le standard édicté par** Schema.org** *(Google, Yahoo, Bing)* recommande l’usage des microdonnées. Mais il est possible aussi de formater ce genre de contenu à l’aide de l’Open Graph de facebook, balisage commun  avec Google plus lors de partage sur ces réseaux sociaux. (fig. 3)

[![fig.2facebookShare-310x129.png](/images/blog/fig.2facebookShare-310x129.png) Fig. 3 Snippet Facebook

Pour mieux comprendre l’impact des RSnippets, voici un exemple (fig.4) dans lequel sur la recherche, « hotel marmiton », apparait une rich snippet que j’analyse ensuite avec l’[outil Google](http://www.google.com/webmasters/tools/richsnippets) afin d’en déduire une interprétation.

[![fig.4-Rich-snippets-decryptage-310x150.png](/images/blog/fig.4-Rich-snippets-decryptage-310x150.png) Fig. 4 Rich Snippets Décryptage
## **Les Microdonnées pour le moteur de recherche Google **

Vu la prédominance de ce moteur en France, pour les producteurs de contenus, il devient une nécessité de prouver qui est à l’**origine d’une publication**. Il n’y a pas 36 solutions, sinon deux pour google, expliquées [ici](http://support.google.com/webmasters/bin/answer.py?hl=fr&answer=1408986), faciles à mettre en œuvre avec une obligation commune : avoir un **profil Google plus**. Donc pour la première solution, c’est la** liaison d’une adresse email avec un domaine personnalisé** et  d'un profil G+, la deuxième *(que j’ai utilisé)*, c’est la **création d’un lien bilatéral entre le profil G+ et le site** ou autre blog (fig.5). Je n’ai pas eu de résultat en passant par le micro- formatage  de personne (microdonnées schema.org).

[![fig.5-auteur-google-310x205.png](/images/blog/fig.5-auteur-google-310x205.png) Fig.5 Balise "Auteur" pour Serp Google
## **Optimiser les rich snippet pour les réseaux sociaux**

### **Facebook **

Il arrive souvent lors d’une diffusion de son contenu sur facebook de n’avoir pas le rendu souhaité, il convient donc de formater la source avec l’[open graph de FB](http://davidwalsh.name/facebook-meta-tags) pour arriver à ses fins. Pour illustrer le propos, ici une page de démo. sur Fb formatée pour l’ajout sur sa plateforme  (fig.5)

[![facebook-snippets.-310x274.png](/images/blog/facebook-snippets.-310x274.png) Fig. 6 Balisage Open Graph Facebook
### **Google + **

Un petit [outil google](http://www.google.com/webmasters/tools/richsnippets) bien pratique, si on n’est pas satisfait du rendu sur la plateforme sociale de Google, elle permet de personnaliser les éléments inclus dans le post. Pour démonstration (en 1) il suffit de remplir le petit formulaire,  puis le code est génèré automatiquement (2),  ensuite le descriptif du snippet  lors du partage par l'internaute  (3), puis son rendu dans un moteur de recherche (4) . J' ai utilisé ici les images modifiées pour ce post de l’excellent article donné par Dana  Lockadoo de  YoyoSeo que je citerai plus loin dans l’article au sujet de sa **méthode SSSF***. *A retenir ici, est le fait que le descriptif dans Google plus  fait par le visiteur *(lettre A)* sert de **lien url dans les Serp de Google,** donc, à méditer pour le paramétrage des mots clés.

[![fig.6.1rendu-google-plus-310x215.png](/images/blog/fig.6.1rendu-google-plus-310x215.png) Fig. 7 Configuration snippet G+
### **Pour Facebook et Google+**

Le méthode évoquée sur le site Seomoz ici par [Dana Lockadoo de Yo ! Yo !  Seo](http://www.seomoz.org/blog/rock-your-seo-with-structured-social-sharing-mozcon-presentation) part du même principe de départ, à savoir, les snippets de partage ne reflètent pas le réel contenu du site, donc il faut retaguer le code source selon l’**OpenGraph de FB**. Elle rajoute ici les idées  d’y adjoindre les **variables utm** afin d’avoir un suivi dans Google analytics, un Hashtag précis, et  un formatage adapté pour la plateforme twitter , le tout regroupé sur un tableur excel (fig. 7).

[![fig.7-sssf-methode-310x157.png](/images/blog/fig.7-sssf-methode-310x157.png) Fig.7 Méthode SSSF de YoYOSeo
### **Pour Twitter**

Depuis le mois de juin dernier, Twitter propose une façon de rendre le contenu partagé sur sa plateforme plus attractif. Le principe est le même que celui évoqué précédemment, à savoir, utilisé les balises natives de la plateforme de micro-blogging (fig.8)

[![twitterRS-310x129.png](/images/blog/twitterRS-310x129.png) Fig.8 Twitter Cards = R. Snippets

Toute la [procédure](https://dev.twitter.com/docs/cards) des **Twittercards** est disponible ici.

### **Pour Youtube**

Ici je rapporte un [article](http://www.swellpath.com/2012/09/author-rich-snippets-for-youtube-video-content/) sur le sujet mais je ne l’ai pas encore testé. Néanmoins, Google automatiquement fait le lien entre votre profil et une éventuelle chaîne YT. (fig.9) si vos comptes sont les mêmes ou liés par quelques autres données.

[![fig.9-Youtueb-snippets-310x166.png](/images/blog/fig.9-Youtueb-snippets-310x166.png) Fig. 9 Youtube R.S.
### **Modifier le contenu source sur WordPress et autres CMS**

Il conviendra de fonctionner au cas par cas pour les plateformes CMS. Certains templates déjà intègrent nativement du balisage de snippets (Og) . Pour ceux qui se sentent capable de modifier le code* (attention lors de mises à jour !)* il sera possible d’intervenir au niveau du **Header**  . Sinon le plus simple, est de recourir à des **plugins** dédiés à cela. Je citerai par exemple pour faire apparaître des votes sur un site joomla «** Rich Snippets Vote **»(fig.10).

[![fig.10-joomla-plugin-rich-snippets-310x69.png](/images/blog/fig.10-joomla-plugin-rich-snippets-310x69.png) Fig. 10 Plugin Pour Joomla
**Liens utiles :**
[http://support.google.com/webmasters/bin/answer.py?hl=fr&answer=146645](http://support.google.com/webmasters/bin/answer.py?hl=fr&answer=146645)
---
title: "Initiation Expressions régulières pour google analytics"
date: 2012-09-12
author: "admin"
categories: ["Google Analytics"]
tags: []
slug: "regex-pour-analyser-son-audience"
---

Abordons avec entrain le sujet des expressions régulières pour l’application Google analytics. Pour les développeurs, les RegEx comme on les appelle, font partie de leur pratique quotidienne. Pour les non développeur, disons, pour les webmarketeurs, dont je fais partie,  le mandarin à côté des regEx,  c’est pichnette ! Donc une petite initiation ne fera pas de mal, car, sans pratique régulière J , il sera difficile de les maitriser. J’expliquerai dans un premier temps leur utilité, puis l’alphabet qui les compose, et enfin donnerai quelques exemples pratiques.

## Les ReGeX à quoi cela sert ?

## **Origine des données **

Elles servent à faire correspondre des chaines de texte donc des caractères, des mots, ou des modèles de caractères (un ensemble) sur un flux de données (audience, publicité, sources de trafic, contenus, conversions).  Elles peuvent servir à filtrer, à créer des objectifs, à segmenter, à relooker un flot de clics. Ces données proviennent du code de tracking de GA installé sur les pages d’un site, qui pose des cookies sur le navigateur de l’internaute, mais aussi par les informations indiquées lors de la configuration du compte GA.  Le moteur Rège de Google analytics repose sur une implémentation partielle de PCRE (perl compatible regular expression).  Ces expressions sont donc composées de caractères littéraux (lettres de l’alphabet) mais aussi de méta caractères au nombre de 11 divisés en 4 catégories : Génériques, points d’ancrage, groupes et autre.

## **Syntaxe *(source Google annotée d’éléments supplémentaires)***

**Caractères littéraux**

Ex : « Google »  dans un champ dédié au RegEx dans GA, est une RegEx !

**Méta-caractères divisé en 4 catégories (source Google) **

**Génériques**
1)    **  .  **  Fait correspondre un seul caractère, quel qu'il soit (lettre, chiffre ou symbole)   goo.gle correspond à gooogle, goodgle ou goo8gle

2)    **  ***   Fait correspondre à zéro ou à plusieurs éléments précédents  L'élément précédent par défaut est le caractère précédent. goo*gle correspond à gooogle ou goooogle, couplé avec un « .* »  indique de prendre tout ce qui précède.

3) **    +**   De même que pour l'étoile, sauf que le signe "plus" doit correspondre au moins au dernier élément               goo+gle correspond à goooogle, mais pas à Google.

4)    **  ?  ** Fait correspondre à zéro ou à un élément précédent    oran?ge correspond à la fois à orage et à orange

5) **     |**   Correspond avec l'expression logique "ou" a|b correspond à a ou b

**Points d’ancrage**
6)  **    ^**   Réclame que vos données soient placées au début de son champ  ^site correspond à site, mais pas à monsite

7) **     $**   Réclame que vos données soient placées à la fin de son champ  site$ correspond à site, mais pas à siteweb

**Groupes**
8)    **  ()  ** Parenthèses pour créer un élément, au lieu d'accepter les valeurs par défaut Merci (bien|encore) va correspondre à la fois à Mercibien et à Merciencore

9)  **    **    Crochets afin de créer une liste d'éléments de correspondance    crée une liste comportant a, b et c

10)   **-**       Tirets avec des crochets afin d'élargir votre liste    crée une liste pour l'alphabet en majuscule

**Autre**
**\  **       Transforme un caractère d'expression régulière en caractère standard  monsite\.fr permet d'éviter que le point soit un caractère générique

**{m,n} **quantificateur borné pour au moins m et au plus n occurrences de ce qui précède (pas documenté dans ga mais fonctionne).
## Pratique des expressions régulières dans Google analytics

### **Cas 1 : Tri simple**** à partir du rapport contenu > Toutes les pages**

**U****tilisation littérale **pour aller chercher **un terme parmi une liste d’urls** consultées (fig.1)

**Seo**

[![Image](https://www.mauricelargeron.com/wp-content/uploads/2012/09/Fig.-1-filtreliteral1.png)](https://www.mauricelargeron.com/wp-content/uploads/2012/09/Fig.-1-filtreliteral1.png) Fig. 1 filtreliteral
### **Filtre**

**Cas 2 : **Filtre et exclusion de cette adresse ip afin de ne pas mesurer l’audience qui provient de cette machine (fig.2)

**Méta utilisée : \ et ***

**192\.168\.0.***

[![Image](https://www.mauricelargeron.com/wp-content/uploads/2012/09/fig.2-filtreIp.png)](https://www.mauricelargeron.com/wp-content/uploads/2012/09/fig.2-filtreIp.png) Fig.2 Filtrage adresse Ip
### **Analyse ****mots clés******

**Cas 3 : **Allons un petit peu plus loin et essayons parmi une liste de mots clés , de trouver ceux qui font référence au terme « *référencement » *avec ou sans accent sur le « e »  afin d’avoir un résultat agrégé (fig.3)

**Méta utilisée : ******

**rfrencement**

[![Image](https://www.mauricelargeron.com/wp-content/uploads/2012/09/fig.3-filtre-mots-cles1.png)](https://www.mauricelargeron.com/wp-content/uploads/2012/09/fig.3-filtre-mots-cles1.png) Fig.3 filtre-mots-cles

**Cas 4 :** Enfin, je souhaite avoir les mots clés faisant référence au terme (référencement **ou **seo)

**Méta utilisée : |**

**rfrencement|seo**

### **Objectif dans GA**

Poussons plus loin notre analyse admettons avoir une liste d’urls qui correspondent à une liste de produit d’une même catégorie et en faire un objectif unique **Fig.4**.

**Méta utilisée : \ , **,**{}******

	- www.domaine.com/categorie1/produit?id=235

	- www.domaine.com/categorie1/produit?id=456

	- www.domaine.com/categorie1/produit?id=154

**\/categorie1\/produit\?id={1,}**

[![Image](https://www.mauricelargeron.com/wp-content/uploads/2012/09/fig.4-Filtre-Objectif-Ga.png)](https://www.mauricelargeron.com/wp-content/uploads/2012/09/fig.4-Filtre-Objectif-Ga.png) fig.4 Filtre-Objectif-Ga
### **Segment personnalisé**

**Cas 5 :** Suivre le trafic de Google image

Cette fois-ci je souhaite retenir le traffic amené par Google image par exemple. Je vais identifier le paramètre  utilisé par Google dans le moteur image lorsque je clique sur l’une d’entre elles et ensuite je l’applique en expression régulière dans GA (Fig.5). C'est la seule difficulté, car pas de méta caractères sont utilisés, uniquement le littéral du paramètres Google.

**/imgres**

[![Image](https://www.mauricelargeron.com/wp-content/uploads/2012/09/fig.5-segments-images.png)](https://www.mauricelargeron.com/wp-content/uploads/2012/09/fig.5-segments-images.png) Fig.5 segments-images

**Cas 6 :** Suivre le trafic des mots clés à rallonge, la long TAIL ou longue traîne (fig.6)

Ici, pas d'expression littérale, car on ne connait pas la donnée source, vu que c'est celle que l'on cherche ! Donc la syntaxe se base sur de l'extraction de caractères avec un arbitrage  sur les espaces situés avant ou après chaque chaîne de caractères.

**^\s*+\s*$ - 1 mot clé **
** ^\s*+(\s++){1}\s*$ - 2 mots clés**
** ^\s*+(\s++){2}\s*$ - 3 mots clés**
** ^\s*+(\s++){3}\s*$ - 4 mots clés**

[![Image](https://www.mauricelargeron.com/wp-content/uploads/2012/09/fig.61-Reg-ex-Mots-cles-3-mots.png)](https://www.mauricelargeron.com/wp-content/uploads/2012/09/fig.61-Reg-ex-Mots-cles-3-mots.png) fig.61 Décryptage RegEx longue traîne

Dans google anlytics cela donne..(fig. 7)

[![Image](https://www.mauricelargeron.com/wp-content/uploads/2012/09/fig.6-Reg-ex-Mots-cles-3-mots1-496x300.png)](https://www.mauricelargeron.com/wp-content/uploads/2012/09/fig.6-Reg-ex-Mots-cles-3-mots1.png) Fig. 7 Reg-ex-Mots-cles-3-mots
### **Construire un tunnel de conversion **(fig.8)

Répérer ses pages ou urls qui marquent votre panier, voici le principe (adapter la syntaxe au chemin de l’url)

1.     /panier/numérodecommande/
2.     /panier/numérodecommande/vosinformations
3.     /panier/numérodecommande /recap
4.     /panier/numérodecommande/paiement
5.     /panier/numérodecommande/remerciement

**RegEx**

**^/panier/\d+/**
** ^/panier/\d+/vosinformations**
** ^/panier/\d+/recap**
** ^/panier/\d+/paiement**
** ^/panier/\d+/remerciement**

[![Image](https://www.mauricelargeron.com/wp-content/uploads/2012/09/fig.7-Panier-ga.png)](https://www.mauricelargeron.com/wp-content/uploads/2012/09/fig.7-Panier-ga.png) fig.8 Tunnel de conversion ga
### **Analyse sous domaine (filtre avancé)**

Analyse sous domaine (si l’on possède  des sous domaines, forum, blog, support) et que l’on souhaite suivre ces sous domaines , il convient de faire un filtre personnalisé. Attention, on veillera à créer un profil dédié sur lequel s’appliquera ce filtre. 2 variables :  Le nom d’hôte « forum » et l’URI  « rubriqueduforum ». Exemple d’url à filtrer : http://forums.mondomaine.fr/forum/rubriqueduforum/ (fig.8)

RegEx : (.*) avec un constructeur (pour associer les 2 champs)

 

[![Image](https://www.mauricelargeron.com/wp-content/uploads/2012/09/fig.8-Analyse-sous-domaine1.png)](https://www.mauricelargeron.com/wp-content/uploads/2012/09/fig.8-Analyse-sous-domaine1.png) Fig.9 Analyse sous domaine
## **Liens utiles pour les expressions régulières**

Articles et documentation :

[http://www.seotakeaways.com/regular-expression-guide-for-seos/](http://www.seotakeaways.com/regular-expression-guide-for-seos/)****

[http://support.google.com/analytics/bin/answer.py?hl=fr&answer=1034324&rd=1](http://support.google.com/analytics/bin/answer.py?hl=fr&answer=1034324&rd=1)

[http://www.lunametrics.com/regex-book/Regular-Expressions-Google-Analytics.pdf](http://www.lunametrics.com/regex-book/Regular-Expressions-Google-Analytics.pdf) (Pratique !)

[http://www.regular-expressions.info/](http://www.regular-expressions.info/) (une bible)

Outils

[http://www.zytrax.com/tech/web/regex.htm#experiment](http://www.zytrax.com/tech/web/regex.htm#experiment)

[http://gskinner.com/RegExr/](http://gskinner.com/RegExr/)** **

Donc , pour résumer, les expresssions régulières , servent à **trier, segmenter,** et** personnaliser** les données issues en amont (sur les serveurs comme celui des moteurs de recherche ) et en aval, celles qui proviennent de l'audience de votre propre serveur web. A la semaine prochaine !
---
title: "8 expressions régulières pour Google Analytics"
date: 2017-03-27
author: "admin"
categories: ["Google Analytics"]
tags: []
slug: "tri-avec-regex-sur-urls"
image: "/images/blog/expression-regul.jpg"
---

Ce n’est pas le sujet dont les marketeurs raffolent, mais pourtant, parfois il faut s’y coller !  Savoir démêler certains rapports  d’audience  dont les urls générées par le site web ne sont pas super propres peut être utiles. Alors voici quelques expressions régulières  (appelées aussi [expressions rationnelles](https://fr.wikipedia.org/wiki/Expression_rationnelle)) testées sur  Google analytics. Je rappelle que les **expressions régulières** servent à faire des tris aussi bien en amont pour les vues analytics, qu’en aval  dans les tableaux et rapports standards ou lors de la création de reporting personnalisés.

**Petit schéma pour rappeler le principe de la syntaxe**

[![fig.61-Reg-ex-Mots-cles-3-mots-310x146.png](/images/blog/fig.61-Reg-ex-Mots-cles-3-mots-310x146.png) Schéma de principe : significations des RegEx

Pour les débutants, pour **débuter avec à les expressions régulières** , allez  [ ici ](https://www.mauricelargeron.com/regex-pour-analyser-son-audience/)
## **Outil  pour tester les regex et Google analytics**

Les expressions régulières sont présentes dans tous les langages de programmation : perl, JavaScript, java, c » , python, c++ , Emacs, C/Posix , grep et sed…

Ils existent bon nombre d’outils en ligne pour tester les regex, j’en citerai 1: http://regexr.com/  il est vraiment pratique, anglophone, mais bien fait. Sur une interface en 3 parties dont : le filtre regex, les correspondances par rapport aux chaines de caractères et ensuite les explications en dernière partie de tableau. Par simple « roll over » il est possible de comprendre l’utilité de chacun des signes d’une expression, son étendue.

[![regexr.com_-480x300.jpg](/images/blog/regexr.com_-480x300.jpg) Outil **regexp**

Alors une petite réserve, les outils en ligne sont bien pour apprendre à faire la syntaxe, mais ensuite il faut tester dans Google analytics directement, au niveau des filtres de tables qui donnent directement le résultat du tri. Le moteur de regex de GA est spécifique à GA et il peut y avoir des décalages de résultats.

[![GOOGLE-ANALYTICS-EXPRESSIONS-REGULIERES-310x135.jpg](/images/blog/GOOGLE-ANALYTICS-EXPRESSIONS-REGULIERES-310x135.jpg) Tester dans GA
## **8 expressions pour y voir plus clair dans ses urls**

 	- 
### **Objectif : Url qui comporte le nom "page" dans son pattern**

 	- Ici avec :  \/page\/?(?:+\/?)*$

 	- Résultats : que les urls dont l’uri contient « page » à l’intérieur du chemin

 	- 
### **Objectif : Urls qui démarrent par le terme « page » ou « référencement »**

 	- Syntaxe : ^(\/page\/)|(\/référencement\/)

 	- Résultat du tri : /page/5/ OU /référencement/

 	- 
### ***Objectif : Url  uniquement avec des paramètres repéré par un « ? »***

 	- Syntaxe : \/?=  ou plus compliqué => (\w+)=(\w+)

 	- Résultat du tri : /google-adwords-2016/?userid=0 OU /html5-est-il-utile-au-referencement/?replytocom=41

 	- 
### ***Objectif :  urls avec 3 caractères dans le dernier répertoire, exemple du coup avec les pages "amp" (3 caractères)***

 	- Syntaxe : /{3}.$

 	- Résultat du tri : /evolution-du-marketing/amp/

[![amp-filtre-310x212.jpg](/images/blog/amp-filtre-310x212.jpg) Champ dont le dernier chemin est constitué par 3 caracteres

 	- 
### ***Objectif :  urls avec des pages profondes***

 	- Syntaxe : /.$

 	- Resultat du tri : /page/5/ ou /referencement/page/2/

 	- 
### ***Objectif : seulement les urls qui se terminent par un "3"***

 	- Syntaxe : \/3.$

 	- Résultat du tri /page/3/   ou  /referencement/page/3/

 	- 
### *Objectif : seulement les urls avec pages profondes (paginées par exemple)*

 	- Syntaxe : /.$

 	- Resultat du tri /page/5/  ou  /referencement/page/2/

 	- 
### ***Objectif : les urls avec 2 chemins dans l’Uri  mais sans tri sur la fin des urls où certains paramètres sont pris en compte comme : ?userid***

 	- Syntaxe : ^(/+){2}.$

 	- Résultat du tri /google-adwords-2016/?userid=0 ou /page/4/

 	- 
### ***Objectif : les urls avec 2 chemins dans l’Uri  mais sans les urls à paramètres, uniquement les urls propres***

 	- Syntaxe : ^(/+){2}.$

 	- Résultat du tri /page/4/ ou /faire-sa-publicite-avec-le-bon-coin/amp/

Il n’y a pas d’expression idéales, certaines sont passe partout comme celles évoquées ici, mais d’autres nécessiteront plus de travail de réflexion !
## **Documentation expression régulières **

 	- https://support.google.com/analytics/answer/1034324?hl=fr

 	- Pense bête Pdf  pour retenir l'essentiel de [David Child](https://www.mauricelargeron.com/wp-content/uploads/2017/03/davechild_regular-expressions.pdf)

 	- Outil externe pour tester les filtres : http://www.analyticsmarket.com/freetools/regex-tester
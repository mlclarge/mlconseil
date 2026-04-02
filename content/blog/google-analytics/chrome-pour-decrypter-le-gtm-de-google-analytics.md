---
title: "Debogage du gestionnaire de balises Google"
date: 2013-12-11
author: "admin"
categories: ["Google Analytics"]
tags: []
slug: "chrome-pour-decrypter-le-gtm-de-google-analytics"
---

La semaine dernière, j’abordais l’intégration d’un suivi de clics via le gestionnaire de balises Google. Après la rédaction de cette article,  je me suis posé la question suivante , existentielle :) : Est-ce que cette manière de taguer son site à distance, nous éloigne t-elle pas un peu de ce qui se passe réellement sur la page ?  Comme je ne dois pas être le seul à avoir cette interrogation , j’ai décidé d’aller plus loin et de partir à la rencontre de l’exécution du code du **tag manager** (autrement dénommé) dans **le navigateur du visiteur**, lors de l’exécution de ces **écouteurs d’évènements** placés sur les liens du site *(voir cas de l'article précédent)* . Dans un premier temps je recadrerai l’environnement de l’expérience, puis décrypterai, sans rentrer dans le code (dev.), la façon dont retrouver ce ‘container à scripts’, qui va devenir sous peu, "un incontournable" dans l’écosystème ‘Googlelien’ de l’analyse d’audience.

## Le contexte du gestionnaire de balises

Je rappelle les 4 opérations, dans l’ordre il faut, pour réaliser un suivi via GTM, avoir un compte Google avec lequel on accèdera à son compte :

	- **Google analytics**  pour traquer son site (UA-XXXXXXXX)

	- Tag manager pour créer son container (GTM-XXXX)

	- Puis ensuite il faut insérer ce «bout de code » juste après l’ouverture de la balise  du template du site.

	- Enfin, vérifier dans le navigateur sa présence, on peut utiliser un plugin dédié «le  Tag assistant » . Ce dernier ne vous montrera  pas les rouages de son exécution, pour cela il faut utiliser des outils dit de "débogage"  nativement embarqués dans un navigateur .

[![Image](https://www.mauricelargeron.com/wp-content/uploads/2013/12/tag-assitant-310x273.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2013/12/tag-assitant.jpg) Tag assistant = Vérif. basique mais pratique !
## Chrome comme outil de vérification de son tracking

### Lancement de la console et première remontée d’erreur

J’ai utilisé  **Chrome** comme browser, avec ses outils de debugage natifs, sans aucun module externe à rajouter, cela simplifie les choses.  Une fois lancé (voir ci dessous) , depuis la deuxième partie de la page, sous l’affichage du site, 8 onglets sont là pour décrypter ce qui se passe sur la page : Elements, Network, sources, timeline, profiles Ressources, Audit et **Console. Cette dernière** justement s’ouvre en premier lors du lancement de l’extension.

Dans un premier temps, la seule chose à faire pour vérifier s’il n’y a pas d’erreur suite à l’insertion dans le code source de la page du container, c’est d’**activer la console JavaScript** et observer ce qui s’y passe, ce qu’elle vous raconte en quelque sorte. Ici, à priori, un seul avertissement, sans grande importance, et pas de signe de Google tag manager, donc cela se présente bien (sous entendu pas d'erreur dans l'intégration)  !

[![Image](https://www.mauricelargeron.com/wp-content/uploads/2013/12/console-javascipt-310x248.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2013/12/console-javascipt.jpg) Test dans Console native Js de Chrome
### La localisation sur la page et les balises assignées

Revenons à l’onglet « Eléments » qui affiche, sur la partie gauche, le code html de la page. Bingo ! **Le Google tag manager **est bien là ! Ouf ! Sur la droite, différents sous onglets décrivent les différents attributs de cette page. Je m’arrête sur « event listeners » . A 2 endroits dans le script GTM je retrouve bien mes écouteurs de clics.

[![Image](https://www.mauricelargeron.com/wp-content/uploads/2013/12/elements1-310x228.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2013/12/elements1.jpg) Localisation du script dans la page
### L’importance de l’appel du container sur le réseau

Cet onglet « **Network **» m’indique que l’objet gtm communique bien avec le serveur lors de l’appel par le navigateur (200 OK) , le poids total est de 24,2 KB  dont 9.7 KB a été appelé et son temps de latence 82 ms.  Bien, pas bien ? Je dirais que c’est le plus important des appels (kbs)  mais situé dans la moyenne en temps de latence par rapport à l’environnement total de la page.

[![Image](https://www.mauricelargeron.com/wp-content/uploads/2013/12/network2-310x154.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2013/12/network2.jpg) Le Réseau = Appel serveur du GTM
### Le code source du container

Sur le « tab : Sources » on retrouve, sous forme d’arborescence, les éléments que peut interpréter le  navigateur, à savoir le **code css, javascript, html** . Donc bien sûr, nous retrouvons dans son ensemble, le code du GTM.

[![Image](https://www.mauricelargeron.com/wp-content/uploads/2013/12/sourceCodePage-310x217.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2013/12/sourceCodePage.jpg) Code source complet du Container

Si je souhaite aller plus loin, dans la lecture de ce code, je peux au travers du moteur de recherche inclus  dans l’outil de débogage, rechercher des éléments qui me parlent comme ceux que j’ai définis lors de la configuration dans les évènements pour mes écouteurs de clics. Je peux ainsi faire **un rapprochement concret entre la plateforme tag manager et ce qui se passe réellement dans ma page**.

[![Image](https://www.mauricelargeron.com/wp-content/uploads/2013/12/tag-manager-et-chrome-debuger-310x170.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2013/12/tag-manager-et-chrome-debuger.jpg) Quand Tag Manager et Navigateur se rejoignent
### La « timeline » déroulement du scénario

L’onglet « ligne de temps » (restons Frenchis !),  et le sous chapitre « **events **»  reste la fonctionnalité la  plus parlante. J’ai en temps réel ce qui se passe, les appels de fonctions, le temps qui passe,  avec un code couleur selon qu’il s’agisse d’un chargement, d’une exécution, d’un rendu ou d’un affichage. Sur l’illustration ici, uniquement sont enregistrés les paramètres qui affectent 2 clics sur liens.

[![Image](https://www.mauricelargeron.com/wp-content/uploads/2013/12/timeline4-2-clics-liens-referencement-evenement-produit-310x202.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2013/12/timeline4-2-clics-liens-referencement-evenement-produit.jpg) La Timeline souligne les clics en temps réel
### Profiles, Resources, Audit…

Je passe sur ces fonctionnalités, elles n’apportent rien à l’objet GTM qui est analysé aujourd’hui.

### La « Console » me console pas !

Pour finir, la « console » permet à tout bon développeur, que je ne suis pas, aïe cela fait mal !, de retrouver ces petits en les appelant par leur nom. Donc je tape «** dataLayer** » , qui est la couche native de données  du gestionnaire de balises , et qui englobe tous les objets (évènements par exemple). Sur l’image, 3 objets sont bien chargés : gtm.js/gtm.dom/gtm.load en revanche, je désespère de faire apparaître les gtm.click et gtm.linkClick que j’ai installé pour configurer mon suivi de clics.  Ils sont bien là vu qu’ils enregistrent bien les évènements dans analytics ! Donc, si vous avez un tuyau, je suis preneur.

[![Image](https://www.mauricelargeron.com/wp-content/uploads/2013/12/console-javascipt-chrome-310x232.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2013/12/console-javascipt-chrome.jpg) Usage de la console avec focus sur DataLayer

Au final, ces observations via le browser permettent sans moyen particulier, d'avoir un oeil sur ce qui se passe, et parfois, de découvrir par hasard, d'autres problèmes (ralentissements, bugs) insoupçonnés.
## Petites ressources sur le web

	- Datalayer disséqué : [http://www.swellpath.com/2013/10/google-tag-manager-inspecting-andconfiguring-auto-event-tracking/](http://www.swellpath.com/2013/10/google-tag-manager-inspecting-andconfiguring-auto-event-tracking/)

	- Devtools : [https://developers.google.com/chrome-developer-tools/?hl=en](https://developers.google.com/chrome-developer-tools/?hl=en)

	- plugin google : [tag assistant](https://chrome.google.com/webstore/detail/tag-assistant-by-google/kejbdjndbnbjgmefkgdddjlbokphdefk)
---
title: "Questions fréquentes sur google analytics (part 1)"
date: 2015-09-28
author: "admin"
categories: ["Google Analytics"]
tags: []
slug: "questions-frequentes-google-analytics"
---

L’idée ici est de reporter les **questions fréquentes de [google analytics ](http://www.google.com/intl/fr_fr/analytics/)**et d'ébaucher les principales solutions avec des liens ressources. J’ai retenu 5 thèmes pour démarrer cette série, qui je pense, se verra agrémentée  au fur et à mesure par d'autres thématiques,  le sujet est vaste ! Au menu cette semaine : luttre contre le spam de référents, configuration de compte, sources de trafic , techniques de tracking , taux de rebond et conversion.

## **Comment lutter contre le faux trafic dans google analytics ?**

Pas de solution miracle vu que les sources de spam peuvent changer au fil du temps, et les techniques d'attaques sont pléthoriques usant de technologies variées.

SINON, **retenez 2 types de SPAM**, celui qui ne passe pas par votre site le Spam Fantôme qui envoie juste un signal 'ping' sur l'UA de votre site et celui des robots qui eux viennent scanner votre site web.

--> Ci-dessous, 6** méthodes** pour lutter contre cette pollution malveillante qui agacent nos rapports d'audience dû aux robots.

**1/** Merci à **Simo ahova** développeur expert  pour cette technique qui utilise l'api de google analytics , dont le but est d'installer automatiquement des filtres anti spam dans les vues des propriétés. Deux façons d'utiliser cette outil : en mode complet (à installer sur le serveur web) , en mode invité prêt à l'emploi (donner l'autorisation d'accès à l'application au compte google analytics).

 	- Comprendre le Fonctionnement de l'outil: [ http://goo.gl/DREgdx](http://goo.gl/DREgdx)

 	- Code source: [https://goo.gl/1FW5a](https://goo.gl/1FW5a)4 à installer sur son propre serveur (et ouvrir un accès api sur google console)

 	- Accès prête à l'emploi , une sorte de version démo valable pour se familiariser avec l'outil (fonctionne pour 2000 requetes  jour): http://www.simoahava.com/spamfilter/. Les filtres seront insérés automatiquement dans la vue..pratique !

**2/** Avec  un **fichier htacces**s sur le serveur (copier coller une liste à jour dans l'outil) , syntaxe avec cet outil : http://tools.dynamicdrive.com/userban/

**3/** Avec un** filtre créé manuellement ** (création filtre ga :https://support.google.com/analytics/answer/1034842?hl=fr) en amont dans GA, ici une liste au 20/05/2015 avec la syntaxe à insérer dans le filtre : [http://lonegoatuk.tumblr.com/post/107307494431/google-analytics-referral-spambot-list](http://lonegoatuk.tumblr.com/post/107307494431/google-analytics-referral-spambot-list)

**4/** Sous WordPress par exemple, vous pouvez utiliser aussi **un plugin** (pas testé): https://wordpress.org/support/view/plugin-reviews/spamreferrerblock (vérifier la fiabilité selon les versions WP)

5 / Le **cookie** pour lutter contre le spam de référent provenant de hits malveillant via le protocole de mesure de GA, alors la parade du filtre sur le nom d’hôte de votre domaine ne suffit plus,  car ce "measurement protocol" via son payload passe à au-delà du filtre du hostname, une solution pourtant ,  en 3 étapes ingénieuses :

 	- Créer un **cookie** qui va s’enregistrer sur le poste du visiteur

 	- Déclenchée selon la** valeur du référent** (doit correspondre au nom de domaine du site)

 	- Une **balise google analytics** va récupérer, en plus de la page vue traditionnelle, **via une dimension personnalisée** (créer dans l’admin de GA niveau propriété au préalable)  cette variable stockée par le cookie qui va servir de filtre ensuite en amont dans une vue de cette même propriété.

 	- Source : [http://www.lunametrics.com/blog/2015/03/19/eliminating-dumb-ghost-referral-traffic/](http://www.lunametrics.com/blog/2015/03/19/eliminating-dumb-ghost-referral-traffic/)

 	- Tuto vidéo ci dessous avec l'intégration de **Julien Juenemann** avec [Google Tag Manager](https://www.mauricelargeron.com/passage-de-la-version-1-a-la-version-2-du-gtm/): https://www.youtube.com/embed/rcOf4DOesW8

Cette méthode n’est bien sûr pas infaillible si le spammeur identifie la source du filtre …mais bon, c’est tout de même un bon début de lutte couplée à la méthode 1/ , on peut commencer à y voir plus clair..
6/ --> **Les Spam de referrer** , une seule méthode décrite ci dessous en 2 étapes : vous reperez la présence ou non de spam fantômes et ensuite faire un filtre sur votre nom de domaine.

[![Image](https://www.mauricelargeron.com/wp-content/uploads/2015/09/anti-spam-ga-2-310x192.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2015/09/anti-spam-ga-2.jpg) anti spam ga fantomes
## ***Configuration de compte Google analytics***

### ***Au secours j’ai effacé mon compte Google analytics !***

On à bosser à la communauté Google pour Adwords et Ganalytics en gros suivre ces étapes :

 	- Contactez le support officiel Google Adwords (le support Google Analytics n'existe pas en version gratuite) : [https://support.google.com/adwords/answer/8206?hl=fr](https://support.google.com/adwords/answer/8206?hl=fr)

 	- Google tentera de contacter l'administrateur pour vous

 	- Si ce dernier ne répond pas, vous devrez prouver la propriété du site en ajoutant un fichier .txt

Merci à Valentin pour cet article d’ailleurs **: **[https://www.fr.adwords-community.com/t5/Articles-d-utilisateurs/Article-Comment-r%C3%A9cup%C3%A9rer-son-compte-Google-Analytics/ba-p/46247](https://www.fr.adwords-community.com/t5/Articles-d-utilisateurs/Article-Comment-r%C3%A9cup%C3%A9rer-son-compte-Google-Analytics/ba-p/46247)

Sinon, depuis quelques mois, il est difficile de supprimer par mégarde des entités dans ga avec l’arrivée de la corbeille : https://support.google.com/analytics/answer/6154772?hl=fr&utm_id=ad

### ***Comment transférer un compte GA ?***

3 niveaux dans la hiérarchie : compte GA (sous le compte Google), propriété, et vue. L’idéal est de toujours créer un compte Google puis  GA spécifique  par clients nouveau pour le compte du client (il en possède donc  les identifiants) et ensuite de se positionner comme administrateur « délégué » de ce compte en s’octroyant les droits en conséquence.

Dans la mesure où ce compte GA à des droits suffisants (ici le maxi : modification, collaboration) il suffit de rentrer l’adresse mail (qui possède un compte Google pas forcément Gmail) du futur propriétaire et de se supprimer ensuite, enfin façon de parler J .

En revanche, si plusieurs sites de clients différents  ont été créés au niveau « propriété »  sous un compte GA d’agence, le transfert de propriété sera ingérable. Les lectures simples de rapports pourront se faire au niveau « vue ».

### ***Peux ton faire un suivi global de plusieurs sites à la fois ?***

Tout d’abord dans GA -> admin -> listes exclusion auto référent  il faudra  exclure le domaine en question comme référent

Analytics.js gère cela très bien maintenant avec Google tag manager.  Le but du jeu est de faire suivre les données de session  (enregistré via ga cookie) d’un domaine à l’autre via les liens hypertextes (url) grâce à la collecte du dit cookie et son ajout comme paramètres,  situés après le ? de l’url cliquée.  2 méthodes sont possibles : 1 rajouter au script GA de suivi ceci : ga('create', 'UA-XXXX-Y', 'auto', {'allowLinker': true}); mais cette méthode implique que le lien soit cliquer dans les 2 minutes Sinon, la 2eme méthode est celle de la décoration de lien qui déclenche le tracking uniquement lorsqu’il y a clic ou entrée clavier (voir ici pour plus de détails). Et pour le suivi multi-domaines en cas d’iframe  voir ici : [http://www.knewledge.com/en/blog/2013/11/cross-domain-tracking-for-iframes-with-gtm/](http://www.knewledge.com/en/blog/2013/11/cross-domain-tracking-for-iframes-with-gtm/)

### ***Comment faire importer des marqueurs seo et les rapprocher des pages vues collectées par GA ?***

Le principe est d’importer ces données via un fichier csv dans Ga, c’est possible !  La  configuration, consiste  à déclarer les items à importer : PA, Bl, DA, citation flow, trust flow  (sous forme de dimensions personnalisées de type ga :dimension1, etc)  dans l’admin de GA et à télécharger le fichier .csv templaté par GA. Thasos all folks .Bon , voici un excellent tuto pour l’occasion : [http://www.tatvic.com/blog/dimension-widening-use-case-integrate-page-seo-data-universal-analytics/](http://www.tatvic.com/blog/dimension-widening-use-case-integrate-page-seo-data-universal-analytics/)

[![Image](https://www.mauricelargeron.com/wp-content/uploads/2015/09/seo-et-google-analytics-310x97.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2015/09/seo-et-google-analytics.jpg) seo et google analytics
## **Identification des sources de trafic **

### ***Comment GA interprète les redirections d’url ?***

Ne pas oublier de faire des 301, 302 en règle général GA ne voit rien et retransmet l’origine du référent de la manière suivante (merci à phil pearce pour ce résumé synthétique) :

* 301 > 301 > 200 =** ****référent perdure **(refonte de site)
* 302 > 302 > 200 = **référent perdure  **(exemple lien affilié)
* 302 > 200 meta refresh with delay > 200 =** ****référent perdu ** (page intermédiaire)

Attention dans les redirections http vers https, cela ne fonctionne pas le référent est perdu. Des techniques de Geek existe pour permettre de conserver le référent voir ici : [http://webmasters.stackexchange.com/questions/47405/how-can-i-pass-referrer-header-from-my-https-domain-to-http-domains](http://webmasters.stackexchange.com/questions/47405/how-can-i-pass-referrer-header-from-my-https-domain-to-http-domains)

### ***Pourquoi j’ai des visites provenant de pages non indexée dans Google qui apparaissent comme organiques ?***

GA parfois interprète les sources de trafic selon une certaine préséance : il se peut que lors d'une première visite sur une url indexée normalement dans les serp Google donc estampillée "organique", que ce même visiteur ait fait une recherche, mise en "favoris", avec les url et ses paramètres, puis ensuite revienne plus tard , via ce favori. Ga enregistrera la source comme "organique" et non "directe".

### ***Euh c’est quoi le trafic direct en fait ?***

Quelques sources considérées comme direct de la part de ga :

 	- Le visiteur vous connait (notoriété) il tape l’adresse du site dans sa barre d’adresse

 	- Clic à l’intérieur d’un document PDF

 	- Un lien cliqué dans l’envoi d’un mail (sauf si traqué bien sûr)

 	- Favoris chez le visiteur

 	- Des campagnes non tagguées

 	- Redirection hasardeuse (qui fait sauter la bonne source référente, cas http -> https donné plus haut)

 	- Liens Js qui font sauter le référent

 	- Des petits malins qui font du spam de referrer depuis leur navigateur  :)

 	- Des pages d’accueil qui s’ouvrent sur votre big entreprise, fait du "direct" aussi et fausse les résultats.

 	- Un lien provenant d’une iframe ou le referrer encore passe mal

Google analytics a tendance dans des scénarios de visites répétées de la part d’un même visiteur  de favoriser la source  non directe  s’il celle-ci se situe  en amont ou en intermédiation..

## **Tout sur le Taux de rebond**

### ***Le taux de rebond est proche de zéro, pourquoi ?***

Un taux de rebond faible est déjà un bon point qui souligne l’engagement de l’utilisateur sur un site web car cela indique qu’il se s’arrête pas à sa 1ère page vue de destination, mais continue sa consultation sur une seconde au moins.

Causes possibles :

 	- Certains ajouts d’évènements sur cette « landing page » (suivi d’un clic par exemple) peuvent faire chuter le taux de rebond si ce comportement est paramétré  « comme si «  c’était la consultation d’une autre page vue voir ici : ga('send', 'event', 'category', 'action', {'nonInteraction': 0}); infos : [https://developers.google.com/analytics/devguides/collection/analyticsjs/events](https://developers.google.com/analytics/devguides/collection/analyticsjs/events)

 	- un double appel du code GA sur la même propriété, c’est ballot :) . C’est souvent le cas lors de migration ou cumul d’une collecte classique adossée à celle d’un gestionnaire de tags.

### **J’ai des taux de rebond à 100 %.  Ce n’est pas normal non ?  C’est quoi un bon taux de rebond ?**

Pour faire court, il faut 2 consultations   de pages à Google pour calculer le temps passé lors d’une visite. Le timestamp page 2 - timestamp page 1 = temps total. Mais que se passe-t-il dans le cadre d’une page vue….pendant longtemps ? On peut supposer que le lecteur ne consulte que cette page, il est satisfait et arrête sa visite (souvent le cas de blogs), ou alors une page de destination avec un numéro de téléphone, une adresse, un formulaire (qui ne déclenche rien)  où l’utilisateur est conquis, rien ne sert d’aller plus loin, il possède l’information recherchée. C’est du 100% taux de rebond et 0 seconde en temps passé. On peut déclencher dans GA un évènement basé sur un compteur en secondes qui pourra souligner qu’au-delà d’une timeframe, l’utilisateur a été intéressé.

[![Image](https://www.mauricelargeron.com/wp-content/uploads/2015/09/impact-taux-de-rebond-228x300.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2015/09/impact-taux-de-rebond.jpg) Calcul taux de rebond. Merci à son auteur

***Bon j’ai récupérer ces chiffres sur le site de Blastam.com (toujours de bons conseils) ***

 	- **40-60%**Site de contenus

 	- **30-50%**Acquisition de leads

 	- **70-98%**Blogs

 	- **20-40%**Vente détail

 	- **10-30%**BtoB

 	- **70-90%**Pages de destination

Pour tout savoir sur le taux de rebond…

Encore un super article de Julien Coquet sur le sujet : [http://juliencoquet.com/2014/07/02/taux-de-rebond-definition-demystification-veni-vidi-vomi/](http://juliencoquet.com/2014/07/02/taux-de-rebond-definition-demystification-veni-vidi-vomi/)

### **Taux de rebond, taux de sortie, taux d’abandon  sur une page de destination, quesaquo ?**

Accrochez-vous, cela va chauffer, si vous voulez comprendre les tenants et aboutissants de ces items , suivez ce post ou lisez le plus tard : Merci à Smaïne pour sa contribution !

[https://www.fr.adwords-community.com/t5/Google-Analytics/Rapport-flux-d-utilisateurs/td-p/47840/page/2](https://www.fr.adwords-community.com/t5/Google-Analytics/Rapport-flux-d-utilisateurs/td-p/47840/page/2)

## **Tracking mono-page**

### ***Est-il possible de suivre les #ancres de texte dans les url d’un menu d’une page ?***

Oui bien  sûr, l’idée est de signifier à GA de récupérer les ancres à chaque clics toutes les url avec le « # » : il faudra rajouter à la page vue un petit bout de code :

ga('send', 'pageview', { 'page': location.pathname + location.search + location.hash});

et lui indiquer de bien écouté les clics du visiteur sur le menu sinon, il enverra d’entrée la page vue sans l’ancre  :
&lt;script type="text/javascript"&gt;

jQuery(document).ready(function () {
jQuery('.menu a').click(function(){
var match = jQuery(this).attr('href').match(/#\S+/);
ga('send', 'pageview', location.pathname + match);
});
});
&lt;/script&gt;

### ***J’ai un site une page (à scroller) , comment savoir si le contenu est parcouru ?***

L’idée ici est  d’écouter le scrolling de la page à l’aide d’un script dédié, à chaque étape du glissement de sourie sur l’ascenseur (scindé en 25, 50, 75, 100%) un event est envoyé à GA et voilà…la démo sur cette page (faire F12 muni du plugin GA debug ou le tag assistant).

[![Image](https://www.mauricelargeron.com/wp-content/uploads/2015/09/tag-assistant-scroll-depth-245x300.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2015/09/tag-assistant-scroll-depth.jpg) Rendu par le Tag assistant du scroll depth tracking dans Chrome

***Et le scroll infini alors ?***

Le principe est dans le fond le même, le site push des url qui seront écoutées et associées à des pages vue même si l’on reste physiquement sur la même page.

## **Conversions**

### ***Peut-on avoir des suivis de conversions/objectifs  mutualisés entre GA et Adwords ?***

Oui bien sûr, c’est même plus simple avec Google analytics d’ailleurs, souvent pas de code à copier-coller, juste l’url suffit pour poser des objectifs dans GA dénommés conversions dans Adwords (par association de compte, il suffit ensuite d’actionner la fonctionnalité d’importation des objectifs). Mais attention de ne pas cumuler les 2 moyens.

*** On m’a dit que le suivi que l’attribution de la conversion diffère selon adwords et analytics, vrai ou faux ?***

Vrai ! Pour faire court,  Adwords a souvent la part belle dans l’attribution de la conversion, s’il intervient dans le chemin d’acquisition, mais pas toujours, Ga lui, fonctionne au dernier clic indirect (soit le dernier canal est direct, nada, c’est l’indirect avant qui décroche le pompon) dans sa représentation des chemins de conversion (catégorie conversions -> chemins de conversion)

[![Image](https://www.mauricelargeron.com/wp-content/uploads/2015/09/attribution-des-conversions-298x300.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2015/09/attribution-des-conversions.jpg) Comparatifs Attribution des conversions Ga et Adw
### ***Est-il possible d’annuler une transaction dans ga ?***

Oui, 2 façons :

Par l’envoi de son inverse soit la même transaction id mais en «-«  ce qui ne supprime pas mais annule le montant, l’article etc.. Sans être calé à la date de la transaction à supprimer, d’où problème de synchronisation avec la date réelle, décalage de comptabilisation.

*Je cite l’aide google *

*"Pour annuler une commande ou une transaction, vous devez créer et charger une page de confirmation d'achat dupliquée qui contient des valeurs **négatives** **correspondant au montant total de la transaction (taxes, frais d'expédition et quantité). Par exemple, si le montant de la transaction d'origine s'élevait à 699 euros, l'entrée dupliquée devra indiquer -699 euros comme montant total de la transaction. Google Analytics enregistre cette valeur négative et l'applique à vos totaux, ce qui a pour résultat d'annuler la transaction"*

Sinon, autre choix, faire un rapport personnalisé avec un filtre d’exclusion pour supprimer d’un rapport la transaction  fautive.
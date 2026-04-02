---
title: "Des scripts comme outils d'aide pour sa publicité"
date: 2013-05-15
author: "admin"
categories: ["Outils Web et Marketing"]
tags: []
slug: "utiliser-simplement-le-code-js"
---

Je reviens cette semaine sur une des fonctionnalités qui permet d’automatiser certaines tâches dans la plateforme Google adwords. J’avais déjà ébauché le sujet dans [cet article](https://www.mauricelargeron.com/huit-outils-pour-accelerer-une-gestion-adwords/) il y a quelques mois déjà. Cette fois ci, je vais parler des **scripts adwords**, oui, allez-vous me dire, encore une spécificité pour gérer une campagne !  Tout d’abord, nous recadrerons le débat, puis nous passerons dans le vif du sujet avec des exemples et enfin verrons les limites de cet outil. N’étant pas codeur dans l’âme,  j’avoue qu’écrire un article sur ce sujet m’a rebuté un peu, le post d’[Eric de PPC-Héro](http://www.ppchero.com/3-easy-adwords-scripts-to-analyze-your-account-part-1/) m’a mis le pied à l’étrier :)  .

## Scripts Adwords : origine,  utilité et interface.

Cette fonctionnalité a été déployée en septembre 2012 afin de combler le « gap » entre le développement pur et dur via l’**API adwords**  qui demande des compétences de développeurs et les potentialités des **règles automatiques** déjà présentes sur la plateforme. Les scripts permettent une plus grande flexibilité dans le choix et  l’étendue de leurs indicateurs (croisements) . Une règle automatique par exemple ne peut extraire  un rapport  de données  liées selon leur critère de perf. **avec** un historique spécifique (ex: sur les 3 derniers mois, je souhaite examiner les annonces dont le CTR équivaut à…). Ajoutons   la possibilité de créer des annonces textuelles, des mots clés,  de manipuler des libellés etc...  Pour rester dans le domaine des rapports, pour le non développeur, pas familier avec excel,  certains scripts disponibles prêts à l’emploi donnent accès à l’apprentissage du reporting (voir ci-après), vu que ces derniers produisent par eux même données et graphiques directement lisibles via l’interface de Google docs (drive).

Disponible sur le menu de gauche et positionné dans la catégorie « **opérations groupées** », l’interface  est intuitive et   alimentée par des exemples. Le lien « modifier en masse » situé en dessous,  est quant à lui vouer à des opérations plus simples, souvent fastidieuses comme des "copier-coller"  *(c’est en quelque sorte une version allégée d’adwords éditor, outil externe de manipulation de campagnes).*

[![Image](/images/blog/interface-310x199.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2013/05/interface.jpg) Accessibilité depuis l'iinterface Adw
## Des scripts prêts à l’emploi

### **Focus sur le reporting**

Le centre de développement Google propose un ensemble de scripts pour se faire la main. Mise à part une personnalisation sur certaines variables dans les scripts, un simple vernis de  développeur suffit pour en prendre la main. Pour l’anecdote, Google propose même le cas d’une mise en enchère selon les [prévisions météorologiques](https://developers.google.com/adwords/scripts/docs/tutorials/bid-by-weather) !

[![Image](/images/blog/script-tout-faits-310x210.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2013/05/script-tout-faits.jpg) Menu de scripts à copier-coller
Quality score et Mots clés

Cet [extrait de code](https://developers.google.com/adwords/scripts/docs/tutorials/keyword-performance-report) produit une extraction d’indicateurs segmentée par le **score de qualité**  et les **positions moyennes** des annonces (avec mots clés, impressions, clics, conversions..). Il est parfois surprenant au visuel rendu, de s’apercevoir de certaines tendances, qu’un simple tableau avec ligne et colonne rend aveugle.  Ici,  les QS des mots clés situés entre 8 et 9 sont aux abonnés absents. Il faudrait pousser plus loin l’analyse en corrélant  le nombre de conversions qui leur sont liées.

[![Image](/images/blog/perf-annonces-310x150.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2013/05/perf-annonces.jpg) Extrait Résultat script Perf. Annonces
Taux de clics selon le titre des annonces

Ce [script](https://developers.google.com/adwords/scripts/docs/tutorials/ad-performance-report)  extrait les statistiques d’annonces selon leurs performances (CTR, Titre, Url de destination) avec un graphique, le tout dans un tableur Google docs, que demander de plus ?

[![Image](/images/blog/script-adwords_1-310x261.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2013/05/script-adwords_1.jpg) Etape 1: la table + insersion Url
Extraire des données spécifiques
Ici, l’objectif est de suivre un ensemble de **mots clés de près selon leur score de qualité.** Pour établir ce genre de rapports il faut donc :

	- Installer une **feuille de calcul** sur Google docs avec les éléments que l’on souhaite (liste de mots clés)

	- Récupérer le script *(fournit aimablement par [Martin Roettgerding   ](http://www.ppc-epiphany.com/2012/08/14/an-adwords-script-to-track-quality-scores/) )*

	- Insérer l’url de la feuille de calcul dans ce code

[![Image](/images/blog/qsetMotcles-310x151.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2013/05/qsetMotcles.jpg) Extraction choisie de Mot Clé

Il y a possibilité pour ces scripts de les recevoir dans sa boîte mails.
### Extraits de scripts divers à tester 

Variation de textes d'annonces
[http://adwords-scripts.blogspot.fr/2012/12/google-adwords-optimization-strategies.html](http://adwords-scripts.blogspot.fr/2012/12/google-adwords-optimization-strategies.html)
Alerte suite à une chute d'impressions
[http://econsultancy.com/fr/blog/10685-using-google-s-adwords-scripts-to-set-rules-on-your-campaign](http://econsultancy.com/fr/blog/10685-using-google-s-adwords-scripts-to-set-rules-on-your-campaign)
Partage des budgets selon un  pourcentage
Jours Sans impressions de mots clés
Extraction de budgets journaliers
Trois scripts [Disponibles ici  par  le site cobnut.net ](http://www.cobnut.net/adwords-scripts.php)
Statistiques globales sur le score de qualité
[http://deepfootprints.co.uk/online-marketing/ppc/adwords-script-to-track-quality-score-on-account-campaign-ad-group-level/](http://deepfootprints.co.uk/online-marketing/ppc/adwords-script-to-track-quality-score-on-account-campaign-ad-group-level/)
Divers conseils de scripting avec exemples de search engine land
[http://searchengineland.com/4-ways-to-take-your-adwords-scripts-to-the-next-level-155593](http://searchengineland.com/4-ways-to-take-your-adwords-scripts-to-the-next-level-155593)
Prestataires : [http://www.optmyzr.com/scripts/](http://www.optmyzr.com/scripts/)
## Limites du Javadwords !

Comme tout se gère en ligne, sur le cloud de Google, sans frais supplémentaire,  rien n’est illimité. Un script doit  par conséquent :

	- Retourner au maximum 50 000  entités par littérateur qu’il contient (mots clés, annonces, groupes, ou campagne)

	- Peut manipuler jusqu’à 250 000  entités au total

	- Peut créer jusqu’à 250 000 mots clés et annonces.

	- Pas dépasser 30 minutes pour son exécution et enfin les logs sont limités à 100kbits.

	- Ne peut s'adapter sur du google Adw express ou Vidéo.

	- Je rajouterais que seulement 15 scripts maximum par compte adwords sont autorisés.

Bien que je n'ai souligné ici comme illustrations que du reporting, je confirme que les scripts adwords sont aussi d'une aide puissante pour du monitoring de stratégie de campagne (budget, enchères).
 
Plus d’infos :

	- Ressources G. https://developers.google.com/adwords/scripts/community .A noter que la documentation et les tutoriels sont plus fournis sur la plateforme anglaise que française.

	- Usages :

http://purevisibility.com/blog/search-engine-marketing/ppc/google-adwords/adwords-scripts-for-editing-prices-in-ads/
http://ppcchat.co/2013/03/adwords-scripting-ppc-chat-streamcap/
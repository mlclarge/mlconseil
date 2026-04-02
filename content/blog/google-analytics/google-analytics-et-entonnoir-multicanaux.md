---
title: "Suivre ses actions webmarketing dans une conversion"
date: 2012-09-20
author: "admin"
categories: ["Google Analytics"]
tags: []
slug: "google-analytics-et-entonnoir-multicanaux"
---

Comment mesurer le **poids des différents canaux marketing** lors d’une conversion online ? Je rappelle qu’une conversion regroupe une action que l’on souhaite voir accomplir sur son site *(téléchargement, formulaire rempli, une page vue, un évènement)*, ou  représente tout simplement **une transaction**… banalité dans l’univers de l’e-commerce.  Pouvoir juger de l’impact des différents maillons de la chaîne multicanal peut s’avérer utile surtout pour arbitrer ses budgets webmarketing. j'avais déjà ébauché le thème de l'analyse multicanal il y a quelques mois déjà.

Dans un premier chapitre, je donnerai  du  contexte à  cette analyse  en la resituant dans son **contexte marketing**, puis, dans un second temps, recentrerai le débat sur les différents **leviers e-marketing ** placés dans un contexte d’entonnoir de conversion. Je clôturerai ce billet par une description de la  **fonctionnalité récente de  Google analytics** : l’analyse des entonnoirs multicanaux (2011). Mais avant tout, peut- on tout mesurer ?

## **Quels outils pour mesurer ses actions Online, Offline, multi-écrans, multicanaux ?**

Tous les consultants au top de l’analyse d’audience vous rassureront par un ‘oui’ notre solution unique permet de …Mais c’est oublier qu’aujourd’hui, même si le tracking comportemental a fait des progrès, que le profilage devient de plus en plus précis, n'omettons pas le fait que l’on trace toujours des audiences à base de cookies installés sur une machine, pas sur une personne !

### Poids du Offline vers  le Online

Certes avec les moyens du bord, on va pouvoir tracker les répercussions de **campagnes offline dans le mix média** de la conversion. Dans le Print, il conviendra d’imprimer des urls simplifiées pour mémorisation  sur les annonces et prévoir  une redirection spécifique taguée pour l’analyse, de même que pour les QR codes, le couponing. Des enquêtes  sur un panel  consommateurs pourront aussi être menées en complément, mais le déclaratif à toujours ses propres biais.  La fluctuation du  trafic direct pourra être aussi corrélée  à la date de démarrage d’une campagne radio, tv ou autre.

### Impact du Online vers le retail  *(effet ROPO)*

Chemin inverse ici, les offres nouvelles "Web to Store" devront être elles aussi uniques : numéro d’appel, coupons de réduction à imprimer, trafic sur la page de localisation du magasin sans oublier les enquêtes en magasin auprès d’échantillon de clients.

### **Tracker les Multi-écrans**

Là aussi, quel impact aura eu la visite suite à un lien sponsorisé  depuis un  Smartphone  sur une conversion effectuée au bureau ou à mon domicile ? N’oublions pas, un appareil = un cookie pas un internaute.

### **Analyse digitale Multicanal**

Ah, nous y sommes enfin ! Est-il possible d’attribuer  l’impact de chaque canal lors d’une conversion ?  Je rappelle que les canaux peuvent être une opération emailing, une campagne organiques (seo), du trafic direct, des liens sponsorisés, une syndication (flux rss), une campagne display, un  programme d’affiliation, une action sur les réseaux sociaux.  Mais où replacer ces leviers dans l’obtention d’un acte d’achat ?
L’attribution d’une source de visite génère **3 types de mesure** selon les outils employés.

**As Centric** : mesure d’une agence de com. Sur  la performance de leur  seul canal « apporteur d’affaire » sans se préoccuper  de l’influence d’autres canaux  dont ils ne sont pas les opérateurs (affiliation, bannières, display)

**Site Centric** : Ici on consolide par un plan de taguage tout le flot de clics et donc ses sources de trafic qui entrent dans l’accomplissement de la conversion.

**User Centric** : Elle répertorie l’ensemble des supports publicitaires auxquels un visiteur a été soumis préalablement à une conversion.  Pas d’outil miracle donc, bien que des éditeurs s’y attache bien sûr (AT internet, Site  catalyst..), il faudra donc jongler sur plusieurs  solutions afin d’intégrer données online (multi-écrans, multicanaux, CRM, erp)  et Offline (pris, tv, radio), en extraire les données pertinentes et les agréger dans un tableur personnalisé afin d’avoir une vision 360° ou du moins, tenter d’en approcher. Mais venons-en au concept d’entonnoir multicanal, décryptage.

### **L’entonnoir multicanal balise le cheminement de l’internaute**

Essayons de comprendre le concept d’entonnoir multicanal et revenons sur la mesure multicanal online. La trame online des opérations de webmarketing peuvent se résumer à un processus en 3 phases : Attraction, Argumentation et Persuasion et Conversion.

[![Image](/images/blog/Fig.1-Entonnnoir-de-conversion-253x300.png)](https://www.mauricelargeron.com/wp-content/uploads/2012/09/Fig.1-Entonnnoir-de-conversion.png) Fig.1 Entonnnoir de conversion

A cette trame correspond, généralement, des phases d’actions webmarketing. J’ai repris et traduit pour illustration le tunnel de conversion de la compagnie américaine seomoz.org (merci !)

[![Image](/images/blog/Fig.2-tunnel-emarketing-multicanal-310x281.png)](https://www.mauricelargeron.com/wp-content/uploads/2012/09/Fig.2-tunnel-emarketing-multicanal.png) Fig.2 tunnel-emarketing-multicanal

Pour résumer et dégrossir l’idée de ce tunnel de conversion on peut dire, sans faire de généralité bien sûr, qu’en haut du tunnel, on retrouve le canal display (affichage)  et du trafic organique pour attirer le chaland, puis dans une phase intermédiaire, les liens sponsorisés  qui argumentent et persuadent de la bonne affaire en captant les requêtes ciblées de l’internaute en phase d’achat. Du retargeting peut le ramener s’il s’échappe de l’entonnoir. Enfin, une belle page de destination dont la source peut provenir d’un affilié  scellera la conversion. Maintenant, quel outil utiliser pour mesurer ce cheminement ?

## **Analyse multicanal dans Google analytics**

**Interface dans G. Analytics**

Cette application va aider à comprendre ce qui a bien pu se passer avant le passage à la conversion. Normalement, GA attribue la conversion au dernier canal, soit dans l’exemple cité plus haut, au lien de l’affilié, mais quid de ce qui s’est passé avant ? Le suivi des interactions se fait pendant 30 jours, et GA compte tous les chemins de conversions et les compile afin d’avoir des rapports lisibles. Chaque canal est égal à une source (organique, emailing..)

[![Image](/images/blog/fig.3-interface-multicanal-ga-310x248.png)](https://www.mauricelargeron.com/wp-content/uploads/2012/09/fig.3-interface-multicanal-ga.png) fig.3 Interface-multicanal-ga

Le menu de cet entonnoir est constitué de 2 sous parties. Les conversions indirectes, ce sont les canaux attribués par GA comme faisant partie du cheminement de conversion, ils ont contribué à la conversion, même s’ils n’ont pas été les derniers clics avant l’acte final. Dans le cas où ils sont présents comme canal indirect et direct, ils seront comptabilisés 2 fois en valeur. C’est un des biais de la mesure.

[![Image](/images/blog/Fig.4-Conversions-indirectes-1-310x126.png)](https://www.mauricelargeron.com/wp-content/uploads/2012/09/Fig.4-Conversions-indirectes-1.png) Fig.4 Conversions indirectes
**Méthode pour avoir un entonnoir multicanal fiable**

	- Paramétrer des objectifs (avec valeurs), un panier e-commerce (transactions), bref jalonner le parcours. Si ces éléments n’y sont pas, l’entonnoir multicanal restera muet, avec un encéphalogramme plat J .

	- Laisser remonter les données et observer les groupes de canaux par défaut. Si ces derniers laissent apparaître des zones pas très explicites, constituer son propre groupe de canaux (fig.5).

[![Image](/images/blog/Fig.5-Modification-canal-GA-294x300.png)](https://www.mauricelargeron.com/wp-content/uploads/2012/09/Fig.5-Modification-canal-GA.png) Fig.5 Modification canal GA

	- Toujours utiliser  cette fonctionnalité sur un profil vierge de tout filtre, sinon les données seront tronquées.

	- Consulter GA en faisant des corrélations  : les chemins les plus fréquents, pendant 30 jours,   corrélé au chemin des mots clés par exemple (dans le cadre de cpc), cela peut aider à mieux discerner ceux qui manquent ou qui pourraient compléter une visibilité dans une campagne de liens sponsorisés. (fig. 6)

[![Image](/images/blog/Fig.6-Chemin-fréquents-ganalytics-310x50.png)](https://www.mauricelargeron.com/wp-content/uploads/2012/09/Fig.6-Chemin-fréquents-ganalytics.png) Fig.6-Chemin-fréquents-ganalytics

Niveau avancé (premium)

L’entonnoir multicanal, permet donc de se rendre compte des différentes interactions qui surviennent lors d’une conversion, mais il n’indique pas le poids supposé de chacun des canaux.

En effet, selon son marché (b to b / b to c), sa stratégie (marque, conversion directe..), vaut-il mieux  pas plus focaliser  ses mesures sur le premier canal (ou point de contact), ou bien  le dernier, et pour ceux intermédiaires, le reste ? C’est ce que l’on appelle des modèles d’attributions. Cela peut aboutir à donner une répartition comme celle-ci (fig. 7 Source : aide Google analytics)

[![Image](/images/blog/Fig.7-Modele-attribution-301x300.png)](https://www.mauricelargeron.com/wp-content/uploads/2012/09/Fig.7-Modele-attribution.png) Fig.7 Modele attribution (source Google Analytics)

Ce paramétrage n’est possible que dans la version payante de Google analytics (fig.8).

[![Image](/images/blog/Fig.8-model-attribution-ganalytics-310x163.png)](https://www.mauricelargeron.com/wp-content/uploads/2012/09/Fig.8-model-attribution-ganalytics.png) Fig.8 model attribution ganalytics                                            (source havinash KausHik)
### Conclusion sur les rapports de l'analyse multicanal

Selon les **modèles d’attribution**, les combinaisons de canaux, leurs segmentations, l’analyse multicanal peut être très personnalisée.  A partir de ces rapports de cheminement vers la conversion, il est possible d'ébaucher   le montant total des canaux digitaux (CPCs + emailing + commissions + Seo) qui ont amené à 1 conversion.  Mais attention à ne pas trop se focaliser sur ce seul  aspect car il ne constitue qu’une pièce du puzzle de l’analyse marketing.
Liens utiles

[http://support.google.com/analytics/bin/answer.py?hl=fr&utm_id=ad&answer=1191180](https://support.google.com/analytics/bin/answer.py?hl=fr&utm_id=ad&answer=1191180)

[http://www.kaushik.net/avinash/multi-channel-attribution-data-culture-analysis-faq/](http://www.kaushik.net/avinash/multi-channel-attribution-data-culture-analysis-faq/)
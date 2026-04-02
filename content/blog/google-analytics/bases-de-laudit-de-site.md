---
title: "Les bases du web analytics"
date: 2011-07-07
author: "admin"
categories: ["Google Analytics"]
tags: []
slug: "bases-de-laudit-de-site"
---

Avoir une présence sur Internet c'est bien, l'optimiser (seo, référencement) , la faire connaître (publicité) sont aussi des étapes indispensables. Mais pouvoir répondre aux questions suivantes sont les objectifs du web analytics, de l'audit de site  : Combien d'internautes visitent mon site ? Que recherchent-ils ? Comment cliquent-ils ?

Les ouvrages principaux qui, parmi d'autres sources, m'ont aidé à faire ce billet sont "Google analytics" d'A. Boydell, S.Descombes et S.Manaches, "Web analytics" 2.0 d'a. Kaushik.

Je développerai dans cet article sur l'audit de site,  4 chapîtres qui donneront l'essentiel pour démarrer dans l'analyse web de données (web analytics):

	- Vocabulaire

	- [Les principes généraux du Web analytics (collecte,personnalisation)](#principes)

	- [Les outils (gratuits, payants)](#outils)

	- [L'analyse (Chiffres, Kpi)](#Analyse)

## Vocabulaire

Je me suis inspiré du glossaire Google et  d’oseox.fr pour établir cette liste de termes.

	- **Accès direct** : Accès au site web en tapant l’URL exacte dans la barre d’adresse du navigateur. L’accès au site via un marque-page est considéré comme un accès direct également.

	- **Clic :**Dans les rapports Google Analytics, un clic fait référence à une seule instance d'un utilisateur qui suit un lien hypertexte d'une page de site Web vers un autre site. Par exemple, les clics qui s'affichent dans le rapport Synthèse données/site indiquent à combien de reprises un utilisateur a cliqué sur un lien hypertexte sur la page sélectionnée pour accéder à une autre page.

	- **Contenu (suivi de campagne) :** Lors de l'insertion des [balises de liens](http://www.google.com/support/googleanalytics/bin/answer.py?answer=55518&topic=7154), le contenu permet d'identifier différentes versions d'une annonce. La variable du contenu, utm_content, indique sur quelle version d'un lien le visiteur a cliqué pour atteindre un site Web, par exemple, utm_content=graphic_v2. Le contenu correspond à l'un des cinq éléments du suivi de campagne, les quatre autres étant la source, le support, la campagne et le terme.

	- **Le code de suivi **de Google Analytics est un petit extrait de code qui est inséré dans le corps d'une page HTML. Lorsque la page HTML est chargée, le code de suivi contacte le serveur Google Analytics et enregistre une consultation de page pour cette page. Il collecte également des informations sur la visite et des informations sur le visiteur .

	- **Compte** : Ensemble de profils de sites internet

	- **Conversion** : Une conversion, ou transformation, se produit lorsqu'un visiteur atteint un *objectif* (objectif peut être une page de confirmation d'achat, une page de remerciement d'enregistrement, une page de téléchargement ou une présentation en ligne.)

	- **Cookie** : Petit fragment de données au format texte qu'un serveur Web envoie à un navigateur Web.  il stocke les sources de trafic des internautes ainsi que d'autres informations non nominatives. Ces données sont stockées sur le disque dur de l'utilisateur et renvoyées à un serveur Web spécifique à chaque fois que le navigateur demande une page à ce serveur.

	- **Entonnoir de conversion** : Parcours de l’internaute avant d’effectuer une action de conversion sur un site internet.

	- **Expression régulière** : Script informatique permettant d'isoler des sous ensembles réguliers.

	- **KPI** : L’ indicateur clé de performances (Key Performance Indicator) permet de mesurer l’impact d’une action suivie d’un modèle défini en amont

	- **Objectif** : But à atteindre en fonction d’une stratégie.

	- **Organic** : Trafic en provenance des moteurs de recherche. La valeur du support est : Organic

	- **Page de provenance **: L’URL d'une page HTML qui redirige les visiteurs vers un autre site.

	- **Pages vues** : Nombre de pages consultées sur une période donnée.

	- **Pages par visite** : Nombre de pages consultées de manière successive, c’est à dire, durant une même session de visite.

	- **Plan de marquage** : Opération qui consiste à organiser, structurer et nommer l'ensemble des campagnes e-marketing pour une cohérence optimale des rapports de données de Web Analytics.

	- **Profil** : Règles définies pour l’affichage d’un rapport d’un site web

	- **SEO** : Acronyme de Search Engine Optimization qui signifie Référencement naturel.

	- **SEM** : Acronyme de Search Engine Marketing qui signifie Liens sponsorisés.

	- **Session **: Période d'interaction entre le navigateur du visiteur et un site Web particulier, qui se termine lorsque le visiteur ferme la fenêtre ou le programme de navigation, ou lorsqu'il n'effectue aucune action sur le site pendant une durée donnée. Dans le cadre des rapports Google Analytics, une session est considérée comme terminée si l'utilisateur est inactif sur le site pendant 30 minutes. Vous pouvez mettre à jour ce paramètre par un ajout à votre code de suivi.

	- **Referrer** : Trafic en provenance d’un site tiers (partenaires, annuaire, etc)

	- **Sites référents** : Sites qui font un lien vers un autre site

	- **Segment** : Sous ensemble de données statistiques.

	- **Source de trafic** : Site de provenance de l'internaute avant une visite sur un site.

	- **Taux de rebond** : Pourcentage de visiteurs qui n’ont parcouru qu’une seule page sur un site donné

	- **Variable personnalisée** : Élément permettant la segmentation des visiteurs de manière personnalisée.

	- **Visites** : Session de consultation d’un site (ensemble de plusieurs pages vues sur un site et de manière successive)

	- **Visiteur **: Le terme « Visiteur » est une abstraction dont le but est de fournir, avec le plus de précision possible, le nombre de personnes réelles et distinctes qui ont visité un site Web. Évidemment, il n'existe aucun moyen, à partir du site Web visité, de savoir si deux personnes partagent un ordinateur, mais un système de suivi des visiteurs de bonne qualité peut fournir un nombre assez près de la réalité. Les systèmes de suivi des visiteurs les plus précis utilisent généralement des cookies pour évaluer le nombre de visiteurs distincts.

	- **Nouveaux visiteurs **: Dans Google Analytics, un visiteur est considéré comme "nouveau" lorsqu'il accède pour la première fois à une page de votre site à partir d'un navigateur Web. Un cookie propriétaire est alors enregistré dans son navigateur. Par conséquent, les nouveaux visiteurs sont identifiés grâce à leur navigateur Web, et non à partir des informations personnelles qu'ils fournissent sur votre site.

	- **Visiteurs uniques :** Les visiteurs uniques représentent le nombre de visiteurs de votre site Web non dupliqués (comptabilisés une seule fois) sur une période de temps donnée. Un visiteur unique est déterminé à l'aide des cookies.

## **Les principes généraux du Web analytics **

**La Collecte des données (appliquée ici pour google analytics) **

Elle peut se faire de 2 manières principalement, d'une part par l'exploitation des données collectées sur des fichiers  journaux ou fichiers logs, d'autre part par l'installation de marqueurs Javascript sur les pages web. Sinon, d'autres moyens existent comme les renifleurs de paquets ou des appels de pixels invisibles.

Nous verrons ici, la plus répandue, celle à partir de marqueurs Javascript.

La collecte les données *(extrait traduit depuis le site : *[*http://code.google.com*](http://code.google.com/)* )*

En général, le code de suivi Google Analytics (GATC) récupère les données page web comme suit

[![Image](/images/blog/collecteDonnées1-246x300.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2011/07/collecteDonnées1.jpg) collecte donnees

1.  Un navigateur demande une page Web qui contient le code de suivi.

2. Un tableau de JavaScript nommée _gaq est créé et les commandes de suivi sont envoyés dans ce tableau.

3. Un  élément est créé et activé pour le chargement asynchrone (chargement à l'arrière plan).

4. Le ga.js code de suivi est récupérée, avec le protocole approprié est détecté automatiquement.Une fois le code récupéré et chargé, les commandes sur le  tableau _gaq sont exécutés et le tableau est transformé en un objet de suivi. Après les appels de suivi sont faits directement à Google Analytics.

5. l'élément script pour les DOM.

6. Après le code de suivi recueille des données, la demande GIF est envoyé à la base de données Google Analytics pour exploitation  et post-traitement.
**Le Balisage :**

Afin de suivre l'impact des campagnes de publicité, il convient de baliser tous les liens situés sur ces encarts publicitaires. L'utilisation de Google analytics et Adwords comme prestataire pub, le balisage des urls se sait automatiquement, sinon, pour d'autres plateformes comme Yahoo! microsoft, il conviendra de "tagguer" les urls afin de pouvoir faire un suivi séparé des retombées de chaque campagne.
**Mesures des interactions :**

Les marqueurs Javascript permettent de suivre plusieurs types d'interactions selon les contenus sur la page web. A chaque besoin, des fonctions Javascript (JS) seront rajoutées .

Voici les differents types de suivi et quelques cas possible :

•     ** E-commerce ** sur la page de confirmation d'achat : ajouter code : _pageTracker , _addItem, _addTrans, _trackTrans)

•        **Evènements** : lecture de vidéo, téléchargement de fichier, widgets flash, ajax...

	- Ajout de code : _trackEvent (4 suivis :categorie, action, label, valeur)

	- Catégorie: vidéo, pdf, flash

	- Action :lecture, pause, téléchargement,jouer, partager

	- Label: andeannonce, interviews

	- Valeur : nombre  d'euros..

•      **Chargement des pages **: ajouter code _timeTracker avec option selon les écarts des durées mesurées.

•      **Entonnoir de conversion : ** une série d'urls des pages sont suivis et dans un certain ordre (ex: panier marchand avec page catalogue puis page produit, panier, enregistrement et...)

•      **Autres interactions **: Suivis des liens , des pages dynamiques (ou urls ne change pas: ajonction d'urls virtuelles) , page "404".

**Personnalisation de la collecte des données**

*Principe d'une "**valeur" **personnalisée* : ajout encore de code sur l'élément qui personnalise le groupe à identifier. Un élément peut être une page, un lien (bouton de validation) , un formulaire. Cette ajout de code génère un cookie nommé "_utmv".

*Principe d'une "**variable" **personnalisée (segmentation) *: Segmenter en fonction du comportement visiteur, plusieurs variables par fichier ".gif" sont requetées. Les champs d'application sont le visiteur, la session, et la page avec l'ajout de code _setCustomVar.

**Suivi manuel des clics **

Oui, c'est possible ave google ! Configurez le code de suivi avec la fonction _trackEvents, ajouter la méthode dans la balise   puis modifier les liens sortants avec appel appel de la fonction "onClickOutBoundLink" avec ses paramètres.

**ENCORE LES BONNES QUESTIONS A SE POSER !**

Selon les besoins, l'outil d'analyse du traffic peut être configuré de diverses manières avec des profils variés.

**Suis-je intéressé plus par l'optimisation en recherche naturelle (orientation technique) ? **

Auquel cas, mon suivi aura un profil dédié et paramétré pour suivre les SERP, les requêtes sur le site (suivi du moteur de recherche  interne), la protection des urls des effets du tagguage

**Est-ce que je souhaite optimiser ma campagne d'acquisition de trafic (orientation marketing) ?**

Auquel cas, je ferai un profil dédié pour le suivi de ma campagne de liens sponsorisés Adwords par exemple,  filtrerai les requêtes sur les moteurs, m'attacherai de suivre le traffic des sites référents avec des valeurs personnalisées, adapterai la durée du cookie selon la  campagne.

**Améliorer le contenu et  l'utilisation du site (orientation technique) ?**

Je devrai catégoriser mes pages à l'aide de variables personnalisées pour connaitre le contenu et le détail des pages consultées, paramétrer le suivi des requêtes de recherche sur le site (abouti ou à zéro résultat), controler le suivi des pages d'erreur, récupérer le contenu saisi dans les formulaires..etc

## **Les outils**

**Analyse des clics **

*-> Gratuits*

	- [Piwik ](http://piwik.org/)(Opensource)

	- [Open Web analytics ](http://www.openwebanalytics.com/)(Opensource)

	- [Google analytics](http://www.google.com/intl/fr/analytics/)

	- [web.analytics.yahoo.com](web.analytics.yahoo.com)

*-> Payants *

	- h[ttp://www.omniture.com/en/](http://www.omniture.com/en/)

	- [http://www.unica.com/france/index.htm](http://www.unica.com/france/index.htm)

	- [Coremetrics](http://www.coremetrics.fr/)

	- [Webtrends](http://www.webtrends.com/)

* Plus d’infos (anglais, sorry !) :*

[http://web-analytics-review.toptenreviews.com/](http://web-analytics-review.toptenreviews.com/)

**Expérimentation et test **

*-> Gratuits*

	- Google website optimizer

*-> Payant *

	- [http://www.sitespect.com](http://www.sitespect.com/)

	- http://www.optimost.com/

**Intelligence concurentielle**

	- [Google adplanner](https://www.google.com/accounts/ServiceLogin?hl=fr&service=branding&ltmpl=adplanner&continue=https%3A%2F%2Fwww.google.com%2Fadplanner%23main%3Fhl%3Dfr)

	- [Trends](http://www.google.fr/trends)

	- [Compete](http://www.compete.com/)

**Ecoute Client**

	- **[http://fr.crmmetrix.com/](http://fr.crmmetrix.com/)**

## **L'analyse **

Précision : ne pas confondre chiffres bruts et indicateurs clés de performance (kpi : key performance indicator). Le nombre de pages vues, de visiteurs, de visiteurs uniques ne sont pas des kpi. Les kpi sont des taux , des moyennes, des quotients qui fournissent un contexte dans la durée et utilisent des repères (couleurs, jauges, thermomètres..) , leurs buts de conduire à des actions d'amélioration.

**Les points principaux :**

	- Visites et visiteurs : quotidien, hebdomadaire, mensuel, absolus (fidélité visiteurs).

	- Durée de visite : par Page et par site.

	- Taux de rebond : consultation d'une seule page, puis sortie du site (kpi).

	- Satisfaction des visiteurs : à l’aide d’un sondage en sortie de site.

	- Abonné au flux RSS : feedburner est un excellent outil

	- Pourcentage de sortie qualifiée : internaute qui quitte le site sur un élément de valeur.

	- Taux de conversion : défini selon vos objectifs.

	- Abandon du panier

	- Jour et visite avant achat

	- Valeur moyenne des commandes

Je traiterai d'une manière détaillée dans de prochains articles, les différents aspects traités aujourd'hui (collecte des données, analyse).
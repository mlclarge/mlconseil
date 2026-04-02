---
title: "Halte au Spam de référents fantômes !"
date: 2015-02-16
author: "admin"
categories: ["Google Analytics"]
tags: []
slug: "usages-des-filtres-antispam-dans-google-analytics"
---

J’ai une l’occasion de remarquer il y a quelques semaines lors d’une [formation sur  Google analytics ](https://www.mauricelargeron.com/ateliers-referencement-bordeaux/)que 2 comptes GA de participants étaient touchés par des sources douteuses  de trafic référent pour ne pas dire un peu  spammy .  « Updowner », « Semalt » étaient déjà connus dans le circuit, mais **darodar** non ! Ce cas  a fait depuis le buzz et 10 fois le tour de la toile, mais j’y reviens cette semaine car ce fait divers constitue un bon prétexte pour parler de l’usage des **filtres google analytics** comme remède à ce fléau (bon le mot est un peu fort sans doute).

## **Origines, objectifs, fonctionnement de ce "spam de referrer Darodar"**

La technique utilisée est très ancienne,  bots serveurs, script malveillants sur les navigateurs. Cette technique est utilisée (et fonctionne encore, la preuve)  en seo pour acquérir des visites rétroactives en simulant une source de trafic à une cible (quelconque domaine)  et  éventuellement provoquer la création des liens retours vers son site (**backlinks**).

Ce bot « darodar » ici  est un «visiteur fantôme » construit pour simuler une pseudo visite et marquer son territoire par une fausse identification sur la provenance du visiteur (référent). Le script envoie une pseudo requête http:// directement sur les **serveurs de Google analytics**,  munie des bonnes variables avec les numéros de comptes GA Id qu’il créé  aléatoirement.  De vrais comptes GA sont touchés,  sans passer par le site web !  On aurait pu avoir ce même genre de phénomène avec une page infectée par un script malicieux qui établit une redirection forcée du navigateur avec génération d’une visite  (clics, scroll..), mais non, rien de tel ici, donc le **site web n'est pas attaqué,** ouf  ! D’où son appellation anglophone de  « ghost referral». Tout type de site est touché, cms, ecommerce, standalone, donc pas uniquement Wordpress.

[![procedes-spam-referrer-310x243.jpg](/images/blog/procedes-spam-referrer-310x243.jpg) Procédés spam referrer

Google analytics a été le premier à se faire prendre , vu qu’il ne le filtre rien. Le propriétaire du site, le webmaster, l’analyste  se font prendre à son tour vu que l’arrivée d’une nouvelle source de trafic suscite toujours l’attention et encourage  d’aller cliquer sur le lien qui amène ce trafic.  Le clic vers  ce référent  véreux  aboutit souvent à **une page redirigée et  commerciale**.  Résultat ? une page vue supplémentaire dans le sac !  Bon je ne sais pas si les auteurs le font véritablement pour cela, enfin..

[![spam-referents-google-analytics-291x300.jpg](/images/blog/spam-referents-google-analytics-291x300.jpg) Spam de referents google-analytics

A ce jour, je rassure, il n’y a pas d’effet négatifs sur le **ranking de site** via à vis des moteurs de recherche. Il ne manquerait plus que ça ! Déjà le désagrément de voir un faux trafic n’est pas très plaisant, mais si en plus, cela pénalisait le site !

## **Eviter que les sources de spam arrivent  dans GA  ?**

	- **Côté serveur (Htaccess)**  : s’il n’y a pas de réelle ping sur le serveur web du site, le filtrage par ip ou  par identification du référent, ne marchera pas. Sinon, pour les bots qui passent réellement sur le site comme semalt et consorts, des parades existent , voici un exemple de parade :

# Exemple Bloquer semalt
RewriteEngine On
RewriteCond %{HTTP_REFERER} semalt\.com
RewriteRule ^.* - 
# Exemple bloquer buttons-for-websites
RewriteEngine On
RewriteCond %{HTTP_REFERER} buttons\-for\-website\.com
RewriteRule ^.* - 

	- **Côté client (navigateur) **: euh…non plus, vu que rien ne passe de ce côté-là !

## **Nettoyer les rapports du trafic spammé dans Google analytics**

il ne reste plus qu’à utiliser les filtres …profitons de les  détailler..

	- **Filtres  de vues coté « admin »** en amont au sein d’une vue : permet d’une façon permanente de filtrer l’arrivée  des sources référents fautives (faire un tri inverse et ne laisser passer que les référents connus peut s’envisager aussi). Depuis peu, pour être sûr de son coup, GA propose de tester « live » les conséquences du tri. Il faudra attendre le trafic à venir, pour avoir les rapports nettoyés. L’utilisation de regex permet de filtrer un ensemble de sources indésirables. Notez la limite à 250 caractères par filtres, il faudra donc les démultiplier si la liste du spam est longue..

[![filtres-google-analytics-310x209.jpg](/images/blog/filtres-google-analytics-310x209.jpg) Filtre de vue

	- Dans les rapports standards, **un filtre de table,** permet, lorsque l’on ne peut pas attendre l’effet du  filtre admin, de trier les traces du ou des bots malveillants.

[![filtres-de-table-ga-310x141.jpg](/images/blog/filtres-de-table-ga-310x141.jpg) Filtre de table GA

	- **La segmentation** peut venir aussi en aide pour éclairer le reporting et le contexte des referrers spammy. Dans l’exemple ici, le segment appliqué est inclus, ce qui permet d’avoir une proportion du faux  trafic  en %. Attention la syntaxe en expression régulière n’est pas la même qui celle des filtres, pourquoi ? Je ne sais pas ! Si Julien Coquet passe par là, il doit avoir une idée certainement.

[![segments-filtres-anti-spam-310x161.jpg](/images/blog/segments-filtres-anti-spam-310x161.jpg) Segmentation et évaluation trafic S.

	- Autre solution disponible pour **dépolluer les rapports personnalisés** c’est la création  d’un **filtre d’exclusion**, qui élimine par expression régulière, les sources de trafic inutiles.

	- Enfin, autres solutions de secours :  vu que darodar ne s’attaquerait semble t-il que les ID de compte avec un UA-XXXXXX-1x, il est envisageable de générer une nouvelle propriété munie d’une se terminant pas UA-XXXXXX-2x . L’inconvénient, c’est la perte d’historique des données…

## **Des pages qui peuvent enrichir le sujet **

	- Doc GA : [https://support.google.com/analytics/answer/1034842?hl=fr](https://support.google.com/analytics/answer/1034842?hl=fr)

	- Alternatif :   [http://www.bee4.fr/spam-referer-pollueur-de-stat**/**](http://www.bee4.fr/spam-referer-pollueur-de-stat/)****

	- Technique :http://www.blackmoreops.com/2014/12/19/darodar-com-referrer-spam/
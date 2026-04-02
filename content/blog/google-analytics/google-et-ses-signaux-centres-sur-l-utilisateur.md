---
title: "Rapports multi-appareils avec les signaux de Google Analytics"
date: 2018-09-24
author: "admin"
categories: ["Google Analytics"]
tags: []
slug: "google-et-ses-signaux-centres-sur-l-utilisateur"
image: "/images/blog/rapports-google-analytics-m.jpg"
---

Cela y est, [Google](https://support.google.com/analytics/answer/7668466?hl=fr&ref_topic=7668613) fait sensation avec cette nouvelle fonctionnalité de **tracking multi-appareils** qui est en version bêta pour l’instant mais qui va déployer d’ici quelques jours sur tous les comptes **Google Analytics**. Cela faisait un moment que cela mijotait dans les data centers et voilà chose faîte, cela est déployer dans les comptes. Jusqu’à présent, Facebook avec sa boîte noire, était le seul capable d’avoir une vue centrée utilisateur. Google vient le titiller en rendant sa qualification d’audiences de plus en plus poussée. Avec le principe d’un compte unique Google, selon certaines conditions, Google unifie et restitue le parcours utilisateur ! Alors voyons comment cela marche.

## **Comment marche le suivi multi-appareils  de Google analytics ?**

### ***Activation de la Personnalisation des annonces : condition indispensable***

RGPD oblige, Google a joué des coudes pour notifier ses nouvelles conditions d’utilisations pour les utilisateurs de compte Google. Lorsque les utilisateurs activent **la personnalisation des annonces** Google peut obtenir une vue générale de la manière dont ils interagissent avec une propriété en ligne via différents navigateurs et appareils. Par exemple, cela vous permet d'analyser la manière dont les utilisateurs parcourent les produits de votre site sur leur téléphone, puis reviennent plus tard effectuer un achat via leur tablette ou ordinateur portable.
Quand on active la personnalisation des annonces, on autorise Google de suivre toutes les activités sur  :

 	- le web et applications

 	- les appareils

 	- la géolocalisation

 	- les activités audio et vocales

 	- les vidéos et historique YouTube

[![ecoute-des-services-google-502x269.jpg](/images/blog/ecoute-des-services-google-502x269.jpg) Ecoute des services Google

Impressionnant, le volume d’informations récoltées ! Il  suffit d’aller voir dans son compte pur s’en apercevoir. Google recueille la navigation, mais pas seulement, les activités vocales, par exemple, quand vous envoyez un texto à la voix depuis un smartphone Android, le message est enregistré, comme un répondeur ! Chrome, Android, recherche, aide Google, solutions de publicités, maps, assistant vocal, applications, gmail, Google + , bref, tout quoi !

[![historique-utilisateur-google-159x300.jpg](/images/blog/historique-utilisateur-google-159x300.jpg) Historique Utilisateur Google

Grâce à ce  volume important de données générées par les utilisateurs ayant activé la personnalisation des annonces, Google peut produire des estimations sur le comportement multi-appareil de l'ensemble de votre base d'[utilisateurs](https://www.mauricelargeron.com/google-analytics-et-predictions-de-conversions/). Par défaut, les données Google relatives aux utilisateurs connectés expirent au bout de 26 mois. Vous pouvez toutefois définir le paramètre de conservation des données sur une période plus courte si vous le souhaitez. (doc de Google). Les rapports multi-appareils n'affichent que des données globales. Les données utilisateur individuelles ne sont jamais exposées.

### *Comment les données sont-elles collectées ?*

Google indique qu’analytics observe les taux de connexion et les types d'appareils pour tous les utilisateurs qui se sont logués à un compte Google et qui ont aussi réalisé une conversion. Le système sait sur quel type d'appareil l'utilisateur se connecte lors du clic initial sur l’annonce et sur quel type d'appareil associer lors de la conversion. Il collecte également les autres interactions de l’utilisateur avec le même annonceur entre le clic initial et la conversion. Un utilisateur peut avoir cliqué sur une première annonce avec un téléphone portable, et sur une deuxième annonce sur une tablette, avant de finaliser une conversion sur un ordinateur.

## **Deux visions différentes : User-Id versus Google Signals**

Concernant l’user-Id, cela fait bientôt trois ans environ que Google propose importation des identifiants anonymes provenant d’un site web ou d’un crm afin d’avoir une vue multi-devices d’utilisateurs qui se sont authentifiés de leur plein gré pour faire vite. Donc pas de données personnelles identifiables. Exemple, je suis sur un site de vente en ligne, je m’identifie sur desktop, sur mobile, l’identifiant prospect ou client existe puis poussé dans Google analytics dans une vue dite User-ID. Elle permet de visualiser que l’utilisateur en question est passé par 2 appareils avant de convertir. Notez que mise à part analytics 360, l’user-ID n’est pas multipropriété.

Pour la vision Google signals multi-appareils, c’est tout à fait autre chose. L’utilisateur qui est suivi avec son compte Google unique, va consulter un site, en utilisant les services des plateformes Google évoquées plus haut, sans aucune authentification. Google revend ici donc le potentiel pour cet utilisateur de revenir à la charge en lui présentant à nouveau une offre commercial sur ces supports d’audiences. Bref, c’est encore du remarketing quoi !

Pas évident de s’y retrouver néanmoins, car un utilisateur suivi par Google qui se logue sur le site, sera éligible à la fois pour une vue Google analytics User-Id et d’audience multi-appareils. Quid de la déduplication ?  Cette vision utilisateur est aussi disponible pour plusieurs propriétés (pas pour l’User-ID sauf version premium)

## **Comment activer ces rapports  dans Google analytics ?**

Tant que vous n’avez pas de notifications sous forme de bandeau au top de l’écran, c’est que ce n’est pas disponible. Ensuite il suffit de suivre le didacticiel pour sa mise en œuvre. Il faut cependant avoir des droits d’administration sur la propriété pour pouvoir l’activer.
Img
### ***Usages et limites des rapports multi-appareils***

*Pourquoi faire au final ces statistiques ?*

 	- Savoir le nombre d’utilisateurs au lieu du nombre d’appareils qui arrivent sur un site est toujours plus pertinent

 	- Création de rapports par sous-ensembles selon la combinaison d’appareils pour voir les chemins à valeur ajoutée

 	- Tenter après analyse des entonnoirs de conversions d’améliorer l’expérience utilisateur dans son parcours.

 	- Optimiser les investissements publicitaires selon le cheminement le plus propice à l’utilisateur.

 	- Utiliser des listes de remarketing plus pertinente avec un message plus ciblé vis-à-vis du contexte.

### ***Limites des rapports multi-appareils***

Je reprends l’aide de Google sur ce sujet, notez les « pour l’instant » , qui veut dire que cela va évoluer sous peu !

 	- BigQuery Export : Les données supplémentaires recueillies par Google Signals ne sont pas exportées vers BigQuery.

 	- Tableaux de bord : Pour l'instant, vous ne pouvez pas utiliser les données collectées par les signaux Google dans les tableaux de bord.

 	- Création de rapports personnalisés : Pour l'instant, vous ne pouvez pas utiliser les données collectées par les signaux Google dans les rapports personnalisés.

 	- Tableaux personnalisés : Pour l'instant, vous ne pouvez pas utiliser les données collectées par les signaux Google dans les tableaux personnalisés.

 	- Vues "User ID" :              Pour l'instant, vous ne pouvez pas accéder aux signaux Google dans les vues "User ID".

 	- Segments : Pour l'instant, vous ne pouvez pas appliquer de segments aux rapports multi-appareils.

 	- Traitement toutes les heures des données intra journalières   Pour l'instant, les rapports multi-appareils n'affichent pas de données intra journalières.

 	- Applications mobiles : Pour l'instant, les fonctionnalités multi-appareils ne sont pas activées pour les applications.

 	- API Reporting : Pour l'instant, vous ne pouvez pas utiliser les données collectées par les signaux Google dans l'API Reporting.

 	- Data Studio : Pour l'instant, dans Data Studio, vous ne pouvez pas utiliser les données collectées par les signaux Google.

 	- L'échantillonnage s'applique à ces rapports multi-appareils. Ces rapports sont échantillonnés au-delà de 250 000 sessions.

## **Principales lecture des rapports multi-appareils**

Bon, c’est le parent pauvre de l’article, je n’ai pas suffisamment de data là pour monter des rapports multi-appareils.  Mais pour accéder aux rapports , c’est simple néanmoins :   Vue > section Rapports>  Audience > Multi-appareil. Le type de rapports ressort sous forme d’un diagramme de Venn pour visualiser le chevauchement des appareils.

[![rapport-mutiappareils-sur-chevauchement-409x300.jpg](/images/blog/rapport-mutiappareils-sur-chevauchement-409x300.jpg) Rapport muti-appareils sur chevauchement

Un détail sur le parcours ensuite multi-devices est donné relié à des données d’engagement (temps des visites), de conversions (objectifs).

[![canaux-multiappareils-313x300.jpg](/images/blog/canaux-multiappareils-313x300.jpg) Rapports Canaux multi-appareils
### *Conseils d’interprétation Google*

*« Lorsque vous activez les signaux Google, au départ aucun historique de campagne n'est associé aux utilisateurs Google qui ont activé la personnalisation des annonces. S'il s'agit d'utilisateurs connus, le trafic qui leur est associé est d'abord répertorié dans la catégorie "accès directs". Analytics commence à collecter des historiques de campagne pour ces utilisateurs dès leur première visite après activation des signaux Google. Ainsi, au bout de quelque temps, les chiffres affichés dans les rapports Canaux correspondent. *

*« Dans les rapports multi-appareils, les utilisateurs Google qui ont activé la personnalisation des annonces sont considérés comme étant de nouveaux utilisateurs la première fois qu'ils ouvrent une session sur une propriété après l'activation des signaux Google, même s'ils ont déjà ouvert des sessions sur cette propriété dans le passé.»*

Donc on le voit bien, Google pousse dans ses retranchements son rival Facebook, maintenant reste à voir dans le temps l’intérêt de ces nouvelles statistiques, sans cesse plus poussées, plus intrusives diront certains. Mais appréhender la complexité du monde numérique passe sans doute par ce genre d’outil ?
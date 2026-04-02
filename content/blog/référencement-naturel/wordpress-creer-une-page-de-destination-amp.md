---
title: "Wordpress : créer une page de destination AMP"
date: 2018-04-23
author: "admin"
categories: ["Référencement naturel"]
tags: []
slug: "wordpress-creer-une-page-de-destination-amp"
---

Quoi de plus logique de pousser à **construire des pages [AMP pour ses pages de destination](https://wordpress.org/plugins/accelerated-mobile-pages/)**, quand on sait que l’une des composantes du score de qualité est le temps de chargement de la landing page ? Sinon de bonnes raisons aussi viennent soutenir un projet de créer des pages plus rapides pour mobiles quand on prend connaissances des résultats d’une étude d’Akamaï :

 	- Un retard de** 100 millisecondes** dans le chargement du site Web peut nuire à 7% des taux de conversion

 	- Un** délai de deux secondes** dans le chargement de la page Web augmente les taux de rebond de 103%

 	- **53% des visiteurs du site mobile quittent une page** dont le chargement prend plus de trois secondes

 	- Les **taux de rebond** étaient les plus élevés pour les acheteurs de téléphones mobiles, tandis que les consommateurs de tablettes avaient le taux de rebond le plus bas.

[![google-amp-ads-landing-pages-sequence-502x262.png](/images/blog/google-amp-ads-landing-pages-sequence-502x262.png) temps de chargement AMP

Que faut-il comme outils pour créer sa landing depuis le CMS WordPress ?
## **Eléments pour créer sa page de destination sous format AMP**

Plaçons-nous ici dans le cadre d’une page qui va accueillir un formulaire. Le principal objet critique à coder pour créer ce type de page, c’est justement **le formulaire** ! L’annonceur non codeur va se heurter à un os s’il utilise simplement le plugin AMP de WordPress, les champs du dit formulaire ne seront pas pris en compte, que ce soit dans des articles ou pages dédiées à la collection de leads.
Comment faire alors ?

Soit on fait appel à un Dev, soit on s’inspire d’[exemples du projet amproject.org ](https://ampbyexample.com/) mais là encore il faudra un peu s’y connaître, ou alors, comme le plus souvent, on fait usage d’un plugin.  J’ai choisi un Template freemium dont le socle de base est gratuit et les extensions payantes comme celui que je vais utiliser pour l’occasion soit contact form7 pour AMP. Donc pour aller au bout de notre projet il faudra 4 éléments :
*Briques à ajouter *

 	- Contact form7

 	- [AMP for WP Accelerated Mobile pages](https://ampforwp.com/) d’Ahmed Kaludi, Mohammed Kaludi

 	- Extension Amp-CF7 : extension de formulaire qui fonctionne tout seul  (je veux dire sans le plugin AMP for WP)

 	- Contact Form 7 – Success Page Redirects (celle incluse native ne fonctionne pas)

*Informations contextuelles *

 	- Thème : attention à son incompatibilité dans le codage des CSS (prévoir de désactiver éventuellement certaines fonctions), ici j’ai utilisé le thème « extra » d’eleganthemes.

 	- Gestion du cache : le plugin devra pouvoir lui aussi être désactivable sur la landing page (minification html, css, js)

 	- 1 landing de disponible !

## **Mise en œuvre de la landing Amp**

Les concepteurs ont prévu toutes les intégrations possibles dans l'interface du Plugin :

 	- **Paramétrages** : Monétisation (ajout inventaire format pub), Seo (Yoast), Performance (Minification), Analytics (Google mais pas que..), Rich snippets, Notifications (politique des cookies), Push infos, Formulaire de contact, Commentaires (disqus, Facebook), CTA mode Dev., exclusion (choix de contenus parmi les catégories), traduction

 	- **Design :** possibilité de jouer avec les CSS personnalisés, les entêtes, footer, boutons sociaux, thèmes préfabriqués

 	- **Extensions **: en plus de celle du formulaire, CTA, woo commerce, avis.

Vraiment bluffant comme c’est simple !

[![wizard-394x300.jpg](/images/blog/wizard-394x300.jpg) Wizard de mise en oeuvre amp

 	- Installer et Activer le plugin pour avoir une version AMP des pages, articles, catégories, page accueil.

 	- Touches de personnalisation depuis l'interface :

 	- Certains Css depuis l'interface du plugin mais rien de méchant

 	- Faire un rappel sur le template-amp

[![plugin-amp-pour-wordpress-310x180.jpg](/images/blog/plugin-amp-pour-wordpress-310x180.jpg) Interface Plugin Amp

## **Qu’est-ce que cela donne au final ?**

### ***Aperçu du résultat***

Ok rien d’extraordinaire dans le rendu ici, je n’ai fait que copier-coller la [version non AMP](https://www.mauricelargeron.com/comment-mesurer-les-pages-amp-pour-mobiles/).

[![page-de-destination-189x300.jpg](/images/blog/page-de-destination-189x300.jpg) Page de destination normale

[![amp-adwords-optimize.gif](/images/blog/amp-adwords-optimize.gif) Amp adwords optimize

J’ai vérifié dans l’outil de test, bon cela semble correct.
### ***Consultez cette Démonstration de pages AMP***

Bon, je n’indique pas ici ma landing, il y a encore des améliorations à faire ! Sinon pour ceux qui veulent avoir une idée entre le format classique et le format AMP à l’échelle d’un site voici une démo. : [https://demo.weeblrpress.com/amp/](https://demo.weeblrpress.com/amp/)

Bon est-ce que le fait de mettre en production ce type de landing fera gagner quelques centimes en cpc en compensation du soulagement des Datacenter de Google ?
J’attends avec impatience un benchmark sur le sujet
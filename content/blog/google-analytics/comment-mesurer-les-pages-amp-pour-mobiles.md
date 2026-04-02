---
title: "Mesurer les pages AMP dans Google analytics"
date: 2016-12-26
author: "admin"
categories: ["Google Analytics"]
tags: []
slug: "comment-mesurer-les-pages-amp-pour-mobiles"
image: "/images/blog/amp-wordpress-et-google-ana.jpg"
---

Un post rapide pour la trêve bien méritée des confiseurs euh… référenceurs ! Pour ceux qui auraient basculé sur le standard des pages rapides pour appareils mobiles, dit AMP (accelerated mobile page), il s’agit maintenant, une fois la technologie implantée, de mesurer le  trafic sur ce genre de page sur Google analytics. Passons en revue les différentes solutions, trois par exemple !

## **Rappel pour installer AMP sur son site web**

Allez pour les non développeurs, faites confiance à la maison **automaticc,** vous savez, celle qui édite le **cms WordPress** et qui déploie la plateforme wordpress.com *(modèle payant de WP pour monter son site en 2 clics)* et le programme open source wordpress.org *(téléchargement libre du code source, à installer sur un serveur web)*. Cette belle boîte a  développé un plugin simplissime à installer et à configurer.

[![automaticc-310x135.jpg](/images/blog/automaticc-310x135.jpg) Plugins pour rendre ses pages AMP

Une fois installé,  il suffit pour avoir un aperçu, de rajouter /AMP/ à la fin de toutes les urls du site afin de voir ce que cela donne et de débuguer en rajoutant à la fin de l'url :** #developement=1**

[![console-js-et-debugguage-247x300.jpg](/images/blog/console-js-et-debugguage-247x300.jpg) Vérification et débueugage dans la console JS
## **Mesurer les pages AMP dans Google analytics**

### ***Ce qu’il ne faut pas faire pour les amp***

[![modifier-amp-fichier-automaticc-310x159.jpg](/images/blog/modifier-amp-fichier-automaticc-310x159.jpg) Insérer le script directement dans le template amp du plugin

Rajouter le script de Google analytics dans un des fichiers du plugin AMP de base. Google analytics va fonctionner, mais Google va se fâcher et n’imprimera pas vos pages AMP. Une notification se verra dans la search console de toute façon

[![amp-search-console-google-310x173.jpg](/images/blog/amp-search-console-google-310x173.jpg) Google search console indique un problème critique
### ***Insérer le bon hack sur le Template pour Google analytics***

On hack le code du Template de WordPress, en intégrant dans le fichier function.php, un objet json le seul acceptable par AMP, qui pose le marqueur Google analytics. Bon c’est une solution plutôt technique, mais qui fonctionne. Merci à la développeuse isabel pour ce travail et partage.

/**

* Add the AMP analytics script to head of AMP pages

*/

function isa_amp_scripts( $data ) {

$data = 'https://cdn.ampproject.org/v0/amp-analytics-0.1.js';

return $data;

}

add_filter( 'amp_post_template_data', 'isa_amp_scripts' );

/**

* Add AMP-analytics to the AMP post Template footer

*/

function isa_amp_analytics( $amp_template ) {

?>

{

"vars": {

"account": "UA-xxxxxx-xx"

},

"triggers": {

"trackPageview": {

"on": "visible",

"request": "pageview"

}

}

}

**Google tag manager pour les pages AMP pour WordPress**

Alors là j’avoue, j’ai envoyé une missive avec Thomas « DuracellTomi », développeur du plugin GTM pour WordPress. Il m’a indiqué ne pas avoir eu le temps encore de développer le script qui va bien pour le gestionnaire de balises, mais m’indique que si je trouve des choses intéressantes, je lui en fais part. Eh bien rien du tout pour l’instant. Donc, il faut patienter !

Sinon, en dehors de WordPress, l’article de référence est celui de Simo Ahova, comme d’habitude, qui s’est lâché  sur un tutoriel sur le container AMP dédié dans GTM.
Img AMP gtm
## **Liens utiles  pour les pages AMP**

 	- 1 Hack Template WordPress pour AMP : [https://goo.gl/5uPFuT](https://goo.gl/5uPFuT)

 	- Explication Code AMP pour  GTM : [https://goo.gl/ytt9Gd](https://goo.gl/ytt9Gd)

 	- Plugin WP pour mesurer audience AMP pour GAnalytics : [https://goo.gl/0Qy5AS](https://goo.gl/0Qy5AS)
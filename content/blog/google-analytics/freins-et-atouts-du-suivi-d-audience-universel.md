---
title: "Google classique ou Google Analytics version Universelle ?"
date: 2013-06-19
author: "admin"
categories: ["Google Analytics"]
tags: []
slug: "freins-et-atouts-du-suivi-d-audience-universel"
---

Faut-il passer à  Google  analytics universel ? Quelle  est l'utilité de migrer un compte « classique »  Google analytics  (GA) vers **Universal Analytics** (GUA) ? , ou, lors d’une nouvelle implémentation d’un suivi d’audience, vers quelle  solution s’orienter (premiers paramétrages ici) ? Je n’ai  pas la réponse, mais des éléments qui peuvent aider à prendre une décision, au cas par cas.  Voyons ce qui des points communs, des différences, et des atouts et perspectives du nouveau code universel, peut faire pencher la balance vers un changement.

[![Image](/images/blog/CHOIX-GA-310x205.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2013/06/CHOIX-GA.jpg) Quelle option choisir ?
## **Classique or Not Classique ?**

*Code classique GA et Universal : le même socle de base*

Les 2 codes collectent par défaut les mêmes indicateurs et donnent donc le **même reporting dans l’interface GA (pour l'instant)**, dont l’audience  (les Visiteurs, Nombre de visites, Pages vues), les sources de trafic (directe, référents, moteurs, campagnes, réseaux sociaux), le contenu (pages vues, vitesse du site, analyse de page), tableau de bords, raccourcis, évènements d’alertes et personnalisation compris.

[![Image](/images/blog/code-suivi-310x150.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2013/06/code-suivi.jpg) Seules diffrences visibles dans interface GA

Mêmes interfaces depuis l’admin.  comme la configuration d’évènements via l’onglet « objectifs ». Les paramètres du site, des réseaux sociaux, le remarketing ou les définitions personnalisées. La comparaison s’arrête là ! Ensuite tout diffère..

### **Code de suivi : le grand changement**

La syntaxe JavaScript à insérer dans les pages du site n’est plus du tout la même ! Soit, mais cela veut dire quoi concrètement ? Eh bien, que tout le reste des configurations doivent  suivre cette nouvelle « librairie »  ou vient piocher le nouveau script « **analytics.js** ».

Dans le cadre d’une migration vers ce nouveau suivi, pour un usage avancé,  il faudra donc reconfigurer :

	- Suite de pages personnalisées

	- Evènements (téléchargements, clics..)

	- Tracking e-commerce (panier)

	- Interactions sociales (boutons sociaux)

	- Variables personnalisées (pages, session, visiteur)

	- Suivi multi-domaines

### **Items  du nouveau code de  suivi d’analyse**

Donc, dans le cas d’une migration, prévoir à l’avance du temps pour appréhender la nouvelle librairie. Voici, présenté sous une forme agréable, les principales portions de codes à connaître. Je remercie son auteur, mais j’ai zappé la source (autant pour moi, je corrigerais si je la retrouve).

[![Image](/images/blog/universal-shett-guide-310x219.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2013/06/universal-shett-guide.jpg) [outil de synthèse de GUA](https://docs.google.com/spreadsheet/ccc?key=0ApP4sgBxVMsrdGcyMmtKMURncl8zUXBqZThPUk9WN3c&usp=sharing)

Pour ceux qui souhaitent aller plus loin dans la possibilité de développement il y a cette ressource qui rentre un peu plus dans le [détail](http://www.thyngster.com/2012/12/17/google-analytics-measurement-protocol-cheat-sheet/) des items.

[![Image](/images/blog/universal-shett-guide-2-268x300.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2013/06/universal-shett-guide-2.jpg) Grille Détaillé Code analytics.js
## **Quelles sont les bonnes raisons de basculer vers la nouvelle version alors ?**

### **L’universalité**

Choisissons 1 bonne raison, c’est sa possibilité de tracking universel bien sûr ! Pouvoir suivre un utilisateur au travers de ces usages de plateformes (côté client avec le  userId pas encore disponible) : smartphone, tablette, pc. La nouvelle librairie Javascript (UA) permet de suivre cela.

[![Image](/images/blog/protocole-client-uid-0-310x162.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2013/06/protocole-client-uid-0.jpg) Prococole de mesure : un des atouts de GUA

Elle permet une analyse visiteur et multicanal  plus proche de la réalité où le online rencontre le offline.

[![Image](/images/blog/protocole-client-uid-310x194.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2013/06/protocole-client-uid.jpg) Un suivi concret visiteur avec UserId

L’intégration des **données externes  vers Google analytics** (côté serveur) est l’atout complémentaire qui s’effectue grâce au Protocol multiplateforme de mesure (MP).  Au-delà des Smartphones, pc, tablettes, il devient possible d’envoyer depuis des crm, caisses, imprimés (coupons), d’une cafetière.. des données à GA qui sont agrégées ensuite par visiteur. Un exemple dans le cas d'un suivi d'acquisition de prospects (leads).

[![Image](/images/blog/schema-310x176.jpg)](https://www.mauricelargeron.com/wp-content/uploads/2013/06/schema.jpg) Suivi GUA avec Client ID
### **Un exemple amusant qui vous vient d'Australie !**

Une illustration du tracking à base de puce Rfid paramétrée par  utilisateur et connecté à  l'accès à la cafetière, frigo qui est poussé vers les Google analytics universel grâce au protocole de mesure. Bon , c'est en anglais, mais cela est intéressant !

http://youtu.be/C27yMQOS8n0

### **Des variables et des statistiques créées sur mesure **

Une autre raison est la possibilité de **personnaliser des statistiques**  *( représentent des Nombres : visiteurs, Taux de rebond, Durée sur le site en  moyenne  en colonne dans les rapports)*  et des variables  *(qualifie une entité : Nouveau/ancien visiteur, genre masculin/féminin en ligne , Durée d'une visite ...dans le reporting c'est présenté en ligne )* en plus grand nombre (20 au lieu de 5) dans GA afin d’affiner les rapports et segmentations. Sur ce sujet, pour faire la différence, cette page est bien utile.

### **Autres petits avantages**

Une intégration plus facile depuis l’admin, des durées de sessions et de campagne, de l’adjonction de référents perso. d’exclusion de sites / termes de recherche.

Last but not least, l’analtyics.js ne dépose qu’un seul cookie par défaut (au lieu de 4 auparavant) ce qui rendrait l’exécution du code plus rapide et performant. De  plus les sous domaines sont trackés sans adjonction de code supplémentaire.

### **Et les inconvénients ...pour résumer**

	- Déploiements de l'UserId à venir

	- Reparamétrages des fonctionnalités avancées à refaire

	- Mise à jour chez certaines plateformes Cms pas accomplie

	- Rapports "Multi-devices" pas encore intégré.

## Alors on change  ?

Pour ceux qui partent de zéro, sans connaitre trop l’univers du tracking GA, dans un premier temps, le mieux est de rester sur l’ancienne version, les ressources d’aide sont plus nombreuses. **Pour ceux qui hésitent**, le mieux est d’installer en parallèle les 2 codes (ralentira la page, comme d’hab.) mais sur 2 UA-----1/2 distinctes cela permettra de se hâter lentement. Pour les développeurs, le choix est vite fait ! Pour ceux dont la décision est le modèle économique,  avec  par exemple, les ecommercants  retailers,  ils  y verront une belle opportunité pour mesurer de manière plus adéquate leurs efforts sur les différents **canaux marketing**.
 Plus d'infos : [https://support.google.com/analytics/answer/2817075](https://support.google.com/analytics/answer/2817075)
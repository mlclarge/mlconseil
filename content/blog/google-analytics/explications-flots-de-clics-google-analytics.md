---
title: "Du sens aux données du web "
date: 2011-09-16
author: "admin"
categories: ["Google Analytics"]
tags: []
slug: "explications-flots-de-clics-google-analytics"
---

Ces données sont indubitablement des chiffres, encore des chiffres issus  de tracking qu’effectuent des codes javascript, cookies et autres logs, peuplent nos interfaces de communication (mobile, tablettes, ordinateurs, serveurs) mais aussi proviennent aussi d’enquêtes, de tests (panels), de logiques internes d’une organisation (entreprises) quant à sa façon de suivre l’évolution d’actions, on retrouvera ici les objectifs, actions, cibles, conversions, kpi, et autres segments… Ces données s’accumulent, et enflent les Datacenter de la  planète, mais quel sens donner à cette accumulation numérique ?

Les fournisseurs de data filtrent ces flux numériques par des algorithmes savants. Dans notre quotidien, les données s’accumulent souvent dans nos comptes sous forme de tableaux dont les entêtes de colonnes ne cessent de s’étoffer.

Mais quel sens peut-on apporter à ces données ? Comment les transformer en véritable informations ?

Pour y répondre, je prendrai le cas d’un compte Google analytics.  Dans un premiers temps,  un petit glossaire de définitions  sera proposé  afin de savoir ce dont on parle. Dans un second temps, je partagerai une « grille de lecture » pour mieux comprendre ces données issues de GA (Google analytics). La notion de contexte des données, terminera cet article car des chiffres ne veulent rien dire tant qu’on ne les replace pas dans un certain paysage pour donner du contraste et faire émerger des actions (techniques, marketing..).
## **Petit glossaire de ****définitions des  données : indicateurs,valeurs, **et usages (segmentation, rapports)

### ->  **Indicateurs GA (Google Analytics)**

*Objectifs (goals) :*Un objectif est une page Web à laquelle l’internaute accède après avoir effectué un achat ou une autre action, telle qu’une inscription ou un téléchargement , dixit Google.  Exemple : Temps passé sur le site

*Quotient :* résultat d’une division (bon, facile..)

*Ratio :* outil de comparaison issu d’un quotient dont le résultat reflète une valeur plus ou moins performante.* *Les **ratios** servent à mesurer la rentabilité, la structure des coûts, la productivité, la solvabilité, la liquidité, l’équilibre financier, etc*. (source wikipedia)*

*Mesure : *Une mesure est un nombre (une somme) ou un quotient, exemple : nombre de visites, taux de conversion (kpi)

*KPI : *indicateurs clés de performance, est une mesure qui sert à suivre les objectifs que l’on s’est fixé. *Exemple :* Chiffre d’affaire moyen par visiteur, taux de conversion (c’est aussi une mesure !)

*Cible :* C’est une valeur fixée à un critère pour représenter le succès ou valeur du KPI.

*Dimensions (ou critères) : *C’est ce qui caractérise un visiteur, par exemple, l’origine géographique du visiteur, la version de son navigateur. Cela peut être aussi un des aspects du trafic entrant sur le site, sa source, sa provenance (chemin).

*Statistiques (ou metrics) : *Elles mesurent l’interaction entre les visiteurs et le site web. Cela peut être le % de nouvelles visites, …Les stats sont des chiffres qui comptent quelque chose. Elles peuvent être unique, segmentées ou agrégées.

*Valeurs personnalisées :* A des fins de segmentations, il est possible de personnalisées ses remontées d’informations par visiteur (par exemple le sexe lors d’un remplissage de formulaire), par session utilisateur, ou par page.

Important !: certaines combinaisons ne pas acceptées dans l’interface de Google ANALYTICS il faut mieux se référer sur les choix possibles ici :Article Google sur les possibilités de combiner critères et statistiques.
### -> **Valeurs**

Elles sont fournies sous forme de moyennes, de pourcentages, taux (%) ou autres quotients (ratios), de mesures composites (mesures faîtes à partir d’autres mesures).
### -> Usages

Un petit rappel sur l’interface de GA – Version 5 avant de parler des usages faits à partir de ces données.

L’interface de Google analytics propose 4 onglets (ou boutons situés dans barre horizontale haut de page) :

	- Tableaux de bord (les statistiques principales)

	- Mon site (5 catégories de rapports : visiteurs, publicité, source trafic, contenu, conversion) + alertes

	- Mes conversions (objectifs, commerce électronique, entonnoirs multicanaux)

	- Rapports personnalisés (croisements des statistiques (bleues) et des critères (verts)

*Profil :*

Un profil permet d’afficher les données d’un site web. Pour chaque site, un profil maitre qui ne filtre rien doit être implémenté  (sorte de sauvegarde), puis un profil secondaire qui lui pourra filtrer les données que vous souhaitez voir apparaître (exemple de filtre : l’adresse ip de votre connexion, comme cela, les visite sur vote site ne sont pas comptées !).

Important ! : ne pas confondre filtres et segments, les filtres sont permanents et destructeurs de données en amont (utile pour des tris permanents, pour gérer des accès utilisateurs..), les segments sont modifiables à souhaits et ne modifient pas la source de données et sont manipulables dans instantanément (historiques possibles, comparaisons..).

*Segmentation :*

Utilisation de valeurs personnalisées, de  dimensions afin de produire des rapports mesurés. Exemple : le temps passé par visiteur supérieur à 2 minutes, les visiteurs qui viennent depuis le site de picasa, les internautes qui utilisent un téléphone mobile.

**Grille de lecture : l’exemple des données relatives au « Contenu » consulté par le visiteur.**

Dans le tableau ci-dessous, je donne pour** chaque intitulé de donnée** :

	- Son étendue *(unique, segmentée ou agrégée)*

	- Sa nature : nombre, quotient (tx), libellé (texte)

	- Sa mesure : statistique (metrics) ou  critère (dimension)

	- Combinaison (possibilité entre Stat. et Critères)

	- Kpi : Pas systématique, notamment ici, 1 seul est souligné !

	- Pertinence technique ou marketing (finalité)

[![Image](/images/blog/tableauDonnees-300x222.png)](https://www.mauricelargeron.com/wp-content/uploads/2011/09/tableauDonnees.png)
Carte d'identité des données de google analytics
Ce tableau peut être étendu aux autres catégories de données de GA et notamment à celle(s)

	- de visiteurs

	- Publicité

	- E-commerce

Les kpi, indicateurs clés de performance sont souvent présents sur les catégories mentionnées ci-dessus ! En effet, les équipes marketing et de management y attachent de l’importance car on touche ici aux données pécuniaires !

Mais comment données du** sens à ces indicateurs** ? Le contexte, encore le **contexte**, est le moyen d’apporter de la couleur à ces mesures pour les transformer en réelle information utile au pilotage de l’entreprise.
## Le contexte ou comment donner de la couleur aux données

	- **Croiser une statistique avec critère de contenu**

Dans un tableau de bord, la statistique froide du nombre de visites ne dit pas grand-chose, en revanche, corrélée à un critère, donne du recul. Ici, le nombre de visites ventilées par le chemin (Uri) des pages d’entrée sur le site. La page d’accueil est ici mise à l’honneur, mais ce n’est pas toujours le cas…
[![Image](/images/blog/contexteSegment-257x300.png)](https://www.mauricelargeron.com/wp-content/uploads/2011/09/contexteSegment.png)
Recherche des entrées visiteurs sur un site.

	- **Comparer par période de temps**

[![Image](/images/blog/contextTemps-300x113.png)](https://www.mauricelargeron.com/wp-content/uploads/2011/09/contextTemps.png)
Comparatif de 2 saisons.
Au lieu de se focaliser sur le moment présent, il peut être utile de comparer des données dans le temps, d’une période à l’autre, ici fin d’année vs début d’année.

	- **Pourcentages et moyennes : même combat ?**

**[![Image](/images/blog/contexteMoyennes-300x147.png)](https://www.mauricelargeron.com/wp-content/uploads/2011/09/contexteMoyennes.png)**
****Recherche sur l'impact d'un critère
Ici, on veut souligner l’impact des réseaux sociaux. Ils ne représentent que 2% du trafic. Ce trafic visiteur passe moins de la moitié du temps par rapport au reste de la fréquentation du site.

	- **Chercher la perle « rare » : Source de trafic et indicateur clé**

Impact d'un site référent.
Ici, un site d’information, donc l’analyse ici porte sur le critère « temps passé » et la statistique « taux de rebond »  (abandon du site dès la 1ere page).

Une recherche est effectuée sur les sites référents , parmi lesquels 1 site à forte notoriété, qui représente peu cependant (donc pas représentatif, à approfondir donc), mais qui amène une audience de qualité avec un taux de rebond de 44% (25% inférieur à la moyenne du site) et temps passé supérieur de quasiment 1 minute par rapport à l’ensemble des visiteurs. Faut-il creuser cette ressource (essayer d’améliorer sa stratégie de liens) ?

	- **Mettre en parallèle les opérations du marketing online et offline lors de reporting.**

[![Image](/images/blog/contexteOpexternes-300x152.png)](https://www.mauricelargeron.com/wp-content/uploads/2011/09/contexteOpexternes.png)
Impact des opérations marketing offline.
Cela permet aussi de corréler les opérations multicanaux et d’apporter du sens à l’analyse de l’audience.
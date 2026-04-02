---
title: "Analyse multicanal dans Google Analytics"
date: 2012-01-18
author: "admin"
categories: ["Google Analytics"]
tags: []
slug: "guide-entonnoirs-multicanaux"
---

Après avoir parlé des interactions sociales sur un site web, intéressons-nous  aujourd’hui  à la façon dont un  internaute chemine pour atteindre un objectif précis sur un site web. Dans le jargon des marqueteurs, un objectif atteint s’appelle "**conversion**".  Exemple : je possède un site d’édition d’ouvrages (livresecolo.com) sur l’écologie et lance une campagne pour faire connaître un dernier titre, je propose un téléchargement gratuit d’un chapitre  et souhaite connaître par quels  chemins   sont passés les internautes qui ont téléchargé ce  fichier . Ces chemins plus communément appelés « canaux » pour les professionnels du marketing,  font l'objet d'une des fonctionnalités de l’outil gratuit Google analytics.  Il est en effet pertinent  d'un point de vue marketing de connaître  ces différents canaux liés à l'atteinte d'une cible finale (conversion, objectif) afin de mieux comprendre le comportement d'un visiteur.

[![Image](https://www.mauricelargeron.com/wp-content/uploads/2012/01/entonnoirs-multicanaux-300x194.png)](https://www.mauricelargeron.com/wp-content/uploads/2012/01/entonnoirs-multicanaux.png)
## **Vous avez dit Canal ?**

Alors ici on ne parlera que de canaux « online », ceux qui existent sur la toile, on peut en dénombrer 7, le tableau ci-dessous  les décrit. Les expressions (ou variables)  entre guillemets sont importantes car ce sont elles qui vont marquer ou « tagguer » les urls.

[![Image](https://www.mauricelargeron.com/wp-content/uploads/2012/01/entonnoirGA-300x167.png)](https://www.mauricelargeron.com/wp-content/uploads/2012/01/entonnoirGA.png)

Pour distinguer donc un canal de son voisin, il faut attribuer une **url spécifique** qui sera suivi par Google, afin de dire au final,  cet internaute, avant d’aller télécharger mon document, il a vu ma publicité (1er canal) , puis à fait une recherche parmi les liens « naturels » (2eme  canal) et enfin, à décider de son action de téléchargement en se rendant directement sur mon site  (3eme et dernier  canal). Ces urls sont des  liens hypertextes qui servent à passer d’une page à une autre, d’un document à un autre. Par exemple, on peut utiliser cet outil, disponible [ici](http://www.roirevolution.com/google-analytics/google-analytics-url-builder.php), pour marquer ces urls, ce qui donnera :

[![Image](https://www.mauricelargeron.com/wp-content/uploads/2012/01/creeation-urls-300x217.png)](https://www.mauricelargeron.com/wp-content/uploads/2012/01/creeation-urls.png)
### **Vous avez dit conversion ?**

Une fois le **tagguage** effectué,  il convient d’organiser le suivi du visiteur sur l’objectif fixé lors de sa venue sur le site. Le mot de conversion (ou objectif)  est souvent associé au terme e-commerce,  de vente en ligne. Mais une conversion  peut être aussi une page vue, un formulaire rempli, le visionnage d’une vidéo, un document téléchargé (dans notre exemple ici) .  Cette action sera enregistrée  soit par le clic de souris, soit par la redirection vers une page de téléchargement spécifique.  Ces intéractions  sont trackées par un code de suivi dédié et inséré une fois pour toute sur le site.

[![Image](https://www.mauricelargeron.com/wp-content/uploads/2012/01/codepage-300x36.png)](https://www.mauricelargeron.com/wp-content/uploads/2012/01/codepage.png)

Donc le schéma  de codage d’ensemble peut ressembler à ceci :

[![Image](https://www.mauricelargeron.com/wp-content/uploads/2012/01/schema-global-entonnoir-300x79.png)](https://www.mauricelargeron.com/wp-content/uploads/2012/01/schema-global-entonnoir.png)
**Analyse des données  et l'entonnoir multicanaux **

Ces paramétrages de suivi de canaux et d’évènements accomplis, la lecture des rapports se fait dans Google analytics dans la catégorie conversion.

[![Image](https://www.mauricelargeron.com/wp-content/uploads/2012/01/ga--300x206.png)](https://www.mauricelargeron.com/wp-content/uploads/2012/01/ga-.png)

Puis ensuite on a accès à ce genre d'illustration ..

[![Image](https://www.mauricelargeron.com/wp-content/uploads/2012/01/EntonnoirMulticanaux0cheminGroupe1-300x104.png)](https://www.mauricelargeron.com/wp-content/uploads/2012/01/EntonnoirMulticanaux0cheminGroupe1.png)

Sans rentrer dans les détails, Google remonte les données jusqu’à 30 jours en arrière, décalées de 48 heures maximum. Il faut au moins 1 conversion, sinon aucun schéma n’est produit. Des analyses plus fines démontrent sur l’ensemble  des conversions les types de chemins de l’internaute, ceux qui possèdent 1, 2, 3 etc..canaux différents. La durée avec laquelle les conversions ont été atteintes. Pour plus d’informations : [http://support.google.com/analytics/bin/answer.py?hl=fr&answer=1319312#](http://support.google.com/analytics/bin/answer.py?hl=fr&answer=1319312) et livre sur la [dernière version de Google analytics](http://www.amazon.fr/Google-Analytics-Analysez-am%C3%A9liorer-performances/dp/274607057X/ref=sr_1_1?s=books&ie=UTF8&qid=1326957301&sr=1-1) de Ronan Chardonneau.
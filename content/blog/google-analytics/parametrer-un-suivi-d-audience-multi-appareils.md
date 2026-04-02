---
title: "Essayer de suivre le visiteur multi-écrans"
date: 2014-10-13
author: "admin"
categories: ["Google Analytics"]
tags: []
slug: "parametrer-un-suivi-d-audience-multi-appareils"
---

Parlons multi-écrans cette semaine avec cette récente fonctionnalité **User-Id** [**Google analytics** ](https://www.mauricelargeron.com/tutoriaux-liens-pour-comprendre-le-gestionnaire-de-balises/)qui vient s’intégrer dans le nouveau suivi universel d’audience de site web. J’avais pu déjà en parler mais sans y consacrer du temps. Donc prenons quelques minutes aujourd’hui pour rentrer un peu plus dans les détails d’une intégration lambda sur un prestashop à titre de laboratoire d’essai. Le **marqueur USER ID** permet de recueillir **l'  itinéraire multi-écrans ** du visiteur jusqu'à la conversion. Est-ce vraiment utile ce mode de tracking ? En tous cas c’est une donnée d’actualité !  Les porteurs de smartphones   sont forcément des internautes multi-devices dont le CA développé s’avèrerait  plus élevé que celui des acheteurs  "mono-appareil" (bizarre ce jargon :s ), intéressant pour les e-commerçants non ?

[![1crossdevices-310x173.jpg](/images/blog/1crossdevices-310x173.jpg) Intérêt du suivi Cross Devices
## UserId porte drapeau de  l’universalité  !

### **Concept**

C’est vraiment le cas de le dire ici, l’universalité gagne ses galons par ce protocole de mesure.  J'ai demandé à mon développeur préféré de m'installer donc un mode de tracking qui prendra comme base, l'id de la table de prestashop comme userId, simple ! Un petit croquis explique que cette variable peut être transversale à n'importe quelle application : Crm,  PS, Wpress...

[![2-310x173.jpg](/images/blog/2-310x173.jpg) Concept de l'userId
### **Mis en place dans G Analytics**

Dans GA, rien de plus simple que d’activé une vue UserId, il suffit  d’aller sur l’admin. Puis propriété, User-Id. Ga propose une syntaxe standard pour créer le tracker

[![implementation-userId-1-310x179.jpg](/images/blog/implementation-userId-1-310x179.jpg) implementation userId dans GA
## Précisions Techniques de mise en place  (enfin pas trop non plus !) 

L’intégration malheureusement ne se fait pas par simple copier coller. Le **developpement pour une intégration d’un script GA** ou autre  nécessite ne s’intégrer à l’écosystème de l’application web, ici prestashop. Le developpeur ici, devra manipuler le php et la programmation orientée objet et créer un module.  Plus de 2400 modules existent à ce jour ! Cette intégration se fera donc via un plugin (autre nom pour module) ,   qui va se connecter au  système d’architecture de  PS, par extensions de ce dernier via la création de classes,  objets et fonctions php.  Le plugin joue le rôle donc d’interface entre l’écosystème PS et l’extérieur  comme pour le cas qui nous intéresse, le marqueur Javascript de  GA pour l’userID .

Voici pour matérialiser ces propos , voici un petit extrait de l’intégration du code GA au sein d’une classe Php qui va pousser la donnée pour GA , bon cela ne veut pas dire grand-chose sans contexte , c’est juste pour **matérialiser  la collecte de l’userId**.  Remarquez l’encapsulation du code de tracking JS dans le php.

[![integration-code-userId-270x300.jpg](/images/blog/integration-code-userId-270x300.jpg) Extrait du module d'intégration du script GA

**Machinerie  :** A chaque session, si le visiteur se logue, le tracking se met en place ,  les mises au panier sont conservées bien sûr, mais l’intérêt surtout, est  que cet userId va servir de support pour suivre les différentes visites effectuées par une tablette, un pc ou un smartphone. Dans Firefox on peut controler que le script fait bien son travail en examinant sous l'onglet "Dom" l'objet ga et la collecte de l'userId

[![verif-navigateur-310x64.jpg](/images/blog/verif-navigateur-310x64.jpg) Dans FireFox vue de la variable

**Résultat ?** On peut obtenir ce genre de rapport dans Audience -> Multi-appareils

Ici pour l'illustration, les 2 conversions ont pour origine 3 devices sur 2 acheteurs  (desktop, mobile et tablettes) .

[![utillisation-3-devices-pour-la-conversions-310x229.jpg](/images/blog/utillisation-3-devices-pour-la-conversions-310x229.jpg) Conversions de 2 acheteurs utilisant 3 devices                  (desktop, tablette, mobile)
## **UserId et ses spécifications**

**Récapitulatif de ce qu'il faut savoir**

	- **Applications mobiles via leur SDK** peuvent embarquer un user-id  tout comme les sites web mais ils ne discuteront pas entre eux !

	- UserId n'est pas attribué par Google Analytics (doit venir du Système propre de l'annonceur) et ne doit pas communiquer de données personnelles identifiables. Si l'internaute ne souhaite pas avoir ses données remontées vers les serveurs de Google Analytics, il peut installer un plugin qui bloquera le marquage : [https://support.google.com/chrome/answer/142064](https://support.google.com/chrome/answer/142064)

	- Aucune rétroactivité bien sûr de la collecte.

	- **Pas d'association possible d'une Vue UserId avec une autre propriété** (le compte premium permet lui non pas la fusion mais le rapprochement de plusieurs propriétés.

	- **Unificateur de session** : permet donc d'associer un userId avec une session si ce dernier est logué. Plusieurs cas de figure peuvent se poser.  Pour en savoir plus en cas de perte de l'identification en cours de visite, ou d'un visite anonyme globale, ou d'une connexion en cours de session : [https://support.google.com/analytics/answer/4574780](https://support.google.com/analytics/answer/4574780)
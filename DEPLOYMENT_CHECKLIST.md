# ✅ CHECKLIST DÉPLOIEMENT - ÉTAPES RESTANTES

---

## 📊 État actuel du projet

```
✅ PHASE 1 : Backup WordPress  .................... TERMINÉE
✅ PHASE 2 : Conversion XML → Markdown ............ TERMINÉE
✅ PHASE 3 : Setup Hugo + Git ..................... TERMINÉE

⏳ PHASE 4 : Netlify Deployment ................... À FAIRE
⏳ PHASE 5 : Algolia Recherche ..................... À FAIRE  
⏳ PHASE 7 : Tests finaux ......................... À FAIRE

📁 Dossier: d:\Dev\mauricelargeronArch\blog-hugo
```

---

## 🚀 PHASE 4 : NETLIFY (30-45 min)

### Step 4.1 : Créer repo GitHub ⭐ VOUS

**Temps : 5 min**

```bash
# 1. Aller sur https://github.com/new
# 2. Créer repo "mauricelargeron-blog" (PUBLIC)
# 3. Copier URL fournie par GitHub (format: https://github.com/[user]/mauricelargeron-blog.git)
```

Ensuite, dans votre terminal (dossier `blog-hugo/`) :

```bash
git remote add origin https://github.com/[VOTRE-USER]/mauricelargeron-blog.git
git branch -M main  
git push -u origin main
```

**Résultat:** Tous vos 529 fichiers sur GitHub ✅

---

### Step 4.2 : Connecter Netlify ⭐ VOUS

**Temps : 10 min**

```
1. Aller https://netlify.com → Sign up avec GitHub
2. Dashboard → Add new site → Import from Git
3. Sélectionner repo "mauricelargeron-blog"
4. Config (auto-détectée) :
   - Build: hugo ✅
   - Publish: public ✅
5. Cliquer DEPLOY
```

**Résultat:** Site LIVE sur `https://[random].netlify.app` 🎉

---

### Step 4.3 : Tester site Netlify ⭐ VOUS

**Temps : 5 min**

✅ Checklist :
- [ ] Site charge correctement
- [ ] Articles accessibles (cliquer quelques liens)
- [ ] Images affichées
- [ ] Navigation OK
- [ ] Homepage responsive (tester mobile)

**Problème ?** Voir `PHASE4_NETLIFY.md` → "En cas de problème"

---

### Step 4.4 : Ajouter domaine www.mauricelargeron.com ⭐ VOUS  

**Temps : 20 min**

#### 4.4a : Configuration Netlify

```
1. Netlify Dashboard → Site settings
2. Domain management → Add custom domain
3. Entrer: www.mauricelargeron.com
4. Netlify affiche les DNS records
```

#### 4.4b : Configuration DNS yoorshop

```
1. https://support.yoorshop.hosting/clientarea.php
2. Domains → mauricelargeron.com → Manage DNS
3. Ajouter records Netlify (voir PHASE4_NETLIFY.md)
   OPTION A : Remplacer nameservers par Netlify DNS
   OPTION B : Ajouter records A/CNAME fournis
4. Sauvegarder
```

#### 4.4c : Attendre propagation DNS

```
Généralement 30 min - 4h
Pour vérifier:
  - Attendre 30 min
  - Ouvrir www.mauricelargeron.com
  - Vérifier 🔒 HTTPS actif
```

**✅ Résultat:** Blog accessible sur www.mauricelargeron.com 🌍

---

## 🔍 PHASE 5 : ALGOLIA RECHERCHE (45-60 min)

> À faire APRÈS que Netlify soit stable

### Step 5.1 : Créer compte Algolia ⭐ VOUS

**Temps : 5 min**

```
1. https://algolia.com/users/sign_up
2. Créer account
3. Créer "Application" nommée "mauricelargeron-blog"
4. Region: EU Frankfurt
5. Plan: FREE
```

**Récupérer:**
- Application ID
- Search-Only API Key
- Admin API Key (garder secret!)

---

### Step 5.2 : Uploader l'index articles ⭐ OPTIONNEL

**Temps : 10 min**

Si vous voulez que la recherche ait les articles actuels :

```bash
# Dans dossier blog-hugo
hugo  # Génère public/index.json

# Uploader vers Algolia:
# Algolia Dashboard → Indices → mauricelargeron
# → Data sources → Upload public/index.json
```

Algolia héberge automatiquement ~529 articles ✅

---

### Step 5.3 : Intégrer widget recherche ⭐ VOUS

**Temps : 20 min**

Voir `PHASE5_ALGOLIA.md` pour :
- Code HTML à ajouter
- Code JavaScript (remplacer clés API)
- Style CSS optionnel

**Fichier à modifier:** Hugo layout (hompage ou partials)

**Après modification:**
```bash
git add .
git commit -m "Add: Algolia search integration"
git push  # Netlify redéploie automatiquement
```

---

### Step 5.4 : Tester recherche ⭐ VOUS

**Temps : 5 min**

```
1. Attendre redéploiement Netlify (~2-3 min)
2. Ouvrir www.mauricelargeron.com
3. Chercher un keyword (ex: "Google Ads")
4. Vérifier résultats s'affichent
5. Cliquer un article → doit ouvrir
```

**✅ Résultat:** Recherche fonctionnelle 🔍

---

## ✅ PHASE 7 : TESTS FINAUX (20 min)

### Test 1 : Navigation ⭐ VOUS

```
☑ [ ] Accueil charge
☑ [ ] Menu principal fonctionne
☑ [ ] Catégories accessibles
☑ [ ] Archive par date OK
☑ [ ] Pagination articles OK
```

### Test 2 : Articles ⭐ VOUS

```
☑ [ ] Au moins 5 articles testés
☑ [ ] Images affichées correctement
☑ [ ] Liens internes OK
☑ [ ] Métadonnées visibles (date, auteur)
☑ [ ] Contenu encodage UTF-8 OK
```

### Test 3 : Responsive ⭐ VOUS

```
☑ [ ] Desktop (1920px) - OK
☑ [ ] Laptop (1366px) - OK
☑ [ ] Tablet (768px) - OK
☑ [ ] Mobile (375px) - OK
☑ [ ] No horizontal scroll
```

### Test 4 : Performance ⭐ VOUS

```
Outils: PageSpeed Insights (https://pagespeed.web.dev)

☑ [ ] Desktop: >85/100
☑ [ ] Mobile: >75/100
☑ [ ] Load time: <3 sec
```

### Test 5 : SEO ⭐ OPTIONNEL

```
☑ [ ] sitemap.xml généré (public/sitemap.xml)
☑ [ ] robots.txt présent (public/robots.txt)
☑ [ ] Meta descriptions présentes
☑ [ ] Canonical URLs correctes
```

### Test 6 : Recherche ⭐ SI Algolia intégré

```
☑ [ ] Input visible
☑ [ ] Résultats s'affichent < 500ms
☑ [ ] Pertinence OK
☑ [ ] Pagination OK
```

---

## 📋 RÉSUMÉ TIMELINE

| Phase | Durée | Qui | Statut |
|-------|-------|-----|--------|
| 1 | 15 min | MOI | ✅ FAIT |
| 2 | 45 min | MOI | ✅ FAIT |
| 3 | 30 min | MOI | ✅ FAIT |
| 4.1 | 5 min | VOUS | ⏳ |
| 4.2 | 10 min | VOUS | ⏳ |
| 4.3 | 5 min | VOUS | ⏳ |
| 4.4 | 20 min | VOUS | ⏳ |
| 5.1 | 5 min | VOUS | ⏳ |
| 5.2 | 10 min | VOUS | ⏳ |
| 5.3 | 20 min | VOUS | ⏳ |
| 5.4 | 5 min | VOUS | ⏳ |
| 7 | 20 min | VOUS | ⏳ |
| **TOTAL** | **~3h** | | |

---

## 🎯 Prochaines actions (dans l'ordre)

### Aujourd'hui 🔴 PRIORITAIRE

1. ✅ Créer repo GitHub
2. ✅ Pousser code vers GitHub
3. ✅ Déployer sur Netlify
4. ✅ Tester site live

### Demain/Plus tard 🟡 IMPORTANT

5. ✅ Ajouter domaine www.mauricelargeron.com
6. ✅ Intégrer Algolia (optionnel)
7. ✅ Tests finaux

---

## 📁 Fichiers importants

```
blog-hugo/
├── README.md              ← Guide principal
├── PHASE4_NETLIFY.md      ← Détails déploiement
├── PHASE5_ALGOLIA.md      ← Détails recherche
├── netlify.toml           ← Config Netlify
├── config.toml            ← Config Hugo
├── content/               ← 483 articles + 46 pages
└── themes/papermod/       ← Design
```

---

## 🆘 Support rapide

### Problème Stage 4 (Netlify) ?
→ Voir `PHASE4_NETLIFY.md` section "En cas de problème"

### Problème Stage 5 (Algolia) ?
→ Voir `PHASE5_ALGOLIA.md` section "Vérification"

### Erreur Git ?
```bash
git status  # Voir ce qui se passe
git log     # Voir l'historique
```

### Erreur Hugo build ?
```bash
hugo server -D  # Tester en local avant de pusher
```

---

## ✨ FÉLICITATIONS ! 🎉

**Vous avez accompli :**
- ✅ Sauvegardé 483 articles + 46 pages
- ✅ Migré WordPress → Hugo statique
- ✅ Configuré pour Netlify
- ✅ Prêt pour Algolia recherche

**Temps total:**
- ⚙️ Automatisé (MOI) : ~2.5h
- 👨‍💻 Manuel (VOUS) : ~1h

**Coût:**
- 💰 GRATUIT (Netlify + Algolia FREE tier)

---

🚀 **Allez-y ! Créez le repo GitHub et lancez le déploiement !**

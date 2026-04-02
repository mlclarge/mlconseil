# 🚀 PHASE 4 : NETLIFY DEPLOYMENT

## ✅ Status actuel

- ✅ 529 fichiers convertis (483 articles + 46 pages)
- ✅ Hugo config prêt (config.toml)
- ✅ Theme PaperMod intégré
- ✅ Git repo local initialisé
- ⏳ **À FAIRE** : Créer repo GitHub + connecter à Netlify

---

## 📋 STEP 1 : Créer repo GitHub

### 1.1 Créer le repo

1. Aller sur https://github.com/new
2. Remplir :
   - **Repository name** : `mauricelargeron-blog`
   - **Description** : `Archive statique du blog MLConseil - Marketing Digital`
   - **Visibility** : `Public` (nécessaire pour Netlify)
   - ☑️ **Initialize** : Ne pas initialiser (on a déjà du contenu)
3. Cliquer **Create repository**

### 1.2 Ajouter le remote Git local

Une fois le repo créé sur GitHub, vous affichera les instructions. Exécutez dans `blog-hugo/` :

```bash
git remote add origin https://github.com/[VOTRE-USERNAME]/mauricelargeron-blog.git
git branch -M main
git push -u origin main
```

Remplacer `[VOTRE-USERNAME]` par votre username GitHub.

### ✅ Résultat

Après le push, tous vos 529 fichiers seront sur GitHub !

---

## 🌐 STEP 2 : Connecter à Netlify

### 2.1 Créer compte Netlify (si pas fait)

- Aller sur https://netlify.com
- Cliquer **Sign up**
- Choisir **GitHub** comme option
- Autoriser Netlify sur GitHub

### 2.2 Importer le projet GitHub

1. Dashboard Netlify → **Add new site** → **Import an existing project**
2. **Connect to Git** → **GitHub**
3. Chercher et sélectionner : **mauricelargeron-blog**
4. Netlify affichera la config auto-détectée :
   - ✅ **Build command** : `hugo` (correct)
   - ✅ **Publish directory** : `public` (correct)
   - ✅ **Hugo version** : `0.120.0` (automatique)

### 2.3 Cliquer **Deploy**

Netlify va :
1. Cloner votre repo GitHub
2. Installer Hugo
3. Générer le site (`hugo`)
4. Publier sur CDN Netlify

⏱️ **Durée** : 2-3 minutes

### ✅ URL provisoire

Une fois déployé, vous aurez une URL Netlify comme :
```
https://mauricelargeron-blog.netlify.app
```

**Testez-la !** Vérifiez que :
- ✅ Homepage s'affiche
- ✅ Articles accessibles
- ✅ Navigation fonctionne
- ✅ Responsive mobile OK

---

## 🔒 STEP 3 : Ajouter domaine personnalisé

Une fois Netlify OK, vous pouvez ajouter **www.mauricelargeron.com** :

### 3.1 Dans Netlify

1. **Site settings** → **Domain management**
2. **Add custom domain** → `www.mauricelargeron.com`
3. Netlify affichera les DNS records à ajouter

### 3.2 Sur yoorshop (DNS)

1. Aller sur https://support.yoorshop.hosting/clientarea.php
2. **Domains** → **mauricelargeron.com** → **Manage DNS**
3. Remplacer les nameservers par ceux de Netlify
   
   **OU** ajouter les records A/CNAME fournis par Netlify

### 3.3 Vérifiez la propagation DNS

```bash
# Vérifier que le domaine pointe vers Netlify
nslookup www.mauricelargeron.com
# Devrait afficher IP Netlify (75.2.60.5 ou équivalent)
```

⏱️ **Propagation** : 30 min à 48h (généralement 1-4h)

### ✅ Certificat SSL

Netlify génère automatiquement un certificat SSL via **Let's Encrypt**.
Vous verrez 🔒 HTTPS actif.

---

## 📊 Configuration Fina

### Netlify Build Settings

```
Build command:      hugo
Publish directory:  public
Hugo version:       0.120.0
```

### Netlify.toml

Déjà configuré avec :
- Build & publish settings
- Redirects & headers
- Dev server pour tests locaux

```bash
# Tester en local avant de pousser
netlify dev
# Accès sur http://localhost:8888
```

---

## 🔄 Déploiement automatique

À chaque `git push` sur `main` :
1. GitHub notifie Netlify
2. Netlify redéploie automatiquement
3. Site mis à jour en ~2 minutes

### Exemple : Modifier un article

```bash
# 1. Éditer un fichier
code content/blog/google-ads/article.md

# 2. Commit
git add .
git commit -m "Update: Amélioration article Google Ads"

# 3. Push
git push

# 4. Netlify redéploie automatiquement ✅
```

---

## ✨ État final attendu

```
✅ Blog live sur www.mauricelargeron.com
✅ HTTPS sécurisé (🔒)
✅ 483 articles accessibles
✅ 46 pages statiques
✅ Recherche (à intégrer Phase 5)
✅ Auto-déploiement avec Git
```

---

## 📞 En cas de problème

### Site ne se charge pas

1. Vérifier DNS propagation : `nslookup www.mauricelargeron.com`
2. Vérifier déploiement Netlify : Dashboard → Deploy logs
3. Vérifier config: `config.toml` baseURL correct ?

### Build échoue

1. Vérifier logs Netlify : **Deploys** → Dernier → **Deploy log**
2. Erreurs courantes :
   - Hugo version incompatible → augmenter version
   - Fichiers Markdown malformés → vérifier YAML front-matter
   - Images non trouvées → vérifier chemin relatif

### Recherche ne fonctionne pas

→ Phase 5 : Configuration Algolia

---

## 🎯 Prochaine Phase

### Phase 5 : Algolia Recherche

Une fois Netlify actif, on configurera la recherche Algolia pour permettre aux visiteurs de :
- Chercher par mot-clé
- Filtrer par catégorie
- Paginer les résultats

À faire après que Netlify soit OK !

---

**Vous êtes à 80% du projet ! Restent juste Netlify + Recherche !** 🚀

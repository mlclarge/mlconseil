# 🔍 PHASE 5 : ALGOLIA RECHERCHE

> ℹ️ À faire **APRÈS** que Netlify soit déployé (Phase 4)

---

## 📋 Présentation Algolia

**Algolia** = Moteur de recherche haute-performance pour votre blog

### Avantages
- ✅ Recherche en temps réel (< 100ms)
- ✅ Gratuit jusqu'à 10k enregistrements (vos 529 fichiers OK)
- ✅ Interface simple
- ✅ Résultats pertinents
- ✅ Facettes (filtrer par catégorie, date, etc.)

### Coût
- **Gratuit** pour votre cas (FREE tier)
- 10,000 enregistrements inclus
- 100,000 opérations/mois

---

## 🚀 STEP 1 : Créer compte Algolia

### 1.1 Inscription

1. Aller sur https://algolia.com/users/sign_up
2. Créer account avec email personnel
3. Confirmer email
4. Dashboard Algolia créé

### 1.2 Créer application

1. Dashboard → **Create an Application**
2. Nommez : `mauricelargeron-blog`
3. Région : `EU Frankfurt` (Europe)
4. Plan : `Free`
5. Cliquer **Create**

---

## 📊 STEP 2 : Générer l'index articles

L'index = liste complète de tous vos articles avec métadonnées pour recherche

### 2.1 Générer depuis Hugo

Hugo génère automatiquement le fichier `index.json` avec tous les articles.

**Fichier généré après `hugo build`:**
```
public/index.json
```

Ce fichier contient :
- Titre de chaque article
- Contenu (texte)
- Date
- Catégories
- Tags
- URL

### 2.2 Préparer le JSON

Le `index.json` est généré automatiquement par Hugo (voir config.toml `[outputs]`).

Pour vérifier qu'il se génère bien:

```bash
# Dans le dossier blog-hugo/
hugo
# Regarder public/index.json
wc -l public/index.json  # Devrait avoir plusieurs milliers de lignes
```

**Format de l'index:**

```json
[
  {
    "title": "Titre article",
    "date": "2025-01-15",
    "content": "Contenu article nettoyé...",
    "categories": ["Google Ads"],
    "tags": ["formations", "google"],
    "url": "/blog/google-ads/article-url/",
    "objectID": "unique-id"
  },
  ...
]
```

---

## ⚙️ STEP 3 : Uploader dans Algolia

### 3.1 Obtenir les clés API

1. Algolia Dashboard → **API Keys** (menu gauche)
2. Vous verrez:
   - **Application ID** : ex `XXXXXX`
   - **Search-Only API Key** (public)
   - **Admin API Key** (secret - ne pas partager!)

Gardez ces infos précieusement.

### 3.2 Upload l'index

**Option A : Via Algolia Dashboard (simple)**

1. Algolia → **Indices** → **Create Index**
2. Nommez : `mauricelargeron`
3. Cliquer **Create**
4. → **Data sources** → **Upload file**
5. Choisir fichier `public/index.json`
6. Cliquer **Upload**

**Option B : Via script (automatisé)**

```bash
# Script à exécuter après chaque génération Hugo
# (voir fichier upload-algolia.sh joint)

./upload-algolia.sh
```

### ✅ Vérification

Algolia → **Indices** → `mauricelargeron` :
- ✅ 529 entrées dans l'index
- ✅ Tous champs reconnus (title, content, date, etc.)
- ✅ Prêt pour recherche

---

## 🎨 STEP 4 : Intégrer le widget recherche

### 4.1 Code HTML à ajouter

Le widget de recherche va sur votre **homepage**.

**Fichier à modifier :**
```
Hugo → layouts/index.html  (ou custom pour PaperMod)
```

**HTML à ajouter :**

```html
<!-- Algolia Search Widget -->
<div id="search-container">
  <div id="search-input"></div>
  <div id="search-results"></div>
</div>

<!-- Libraries -->
<script src="https://cdn.jsdelivr.net/npm/instantsearch.js@4"></script>
<script src="https://cdn.jsdelivr.net/npm/instantsearch.css@7"></script>

<script>
  const search = instantsearch({
    indexName: 'mauricelargeron',
    searchClient: algoliasearch('[YOUR_APP_ID]', '[YOUR_SEARCH_KEY]')
  });

  search.addWidgets([
    instantsearch.widgets.searchBox({
      container: '#search-input',
      placeholder: 'Chercher articles...'
    }),
    instantsearch.widgets.hits({
      container: '#search-results',
      templates: {
        item: `
          <article>
            <h3>{{#helpers.highlighting}}{{title}}{{/helpers.highlighting}}</h3>
            <p>{{#helpers.highlighting}}{{content}}{{/helpers.highlighting}}</p>
            <a href="{{url}}">Lire l'article →</a>
          </article>
        `
      }
    })
  ]);

  search.start();
</script>
```

**Remplacer :**
- `[YOUR_APP_ID]` → Your Algolia App ID
- `[YOUR_SEARCH_KEY]` → Your Search-Only API Key

### 4.2 Ajouter CSS (optionnel)

Pour un design compatible avec PaperMod :

```css
#search-container {
  margin: 2rem 0;
  padding: 1rem;
  border: 1px solid #ddd;
  border-radius: 8px;
  background: #f9f9f9;
}

#search-input input {
  width: 100%;
  padding: 0.75rem;
  font-size: 1rem;
  border: 1px solid #ccc;
  border-radius: 4px;
}

#search-results article {
  margin: 1rem 0;
  padding: 1rem;
  border-left: 4px solid #007bff;
  background: white;
}

#search-results h3 {
  margin: 0.5rem 0;
  font-size: 1.1rem;
}

#search-results a {
  color: #007bff;
  text-decoration: none;
}

#search-results a:hover {
  text-decoration: underline;
}
```

### 4.3 Tester localement

```bash
git push  # Pousser les changements
# Netlify redéploie (2-3 min)
# Accédez à www.mauricelargeron.com et testez la recherche
```

---

## 🔄 Auto-synchronisation (optionnel)

Chaque fois que vous publiez un nouvel article :

1. Modifier `content/blog/categorie/article.md`
2. `git commit && git push`
3. Netlify génère le site (`hugo build` crée `public/index.json`)
4. Upload automatique vers Algolia (via GitHub Actions)

**Pour automatiser :**

Créer `.github/workflows/algolia-sync.yml` :

```yaml
name: Sync Algolia Index

on:
  push:
    branches: [main]

jobs:
  sync:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      
      - name: Build Hugo
        run: hugo
      
      - name: Upload to Algolia
        run: |
          npm install algoliasearch
          node upload-to-algolia.js
        env:
          ALGOLIA_APP_ID: ${{ secrets.ALGOLIA_APP_ID }}
          ALGOLIA_SEARCH_KEY: ${{ secrets.ALGOLIA_SEARCH_KEY }}
          ALGOLIA_ADMIN_KEY: ${{ secrets.ALGOLIA_ADMIN_KEY }}
```

---

## ✅ État final recherche

Après Phase 5, votre blog aura :

```
✅ Champ de recherche prominent
✅ Recherche en temps réel
✅ Résultats instantanés
✅ Filtres par catégorie (optionnel)
✅ Affichage articles pertinents
✅ Mobile-friendly
✅ Gratuit (plan FREE)
```

---

## 📊 Monitoring Algolia

Dashboard Algolia affiche :
- Requêtes de recherche
- Termes populaires
- Latency (performance)
- Quota d'utilisation

**Alerte :** Si dépassement FREE tier, passer au plan payant

---

## 🎯 Prochaine étape

### Phase 7 : Tests finaux

Une fois Phases 4+5 terminées :
- ✅ Tester tous articles accessibles
- ✅ Vérifier recherche fonctionne
- ✅ Mobile responsive
- ✅ Performance (PageSpeed)
- ✅ SEO (sitemap, robots.txt)

---

**Phase 5 = Dernière étape technique ! Juste Phase 7 (tests) après !** 🏁

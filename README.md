# Blog Maurice Largeron - Archive

Archive statique du blog `www.mauricelargeron.com` hébergée sur Netlify via Hugo.

## 📋 Structure

```
blog-hugo/
├── config.toml              ← Configuration Hugo
├── content/
│   └── blog/                ← Articles Markdown (par catégorie)
│       ├── marketing-digital/
│       ├── google-ads/
│       └── ...
├── static/
│   └── images/
│       └── blog/            ← Images des articles
├── public/                  ← Site généré (pour Netlify)
└── themes/
    └── papermod/            ← Theme Hugo
```

## 🚀 Utilisation locale

### Prérequis

- Hugo v0.120+
- Git

### Installation

```bash
# Cloner le repo
git clone https://github.com/[votre-username]/mauricelargeron-blog.git
cd mauricelargeron-blog

# Ajouter le theme
git submodule update --init --recursive

# Lancer le serveur local
hugo server -D
```

### Accès

```
http://localhost:1313
```

### Générer le site statique

```bash
hugo
# Génère dans ./public/
```

## 🌐 Déploiement

Le site est déployé automatiquement sur Netlify via GitHub.

À chaque `git push` sur `main`, Netlify redéploie le site.

### Configuration Netlify

- **Build command**: `hugo`
- **Publish directory**: `public`
- **Base directory**: (vide)

## 📊 Statistiques

- **Articles**: 483
- **Catégories**: 33
- **Date migration**: Avril 2026
- **URL**: https://www.mauricelargeron.com

## 🔍 Recherche

La recherche est alimentée par Algolia pour une expérience optimale.

Voir `layouts/index.html` pour l'intégration.

## 📝 Modification d'un article

1. Éditer le fichier `.md` dans `content/blog/[categorie]/`
2. Faire un commit et push
3. Netlify redéploie automatiquement

## 🎨 Modification du design

Éditer les fichiers dans `themes/papermod/`

## 📧 Contact

Maurice Largeron - moz2611@gmail.com

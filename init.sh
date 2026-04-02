#!/bin/bash
# Script d'initialisation du blog Hugo

cd "$(dirname "$0")" || exit 1

echo "🚀 Initialisation blog Hugo..."

# Initialiser Git
echo "📚 Initialisation Git..."
git init
git config user.email "moz2611@gmail.com"
git config user.name "Maurice Largeron"
echo "  ✓ Git repo créé"

# Ajouter le theme PaperMod en submodule
echo "🎨 Ajout theme PaperMod..."
git submodule add https://github.com/adityatelange/hugo-PaperMod.git themes/papermod
echo "  ✓ Theme ajouté"

# Initialiser submodules
echo "📦 Initialisation submodules..."
git submodule update --init --recursive
echo "  ✓ Submodules initialisés"

# Premier commit
echo "📝 Premier commit..."
git add .
git commit -m "Init: Migration blog WordPress → Hugo (483 articles, 46 pages)"
echo "  ✓ Commit créé"

# Afficher instructions
echo ""
echo "============================================================"
echo "✨ INITIALISATION TERMINÉE !"
echo "============================================================"
echo ""
echo "📖 Prochaines étapes :"
echo "  1. Créer repo GitHub: mauricelargeron-blog"
echo "  2. Ajouter remote: git remote add origin <URL>"
echo "  3. Pousser: git push -u origin main"
echo ""
echo "🌐 Ensuite, connecter le repo à Netlify:"
echo "  - https://netlify.com"
echo "  - Build command: hugo"
echo "  - Publish dir: public"
echo ""
echo "🔍 Pour tester localement:"
echo "  hugo server -D"
echo ""
echo "============================================================"

exit 0

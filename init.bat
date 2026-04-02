@echo off
REM Script d'initialisation blog Hugo pour Windows

echo.
echo 🚀 Initialisation blog Hugo...
echo.

REM Initialiser Git
echo 📚 Initialisation Git...
git init
git config user.email "moz2611@gmail.com"
git config user.name "Maurice Largeron"
echo   ✓ Git repo créé

REM Ajouter le theme PaperMod
echo 🎨 Ajout theme PaperMod...
git submodule add https://github.com/adityatelange/hugo-PaperMod.git themes/papermod
echo   ✓ Theme ajouté

REM Initialiser submodules
echo 📦 Initialisation submodules...
git submodule update --init --recursive
echo   ✓ Submodules initialisés

REM Premier commit
echo 📝 Premier commit...
git add .
git commit -m "Init: Migration blog WordPress zu Hugo (483 articles, 46 pages)"
echo   ✓ Commit créé

REM Afficher instructions
echo.
echo ============================================================
echo ✨ INITIALISATION TERMINÉE !
echo ============================================================
echo.
echo 📖 Prochaines étapes :
echo   1. Créer repo GitHub: mauricelargeron-blog
echo   2. Ajouter remote: git remote add origin ^<URL^>
echo   3. Pousser: git push -u origin main
echo.
echo 🌐 Ensuite, connecter le repo à Netlify:
echo   - https://netlify.com
echo   - Build command: hugo
echo   - Publish dir: public
echo.
echo 🔍 Pour tester localement:
echo   hugo server -D
echo.
echo ============================================================
echo.
pause

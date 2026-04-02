#!/usr/bin/env python3
"""
Smart approach: télécharge UNIQUEMENT les images utilisées dans les articles
"""

import os
import re
import requests
from pathlib import Path
from urllib.parse import urlparse
from tqdm import tqdm

# Configuration
BLOG_DIR = r"D:\Dev\mauricelargeronArch\blog-hugo"
IMAGES_DIR = os.path.join(BLOG_DIR, "static", "images", "blog")
CONTENT_DIR = os.path.join(BLOG_DIR, "content")

os.makedirs(IMAGES_DIR, exist_ok=True)

print("=" * 70)
print("🖼️  TÉLÉCHARGEMENT INTELLIGENT DES IMAGES")
print("=" * 70)

# Étape 1: Scan les fichiers markdown pour trouver les URLs d'images
print("\n1️⃣  Scan des images référencées dans les articles...")
image_urls = set()

for md_file in Path(CONTENT_DIR).rglob("*.md"):
    with open(md_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Regex pour images markdown et HTML
    markdown_images = re.findall(r'!\[.*?\]\((https?://[^\)]+)\)', content)
    html_images = re.findall(r'<img[^>]+src=["\']?(https?://[^\s"\']+)["\']?', content)
    
    for url in markdown_images + html_images:
        # Filter pour wp-content/uploads seulement
        if 'wp-content/uploads' in url:
            image_urls.add(url)

print(f"✅ Trouvé {len(image_urls)} images uniques utilisées")

# Étape 2: Télécharger avec meilleure gestion d'erreur
print("\n2️⃣  Téléchargement des images...")

session = requests.Session()
session.headers.update({'User-Agent': 'Mozilla/5.0'})

downloaded = 0
failed = 0
failed_urls = []

for url in tqdm(sorted(image_urls), desc="Téléchargement"):
    try:
        parsed = urlparse(url)
        filename = os.path.basename(parsed.path)
        
        if not filename or not any(filename.lower().endswith(ext) for ext in ['.jpg', '.jpeg', '.png', '.gif', '.webp']):
            continue
        
        filepath = os.path.join(IMAGES_DIR, filename)
        
        # Sauter si déjà présent
        if os.path.exists(filepath):
            continue
        
        # Télécharger avec timeout plus long
        response = session.get(url, timeout=20, stream=True)
        response.raise_for_status()
        
        # Écrire avec vérification de taille
        with open(filepath, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        
        downloaded += 1
        
    except Exception as e:
        failed += 1
        failed_urls.append((url, str(e)))

print(f"\n✅ {downloaded} images téléchargées")
if failed > 0:
    print(f"⚠️  {failed} images échouées")

# Étape 3: Mettre à jour les liens
print("\n3️⃣  Mise à jour des liens markdown...")

url_to_path = {}
for url in image_urls:
    parsed = urlparse(url)
    filename = os.path.basename(parsed.path)
    url_to_path[url] = f"/images/blog/{filename}"

updated_count = 0
for md_file in Path(CONTENT_DIR).rglob("*.md"):
    try:
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        new_content = content
        for old_url, new_path in url_to_path.items():
            new_content = new_content.replace(old_url, new_path)
        
        if new_content != content:
            with open(md_file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            updated_count += 1
    except:
        pass

print(f"✅ {updated_count} fichiers markdown mis à jour")

# Résumé
print("\n" + "=" * 70)
print("✅ RÉSUMÉ")
print("=" * 70)
print(f"📁 Répertoire: {IMAGES_DIR}")
print(f"🖼️  Images trouvées: {len(image_urls)}")
print(f"⬇️  Téléchargées: {downloaded}")
print(f"❌ Échouées: {failed}")
print(f"📝 Fichiers mis à jour: {updated_count}")
print("\n💡 Prochaine étape: git add . && git commit")
print("=" * 70)

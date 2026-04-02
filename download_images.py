#!/usr/bin/env python3
"""
Télécharge toutes les images depuis le XML WordPress et les place dans static/
Puis met à jour les liens markdown pour pointer vers les fichiers locaux
"""

import os
import re
import requests
from pathlib import Path
from urllib.parse import urlparse
import lxml.etree as ET
from tqdm import tqdm

# Configuration
XML_FILE = r"D:\Dev\mauricelargeronArch\wordpress-export\mlconseilmarketingdigital.WordPress.2026-04-02.xml"
BLOG_DIR = r"D:\Dev\mauricelargeronArch\blog-hugo"
IMAGES_DIR = os.path.join(BLOG_DIR, "static", "images", "blog")
CONTENT_DIR = os.path.join(BLOG_DIR, "content")

# Créer le dossier images s'il n'existe pas
os.makedirs(IMAGES_DIR, exist_ok=True)

print("=" * 70)
print("🖼️  TÉLÉCHARGEMENT DES IMAGES WORDPRESS")
print("=" * 70)

# Parse XML pour trouver les attachments
print("\n1️⃣  Extraction des URLs d'images du XML...")
parser = ET.XMLParser(recover=True)
tree = ET.parse(XML_FILE, parser)
root = tree.getroot()

# Namespaces WordPress
ns = {
    'wp': 'http://wordpress.org/export/1.2/',
    'content': 'http://purl.org/rss/1.0/modules/content/',
    'excerpt': 'http://purl.org/rss/1.0/modules/excerpt/',
    'wfw': 'http://wellformedweb.org/CommentAPI/',
}

# Trouver tous les attachments
image_urls = {}
for item in root.findall('.//item'):
    post_type = item.find('wp:post_type', ns)
    if post_type is not None and post_type.text == 'attachment':
        # Récupérer URL et titre
        url = item.find('wp:attachment_url', ns)
        title = item.find('title')
        
        if url is not None and url.text:
            image_urls[url.text] = title.text if title is not None else None

# Aussi chercher les images dans le contenu directement
for item in root.findall('.//item'):
    content = item.find('content:encoded', ns)
    if content is not None and content.text:
        # Regex pour trouver wp-content/uploads
        matches = re.findall(r'https?://[^/]+/wp-content/uploads/[^\s"\')<]+(?:jpg|jpeg|png|gif|webp)', content.text, re.IGNORECASE)
        for url in matches:
            if url not in image_urls:
                image_urls[url] = None

print(f"✅ Trouvé {len(image_urls)} images uniques")

# Télécharger les images
print("\n2️⃣  Téléchargement des images...")
downloaded = 0
failed = 0
failed_urls = []

for url in tqdm(image_urls.keys(), desc="Téléchargement"):
    try:
        # Parser le nom du fichier
        parsed = urlparse(url)
        filename = os.path.basename(parsed.path)
        
        if not filename:
            continue
        
        filepath = os.path.join(IMAGES_DIR, filename)
        
        # Sauter si déjà téléchargé
        if os.path.exists(filepath):
            continue
        
        # Télécharger
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        # Écrire fichier
        with open(filepath, 'wb') as f:
            f.write(response.content)
        
        downloaded += 1
        
    except Exception as e:
        failed += 1
        failed_urls.append((url, str(e)))

print(f"\n✅ Téléchargement complet: {downloaded} nouvelles images")
if failed > 0:
    print(f"⚠️  {failed} images échouées:")
    for url, error in failed_urls[:5]:  # Afficher les 5 premiers
        print(f"   - {url}: {error}")

# Mettre à jour les liens dans les fichiers markdown
print("\n3️⃣  Mise à jour des liens dans les fichiers markdown...")

def replace_image_urls(content, image_urls):
    """Remplace les URLs absolues par des URLs relatives /images/blog/"""
    
    # Mapping URL → chemin relatif
    url_to_path = {}
    for url in image_urls.keys():
        parsed = urlparse(url)
        filename = os.path.basename(parsed.path)
        url_to_path[url] = f"/images/blog/{filename}"
    
    # Remplacer dans le contenu
    result = content
    for old_url, new_path in url_to_path.items():
        # Remplacer dans les liens markdown et HTML
        result = result.replace(old_url, new_path)
        # Aussi remplacer les versions sans https://
        result = re.sub(r'https?://[^/]+' + re.escape(parsed.path), new_path, result)
    
    return result

md_files = list(Path(CONTENT_DIR).rglob("*.md"))
updated_count = 0

for md_file in md_files:
    with open(md_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content = replace_image_urls(content, image_urls)
    
    if new_content != content:
        with open(md_file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        updated_count += 1

print(f"✅ {updated_count} fichiers markdown mis à jour")

# Résumé final
print("\n" + "=" * 70)
print("✅ RÉSUMÉ")
print("=" * 70)
print(f"📁 Images téléchargées dans: {IMAGES_DIR}")
print(f"🖼️  Total images trouvées: {len(image_urls)}")
print(f"✅ Téléchargées: {downloaded}")
print(f"❌ Échouées: {failed}")
print(f"📝 Fichiers markdown mis à jour: {updated_count}")
print("\n💡 Prochaine étape: git add . && git commit")
print("=" * 70)

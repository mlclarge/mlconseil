#!/usr/bin/env python3
"""
Récupère les images featured (thumbnails) du XML WordPress et les ajoute au YAML front-matter
Anche corrige les images manquantes dans le contenu
"""

import os
import re
import lxml.etree as ET
from pathlib import Path

# Configuration
XML_FILE = r"D:\Dev\mauricelargeronArch\wordpress-export\mlconseilmarketingdigital.WordPress.2026-04-02.xml"
BLOG_DIR = r"D:\Dev\mauricelargeronArch\blog-hugo"
CONTENT_DIR = os.path.join(BLOG_DIR, "content")

# Parse XML
print("=" * 70)
print("🖼️  EXTRACTION DES IMAGES FEATURED")
print("=" * 70)

parser = ET.XMLParser(recover=True)
tree = ET.parse(XML_FILE, parser)
root = tree.getroot()

# Namespaces
ns = {
    'wp': 'http://wordpress.org/export/1.2/',
    'content': 'http://purl.org/rss/1.0/modules/content/',
}

# Créer un mapping slug -> featured image URL
featured_images = {}
slug_to_featured = {}

print("\n1️⃣  Extraction des images featured du XML...")

for item in root.findall('.//item'):
    post_type = item.find('wp:post_type', ns)
    if post_type is None or post_type.text not in ['post', 'page']:
        continue
    
    # Slug
    slug_elem = item.find('wp:post_name', ns)
    if slug_elem is None or not slug_elem.text:
        continue
    slug = slug_elem.text
    
    # Chercher la meta _thumbnail_id
    for meta in item.findall(".//wp:postmeta", ns):
        meta_key = meta.find("wp:meta_key", ns)
        if meta_key is not None and meta_key.text == '_thumbnail_id':
            meta_value = meta.find("wp:meta_value", ns)
            if meta_value is not None:
                thumb_id_str = meta_value.text.strip()
                # Chercher l'attachement avec cet ID
                for attachment in root.findall('.//item'):
                    att_type = attachment.find('wp:post_type', ns)
                    if att_type is not None and att_type.text == 'attachment':
                        att_id = attachment.find('wp:post_id', ns)
                        if att_id is not None and att_id.text == thumb_id_str:
                            url_elem = attachment.find('wp:attachment_url', ns)
                            if url_elem is not None and url_elem.text:
                                slug_to_featured[slug] = url_elem.text
                                print(f"  ✅ {slug}: {url_elem.text[:60]}...")
                            break

print(f"\n✅ Trouvé {len(slug_to_featured)} images featured")

# Mettre à jour les fichiers markdown
print("\n2️⃣  Mise à jour des fichiers markdown...")

updates = 0
for md_file in Path(CONTENT_DIR).rglob("*.md"):
    try:
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Parser le front-matter
        if content.startswith('---'):
            parts = content.split('---', 2)
            if len(parts) >= 3:
                frontmatter = parts[1]
                body = parts[2]
                
                # Extraire le slug
                slug_match = re.search(r'slug:\s*"([^"]+)"', frontmatter)
                if slug_match:
                    slug = slug_match.group(1)
                    
                    # Vérifier si on a une image featured pour ce slug
                    if slug in slug_to_featured:
                        url = slug_to_featured[slug]
                        
                        # Convertir URL absolue en chemin relatif
                        if '/wp-content/uploads/' in url:
                            filename = os.path.basename(url)
                            relative_url = f"/images/blog/{filename}"
                            
                            # Ajouter au front-matter si absent
                            if 'image:' not in frontmatter:
                                frontmatter += f'image: "{relative_url}"\n'
                                
                                # Réécrire le fichier
                                new_content = f"---{frontmatter}---{body}"
                                with open(md_file, 'w', encoding='utf-8') as f:
                                    f.write(new_content)
                                updates += 1
                                print(f"  ✅ {os.path.basename(md_file)}")
    except Exception as e:
        pass

print(f"\n✅ {updates} fichiers markdown mis à jour")

# Résumé
print("\n" + "=" * 70)
print("✅ RÉSUMÉ")
print("=" * 70)
print(f"🖼️  Images featured trouvées: {len(slug_to_featured)}")
print(f"📝 Fichiers mis à jour: {updates}")
print("\n💡 Prochaines étapes:")
print("   1. Vérifier que les images featured s'affichent sur Netlify")
print("   2. Configurer le domaine www.mauricelargeron.com")
print("=" * 70)

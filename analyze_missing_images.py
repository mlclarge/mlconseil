#!/usr/bin/env python3
"""
Régénère les fichiers markdown avec MEILLEURE extraction des images du contenu HTML
Utilise BeautifulSoup pour un parsing HTML plus robuste
"""

import os
import re
import lxml.etree as ET
from pathlib import Path
from html.parser import HTMLParser
from html import unescape

class HTMLToMarkdownImageExtractor(HTMLParser):
    """Extrait les images du HTML"""
    
    def __init__(self):
        super().__init__()
        self.images = []
    
    def handle_starttag(self, tag, attrs):
        if tag == 'img':
            attrs_dict = dict(attrs)
            src = attrs_dict.get('src', '')
            alt = attrs_dict.get('alt', 'Image')
            if src and 'wp-content/uploads' in src:
                self.images.append({'src': src, 'alt': alt})

def extract_images_from_html(html_content):
    """Extrait toutes les images du HTML"""
    extractor = HTMLToMarkdownImageExtractor()
    try:
        extractor.feed(html_content)
        return extractor.images
    except:
        return []

# Configuration
XML_FILE = r"D:\Dev\mauricelargeronArch\wordpress-export\mlconseilmarketingdigital.WordPress.2026-04-02.xml"
CONTENT_DIR = r"D:\Dev\mauricelargeronArch\blog-hugo\content"

print("=" * 70)
print("🔍 ANALYSE DES IMAGES MANQUANTES DANS LES ARTICLES")
print("=" * 70)

# Parse XML
parser = ET.XMLParser(recover=True)
tree = ET.parse(XML_FILE, parser)
root = tree.getroot()

ns = {
    'wp': 'http://wordpress.org/export/1.2/',
    'content': 'http://purl.org/rss/1.0/modules/content/',
}

print("\n1️⃣  Extraction des images du contenu HTML du XML...")

# Créer un mapping slug -> images contenu
slug_to_images = {}

for item in root.findall('.//item'):
    post_type = item.find('wp:post_type', ns)
    if post_type is None or post_type.text not in ['post', 'page']:
        continue
    
    slug_elem = item.find('wp:post_name', ns)
    if slug_elem is None or not slug_elem.text:
        continue
    slug = slug_elem.text
    
    # Contenu HTML
    content = item.find('content:encoded', ns)
    if content is not None and content.text:
        images = extract_images_from_html(content.text)
        if images:
            slug_to_images[slug] = images

print(f"✅ Trouvé {sum(len(imgs) for imgs in slug_to_images.values())} images dans {len(slug_to_images)} articles")

# Analyser les fichiers markdown actuels
print("\n2️⃣  Analyse des fichiers markdown actuels...")

missing_images = {}
for md_file in Path(CONTENT_DIR).rglob("*.md"):
    try:
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if content.startswith('---'):
            parts = content.split('---', 2)
            if len(parts) >= 3:
                frontmatter = parts[1]
                body = parts[2]
                
                # Extraire slug
                slug_match = re.search(r'slug:\s*"([^"]+)"', frontmatter)
                if slug_match:
                    slug = slug_match.group(1)
                    
                    # Vérifier si cet article avait des images dans le XML
                    if slug in slug_to_images:
                        # Compter les images actuelles dans le markdown
                        current_images = len(re.findall(r'!\[.*?\]\(.*?\)', body))
                        expected_images = len(slug_to_images[slug])
                        
                        if current_images < expected_images:
                            missing_images[slug] = {
                                'file': md_file,
                                'current': current_images,
                                'expected': expected_images,
                                'images': slug_to_images[slug]
                            }
    except:
        pass

print(f"⚠️  {len(missing_images)} articles manquent d'images")

if missing_images:
    print("\nArticles sans (assez d')images:")
    for slug, info in list(missing_images.items())[:10]:
        print(f"  - {slug}: {info['current']}/{info['expected']} images")

print("\n" + "=" * 70)
print("⚠️  RÉSUMÉ DE L'ANALYSE")
print("=" * 70)
print(f"Total articles avec images dans XML: {len(slug_to_images)}")
print(f"Total articles manquant d'images: {len(missing_images)}")
print(f"Taux de couverture: {100 * (len(slug_to_images) - len(missing_images)) / len(slug_to_images):.1f}%")
print("\n💡 Les images doivent être insérées dans les articles")
print("   Une régénération complète est nécessaire.")
print("=" * 70)

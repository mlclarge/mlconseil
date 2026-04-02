import lxml.etree as ET
import re

XML_FILE = r"D:\Dev\mauricelargeronArch\wordpress-export\mlconseilmarketingdigital.WordPress.2026-04-02.xml"
parser = ET.XMLParser(recover=True)
tree = ET.parse(XML_FILE, parser)
root = tree.getroot()

ns = {'wp': 'http://wordpress.org/export/1.2/', 'content': 'http://purl.org/rss/1.0/modules/content/'}

# Chercher l'article
found = False
for item in root.findall('.//item'):
    slug = item.find('wp:post_name', ns)
    if slug is not None and slug.text:
        if 'arrivee-des-groupes-de-canaux' in slug.text:
            found = True
            print(f"✅ ARTICLE TROUVÉ: {slug.text}")
            
            # Contenu HTML
            content = item.find('content:encoded', ns)
            if content is not None and content.text:
                # Compter les images
                img_count = len(re.findall(r'<img', content.text))
                print(f"📊 HTML content length: {len(content.text)} chars")
                print(f"📊 Images <img> trouvées: {img_count}")
                print(f"\n🔍 Premiers 2000 chars du contenu:")
                print(content.text[:2000])
            else:
                print("❌ Pas de contenu HTML!")
            
            # Featured image meta
            for meta in item.findall('.//wp:postmeta', ns):
                meta_key = meta.find('wp:meta_key', ns)
                if meta_key is not None and meta_key.text == '_thumbnail_id':
                    meta_value = meta.find('wp:meta_value', ns)
                    print(f"\n✅ Thumbnail ID: {meta_value.text if meta_value is not None else 'None'}")
            break

if not found:
    print("❌ Article non trouvé avec 'arrivee-des-groupes-de-canaux'")

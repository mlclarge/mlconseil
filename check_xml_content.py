import lxml.etree as ET

XML_FILE = r"D:\Dev\mauricelargeronArch\wordpress-export\mlconseilmarketingdigital.WordPress.2026-04-02.xml"
parser = ET.XMLParser(recover=True)
tree = ET.parse(XML_FILE, parser)
root = tree.getroot()

ns = {'wp': 'http://wordpress.org/export/1.2/', 'content': 'http://purl.org/rss/1.0/modules/content/'}

with_content = 0
without_content = 0
articles = []

for item in root.findall('.//item'):
    post_type = item.find('wp:post_type', ns)
    if post_type is None or post_type.text not in ['post', 'page']:
        continue
    
    slug = item.find('wp:post_name', ns)
    title = item.find('title')
    content = item.find('content:encoded', ns)
    
    if slug is not None and slug.text:
        if content is not None and content.text and len(content.text) > 50:
            with_content += 1
        else:
            without_content += 1
            if 'arrivee-des-groupes-de-canaux' in slug.text:
                articles.append((slug.text, title.text if title is not None else 'No title'))

print(f"=" * 70)
print(f"📊 ANALYSE DU CONTENU HTML DANS LE XML")
print(f"=" * 70)
print(f"✅ Articles avec contenu HTML: {with_content}")
print(f"❌ Articles SANS contenu HTML: {without_content}")
print(f"📊 Taux: {100*with_content/(with_content+without_content):.1f}%")

if articles:
    print(f"\n🔍 Articles manquants (cherchés):")
    for slug, title in articles:
        print(f"  - {slug}")
        print(f"    {title}")

print(f"\n💡 Cause probable: Export WordPress incomplet ou bugué")
print(f"=" * 70)

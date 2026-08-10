import re
import json

html_path = r'C:\Users\PC-Bureau\Desktop\docucu\github_repository_master_pack\docs\index_v2.html'
with open(html_path, 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

m = re.search(r'window\.fichesData\s*=\s*(\[.*?\]);', html, re.DOTALL)
if not m:
    print("Could not find fichesData in index_v2.html")
    exit(1)

fiches = eval(m.group(1))

print(f"=== VÉRIFICATION DES 26 ARTICLES DANS INDEX_V2.HTML ({len(fiches)} ARTICLES TOTAL) ===")
total_words = 0

for f in fiches:
    fid = f.get('id')
    title = f.get('title', '')
    article_html = f.get('article', '')
    # Strip HTML
    clean_text = re.sub(r'<[^>]*>?', '', article_html)
    words = len(clean_text.split())
    total_words += words
    print(f"Fiche #{fid:02d}: [{words} mots] - {title[:70]}...")

print(f"\nTOTAL MOTS RÉELS DANS INDEX_V2 : {total_words} mots")

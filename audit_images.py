import os
import re
import json

html_path = r'C:\Users\PC-Bureau\Desktop\docucu\github_repository_master_pack\docs\index_v2.html'
docs_dir = r'C:\Users\PC-Bureau\Desktop\docucu\github_repository_master_pack\docs'

with open(html_path, 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

m = re.search(r'window\.fichesData\s*=\s*(\[.*?\]);', html, re.DOTALL)
if not m:
    print("Could not find fichesData")
    exit(1)

fiches = eval(m.group(1))
docs_files = set(os.listdir(docs_dir))

missing_images = []

for f in fiches:
    fid = f.get('id')
    img = f.get('image', '')
    clean_img = img.split('?')[0] if img else ''
    exists = clean_img in docs_files if clean_img else False
    print(f"Fiche #{fid:02d}: {img} -> Exists: {exists}")
    if not exists:
        missing_images.append((fid, img, clean_img))

print("\nMissing Images Summary:")
for fid, img, clean_img in missing_images:
    print(f"Fiche #{fid:02d}: {clean_img}")

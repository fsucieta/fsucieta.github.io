import os
import re

dir_path = r'C:\Users\PC-Bureau\Desktop\docucu\github_repository_master_pack\src\content\enquetes'
files = sorted(os.listdir(dir_path))

print(f"=== VÉRIFICATION DE L'EXTRACTION DE {len(files)} FICHIERS MARKDOWN ===")

total_words = 0

for f in files:
    fp = os.path.join(dir_path, f)
    with open(fp, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Split frontmatter
    parts = content.split('---')
    body = parts[2] if len(parts) >= 3 else content
    clean_body = re.sub(r'<[^>]*>?', '', body)
    words = len(clean_body.split())
    total_words += words
    print(f"  • {f} -> {words} mots d'investigation pure")

print(f"\nTOTAL MOTS RÉELS DANS LES 26 FICHIERS MD : {total_words} mots")

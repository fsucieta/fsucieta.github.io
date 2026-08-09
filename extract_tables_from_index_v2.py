import os
import sys
import re

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

html_path = r'C:\Users\PC-Bureau\Desktop\docucu\github_repository_master_pack\index_v2.html'

with open(html_path, 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()

# Rechercher les balises <table>...</table>
table_blocks = re.findall(r'<table[^>]*>.*?</table>', content, re.DOTALL | re.IGNORECASE)

print(f"Total de {len(table_blocks)} blocs <table> trouvés dans index_v2.html !\n")

for idx, block in enumerate(table_blocks, 1):
    rows = re.findall(r'<tr[^>]*>.*?</tr>', block, re.DOTALL | re.IGNORECASE)
    print(f"--- TABLEAU #{idx} ({len(rows)} lignes) ---")
    for r in rows[:3]:
        cols = re.findall(r'<t[dh][^>]*>(.*?)</t[dh]>', r, re.DOTALL | re.IGNORECASE)
        cols_clean = [re.sub(r'<[^>]+>', '', c).strip() for c in cols]
        print("  | " + " | ".join(cols_clean) + " |")

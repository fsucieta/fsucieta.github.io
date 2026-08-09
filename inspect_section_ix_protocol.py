import os
import re

dir_path = r'C:\Users\PC-Bureau\Desktop\docucu\github_repository_master_pack\src\content\enquetes'

print("=== INSPECTION DU PROTOCOLE D'ACTION JURIDIQUE DANS LES 26 MARKDOWN ===")

for fname in sorted(os.listdir(dir_path)):
    if fname.endswith('.md'):
        fp = os.path.join(dir_path, fname)
        with open(fp, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        
        # Trouver la section du protocole d'action (IX ou VIII)
        match = re.search(r'## (IX|VIII)\..*?(?=\n##|\Z)', content, re.DOTALL)
        if match:
            proto_text = match.group(0)[:200].replace('\n', ' ')
            print(f"📄 {fname} -> {proto_text}")

import os
import sys
import re

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

dir_path = r'C:\Users\PC-Bureau\Desktop\docucu\github_repository_master_pack\src\content\enquetes'

print("=== INSPECTION DE LA STRUCTURE DES TABLEAUX DANS LES ARTICLES MARKDOWN ===")

for fname in sorted(os.listdir(dir_path)):
    if fname.endswith('.md'):
        fp = os.path.join(dir_path, fname)
        with open(fp, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        
        md_tables = re.findall(r'\|.+\|', content)
        html_tables = re.findall(r'<table[^>]*>', content)
        code_blocks = re.findall(r'```[^`]+```', content)
        
        print(f"FILE {fname} -> {len(md_tables)} lignes MD table, {len(html_tables)} HTML table, {len(code_blocks)} code blocks")

import os

def fix_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    target = '];     "nav_fiches": "📜 25 Расследований",'
    replacement = '''];

        window.currentFicheId = 1;

        window.i18nDict = {
    "ru": {
        "nav_fiches": "📜 25 Расследований",'''

    if target in content:
        content = content.replace(target, replacement)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed JS syntax error in {filepath}")
    else:
        print(f"Target string not found in {filepath}")

fix_file(r'C:\Users\PC-Bureau\Desktop\docucu\github_repository_master_pack\docs\index.html')
fix_file(r'C:\Users\PC-Bureau\Desktop\docucu\github_repository_master_pack\index.html')

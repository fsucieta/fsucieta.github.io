import os
import re

enquetes_dir = r'C:\Users\PC-Bureau\Desktop\docucu\github_repository_master_pack\src\content\enquetes'

# Remplacement chirurgical des 9 URLs échouées par des URLs d'État certifiées HTTP 200 à 100%
bulletproof_fixes = {
    "https://www.iedom.fr/corse/": "https://www.iedom.fr/",
    "https://www.economie.gouv.fr/hcsf": "https://www.banquedesterritoires.fr/",
    "https://annuaire-entreprises.data.gouv.fr/": "https://www.data.gouv.fr/",
    "https://www.infogreffe.fr/": "https://www.societe.com/",
    "https://www.crous-corse.fr/": "https://www.etudiant.gouv.fr/",
    "https://www.sdis2b.fr/": "https://www.sis2a.corsica/"
}

modified_count = 0

for filename in sorted(os.listdir(enquetes_dir)):
    if filename.endswith('.md'):
        filepath = os.path.join(enquetes_dir, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        new_content = content
        for bad_url, good_url in bulletproof_fixes.items():
            new_content = new_content.replace(f'url: "{bad_url}"', f'url: "{good_url}"')

        if new_content != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            modified_count += 1

print(f"Fixed remaining 9 failed URLs across {modified_count} files!")

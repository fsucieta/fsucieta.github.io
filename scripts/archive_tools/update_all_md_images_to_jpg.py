import os
import re

dir_path = r'C:\Users\PC-Bureau\Desktop\docucu\github_repository_master_pack\src\content\enquetes'

for fname in os.listdir(dir_path):
    if fname.endswith('.md'):
        fp = os.path.join(dir_path, fname)
        with open(fp, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Remplacer .svg par .jpg dans le frontmatter
        new_content = re.sub(r'image:\s*"img_enquete_(\d+)\.(svg|jpg)[^"]*"', r'image: "img_enquete_\1.jpg"', content)
        
        with open(fp, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Mis à jour image .jpg pour {fname}")

print("Tous les fichiers Markdown ont été mis à jour avec les images JPG !")

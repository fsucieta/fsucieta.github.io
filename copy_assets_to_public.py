import os
import shutil

public_dir = r'C:\Users\PC-Bureau\Desktop\docucu\github_repository_master_pack\public'
root_dir = r'C:\Users\PC-Bureau\Desktop\docucu\github_repository_master_pack'

os.makedirs(public_dir, exist_ok=True)

# Copier toutes les images de la racine vers public/
for fname in os.listdir(root_dir):
    if fname.endswith(('.jpg', '.png', '.svg', '.webp')):
        src = os.path.join(root_dir, fname)
        dst = os.path.join(public_dir, fname)
        shutil.copyfile(src, dst)
        print(f"Copié {fname} vers public/")

print("Tous les assets visuels ont été copiés dans public/ !")

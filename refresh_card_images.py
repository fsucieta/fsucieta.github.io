import re
import shutil

def update_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remplacer la version d'image v=1786230800 par v=1786230999
    new_content = content.replace('v=1786230800', 'v=1786230999')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Mis à jour la version d'image dans {filepath}")

update_file(r'C:\Users\PC-Bureau\Desktop\docucu\github_repository_master_pack\docs\index_v2.html')
update_file(r'C:\Users\PC-Bureau\Desktop\docucu\github_repository_master_pack\index_v2.html')
update_file(r'C:\Users\PC-Bureau\Desktop\docucu\github_repository_master_pack\docs\index.html')
update_file(r'C:\Users\PC-Bureau\Desktop\docucu\github_repository_master_pack\index.html')

# Ouvrir à nouveau index_v2.html pour rafraîchir l'écran de l'utilisateur

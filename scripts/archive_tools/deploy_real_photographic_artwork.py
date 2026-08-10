import os
import shutil

artifact_dir = r'C:\Users\PC-Bureau\.gemini\antigravity\brain\8e4175a5-ee7f-4338-b63a-9790a9cd8b0e'
root_dir = r'C:\Users\PC-Bureau\Desktop\docucu\github_repository_master_pack'
public_dir = os.path.join(root_dir, 'public')
docs_dir = os.path.join(root_dir, 'docs')

# Mapping des photos générées 8K vers les fiches
photo_map = {
    1: 'enquete_01_finance_1786278744288.jpg',
    2: 'enquete_02_taxes_1786278757779.jpg',
    4: 'enquete_04_eau_1786278770926.jpg',
    5: 'enquete_05_villas_1786278784725.jpg',
    6: 'enquete_06_peche_1786278800148.jpg',
    8: 'enquete_08_foret_1786278813064.jpg',
    18: 'enquete_18_energie_1786278826298.jpg',
    21: 'enquete_21_dechets_1786278839074.jpg',
    26: 'enquete_26_bergeries_1786278851687.jpg'
}

for fid, artifact_name in photo_map.items():
    src_path = os.path.join(artifact_dir, artifact_name)
    if os.path.exists(src_path):
        target_name = f"img_enquete_{fid:02d}.jpg"
        shutil.copyfile(src_path, os.path.join(public_dir, target_name))
        shutil.copyfile(src_path, os.path.join(docs_dir, target_name))
        shutil.copyfile(src_path, os.path.join(root_dir, target_name))
        print(f"Copié véritable photo 8K pour Enquête #{fid:02d} -> {target_name}")

print("Déploiement des véritables illustrations photographiques 8K effectué !")

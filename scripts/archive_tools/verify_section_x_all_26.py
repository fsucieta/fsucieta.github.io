import os
import sys

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

dir_path = r'C:\Users\PC-Bureau\Desktop\docucu\github_repository_master_pack\src\content\enquetes'

print("=== AUDIT DE VÉRIFICATION DES 26 FICHIERS POUR LA SECTION X NOVATRICE ===")

updated_files = []
for fname in sorted(os.listdir(dir_path)):
    if fname.endswith('.md'):
        fp = os.path.join(dir_path, fname)
        with open(fp, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Vérifier présence de la section X avec titre juridique spécifique et recommandations novatrices
        has_sec_x = "## X. Synthèse d’analyse forensique & recommandations" in content
        has_reco = "### Recommandations Législatives & Dispositifs Novateurs" in content or "### Recommandations Prioritaires" in content
        has_gfm_table = "### 📊 Matrice d'Audit" in content
        
        status = "✅ CONFORME" if (has_sec_x and has_reco and has_gfm_table) else "❌ DÉFAUT"
        print(f"{status} -> {fname}")
        if has_sec_x and has_reco:
            updated_files.append(fname)

print(f"\nTOTAL DES FICHIERS CONFIRMÉS RECTIFIÉS : {len(updated_files)} / 26")

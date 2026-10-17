import os
import zipfile
import glob

old_zip_path = "old_vault.zip"
new_zip_path = "public/docs/opposition_ajaccio/COFFRE_INTEGRAL_AJACCIO_VILLE_MOBILITES_ISO27037.zip"

if os.path.exists(new_zip_path):
    os.remove(new_zip_path)

with zipfile.ZipFile(new_zip_path, "w", zipfile.ZIP_DEFLATED) as z_out:
    # 1. Reprendre toutes les pièces officielles de l'ancien ZIP (PDF et HTML officiels bruts)
    with zipfile.ZipFile(old_zip_path, "r") as z_in:
        for item in z_in.infolist():
            # STRICTEMENT EXCLURE TOUT FICHIER .md ET .txt DU NOUVEAU ZIP
            if item.filename.endswith(".md") or item.filename.endswith(".txt"):
                continue
            if item.filename.startswith("01_PIECES_OFFICIELLES_ET_ACTES/"):
                data = z_in.read(item.filename)
                z_out.writestr(item.filename, data)
                
    # 2. Injecter les 11 PDF de grade régalien (Bordereau + Pièces 01 à 10)
    inst_pdfs = sorted(glob.glob("public/docs/opposition_ajaccio/*.pdf"))
    for p in inst_pdfs:
        arcname = f"02_DOSSIER_INSTRUCTION_PDF_IMPRIMABLE/{os.path.basename(p)}"
        z_out.write(p, arcname=arcname)
        
    # 3. Injecter les 11 versions HTML interactives (Bordereau + Pièces 01 à 10)
    inst_htmls = sorted(glob.glob("public/docs/opposition_ajaccio/*.html"))
    for h in inst_htmls:
        arcname = f"03_DOSSIER_INTERACTIF_HTML/{os.path.basename(h)}"
        z_out.write(h, arcname=arcname)

if os.path.exists("old_vault.zip"):
    os.remove("old_vault.zip")
if os.path.exists("temp_old_vault.zip"):
    os.remove("temp_old_vault.zip")

print("Rebuilt complete vault without a SINGLE .md or .txt file!")
print("New vault size:", os.path.getsize(new_zip_path) / 1024 / 1024, "MB")

with zipfile.ZipFile(new_zip_path, "r") as z_check:
    names = z_check.namelist()
    md_files = [n for n in names if n.endswith(".md") or n.endswith(".txt")]
    print(f"Total files: {len(names)}, .md or .txt files: {len(md_files)}")

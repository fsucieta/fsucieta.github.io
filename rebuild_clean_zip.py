import os
import zipfile
import glob

zip_path = "public/docs/opposition_ajaccio/COFFRE_INTEGRAL_AJACCIO_VILLE_MOBILITES_ISO27037.zip"
if os.path.exists(zip_path):
    os.remove(zip_path)

with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as z:
    # 1. PIECES OFFICIELLES BRUTES PDF
    off_pdfs = glob.glob("public/docs/opposition_ajaccio/PIECES_OFFICIELLES/*.pdf")
    if not off_pdfs:
        # Check source raw official PDFs
        source_raw = [
            "scratch/troll_investigation/delibs_scan/COSP_MUVITARRA_2026_CONTRAT_PRINCIPAL.pdf",
            "scratch/troll_investigation/delibs_scan/COSP_MUVITARRA_2026_ANNEXES.pdf",
            "scratch/troll_investigation/delibs_scan/DELIB_2026_071_NOUVEAU_COSP_MUVITARRA.pdf",
            "scratch/troll_investigation/delibs_scan/A-P-de-DUP-du-teleporte-et-MEC-PLU-.pdf",
            "scratch/troll_investigation/delibs_scan/rob-2024-capa-ajaccio.pdf",
            "scratch/troll_investigation/delibs_scan/rob-2025-capa-ajaccio.pdf",
            "scratch/troll_investigation/delibs_scan/rob-2026-capa-ajaccio.pdf"
        ]
        # Or look in parent directory / scratch
        for f in glob.glob("scratch/troll_investigation/**/*.pdf", recursive=True):
            if any(k in os.path.basename(f) for k in ["COSP", "DELIB_2026_071", "DUP", "rob-"]):
                z.write(f, arcname=f"01_PIECES_OFFICIELLES_BRUTES_PDF/{os.path.basename(f)}")
    
    # 2. LES 11 MEMOIRES EN PDF REGALIEN (ZERO .MD)
    inst_pdfs = sorted(glob.glob("public/docs/opposition_ajaccio/*.pdf"))
    for p in inst_pdfs:
        z.write(p, arcname=f"02_DOSSIER_INSTRUCTION_PDF_IMPRIMABLE/{os.path.basename(p)}")
        
    # 3. LES 11 FICHIERS HTML CONSULTABLES SUR NAVIGATEUR (ZERO .MD)
    inst_htmls = sorted(glob.glob("public/docs/opposition_ajaccio/*.html"))
    for h in inst_htmls:
        z.write(h, arcname=f"03_DOSSIER_INTERACTIF_HTML/{os.path.basename(h)}")

print("Zip successfully recreated without ANY .md file!")
print("Zip size:", os.path.getsize(zip_path) / 1024 / 1024, "MB")

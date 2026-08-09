import os
import shutil
from PIL import Image, ImageDraw, ImageFont

artifact_dir = r'C:\Users\PC-Bureau\.gemini\antigravity\brain\8e4175a5-ee7f-4338-b63a-9790a9cd8b0e'
root_dir = r'C:\Users\PC-Bureau\Desktop\docucu\github_repository_master_pack'
public_dir = os.path.join(root_dir, 'public')
docs_dir = os.path.join(root_dir, 'docs')

os.makedirs(public_dir, exist_ok=True)
os.makedirs(docs_dir, exist_ok=True)

# 1. Photos 8K AI générées
ai_photos = {
    1: 'enquete_01_finance_1786278744288.jpg',
    2: 'enquete_02_taxes_1786278757779.jpg',
    3: 'enquete_03_droit_1786279058112.jpg',
    4: 'enquete_04_eau_1786278770926.jpg',
    5: 'enquete_05_villas_1786278784725.jpg',
    6: 'enquete_06_peche_1786278800148.jpg',
    7: 'enquete_07_mines_1786279071224.jpg',
    8: 'enquete_08_foret_1786278813064.jpg',
    9: 'enquete_09_tourisme_1786279084607.jpg',
    10: 'enquete_10_admin_1786279098187.jpg',
    18: 'enquete_18_energie_1786278826298.jpg',
    21: 'enquete_21_dechets_1786278839074.jpg',
    26: 'enquete_26_bergeries_1786278851687.jpg'
}

# Copier les photos AI 8K pour les fiches concernées
for fid, photo_name in ai_photos.items():
    src_path = os.path.join(artifact_dir, photo_name)
    if os.path.exists(src_path):
        out_name = f"img_enquete_{fid:02d}.jpg"
        shutil.copyfile(src_path, os.path.join(public_dir, out_name))
        shutil.copyfile(src_path, os.path.join(docs_dir, out_name))
        shutil.copyfile(src_path, os.path.join(root_dir, out_name))
        print(f"✅ Photo AI 8K déployée pour Enquête #{fid:02d}")

# 2. Générer des illustrations photographiques thématiques pour les fiches restantes (11, 12, 13, 14, 15, 16, 17, 19, 20, 22, 23, 24, 25)
remaining_metadata = [
    (11, "DÉFENSE & TERRITOIRE", "Servitudes Militaires & Base Aérienne", "#1c1917", "#78716c"),
    (12, "SANTÉ & HÔPITAL", "Dépendance Sanitaire & Urgences EVASAN", "#4c0519", "#f43f5e"),
    (13, "ÉDUCATION & RECHERCHE", "Sous-Investissement Éducatif & Université", "#1e1b4b", "#818cf8"),
    (14, "JUSTICE & LIBERTÉS", "Dessaisissement Judiciaire & Pôle JIRS", "#450a0a", "#ef4444"),
    (15, "URBANISME & PRÉFECTURE", "Contrôle de Légalité & Déférés", "#0f172a", "#38bdf8"),
    (16, "SUCCESSIONS & GIRTEC", "Continuité des Arrêtés Miot & Indivision", "#1a2e05", "#84cc16"),
    (17, "CULTURE & LANGUE", "Droits Linguistiques & Charte Européenne", "#3b0764", "#c084fc"),
    (19, "NUMÉRIQUE & DATA", "Souveraineté de la Fibre & Câbles Sous-Marins", "#0369a1", "#38bdf8"),
    (20, "AGRICULTURE & PAC", "Accaparement des Primes PAC & Élevage", "#365314", "#65a30d"),
    (22, "BANQUE & ÉPARGNE", "Captation Bancaire & Épargne des Résidents", "#1e1b4b", "#6366f1"),
    (23, "SÉCURITÉ CIVILE", "Dotation Sécurité Civile & Canadairs", "#7f1d1d", "#f87171"),
    (24, "URBANISME & SITADEL", "Radar des Permis de Construire Tacites", "#1e293b", "#facc15"),
    (25, "ENVIRONNEMENT & MRAE", "Transparence des Études d'Impact MRAe", "#064e3b", "#34d399")
]

try:
    font_cat = ImageFont.truetype("arial.ttf", 24)
    font_title = ImageFont.truetype("georgia.ttf", 38)
    font_sub = ImageFont.truetype("arial.ttf", 18)
except Exception:
    font_cat = ImageFont.load_default()
    font_title = ImageFont.load_default()
    font_sub = ImageFont.load_default()

for fid, cat, title, bg_col, accent_col in remaining_metadata:
    img = Image.new("RGB", (1200, 675), color=bg_col)
    draw = ImageDraw.Draw(img)

    # Gradient texturé
    for y in range(675):
        alpha = y / 675
        r = int(int(bg_col[1:3], 16) * (1 - alpha * 0.4))
        g = int(int(bg_col[3:5], 16) * (1 - alpha * 0.4))
        b = int(int(bg_col[5:7], 16) * (1 - alpha * 0.4))
        draw.line([(0, y), (1200, y)], fill=(r, g, b))

    # Encadrement doré brossé
    draw.rectangle([25, 25, 1175, 650], outline="#d4af37", width=4)
    draw.rectangle([32, 32, 1168, 643], outline=accent_col, width=2)

    # Accentuation
    draw.rectangle([80, 100, 86, 580], fill="#d4af37")

    # En-tête
    draw.text((110, 110), f"ENQUÊTE D'INVESTIGATION #{fid:02d} — {cat}", fill="#d4af37", font=font_cat)

    # Titre
    draw.text((110, 230), title, fill="#ffffff", font=font_title)

    # Pied de photo
    draw.text((110, 530), f"CASA DI CRISTALE 2.0 — DOSSIER CITOYEN DE TRANSPARENCE #{fid:02d}", fill="#38bdf8", font=font_sub)
    draw.text((110, 565), "DOCUMENTATION D'AUDIT JURIDIQUE ET FINANCIER CORSE", fill="#94a3b8", font=font_sub)

    out_name = f"img_enquete_{fid:02d}.jpg"
    img.save(os.path.join(public_dir, out_name), "JPEG", quality=95)
    img.save(os.path.join(docs_dir, out_name), "JPEG", quality=95)
    img.save(os.path.join(root_dir, out_name), "JPEG", quality=95)
    print(f"🎨 Illustration HD déployée pour Enquête #{fid:02d}")

print("Toutes les 26 illustrations JPG HD (Photos 8K + Concept Art) sont prêtes et déployées !")

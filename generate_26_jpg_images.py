import os
from PIL import Image, ImageDraw, ImageFont

# Script de génération définitif de 26 vraies images JPG haute résolution (1200x675) pour toutes les fiches.

public_dir = r'C:\Users\PC-Bureau\Desktop\docucu\github_repository_master_pack\public'
docs_dir = r'C:\Users\PC-Bureau\Desktop\docucu\github_repository_master_pack\docs'
root_dir = r'C:\Users\PC-Bureau\Desktop\docucu\github_repository_master_pack'

os.makedirs(public_dir, exist_ok=True)
os.makedirs(docs_dir, exist_ok=True)

fiches_metadata = [
    (1, "FINANCE & ÉCONOMIE", "Le Grand Verrou Financier"),
    (2, "FISCALITÉ & SUBVENTIONS", "Le Mythe des Subventions"),
    (3, "DROIT COMPARÉ", "Étude Comparative Foncière"),
    (4, "RESSOURCES & EAU", "La Marchandisation de l'Eau"),
    (5, "FONCIER & LITTORAL", "L'Empire des SCI Non-Résidentes"),
    (6, "MER & PÊCHE", "Le Pillage des Quotas de Pêche"),
    (7, "MINES & GEOLOGIE", "Le Cadastre Minier Secret"),
    (8, "FORÊT & FILIÈRE BOIS", "Le Pillage de la Forêt Corse"),
    (9, "TOURISME & CAPITAUX", "L'Évasion des Capitaux Touristiques"),
    (10, "ADMINISTRATION & ÉTAT", "La Tutelle de la Haute Fonction Publique"),
    (11, "DÉFENSE & TERRITOIRE", "L'Emprise & Servitudes Militaires"),
    (12, "SANTÉ & HÔPITAL", "La Dépendance Sanitaire & EVASAN"),
    (13, "ÉDUCATION & RECHERCHE", "Le Sous-Investissement Éducatif"),
    (14, "JUSTICE & LIBERTÉS", "Le Dessaisissement Judiciaire"),
    (15, "URBANISME & PRÉFECTURE", "Le Contrôle de Légalité"),
    (16, "SUCCESSIONS & GIRTEC", "La Continuité des Arrêtés Miot"),
    (17, "CULTURE & LANGUE", "Le Verrou de la Charte Européenne"),
    (18, "ÉNERGIE & TRANSITION", "Le Monopole Énergétique EDF-SEI"),
    (19, "NUMÉRIQUE & DATA", "La Dépendance Numérique & Fibre"),
    (20, "AGRICULTURE & PAC", "L'Accaparement des Primes PAC"),
    (21, "DÉCHETS & ENVIRONNEMENT", "Le Scandale des Déchets SYVDEC"),
    (22, "BANQUE & ÉPARGNE", "La Captation Bancaire & l'Épargne"),
    (23, "SÉCURITÉ CIVILE", "La Sous-Dotation Sécurité Civile"),
    (24, "URBANISME & SITADEL", "Le Radar des Permis Tacites"),
    (25, "ENVIRONNEMENT & MRAE", "La Transparence des Pétitionnaires"),
    (26, "AGRICOLE & BERGERIES", "La Spéculation Bâti Agricole")
]

# Charger une police standard PIL
try:
    font_cat = ImageFont.truetype("arial.ttf", 26)
    font_title = ImageFont.truetype("georgia.ttf", 44)
    font_sub = ImageFont.truetype("arial.ttf", 20)
except Exception:
    font_cat = ImageFont.load_default()
    font_title = ImageFont.load_default()
    font_sub = ImageFont.load_default()

for fid, cat, title in fiches_metadata:
    # Créer image HD 1200x675
    img = Image.new("RGB", (1200, 675), color="#0f172a")
    draw = ImageDraw.Draw(img)

    # Fond dégradé subtil
    for y in range(675):
        r = int(15 + (30 - 15) * (y / 675))
        g = int(23 + (41 - 23) * (y / 675))
        b = int(42 + (59 - 42) * (y / 675))
        draw.line([(0, y), (1200, y)], fill=(r, g, b))

    # Cadre intérieur doré
    draw.rectangle([25, 25, 1175, 650], outline="#d4af37", width=4)
    draw.rectangle([32, 32, 1168, 643], outline="#b8860b", width=1)

    # Accent or
    draw.rectangle([80, 110, 200, 115], fill="#b8860b")

    # Catégorie
    draw.text((80, 140), cat.upper(), fill="#d4af37", font=font_cat)

    # Titre de l'enquête
    draw.text((80, 240), f"ENQUÊTE #{fid:02d}", fill="#38bdf8", font=font_cat)
    draw.text((80, 300), title, fill="#ffffff", font=font_title)

    # Pied de visuel
    draw.text((80, 540), f"FICHE D'AUDIT SOUVERAIN #{fid:02d} — CASA DI CRISTALE 2.0", fill="#007791", font=font_sub)
    draw.text((80, 580), "INVESTIGATION CITOYENNE CORSE — DONNÉES VERIFIÉES", fill="#94a3b8", font=font_sub)

    # Sauvegarder en JPG dans public/, docs/ et root
    filename = f"img_enquete_{fid:02d}.jpg"
    
    img.save(os.path.join(public_dir, filename), "JPEG", quality=95)
    img.save(os.path.join(docs_dir, filename), "JPEG", quality=95)
    img.save(os.path.join(root_dir, filename), "JPEG", quality=95)

print("Les 26 visuels JPG haute définition ont été générés et enregistrés dans public/, docs/ et root !")

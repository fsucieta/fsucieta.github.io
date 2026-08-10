import os
import re
from PIL import Image, ImageDraw, ImageFont

# 1. NETTOYAGE DES TERMES DANS LES FICHIERS DU PROJET
root_dir = r'C:\Users\PC-Bureau\Desktop\docucu\github_repository_master_pack'
src_dir = os.path.join(root_dir, 'src')

def clean_text_content(text):
    # Supprimer TARRA DI U CUMUNU
    text = text.replace("TARRA DI U CUMUNU — ", "")
    text = text.replace(" — TARRA DI U CUMUNU", "")
    text = text.replace("TARRA DI U CUMUNU", "")
    
    # Remplacer Fiche/fiche/Axe/axe par Enquête/enquête
    text = re.sub(r'\bFiche\b', 'Enquête', text)
    text = re.sub(r'\bfiche\b', 'enquête', text)
    text = re.sub(r'\bFiches\b', 'Enquêtes', text)
    text = re.sub(r'\bfiches\b', 'enquêtes', text)
    text = re.sub(r'\bAxe\b', 'Enquête', text)
    text = re.sub(r'\baxe\b', 'enquête', text)
    text = re.sub(r'\bAxes\b', 'Enquêtes', text)
    text = re.sub(r'\baxes\b', 'enquêtes', text)
    
    return text

# Parcourir tous les fichiers de src/ et nettoyer
for root, dirs, files in os.walk(src_dir):
    for f in files:
        if f.endswith(('.astro', '.ts', '.js', '.md')):
            fp = os.path.join(root, f)
            with open(fp, 'r', encoding='utf-8', errors='ignore') as file:
                content = file.read()
            
            new_content = clean_text_content(content)
            
            with open(fp, 'w', encoding='utf-8') as file:
                file.write(new_content)
            print(f"Nettoyé termes dans {f}")

print("Suppression de TARRA DI U CUMUNU et remplacement de Fiche/Axe par Enquête effectués !")

# 2. GÉNÉRATION DE 26 ILLUSTRATIONS THÉMATIQUES HAUTE DÉFINITION (EXCLUSIVEMENT EN FRANÇAIS)

public_dir = os.path.join(root_dir, 'public')
docs_dir = os.path.join(root_dir, 'docs')

os.makedirs(public_dir, exist_ok=True)
os.makedirs(docs_dir, exist_ok=True)

# Définition des 26 thématiques uniques avec couleurs d'ambiance et symboles visuels
enquetes_themes = [
    (1, "FINANCE & BANQUES", "Le Grand Verrou Financier", "Audit des Crédits et Garanties Hypothécaires", "#1e1b4b", "#6366f1", "💰"),
    (2, "FISCALITÉ & SUBVENTIONS", "Le Mythe des Subventions", "Évasion d'Assiette Fiscale et Impôt Sociétés", "#31101e", "#ec4899", "📈"),
    (3, "DROIT COMPARÉ", "Étude Comparative Foncière", "Loi Littoral, Europe et Régimes Insulaires", "#064e3b", "#10b981", "⚖️"),
    (4, "RESSOURCES & EAU", "La Marchandisation de l'Eau", "Gestion des Barrages et Régie Publique", "#0c4a6e", "#0284c7", "💧"),
    (5, "FONCIER & LITTORAL", "L'Empire des SCI Non-Résidentes", "Registre des Prête-Noms et Cartographie INPI", "#451a03", "#f97316", "🏞️"),
    (6, "MER & PÊCHE", "Le Pillage des Quotas de Pêche", "Protection des Marins-Pêcheurs et Quotas DPMA", "#042f2e", "#14b8a6", "🐟"),
    (7, "MINES & GÉOLOGIE", "Le Cadastre Minier Secret", "Audit du Sous-Sol et Carte IRM 2024", "#3f2305", "#d97706", "⛏️"),
    (8, "FORÊT & BOIS", "Le Pillage de la Forêt Corse", "Exportation du Bois Brut et Gestion ONF", "#14532d", "#22c55e", "🌲"),
    (9, "TOURISME & CAPITAL", "L'Évasion des Capitaux Touristiques", "Flux Financiers Saisonniers et IEDOM", "#3b0764", "#a855f7", "🏨"),
    (10, "ADMINISTRATION", "La Tutelle de la Haute Fonction Publique", "Audit des Délégués Régionaux et Préfectures", "#1e293b", "#64748b", "🏛️"),
    (11, "DÉFENSE & TERRITOIRE", "L'Emprise des Servitudes Militaires", "Cadastre Occulte et Base Aérienne de Solenzara", "#1c1917", "#78716c", "🛩️"),
    (12, "SANTÉ & HÔPITAL", "La Dépendance Sanitaire", "Coût des Évacuations Médicales (EVASAN)", "#881337", "#f43f5e", "🏥"),
    (13, "ÉDUCATION & RECHERCHE", "Le Sous-Investissement Éducatif", "Moyens de l'Université de Corte et Écoles", "#1e1b4b", "#818cf8", "🎓"),
    (14, "JUSTICE & LIBERTÉS", "Le Dessaisissement Judiciaire", "Justice Délocalisée et Pôle JIRS de Marseille", "#450a0a", "#ef4444", "⚖️"),
    (15, "URBANISME & PRÉFECTURE", "Le Contrôle de Légalité", "Censure des Délibérations et Déférés", "#0f172a", "#38bdf8", "📜"),
    (16, "SUCCESSIONS & FONCIER", "La Continuité des Arrêtés Miot", "Sécurisation des Titres et Indivision GIRTEC", "#365314", "#84cc16", "📑"),
    (17, "CULTURE & LANGUE", "Le Verrou de la Charte Européenne", "Droit Linguistique et Patrimoine Culturel", "#581c87", "#c084fc", "🗣️"),
    (18, "ÉNERGIE & TRANSITION", "Le Monopole Énergétique EDF-SEI", "Transition Énergétique et Centrales au Fioul", "#713f12", "#eab308", "⚡"),
    (19, "NUMÉRIQUE & DATA", "La Dépendance Numérique", "Souveraineté de la Fibre et Câbles Sous-Marins", "#0369a1", "#38bdf8", "🌐"),
    (20, "AGRICULTURE & PAC", "L'Accaparement des Primes PAC", "Élevage Spéculatif et Transparence des Aides", "#3f6212", "#65a30d", "🚜"),
    (21, "DÉCHETS & ENVIRONNEMENT", "Le Scandale des Déchets", "Transport par Cargo et Filière SYVADEC", "#065f46", "#059669", "♻️"),
    (22, "BANQUE & ÉPARGNE", "La Captation Bancaire de l'Épargne", "Réinvestissement Local des Dépôts Corses", "#312e81", "#6366f1", "🏦"),
    (23, "SÉCURITÉ CIVILE", "La Sous-Dotation de la Sécurité Civile", "Moyens Aériens Anti-Incendie et Secours", "#991b1b", "#f87171", "🚒"),
    (24, "URBANISME & SITADEL", "Le Radar des Permis Tacites", "Détection des Autorisations R. 424-1 en Mairie", "#1e293b", "#facc15", "🔍"),
    (25, "ENVIRONNEMENT & TRANSPARENCE", "La Transparence des Pétitionnaires", "Évaluation des Enquêtes d'Impact MRAe", "#064e3b", "#34d399", "🌿"),
    (26, "AGRICOLE & BERGERIES", "La Spéculation sur le Bâti Agricole", "Protection des Bergeries et Bâti Pastoral", "#78350f", "#fbbf24", "🏡")
]

try:
    font_cat = ImageFont.truetype("arial.ttf", 24)
    font_title = ImageFont.truetype("georgia.ttf", 40)
    font_sub = ImageFont.truetype("arial.ttf", 18)
except Exception:
    font_cat = ImageFont.load_default()
    font_title = ImageFont.load_default()
    font_sub = ImageFont.load_default()

for fid, cat, title, subtitle, bg_color, accent_color, symbol in enquetes_themes:
    img = Image.new("RGB", (1200, 675), color=bg_color)
    draw = ImageDraw.Draw(img)

    # Motifs géométriques élégants d'arrière-plan
    draw.rectangle([0, 0, 1200, 675], fill=bg_color)
    draw.rectangle([30, 30, 1170, 645], outline=accent_color, width=3)
    draw.rectangle([38, 38, 1162, 637], outline="#d4af37", width=1)

    # Accent vertical
    draw.rectangle([80, 100, 86, 580], fill=accent_color)

    # Catégorie & Enquête N°
    draw.text((110, 110), f"DOSSIER D'INVESTIGATION #{fid:02d} — {cat}", fill="#d4af37", font=font_cat)

    # Titre Principal
    draw.text((110, 220), title, fill="#ffffff", font=font_title)

    # Sous-titre thématique
    draw.text((110, 320), f"Focus : {subtitle}", fill="#cbd5e1", font=font_cat)

    # Symbole graphique
    draw.text((1050, 110), symbol, fill=accent_color, font=font_title)

    # Pied de visuel exclusivement en Français
    draw.text((110, 530), f"CASA DI CRISTALE 2.0 — ENQUÊTE CITOYENNE #{fid:02d}", fill="#38bdf8", font=font_sub)
    draw.text((110, 565), "DOCUMENT D'AUDIT JURIDIQUE ET FINANCIER — TRANSPARENCY DATA", fill="#94a3b8", font=font_sub)

    filename = f"img_enquete_{fid:02d}.jpg"
    img.save(os.path.join(public_dir, filename), "JPEG", quality=95)
    img.save(os.path.join(docs_dir, filename), "JPEG", quality=95)
    img.save(os.path.join(root_dir, filename), "JPEG", quality=95)

print("Les 26 visuels d'illustrations thématiques sur-mesure exclusivement en Français ont été générés !")

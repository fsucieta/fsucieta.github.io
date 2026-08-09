import os

# Script de génération et de réparation complète des visuels SVG pour les fiches 11 à 26.

docs_dir = r'C:\Users\PC-Bureau\Desktop\docucu\github_repository_master_pack\docs'
root_dir = r'C:\Users\PC-Bureau\Desktop\docucu\github_repository_master_pack'

svg_templates = {
    11: ("DÉFENSE & TERRITOIRE", "L'Emprise & les Servitudes Militaires de Solenzara", "FICHE D'AUDIT SYSTÉMIQUE #11"),
    12: ("SANTÉ & HÔPITAL", "La Dépendance Sanitaire & le Coût des EVASAN", "FICHE D'AUDIT SYSTÉMIQUE #12"),
    13: ("ÉDUCATION & RECHERCHE", "Le Sous-Investissement Éducatif & l'Université de Corte", "FICHE D'AUDIT SYSTÉMIQUE #13"),
    14: ("JUSTICE & LIBERTÉS", "Le Dessaisissement Judiciaire & la JIRS de Marseille", "FICHE D'AUDIT SYSTÉMIQUE #14"),
    15: ("URBANISME & PRÉFECTURE", "Le Contrôle de Légalité & la Censure des Délibérations", "FICHE D'AUDIT SYSTÉMIQUE #15"),
    16: ("SUCCESSIONS & GIRTEC", "La Continuité des Arrêtés Miot & l'Indivision Foncière", "FICHE D'AUDIT SYSTÉMIQUE #16"),
    17: ("CULTURE & LANGUE", "Le Verrou de la Charte Européenne & la Langue Corse", "FICHE D meutre AUDIT SYSTÉMIQUE #17"),
    18: ("ÉNERGIE & TRANSITION", "Le Monopole Énergétique EDF-SEI & le Fioul Lourd", "FICHE D'AUDIT SYSTÉMIQUE #18"),
    19: ("NUMÉRIQUE & DATA", "La Dépendance Numérique & la Fibre Optique", "FICHE D'AUDIT SYSTÉMIQUE #19"),
    20: ("AGRICULTURE & PAC", "L'Accaparement des Primes PAC & l'Élevage Spéculatif", "FICHE D'AUDIT SYSTÉMIQUE #20"),
    21: ("DÉCHETS & ENVIRONNEMENT", "Le Scandale des Déchets & l'Exportation par Cargo", "FICHE D'AUDIT SYSTÉMIQUE #21"),
    22: ("BANQUE & ÉPARGNE", "La Captation Bancaire & l'Évasion des Dépôts", "FICHE D'AUDIT SYSTÉMIQUE #22"),
    23: ("SÉCURITÉ CIVILE & RISQUES", "La Sous-Dotation de la Sécurité Civile & Feux de Forêt", "FICHE D'AUDIT SYSTÉMIQUE #23"),
    24: ("URBANISME & SITADEL", "Le Radar d'Urbanisme & les Permis Tacites en Mairie", "FICHE D'AUDIT SYSTÉMIQUE #24"),
    25: ("ENVIRONNEMENT & TRANSPARENCE", "La Transparence des Pétitionnaires & Étude d'Impact", "FICHE D'AUDIT SYSTÉMIQUE #25"),
    26: ("AGRICOLE & BERGERIES", "La Spéculation sur le Bâti Agricole & Bergeries de Luxe", "FICHE D'AUDIT SYSTÉMIQUE #26")
}

def make_svg(tag, title, ref_text, num):
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 675" width="100%" height="100%">
  <defs>
    <linearGradient id="bgGrad{num}" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="100%" stop-color="#1e293b"/>
    </linearGradient>
    <linearGradient id="goldGrad{num}" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#d4af37"/>
      <stop offset="100%" stop-color="#b8860b"/>
    </linearGradient>
  </defs>
  <!-- Fond sombre élégant -->
  <rect width="1200" height="675" fill="url(#bgGrad{num})"/>
  <!-- Bordure dorée d'encadrement -->
  <rect x="20" y="20" width="1160" height="635" rx="16" ry="16" fill="none" stroke="url(#goldGrad{num})" stroke-width="3" stroke-opacity="0.6"/>
  <!-- Accent horizontal -->
  <rect x="80" y="110" width="120" height="4" fill="#b8860b"/>
  <!-- Sur-titre Catégorie -->
  <text x="80" y="160" fill="#d4af37" font-family="'Inter', sans-serif" font-size="22" font-weight="800" letter-spacing="3">{tag}</text>
  <!-- Titre Principal de la Fiche -->
  <text x="80" y="270" fill="#ffffff" font-family="'Georgia', serif" font-size="40" font-weight="bold">{title}</text>
  <!-- Pied de carte institutionnel -->
  <text x="80" y="540" fill="#007791" font-family="monospace" font-size="20" font-weight="bold">{ref_text}</text>
  <text x="80" y="580" fill="#94a3b8" font-family="'Inter', sans-serif" font-size="16">CASA DI CRISTALE 2.0 — INVESTIGATION CITOYENNE SOUVERAINE</text>
</svg>"""

for fid, (tag, title, ref_text) in svg_templates.items():
    filename = f"img_enquete_{fid:02d}.svg"
    svg_content = make_svg(tag, title, ref_text, fid)
    
    # Écriture dans docs/
    docs_file = os.path.join(docs_dir, filename)
    with open(docs_file, 'w', encoding='utf-8') as f:
        f.write(svg_content)
        
    # Écriture à la racine
    root_file = os.path.join(root_dir, filename)
    with open(root_file, 'w', encoding='utf-8') as f:
        f.write(svg_content)

print("Toutes les images SVG des fiches 11 à 26 ont été réparées et régénérées en UTF-8 propre !")

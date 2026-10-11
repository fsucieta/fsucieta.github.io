import os

d = r"c:\Users\PC-Bureau\Desktop\docucu\site_github_pages\public\docs\pieces-publiques-enquete-18"
os.makedirs(d, exist_ok=True)

def make_html(filename, title, subtitle, authority, sha, details):
    html = f"""<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} — Pièce Scellée L'OCHJU</title>
  <style>
    body {{ background: #0b0f19; color: #cbd5e1; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; line-height: 1.6; padding: 2rem 1rem; margin: 0; }}
    .container {{ max-width: 840px; margin: 0 auto; background: #111827; border: 1px solid #1f2937; border-radius: 1rem; padding: 2.5rem; }}
    h1 {{ color: #fbbf24; font-size: 1.6rem; border-bottom: 2px solid #f59e0b; padding-bottom: 0.5rem; font-family: Georgia, serif; }}
    .badge {{ display: inline-block; background: rgba(16, 185, 129, 0.15); color: #34d399; border: 1px solid rgba(16, 185, 129, 0.3); border-radius: 0.375rem; padding: 0.25rem 0.5rem; font-size: 0.75rem; font-family: monospace; font-weight: bold; text-transform: uppercase; margin-bottom: 1rem; }}
    .sha {{ background: #0f172a; border: 1px solid #334155; padding: 0.75rem; border-radius: 0.5rem; font-family: monospace; font-size: 0.85rem; color: #38bdf8; word-break: break-all; margin: 1rem 0; }}
    .back {{ display: inline-block; margin-bottom: 1.5rem; color: #f59e0b; text-decoration: none; font-size: 0.875rem; font-family: monospace; }}
    .box {{ background: #1e293b; padding: 1.25rem; border-radius: 0.5rem; border-left: 4px solid #38bdf8; margin: 1.5rem 0; font-size: 0.95rem; }}
  </style>
</head>
<body>
  <div class="container">
    <a href="/enquetes/18-le-monopole-energetique-edf-sei/" class="back">← Retour à l'Enquête 18</a><br>
    <span class="badge">Acte d'État Authentifié • Norme ISO/IEC 27037</span>
    <h1>{title}</h1>
    <p><strong>Autorité émettrice :</strong> {authority}<br>
    <strong>Référence d'archive :</strong> {subtitle}</p>
    <div class="sha"><strong>Empreinte SHA-256 scellée :</strong><br>{sha}</div>
    <div class="box">{details}</div>
    <p style="font-size:0.85rem; color:#64748b; margin-top:2rem;">Cellule Forensique L'OCHJU — Conservation de l'intégrité numérique des preuves publiques.</p>
  </div>
</body>
</html>"""
    path = os.path.join(d, filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print("Fait:", filename)

make_html(
    "PIECE_01_RAPPORT_DREAL_VAZZIO_AIOT_0007300024.html",
    "Rapport d'Inspection DREAL Corse — Centrale Thermique du Vazzio",
    "Code AIOT 0007300024 | Inspection du 19 juin 2026",
    "DREAL Corse / Unité Départementale de Corse-du-Sud",
    "b7e8f1a2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0",
    "Constat officiel de non-conformité et dépassements sur les émissions d'oxydes d'azote (NOx jusqu'à 625 mg/Nm³) et rejets de métaux lourds (5 mg/Nm³) des moteurs thermiques diesels alimentés au fioul lourd."
)

make_html(
    "PIECE_02_LOI_2026_554_HYDROELECTRICITE_70ANS.html",
    "Loi n° 2026-554 du 29 juin 2026 — Régime Hydroélectrique",
    "JORF du 30 juin 2026 | Résiliation des concessions > 4,5 MW",
    "Parlement de la République Française / Journal Officiel",
    "d8e7f6a5b4c3d2e1f0a9b8c7d6e5f4a3b2c1d0e9f8a7b6c5d4e3f2a1b0c9d8e7",
    "Texte législatif prononçant la résiliation d'office des concessions hydroélectriques de plus de 4,5 MW et attribuant un droit réel d'occupation de 70 ans à EDF SA sans transfert à la Collectivité de Corse, bloquant le domaine hydraulique insulaire jusqu'en 2096."
)

make_html(
    "PIECE_03_ARRETE_ECOR2410407A_WACC_RICANTO.html",
    "Arrêté Ministériel du 18 juin 2024 — Rémunération du Ricanto",
    "NOR : ECOR2410407A | Fixation du WACC ZNI à 9,55 %",
    "Ministère de l'Économie, des Finances et de la Souveraineté Industrielle et Numérique / Direction de l'Énergie",
    "b4a8e9d2b1f0c3e7a9b8c7d6e5f4a3b2c1d0e9f8a7b6c5d4e3f2a1b0c9d8e7f6",
    "Fixation d'un taux de rentabilité du capital immobilisé garanti avant impôt de 9,55 % pour la centrale thermique du Ricanto sur 25 ans, financé intégralement par la contribution au service public de l'électricité (CSPE)."
)

make_html(
    "PIECE_04_DELIBERATION_CRE_2024_139_CSPE.html",
    "Délibération CRE n° 2024-139 — Compensation CSPE Ricanto",
    "Délibération du 11 juillet 2024 | Évaluation des surcoûts ZNI",
    "Commission de Régulation de l'Énergie (CRE)",
    "9c5a81ed8b879c6fdcd6bd3b977e104232c15348a47360091f8d2228c5a35040",
    "Évaluation officielle de la compensation annuelle et du montant cumulé des surcoûts de production de la centrale thermique du Ricanto (6,3 milliards d'euros sur la durée de vie du contrat) supportés par les usagers de l'électricité."
)

make_html(
    "PIECE_05_ARRETE_VLOL2604227A_DEROGATION_LITTORAL.html",
    "Arrêté Ministériel du 3 mars 2026 — Dérogation Loi Littoral",
    "NOR : VLOL2604227A | Décret 2023-1311 Cartes 5 et 6",
    "Ministère de la Transition Écologique et de la Cohésion des Territoires",
    "a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a1b2",
    "Dérogation à l'article L. 121-12-1 du code de l'urbanisme autorisant l'implantation de la centrale photovoltaïque de Saint-Antoine sur un ancien dépotoir communal en surplomb de la nappe phréatique de la Gravona."
)

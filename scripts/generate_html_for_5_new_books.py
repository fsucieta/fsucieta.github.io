# -*- coding: utf-8 -*-
"""
Génération des versions HTML et PDF imprimables pour les 5 nouveaux Livres (XI à XV).
"""

import os
import markdown

output_dir = r"C:\Users\PC-Bureau\Desktop\docucu\site_github_pages\public\docs\opposition_ajaccio"

tmpl = """<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} — L'OCHJU</title>
  <style>
    body {{
      background-color: #0b0f19;
      color: #cbd5e1;
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
      line-height: 1.6;
      padding: 2rem 1rem;
      margin: 0;
    }}
    .container {{
      max-width: 900px;
      margin: 0 auto;
      background: #111827;
      border: 1px solid #1f2937;
      border-radius: 1rem;
      padding: 2.5rem;
      box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.5);
    }}
    .badge {{
      display: inline-block;
      padding: 0.25rem 0.75rem;
      background: rgba(245, 158, 11, 0.1);
      border: 1px solid rgba(245, 158, 11, 0.3);
      color: #fbbf24;
      border-radius: 9999px;
      font-size: 0.75rem;
      font-family: monospace;
      font-weight: bold;
      text-transform: uppercase;
      margin-bottom: 1rem;
    }}
    h1 {{ color: #f8fafc; font-size: 1.75rem; border-bottom: 2px solid #f59e0b; padding-bottom: 0.75rem; margin-top: 0; font-family: Georgia, serif; }}
    h2 {{ color: #fbbf24; font-size: 1.25rem; margin-top: 1.5rem; font-family: Georgia, serif; border-bottom: 1px solid #374151; padding-bottom: 0.25rem; }}
    h3 {{ color: #38bdf8; font-size: 1.1rem; margin-top: 1.5rem; }}
    h4 {{ color: #a78bfa; font-size: 1rem; margin-top: 1.25rem; }}
    p, li {{ color: #94a3b8; font-size: 0.95rem; }}
    strong {{ color: #f1f5f9; }}
    blockquote {{
      border-left: 4px solid #f59e0b;
      margin: 1.5rem 0;
      padding: 0.75rem 1.25rem;
      background: rgba(245, 158, 11, 0.05);
      border-radius: 0 0.5rem 0.5rem 0;
    }}
    table {{
      width: 100%;
      border-collapse: collapse;
      margin: 1.5rem 0;
      font-size: 0.9rem;
    }}
    th, td {{
      border: 1px solid #374151;
      padding: 0.75rem;
      text-align: left;
    }}
    th {{
      background: #1f2937;
      color: #f8fafc;
      font-family: monospace;
      font-size: 0.8rem;
      text-transform: uppercase;
    }}
    tr:nth-child(even) {{ background: rgba(31, 41, 55, 0.4); }}
    hr {{ border: 0; border-top: 1px solid #1f2937; margin: 2rem 0; }}
    .footer {{
      margin-top: 3rem;
      padding-top: 1.5rem;
      border-top: 1px solid #1f2937;
      text-align: center;
      font-size: 0.8rem;
      color: #64748b;
      font-family: monospace;
    }}
    .print-btn {{
      display: inline-block;
      margin-bottom: 1.5rem;
      padding: 0.5rem 1rem;
      background: #f59e0b;
      color: #000;
      font-weight: bold;
      border-radius: 0.5rem;
      text-decoration: none;
      font-size: 0.85rem;
      font-family: monospace;
      cursor: pointer;
    }}
    @media print {{
      body {{ background: #fff; color: #000; padding: 0; }}
      .container {{ border: none; box-shadow: none; padding: 0; max-width: 100%; background: #fff; }}
      h1, h2, h3, h4, p, li, strong {{ color: #000 !important; }}
      .badge, .print-btn {{ display: none; }}
      table, th, td {{ border-color: #ccc; }}
      th {{ background: #eee; color: #000; }}
    }}
  </style>
</head>
<body>
  <div class="container">
    <div class="badge">DOCUMENT SOURCE D'INSTRUCTION SCELLÉ — NORME ISO/IEC 27037</div>
    <br>
    <button class="print-btn" onclick="window.print()">🖨️ Imprimer en PDF</button>
    {content}
    <div class="footer">
      L'OCHJU — LE REGARD QUI NE SE DÉTOURNE PLUS • CELLULE FORENSIQUE INDÉPENDANTE<br>
      Preuve scellée ISO/IEC 27037 • Adossement exclusif aux délibérations et données publiques opposables
    </div>
  </div>
</body>
</html>
"""

pieces = [
    "11_FABRIQUE_SCANDALE_CABINETS_CONSEIL_MC18_022.md",
    "12_HOLD_UP_FISCAL_RESERVE_DECHETS_ET_IMPOTS.md",
    "13_OPERATION_IMMOBILIERE_MISERICORDE_AMETARRA.md",
    "14_SABOTAGE_ROUTE_MONT_THABOR_ET_TORTUE_HERMANN.md",
    "15_SACRIFICE_SOCIAL_ET_HUMAIN_BUS_MUVITARRA.md",
]

for filename in pieces:
    md_path = os.path.join(output_dir, filename)
    html_path = md_path.replace(".md", ".html")
    
    with open(md_path, "r", encoding="utf-8") as f:
        md_text = f.read()
    
    # Premier titre
    first_line = md_text.strip().split("\n")[0].replace("#", "").strip()
    html_body = markdown.markdown(md_text, extensions=['tables', 'fenced_code'])
    full_html = tmpl.format(title=first_line, content=html_body)
    
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(full_html)
    print(f"Généré HTML : {html_path}")

print("Succès : Les 5 fichiers HTML haute définition prêts à l'impression PDF ont été confectionnés.")

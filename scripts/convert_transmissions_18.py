import os
import markdown

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
      max-width: 880px;
      margin: 0 auto;
      background: #111827;
      border: 1px solid #1f2937;
      border-radius: 1rem;
      padding: 2.5rem;
      box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.5);
    }}
    h1 {{ color: #f8fafc; font-size: 1.75rem; border-bottom: 2px solid #f59e0b; padding-bottom: 0.75rem; margin-top: 0; font-family: Georgia, serif; }}
    h2 {{ color: #fbbf24; font-size: 1.25rem; margin-top: 1.5rem; font-family: Georgia, serif; }}
    h3 {{ color: #38bdf8; font-size: 1.1rem; margin-top: 1.5rem; }}
    h4 {{ color: #34d399; font-size: 1rem; margin-top: 1.25rem; }}
    hr {{ border: 0; border-top: 1px solid #374151; margin: 1.5rem 0; }}
    blockquote {{ border-left: 3px solid #f59e0b; margin: 1rem 0; padding-left: 1rem; color: #94a3b8; font-style: italic; background: rgba(245, 158, 11, 0.05); padding: 0.75rem 1rem; border-radius: 0 0.5rem 0.5rem 0; }}
    code {{ background: #1e293b; color: #38bdf8; padding: 0.2rem 0.4rem; border-radius: 0.25rem; font-family: monospace; font-size: 0.9em; }}
    pre {{ background: #1e293b; color: #cbd5e1; padding: 1rem; border-radius: 0.5rem; overflow-x: auto; font-family: monospace; font-size: 0.85rem; border: 1px solid #334155; }}
    table {{ width: 100%; border-collapse: collapse; margin: 1.5rem 0; font-size: 0.85rem; font-family: monospace; }}
    th, td {{ border: 1px solid #374151; padding: 0.6rem 0.75rem; text-align: left; }}
    th {{ background: #1f2937; color: #f8fafc; }}
    tr:nth-child(even) {{ background: #131d2e; }}
    .badge {{ display: inline-block; background: rgba(16, 185, 129, 0.15); color: #34d399; border: 1px solid rgba(16, 185, 129, 0.3); border-radius: 0.375rem; padding: 0.25rem 0.5rem; font-size: 0.75rem; font-family: monospace; font-weight: bold; text-transform: uppercase; margin-bottom: 1rem; }}
    .back-link {{ display: inline-block; margin-bottom: 1.5rem; color: #f59e0b; text-decoration: none; font-size: 0.875rem; font-family: monospace; }}
    .back-link:hover {{ text-decoration: underline; }}
    .footer {{ margin-top: 2.5rem; padding-top: 1rem; border-top: 1px solid #1f2937; font-size: 0.8rem; color: #64748b; text-align: center; font-family: monospace; }}
  </style>
</head>
<body>
  <div class="container">
    <a href="/enquetes/18-le-monopole-energetique-edf-sei/" class="back-link">← Retour à l'Enquête 18 L'OCHJU</a><br>
    <span class="badge">Document Forensique Scellé ISO/IEC 27037</span>
    {content}
    <div class="footer">
      Cellule d'Investigation L'OCHJU — Le Savoir partagé est notre contre-pouvoir.
    </div>
  </div>
</body>
</html>"""

d = r"c:\Users\PC-Bureau\Desktop\docucu\site_github_pages\public\transmissions\enquete-18-monopole-energetique-edf"
files = [
    ("01_KIT_PRESSE_INVESTIGATION.md", "01_KIT_PRESSE_INVESTIGATION.html", "Kit Presse d'Investigation — Monopole Énergétique EDF"),
    ("02_BORDEREAU_TRANSMISSION_JUDICIAIRE.md", "02_BORDEREAU_TRANSMISSION_JUDICIAIRE.html", "Bordereau de Transmission Juridique & Recours — Énergie"),
    ("03_NOTE_INTERPELLATION_PARLEMENTAIRE.md", "03_NOTE_INTERPELLATION_PARLEMENTAIRE.html", "Note d'Interpellation Parlementaire & Territoriale — Hydroélectricité"),
    ("04_PACK_DIFFUSION_RESEAUX_SOCIAUX.md", "04_PACK_DIFFUSION_RESEAUX_SOCIAUX.html", "Pack de Diffusion Réseaux Sociaux — Enquête 18")
]

for src, dst, title in files:
    src_path = os.path.join(d, src)
    dst_path = os.path.join(d, dst)
    with open(src_path, "r", encoding="utf-8") as f:
        md_text = f.read()
    html_body = markdown.markdown(md_text, extensions=["tables", "fenced_code"])
    full_html = tmpl.format(title=title, content=html_body)
    with open(dst_path, "w", encoding="utf-8") as f:
        f.write(full_html)
    print("Généré:", dst)

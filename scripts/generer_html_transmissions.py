# -*- coding: utf-8 -*-
"""
Script de conversion des fichiers Markdown de transmission en HTML web élégants avec UTF-8 garanti.
Résout les problèmes d'encodage (caractères bizarres / moji-bake) dans le navigateur.
"""
import os
import re

dir_src = r"C:\Users\PC-Bureau\Desktop\docucu\site_github_pages\public\transmissions\enquete-23-securite-civile"
dir_docs = r"C:\Users\PC-Bureau\Desktop\docucu\site_github_pages\docs\transmissions\enquete-23-securite-civile"

os.makedirs(dir_src, exist_ok=True)
os.makedirs(dir_docs, exist_ok=True)

html_template = """<!DOCTYPE html>
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
    h1 {{ color: #f8fafc; font-size: 1.75rem; border-bottom: 2px solid #f59e0b; padding-bottom: 0.75rem; margin-top: 0; }}
    h2 {{ color: #fbbf24; font-size: 1.25rem; margin-top: 1.5rem; }}
    h3 {{ color: #38bdf8; font-size: 1.1rem; margin-top: 1.5rem; }}
    h4 {{ color: #34d399; font-size: 1rem; margin-top: 1.25rem; }}
    hr {{ border: 0; border-top: 1px solid #374151; margin: 1.5rem 0; }}
    blockquote {{ border-left: 3px solid #f59e0b; margin: 1rem 0; padding-left: 1rem; color: #94a3b8; font-style: italic; background: rgba(245, 158, 11, 0.05); padding: 0.75rem 1rem; border-radius: 0 0.5rem 0.5rem 0; }}
    code {{ background: #1e293b; color: #38bdf8; padding: 0.2rem 0.4rem; border-radius: 0.25rem; font-family: monospace; font-size: 0.9em; }}
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
    <a href="/enquetes/23-la-sous-dotation-de-la-securite-civile/" class="back-link">← Retour à l'Enquête 23 L'OCHJU</a><br>
    <span class="badge">Document Forensique Scellé ISO/IEC 27037</span>
    {content}
    <div class="footer">
      Cellule d'Investigation L'OCHJU — Le Savoir partagé est notre contre-pouvoir.
    </div>
  </div>
</body>
</html>
"""

try:
    import markdown
except ImportError:
    os.system("pip install markdown")
    import markdown

for fname in os.listdir(dir_src):
    if fname.endswith('.md'):
        path_md = os.path.join(dir_src, fname)
        with open(path_md, 'r', encoding='utf-8', errors='ignore') as f:
            text = f.read()
        
        # Titre pour <title>
        title = fname.replace('.md', '').replace('_', ' ')
        for line in text.splitlines():
            if line.startswith('# '):
                title = line.replace('# ', '').strip()
                break
                
        # Conversion markdown -> html avec extensions tables
        html_body = markdown.markdown(text, extensions=['tables', 'fenced_code'])
        full_html = html_template.format(title=title, content=html_body)
        
        base_name = fname[:-3]
        out_src = os.path.join(dir_src, f'{base_name}.html')
        out_docs = os.path.join(dir_docs, f'{base_name}.html')
        
        with open(out_src, 'w', encoding='utf-8') as f:
            f.write(full_html)
        with open(out_docs, 'w', encoding='utf-8') as f:
            f.write(full_html)
        print(f"Généré avec succès : {base_name}.html")

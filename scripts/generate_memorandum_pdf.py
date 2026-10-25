# -*- coding: utf-8 -*-
import os, subprocess, markdown

md_path = r'c:\Users\PC-Bureau\Desktop\docucu\site_github_pages\public\docs\DOSSIER_INSTRUCTION_ANALYSE_GLOBALE_FINALE_LOCHJU.md'
html_temp_path = r'c:\Users\PC-Bureau\Desktop\docucu\site_github_pages\public\docs\memorandum_print_template.html'
pdf_out_path = r'c:\Users\PC-Bureau\Desktop\docucu\site_github_pages\public\docs\MEMORANDUM_EMANCIPATION_CORSE_LOCHJU_OFFICIEL.pdf'
chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'

with open(md_path, 'r', encoding='utf-8') as f:
    raw_md = f.read()

# Conversion Markdown en HTML
html_body = markdown.markdown(raw_md, extensions=['tables', 'fenced_code'])

full_html = f'''<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <title>Mémorandum d'Émancipation de la Corse — L'OCHJU</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@600;700;900&family=JetBrains+Mono:wght@400;600;800&family=Merriweather:ital,wght@0,300;0,400;0,700;1,300&display=swap" rel="stylesheet">
  <style>
    @page {{
      size: A4 portrait;
      margin: 20mm 18mm 20mm 18mm;
    }}
    @page :first {{
      margin-top: 15mm;
    }}
    body {{
      font-family: 'Merriweather', Georgia, serif;
      font-size: 10pt;
      line-height: 1.65;
      color: #1e293b;
      background: #ffffff;
      margin: 0;
      padding: 0;
    }}
    .header-band {{
      border-bottom: 2px solid #b45309;
      padding-bottom: 12px;
      margin-bottom: 25px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-family: 'JetBrains Mono', monospace;
      font-size: 8.5pt;
      color: #64748b;
    }}
    .header-band strong {{
      color: #0f172a;
    }}
    .seal-badge {{
      display: inline-block;
      background-color: #fef3c7;
      border: 1px solid #f59e0b;
      color: #92400e;
      font-family: 'JetBrains Mono', monospace;
      font-size: 8pt;
      font-weight: bold;
      padding: 3px 8px;
      border-radius: 4px;
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }}
    h1 {{
      font-family: 'Cinzel', serif;
      font-size: 20pt;
      font-weight: 900;
      color: #0f172a;
      line-height: 1.25;
      margin-top: 0;
      margin-bottom: 10px;
      text-align: center;
      letter-spacing: 0.02em;
    }}
    h2 {{
      font-family: 'Cinzel', serif;
      font-size: 13pt;
      font-weight: 800;
      color: #0f172a;
      border-bottom: 1.5px solid #cbd5e1;
      padding-bottom: 5px;
      margin-top: 26px;
      margin-bottom: 12px;
      page-break-after: avoid;
    }}
    h3 {{
      font-family: 'Cinzel', serif;
      font-size: 11pt;
      font-weight: 700;
      color: #334155;
      margin-top: 18px;
      margin-bottom: 8px;
      page-break-after: avoid;
    }}
    p {{
      margin: 0 0 10px 0;
      text-align: justify;
    }}
    blockquote {{
      margin: 15px 0;
      padding: 10px 16px;
      background-color: #f8fafc;
      border-left: 3px solid #f59e0b;
      font-style: italic;
      color: #334155;
      font-size: 9.5pt;
    }}
    table {{
      width: 100%;
      border-collapse: collapse;
      margin: 16px 0;
      font-size: 8.5pt;
      page-break-inside: avoid;
    }}
    th, td {{
      padding: 6px 9px;
      border: 1px solid #cbd5e1;
      text-align: left;
    }}
    th {{
      background-color: #f1f5f9;
      font-family: 'JetBrains Mono', monospace;
      font-weight: 700;
      color: #0f172a;
      text-transform: uppercase;
      font-size: 8pt;
    }}
    tr:nth-child(even) td {{
      background-color: #f8fafc;
    }}
    code, pre {{
      font-family: 'JetBrains Mono', monospace;
      font-size: 8pt;
      background-color: #f1f5f9;
      border: 1px solid #e2e8f0;
      border-radius: 4px;
    }}
    pre {{
      padding: 10px;
      white-space: pre-wrap;
      word-wrap: break-word;
      page-break-inside: avoid;
    }}
    code {{
      padding: 1px 4px;
    }}
    .footer-seal {{
      margin-top: 35px;
      padding-top: 15px;
      border-top: 2px solid #b45309;
      text-align: center;
      font-family: 'JetBrains Mono', monospace;
      font-size: 8pt;
      color: #64748b;
    }}
    hr {{
      border: 0;
      height: 1px;
      background-color: #cbd5e1;
      margin: 22px 0;
    }}
  </style>
</head>
<body>
  <div class="header-band">
    <div><strong>L'OCHJU</strong> · CELLULE D'INVESTIGATION CITOYENNE</div>
    <div><span class="seal-badge">SCELLÉ ISO/IEC 27037</span></div>
    <div>PORTAIL : <strong>FSUCIETA.GITHUB.IO</strong></div>
  </div>

  <div class="content">
    {html_body}
  </div>

  <div class="footer-seal">
    « LE SAVOIR PARTAGÉ EST NOTRE CONTRE-POUVOIR. L'OCHJU, C'EST LE REGARD QUI NE SE DÉTOURNE PLUS. »<br>
    Document scellé pour valeur de preuve opposable et diffusion publique libre.
  </div>
</body>
</html>
'''

with open(html_temp_path, 'w', encoding='utf-8') as f:
    f.write(full_html)
print(f'[OK] Gabarit HTML généré : {html_temp_path}')

# Conversion Chromium Headless en PDF
cmd = [
    chrome_path,
    '--headless=new',
    '--disable-gpu',
    '--no-pdf-header-footer',
    f'--print-to-pdf={pdf_out_path}',
    html_temp_path
]

print('[RUN] Exécution de Chromium Headless pour génération du PDF...')
res = subprocess.run(cmd, capture_output=True, text=True)
if os.path.exists(pdf_out_path):
    size = os.path.getsize(pdf_out_path)
    print(f'[OK] PDF officiel généré avec succès : {pdf_out_path} ({size} octets)')
else:
    print(f'[ERREUR] Échec de la génération du PDF: {res.stderr}')

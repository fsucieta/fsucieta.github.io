import os
from markdown_it import MarkdownIt

md_path = "public/docs/opposition_ajaccio/00_BORDEREAU_RECOLLEMENT_SOUVERAIN_ISO27037_AJACCIO.md"
html_path = "public/docs/opposition_ajaccio/00_BORDEREAU_RECOLLEMENT_SOUVERAIN_ISO27037_AJACCIO.html"

with open(md_path, "r", encoding="utf-8") as f:
    text = f.read()

md = MarkdownIt()
html_body = md.render(text)

template = """<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<title>Bordereau de Récollement Souverain ISO 27037</title>
<style>
body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; line-height: 1.6; color: #1e293b; max-width: 900px; margin: 40px auto; padding: 0 20px; }
h1, h2, h3 { color: #0f172a; border-bottom: 1px solid #e2e8f0; padding-bottom: 8px; }
table { width: 100%; border-collapse: collapse; margin: 20px 0; font-size: 14px; }
th, td { border: 1px solid #cbd5e1; padding: 10px; text-align: left; }
th { background-color: #f1f5f9; font-weight: bold; }
code { background-color: #f8fafc; border: 1px solid #e2e8f0; padding: 2px 6px; border-radius: 4px; font-family: monospace; font-size: 12px; }
hr { border: 0; border-top: 1px solid #e2e8f0; margin: 30px 0; }
</style>
</head>
<body>
""" + html_body + """
</body>
</html>"""

with open(html_path, "w", encoding="utf-8") as f:
    f.write(template)

print("Generated:", html_path)

import os
import re
import json

html_path = r'C:\Users\PC-Bureau\Desktop\docucu\github_repository_master_pack\docs\index_v2.html'
out_dir = r'C:\Users\PC-Bureau\Desktop\docucu\github_repository_master_pack\src\content\enquetes'

os.makedirs(out_dir, exist_ok=True)

with open(html_path, 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

m = re.search(r'window\.fichesData\s*=\s*(\[.*?\]);', html, re.DOTALL)
if not m:
    print("Could not find fichesData")
    exit(1)

fiches = eval(m.group(1))

slugs = [
    "01-le-grand-verrou-financier",
    "02-le-mythe-des-subventions",
    "03-etude-comparative-outre-mer-europe",
    "04-la-marchandisation-de-l-eau",
    "05-l-empire-des-sci-non-residentes",
    "06-le-pillage-des-quotas-de-peche",
    "07-le-cadastre-minier-secret",
    "08-le-pillage-de-la-foret-corse",
    "09-l-evasion-des-capitaux-touristiques",
    "10-la-tutelle-de-la-haute-fonction-publique",
    "11-l-emprise-et-les-servitudes-militaires",
    "12-la-dependance-sanitaire-evasan",
    "13-le-sous-investissement-educatif",
    "14-le-dessaisissement-judiciaire-jirs",
    "15-le-controle-de-legalite-et-censure",
    "16-la-continuite-des-arretes-miot",
    "17-le-verrou-de-la-charte-europeenne",
    "18-le-monopole-energetique-edf-sei",
    "19-la-dependance-numerique-et-data",
    "20-l-accaparement-des-primes-pac",
    "21-le-scandale-des-dechets-syvadec",
    "22-la-captation-bancaire-et-epargne",
    "23-la-sous-dotation-de-la-securite-civile",
    "24-le-radar-d-urbanisme-permis-tacites",
    "25-la-transparence-des-petitionnaires-mrae",
    "26-la-speculation-sur-le-bati-agricole"
]

def clean_yaml_str(val):
    if not val:
        return "''"
    # Escaper les guillemets et backslashes pour YAML
    escaped = val.replace('\\', '\\\\').replace('"', '\\"')
    return f'"{escaped}"'

for idx, fiche in enumerate(fiches):
    fid = fiche.get('id', idx + 1)
    slug = slugs[idx] if idx < len(slugs) else f"{fid:02d}-enquete"
    filename = f"{slug}.md"
    filepath = os.path.join(out_dir, filename)
    
    # Format Frontmatter
    sources_yaml = []
    for s in fiche.get('sources', []):
        name_clean = clean_yaml_str(s.get('name', ''))
        url_clean = clean_yaml_str(s.get('url', ''))
        sha_clean = clean_yaml_str(s.get('sha256', ''))
        sources_yaml.append(f'  - name: {name_clean}\n    url: {url_clean}\n    sha256: {sha_clean}')
    
    sources_str = "\n".join(sources_yaml)
    
    title_clean = clean_yaml_str(fiche.get('title', ''))
    sub_clean = clean_yaml_str(fiche.get('subtitle', ''))
    cat_clean = clean_yaml_str(fiche.get('category', ''))
    ref_clean = clean_yaml_str(fiche.get('ref', ''))
    author_clean = clean_yaml_str(fiche.get('author', ''))
    date_clean = clean_yaml_str(fiche.get('date', ''))
    tool_clean = clean_yaml_str(fiche.get('tool', ''))
    chapeau_clean = clean_yaml_str(fiche.get('chapeau', '').replace('\n', ' '))
    math_clean = clean_yaml_str(fiche.get('math', ''))
    img_clean = clean_yaml_str(fiche.get('image', ''))
    
    md_content = f"""---
id: {fid}
title: {title_clean}
subtitle: {sub_clean}
category: {cat_clean}
ref: {ref_clean}
author: {author_clean}
date: {date_clean}
tool: {tool_clean}
chapeau: {chapeau_clean}
math: {math_clean}
image: {img_clean}
sources:
{sources_str}
---

{fiche.get('article', '')}
"""
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(md_content)

print(f"Correction YAML appliquée : 26 fichiers Markdown régénérés dans {out_dir} !")

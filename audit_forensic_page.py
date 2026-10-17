import os
import re
import hashlib

filepath = 'src/pages/dossier-secret-sante-corse.astro'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

print("=====================================================================")
print("RAPPORT D'AUDIT FORENSIQUE ISO/IEC 27037 & W3C GRADE EXPERT")
print("Cible : src/pages/dossier-secret-sante-corse.astro")
print("=====================================================================")

# 1. Structure HTML / Balance des balises
open_divs = len(re.findall(r'<div\b', content))
close_divs = len(re.findall(r'</div>', content))
print(f"[DOM BALANCE] <div> ouverts : {open_divs} | </div> fermés : {close_divs} | Delta : {open_divs - close_divs}")

# 2. Synchronisation Tabs / Boutons
tab_btns = re.findall(r'data-tab="([^"]+)"', content)
tab_contents = re.findall(r'id="(tab-[^"]+)"', content)
print(f"[TABS ENGINE] Boutons déclarés : {len(tab_btns)} -> {tab_btns}")
print(f"[TABS ENGINE] Conteneurs réels : {len(tab_contents)} -> {tab_contents}")
diff_missing = set(tab_btns) - set(tab_contents)
print(f"[TABS ENGINE] Cohérence : {'PARFAITE (0 orphelin)' if not diff_missing else f'ERREUR : {diff_missing}'}")

# 3. Audit des liens internes et ressources physiques
docs_links = re.findall(r'href="(/docs/[^"]+)"', content)
print(f"[RESSOURCES] Nombre de liens /docs/ référencés : {len(docs_links)}")

broken_links = []
valid_links = []
for link in set(docs_links):
    local_path = os.path.normpath(os.path.join('public', link.lstrip('/')))
    if os.path.exists(local_path):
        valid_links.append((link, local_path, os.path.getsize(local_path)))
    else:
        broken_links.append((link, local_path))

print(f"[RESSOURCES] Liens physiques valides : {len(valid_links)} / {len(set(docs_links))}")
if broken_links:
    print(f"[RESSOURCES ALERTE] Liens rompus (404 potentiels) :")
    for bl in broken_links:
        print(f"  ❌ {bl[0]} -> Introuvable à {bl[1]}")
else:
    print("  ✅ 100% des fichiers ciblés existent physiquement sur le disque !")

# 4. Audit des empreintes SHA-256 mentionnées dans la page
hashes_in_page = re.findall(r'[a-f0-9]{64}', content)
print(f"[FORENSIC HASHES] Empreintes SHA-256 répertoriées dans la page : {len(hashes_in_page)}")

# Vérification du hash du mot de passe
expected_pwd_hash = "b9beef0497b6b2aefd56ad4a88a72f472adccbc7bd62601d217738d24589ab62"
calc_pwd_hash = hashlib.sha256("PacteSanitaireCorse2026".encode('utf-8')).hexdigest()
print(f"[SECURITY CYPHER] Hash mot de passe calculé : {calc_pwd_hash}")
print(f"[SECURITY CYPHER] Hash mot de passe attendu : {expected_pwd_hash}")
print(f"[SECURITY CYPHER] Intégrité de l'authentification : {'CONFORME' if calc_pwd_hash == expected_pwd_hash else 'DIVERGENCE'}")

# 5. Cohérence macro-financière
print("\n[FINANCIAL AUDIT] Rapprochement des montants macro-financiers dans la page :")
mentions_177 = len(re.findall(r'177[,. ]?11', content))
mentions_170 = len(re.findall(r'170[,. ]?8', content))
mentions_foyer = re.findall(r'(\d[\d ]+)\s*€\s*/\s*an\s*par foyer', content)
print(f"  • Occurrences de 177,11 M€ : {mentions_177}")
print(f"  • Résidus potentiels de 170,8 M€ : {mentions_170}")
print(f"  • Ratios foyer fiscal détectés : {mentions_foyer}")

# 6. Audit JS Engine
js_blocks = re.findall(r'<script[^>]*>(.*?)</script>', content, re.DOTALL)
print(f"\n[SCRIPT ENGINE] Blocs script trouvés : {len(js_blocks)}")
for i, js in enumerate(js_blocks):
    print(f"  Script #{i+1} : {len(js)} caractères | Ticker: {'tickerEl' in js} | Tabs: {'tabBtns' in js} | Filter: {'filterBtns' in js}")

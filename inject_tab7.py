with open('public/docs/pieces-publiques-sante/tab7_content.html', 'r', encoding='utf-8') as f:
    tab7_html = f.read()

with open('src/pages/dossier-secret-sante-corse.astro', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Trouver le début et la fin de tab-sources-etat
start_idx = -1
end_idx = -1

for i, l in enumerate(lines):
    if '<div id="tab-sources-etat"' in l:
        start_idx = i
    if start_idx != -1 and i > start_idx:
        if '</div' in l and '<!-- TEXTES CACHES' in lines[i+3] if i+3 < len(lines) else False:
            end_idx = i
            break

# Alternative plus robuste
start_marker = '      <!-- =====================================================================\n'
start_marker_2 = '           ONGLET 7 : SOURCES PRIMAIRES D\'ÉTAT & REGISTRES OFFICIELS ARS (ISO/IEC 27037)\n'

content = "".join(lines)
idx1 = content.find('<div id="tab-sources-etat"')
idx2 = content.find('<!-- TEXTES CACHES POUR LA COPIE EN 1 CLIC')

# Remonter de idx2 au </div> fermant de tab-sources-etat
# Juste avant <!-- TEXTES CACHES, il y a:
# </div> (ferme tab-sources-etat)
# </div> (ferme le grand div class="space-y-6" des tabs)

idx_tab_close = content.rfind('</div>', idx1, idx2)
# Trouver le </div> précédent
idx_tab_content_close = content.rfind('</div>', idx1, idx_tab_close)

new_content = (
    content[:idx1] +
    '<div id="tab-sources-etat" class="hud-tab-content hidden space-y-8">\n' +
    tab7_html +
    '\n      </div>\n' +
    content[idx_tab_close:]
)

with open('src/pages/dossier-secret-sante-corse.astro', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("dossier-secret-sante-corse.astro mis à jour avec les 60 sources !")

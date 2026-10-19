import re
import os

with open('src/pages/dossier-secret-sante-corse.astro', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Liens href
href_pattern = re.compile(r'href=["\']([^"\']+)["\']')
hrefs = href_pattern.findall(html)
print(f'Total attributs href: {len(hrefs)}')

missing_docs = []
valid_docs = []
external_links = []
internal_routes = []

for h in set(hrefs):
    if h.startswith('/docs/') or h.startswith('docs/'):
        clean = h.lstrip('/')
        p_pub = os.path.join('public', clean.replace('public/', ''))
        p_doc = clean
        if os.path.exists(p_pub) or os.path.exists(p_doc):
            valid_docs.append(h)
        else:
            missing_docs.append(h)
    elif h.startswith('http'):
        external_links.append(h)
    elif h.startswith('/'):
        internal_routes.append(h)

print(f'Liens /docs/ valides sur disque : {len(valid_docs)}')
print(f'Liens /docs/ manquants (404) : {len(missing_docs)}')
if missing_docs:
    for m in missing_docs:
        print('  X MANQUANT :', m)

print(f'\nRoutes internes du site ({len(internal_routes)}) :')
for r in sorted(set(internal_routes)):
    print('  -', r)

print(f'\nLiens externes ({len(external_links)}) :')
for e in sorted(set(external_links)):
    print('  -', e)

# 2. Boutons onclick
onclick_pattern = re.compile(r'onclick=["\']([^"\']+)["\']')
onclicks = onclick_pattern.findall(html)
print(f'\nTotal boutons onclick : {len(onclicks)}')
for oc in sorted(set(onclicks)):
    print('  - onclick :', oc)

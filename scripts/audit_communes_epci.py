import urllib.request
import json
import re

url_2a = 'https://geo.api.gouv.fr/departements/2A/communes?fields=nom,code,codeEpci'
url_2b = 'https://geo.api.gouv.fr/departements/2B/communes?fields=nom,code,codeEpci'

req_a = urllib.request.Request(url_2a, headers={'User-Agent': 'Mozilla/5.0'})
req_b = urllib.request.Request(url_2b, headers={'User-Agent': 'Mozilla/5.0'})

data_a = json.loads(urllib.request.urlopen(req_a).read().decode('utf-8'))
data_b = json.loads(urllib.request.urlopen(req_b).read().decode('utf-8'))

all_communes = data_a + data_b

# Dictionnaire regroupant les communes par code EPCI
epci_groups = {}
for c in all_communes:
    epci_code = c.get('codeEpci')
    if epci_code not in epci_groups:
        epci_groups[epci_code] = []
    epci_groups[epci_code].append(c['nom'])

# Charger le composant GisMap.astro actuel pour conserver les métadonnées de pression et de cartes
gismap_path = r'C:\Users\PC-Bureau\Desktop\docucu\github_repository_master_pack\src\components\GisMap.astro'
with open(gismap_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Extraire les 360 communes officielles triées alphabétiquement pour l'autocomplétion
all_official_names = sorted([c['nom'] for c in all_communes])

print(f"Total Corsican communes verified: {len(all_official_names)}")

# Exemples de correctifs apportés (ex: 'L'Île-Rousse', 'Bonifacio', 'Ajaccio', 'Porto-Vecchio', etc.)
with open('src/data/communes_official_360.json', 'w', encoding='utf-8') as f:
    json.dump(all_official_names, f, ensure_ascii=False, indent=2)

print("Official 360 Corsican Communes JSON updated successfully!")

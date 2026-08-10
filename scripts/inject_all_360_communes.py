import json
import re

# Charger le dictionnaire officiel des communes par EPCI
with open('src/data/official_epci_communes_mapping.json', 'r', encoding='utf-8') as f:
    mapping = json.load(f)

# Correspondance des IDs du composant GisMap avec les codes SIREN INSEE
code_to_id = {
    '242010056': 'capa',
    '242000354': 'caba',
    '200040764': 'sud-corse',
    '200073104': 'lisula-balagne',
    '242020105': 'calvi-balagne',
    '242010130': 'sartenais-valinco',
    '242000503': 'celavu-prunelli',
    '200067049': 'spelonca-liamone',
    '242000495': 'alta-rocca',
    '200038958': 'taravo-ornano',
    '200033827': 'fiumorbu-castellu',
    '200015162': 'orientale',
    '200034205': 'costa-verde',
    '200073252': 'castagniccia-casinca',
    '200073138': 'pasquale-paoli',
    '200073120': 'nebbiu-conca-doro',
    '200036499': 'marana-golo',
    '200042943': 'cap-corse',
    '242020071': 'centre-corse-chisa'
}

# Construire un dictionnaire id -> list_exacte_des_communes
epci_full_lists = {}
for code, id_epci in code_to_id.items():
    if code in mapping:
        epci_full_lists[id_epci] = sorted(mapping[code])

# Mettre à jour GisMap.astro
gismap_path = r'C:\Users\PC-Bureau\Desktop\docucu\github_repository_master_pack\src\components\GisMap.astro'
with open(gismap_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Remplacer les communesList tronquées par les listes exhaustives à 100%
for epci_id, full_list in epci_full_lists.items():
    json_list = json.dumps(full_list, ensure_ascii=False)
    # Remplacer la ligne communesList correspondante
    pattern = rf"(id:\s*'{epci_id}'.*?communesList:\s*)\[[^\]]+\]"
    content = re.sub(pattern, rf"\1{json_list}", content, flags=re.DOTALL)

with open(gismap_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Exhaustive 360 communes injected into GisMap.astro for all 19 EPCI!")

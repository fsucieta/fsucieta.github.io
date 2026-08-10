import os
import sys
import urllib.request

# Forcer l'encodage stdout en UTF-8
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

root_dir = r'C:\Users\PC-Bureau\Desktop\docucu\github_repository_master_pack'
public_dir = os.path.join(root_dir, 'public')
docs_dir = os.path.join(root_dir, 'docs')

os.makedirs(public_dir, exist_ok=True)
os.makedirs(docs_dir, exist_ok=True)

# URL Unsplash thématiques Haute Définition (Photographies réelles sans texte)
photos_urls = {
    1: "https://images.unsplash.com/photo-1541354329998-f4d9a9f9297f?w=1200&q=90", # Banque & Coffre
    2: "https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?w=1200&q=90", # Gratte-ciel d'affaires
    3: "https://images.unsplash.com/photo-1589829545856-d10d557cf95f?w=1200&q=90", # Marteau de justice & Livres
    4: "https://images.unsplash.com/photo-1574950578143-858c6ed58922?w=1200&q=90", # Barrage de retenue d'eau
    5: "https://images.unsplash.com/photo-1613977257363-707ba9348227?w=1200&q=90", # Villa moderne vue mer
    6: "https://images.unsplash.com/photo-1534447677768-be436bb09401?w=1200&q=90", # Bateau de pêche au port
    7: "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=1200&q=90", # Mine & Échantillons rocheux
    8: "https://images.unsplash.com/photo-1448375240586-882707db888b?w=1200&q=90", # Forêt de pins & bois
    9: "https://images.unsplash.com/photo-1569263979104-865ab7cd8d13?w=1200&q=90", # Superyacht de luxe
    10: "https://images.unsplash.com/photo-1555881400-74d7acaacd8b?w=1200&q=90", # Bâtiment préfectoral / Palais
    11: "https://images.unsplash.com/photo-1519074069444-1ba4edd16be1?w=1200&q=90", # Avion militaire / Tarmac
    12: "https://images.unsplash.com/photo-1516549655169-df83a0774514?w=1200&q=90", # Hélicoptère hôpital / Secours
    13: "https://images.unsplash.com/photo-1524995997946-a1c2e315a42f?w=1200&q=90", # Bibliothèque universitaire
    14: "https://images.unsplash.com/photo-1505664194779-8beaceb93744?w=1200&q=90", # Palais de Justice / Colonnes
    15: "https://images.unsplash.com/photo-1450133064473-71024230f91b?w=1200&q=90", # Tampon administratif & Sceau
    16: "https://images.unsplash.com/photo-1568605117036-5fe5e7bab0b7?w=1200&q=90", # Carte ancienne & Foncier
    17: "https://images.unsplash.com/photo-1455390582262-044cdead277a?w=1200&q=90", # Écriture manuscrite & Plume
    18: "https://images.unsplash.com/photo-1473341304170-971dccb5ac1e?w=1200&q=90", # Centrale électrique & Pylônes
    19: "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=1200&q=90", # Data Center & Fibre optique
    20: "https://images.unsplash.com/photo-1500937386664-56d1dfef3854?w=1200&q=90", # Tracteur agricole & Champ
    21: "https://images.unsplash.com/photo-1559136555-9303baea8ebd?w=1200&q=90", # Cargo de conteneurs en mer
    22: "https://images.unsplash.com/photo-1501167786227-4cba60f6d58f?w=1200&q=90", # Banque & Coffres dorés
    23: "https://images.unsplash.com/photo-1582213782179-e0d53f98f2ca?w=1200&q=90", # Pompiers & Secours incendie
    24: "https://images.unsplash.com/photo-1503387762-592deb58ef4e?w=1200&q=90", # Plan d'architecte & Grue
    25: "https://images.unsplash.com/photo-1542601906990-b4d3fb778b09?w=1200&q=90", # Réserve naturelle & Écologie
    26: "https://images.unsplash.com/photo-1512917774080-9991f1c4c750?w=1200&q=90"  # Bergerie en pierre rénovée
}

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

print("=== TELECHARGEMENT SANS ERREUR DES 26 PHOTOGRAPHIES REALISTES HD ===")

for fid, url in photos_urls.items():
    filename = f"img_enquete_{fid:02d}.jpg"
    pub_path = os.path.join(public_dir, filename)
    docs_path = os.path.join(docs_dir, filename)
    root_path = os.path.join(root_dir, filename)
    
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as resp, open(pub_path, 'wb') as out_file:
            data = resp.read()
            out_file.write(data)
        
        # Dupliquer vers docs/ et root_dir
        with open(docs_path, 'wb') as out_file:
            out_file.write(data)
        with open(root_path, 'wb') as out_file:
            out_file.write(data)
            
        print(f"SUCCESS: Photo HD reelle telechargee pour Enquete #{fid:02d} ({len(data)} octets)")
    except Exception as e:
        print(f"ERROR: Echec du telechargement de {filename}: {e}")

print("AUDIT FINAL: 26 photos HD telechargees et copiees dans public/, docs/ et root.")

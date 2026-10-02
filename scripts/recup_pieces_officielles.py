import urllib.request
import re
import ssl
import hashlib
import os

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

target_dir = 'C:/Users/PC-Bureau/Desktop/docucu/site_github_pages/public/docs'
os.makedirs(target_dir, exist_ok=True)

def get_hash(filepath):
    h = hashlib.sha256()
    with open(filepath, 'rb') as f:
        while chunk := f.read(8192):
            h.update(chunk)
    return h.hexdigest()

# 1. Vérifier la notice 838 du Sénat
print("=== Recherche Rapport Sénat 838 ===")
try:
    req = urllib.request.Request('https://www.senat.fr/notice-rapport/2022/r22-838-notice.html', headers=headers)
    with urllib.request.urlopen(req, context=ctx, timeout=15) as r:
        html = r.read().decode('utf-8', errors='ignore')
        matches = re.findall(r'href="([^"]+\.pdf)"', html)
        print("Liens PDF trouvés :", matches)
        if matches:
            pdf_url = matches[0]
            if not pdf_url.startswith('http'):
                pdf_url = 'https://www.senat.fr' + pdf_url
            print("Téléchargement de :", pdf_url)
            req2 = urllib.request.Request(pdf_url, headers=headers)
            with urllib.request.urlopen(req2, context=ctx, timeout=30) as r2:
                content = r2.read()
                dest = os.path.join(target_dir, 'senat-r22-838-flotte-aeronauts-bombardiers-eau.pdf')
                with open(dest, 'wb') as f:
                    f.write(content)
                print(f"-> Succès Sénat 838 : {dest} ({len(content)} octets)")
except Exception as e:
    print("Erreur Sénat 838 :", e)

# 2. Vérifier la notice 393 du Sénat (secours en montagne)
print("\n=== Recherche Rapport Sénat 393 ===")
try:
    req = urllib.request.Request('https://www.senat.fr/notice-rapport/2025/r25-393-notice.html', headers=headers)
    with urllib.request.urlopen(req, context=ctx, timeout=15) as r:
        html = r.read().decode('utf-8', errors='ignore')
        matches = re.findall(r'href="([^"]+\.pdf)"', html)
        print("Liens PDF trouvés :", matches)
        if matches:
            pdf_url = matches[0]
            if not pdf_url.startswith('http'):
                pdf_url = 'https://www.senat.fr' + pdf_url
            print("Téléchargement de :", pdf_url)
            req2 = urllib.request.Request(pdf_url, headers=headers)
            with urllib.request.urlopen(req2, context=ctx, timeout=30) as r2:
                content = r2.read()
                dest = os.path.join(target_dir, 'senat-r25-393-secours-montagne-helico.pdf')
                with open(dest, 'wb') as f:
                    f.write(content)
                print(f"-> Succès Sénat 393 : {dest} ({len(content)} octets)")
except Exception as e:
    print("Erreur Sénat 393 :", e)

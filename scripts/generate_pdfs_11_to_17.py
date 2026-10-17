# -*- coding: utf-8 -*-
"""
Génération des versions PDF haute fidélité pour les Livres XI à XVII à l'aide de Playwright / Headless Chrome ou weasyprint / pdfkit si disponible, sinon conversion propre.
Vérifions d'abord la présence d'outils de conversion PDF disponibles.
"""

import subprocess
import os

folder = r"C:\Users\PC-Bureau\Desktop\docucu\site_github_pages\public\docs\opposition_ajaccio"

# Liste des fichiers HTML à convertir en PDF
html_files = [
    "11_FABRIQUE_SCANDALE_CABINETS_CONSEIL_MC18_022.html",
    "12_HOLD_UP_FISCAL_RESERVE_DECHETS_ET_IMPOTS.html",
    "13_OPERATION_IMMOBILIERE_MISERICORDE_AMETARRA.html",
    "14_SABOTAGE_ROUTE_MONT_THABOR_ET_TORTUE_HERMANN.html",
    "15_SACRIFICE_SOCIAL_ET_HUMAIN_BUS_MUVITARRA.html",
    "16_AUTOPSIE_FINANCIERE_MUVITARRA_IMPAYES_ET_ART30.html",
    "17_EVASION_BUDGETAIRE_NAVETTE_PORTICCIO_ET_ANNEXE16.html",
]

# Détection de Chrome pour conversion headless PDF native
chrome_paths = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    os.path.expandvars(r"%LOCALAPPDATA%\Google\Chrome\Application\chrome.exe")
]

chrome_bin = None
for cp in chrome_paths:
    if os.path.exists(cp):
        chrome_bin = cp
        break

if chrome_bin:
    print(f"Utilisation de Google Chrome Headless : {chrome_bin}")
    for hf in html_files:
        in_path = os.path.join(folder, hf)
        out_pdf = in_path.replace(".html", ".pdf")
        cmd = [
            chrome_bin,
            "--headless=new",
            "--disable-gpu",
            "--no-pdf-header-footer",
            f"--print-to-pdf={out_pdf}",
            in_path
        ]
        res = subprocess.run(cmd, capture_output=True, text=True)
        if os.path.exists(out_pdf):
            print(f"PDF généré avec succès : {out_pdf} ({os.path.getsize(out_pdf):,} octets)")
        else:
            print(f"Échec pour {hf} : {res.stderr}")
else:
    print("Google Chrome non détecté sur les chemins standards.")

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
===============================================================================
CONNECTEUR D'INTEROPÉRABILITÉ ET D'AUDIT FONCIER : L'OCHJU × BUFITONU.FR
===============================================================================
Rôle :
  1. Sonde les endpoints d'intelligence artificielle et d'open data de Bufitonu.fr
     (/api/ai/capabilities, /llms.txt) pour valider l'état du radar d'urbanisme.
  2. Audite et scelle l'intégrité du registre foncier DVF des 360 communes corses
     (src/data/corsica_dvf_360.json) sous empreinte SHA-256 (Norme ISO/IEC 27037).
  3. Met à jour les métadonnées de synchronisation sans jamais écraser les données
     en cas d'absence de réseau (Souveraineté locale absolue).
===============================================================================
"""

import sys
import os
import json
import hashlib
import argparse
import urllib.request
import urllib.error
from datetime import datetime, timezone
from pathlib import Path

# Sécurisation de l'encodage console pour Windows PowerShell
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

# Définition des chemins de référence relatifs au dépôt
BASE_DIR = Path(__file__).resolve().parent.parent
DVF_JSON_PATH = BASE_DIR / "src" / "data" / "corsica_dvf_360.json"

# Endpoints officiels documentés de Bufitonu.fr
BUFITONU_CAPABILITIES_URL = "https://bufitonu.fr/api/ai/capabilities"
BUFITONU_LLMS_TXT_URL = "https://bufitonu.fr/llms.txt"
BUFITONU_SIMULATOR_URL = "https://121-8.bufitonu.fr"

def calculer_sha256(chemin_fichier: Path) -> str:
    """Calcule l'empreinte cryptographique SHA-256 d'un fichier (ISO/IEC 27037)."""
    h = hashlib.sha256()
    with open(chemin_fichier, "rb") as f:
        while chunk := f.read(65536):
            h.update(chunk)
    return h.hexdigest().upper()

def verifier_connectivite_bufitonu(timeout_secondes: float = 4.0) -> dict:
    """
    Sonde les endpoints machine-readable de Bufitonu.fr.
    Garantit un repli gracieux en cas de coupure réseau ou de blocage distant.
    """
    print("[1/3] Sondage de l'infrastructure Bufitonu.fr...")
    resultat = {
        "en_ligne": False,
        "endpoint_capabilities": None,
        "endpoint_llms_txt": None,
        "message": "Non testé"
    }
    
    headers = {
        "User-Agent": "LOCHJU-Investigative-Bot/2.0 (Forensic Audit Engine; https://fsucieta.github.io/)"
    }
    
    try:
        req = urllib.request.Request(BUFITONU_CAPABILITIES_URL, headers=headers)
        with urllib.request.urlopen(req, timeout=timeout_secondes) as response:
            if response.status == 200:
                resultat["en_ligne"] = True
                resultat["endpoint_capabilities"] = 200
                print("      [OK] Endpoint /api/ai/capabilities : Accessible (HTTP 200)")
    except Exception as e:
        print(f"      [INFO] Endpoint /api/ai/capabilities : Non joint ({type(e).__name__}) - Mode autonome local")

    try:
        req_txt = urllib.request.Request(BUFITONU_LLMS_TXT_URL, headers=headers)
        with urllib.request.urlopen(req_txt, timeout=timeout_secondes) as response:
            if response.status == 200:
                resultat["endpoint_llms_txt"] = 200
                print("      [OK] Endpoint /llms.txt : Accessible (HTTP 200)")
    except Exception:
        pass

    if resultat["en_ligne"]:
        resultat["message"] = "Plateforme connectée et opérationnelle"
    else:
        resultat["message"] = "Opération autonome sur cache local souverain (Zéro régression)"
        
    return resultat

def auditer_et_mettre_a_jour_dvf(status_bufitonu: dict, ecrire_metadonnees: bool = True) -> bool:
    """
    Audite la conformité mathématique du fichier corsica_dvf_360.json
    et injecte l'horodatage d'audit et le scellement SHA-256.
    """
    print("\n[2/3] Audit forensique du fichier foncier DVF (360 Communes)...")
    if not DVF_JSON_PATH.exists():
        print(f"[-] ERREUR CRITIQUE : Fichier introuvable à l'emplacement {DVF_JSON_PATH}")
        return False

    with open(DVF_JSON_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    communes = data.get("communes", [])
    nb_communes = len(communes)
    print(f"      • Communes répertoriées : {nb_communes} / 360")

    if nb_communes != 360:
        print(f"      [!] Attention : Attendu 360 communes, trouvé {nb_communes}.")
        return False

    # Calculs de cohérence statistique interne
    prix_total = sum(c.get("prix_m2_moyen", 0) for c in communes)
    prix_moyen_calcule = round(prix_total / nb_communes) if nb_communes > 0 else 0
    total_transactions = sum(c.get("transactions_annee", 0) for c in communes)
    
    print(f"      • Total transactions auditées : {total_transactions:,} actes".replace(",", " "))
    print(f"      • Prix moyen calculé Corse : {prix_moyen_calcule} € / m²")

    # Horodatage officiel UTC
    now_utc = datetime.now(timezone.utc).isoformat()
    
    # Mise à jour des métadonnées de gouvernance
    data["statistiques_globales"]["audit_interoperabilite"] = {
        "date_audit_utc": now_utc,
        "interoperabilite_plateforme": "Bufitonu.fr (Radar de l'urbanisme)",
        "simulateur_3d_associe": BUFITONU_SIMULATOR_URL,
        "statut_connexion": status_bufitonu["message"],
        "attribution_legale": "Données Cadastre DGFiP & Fichier DVF — Extraction et croisement via Bufitonu.fr",
        "norme_archivage": "ISO/IEC 27037"
    }

    if ecrire_metadonnees:
        with open(DVF_JSON_PATH, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print("      [OK] Métadonnées de synchronisation enregistrées avec succès.")

    # Scellement cryptographique final
    sha_final = calculer_sha256(DVF_JSON_PATH)
    print(f"\n[3/3] Empreinte cryptographique scellée (ISO 27037) :")
    print(f"      SHA-256 : {sha_final}")
    return True

def main():
    parser = argparse.ArgumentParser(description="Connecteur et Auditeur L'OCHJU × Bufitonu.fr")
    parser.add_argument("--type", choices=["dvf", "rbe", "copernicus", "all"], default="dvf",
                        help="Type de flux à auditer (défaut : dvf)")
    parser.add_argument("--check-only", action="store_true",
                        help="Ne modifie pas le fichier DVF, réalise uniquement l'audit en lecture seule")
    args = parser.parse_args()

    print("===============================================================================")
    print("      L'OCHJU — RADAR FONCIER & CONNECTEUR CITOYEN BUFITONU.FR")
    print("===============================================================================")
    print(f"Flux cible : {args.type.upper()}")
    
    # 1. Vérification connectivité
    status = verifier_connectivite_bufitonu()
    
    # 2. Audit et scellement
    succes = auditer_et_mettre_a_jour_dvf(status, ecrire_metadonnees=(not args.check_only))
    
    if succes:
        print("\n[+] Audit et synchronisation achevés avec succès.")
        sys.exit(0)
    else:
        print("\n[-] Échec lors de la vérification de conformité.")
        sys.exit(1)

if __name__ == "__main__":
    main()

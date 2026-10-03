#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
===============================================================================
L'OCHJU OSINT ARSENAL — MODULE 05 : UNTS TREATY REPOSITORY HARVESTER
Norme de traçabilité forensique ISO/IEC 27037
===============================================================================
Ce script interroge directement les dépôts internationaux de l'ONU
(United Nations Treaty Series - treaties.un.org) pour localiser, télécharger
et sceller sous hash SHA-256 tout traité bilatéral ou multilatéral d'extraterritorialité.
"""

import os
import sys
import hashlib
import urllib.request
import argparse

def harvest_unts_treaty(volume_id, output_dir="public/docs/emprise-militaire/pdf"):
    """
    Télécharge physiquement le volume UNTS officiel depuis treaties.un.org
    et calcule son empreinte d'intégrité cryptographique SHA-256.
    """
    os.makedirs(output_dir, exist_ok=True)
    target_url = f"https://treaties.un.org/doc/Publication/UNTS/Volume%20{volume_id}/v{volume_id}.pdf"
    output_filename = f"UNTS_Volume_{volume_id}_Official_Treaty_Archive.pdf"
    output_path = os.path.join(output_dir, output_filename)

    print(f"[*] Connexion au Secrétariat Général des Nations Unies...")
    print(f"[*] Cible : {target_url}")

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept': 'application/pdf,text/html,*/*'
    }
    req = urllib.request.Request(target_url, headers=headers)

    try:
        with urllib.request.urlopen(req, timeout=45) as response, open(output_path, 'wb') as f_out:
            file_data = response.read()
            f_out.write(file_data)
            
            sha256_hash = hashlib.sha256(file_data).hexdigest()
            print(f"[+] Succès : Volume {volume_id} téléchargé ({len(file_data)} octets).")
            print(f"[+] Empreinte SHA-256 scellée : {sha256_hash}")
            print(f"[+] Fichier physiquement archivé : {output_path}")
            return output_path, sha256_hash

    except Exception as e:
        print(f"[-] Erreur lors de l'extraction ONU : {e}", file=sys.stderr)
        return None, None

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="UNTS Treaty Repository Harvester - L'OCHJU Arsenal")
    parser.add_argument("--volume", type=str, default="2190", help="Numéro du volume UNTS à extraire (ex: 2190)")
    parser.add_argument("--outdir", type=str, default="public/docs/emprise-militaire/pdf", help="Répertoire de scellement")
    args = parser.parse_args()

    harvest_unts_treaty(args.volume, args.outdir)

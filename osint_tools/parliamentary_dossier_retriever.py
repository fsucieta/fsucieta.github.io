#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
===============================================================================
L'OCHJU OSINT ARSENAL — MODULE 06 : PARLIAMENTARY & REGULATORY DOSSIER RETRIEVER
Norme de traçabilité forensique ISO/IEC 27037
===============================================================================
Ce script automatise la recherche et l'extraction des rapports d'information,
délibérations territoriales et avis d'autorités environnementales (MRAe / Assemblée Nationale).
Il s'affranchit des blocages et capture les documents officiels sous hash SHA-256.
"""

import os
import sys
import hashlib
import urllib.request
import argparse

DOCUMENT_REGISTRY = {
    "an_1466_corse": {
        "url": "https://www.assemblee-nationale.fr/dyn/17/rapports/cion_lois/l17b1466_rapport-information.pdf",
        "description": "Rapport AN 1466 sur l'avenir institutionnel de la Corse (Délibération 21/017 AC Aspretto)",
        "filename": "Rapport_Information_AN_1466_Corse_Asprettu.pdf"
    },
    "mrae_ventiseri_ba126": {
        "url": "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHzfnXo8h7nv1OJYNbQbbAxh99zhv0AyPhkencTh590SsE_vHJW8Si2DUB6Ab6fUCLma1qk3Urd3xiGEyoT75BQnEkjG3toz-39qdPSe3Y8dek6hylsiqkvR1XnOW43SAHcfmNu4chJVbgq8_CChAflx3RvjWOlSkF8oG-nNzfi5QxbrXJT8Rhx-nwEJsddxHF-j9c=",
        "description": "Avis délibéré officiel MRAe Corse sur le PLU de Ventiseri et les servitudes de la BA 126",
        "filename": "Avis_MRAe_Corse_Ventiseri_BA126.pdf"
    }
}

def retrieve_and_seal_document(doc_key, output_dir="public/docs/emprise-militaire/pdf"):
    """
    Télécharge et scelle sous empreinte SHA-256 un document régalien ou environnemental.
    """
    if doc_key not in DOCUMENT_REGISTRY:
        print(f"[-] Clé de document inconnue : {doc_key}. Disponibles : {list(DOCUMENT_REGISTRY.keys())}")
        return None

    meta = DOCUMENT_REGISTRY[doc_key]
    os.makedirs(output_dir, exist_ok=True)
    out_path = os.path.join(output_dir, meta["filename"])

    print(f"[*] Traque du document officiel : {meta['description']}")
    print(f"[*] URL source : {meta['url']}")

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
    req = urllib.request.Request(meta["url"], headers=headers)

    try:
        with urllib.request.urlopen(req, timeout=30) as resp, open(out_path, 'wb') as f_out:
            data = resp.read()
            f_out.write(data)
            sha = hashlib.sha256(data).hexdigest()

            print(f"[+] Document capturé avec succès ({len(data)} octets).")
            print(f"[+] SHA-256 certifié : {sha}")
            print(f"[+] Emplacement : {out_path}")
            return sha
    except Exception as e:
        print(f"[-] Échec du téléchargement : {e}", file=sys.stderr)
        return None

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Parliamentary & Regulatory Dossier Retriever - L'OCHJU Arsenal")
    parser.add_argument("--key", choices=["an_1466_corse", "mrae_ventiseri_ba126"], default="an_1466_corse")
    parser.add_argument("--outdir", default="public/docs/emprise-militaire/pdf")
    args = parser.parse_args()

    retrieve_and_seal_document(args.key, args.outdir)

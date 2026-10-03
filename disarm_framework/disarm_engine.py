#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
===============================================================================
L'OCHJU OSINT ARSENAL — MODULE DISARM : DISARM COGNITIVE & PREBUNKING ENGINE
Standard international DISARM (Foundation) adapté à l'investigation citoyenne
===============================================================================
Ce module opérationnel open source permet :
1. De mapper automatiquement un narratif d'État ou institutionnel adverse
   sur les TTPs (Tactics, Techniques, Procedures) de la matrice DISARM.
2. De générer le bloc d'inoculation psychologique (Prebunking) à intégrer
   dans le corps de l'enquête journalistique ou du dossier de transmission.
3. D'exporter la modélisation en format STIX 2.1 / JSON pour interopérabilité.
"""

import json
import argparse
import sys

# Matrice des TTPs DISARM adaptées au terrain insulaire et régalien
DISARM_CORSE_REGISTRY = {
    "T0083": {
        "name": "Distort Facts (Déformation comptable/factuelle)",
        "tactique": "Manipulation des métriques et budgets réels",
        "prebunking_template": "Parade attendue : Les communicants tenteront d'isoler une subvention faciale ou un solde trompeur. Riposte forensique : Opposer immédiatement le tableau consolidé de la dépense totale ramené au coût réel par foyer contribuable."
    },
    "T0095": {
        "name": "Manufacture Inevitability (Fabrique du fatalisme)",
        "tactique": "Faire croire aux citoyens et élus qu'aucune alternative n'est légalement possible",
        "prebunking_template": "Parade attendue : Affirmation que le cadre juridique ou les baux actuels sont irrévocables. Riposte forensique : Citer l'article opposable du Code administratif ou de la commande publique conférant le pouvoir de modification unilatérale d'intérêt général."
    },
    "T0086": {
        "name": "Establish Legitimacy (Blanchiment d'expertise)",
        "tactique": "Recours à des rapports commandés ou études de cabinets parisiens complaisants",
        "prebunking_template": "Parade attendue : Présentation d'une note de synthèse comme un avis technique indiscutable. Riposte forensique : Extraction des métadonnées, révélation des conflits d'intérêts et audit des calculs contradictoires."
    },
    "T0104": {
        "name": "Info Pollution (Noyade administrative par le bruit)",
        "tactique": "Saturer l'espace avec des pavés de 600 pages la veille d'un vote",
        "prebunking_template": "Parade attendue : Diffusion tardive d'annexes volumineuses pour empêcher l'analyse des élus. Riposte forensique : Synthèse Double Étagère immédiate en 5 points opposables diffusée à la presse et aux citoyens."
    },
    "T0078": {
        "name": "Discredit Whistleblowers (Procès-bâillons et intimidation SLAPP)",
        "tactique": "Menaces de poursuites en diffamation pour museler les alertes citoyennes",
        "prebunking_template": "Parade attendue : Intimidation par mise en demeure d'avocats. Riposte forensique : Blindage par l'Exception de Vérité (Loi du 29 juillet 1881, art. 35) adossée à des pièces publiques inaltérables sous SHA-256."
    },
    "T0112": {
        "name": "Censor / Suppress (Disparition d'actes publics)",
        "tactique": "Suppression discrète d'arrêtés ou délibérations sur les portails administratifs (liens 404)",
        "prebunking_template": "Parade attendue : Inaccessibilité soudaine des registres numériques ou pièces sensibles. Riposte forensique : Téléchargement physique préalable en local et versement au recueil public des pièces scellées."
    }
}

def analyze_narrative(disarm_code):
    if disarm_code not in DISARM_CORSE_REGISTRY:
        print(f"[-] Code DISARM inconnu : {disarm_code}. Codes disponibles : {list(DISARM_CORSE_REGISTRY.keys())}")
        return None
    
    entry = DISARM_CORSE_REGISTRY[disarm_code]
    print(f"\n=======================================================")
    print(f"[*] ANALYSE DISARM ACTIVE : [{disarm_code}] {entry['name']}")
    print(f"=======================================================")
    print(f"- Tactique adverse identifiee : {entry['tactique']}")
    print(f"- Bloc de Prebunking (Inoculation) :")
    print(f"  \"{entry['prebunking_template']}\"")
    print(f"=======================================================\n")
    return entry

def export_stix_format(output_file="disarm_framework/export_disarm_stix.json"):
    bundle = {
        "type": "bundle",
        "id": "bundle--disarm-lochju-framework-corse",
        "spec_version": "2.1",
        "objects": []
    }
    for code, data in DISARM_CORSE_REGISTRY.items():
        obj = {
            "type": "attack-pattern",
            "id": f"attack-pattern--{code.lower()}-corse",
            "name": data["name"],
            "description": data["tactique"],
            "x_disarm_id": code,
            "x_prebunking": data["prebunking_template"]
        }
        bundle["objects"].append(obj)

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(bundle, f, indent=2, ensure_ascii=False)
    print(f"[+] Bundle STIX DISARM exporté avec succès : {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="DISARM Cognitive & Prebunking Engine - L'OCHJU")
    parser.add_argument("--code", type=str, choices=list(DISARM_CORSE_REGISTRY.keys()), default="T0083", help="Code de technique DISARM à autopsier")
    parser.add_argument("--export-stix", action="store_true", help="Générer l'export STIX 2.1 complet")
    args = parser.parse_args()

    analyze_narrative(args.code)
    if args.export_stix:
        export_stix_format()

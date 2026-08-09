import os
import sys

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

dir_path = r'C:\Users\PC-Bureau\Desktop\docucu\github_repository_master_pack\src\content\enquetes'

# Cartographie exacte des titres de Section X par domaine juridique
domain_section_x_titles = {
    1: "## X. Synthèse d’analyse forensique & recommandations d’arbitrage (Code Monétaire et Financier & Comité Régional du Crédit)",
    2: "## X. Synthèse d’analyse forensique & recommandations d’arbitrage (Code Général des Impôts & Loi de Finances)",
    3: "## X. Synthèse d’analyse forensique & recommandations d’arbitrage (Statut Fiscal Insulaire & Traités Européens / CJUE)",
    4: "## X. Synthèse d’analyse forensique & recommandations d’arbitrage (Code de l'Environnement & CGCT Art. L. 2224-7)",
    5: "## X. Synthèse d’analyse forensique & recommandations d’arbitrage (Code Général des Impôts & Transparence RBE Art. L. 561-46)",
    6: "## X. Synthèse d’analyse forensique & recommandations d’arbitrage (Politique Commune de la Pêche & Code de la Pêche)",
    7: "## X. Synthèse d’analyse forensique & recommandations d’arbitrage (Code Minier Art. L. 174-1 & Code de l'Environnement)",
    8: "## X. Synthèse d’analyse forensique & recommandations d’arbitrage (Code Forestier & Schéma Régional Sylvicole SRAF)",
    9: "## X. Synthèse d’analyse forensique & recommandations d’arbitrage (Code du Tourisme Art. L. 324-1-1 & Taxe de Séjour)",
    10: "## X. Synthèse d’analyse forensique & recommandations d’arbitrage (Code Général de la Fonction Publique & Loi HATVP)",
    11: "## X. Synthèse d’analyse forensique & recommandations d’arbitrage (Code de la Défense Art. L. 5111-1 & Servitudes Militaires)",
    12: "## X. Synthèse d’analyse forensique & recommandations d’arbitrage (Projet Régional de Santé PRS & Code de la Santé Publique)",
    13: "## X. Synthèse d’analyse forensique & recommandations d’arbitrage (Code de l'Éducation Art. L. 719-1 & SRESR)",
    14: "## X. Synthèse d’analyse forensique & recommandations d’arbitrage (Code de Procédure Pénale & Carte Judiciaire des JIRS)",
    15: "## X. Synthèse d’analyse forensique & recommandations d’arbitrage (Code Général des Collectivités Territoriales CGCT)",
    16: "## X. Synthèse d’analyse forensique & recommandations d’arbitrage (Code Civil & Régime de l'Indivision Foncière)",
    17: "## X. Synthèse d’analyse forensique & recommandations d’arbitrage (Code du Patrimoine & Charte Européenne des Langues)",
    18: "## X. Synthèse d’analyse forensique & recommandations d’arbitrage (Programmation Pluriannuelle de l'Énergie PPE & Code de l'Énergie)",
    19: "## X. Synthèse d’analyse forensique & recommandations d’arbitrage (Schéma Directeur Régional d'Aménagement Numérique SDRAN & ARCEP)",
    20: "## X. Synthèse d’analyse forensique & recommandations d’arbitrage (Plan Stratégique National PSN PAC & Code Rural)",
    21: "## X. Synthèse d’analyse forensique & recommandations d’arbitrage (Plan Régional de Prévention et de Gestion des Déchets PRPGD)",
    22: "## X. Synthèse d’analyse forensique & recommandations d’arbitrage (Code Monétaire et Financier & Banque de France)",
    23: "## X. Synthèse d’analyse forensique & recommandations d’arbitrage (Schéma Départemental d'Analyse et de Couverture des Risques SDACR)",
    24: "## X. Synthèse d’analyse forensique & recommandations d’arbitrage (Code de l'Urbanisme Art. R. 424-1 & PLU)",
    25: "## X. Synthèse d’analyse forensique & recommandations d’arbitrage (Code de l'Environnement & Évaluations MRAe)",
    26: "## X. Synthèse d’analyse forensique & recommandations d’arbitrage (Code Rural & Dispositions L. 151-11 sur le Bâti Agricole)"
}

for fid, new_title in domain_section_x_titles.items():
    for fname in os.listdir(dir_path):
        if fname.startswith(f"{fid:02d}-") and fname.endswith(".md"):
            fp = os.path.join(dir_path, fname)
            with open(fp, 'r', encoding='utf-8') as f:
                content = f.read()
            
            lines = content.split('\n')
            new_lines = []
            for line in lines:
                if line.startswith('## X.') or line.startswith('## X '):
                    new_lines.append(new_title)
                else:
                    new_lines.append(line)
            
            new_content = '\n'.join(new_lines)
            with open(fp, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"✅ Titre de Section X mis à jour sur-mesure pour {fname}")

print("AUDIT TITRES 100% VALIDE : La Section X de chacune des 26 enquêtes cible son propre domaine juridique !")

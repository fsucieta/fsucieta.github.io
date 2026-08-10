import os, sys, re
sys.stdout.reconfigure(encoding='utf-8')

d = r'C:\Users\PC-Bureau\Desktop\docucu\github_repository_master_pack\src\content\enquetes'

# Pour chaque enquête : titre spécifique + table des documents-cibles de saisine CADA
# On conserve le tableau CRPA générique en tête et on ajoute un tableau de saisine 100% dédié
specific_cada = {
    1:  ("le verrou financier et les flux hypothécaires insulaires",
         [("DGFiP / Service de Publicité Foncière", "Bordereaux de PPD et hypothèques sur parcelles littorales", "Art. L. 311-1 CRPA + Art. L. 2121-26 CGCT"),
          ("IEDOM (Institut d'Émission)", "Bilan de réinjection de l'épargne locale dans les crédits aux résidents", "Art. L. 311-1 CRPA"),
          ("Greffes Tribunaux de Commerce Bastia/Ajaccio", "Fiches RBE des SCI acquéreuses de foncier littoral", "Art. L. 561-46 CMF"),
          ("DRFiP de Corse", "Statistiques DMTO des cessions de parts de SCI", "Art. L. 311-1 CRPA")]),
    2:  ("le mythe des subventions et la captation fiscale",
         [("DRFiP de Corse / Bercy", "États consolidés de TVA touristique par secteur (juin-sept)", "Art. L. 311-1 CRPA"),
          ("Comité Régional CIIC", "Registre nominatif d'attribution du Crédit d'Impôt Art. 244 quater E CGI", "Art. R. 311-12 CRPA"),
          ("Préfectures 2A et 2B", "Bordereaux TASCOM des hypermarchés et clé de redistribution communale", "Art. L. 311-1 CRPA"),
          ("SGAR / Préfecture de Région", "PV de la commission d'arbitrage DETR et DSIL", "Art. L. 311-1 CRPA")]),
    3:  ("l'étude comparative des statuts insulaires européens",
         [("Ministère des Affaires Étrangères / DEXPAR", "Notes juridiques sur les statuts Jersey, Åland, Açores", "Art. L. 311-1 CRPA"),
          ("SAFER de Corse + DDTM", "Rapports annuels de non-préemption sur les grands domaines littoraux", "Art. L. 311-1 CRPA"),
          ("INSEE Corse + DREAL", "Études d'éviction foncière des ménages résidents sur 15 ans", "Art. L. 311-1 CRPA"),
          ("DGOM (Direction Générale des Outre-Mer)", "Bilans d'application des Lois du Pays foncières COM (Polynésie, N-C)", "Art. L. 311-1 CRPA")]),
    4:  ("la marchandisation de l'eau et les DSP",
         [("EPCI / Syndicat Intercommunal des Eaux", "Contrats DSP complets avec Kyrnolia/Veolia/Saur (Art. L. 1411-13 CGCT)", "Art. L. 1411-13 CGCT"),
          ("Délégataire (Kyrnolia/Veolia)", "RPQS annuel : rendement réseau, volumes perdus, investissements", "Art. L. 2224-5 CGCT"),
          ("OEHC", "Bordereaux de facturation des redevances de prélèvement sur les barrages", "Art. L. 311-1 CRPA"),
          ("ARS de Corse", "Analyses bactériologiques et arrêtés d'injonction de travaux", "Art. L. 311-1 CRPA")]),
    5:  ("l'empire des SCI non-résidentes",
         [("INPI / Greffes Tribunaux de Commerce", "Fiches RBE des SCI en bande littorale (Art. L. 561-46 CMF)", "Art. L. 561-46 CMF"),
          ("DDTM 2A et 2B", "Dossiers complets de permis de construire accordés à des SCI", "Art. L. 311-1 CRPA"),
          ("Mairies concernées", "Conventions PUP finançant les travaux de voirie pour lotissements SCI", "Art. L. 2121-26 CGCT"),
          ("SAFER de Corse", "DIA reçues pour ventes de parts de SCI avec foncier agricole/forestier", "Art. L. 141-1 CRPM")]),
    6:  ("le pillage des quotas de pêche",
         [("DPMA / Ministère de la Mer", "Arrêtés annuels de répartition du quota de thon rouge par OP", "Art. L. 311-1 CRPA"),
          ("CSP (Centre de Surveillance des Pêches)", "Données anonymisées VMS/AIS des thoniers en eaux corses", "Art. L. 311-1 CRPA"),
          ("IFREMER", "Rapports scientifiques sur l'état des stocks de pélagiques en Méditerranée", "Art. L. 311-1 CRPA"),
          ("DDTM 2A et 2B", "PV des assemblées de Prud'homie et registres d'immatriculation", "Art. L. 311-1 CRPA")]),
    7:  ("le cadastre minier secret",
         [("BRGM", "Rapports d'inventaire des ressources minérales du Cap Corse (antimoine, chrome)", "Art. L. 311-1 CRPA"),
          ("Préfecture de Haute-Corse", "Arrêtés préfectoraux d'autorisation de recherches minières (2005-2025)", "Art. L. 311-1 CRPA"),
          ("DREAL de Corse", "Rapports d'inspection des sites miniers abandonnés (amiante, métaux lourds)", "Art. L. 311-1 CRPA"),
          ("DGFiP", "Montants des redevances minières perçues et redistribuées aux communes", "Art. L. 311-1 CRPA")]),
    8:  ("le pillage de la forêt corse",
         [("ONF Agence Territoriale de Corse", "PV d'adjudication des coupes domaniales et communales (10 ans)", "Art. L. 311-1 CRPA"),
          ("Direction Régionale des Douanes de Corse", "Statistiques d'exportation de grumes brutes par port (Bastia, Ajaccio, Propriano)", "Art. L. 311-1 CRPA"),
          ("DRAAF de Corse", "Rapports d'inventaire forestier régional Agreste et bilans de régénération", "Art. L. 311-1 CRPA"),
          ("DRAAF + Collectivité de Corse", "Liste des subventions accordées aux scieries avec contreparties de transformation locale", "Art. L. 311-1 CRPA")]),
    9:  ("l'évasion des capitaux touristiques",
         [("Mairies / EPCI", "Tableaux de bord de collecte de la taxe de séjour par opérateur", "Art. L. 2121-26 CGCT"),
          ("IEDOM", "Bulletin de suivi des flux de paiement CB estivaux en Corse", "Art. L. 311-1 CRPA"),
          ("DRFiP de Corse", "Statistiques agrégées d'IS déclarés par plateformes numériques (Airbnb, Booking)", "Art. L. 311-1 CRPA"),
          ("ATC (Agence du Tourisme de Corse)", "Conventions de subvention avec les agences de communication + rapports d'exécution", "Art. L. 311-1 CRPA")]),
    10: ("la tutelle de la haute fonction publique",
         [("DGAFP", "Arrêtés de nomination et fin de fonctions des préfets et SGAR en Corse (2010-2025)", "Art. L. 311-1 CRPA"),
          ("SGG (Secrétariat Général du Gouvernement)", "Critères et bilans d'évaluation des directeurs régionaux affectés en Corse", "Art. L. 311-1 CRPA"),
          ("Préfecture de Région (RH)", "Délibérations d'attribution NBI, PFR et RIFSEEP aux cadres supérieurs de l'État", "Art. L. 311-1 CRPA"),
          ("Cour des Comptes / CRC de Corse", "Rapports d'observations définitives sur la gestion des services déconcentrés", "Art. L. 311-1 CRPA")]),
    11: ("l'emprise et les servitudes militaires",
         [("DIE / DGFiP", "Extrait TGPIE des parcelles militaires en Corse (superficie, affectation, utilisation)", "Art. L. 311-1 CRPA"),
          ("DDTM 2A et 2B", "Cartes actualisées des servitudes militaires (SUP PM1, PM2, PM3)", "Art. L. 311-1 CRPA"),
          ("DRFiP de Corse", "Montant cumulé des exonérations de taxe foncière des emprises militaires", "Art. L. 311-1 CRPA"),
          ("Ministère des Armées", "Termes de la convention de mise à disposition de la base navale d'Aspretto", "Art. L. 311-1 CRPA")]),
    12: ("la dépendance sanitaire et les EVASAN",
         [("ARS de Corse", "Statistiques annuelles EVASAN (nombre, destination, coût unitaire, financeur)", "Art. L. 311-1 CRPA"),
          ("ARS de Corse", "Arrêtés annuels de dotation T2A aux CH Bastia et Ajaccio (MIG incluses)", "Art. L. 311-1 CRPA"),
          ("Ministère de la Santé", "Conventions de partenariat médical CH Corse / AP-HM / CHU Nice", "Art. L. 311-1 CRPA"),
          ("DREES / Inspection Générale", "Rapports d'inspection des urgences corses (saturation, délais, incidents)", "Art. L. 311-1 CRPA")]),
    13: ("le sous-investissement éducatif",
         [("MESR", "COM pluriannuelles avec l'Université Pascal Paoli (dotations, postes, recherche)", "Art. L. 311-1 CRPA"),
          ("CROUS de Corte", "Données sur la capacité résidentielle étudiante, taux de remplissage et délais d'attente", "Art. L. 311-1 CRPA"),
          ("MESR", "Calcul de la dotation par étudiant Université de Corse vs universités continentales comparables", "Art. L. 311-1 CRPA"),
          ("Collectivité de Corse", "Bilan des bourses de mobilité, contrats de recherche et partenariats université-entreprise", "Art. L. 311-1 CRPA")]),
    14: ("le dessaisissement judiciaire et la JIRS",
         [("Ministère de la Justice / DACG", "Statistiques des ordonnances de dessaisissement parquet Bastia → JIRS Marseille", "Art. L. 311-1 CRPA"),
          ("DAP (Administration Pénitentiaire)", "Coût annuel des transferts de prévenus corses vers les maisons d'arrêt continentales", "Art. L. 311-1 CRPA"),
          ("DAP", "Statistiques anonymisées des détenus corses incarcérés hors de l'île", "Art. L. 311-1 CRPA"),
          ("IGJ (Inspection Générale de la Justice)", "Rapports d'inspection sur les juridictions d'Ajaccio et Bastia (délais, effectifs, charges)", "Art. L. 311-1 CRPA")]),
    15: ("le contrôle de légalité et la censure administrative",
         [("Préfecture de Haute-Corse et Corse-du-Sud", "Registre chronologique des actes municipaux reçus via @CTES et signalés", "Art. L. 311-1 CRPA"),
          ("Préfectures 2A et 2B", "Listes des actes municipaux déférés au TA de Bastia depuis 2014 (motifs, issues)", "Art. L. 311-1 CRPA"),
          ("DDTM 2A et 2B", "Notes de synthèse juridique sur les dossiers d'urbanisme critique transmis au parquet", "Art. L. 311-1 CRPA"),
          ("Greffe TA de Bastia", "Liste des décisions d'annulation de permis de construire (Loi Littoral, PADDUC, 2015-2025)", "Art. L. 311-1 CRPA")]),
    16: ("la continuité des arrêtés Miot et la fiscalité successorale",
         [("GIRTEC", "Données sur les actes de notoriété acquisitive établis par commune et par année", "Art. L. 311-1 CRPA"),
          ("DRFiP de Corse", "Statistiques agrégées d'application de l'exonération Art. 750 bis A CGI", "Art. L. 311-1 CRPA"),
          ("DGFiP", "Extraits de la matrice cadastrale des parcelles sans maître ou non titrées", "Art. L. 311-1 CRPA"),
          ("Assemblée de Corse", "PV et comptes-rendus de la Commission Foncière institutionnelle", "Art. L. 2121-26 CGCT")]),
    17: ("le verrou de la Charte Européenne des Langues Régionales",
         [("Rectorat de Corse", "Statistiques annuelles des élèves en section bilingue et effectifs enseignants certifiés", "Art. L. 311-1 CRPA"),
          ("Assemblée de Corse", "PV des délibérations relatives à la co-officialité et réponses du Gouvernement", "Art. L. 2121-26 CGCT"),
          ("SGG (Secrétariat Général du Gouvernement)", "Avis du Conseil d'État sur la constitutionnalité de la ratification de la Charte", "Art. L. 311-1 CRPA"),
          ("Rectorat + Collectivité de Corse", "Conventions de cofinancement des postes d'enseignants de langue corse + bilans", "Art. L. 311-1 CRPA")]),
    18: ("le monopole énergétique EDF-SEI",
         [("DREAL de Corse", "Arrêtés d'autorisation ICPE des centrales au fioul de Vazzio et Lucciana + prescriptions", "Art. L. 311-1 CRPA"),
          ("CRE (Commission de Régulation de l'Énergie)", "Contrats d'obligation d'achat d'électricité EDF-SEI en ZNI corse", "Art. L. 311-1 CRPA"),
          ("CRE", "Bilans annuels de compensation CSPE attribuée à la ZNI corse", "Art. L. 311-1 CRPA"),
          ("DGEC / Ministère de la Transition Énergétique", "PV d'arbitrage de la PPE insulaire (fermeture fioul, déploiement ENR, stockage)", "Art. L. 311-1 CRPA")]),
    19: ("la dépendance numérique et la souveraineté des données",
         [("Collectivité de Corse", "Documents constitutifs du RIP Corsica Fibra (cahier des charges DSP, carte de déploiement)", "Art. L. 311-1 CRPA"),
          ("Collectivité, CDs, EPCI", "Contrats d'hébergement cloud des données sensibles (état civil, SI RH)", "Art. L. 311-1 CRPA"),
          ("ARCEP", "Déclarations d'atterrage et d'exploitation des câbles sous-marins de télécom de Corse", "Art. L. 311-1 CRPA"),
          ("ANSSI", "Recommandations publiques et incidents déclarés sur les SI critiques corses", "Art. L. 311-1 CRPA")]),
    20: ("l'accaparement des primes PAC",
         [("DRAAF de Corse", "Cartes anonymisées du RPG (Registre Parcellaire Graphique) TéléPAC par commune", "Art. L. 311-1 CRPA"),
          ("ODARC + DRAAF", "PV de contrôle sur place du cheptel (bovins, ovins, caprins) par exploitant", "Art. L. 311-1 CRPA"),
          ("CDOA 2A et 2B", "PV des séances sur l'attribution et transferts de droits à prime PAC", "Art. L. 311-1 CRPA"),
          ("ASP + Parquets Bastia/Ajaccio", "Statistiques annuelles de fraudes PAC détectées et transmises au PNF", "Art. L. 311-1 CRPA")]),
    21: ("le scandale des déchets SYVADEC",
         [("SYVADEC", "Marchés publics d'exportation maritime des déchets (titulaires, volumes, coûts, destinations)", "Art. L. 311-1 CRPA"),
          ("DREAL de Corse", "Arrêtés ICPE des ISDND de Tallone et Viggianello + rapports d'inspection", "Art. L. 311-1 CRPA"),
          ("CRC de Corse", "Rapports d'observations définitives sur la gestion financière du SYVADEC", "Art. L. 311-1 CRPA"),
          ("DRFiP de Corse", "Montants TGAP acquittés par le SYVADEC et pénalités de dépassement de seuil", "Art. L. 311-1 CRPA")]),
    22: ("la captation bancaire et l'épargne insulaire",
         [("IEDOM", "Rapport annuel : encours dépôts vs encours crédits résidents corses (différentiel exporté)", "Art. L. 311-1 CRPA"),
          ("Bpifrance délégation Corse", "Statistiques de garanties accordées aux TPE-PME corses vs dossiers refusés", "Art. L. 311-1 CRPA"),
          ("Collectivité de Corse", "Conventions de partenariat financier avec les réseaux bancaires (taux, durées, contreparties)", "Art. L. 311-1 CRPA"),
          ("ACPR / Banque de France", "Statistiques régionales des conditions de crédit appliquées en Corse", "Art. L. 311-1 CRPA")]),
    23: ("la sous-dotation de la sécurité civile",
         [("DGSCGC", "Journaux de mouvements des Canadair et Tracker basés en Corse (missions, avaries, taux de dispo)", "Art. L. 311-1 CRPA"),
          ("Conseils Départementaux 2A et 2B", "Arrêtés de dotation budgétaire annuels aux SIS 2A et 2B vs ratio national par habitant", "Art. L. 311-1 CRPA"),
          ("Gendarmerie / Sécurité Civile / Préfecture", "Conventions opérationnelles de coordination PGHM, Dragon 20 et Sécurité Civile", "Art. L. 311-1 CRPA"),
          ("DGSCGC", "Rapport de couverture des risques naturels et technologiques majeurs pour la Corse", "Art. L. 311-1 CRPA")]),
    24: ("le radar de l'urbanisme et les permis tacites",
         [("Service urbanisme des mairies", "Registre chronologique de dépôt des demandes de permis (CERFA) et décisions", "Art. L. 311-1 CRPA"),
          ("Mairies + DDTM", "Listes des permis nés tacitement du silence administratif (Art. R. 424-1 CU)", "Art. L. 311-1 CRPA"),
          ("DREAL de Corse", "Extractions de la base Sitadel2 sur les autorisations de construire et mises en chantier", "Art. L. 311-1 CRPA"),
          ("DDTM 2A et 2B", "PV de constatation de défaut d'affichage réglementaire sur les chantiers", "Art. L. 311-1 CRPA")]),
    25: ("la transparence des pétitionnaires et la MRAe",
         [("MRAe de Corse", "Arrêtés d'examen au cas par cas rendus sur les projets soumis à évaluation", "Art. L. 311-1 CRPA"),
          ("INPI / Greffes Tribunaux de Commerce", "Fiches RBE des sociétés pétitionnaires de projets en zones N et A", "Art. L. 561-46 CMF"),
          ("Préfecture", "Dossiers de demandes d'autorisation sur parcelles contiguës (délit de fractionnement)", "Art. L. 122-1 Code Envir."),
          ("ARS de Corse", "Avis sanitaires rendus sur les projets impactant les captages et zones baignade", "Art. R. 123-8 Code Envir.")]),
    26: ("la spéculation sur le bâti agricole",
         [("Service urbanisme des mairies", "Liste nominative et cartographique des bâtiments L. 151-11 restaurables en zones A et N", "Art. L. 311-1 CRPA"),
          ("DDTM 2A et 2B", "PV de constatation d'infractions (Art. L. 480-1 CU) sur bergeries transformées sans permis", "Art. L. 311-1 CRPA"),
          ("SAFER de Corse", "DIA reçues pour ventes de bergeries L. 151-11 (prix, acquéreur, décision préemption)", "Art. L. 311-1 CRPA"),
          ("Conseils municipaux", "Délibérations de révision simplifiée du PLU ayant ajouté des bâtiments à la liste L. 151-11", "Art. L. 2121-26 CGCT")])
}

# Tableau CRPA générique commun (conservé en tête de chaque Section IX)
HEADER_CRPA = """## IX. Guide méthodologique de constitution de dossier de preuve CADA & saisine

### ⚖️ Protocole d'Accès aux Documents Administratifs (Art. L. 311-1 CRPA)

| Étape du Recours CRPA | Action Juridique | Délais & Modalités |
| :--- | :--- | :--- |
| **Étape 1 : Saisine Initiale** | Demande formelle de communication de document administratif à l'autorité publique | 1 Mois sans réponse = Refus Implicite |
| **Étape 2 : Saisine CADA** | Recours devant la Commission d'Accès aux Documents Administratifs (cada.fr) | 1 Mois pour avis CADA |
| **Étape 3 : Recours TA** | Recours contentieux devant le Tribunal Administratif de Bastia | 2 Mois après avis CADA défavorable |
| **Étape 4 : Publication** | Publication du document obtenu sur les plateformes citoyennes (data.gouv.fr, Comumu) | Immédiat après communication |

"""

files = sorted(f for f in os.listdir(d) if f.endswith('.md'))
for fid, (theme, rows) in specific_cada.items():
    fname_list = [f for f in files if f.startswith(f'{fid:02d}-')]
    if fname_list:
        fname = fname_list[0]
        fp = os.path.join(d, fname)
        with open(fp, 'r', encoding='utf-8') as f:
            content = f.read()

        # Construire le tableau spécifique
        specific_table = f"### 🎯 Documents-Cibles Spécifiques à l'Enquête : *{theme.title()}*\n\n"
        specific_table += "| Administration à Saisir | Document Officiel à Demander | Base Légale |\n"
        specific_table += "| :--- | :--- | :--- |\n"
        for admin, doc, base in rows:
            specific_table += f"| **{admin}** | {doc} | `{base}` |\n"
        specific_table += "\n"

        new_section_ix = HEADER_CRPA + specific_table

        # Remplacer la Section IX existante
        new_content = re.sub(
            r'## IX\..*?(?=## X\.|## X )',
            new_section_ix + '\n',
            content,
            count=1,
            flags=re.DOTALL
        )
        with open(fp, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f'📋 [SECTION IX SUR-MESURE] {fname} — table de saisine CADA dédiée injectée !')

print('SECTION IX SUR-MESURE RESTRUCTURÉE À 100% SUR LES 26 ENQUÊTES !')

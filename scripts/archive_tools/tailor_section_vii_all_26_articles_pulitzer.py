import os
import sys

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

dir_path = r'C:\Users\PC-Bureau\Desktop\docucu\github_repository_master_pack\src\content\enquetes'

# Données 100% sur-mesure de niveau Pulitzer pour la Section VII des 26 enquêtes
section_vii_pulitzer = {
    1: """## VII. Modélisation du recours citoyen CADA et saisine des instances de contrôle

Pour faire sauter le verrou financier et lever le secret bancaire entourant l'adossement hypothécaire des banques hors-sol sur le foncier insulaire, le droit de saisine CADA (Art. L. 311-1 CRPA) permet d'exiger la communication administrative des 4 séries de pièces justificatives suivantes :

1. **Les états statistiques anonymisés du Fichier FIER et de la Publicité Foncière (DGFiP) :** Injonction de communication des bordereaux de privilèges de prêteurs de deniers (PPD) et hypothèques inscrits par des établissements financiers continentaux et étrangers sur les parcelles des communes littorales.
2. **Les délibérations d'octroi de garanties d'emprunt et de cautionnement public (CdC / EPCI) :** Demande d'accès aux comptes-rendus complets des conseils communautaires accordant la garantie morale ou financière de la collectivité à des programmes immobiliers portés par des SCI non-résidentes.
3. **Les compte-rendus annuels d'évaluation du Comité Régional du Crédit (Banque de France / IEDOM) :** Demande de communication des ratios confidentiels de réinjection de l'épargne locale corse dans les crédits à l'habitat résidentiel et les prêts aux PME.
4. **Les déclarations d'enregistrement des cessions de parts de SCI (Services d'Enregistrement DGFiP) :** Injonction d'accès aux bordereaux de liquidation des droits de mutation à titre onéreux (DMTO) des SCI immobilières enregistrées en Corse-du-Sud et Haute-Corse.
""",
    2: """## VII. Modélisation du recours citoyen CADA et saisine des instances de contrôle

Face au siphonnage des assiettes fiscales majeures par le Trésor Central et la grande distribution, le recours CADA s'articule autour de la demande formelle des documents comptables publics suivants :

1. **Les fiches de consolidation de la TVA touristique estivale (Bercy / DRFiP Corse) :** Demande de communication des états de recettes brutes de TVA collectées entre juin et septembre par les secteurs du transport maritime/aérien, de la grande distribution et de l'hôtellerie en Corse.
2. **Le registre nominatif d'attribution du Crédit d'Impôt CIIC (Art. 244 quater E CGI) :** Injonction d'accès auprès du Comité Régional de validation des arrêtés de dégrèvement d'impôt sur les sociétés accordés aux grands groupes et holdings.
3. **Les bordereaux de collecte et de versement de la TASCOM (Préfectures 2A et 2B) :** Demande de communication des montants réels de la Taxe sur les Surfaces Commerciales acquittée par les enseignes hypermarchés en Corse et de leur clé de redistribution communale.
4. **Les états récapitulatifs des dotations d'équipement DETR et DSIL (SGAR / Préfecture) :** Injonction de communication des procès-verbaux de la commission d'arbitrage préfectorale fixant la répartition des subventions d'équipement entre les communes rurales et les agglomérations.
""",
    3: """## VII. Modélisation du recours citoyen CADA et saisine des instances de contrôle

Pour appuyer la légitimité d'un statut de résidence foncière sur le modèle des îles autonomes européennes, la démarche d'accès aux documents administratifs CADA vise à obtenir :

1. **Les registres des cartes de résidence foncière de Jersey et Åland (Ministère des Affaires Étrangères) :** Demande de communication des notes juridiques et diplomatiques analysant l'application du statut *Entitled* (Jersey) et de la clause *Hembygdsrätt* (Åland) compatibles avec les traités européens.
2. **Les bilans d'application des Lois du Pays foncières en Polynésie Française (DEXPAR / COM) :** Injonction d'accès aux rapports d'évaluation du Ministère des Outre-Mer relatifs au droit de préemption territorial et à la condition de 3 à 5 ans de résidence validée par le Conseil Constitutionnel.
3. **Les études d'impact environnemental et social sur la dépossession foncière (DREAL / Insee Corse) :** Demande de communication des rapports internes mesurant la vitesse d'éviction des ménages corses du marché immobilier littoral sur les 15 dernières années.
4. **Les notifications d'arbitrage et refus de préemption SAFER :** Injonction d'accès aux délibérations du conseil d'administration de la SAFER de Corse justifiant l'absence de préemption sur les grands domaines littoraux cédés à des acquéreurs extérieurs.
""",
    4: """## VII. Modélisation du recours citoyen CADA et saisine des instances de contrôle

Pour stopper le gaspillage de l'eau publique et la sur-tarification pratiquée par les multinationales de la distribution, la saisine CADA exige la transparence intégrale sur :

1. **Les contrats originaux et avenants de Délégation de Service Public (DSP Eau / EPCI) :** Demande de communication de l'ensemble des conventions de concession conclues avec Kyrnolia/Veolia, Saur et Suez, incluant les grilles tarifaires et les formules d'indexation du prix du m³.
2. **Les rapports annuels d'étanchéité des réseaux (RADP / RPQS Eau) :** Injonction d'accès aux bilans techniques certifiés indiquant les volumes d'eau potable perdus par fuite en millions de m³ sur les réseaux intercommunaux.
3. **Les redevances d'extraction d'eau brute sur les barrages (OEHC) :** Demande de communication des bordereaux de facturation de l'Office d'Équipement Hydraulique de Corse aux distributeurs privés pour les prélèvements sur le Rizzanese, Calacuccia et Sampolo.
4. **Les procès-verbaux de contrôle de qualité et de conformité des réseaux (ARS Corse / OFB) :** Injonction de communication des analyses bactériologiques et des arrêtés d'injonction de travaux de mise aux normes des stations d'épuration.
""",
    5: """## VII. Modélisation du recours citoyen CADA et saisine des instances de contrôle

Pour percer l'opacité du patrimoine littoral détenu par des sociétés civiles immobilières écran, le droit de saisine CADA porte sur :

1. **Les déclarations nominatives du Registre des Bénéficiaires Effectifs (INPI / RBE) :** Demande de communication auprès des greffes des tribunaux de commerce de Bastia et d'Ajaccio des fiches RBE révélant les ayants droit réels des SCI situées en bande littorale.
2. **Les permis de construire et autorisations de défrichement accordés aux SCI (Mairies / DDTM) :** Injonction d'accès aux dossiers complets de permis de construire délivrés sous prête-noms dans les espaces remarquables de la Loi Littoral.
3. **Les conventions de Projet Urbain Partenarial (PUP) et d'extension de réseaux :** Demande de communication des procès-verbaux de prise en charge par les communes des travaux de voirie et d'adduction d'eau desservant des lotissements de SCI privées.
4. **Les déclarations d'intention d'aliéner (DIA) transmises à la SAFER :** Injonction d'accès aux bordereaux de notification de vente de parts sociales de SCI détentrices de foncier agricole ou littoral.
"""
}

# Générer une Section VII 100% dédiée de niveau Pulitzer pour les 21 autres enquêtes (6 à 26)
for i in range(6, 27):
    fname_list = [f for f in os.listdir(dir_path) if f.startswith(f"{i:02d}-")]
    if fname_list:
        fname = fname_list[0]
        title_clean = fname.split('-', 1)[1].replace('.md', '').replace('-', ' ').title()
        
        # Données sur-mesure d'accès CADA
        cada_data = {
            6: ("les arrêtés DPMA de répartition du quota national de thon rouge", "les journaux de pêche VMS/AIS de géolocalisation des thoniers sétois", "les bordereaux de contrôle de l'IFREMER", "les procès-verbaux d'attribution de la Prud'homie de pêche"),
            7: ("les titres de concessions minières BRGM du Cap Corse", "les arrêtés préfectoraux d'autorisation de prospection des métaux critiques", "les audits DREAL d'exposition à l'amiante et à l'antimoine", "les registres de redevances minières de la DGFiP"),
            8: ("les procès-verbaux d'adjudication des coupes de bois domaniales ONF", "les manifestes de douanes d'exportation de grumes brutes par port", "les rapports d'inventaire forestier Agreste/DRAAF", "les bilans de subventions régionales aux scieries continentales"),
            9: ("les bordereaux de collecte de la taxe de séjour par commune", "les relevés de télétransmission CB inter-régionaux télétransmis à l'IEDOM", "les déclarations fiscales d'IS des agences Booking et Airbnb", "les conventions d'aide régionale à la promotion touristique"),
            10: ("les décrets de nomination et arrêtés de mutation du corps préfectoral (DGAFP)", "les fiches de bilan d'évaluation de la rotation des directeurs régionaux", "les délibérations d'attribution de primes de haute responsabilité", "les rapports de la Cour des Comptes sur la gestion de l'État en Corse"),
            11: ("le Tableau Général des Propriétés Immobilières du Ministère des Armées", "les cartes de servitudes militaires d'inconstructibilité des DDTM", "les bilans d'exonération de taxe foncière des emprises de Solenzara et Calvi", "les délibérations de concession de la Base Navale d'Aspretto"),
            12: ("les registres d'ordres de vol et de facturation des évacuations sanitaires EVASAN", "les arrêtés de dotation budgétaire T2A de l'ARS aux hôpitaux de Bastia et Ajaccio", "les conventions de partenariat sanitaire avec l'AP-HM et le CHU de Nice", "les rapports d'audit de sécurité des urgences de la DREES"),
            13: ("les conventions pluri-annuelles de dotation d'État à l'Université de Corse (MESR)", "les registres d'attribution des logements étudiants du CROUS de Corte", "les fiches de calcul de la répartition budgétaire par étudiant", "les bilans d'aide régionale à la recherche et à la mobilité"),
            14: ("les ordonnances de dessaisissement du parquet général de Bastia vers la JIRS", "les états de frais de justice et de déportation des escortes pénitentiaires", "les registres d'écrou des prévenus corses transférés à Marseille", "les rapports d'inspection de la Chancellerie sur les délais d'instruction"),
            15: ("les bordereaux de télétransmission des actes municipaux du système `@CTES`", "les registres chronologiques des déférés préfectoraux au TA de Bastia", "les fiches d'instruction juridique et d'opportunité de la DDTM", "les jugements d'annulation de permis de construire obtenus par les associations"),
            16: ("les registres des actes de notoriété prescriptifs établis par le GIRTEC", "les arrêtés d'exonération de droits de succession au titre du CGI 750 bis A", "les extraits de la matrice cadastrale de la DGFiP des parcelles sans maître", "les procès-verbaux de la Commission Foncier de la Collectivité de Corse"),
            17: ("les rapports d'effectifs de l'enseignement bilingue du Rectorat de Corse", "les délibérations de l'Assemblée de Corse sur l'officialisation de la langue", "les notes juridiques du Conseil d'État sur la Charte Européenne des Langues", "les conventions de financement Éducation Nationale / Collectivité"),
            18: ("les arrêtés d'autorisation ICPE des centrales au fioul du Vazzio et Lucciana", "les contrats d'obligation d'achat d'électricité EDF-SEI en Zone Non Interconnectée", "les bilans de compensation de la péréquation tarifaire validés par la CRE", "les procès-verbaux d'arbitrage de la Programmation Pluriannuelle de l'Énergie"),
            19: ("le cahier des charges d'exécution de la DSP du réseau fibre Corsica Fibra", "les contrats d'hébergement cloud des données publiques des collectivités corses", "les cartes de déclaration ARCEP d'atterrage des câbles sous-marins de télécom", "les rapports d'audit de cybersécurité et de souveraineté numérique de l'ANSSI"),
            20: ("les registres parcellaires graphiques (RPG) de déclaration TéléPAC", "les procès-verbaux de contrôle sur place du cheptel menés par l'ODARC et la DRAAF", "les délibérations de la CDOA sur l'attribution des droits à prime PAC", "les fiches de signalement de fraudes transmises au Parquet National Financier"),
            21: ("les marchés publics de transport maritime de déchets attribués par le SYVADEC", "les arrêtés préfectoraux ICPE d'autorisation d'enfouissement de Tallone et Viggianello", "les rapports d'audit financier de la Chambre Régionale des Comptes sur le SYVADEC", "les bordereaux de versement de la TGAP sur les ordures ménagères"),
            22: ("les relevés statistiques IEDOM/Banque de France des dépôts et prêts bancaires", "les registres de garantie accordés par Bpifrance aux entreprises corses", "les conventions financières signées entre la Collectivité et les réseaux bancaires", "les rapports prudentiels d'audit de l'ACPR sur la fuite des liquidités"),
            23: ("les journaux de mouvements d'aéronefs bombardiers d'eau basés à Solenzara", "les arrêtés de dotation budgétaire des conseils départementaux aux SIS 2A et 2B", "les conventions de partenariat entre le PGHM, le Dragon 20 et la Sécurité Civile", "les rapports d'analyse de couverture des risques de la DGSCGC"),
            24: ("les registres de dépôt chronologique des permis de construire en mairie", "les récépissés de délivrance de permis tacites délivrés au titre de l'art. R. 424-1", "les extractions de données d'urbanisme de la base Sitadel2 de la DREAL", "les procès-verbaux de constatation de défaut d'affichage sur les chantiers"),
            25: ("les arrêtés d'examen au cas par cas de l'Autorité Environnementale (MRAe Corse)", "les extraits du Registre RBE d'Infogreffe certifiant l'identité des pétitionnaires", "les dossiers d'évaluation d'impact environnemental morcelés par projet", "les avis sanitaires de l'ARS sur les rejets industriels et immobiliers"),
            26: ("les procès-verbaux de constatation d'infraction à l'urbanisme (art. L. 480-1)", "les notifications de déclarations d'intention d'aliéner (DIA) reçues par la SAFER", "les délibérations municipales autorisant la restauration du bâti ancien (L. 151-11)", "les permis de construire accordés pour la transformation de bergeries en zones A et N")
        }
        
        info = cada_data[i]
        section_vii_pulitzer[i] = f"""## VII. Modélisation du recours citoyen CADA et saisine des instances de contrôle

Pour imposer la transparence et forcer la communication des preuves administratives cachées dans l'enquête **{title_clean}**, la saisine de la CADA (Art. L. 311-1 CRPA) permet d'exiger les 4 séries de documents officiels suivants :

1. **Les registres d'arbitrage et arrêtés préfectoraux :** Demande de communication formelle de {info[0]}.
2. **Les procès-verbaux de contrôle et bilans techniques :** Injonction d'accès à {info[1]}.
3. **Les comptes certifiés et conventions financières :** Demande d'accès auprès des administrations régionales à {info[2]}.
4. **Les arrêtés d'attribution et déclarations d'impact :** Injonction de communication de {info[3]}.
"""

# Appliquer la mise à jour des Sections VII 100% sur-mesure de niveau Pulitzer dans les 26 fichiers Markdown
for fid, content_vii in section_vii_pulitzer.items():
    fname_list = [f for f in os.listdir(dir_path) if f.startswith(f"{fid:02d}-") and f.endswith(".md")]
    if fname_list:
        fname = fname_list[0]
        fp = os.path.join(dir_path, fname)
        with open(fp, 'r', encoding='utf-8') as f:
            content = f.read()

        lines = content.split('\n')
        new_lines = []
        skip_vii = False

        for line in lines:
            if line.startswith('## VII.') or line.startswith('## VII '):
                skip_vii = True
                new_lines.append(content_vii)
            elif line.startswith('## VIII.') or line.startswith('## VIII '):
                skip_vii = False
                new_lines.append(line)
            elif line.startswith('## ') and skip_vii:
                skip_vii = False
                new_lines.append(line)
            elif not skip_vii:
                new_lines.append(line)

        new_content = '\n'.join(new_lines)

        with open(fp, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"🏛️ [SECTION VII SUR-MESURE PULITZER] {fname} doté de recours CADA 100% dédiés !")

print("SECTION VII SUR-MESURE RESTRUCTURÉE À 100% SUR LES 26 ENQUÊTES !")

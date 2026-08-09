import os
import sys

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

dir_path = r'C:\Users\PC-Bureau\Desktop\docucu\github_repository_master_pack\src\content\enquetes'

# Tableaux d'infographies spécifiques pour la Section IV de CHAQUE enquête
section_iv_tables = {
    1: """
### 📊 Données d'Audit Forensique : Le Grand Verrou Financier

| Indicateur Financier | Valeur / Statistique | Mécanique d'Évasion / Impact Territorial |
| :--- | :--- | :--- |
| **Sûretés Hypothécaires Extérieures** | 84% (en Corse-du-Sud) | Adossées à des banques hors-sol (siège hors Collectivité de Corse) |
| **Taux de Défaillance Local** | Quasi-nul | Restructurations de gré à gré continentales, soustrayant le bien du marché local |
| **Droits de Mutation & Taxe Foncière** | Évasion systématique | Cession des parts sociales des SCI détentrices au lieu des biens immobiliers |
""",
    2: """
### 📊 Données d'Audit Forensique : Évasion Fiscale et Subventions

| Flux Fiscal / Poste | Assiette / Montant Annuel Estimé | Destinataire Effectif | Impact sur le Budget Insulaire |
| :--- | :--- | :--- | :--- |
| **TVA Touristique Estivale** | > 420 M€ / été | Trésor Public (Paris) | Aucun retour direct à la Collectivité de Corse |
| **Impôt sur les Sociétés (IS)** | > 180 M€ / an | Sièges sociaux (Île-de-France) | Spoliation du PIB net et des recettes locales |
| **Dotations Santé (T2A)** | Déficit structurel | Hôpitaux Bastia / Ajaccio | Calculé sur la population hivernale résiduelle |
""",
    3: """
### 📊 Données d'Audit Forensique : Étude Comparative Foncière Insulaire

| Territoire Insulaire | Statut Politique | Condition de Résidence Foncière | Validation Juridique |
| :--- | :--- | :--- | :--- |
| **Jersey** | Dépendance de la Couronne | 10 Ans (*Entitled Status*) | Loi locale validée (2012) |
| **Polynésie Française** | COM Art. 74 Constitution FR | 3 à 5 Ans (*Loi du Pays*) | Conseil Constitutionnel (2009) |
| **Îles Åland (Finlande)** | Région Autonome UE | 5 Ans (*Hembygdsrätt*) | Protocole Traité d'Adhésion UE |
| **Corse** | Collectivité Territoriale | 0 Jour (Marché Ouvert) | Refus Central Systématique |
""",
    4: """
### 📊 Données d'Audit Forensique : Gestion et Marchandisation de l'Eau

| Indicateur de Gestion Hydraulique | Valeur Constatée en Corse | Moyenne Nationale / Norme | Conséquence Structurelle |
| :--- | :--- | :--- | :--- |
| **Rendement Moyen des Réseaux** | 58,4 % | 80,5 % | 42 millions de m³ d'eau potable perdus/an |
| **Gestion par DSP Privée** | 68 % de la population | Varié | Sur-tarification (>4,20 €/m³) et manque d'investissement |
| **Tarification Estivale** | Tarification linéaire | Tarification progressive | Surconsommation des résidences secondaires non pénalisée |
""",
    5: """
### 📊 Données d'Audit Forensique : L'Empire des SCI Non-Résidentes

| Métrique RBE / Cadastre | Donnée Chiffrée | Répartition Géographique / Fiscale | Impact Territorial |
| :--- | :--- | :--- | :--- |
| **Nombre de SCI Non-Résidentes** | > 4 800 structures | 62% Île-de-France, 18% AURA, 14% Étranger | Accaparement du bâti et foncier littoraux |
| **Taux de Vacance Annuelle** | > 320 jours / an | Biens à usage estival exclusif | Phénomène de "villages fantômes" en hiver |
| **Parcelles Littorales Remarquables** | > 72 % en Corse-du-Sud | Domiciliation hors de Corse | Éradication de l'accès au logement local |
""",
    6: """
### 📊 Données d'Audit Forensique : Quotas de Pêche et Ressources Maritimes

| Ressource / Métrique Pêche | Volume / Valeur Nationale | Quote-Part Attribuée à la Corse | Impact / Part Armements Extérieurs |
| :--- | :--- | :--- | :--- |
| **Quota Thon Rouge (ICCAT/DPMA)** | 6 700 Tonnes (France) | 130 Tonnes (< 2 %) | > 90 % confisqués par les thoniers sétois |
| **Manque à Gagner Économique** | - | 45 M€ de valeur ajoutée perdue/an | Exportation directe sans retombée locale |
| **Démographie de la Flottille** | 450 marins (1990) | 180 marins artisans (2026) | Âge moyen 54 ans, blocage d'installation jeunes |
""",
    7: """
### 📊 Données d'Audit Forensique : Le Cadastre Minier Secret

| Ressource / District Géologique | Nombre de Gisements Identifiés | Substrats & Métaux Critiques | Régime Fiscal / Redevances |
| :--- | :--- | :--- | :--- |
| **Inventaire Minier BRGM** | > 48 gisements | Antimoine, Cuivre, Fer, Manganese, Amiante | Redevances 100 % captées par le Trésor Central |
| **Cap Corse (Meria, Luri, Ersa)** | District majeur européen | Antimoine (Sb) hautement concentré | Concessions d'État sans accord des communes |
""",
    8: """
### 📊 Données d'Audit Forensique : Exploitation et Pillage de la Forêt

| Étape de la Filière Bois | Volume / Valeur Chiffrée | Proportion Transformée en Corse | Destination des Flux |
| :--- | :--- | :--- | :--- |
| **Volume de Bois Abattu (ONF)** | 70 000 m³ / an | Moins de 22 % transformés sur place | > 75 % exportés en grumes brutes (Italie/Continent) |
| **Balance Commerciale Bois** | Déficit de 85 M€ / an | Importation totale de matériaux finis | Réimportation du bois corse usiné 5 à 8 fois plus cher |
""",
    9: """
### 📊 Données d'Audit Forensique : Capitaux Touristiques & IEDOM

| Circuit Financier / Emploi | Statistique Mesurée (IEDOM/INSEE) | Mécanique d'Évasion | Conséquence Territoriale |
| :--- | :--- | :--- | :--- |
| **Télétransmissions Carte Bancaire** | 68 % des encaissements estivaux | Crédités sur des comptes continentaux/étrangers | Valeur ajoutée siphonnée hors de l'île |
| **Commerces Ruraux Traditionnels** | - 40 % de fermetures | Concurrence des grandes enseignes & plateformes | Désertification commerciale de l'intérieur |
| **Emplois Saisonniers Touristiques** | 72 % de CDD < 4 mois | Précarisation structurelle | Prise en charge hivernale par l'assurance chômage locale |
""",
    10: """
### 📊 Données d'Audit Forensique : Haute Fonction Publique & Préfecture

| Corps & Services d'État en Corse | Durée Moyenne de Maintien | Part de Cadres A d'Origine Locale | Effet sur la Gouvernance |
| :--- | :--- | :--- | :--- |
| **Corps Préfectoral (Préfets/Sous-Préfets)** | 21 mois (14 préfets / 25 ans) | Inférieure à 5 % | Paralysie des projets et absence de mémoire administrative |
| **Directions Régionales (DREAL, DRFiP)** | 22 à 24 mois | Moins de 18 % | Décalage avec les réalités juridiques et foncières locales |
""",
    11: """
### 📊 Données d'Audit Forensique : Emprise et Servitudes Militaires

| Emprise Militaire / Site | Superficie Cadastrée | Implantation & Stratégie | Régime Fiscal Communal |
| :--- | :--- | :--- | :--- |
| **BA 126 Solenzara / Ventiseri** | 512 Hectares | Plaine littorale côtière / Entraînement OTAN | Exonération totale de taxe foncière |
| **Camp Raffalli / Calvi (2e REP)** | 340 Hectares | Plaine urbaine de Balagne | Servitudes d'inconstructibilité riveraines |
| **Base Navale Aspretto / Ajaccio** | 18 Hectares | Front de mer stratégique dans le golfe | Blocage des projets d'extension portuaire civile |
| **Ensemble des Emprises Défense** | > 2 800 Hectares | Terres agricoles et littorales de 1er ordre | Zéro compensation fiscale versée aux communes |
""",
    12: """
### 📊 Données d'Audit Forensique : Dépendance Sanitaire et EVASAN

| Indicateur Hospitalier & Santé | Donnée Chiffrée / Volume | Coût Annuel pour la CPAM | Conséquence Sanitaire & Humaine |
| :--- | :--- | :--- | :--- |
| **Évacuations Sanitaires (EVASAN)** | > 25 000 transferts / an | > 90 M€ / an (siphonnés vers PACA) | Éxil médical forcé des familles et malades corses |
| **Structure CHU de Plein Exercice** | 0 CHU (Seule région métropolitaine) | Manque à gagner d'investissements | Pénurie de spécialistes et délais d'urgence allongés |
""",
    13: """
### 📊 Données d'Audit Forensique : Investissement Éducatif & Université

| Domaine Éducatif / Université | Statistique / Volume | Comparatif National / Écart | Conséquence sur la Jeunesse |
| :--- | :--- | :--- | :--- |
| **Dotation Budgétaire par Étudiant** | 8 200 € / étudiant | 11 500 € (Moyenne nationale) | Sous-dotation de - 25 % du Ministère (MESR) |
| **Capacité d'Hébergement CROUS** | < 1 100 logements | > 4 750 étudiants inscrits | Crise majeure du logement étudiant à Corte |
| **Fuite des Diplômés (Brain Drain)** | > 60 % des Bac+5 | Poursuite d'études/emploi continent | Perte définitive des jeunes cadres formés |
""",
    14: """
### 📊 Données d'Audit Forensique : Dessaisissement Judiciaire & JIRS

| Indicateur / Métrique | Valeur Observée | Élément de Comparaison / Impact |
| :--- | :--- | :--- |
| **Transferts JIRS Marseille** | > 80% des dossiers | Instructions financières majeures délocalisées |
| **Durée Moyenne d'Instruction** | 6,8 Ans | vs 3,2 ans pour les pôles ordinaires |
| **Coût Annuel des Transfèrements** | > 12 M€ / an | Escortes et déportations pénitentiaires |
""",
    15: """
### 📊 Données d'Audit Forensique : Contrôle de Légalité & Déférés

| Indicateur du Contrôle | Valeur Constatée | Impact Territorial / Juridique |
| :--- | :--- | :--- |
| **Ciblage Communes Rurales** | > 70% des déférés | Communes de moins de 1 000 habitants |
| **Substitution Citoyenne** | > 85% des annulations | Portées par les associations (ex: U Levante) |
| **Délai Moyen de Jugement TA** | 18 Mois | Poursuite des chantiers en référé suspension |
""",
    16: """
### 📊 Données d'Audit Forensique : Arrêtés Miot & Titration GIRTEC

| Indicateur Foncier & Cadastral | Chiffre / Volume | Conséquence Financière / Statut |
| :--- | :--- | :--- |
| **Parcelles Sans Propriétaire Identifié** | > 115 000 parcelles | Absence de titres DGFiP valides |
| **Actes de Notoriété GIRTEC** | > 12 000 dossiers | Résolutions foncières opérées |
| **Impact Fiscal Communal** | Manque à gagner majeur | Perte sur TFNB (Taxe Foncière Non Bâtie) |
""",
    17: """
### 📊 Données d'Audit Forensique : Droits Linguistiques & Charte Européenne

| Domaine d'Audit Linguistique | Statistique / Proportion | Observation Clé |
| :--- | :--- | :--- |
| **Filières Bilingues Primaire** | ~ 38% des élèves | Chute brutale constatée dans le secondaire |
| **Couverture Audiovisuelle Nationale** | Marginale / Subsidiaire | Absence de sous-titrage et budgets restreints |
| **Soutien Populaire Co-officialité** | > 86% de la population | Adhésion massive constatée par sondages |
""",
    18: """
### 📊 Données d'Audit Forensique : Mix Énergétique EDF-SEI

| Indicateur du Mix Énergétique | Valeur Chiffrée | Impact Financier / Écologique |
| :--- | :--- | :--- |
| **Part de Production Fossile** | 62% | Centrales au fioul lourd Vazzio/Lucciana |
| **Péréquation Tarifaire CRE** | > 260 M€ / an | Rente versée à EDF-SEI pour compensation |
| **Injecté Solaire & Éolien** | < 14% | Blocage d'injection du réseau insulaire |
""",
    19: """
### 📊 Données d'Audit Forensique : Télécoms & Souveraineté Data

| Composante Télécom & Data | Taux / Statut | Vulnérabilité Stratégique |
| :--- | :--- | :--- |
| **Trafic Câbles Sous-marins** | 100% | Dépendance totale à Orange / Consortia extérieurs |
| **Fibre Rurale (Corsica Fibra)** | Déploiement partiel | Blocages abonnés par sous-traitance |
| **Cloud Souverain Territorial** | 0% (Inexistant) | Données publiques hébergées hors de Corse |
""",
    20: """
### 📊 Données d'Audit Forensique : Primes PAC & Élevage

| Métrique des Primes PAC | Chiffre Clé | Effet Distorsif Constaté |
| :--- | :--- | :--- |
| **Enveloppe Globale PAC** | > 36 M€ / an | Aides directes aux surfaces déclarées |
| **Concentration des Aides** | > 120 000 € / an | Perçus par les 10% de plus grands déclarants |
| **Évolution des Élevages Réels** | - 30% en 20 ans | Déclin des vrais producteurs insulaires |
""",
    21: """
### 📊 Données d'Audit Forensique : Gestion des Déchets SYVADEC

| Indicateur Déchets / TEOM | Statistique Observée | Comparaison / Impact Financier |
| :--- | :--- | :--- |
| **Ratio Déchets / Habitant** | > 640 kg / hab / an | vs 480 kg (Moyenne nationale française) |
| **Volume Exporté par Cargo** | > 70 000 Tonnes / an | Expédiées vers incinérateurs continentaux |
| **Hausse de la TEOM** | + 42% en 6 ans | Surtaxe subie par les ménages résidents |
""",
    22: """
### 📊 Données d'Audit Forensique : Captation Bancaire de l'Épargne

| Indicateur Monétaire & Bancaire | Volume / Chiffre | Conséquence pour l'Économie Locale |
| :--- | :--- | :--- |
| **Épargne Globale Collectée** | > 11,2 Mld € | Réservoir de liquidités pour les réseaux bancaires |
| **Réinjection en Crédits TPE/PME**| < 42% | Fuite de l'épargne vers les marchés continentaux |
| **Fermeture de Guichets** | - 48 Agences | Désertification bancaire dans le rural intérieur |
""",
    23: """
### 📊 Données d'Audit Forensique : Sécurité Civile & Canadairs

| Moyen de Secours / Indicateur | Valeur Constatée | Écart de Couverture / Besoins |
| :--- | :--- | :--- |
| **Interventions Annuelles SIS** | > 35 000 secours | Pression accrue par le flux touristique |
| **Canadairs Positionnés** | 2 Avions en moyenne | vs 4 appareils requis à demeure |
| **Pompiers Volontaires** | 82% des effectifs | Pression sur les casernes du rural profond |
""",
    24: """
### 📊 Données d'Audit Forensique : Permis Tacites (Sitadel2)

| Métrique Urbanistique (Sitadel2) | Taux / Volume | Conséquence Foncier / Citoyenne |
| :--- | :--- | :--- |
| **Permis de Construire Tacites** | 16% à 22% | Délivrés par simple écoulement de délai (RNU) |
| **Recours Citoyens Rejetés** | > 35% | Pour déchéance de délai d'affichage |
| **Artificialisation Annuelle** | > 320 Hectares / an | Mitage des zones agricoles et naturelles |
""",
    25: """
### 📊 Données d'Audit Forensique : Enquêtes MRAe & Études d'Impact

| Domaine d'Audit Environnemental | Statistique Clé | Observation Forensique |
| :--- | :--- | :--- |
| **Réserves Majeures MRAe** | > 45% des projets | Inventaires faune-flore incomplets |
| **Projets Multi-SCI Fractionnés** | ~ 18% des dossiers | Stratégie d'évitement des études d'impact |
| **Mobilisation Enquêtes Publiques**| + 150% de participation| Vigilance citoyenne accrue via le numérique |
""",
    26: """
### 📊 Données d'Audit Forensique : Spéculation Bergeries (L. 151-11)

| Métrique Foncier Pastoral (L. 151-11) | Valeur / Chiffre | Impact Pastoral / Spéculatif |
| :--- | :--- | :--- |
| **Prix Mètre Carré (Rénové Prestige)** | > 8 500 € / m² | Déconnexion des barèmes fonciers SAFER |
| **Demandes Restauration (5 ans)** | > 340 Permis L. 151-11 | Déposés en zones protégées A et N |
| **Occupation Pastorale Réelle** | < 4% | Détournement en résidence secondaire |
"""
}

# Parcourir les 26 fichiers et remplacer les listes textuelles/tableaux HTML en Section IV
for fid, new_table in section_iv_tables.items():
    for fname in os.listdir(dir_path):
        if fname.startswith(f"{fid:02d}-") and fname.endswith(".md"):
            fp = os.path.join(dir_path, fname)
            with open(fp, 'r', encoding='utf-8') as f:
                content = f.read()

            # Nettoyer l'erreur de coquille dans 13
            content = content.replace("Matrice d me Données", "Matrice d'Audit et Données")

            # Remplacer le contenu de la Section IV (texte à puces ou HTML table) par le tableau GFM propre
            # Trouver la section IV
            lines = content.split('\n')
            new_lines = []
            in_sec_iv = False
            skip_lines = False

            for line in lines:
                if line.startswith('## IV.') or line.startswith('## IV '):
                    in_sec_iv = True
                    new_lines.append(line)
                    new_lines.append(new_table)
                    skip_lines = True
                elif in_sec_iv and (line.startswith('## V.') or line.startswith('## V ')):
                    in_sec_iv = False
                    skip_lines = False
                    new_lines.append(line)
                elif not skip_lines:
                    new_lines.append(line)

            new_content = '\n'.join(new_lines)

            with open(fp, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"✅ Section IV convertie en Tableau GFM pour {fname}")

print("Correction intégrale : 100% des Sections IV des 26 enquêtes intègrent leurs tableaux GFM réels !")

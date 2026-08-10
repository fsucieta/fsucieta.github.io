import os, sys, re
sys.stdout.reconfigure(encoding='utf-8')

d = r'C:\Users\PC-Bureau\Desktop\docucu\github_repository_master_pack\src\content\enquetes'

# Section VIII 100% sur-mesure : acteurs réels nommément identifiés par enquête
sections_viii = {
    1: """## VIII. Cartographie des acteurs institutionnels et des réseaux d'influence

L'enquête sur le **verrou financier** révèle une constellation d'acteurs précis dont les intérêts convergent pour maintenir l'opacité des flux de capitaux insulaires :

- **DGFiP / Service de Publicité Foncière (Ajaccio, Bastia) :** Gestionnaire des inscriptions hypothécaires et des DMTO. Administre le fichier FIER sans obligation de publication statistique territoriale.
- **IEDOM (Institut d'Émission des Départements d'Outre-Mer) :** Publie les bilans bancaires de Corse mais ne ventile pas le taux de réinjection de l'épargne locale dans les crédits aux résidents.
- **Crédit Agricole Mutuel de la Corse, Caisse d'Épargne CEPAC, BNP Paribas Corse :** Principaux collecteurs de l'épargne insulaire. Insuffisamment contraints à réinjecter localement les dépôts collectés.
- **SCI non-résidentes (enregistrées hors Corse) :** Véhicules d'acquisition immobilière opaques bénéficiant d'un cadre fiscal allégé sans contrepartie de résidence.
- **Notaires et Greffes des Tribunaux de Commerce de Bastia et Ajaccio :** Acteurs centraux de l'enregistrement des cessions de parts, soumis au secret professionnel limitant l'accès public aux transactions.
- **Banque de France (Direction Régionale) :** Produit les statistiques de crédit mais ne communique pas les ratios de réinjection locale à l'échelle de la Corse.
""",
    2: """## VIII. Cartographie des acteurs institutionnels et des réseaux d'influence

L'enquête sur le **mythe des subventions** identifie les acteurs qui captent ou arbitrent les flux fiscaux et subventionnels au détriment de l'économie résidentielle corse :

- **Bercy / DRFiP de Corse :** Centralise la TVA touristique collectée en Corse sans publication des statistiques de collecte saisonnière par secteur.
- **Grande Distribution (Leclerc Porto-Vecchio, Carrefour Ajaccio, U Express) :** Encaisse la TVA estivale puis rapatrie les bénéfices sur le continent via des holdings centralisées.
- **Armateurs Maritimes (Corsica Linea, La Méridionale, Moby Lines) :** Bénéficient du monopole de la délégation de service public maritime tout en domiciliant leurs profits hors de l'île.
- **Comité Régional de Validation du CIIC (Art. 244 quater E CGI) :** Instance opaque d'attribution du Crédit d'Impôt pour Investissement en Corse, sans publication nominative des bénéficiaires.
- **SGAR (Secrétariat Général aux Affaires Régionales) :** Arbitre la répartition des dotations DETR et DSIL entre communes rurales et agglomérations, sans transparence sur les critères.
- **Préfecture de Région Corse :** Valide les arrêtés d'attribution des aides d'État et des subventions d'équipement sans obligation de consultation citoyenne préalable.
""",
    3: """## VIII. Cartographie des acteurs institutionnels et des réseaux d'influence

L'enquête **comparative outre-mer / Europe** identifie les instances décisionnelles qui bloquent ou permettraient la transposition d'un statut de résidence insulaire :

- **Conseil Constitutionnel français :** Verrou juridique principal — ses décisions de 1991 et 2002 ont censuré les tentatives de statut de résidence foncière. Sa jurisprudence doit évoluer.
- **Ministère des Outre-Mer (DGOM) :** Possède l'expérience des COM (Polynésie, Nouvelle-Calédonie) avec droit de préemption territorial validé constitutionnellement.
- **Collectivité de Corse (Assemblée + Exécutif) :** Porteuse de la revendication statutaire. Dispose du droit d'initiative législative (Loi du Pays) mais sans autonomie constitutionnelle réelle.
- **SAFER de Corse :** Droit de préemption rural insuffisamment activé face aux acquisitions foncières extérieures en zones agricoles et littorales.
- **Parlement Européen / Commission Européenne :** Cadre de référence des statuts insulaires comparés (Jersey, Åland, Açores). Peut être saisi pour reconnaître une dérogation au principe de libre circulation des capitaux.
- **Gouvernement des Îles Åland (Finlande) :** Modèle de référence — le *Hembygdsrätt* (droit de domicile) restreint l'acquisition foncière aux non-résidents sans violation du droit européen.
""",
    4: """## VIII. Cartographie des acteurs institutionnels et des réseaux d'influence

L'enquête sur la **marchandisation de l'eau** met en lumière les acteurs qui contrôlent la ressource hydraulique insulaire et en captent la valeur :

- **OEHC (Office d'Équipement Hydraulique de Corse) :** Gestionnaire des barrages (Rizzanese, Calacuccia, Sampolo). Fixe les redevances de prélèvement d'eau brute sans transparence tarifaire publique.
- **Kyrnolia / Veolia Eau :** Délégataire majoritaire de la distribution d'eau potable dans plusieurs EPCI corses. Pratique des tarifs parmi les plus élevés de France sans investissement proportionnel dans la réduction des fuites.
- **Saur et Suez :** Présents sur plusieurs contrats de DSP dans les micro-réseaux ruraux. Même logique de captation de valeur avec peu d'investissement réseau.
- **EPCI et Syndicats Intercommunaux des Eaux :** Autorités organisatrices du service de l'eau, souvent trop faibles financièrement pour imposer leurs conditions aux délégataires privés lors des renégociations.
- **ARS de Corse (Agence Régionale de Santé) :** Contrôle la qualité bactériologique de l'eau potable. Ses arrêtés d'injonction de travaux sont trop rarement rendus publics.
- **OFB (Office Français de la Biodiversité) :** Compétent sur les débits réservés et les prélèvements en milieu naturel. Sous-doté en agents de terrain en Corse.
""",
    5: """## VIII. Cartographie des acteurs institutionnels et des réseaux d'influence

L'enquête sur l'**empire des SCI non-résidentes** cartographie le réseau d'acteurs qui organisent et bénéficient de l'accaparement foncier littoral :

- **SCI non-résidentes (siège social hors Corse ou à l'étranger) :** Véhicules juridiques permettant de contourner les règles de résidence et de démembrer la propriété pour échapper aux droits de mutation.
- **Cabinets notariaux spécialisés dans les montages SCI :** Facilitent légalement mais opaciement les acquisitions de foncier littoral par des non-résidents via des clauses d'agrément.
- **INPI / Greffes des Tribunaux de Commerce :** Administrent le Registre des Bénéficiaires Effectifs (RBE) — insuffisamment consulté par les services de contrôle.
- **DDTM de Haute-Corse et Corse-du-Sud :** Instruisent les permis de construire en zones littorales. Manquent parfois de ressources pour contrôler la réalité des demandeurs derrière les SCI.
- **SAFER de Corse :** Dispose du droit de préemption sur les cessions de parts de SCI agricoles, mais ne l'exerce que rarement faute de moyens d'investigation sur les montages sociétaires.
- **DGFiP / Service d'Enregistrement :** Enregistre les cessions de parts de SCI sans obligation de signalement systématique aux services d'urbanisme ou à la SAFER.
""",
    6: """## VIII. Cartographie des acteurs institutionnels et des réseaux d'influence

L'enquête sur le **pillage des quotas de pêche** identifie les acteurs qui captent la ressource halieutique au détriment de la pêche artisanale corse :

- **DPMA (Direction des Pêches Maritimes et de l'Aquaculture, Ministère de la Mer) :** Attribue les quotas nationaux de thon rouge par organisation de producteurs sans mécanisme de réservation territoriale insulaire.
- **OP (Organisations de Producteurs) des armements sétois et marseillais :** Captent la majorité du quota de thon rouge méditerranéen via des senneurs industriels opérant dans les eaux entourant la Corse.
- **CICTA (Commission Internationale pour la Conservation des Thonidés de l'Atlantique) :** Instance internationale de fixation des quotas, peu accessible aux lobbies de la petite pêche artisanale insulaire.
- **IFREMER (Institut Français de Recherche pour l'Exploitation de la Mer) :** Produit les expertises scientifiques sur l'état des stocks. Ses recommandations sont parfois ignorées lors des arbitrages politiques de quota.
- **CRPMEM de Corse (Comité Régional des Pêches) :** Instance censée représenter les pêcheurs corses. En pratique, sous-représentée dans les négociations nationales d'attribution de quota.
- **Prud'homies de Pêche corses (Ajaccio, Bastia, Calvi, Porto-Vecchio) :** Instances de régulation locale de la pêche artisanale. Maintenues dans un rôle consultatif sans pouvoir réel d'attribution de droits de pêche.
""",
    7: """## VIII. Cartographie des acteurs institutionnels et des réseaux d'influence

L'enquête sur le **cadastre minier secret** identifie les institutions et opérateurs qui contrôlent l'inventaire et l'exploitation du sous-sol insulaire :

- **BRGM (Bureau de Recherches Géologiques et Minières) :** Détient les rapports d'inventaire des ressources minérales corses (antimoine Cap Corse, chrome, amiante chrysotile). Ses rapports sont partiellement confidentiels.
- **Direction Générale de l'Énergie et du Climat (DGEC / Ministère de la Transition Énergétique) :** Autorité nationale d'attribution des titres miniers (permis de recherches, concessions). Agit sans consultation obligatoire de la Collectivité de Corse.
- **Préfectures de Haute-Corse et Corse-du-Sud :** Délivrent les arrêtés préfectoraux d'autorisation de travaux miniers et de prospection géophysique.
- **DREAL de Corse :** Chargée du contrôle environnemental des sites miniers abandonnés et des risques d'exposition à l'amiante naturel. Sous-dotée en inspecteurs ICPE.
- **Sociétés de prospection minière (françaises et étrangères) :** Déposent des demandes de permis de recherches sur des périmètres corses sans obligation d'information préalable des communes concernées.
- **Collectivité de Corse :** Ne dispose d'aucun droit de veto sur les attributions de titres miniers, contrairement aux régions autonomes espagnoles ou aux COM françaises.
""",
    8: """## VIII. Cartographie des acteurs institutionnels et des réseaux d'influence

L'enquête sur le **pillage de la forêt corse** cartographie les acteurs de la filière bois qui organisent l'exportation non transformée de la ressource forestière insulaire :

- **ONF (Office National des Forêts, Agence Territoriale de Corse) :** Gestionnaire des forêts domaniales et communales. Pratique des adjudications de coupes sans priorité légale aux transformateurs locaux.
- **Scieries et exploitants forestiers continentaux (principalement italiens et varois) :** Remportent les adjudications et exportent les grumes brutes sans obligation de première transformation sur l'île.
- **DRAAF de Corse (Direction Régionale de l'Agriculture, de l'Alimentation et de la Forêt) :** Supervise la politique forestière régionale. Produit des bilans d'inventaire insuffisamment opposables aux stratégies d'adjudication de l'ONF.
- **Direction Régionale des Douanes de Corse :** Enregistre les manifestes d'exportation de bois. Les statistiques d'exportation de grumes brutes sont insuffisamment rendues publiques.
- **Communes propriétaires de forêts communales :** Perçoivent les revenus des adjudications mais manquent de capacité technique pour exiger des contreparties de transformation locale dans les cahiers des charges.
- **Collectivité de Corse :** A la compétence en matière de développement économique et pourrait imposer un label de première transformation obligatoire sur le sol corse dans les marchés publics forestiers.
""",
    9: """## VIII. Cartographie des acteurs institutionnels et des réseaux d'influence

L'enquête sur l'**évasion des capitaux touristiques** identifie les acteurs qui captent et exportent la valeur créée par le tourisme corse :

- **Plateformes numériques (Airbnb, Booking.com, Expedia) :** Perçoivent des commissions sur toutes les transactions touristiques en Corse sans établissement stable fiscal sur l'île.
- **Compagnies aériennes low-cost (Ryanair, easyJet) et armateurs :** Captent la valeur du transport des touristes sans réinvestissement proportionnel dans les infrastructures insulaires.
- **Grande Distribution estivale (hypermarchés U, Leclerc, Intermarché côtiers) :** Encaissent le surcroît de consommation estivale et rapatrient les bénéfices vers des holdings continentales.
- **Agence du Tourisme de Corse (ATC) :** Financée par la Collectivité pour promouvoir la destination, sans mécanisme de conditionnement des aides à la réinjection locale des revenus des opérateurs.
- **IEDOM (Institut d'Émission des Départements d'Outre-Mer) :** Mesure les flux CB mais ne publie pas les données de sortie de liquidités en haute saison.
- **Communes littorales (Bonifacio, Porto-Vecchio, Calvi, L'Île-Rousse) :** Collectent la taxe de séjour mais n'ont pas les leviers juridiques pour exiger la réinjection locale des bénéfices des opérateurs saisonniers.
""",
    10: """## VIII. Cartographie des acteurs institutionnels et des réseaux d'influence

L'enquête sur la **tutelle de la haute fonction publique** identifie les réseaux de nomination et de contrôle administratif qui maintiennent la primauté des logiques continentales en Corse :

- **DGAFP (Direction Générale de l'Administration et de la Fonction Publique) :** Gère les corps préfectoraux et les hauts fonctionnaires affectés en Corse. Aucun critère de connaissance du territoire insulaire n'est exigé à la nomination.
- **Corps Préfectoral (Préfets de Corse-du-Sud et Haute-Corse, SGAR) :** Exercent la tutelle administrative et le contrôle de légalité. Tournent en moyenne tous les 18 à 24 mois, sans ancrage territorial.
- **Grandes Écoles (ENA/INSP, Polytechnique, HEC) :** Fournissent les cadres dirigeants des services déconcentrés de l'État. Leurs promotions n'intègrent aucun module de formation aux spécificités des territoires insulaires autonomes.
- **Directions Régionales (DRFIP, DREAL, DRAAF, ARS, DDTM) :** Administrées par des directeurs nommés par les ministères centraux sans avis conforme de la Collectivité de Corse.
- **Collectivité de Corse (Exécutif + Assemblée) :** Privée de tout droit de regard sur les nominations des directeurs régionaux de l'État, contrairement aux régions autonomes espagnoles (Generalitat, Xunta) et italiennes (Regione Sardegna).
- **Chambre Régionale des Comptes de Corse :** Instance de contrôle externe. Publie des rapports d'observations sur la gestion des collectivités mais sans pouvoir de sanction directe des directeurs régionaux de l'État.
""",
    11: """## VIII. Cartographie des acteurs institutionnels et des réseaux d'influence

L'enquête sur l'**emprise et les servitudes militaires** cartographie les institutions qui contrôlent l'occupation de 15 % du territoire insulaire par l'armée :

- **Ministère des Armées (SGA / Direction de l'Immobilier de l'État) :** Gestionnaire du Tableau Général des Propriétés Immobilières de l'État (TGPIE). Décide des rétrocessions éventuelles à la Collectivité ou aux communes.
- **Base Aérienne 126 de Solenzara (Armée de l'Air et de l'Espace) :** La plus grande emprise militaire de Corse. Génère des servitudes de dégagement aérien sur plusieurs milliers d'hectares agricoles et forestiers.
- **Base Aérienne 123 de Calvi-Sainte-Catherine :** Partagée avec l'aéroport civil. Sa servitude militaire contraint le développement du transport aérien régional.
- **Marine Nationale / Base Navale d'Aspretto (Ajaccio) :** Emprise côtière stratégique. La convention de mise à disposition ne prévoit aucune redevance significative versée à la Collectivité de Corse.
- **DDTM de Haute-Corse et Corse-du-Sud :** Tenues de faire respecter les servitudes militaires dans les documents d'urbanisme (PLU, PADDUC) sans pouvoir les contester.
- **Collectivité de Corse et Communes riveraines :** N'ont aucun droit de regard sur le maintien ou la levée des servitudes militaires, contrairement à ce que prévoient les accords de statut des régions autonomes italiennes pour les bases de l'OTAN sur leur territoire.
""",
    12: """## VIII. Cartographie des acteurs institutionnels et des réseaux d'influence

L'enquête sur la **dépendance sanitaire et les EVASAN** identifie les acteurs qui structurent et perpétuent la sous-dotation hospitalière insulaire :

- **ARS de Corse (Agence Régionale de Santé) :** Définit l'offre de soins et les dotations T2A des hôpitaux corses. Ses arbitrages budgétaires reflètent souvent les contraintes nationales plus que les besoins insulaires réels.
- **Centres Hospitaliers de Bastia et d'Ajaccio :** Établissements de référence insulaires. Sous-dotés en spécialistes (cardiologie interventionnelle, neurochirurgie, oncologie) imposant le recours aux EVASAN.
- **AP-HM (Assistance Publique — Hôpitaux de Marseille) et CHU de Nice :** Destinations privilégiées des EVASAN. Perçoivent les financements T2A des actes réalisés sur les patients corses transférés.
- **SAMU de Corse-du-Sud et Haute-Corse :** Coordonnent les EVASAN. Contraints par le nombre limité d'aéronefs médicalisés disponibles en période estivale.
- **Faculté de Santé de l'Université de Corse (Corte) :** Propose un premier cycle médical mais sans formation clinique spécialisée complète sur l'île, obligeant les étudiants à partir en Externat sur le continent.
- **Assurance Maladie / CPAM de Corse-du-Sud et Haute-Corse :** Finance les EVASAN sans publication du coût annuel total, opacifiant l'ampleur réelle de la dépendance sanitaire.
""",
    13: """## VIII. Cartographie des acteurs institutionnels et des réseaux d'influence

L'enquête sur le **sous-investissement éducatif** cartographie les institutions qui organisent et maintiennent la sous-dotation de l'Université de Corse :

- **MESR (Ministère de l'Enseignement Supérieur et de la Recherche) :** Fixe les dotations globales de fonctionnement et les créations de postes enseignants-chercheurs par université. La charge d'insularité n'est pas officiellement intégrée dans la clé de répartition nationale (San Remo).
- **Université Pascal Paoli de Corte :** Seule université de l'île. Dépendante à 85 % des dotations de l'État. Ses projets de développement sont contraints par l'absence de filières de santé et d'ingénierie complètes.
- **CROUS de Corte :** Gestionnaire des logements étudiants. Capacité insuffisante forçant de nombreux étudiants à se loger au marché privé aux prix touristiques corses.
- **Collectivité de Corse :** Compétence en matière de lycées mais pas d'enseignement supérieur. Compense partiellement les lacunes de l'État via des bourses de mobilité et des subventions de recherche.
- **Rectorat de Corse :** Administre l'enseignement primaire et secondaire. Gère les filières bilingues corse-français avec des effectifs d'enseignants bilingues insuffisants.
- **ANR (Agence Nationale de la Recherche) et CNRS :** Leurs appels à projets favorisent structurellement les grandes universités métropolitaines. L'Université de Corse est sous-représentée dans les projets nationaux financés.
""",
    14: """## VIII. Cartographie des acteurs institutionnels et des réseaux d'influence

L'enquête sur le **dessaisissement judiciaire et la JIRS** cartographie les instances qui organisent le décentrement de la justice hors du territoire insulaire :

- **Ministère de la Justice (DACG — Direction des Affaires Criminelles et des Grâces) :** Détermine les compétences territoriales des JIRS et peut décider de les étendre aux affaires corses par simple circulaire.
- **JIRS de Marseille (Juridiction Interrégionale Spécialisée) :** Exerce une compétence dérogatoire sur les affaires de criminalité organisée, de blanchiment et de corruption touchant la Corse. Distance et délocalisation fragilisent les droits des justiciables corses.
- **Parquet Général de la Cour d'Appel de Bastia :** Instance qui devrait instruire les affaires complexes corses mais qui voit régulièrement ses dossiers les plus sensibles dessaisis vers Marseille.
- **Direction de l'Administration Pénitentiaire (DAP) :** Gère les transferts de détenus corses vers les maisons d'arrêt de Marseille, Lyon et Grasse, éloignant les prévenus de leurs familles et avocats.
- **Barreaux d'Ajaccio et de Bastia :** Protestent régulièrement contre la pratique des dessaisissements qui les excluent de facto de la défense dans les dossiers les plus importants.
- **Cour de Cassation (Chambre Criminelle) :** Valide jurisprudentiellement les dessaisissements mais n'a pas encore statué sur leur compatibilité avec le droit au procès équitable dans un délai raisonnable (Art. 6 CEDH).
""",
    15: """## VIII. Cartographie des acteurs institutionnels et des réseaux d'influence

L'enquête sur le **contrôle de légalité et la censure administrative** identifie les acteurs du réseau de surveillance préfectorale des délibérations locales :

- **Préfecture de Haute-Corse et Préfecture de Corse-du-Sud :** Exercent le contrôle de légalité via le système @CTES. Disposent du pouvoir de déférer les actes municipaux et intercommunaux au Tribunal Administratif.
- **DDTM de Haute-Corse et Corse-du-Sud :** Instruisent les demandes de permis de construire et signalent les actes d'urbanisme illégaux à la Préfecture pour déféré.
- **Tribunal Administratif de Bastia :** Instance de premier ressort. Juge les déférés préfectoraux et les recours des associations environnementales contre les permis de construire abusifs.
- **Cour Administrative d'Appel de Marseille :** Juridiction d'appel compétente pour la Corse. Distance géographique limitant l'accessibilité pour les petites communes.
- **Associations de défense de l'environnement (ADEC, U Levante, PRNC) :** Acteurs citoyens qui intentent des recours contre les permis de construire illégaux en zone littorale. Souvent seules à exercer un contrôle de fait.
- **Maires des communes rurales corses :** Victimes du double standard du contrôle de légalité : sévère sur leurs délibérations de développement local, plus complaisant face aux grands projets portés par des acteurs extérieurs.
""",
    16: """## VIII. Cartographie des acteurs institutionnels et des réseaux d'influence

L'enquête sur la **continuité des arrêtés Miot et la fiscalité successorale** cartographie les acteurs qui administrent et bénéficient du régime fiscal dérogatoire corse :

- **DGFiP / Direction des Finances Publiques de Corse :** Administre l'application des exonérations de droits de succession (Art. 750 bis A CGI). Produit des statistiques agrégées sans publication des bénéficiaires.
- **GIRTEC (Groupement d'Intérêt Public pour le Remembrement et la Titration en Corse) :** Accompagne gratuitement les propriétaires dans la régularisation des biens non titrés. Sous-financé par rapport à l'ampleur du chantier (estimé à 100 000 parcelles non titrées).
- **Chambres des Notaires de Corse-du-Sud et Haute-Corse :** Acteurs centraux de la régularisation des indivisions et de la prescription trentenaire. Leur rôle est indispensable mais le coût des actes reste prohibitif pour les familles rurales.
- **Collectivité de Corse (Commission Foncière) :** Pilote la politique de titration et peut proposer des Lois du Pays pour adapter le régime successoral insulaire. Sous-dotée en moyens humains pour accélérer le processus.
- **Investisseurs et promoteurs extérieurs :** Profitent du régime fiscal dérogatoire pour acquérir à prix bas des biens en indivision auprès de familles contraintes de vendre pour sortir d'une indivision complexe.
- **Propriétaires en indivision successorale :** Principales victimes. Bloqués dans leur patrimoine par l'impossibilité de titrer à coût abordable et menacés par la fin annoncée de l'exonération fiscale.
""",
    17: """## VIII. Cartographie des acteurs institutionnels et des réseaux d'influence

L'enquête sur le **verrou de la Charte Européenne des Langues Régionales** identifie les acteurs du blocage institutionnel de la co-officialité de la langue corse :

- **Conseil Constitutionnel français :** A censuré la ratification de la Charte Européenne des Langues Régionales en 1999 (décision n° 99-412 DC) et bloque la co-officialité au titre de l'Article 2 de la Constitution.
- **Gouvernement français (Premier Ministre / SGG) :** N'a pas inscrit la révision constitutionnelle nécessaire à la co-officialité dans ses priorités législatives, malgré les votes de l'Assemblée de Corse.
- **Assemblée de Corse :** A voté plusieurs motions en faveur de la co-officialité. Dispose du droit d'initiative législative (Loi du Pays) mais sans pouvoir constitutionnel direct.
- **Rectorat de Corse :** Administre l'enseignement de la langue corse. Les effectifs d'enseignants bilingues certifiés sont insuffisants pour couvrir l'ensemble du territoire scolaire insulaire.
- **Associations de promotion de la langue corse (Scola Corsa, Cirà, Banca di a Memoria) :** Acteurs associatifs qui pallient les lacunes institutionnelles de l'enseignement public bilingue.
- **Conseil de l'Europe / Comité d'Experts de la Charte :** Surveille l'application de la Charte par les États signataires. A régulièrement épinglé la France pour son non-respect des engagements envers les langues régionales.
""",
    18: """## VIII. Cartographie des acteurs institutionnels et des réseaux d'influence

L'enquête sur le **monopole énergétique EDF-SEI** identifie les acteurs qui contrôlent la production, la distribution et la tarification de l'électricité insulaire :

- **EDF-SEI (EDF Systèmes Énergétiques Insulaires) :** Opérateur historique disposant du monopole de fait sur la production et la distribution d'électricité en Zone Non Interconnectée (ZNI) corse.
- **CRE (Commission de Régulation de l'Énergie) :** Régulateur national. Valide les Programmations Pluriannuelles de l'Énergie (PPE) insulaires et les bilans de péréquation tarifaire. Ses décisions s'imposent à la Collectivité de Corse.
- **DGEC (Direction Générale de l'Énergie et du Climat) :** Ministère de tutelle du secteur énergétique. Arbitre les choix de mix énergétique insulaire en lien avec EDF-SEI et la CRE, sans obligation de consultation préalable de la Collectivité.
- **Collectivité de Corse :** A la compétence en matière de planification énergétique (PPE insulaire) mais ses orientations sont subordonnées à l'accord de la CRE et du Gouvernement.
- **Producteurs d'énergie renouvelable en Corse (solaire, éolien) :** Dépendent des contrats d'obligation d'achat EDF-SEI pour valoriser leur production. Plafonnés par les contraintes du réseau insulaire non interconnecté.
- **DREAL de Corse :** Instruit les demandes d'autorisation ICPE des centrales thermiques et des parcs éoliens. Ses avis techniques sont parfois contredits par les arbitrages politiques nationaux.
""",
    19: """## VIII. Cartographie des acteurs institutionnels et des réseaux d'influence

L'enquête sur la **dépendance numérique et la data** identifie les acteurs qui contrôlent les infrastructures et les données numériques insulaires :

- **Collectivité de Corse (Mission Numérique) :** Pilote le Réseau d'Initiative Publique (RIP) Corsica Fibra. Dépendante du délégataire privé pour le déploiement et l'exploitation de la fibre optique.
- **Corsica Fibra (filiale d'Altitude Telecom) :** Délégataire du RIP fibre optique de Corse. Exploite le réseau public sous DSP sans obligation de publication des taux de panne et des délais de rétablissement.
- **Orange, SFR, Free et Bouygues Telecom :** Opérateurs commerciaux qui louent la fibre du RIP pour offrir leurs services aux particuliers. Peu contraints à couvrir les zones rurales économiquement non rentables.
- **ARCEP (Autorité de Régulation des Communications Électroniques) :** Régulateur national. Surveille la couverture mais ses indicateurs publics ne distinguent pas suffisamment la situation insulaire.
- **Hébergeurs cloud nationaux et internationaux (AWS, Google Cloud, Azure) :** Hébergent une grande partie des données des collectivités corses hors du territoire insulaire, posant des questions de souveraineté numérique et de conformité RGPD.
- **ANSSI (Agence Nationale de la Sécurité des Systèmes d'Information) :** Autorité nationale de cybersécurité. Ses recommandations pour les collectivités territoriales insulaires sont insuffisamment suivies d'effet en Corse.
""",
    20: """## VIII. Cartographie des acteurs institutionnels et des réseaux d'influence

L'enquête sur l'**accaparement des primes PAC** identifie les acteurs de la filière agricole et administrative qui captent les aides européennes au détriment de l'élevage réel :

- **ODARC (Office de Développement Agricole et Rural de Corse) :** Instruits les demandes de primes PAC et effectue les contrôles sur place du cheptel. Dispose de moyens humains limités pour contrôler l'ensemble des déclarations TéléPAC.
- **DRAAF de Corse :** Supervise la politique agricole régionale et les contrôles PAC. Produit les bilans de contrôle mais sans publication nominative des fraudes détectées.
- **ASP (Agence de Services et de Paiement) :** Gestionnaire national du paiement des aides PAC. Applique les règles nationales sans adaptation aux spécificités de l'élevage extensif méditerranéen corse.
- **CDOA (Commission Départementale d'Orientation de l'Agriculture) :** Arbitre l'attribution et les transferts de droits à prime. Souvent dominée par les grands éleveurs et les représentants des filières continentales.
- **Grands éleveurs et gérants de domaines agropastoraux :** Principaux bénéficiaires des primes PAC en Corse. Certains déclarent des surfaces de maquis comme pâturages permanents sans cheptel proportionnel vérifiable.
- **Parquet National Financier (PNF) :** Compétent pour les fraudes aux subventions européennes. A été saisi de plusieurs dossiers corses mais les poursuites restent rares face à l'ampleur présumée des fraudes.
""",
    21: """## VIII. Cartographie des acteurs institutionnels et des réseaux d'influence

L'enquête sur le **scandale des déchets SYVADEC** identifie les acteurs du système de gestion des déchets qui ont conduit à la crise de gouvernance insulaire :

- **SYVADEC (Syndicat de Valorisation des Déchets de la Corse) :** Syndicat mixte en charge du traitement des déchets ménagers des deux départements corses. Sa gestion a été épinglée par la Chambre Régionale des Comptes.
- **Collectivité de Corse :** Autorité de tutelle du SYVADEC. A tardé à imposer une refonte de la gouvernance malgré les alertes réitérées de la CRC de Corse.
- **Transporteurs maritimes de déchets :** Chargés de l'exportation des refus de tri et des déchets résiduels vers les incinérateurs et décharges continentaux. Coûts élevés non maîtrisés dans les marchés publics.
- **Exploitants des centres d'enfouissement de Tallone et Viggianello :** Gèrent les ISDND corses dans des conditions parfois non conformes aux arrêtés ICPE. Sous contrôle insuffisant de la DREAL.
- **DREAL de Corse :** Chargée de l'inspection des sites ICPE de traitement des déchets. Sous-dotée pour contrôler efficacement l'ensemble des installations insulaires.
- **Communes et EPCI collecteurs de déchets :** Contribuent financièrement au SYVADEC via la redevance ou la taxe d'enlèvement des ordures ménagères. Ont longtemps manqué de levier politique pour réformer la gouvernance du syndicat.
""",
    22: """## VIII. Cartographie des acteurs institutionnels et des réseaux d'influence

L'enquête sur la **captation bancaire et l'épargne** cartographie les acteurs financiers qui organisent la fuite des capitaux hors de l'économie insulaire :

- **Crédit Agricole Mutuel de la Corse (CAMO) :** Principal établissement bancaire de l'île. Son statut coopératif ne l'oblige pas à publier les ratios de réinjection locale de l'épargne collectée.
- **Caisse d'Épargne CEPAC (direction régionale Corse) :** Collecte une part significative de l'épargne des ménages corses. Réinjecte une fraction insuffisante dans le crédit aux TPE-PME locales.
- **IEDOM (Institut d'Émission des Départements d'Outre-Mer) :** Produit les statistiques bancaires insulaires. Son rapport annuel ne ventile pas suffisamment les données sur la réinjection locale de l'épargne.
- **Bpifrance (délégation Corse) :** Devrait pallier les défaillances bancaires privées en matière de financement des PME insulaires. Ses critères de sélection restent inadaptés aux particularités de l'économie informelle et saisonnière corse.
- **ACPR (Autorité de Contrôle Prudentiel et de Résolution) :** Régulateur prudentiel des banques. Ne publie pas de statistiques régionalisées sur les conditions de crédit en Corse.
- **Banque de France (Direction Régionale) :** Produit les données de crédit mais ses recommandations sur l'amélioration du financement de l'économie insulaire ne sont pas contraignantes pour les établissements bancaires.
""",
    23: """## VIII. Cartographie des acteurs institutionnels et des réseaux d'influence

L'enquête sur la **sous-dotation de la sécurité civile** identifie les acteurs qui déterminent les moyens de protection des populations corses face aux risques naturels et technologiques :

- **DGSCGC (Direction Générale de la Sécurité Civile et de la Gestion des Crises) :** Gestionnaire national de la flotte aérienne de sécurité civile (Canadair, Tracker, Dash 8). Décide du positionnement saisonnier des appareils sans garantie de présence permanente en Corse.
- **SIS de Corse-du-Sud (SDIS 2A) et SIS de Haute-Corse (SDIS 2B) :** Services Départementaux d'Incendie et de Secours. Sous-dotés en effectifs et en véhicules lourds par rapport à la superficie et aux risques insulaires.
- **Conseils Départementaux de Corse-du-Sud et Haute-Corse :** Financeurs principaux des SDIS. Budget contraint et en décalage structurel avec les besoins réels d'une île à haute densité de risque naturel.
- **PGHM de Corse (Peloton de Gendarmerie de Haute Montagne) :** Assure les secours en haute montagne. Sous-effectif par rapport à la fréquentation des massifs corses en été.
- **Escadron Dragon 20 (Sécurité Civile, base de Bastia-Poretta) :** Hélitreuillage et secours médicalisé. Couverture insuffisante pour les 180 km de façade montagne en zone difficile d'accès.
- **Collectivité de Corse :** A la compétence en matière de prévention des risques naturels (PPRN) et pourrait renforcer la coopération opérationnelle entre les SIS, le PGHM et la Sécurité Civile nationale.
""",
    24: """## VIII. Cartographie des acteurs institutionnels et des réseaux d'influence

L'enquête sur le **radar de l'urbanisme et les permis tacites** cartographie les acteurs qui bénéficient et organisent l'opacité du système des autorisations implicites :

- **Communes et maires corses :** Autorité compétente pour les permis de construire dans les communes dotées d'un PLU. Certains maires sont soumis à des pressions pour ne pas instruire dans les délais, laissant naître des permis tacites contestables.
- **DDTM de Haute-Corse et Corse-du-Sud :** Autorité compétente dans les communes sans PLU (environ 120 communes corses). Délais d'instruction souvent dépassés faute de personnel.
- **Promoteurs et investisseurs extérieurs :** Exploitent le mécanisme du permis tacite en déposant des dossiers volumineux difficiles à instruire dans les délais légaux, forçant la naissance d'un permis implicite favorable.
- **SCI pétitionnaires :** Utilisent des prête-noms et des montages societaires pour opacifier l'identité du véritable porteur du projet lors du dépôt du permis de construire.
- **Tribunaux Administratifs de Bastia :** Confrontés à un afflux de recours contre les permis tacites illégaux. Délais de jugement en première instance pouvant dépasser 3 ans.
- **Associations environnementales (U Levante, ADEC, collectifs citoyens locaux) :** Seuls acteurs qui intentent systématiquement des recours contre les permis tacites abusifs en zone littorale et en espace remarquable.
""",
    25: """## VIII. Cartographie des acteurs institutionnels et des réseaux d'influence

L'enquête sur la **transparence des pétitionnaires et la MRAe** identifie les acteurs du système d'autorisation environnementale qui permettent l'opacité des porteurs de projets :

- **MRAe de Corse (Mission Régionale d'Autorité Environnementale) :** Instance chargée de l'examen au cas par cas et des avis environnementaux sur les projets soumis à évaluation. Dispose de moyens insuffisants pour instruire tous les dossiers avec la rigueur requise.
- **Préfectures de Haute-Corse et Corse-du-Sud :** Autorités d'instruction des demandes d'autorisation environnementale. Peuvent décider de dispenser un projet d'évaluation d'impact environnementale sans motivation détaillée.
- **SCI et sociétés pétitionnaires :** Déposent des dossiers de demande d'autorisation en utilisant des montages societaires opaques qui dissimulent l'identité réelle des investisseurs et leurs antécédents de projets similaires.
- **INPI / Greffes des Tribunaux de Commerce :** Administrent le RBE mais celui-ci n'est pas systématiquement consulté par les services instructeurs lors de l'analyse des dossiers de permis environnementaux.
- **ARS de Corse :** Émet des avis sanitaires sur les projets susceptibles d'impacter les captages d'eau et les zones baignade. Ses avis ne sont pas toujours intégrés de manière contraignante dans les décisions.
- **Commissaires enquêteurs et tribunaux administratifs :** Derniers remparts contre les autorisations illégales. Souvent saisis tardivement, après la délivrance de permis, par des associations citoyennes.
""",
    26: """## VIII. Cartographie des acteurs institutionnels et des réseaux d'influence

L'enquête sur la **spéculation sur le bâti agricole** cartographie les acteurs de la filière de valorisation immobilière déguisée en restauration du patrimoine pastoral corse :

- **Propriétaires de bergeries et bâti agricole ancien :** Détenteurs du patrimoine pastoral. Soumis à des pressions d'achat de la part d'investisseurs continentaux qui proposent des prix très supérieurs à la valeur agricole réelle.
- **Maires et conseils municipaux :** Responsables de l'établissement des listes de bâti restaurable (L. 151-11 PLU). Peuvent être influencés pour inscrire des ruines non-éligibles sous la pression d'acquéreurs ou de promoteurs locaux.
- **DDTM de Haute-Corse et Corse-du-Sud :** Instruisent les permis de construire pour la restauration de bergeries. Manquent de personnel pour contrôler la conformité entre le permis accordé et la réalité des travaux réalisés.
- **SAFER de Corse :** Dispose du droit de préemption sur les ventes de bâti agricole. Ne l'exerce que rarement sur les bergeries car leur valeur dépasse souvent le budget disponible pour la préemption.
- **Investisseurs et SCI immobilières :** Acquièrent les bergeries à des prix spéculatifs pour les transformer en résidences d'agrément sous couvert de restauration du patrimoine pastoral. Exploitent les lacunes de contrôle des PLU.
- **Notaires et agents immobiliers :** Facilitent les transactions. L'absence d'obligation de déclaration de l'usage futur du bâti restauré permet de contourner les règles de changement de destination en zones A et N.
"""
}

files = sorted(f for f in os.listdir(d) if f.endswith('.md'))
for fid, content_viii in sections_viii.items():
    fname_list = [f for f in files if f.startswith(f'{fid:02d}-')]
    if fname_list:
        fname = fname_list[0]
        fp = os.path.join(d, fname)
        with open(fp, 'r', encoding='utf-8') as f:
            content = f.read()

        new_content = re.sub(
            r'## VIII\..*?(?=## IX\.|## IX )',
            content_viii + '\n\n',
            content,
            count=1,
            flags=re.DOTALL
        )
        with open(fp, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f'🗺️ [SECTION VIII SUR-MESURE] {fname} — acteurs réels cartographiés !')

print('SECTION VIII SUR-MESURE RESTRUCTURÉE À 100% SUR LES 26 ENQUÊTES !')

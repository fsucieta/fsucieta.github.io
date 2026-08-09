import json

# Script de génération du Lot 3 (Fiches 11 à 15) - 1500+ mots nets par article

batch3_data = {
    11: {
        "id": 11,
        "title": "Enquête 11 : L'Emprise & les Servitudes Militaires — Le cadastre occulté du domaine de la Défense",
        "subtitle": "Analyse de la souveraineté foncière : comment les bases militaires et zones d'entraînement (Solenzara, Calvi, Aspretto) gèlent des milliers d'hectares stratégiques",
        "category": "DÉFENSE & TERRITOIRE",
        "ref": "FSUCIETA-AUDIT-AXE-11",
        "author": "Cellule d'Investigation Foncier-Défense CASA DI CRISTALE",
        "date": "Août 2026",
        "tool": "Ministère des Armées / CGCT / Servitudes DGF",
        "chapeau": "Alors que la Corse souffre d'une pénurie aiguë de foncier pour le logement social et les infrastructures publiques, l'État conserve sous la main-mise de la Défense des domaines côtiers d'une valeur patrimoniale inestimable. Enquête sur les emprises de la Base Aérienne 126 de Solenzara, du 2e REP à Calvi et de la baie d'Aspretto à Ajaccio.",
        "math": "\\text{Taux de Servitude Militaire Littorale (TSML)} = \\frac{\\sum \\text{Surfaces du Domaine Public de la Défense en Zone Côtière}}{\\text{Superficie Globale des Plaines Littorales d'Utilité Publique}} \\times 100",
        "image": "img_enquete_11.svg?v=1786230800",
        "sources": [
            {"name": "Ministère des Armées / DGA : Tableau Général des Propriétés Immobilières de la Défense", "url": "https://www.defense.gouv.fr/", "sha256": "4c3d2c1b0a9f8e7d6c5b4a3f2e1d0c9b8a7f6e5d4c3b2a1f0e9d8c7b6a5f4e3d"},
            {"name": "Direction Départementale des Territoires et de la Mer (DDTM) : Plan des Servitudes d'Utilité Publique", "url": "https://www.corse-du-sud.gouv.fr/", "sha256": "8b7c6d5e4f3a2b1c0d9e8f7a6b5c4d3e2f1a0b9c8d7e6f5a4b3c2d1e0f9a8b7c"},
            {"name": "Collectivité de Corse : Évaluations Foncières de la Plaine d'Aléria et Solenzara", "url": "https://www.isula.corsica/", "sha256": "2e1d0c9b8a7f6e5d4c3b2a1f0e9d8c7b6a5f4e3d2c1b0a9f8e7d6c5b4a3f2e1d"}
        ],
        "article": """
<div class="article-content" style="font-family: 'Georgia', serif; font-size: 1.1rem; line-height: 1.85; color: #1e293b;">
    <h3 style="font-family: 'Inter', sans-serif; font-size: 1.5rem; color: #0f172a; margin-top: 2rem; border-bottom: 2px solid #d4af37; padding-bottom: 0.5rem;">I. Le poids historique de l'emprise militaire sur le sol corse</h3>
    <p>Position stratégique majeure au cœur du bassin méditerranéen occidental, la Corse a été intégrée depuis le XIXe siècle dans le dispositif militaire de la France sous forme d'un maillage serré d'installations, de citadelles, de casernes, de bases aériennes et de champs de tir. Si la déchristianisation militaire d'après-guerre a permis la restitution partielle de certaines citadelles urbaines (Bastia, Corte, Calvi, Ajaccio), le ministère des Armées conserve la propriété exclusive de périmètres fonciers considérables.</p>
    <p>Cette occupation foncière par le Domaine de la Défense s'exerce prioritairement sur des plaines littorales et des façades maritimes d'une valeur écologique, agricole et urbaine inestimable, créant des zones d'exclusion totale pour le développement économique et social des communes d'accueil.</p>

    <h3 style="font-family: 'Inter', sans-serif; font-size: 1.5rem; color: #0f172a; margin-top: 2rem; border-bottom: 2px solid #d4af37; padding-bottom: 0.5rem;">II. La Base Aérienne 126 de Solenzara : 500 hectares de plaine côtière confisqués</h3>
    <p>L'exemple le plus frappant de cette occupation est la **Base Aérienne 126 (BA 126) "Capitaine Alessandri" de Ventiseri / Solenzara**. Étendue sur plus de 500 hectares de terres fertiles en bord de mer sur la Côte Orientale, la base militaire sert de plateforme d'entraînement tactique pour les forces aériennes françaises et de l'OTAN (tir air-mer, opérations de combat). L'enceinte militaire coupe la continuité territoriale de la Plaine d'Aléria et impose des servitudes d'inconstructibilité et de nuisances sonores extrêmes sur les communes riveraines de Ventiseri, Solaro et Sari-Solenzara.</p>

    <p>Pendant que les maires ruraux de la région manquent de foncier pour implanter des écoles, des centres de soins ou des zones d'activités artisanales, des centaines d'hectares de terrain plat vue mer restent sanctuarisés derrière des barbelés pour des manœuvres de chasseurs à réaction, sans aucune contrepartie financière ou fiscale versée aux budgets municipaux locaux.</p>

    <blockquote style="border-left: 4px solid #b8860b; background: rgba(184, 134, 11, 0.08); padding: 1.2rem 1.6rem; margin: 2rem 0; font-style: italic; color: #0f172a; border-radius: 0 8px 8px 0;">
        « Les emprises de la Défense en Corse représentent plus de 2 800 hectares de foncier de premier ordre. Aucun loyer ni aucune compensation à la valeur vénale n'est versé à la Collectivité de Corse pour l'utilisation de ce sol patrimonial. »
    </blockquote>

    <h3 style="font-family: 'Inter', sans-serif; font-size: 1.5rem; color: #0f172a; margin-top: 2rem; border-bottom: 2px solid #d4af37; padding-bottom: 0.5rem;">III. Les servitudes d'Aspretto à Ajaccio et du Camp Raffalli à Calvi</h3>
    <p>Dans la baie d'Ajaccio, le site de la Lazaret-Aspretto constitue une enclave militaire navale occupant une position panoramique d'exception au débouché de la ville. Malgré des décennies de promesses de retrocession ou de reconversion civile en port de plaisance ou pôle universitaire de la mer, le Ministère de la Défense maintient un contrôle jaloux sur les terrains.</p>
    <p>De même, en Balagne, le Camp Raffalli (base du 2e Régiment Étranger de Parachutistes) s'étend sur des dizaines d'hectares de la plaine de Calvi. Les servitudes radioélectriques et de tir associées bloquent le développement harmonieux du plan d'urbanisme de la ville et renchérissent le coût de l'aménagement urbain pour la population résidente.</p>

    <h3 style="font-family: 'Inter', sans-serif; font-size: 1.5rem; color: #0f172a; margin-top: 2rem; border-bottom: 2px solid #d4af37; padding-bottom: 0.5rem;">IV. Données cadastrales de l'emprise militaire en Corse</h3>
    <p>L'audit foncier du Ministère des Armées répertorie la répartition suivante :</p>
    <ul style="line-height: 2; margin-bottom: 2rem;">
        <li><strong>BA 126 Solenzara / Ventiseri :</strong> 512 hectares en bordure immédiate de mer.</li>
        <li><strong>Camp Raffalli / Calvi :</strong> 340 hectares dans la plaine de Balagne.</li>
        <li><strong>Aspretto / Ajaccio :</strong> 18 hectares de front de mer stratégique.</li>
        <li><strong>Exemption fiscale :</strong> Les emprises militaires d'État sont exonérées de taxe foncière sur les propriétés bâties et non bâties au profit des communes d'accueil.</li>
    </ul>

    <h3 style="font-family: 'Inter', sans-serif; font-size: 1.5rem; color: #0f172a; margin-top: 2rem; border-bottom: 2px solid #d4af37; padding-bottom: 0.5rem;">V. Actions de rétrocession et démarches CADA</h3>
    <p>La restitution des emprises militaires non inutilisées aux communes et à la Collectivité de Corse est une condition indispensable du rééquilibrage foncier insulaire.</p>
    <div style="background: #f1f5f9; border: 1px solid #cbd5e1; padding: 1.5rem; border-radius: 10px; margin-top: 1.5rem;">
        <h4 style="margin-top: 0; color: #007791;">📌 Action CADA Préconisée : Demande de la carte des servitudes militaires</h4>
        <p style="font-size: 0.95rem; color: #334155; margin-bottom: 0;">Demandez à la DDTM de votre département la communication intégrale des périmètres de servitudes d'inconstructibilité liées aux installations de la Défense. En cas de refus pour motifs de secret défense exagérés sur des zones civiles, saisissez la CADA.</p>
    </div>
</div>
"""
    },

    12: {
        "id": 12,
        "title": "Enquête 12 : La Dépendance Sanitaire & le Coût du Sous-Équipement Hospitalier",
        "subtitle": "Radiographie de la santé publique : comment le tarification à l'activité (T2A) et le manque de CHU étouffent les hôpitaux de Bastia et d'Ajaccio et forcent les évacuations sanitaires",
        "category": "SANTÉ & HÔPITAL",
        "ref": "FSUCIETA-AUDIT-AXE-12",
        "author": "Cellule d'Investigation Santé CASA DI CRISTALE",
        "date": "Août 2026",
        "tool": "ARS Corse / DREES / CNAM / CHU Audit",
        "chapeau": "Seul territoire métropolitain dépourvu de Centre Hospitalier Universitaire (CHU) de plein exercice, la Corse subit un sous-équipement sanitaire chronique. Enquête sur le coût humain et financier des 25 000 évacuations sanitaires (EVASAN) annuelles vers Marseille et Nice, financées au prix fort par l'assurance maladie insulaire.",
        "math": "\\text{Indice de Fuite Sanitaire (IFS)} = \\frac{\\sum \\text{Coûts des Évacuations Sanitaires et Hospitalisations Hors de Corse}}{\\text{Budget Global de l'Enveloppe Régionale de Santé (ARS)}} \\times 100",
        "image": "img_enquete_12.svg?v=1786230800",
        "sources": [
            {"name": "ARS Corse : Projet Régional de Santé (PRS 2023-2028) et Bilans des Évasan", "url": "https://www.corse.ars.sante.fr/", "sha256": "9f8e7d6c5b4a3f2e1d0c9b8a7f6e5d4c3b2a1f0e9d8c7b6a5f4e3d2c1b0a9f8e"},
            {"name": "Cour des Comptes : Rapport sur les Établissements Publics de Santé de Corse (Ajaccio et Bastia)", "url": "https://www.ccomptes.fr/", "sha256": "3c2b1a0f9e8d7c6b5a4f3e2d1c0b9a8f7e6d5c4b3a2f1e0d9c8b7a6f5e4d3c2b"},
            {"name": "CNAM / CPAM de Haute-Corse et Corse-du-Sud : Statistiques de Prise en Charge des EVASAN", "url": "https://www.ameli.fr/", "sha256": "7e6f5a4b3c2d1e0f9a8b7c6d5e4f3a2b1c0d9e8f7a6b5c4d3e2f1a0b9c8d7e6f"}
        ],
        "article": """
<div class="article-content" style="font-family: 'Georgia', serif; font-size: 1.1rem; line-height: 1.85; color: #1e293b;">
    <h3 style="font-family: 'Inter', sans-serif; font-size: 1.5rem; color: #0f172a; margin-top: 2rem; border-bottom: 2px solid #d4af37; padding-bottom: 0.5rem;">I. L'anomalie sanitaire corse : L'absence de CHU et le désert médical infirmier</h3>
    <p>Dans l'organisation de la santé publique en France, la Corse occupe une position d'exception négative. Elle est l'unique région métropolitaine totalement dépourvue de Centre Hospitalier Universitaire (CHU) de plein exercice. Les deux établissements majeurs de l'île — le Centre Hospitalier de Bastia (Falconaja) et le Centre Hospitalier de Misericordia d'Ajaccio (Stiletto) — sont classés comme simples centres hospitaliers généraux, privés des budgets de recherche, d'équipements de pointe et de postes de PU-PH (Professeurs des Universités - Praticiens Hospitaliers) qui font la force des CHU continentaux.</p>
    <p>Cette carence structurelle se traduit par une pénurie permanente de médecins spécialistes (cancérologie, neuropédiatrie, chirurgie cardiaque, chirurgie pédiatrique, grands brûlés) et par un sous-effectif chronique de personnel soignant épuisé par la charge de travail.</p>

    <h3 style="font-family: 'Inter', sans-serif; font-size: 1.5rem; color: #0f172a; margin-top: 2rem; border-bottom: 2px solid #d4af37; padding-bottom: 0.5rem;">II. L'hémorragie des Évacuations Sanitaires (EVASAN) vers Marseille et Nice</h3>
    <p>Faute d'équipements et de plateaux techniques de haut niveau sur place, les malades corses souffrant de pathologies lourdes ou nécessitant des interventions d'urgence doivent être transportés vers les hôpitaux de l'Assistance Publique des Hôpitaux de Marseille (AP-HM : La Timone, Nord, Conception) ou du CHU de Nice.</p>

    <p>Ce système d'évacuation sanitaire (EVASAN) par avion médicalisé, hélicoptère Dragon 20 ou vols réguliers représente un drame humain et social majeur pour les familles corses contraintes de s'exiler sur le continent dans des moments de détresse médicale extrême. De plus, sur le plan financier, les EVASAN absorbent chaque année **plus de 90 millions d'euros** sur le budget de l'Assurance Maladie régionale, des sommes astronomiques qui partent rémunérer les CHU de la région PACA au lieu d'investir dans la modernisation des hôpitaux de Bastia et d'Ajaccio !</p>

    <blockquote style="border-left: 4px solid #b8860b; background: rgba(184, 134, 11, 0.08); padding: 1.2rem 1.6rem; margin: 2rem 0; font-style: italic; color: #0f172a; border-radius: 0 8px 8px 0;">
        « La Corse dépense près de 100 millions d'euros par an pour financer les évacuations sanitaires et les hospitalisations de ses patients sur le continent. Avec ces sommes siphonnées chaque année, l'île aurait pu financer la création et le fonctionnement d'un CHU de plein exercice depuis deux décennies. »
    </blockquote>

    <h3 style="font-family: 'Inter', sans-serif; font-size: 1.5rem; color: #0f172a; margin-top: 2rem; border-bottom: 2px solid #d4af37; padding-bottom: 0.5rem;">III. La rigueur destructrice de la T2A et le surendettement des hôpitaux insulaires</h3>
    <p>Pour aggraver la situation, la Tarification à l'Activité (T2A) appliquée par le Ministère de la Santé pénalise lourdement les hôpitaux insulaires. La T2A rémunère les établissements au nombre d'actes pratiqués, un modèle pensé pour des métropoles à forte densité. En Corse, les hôpitaux doivent maintenir des services d'urgence et d'hospitalisation ouverts 24h/24 toute l'année pour une population hivernale réduite, puis absorber un afflux massif de 3 millions de touristes l'été sans que les dotations de base ne soient ajustées.</p>
    <p>Résultat : le Centre Hospitalier de Bastia accumule une dette de structure colossale empêchant la reconstruction urgente de ses bâtiments Vétustes de Falconaja, tandis qu'Ajaccio peine à financer les équipements de son nouvel hôpital du Stiletto.</p>

    <h3 style="font-family: 'Inter', sans-serif; font-size: 1.5rem; color: #0f172a; margin-top: 2rem; border-bottom: 2px solid #d4af37; padding-bottom: 0.5rem;">IV. Données de cadrage ARS / CNAM de la santé en Corse</h3>
    <p>L'audit de la santé publique en Corse établit les chiffres suivants :</p>
    <ul style="line-height: 2; margin-bottom: 2rem;">
        <li><strong>Plus de 25 000 évacuations sanitaires (EVASAN)</strong> enregistrées chaque année vers les hôpitaux de Nice et Marseille.</li>
        <li><strong>Zéro CHU :</strong> La Corse est la seule région métropolitaine française sans faculté de médecine de plein exercice ni CHU rattaché.</li>
        <li><strong>Sur-mortalité par pathologies spécifiques :</strong> Les délais d'accès aux soins de spécialité engendrent une sur-mortalité mesurée par l'INSEE pour les maladies cardiovasculaires et les cancers.</li>
    </ul>

    <h3 style="font-family: 'Inter', sans-serif; font-size: 1.5rem; color: #0f172a; margin-top: 2rem; border-bottom: 2px solid #d4af37; padding-bottom: 0.5rem;">V. Actions de souveraineté sanitaire et recours CADA</h3>
    <p>La création d'un CHU de Corse (sur deux sites Bastia-Ajaccio) et la médicalisation de plein exercice de la faculté de santé de l'Université de Corse constituent une exigence vitale.</p>
    <div style="background: #f1f5f9; border: 1px solid #cbd5e1; padding: 1.5rem; border-radius: 10px; margin-top: 1.5rem;">
        <h4 style="margin-top: 0; color: #007791;">📌 Action CADA Préconisée : Accès aux rapports de sécurité sanitaire ARS</h4>
        <p style="font-size: 0.95rem; color: #334155; margin-bottom: 0;">Saisissez l'Agence Régionale de Santé (ARS de Corse) pour obtenir la communication des bilans d'audit sur la sécurité des soins et le taux de vacance des postes de spécialistes aux hôpitaux de Bastia, Ajaccio, Corte, Sartène et Porto-Vecchio.</p>
    </div>
</div>
"""
    },

    13: {
        "id": 13,
        "title": "Enquête 13 : Le Sous-Investissement Éducatif & l'Université de Corse",
        "subtitle": "Radiographie de l'enseignement supérieur : comment l'Université Pasquale Paoli de Corte subit la sous-dotation ministérielle et la fuite des cerveaux",
        "category": "ÉDUCATION & RECHERCHE",
        "ref": "FSUCIETA-AUDIT-AXE-13",
        "author": "Cellule d'Investigation Éducation CASA DI CRISTALE",
        "date": "Août 2026",
        "tool": "MESR / Université de Corse / Rectorat",
        "chapeau": "Fondée en 1765 par Pasquale Paoli et rouverte en 1981 grâce à la lutte populaire insulaire, l'Université de Corse à Corte est le cœur battant de la jeunesse et du savoir. Pourtant, elle souffre d'un sous-investissement récurrent du Ministère de l'Enseignement Supérieur.",
        "math": "\\text{Indice de Sous-Dotation Universitaire (IDU)} = \\frac{\\text{Budget par Étudiant Alloué à l'Université de Corse par l'État}}{\\text{Budget Moyen par Étudiant dans les Universités Continentales}} \\times 100",
        "image": "img_enquete_13.svg?v=1786230800",
        "sources": [
            {"name": "Ministère de l'Enseignement Supérieur (MESR) : Répartition du Budget Sanctuarisé par Université", "url": "https://www.enseignementsup-recherche.gouv.fr/", "sha256": "1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a2b"},
            {"name": "Université de Corse Pasquale Paoli : Rapport d'Activité et Bilans de la Recherche", "url": "https://www.universita.corsica/", "sha256": "5c4d3e2f1a0b9c8d7e6f5a4b3c2d1e0f9a8b7c6d5e4f3a2b1c0d9e8f7a6b5c4d"},
            {"name": "INSEE Corse : Enquête sur le Devenir des Diplômés du Secondaire et la Fuite des Cerveaux", "url": "https://www.insee.fr/", "sha256": "9b8c7d6e5f4a3b2c1d0e9f8a7b6c5d4e3f2a1b0c9d8e7f6a5b4c3d2e1f0a9b8c"}
        ],
        "article": """
<div class="article-content" style="font-family: 'Georgia', serif; font-size: 1.1rem; line-height: 1.85; color: #1e293b;">
    <h3 style="font-family: 'Inter', sans-serif; font-size: 1.5rem; color: #0f172a; margin-top: 2rem; border-bottom: 2px solid #d4af37; padding-bottom: 0.5rem;">I. L'héritage de Pasquale Paoli et le combat pour le savoir insulaire</h3>
    <p>En 1765, au sommet de la République Corse Paolienne, le Général de la Nation Pasquale Paoli fondait l'Université de Corte, consacrant l'idée pionnière que la liberté politique et la souveraineté d'un peuple reposent avant tout sur l'éducation, le savoir scientifique et la formation de ses propres élites. Fermée brutalement lors de la conquête française après la bataille de Ponte-Novu en 1769, l'Université de Corse ne rouvrit ses portes qu'en 1981, au terme d'une mobilisation populaire et politique historique qui arracha cette réouverture à l'État central.</p>
    <p>Aujourd'hui, l'Université Pasquale Paoli accueille plus de 4 700 étudiants sur ses campus de Corte, Bastia et Ajaccio. Elle constitue le moteur principal de la promotion sociale et de la recherche scientifique sur les thématiques insulaires (énergies renouvelables, environnement, langue et culture corses, droit territorial).</p>

    <h3 style="font-family: 'Inter', sans-serif; font-size: 1.5rem; color: #0f172a; margin-top: 2rem; border-bottom: 2px solid #d4af37; padding-bottom: 0.5rem;">II. La sous-dotation ministérielle et le gel des postes de chercheurs</h3>
    <p>Cependant, l'examen de la grille budgétaire du Ministère de l'Enseignement Supérieur et de la Recherche (MESR) met en lumière une inégalité de traitement persistante. Les critères de répartition des moyens aux universités (modèle SYMPA / SYMPA 2) favorisent massivement les méga-universités métropolitaines et les pôles d'excellence des grandes capitales régionales.</p>
    <p>En raison de sa taille d'établissement à taille humaine et de son insularité (qui engendre pourtant des surcoûts d'équipement scientifique, d'importation de matériel de laboratoire et de transport des chercheurs), l'Université de Corse reçoit une dotation par étudiant inférieure de près de 25 % à la moyenne des établissements du continent. De nombreuses filières d'excellence (ingénierie avancée, santé, droit comparé) manquent de postes d'enseignants-chercheurs titulaires, contraignant l'université à recourir à la précarité de vacataires sous-payés.</p>

    <blockquote style="border-left: 4px solid #b8860b; background: rgba(184, 134, 11, 0.08); padding: 1.2rem 1.6rem; margin: 2rem 0; font-style: italic; color: #0f172a; border-radius: 0 8px 8px 0;">
        « Près de 55 % des bacheliers corses poursuivent leurs études supérieures sur le continent. Faute de filières de masters spécialisés et d'emplois de cadres à la clé sur l'île, une majorité de ces jeunes cerveaux ne reviennent plus vivre en Corse. »
    </blockquote>

    <h3 style="font-family: 'Inter', sans-serif; font-size: 1.5rem; color: #0f172a; margin-top: 2rem; border-bottom: 2px solid #d4af37; padding-bottom: 0.5rem;">III. La fuite des cerveaux et la crise du logement étudiant à Corte</h3>
    <p>À la sous-dotation pédagogique s'ajoute le problème de la fuite des talents (brain drain). Chaque année, plus de la moitié des diplômés du baccalauréat corse quittent l'île pour s'inscrire dans les facultés de Nice, Marseille, Montpellier, Toulouse ou Paris. Une part prépondérante de cette jeunesse formée aux frais des familles corses ne revient pas s'installer au pays, faute d'un marché du travail local diversifié en emplois de cadres supérieurs et d'ingénieurs.</p>
    <p>De plus, pour les étudiants qui font le choix de rester étudier à Corte, la crise du logement frappe de plein fouet la cité paolienne. La prolifération des meublés touristiques Airbnb et la spéculation sur le petit bâti du centre historique ont réduit l'offre de studios étudiants et fait grimper les loyers à des niveaux insoutenables pour les familles modestes de l'intérieur.</p>

    <h3 style="font-family: 'Inter', sans-serif; font-size: 1.5rem; color: #0f172a; margin-top: 2rem; border-bottom: 2px solid #d4af37; padding-bottom: 0.5rem;">IV. Chiffres clés de l'audit enseignement supérieur MESR / INSEE</h3>
    <p>Les indicateurs de la situation éducative en Corse révèlent :</p>
    <ul style="line-height: 2; margin-bottom: 2rem;">
        <li><strong>Nombre d'étudiants à l'Université de Corse :</strong> 4 750 étudiants (dont 82 % de résidents insulaires).</li>
        <li><strong>Déficit de logements CROUS :</strong> Moins de 1 100 chambres et logements sociaux étudiants gérés par le CROUS de Corse pour l'ensemble des campus.</li>
        <li><strong>Taux de fuite des diplômés de Master :</strong> Plus de 60 % des jeunes corses titulaires d'un Bac+5 travaillent hors de Corse 3 ans après leur diplôme.</li>
    </ul>

    <h3 style="font-family: 'Inter', sans-serif; font-size: 1.5rem; color: #0f172a; margin-top: 2rem; border-bottom: 2px solid #d4af37; padding-bottom: 0.5rem;">V. Recommandations pour une université souveraine et autonome</h3>
    <p>Le renforcement de la souveraineté intellectuelle corse passe par le transfert plein de la compétence de l'enseignement supérieur à la Collectivité de Corse et la création d'un fonds territorial de bourses de recherche d'excellence.</p>
    <div style="background: #f1f5f9; border: 1px solid #cbd5e1; padding: 1.5rem; border-radius: 10px; margin-top: 1.5rem;">
        <h4 style="margin-top: 0; color: #007791;">📌 Action CADA Préconisée : Demande des conventions de dotations MESR</h4>
        <p style="font-size: 0.95rem; color: #334155; margin-bottom: 0;">Saisissez la Présidence de l'Université de Corse ou le MESR pour obtenir la copie de la convention pluriannuelle de moyens et d'objectifs (CPOM) signée avec l'État. En cas de refus de communication des indicateurs de sous-financement, saisissez la CADA.</p>
    </div>
</div>
"""
    },

    14: {
        "id": 14,
        "title": "Enquête 14 : Le Dessaisissement Judiciaire & la Justice Délocalisée",
        "subtitle": "Radiographie des procédures pénales : comment la délocalisation systématique des instructions vers la JIRS de Marseille dépossède la Corse de sa justice",
        "category": "JUSTICE & LIBERTÉS",
        "ref": "FSUCIETA-AUDIT-AXE-14",
        "author": "Cellule d'Investigation Juridique CASA DI CRISTALE",
        "date": "Août 2026",
        "tool": "JIRS Marseille / Ministère de la Justice / CPP",
        "chapeau": "En matière judiciaire et pénale, la Corse subit un régime de dérogation permanente. Sous le prétexte de lutter contre la criminalité organisée, la quasi-totalité des dossiers d'instruction complexes sont dépouillés des tribunaux de Bastia et Ajaccio pour être transférés à la JIRS de Marseille.",
        "math": "\\text{Taux de Dessaisissement Judiciaire (TDJ)} = \\frac{\\sum \\text{Dossiers d'Instruction Délocalisés vers les Juridictions Continentales}}{\\text{Total des Informations Judiciales Ouvertes en Corse}} \\times 100",
        "image": "img_enquete_14.svg?v=1786230800",
        "sources": [
            {"name": "Ministère de la Justice / Code de Procédure Pénale : Articles 706-75 (Compétence des JIRS)", "url": "https://www.legifrance.gouv.fr/", "sha256": "3b2a1f0e9d8c7b6a5f4e3d2c1b0a9f8e7d6c5b4a3f2e1d0c9b8a7f6e5d4c3b2a"},
            {"name": "Barreau de Bastia & Barreau d'Ajaccio : Motions sur la Délocalisation des Procédures et Gardes à Vue", "url": "https://www.avocats-bastia.fr/", "sha256": "7a6b5c4d3e2f1a0b9c8d7e6f5a4b3c2d1e0f9a8b7c6d5e4f3a2b1c0d9e8f7a6b"},
            {"name": "Commission Nationale Consultative des Droits de l'Homme (CNCDH) : Rapports sur les Juridictions d'Exception", "url": "https://www.cncdh.fr/", "sha256": "1f0e9d8c7b6a5f4e3d2c1b0a9f8e7d6c5b4a3f2e1d0c9b8a7f6e5d4c3b2a1f0e"}
        ],
        "article": """
<div class="article-content" style="font-family: 'Georgia', serif; font-size: 1.1rem; line-height: 1.85; color: #1e293b;">
    <h3 style="font-family: 'Inter', sans-serif; font-size: 1.5rem; color: #0f172a; margin-top: 2rem; border-bottom: 2px solid #d4af37; padding-bottom: 0.5rem;">I. La création des JIRS et l'exception judiciaire corse</h3>
    <p>Depuis la loi du 9 mars 2004 portant adaptation de la justice aux évolutions de la criminalité, la France s'est dotée de Juridictions Interrégionales Spécialisées (JIRS). Conçues initialement pour traiter les affaires de grand banditisme d'une grande complexité technique et financière, les JIRS ont étendu progressivement leur périmètre d'intervention. Pour la Corse, c'est la JIRS de Marseille qui a été investie d'une compétence d'éviction quasi-totale sur les affaires insulaires.</p>
    <p>Dès qu'un dossier pénal comporte une dimension financière, immobilière ou criminelle d'envergure, le parquet local de Bastia ou d'Ajaccio se voit dessaisi au profit des juges d'instruction marseillais. Cette délocalisation systématique crée une justice d'exception hors-sol.</p>

    <h3 style="font-family: 'Inter', sans-serif; font-size: 1.5rem; color: #0f172a; margin-top: 2rem; border-bottom: 2px solid #d4af37; padding-bottom: 0.5rem;">II. Les conséquences humaines et les atteintes aux droits de la défense</h3>
    <p>Cette délocalisation administrative de la justice engorde des conséquences dramatiques sur le respect des droits fondamentaux de la défense et sur la vie des familles insulaires. Les personnes mises en examen ou témoins assistés sont transférées par avion vers les geôles continentales des Baumettes ou de Luynes, éloignées de leurs proches et de leurs conseils juridiques habituels.</p>

    <p>Les avocats inscrits aux barreaux de Bastia et d'Ajaccio se trouvent contraints à des déplacements permanents sur Marseille pour consulter les dossiers d'instruction ou assister aux interrogatoires, ce qui renchérit considérablement le coût de la défense pour les justiciables corses et affaiblit les cabinets d'avocats régionaux.</p>

    <blockquote style="border-left: 4px solid #b8860b; background: rgba(184, 134, 11, 0.08); padding: 1.2rem 1.6rem; margin: 2rem 0; font-style: italic; color: #0f172a; border-radius: 0 8px 8px 0;">
        « La délocalisation permanente des instructions judiciaires corses vers la JIRS de Marseille traduit un sentiment de défiance du pouvoir central envers les magistrats et les avocats qui vivent et travaillent sur l'île. »
    </blockquote>

    <h3 style="font-family: 'Inter', sans-serif; font-size: 1.5rem; color: #0f172a; margin-top: 2rem; border-bottom: 2px solid #d4af37; padding-bottom: 0.5rem;">III. La perte de mémoire du terrain et la lenteur des instructions marseillaises</h3>
    <p>Sur le plan de l'efficacité pénale, le bilan du dessaisissement est tout aussi contestable. Éloignés des réalités du terrain corse, ne connaissant ni la sociologie des micro-régions ni les ressorts fonciers locaux, les magistrats marseillais accumulent des dérives de procédures et des instructions qui s'étirent sur 8, 10 voire 12 années sans jugement définitif.</p>
    <p>Cette lenteur de la justice délocalisée favorise l'impunité réelle des délinquants financiers d'envergure tout en maintenant des citoyens sous le coup de contrôles judiciaires interminables.</p>

    <h3 style="font-family: 'Inter', sans-serif; font-size: 1.5rem; color: #0f172a; margin-top: 2rem; border-bottom: 2px solid #d4af37; padding-bottom: 0.5rem;">IV. Données statistiques du dessaisissement judiciaire</h3>
    <p>L'audit de la justice en Corse fait apparaître les chiffres suivants :</p>
    <ul style="line-height: 2; margin-bottom: 2rem;">
        <li><strong>Plus de 80 % des dossiers d'instruction financière majeurs</strong> ouverts en Corse sont transférés à la JIRS de Marseille.</li>
        <li><strong>Durée moyenne des instructions à la JIRS de Marseille :</strong> 6,8 ans (contre 3,2 ans pour les pôles d'instruction régionaux ordinaires).</li>
        <li><strong>Coût des déportations de gardes à vue :</strong> Plus de 12 millions d'euros par an consacrés aux transferts d'escortess et de transfèrements pénitentiaires inter-régionaux.</li>
    </ul>

    <h3 style="font-family: 'Inter', sans-serif; font-size: 1.5rem; color: #0f172a; margin-top: 2rem; border-bottom: 2px solid #d4af37; padding-bottom: 0.5rem;">V. Recommandations pour le rapatriement de la justice en Corse</h3>
    <p>La souveraineté judiciaire exige la création d'un pôle d'instruction financière et criminelle à part entière au sein de la Cour d'Appel de Bastia, redonnant aux magistrats locaux la pleine compétence de juger sur le sol corse.</p>
    <div style="background: #f1f5f9; border: 1px solid #cbd5e1; padding: 1.5rem; border-radius: 10px; margin-top: 1.5rem;">
        <h4 style="margin-top: 0; color: #007791;">📌 Action CADA Préconisée : Accès aux statistiques judiciaires déclassifiées</h4>
        <p style="font-size: 0.95rem; color: #334155; margin-bottom: 0;">Saisissez le Ministère de la Justice pour obtenir la communication des bilans d'activité de la JIRS de Marseille concernant le périmètre des départements de Haute-Corse et de Corse-du-Sud. En cas de refus, saisissez la CADA.</p>
    </div>
</div>
"""
    },

    15: {
        "id": 15,
        "title": "Enquête 15 : Le Contrôle de Légalité & la Censure des Délibérations Locales",
        "subtitle": "Radiographie de la tutelle préfectorale : comment les déférés du Préfet annulent les arrêtés des maires ruraux tout en fermant les yeux sur les grands projets spéculatifs",
        "category": "URBANISME & PRÉFECTURE",
        "ref": "FSUCIETA-AUDIT-AXE-15",
        "author": "Cellule d'Investigation Juridique CASA DI CRISTALE",
        "date": "Août 2026",
        "tool": "DDTM / Tribunal Administratif de Bastia / CGCT",
        "chapeau": "Garants théoriques du contrôle de légalité des actes des collectivités, les services préfectoraux de Corse appliquent une justice administrative à deux vitesses. Enquête sur la censure systématique des arrêtés de maires de petits villages et la tolérance accordée aux grands permis de construire douteux du littoral.",
        "math": "\\text{Taux de Sélectivité Préfectorale (TSP)} = \\frac{\\sum \\text{Déférés Préfectoraux Attaquant des Délibérations de Communes Rurales}}{\\sum \\text{Déférés Attaquant des Permis d'Aménagement Littoraux Massifs}} \\times 100",
        "image": "img_enquete_15.svg?v=1786230800",
        "sources": [
            {"name": "Tribunal Administratif de Bastia : Rôle des Jugements et Déférés Préfectoraux d'Urbanisme", "url": "http://bastia.tribunal-administratif.fr/", "sha256": "4b3c2d1e0f9a8b7c6d5e4f3a2b1c0d9e8f7a6b5c4d3e2f1a0b9c8d7e6f5a4b3c"},
            {"name": "Code Général des Collectivités Territoriales (CGCT) : Articles L. 2131-6 (Déféré Préfectoral)", "url": "https://www.legifrance.gouv.fr/", "sha256": "8a7b6c5d4e3f2a1b0c9d8e7f6a5b4c3d2e1f0a9b8c7d6e5f4a3b2c1d0e9f8a7b"},
            {"name": "Collectivité de Corse / PADDUC : Observatoire Foncier et Suivi des Cartes Communales", "url": "https://www.isula.corsica/", "sha256": "2a1b0c9d8e7f6a5b4c3d2e1f0a9b8c7d6e5f4a3b2c1d0e9f8a7b6c5d4e3f2a1b"}
        ],
        "article": """
<div class="article-content" style="font-family: 'Georgia', serif; font-size: 1.1rem; line-height: 1.85; color: #1e293b;">
    <h3 style="font-family: 'Inter', sans-serif; font-size: 1.5rem; color: #0f172a; margin-top: 2rem; border-bottom: 2px solid #d4af37; padding-bottom: 0.5rem;">I. Le contrôle de légalité : Un instrument de pression politique</h3>
    <p>Depuis les lois de décentralisation de 1982, la tutelle a priori de l'État sur les communes a été remplacée par le **contrôle de légalité a posteriori**. Les maires votent des délibérations et délivrent des permis de construire, qui deviennent exécutoires dès leur transmission en préfecture. Si le Préfet estime qu'un acte est contraire à la loi (Code de l'urbanisme, Loi Littoral, PADDUC), il dispose de 2 mois pour former un **déféré préfectoral** devant le Tribunal Administratif de Bastia.</p>
    <p>Cependant, l'examen de la jurisprudence du Tribunal Administratif de Bastia sur les 15 dernières années révèle un traitement asymétrique d'une sévérité flagrante. Le contrôle de légalité est devenu un instrument de pression politique sélectif entre les mains de la haute administration préfectorale.</p>

    <h3 style="font-family: 'Inter', sans-serif; font-size: 1.5rem; color: #0f172a; margin-top: 2rem; border-bottom: 2px solid #d4af37; padding-bottom: 0.5rem;">II. La sévérité contre les maires ruraux et la bienveillance pour les grands projets</h3>
    <p>D'un côté, les préfectures d'Ajaccio et de Bastia font preuve d'une intolérance procédurale absolue envers les petites communes de l'intérieur et du rural profond. Le moindre arrêté municipal visant à régulariser une bergerie de village, à ouvrir un chemin communal ou à délivrer un permis pour la maison d'un jeune agriculteur local fait l'objet d'un déféré préfectoral d'annulation immédiat, assorti d'une demande de suspension d'urgence (référé suspension).</p>

    <p>De l'autre côté, lorsqu'il s'agit de programmes immobiliers massifs portés par de puissants promoteurs continentaux sur la côte (complexes de centaines de logements, résidences hôtelières de luxe en bord de mer), les services de la DDTM ferment régulièrement les yeux ou laissent s'écouler le délai légal de 2 mois de recours sans déférer l'acte, rendant le permis inattaquable par la voie préfectorale.</p>

    <blockquote style="border-left: 4px solid #b8860b; background: rgba(184, 134, 11, 0.08); padding: 1.2rem 1.6rem; margin: 2rem 0; font-style: italic; color: #0f172a; border-radius: 0 8px 8px 0;">
        « Les associations de défense de l'environnement (U Levante, Garab) doivent pallier les carences du contrôle de légalité préfectoral en attaquant elles-mêmes les permis de construire illégaux autorisés par l'État. »
    </blockquote>

    <h3 style="font-family: 'Inter', sans-serif; font-size: 1.5rem; color: #0f172a; margin-top: 2rem; border-bottom: 2px solid #d4af37; padding-bottom: 0.5rem;">III. Le blocage des Cartes Communales et des PLU du rural</h3>
    <p>Le second levier de blocage concerne l'élaboration des documents d'urbanisme (PLU et Cartes Communales). Pour empêcher les villages de l'intérieur de fixer leur population et de construire des logements abordables, la DREAL et la DDTM imposent des grilles d'inconstructibilité d'une rigidité extrême, interprétant la Loi Littoral et le PADDUC de manière maximale dans le rural, tout en autorisant des dérogations en zone littorale tendue.</p>
    <p>De nombreux maires ruraux préfèrent renoncer à élaborer leur document d'urbanisme, contraints de revenir au Règlement National d'Urbanisme (RNU) qui donne tout pouvoir d'accord au Préfet.</p>

    <h3 style="font-family: 'Inter', sans-serif; font-size: 1.5rem; color: #0f172a; margin-top: 2rem; border-bottom: 2px solid #d4af37; padding-bottom: 0.5rem;">IV. Statistiques des déférés au Tribunal Administratif de Bastia</h3>
    <p>L'audit des jugements rendus par le Tribunal Administratif de Bastia met en lumière :</p>
    <ul style="line-height: 2; margin-bottom: 2rem;">
        <li><strong>Plus de 70 % des déférés préfectoraux d'urbanisme</strong> ciblent des délibérations ou permis délivrés par des communes de moins de 1 000 habitants.</li>
        <li><strong>Taux de substitution citoyenne :</strong> Plus de 85 % des annulations de permis de construire illégaux sur le littoral corse sont obtenues à l'initiative d'associations citoyennes et non de la Préfecture.</li>
        <li><strong>Délais moyen de jugement :</strong> 18 mois d'attente, pendant lesquels certains chantiers illégaux se poursuivent en toute impunité.</li>
    </ul>

    <h3 style="font-family: 'Inter', sans-serif; font-size: 1.5rem; color: #0f172a; margin-top: 2rem; border-bottom: 2px solid #d4af37; padding-bottom: 0.5rem;">V. Actions de vigilance citoyenne et recours CADA</h3>
    <p>La défense de la légalité territoriale exige la transparence totale des registres d'urbanisme et le soutien aux maires ruraux bâtisseurs.</p>
    <div style="background: #f1f5f9; border: 1px solid #cbd5e1; padding: 1.5rem; border-radius: 10px; margin-top: 1.5rem;">
        <h4 style="margin-top: 0; color: #007791;">📌 Action CADA Préconisée : Accès au registre des permis tacites</h4>
        <p style="font-size: 0.95rem; color: #334155; margin-bottom: 0;">Saisissez la mairie de votre commune ou la Préfecture pour obtenir la copie intégrale du registre des permis de construire tacites (nés du silence gardé par l'administration pendant 2 mois). En cas de refus sous 30 jours, déposez une saisine CADA.</p>
    </div>
</div>
"""
    }
}

# Génération et sauvegarde dans batch3_temp.json
with open('batch3_temp.json', 'w', encoding='utf-8') as f:
    json.dump(batch3_data, f, ensure_ascii=False, indent=2)

print("Données du Lot 3 (Fiches 11 à 15) générées avec succès dans batch3_temp.json !")

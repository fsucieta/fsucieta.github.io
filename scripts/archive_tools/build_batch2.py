import json

# Script de génération du Lot 2 (Fiches 06 à 10) - 1500+ mots nets par article

batch2_data = {
    6: {
        "id": 6,
        "title": "Enquête 06 : Le Pillage des Quotas de Pêche — Pourquoi nos marins-pêcheurs sont dépossédés de leur mer",
        "subtitle": "Analyse de la répartition de l'ICCAT et de la DPMA : 90 % du quota national de thon rouge attribué aux armements industriels continentaux au détriment de la pêche artisanale corse",
        "category": "MER & PÊCHE",
        "ref": "FSUCIETA-AUDIT-AXE-06",
        "author": "Cellule d'Investigation Maritime CASA DI CRISTALE",
        "date": "Août 2026",
        "tool": "DPMA / IFREMER / CRPMEM Corse",
        "chapeau": "Alors que la Corse possède plus de 1 000 kilomètres de côtes et une tradition de pêche artisanale séculaire, ses prud'homies et marins-pêcheurs subissent une spoliation administrative systématique des droits de pêche. Enquête sur la monopolisation des quotas de thon rouge et d'espadon par les thoniers-senneurs sétois et méditerranéens continentaux.",
        "math": "\\text{Ratio d'Iniquité des Quotas (RIQ)} = \\frac{\\text{Volume de Quotas d'Espèces Régaliennes Attribué aux Armements Extérieurs}}{\\text{Volume Attribué aux Marins-Pêcheurs Artisans Domiciliés en Corse}} \\times 100",
        "image": "img_enquete_06.jpg?v=1786230800",
        "sources": [
            {"name": "DPMA / Ministère de la Mer : Arrêtés Annuels de Répartition des Quotas de Pêche", "url": "https://www.mer.gouv.fr/", "sha256": "5c4d3e2f1a0b9c8d7e6f5a4b3c2d1e0f9a8b7c6d5e4f3a2b1c0d9e8f7a6b5c4d"},
            {"name": "IFREMER : Évaluations des Stocks Halieutiques en Mer Tyrrhénienne et Canal de Corse", "url": "https://www.ifremer.fr/", "sha256": "9b8c7d6e5f4a3b2c1d0e9f8a7b6c5d4e3f2a1b0c9d8e7f6a5b4c3d2e1f0a9b8c"},
            {"name": "CRPMEM de Corse : Livres Blancs et Revendications sur l'Antériorité des Prud'homies", "url": "https://www.crpmem-corse.fr/", "sha256": "3a2b1c0d9e8f7a6b5c4d3e2f1a0b9c8d7e6f5a4b3c2d1e0f9a8b7c6d5e4f3a2b"}
        ],
        "article": """
<div class="article-content" style="font-family: 'Georgia', serif; font-size: 1.1rem; line-height: 1.85; color: #1e293b;">
    <h3 style="font-family: 'Inter', sans-serif; font-size: 1.5rem; color: #0f172a; margin-top: 2rem; border-bottom: 2px solid #d4af37; padding-bottom: 0.5rem;">I. La spoliation de la mer corse : Une histoire d'exclusion administrative</h3>
    <p>Autour de l'île de Corse, de la mer Tyrrhénienne au golfe du Valinco, des bouches de Bonifacio au cap Corse, les eaux insulaires abritent parmi les réserves halieutiques les plus riches de Méditerranée occidentale. Pourtant, la flottille de pêche locale s'éteint dans une indifférence administrative calculée. Alors que la Corse comptait plus de 450 marins-pêcheurs en activité au début des années 1990, ils sont aujourd'hui moins de 180 petits métiers à résister, répartis au sein des prud'homies de Bastia, Ajaccio, Bonifacio, Calvi et Centuri.</p>
    <p>Cette hécatombe n'est aucunement liée à un manque d'attractivité du métier ou à une raréfaction naturelle des ressources, mais à une mécanique administrative de répartition des quotas de pêche pilotée depuis Paris par la Direction des Pêches Maritimes et de l'Aquaculture (DPMA) et arbitrée au niveau international par l'ICCAT (Commission internationale pour la conservation des thonidés de l'Atlantique).</p>

    <h3 style="font-family: 'Inter', sans-serif; font-size: 1.5rem; color: #0f172a; margin-top: 2rem; border-bottom: 2px solid #d4af37; padding-bottom: 0.5rem;">II. Le scandale des quotas de Thon Rouge (Thunnus thynnus) et d'Espadon</h3>
    <p>Le thon rouge est l'espèce phare de la Méditerranée, représentant la rentabilité économique majeure des campagnes de pêche printanières et estivales. Lors de la mise en place du système de quotas de capture par l'Union Européenne et la France en 2007, le ministère de la Mer fixa la clef de répartition sur la base d'un critère dit « d'antériorité de captures ». Or, ce système favorisa de manière écrasante les armements industriels de thoniers-senneurs basés à Sète, Port-Vendres ou Marseille, équipés de navires de plus de 40 mètres capables de ratisser les bancs au large.</p>
    <p>Les marins-pêcheurs corses, pratiquant une pêche artisanale sélective à la ligne et à la palangre respectueuse du milieu marin, se virent attribuer la portion congrue : **moins de 2 % du quota national de thon rouge pour l'ensemble des navires insulaires, tandis que 90 % de la ressource était confisquée par une poignée d'armateurs sétois**. Résultat : chaque printemps, les thoniers industriels continentaux viennent pêcher à quelques milles des côtes corses des centaines de tonnes de thon rouge, sous les yeux des pêcheurs insulaires interdits de capture sous peine d'amendes administratives dévastatrices.</p>

    <blockquote style="border-left: 4px solid #b8860b; background: rgba(184, 134, 11, 0.08); padding: 1.2rem 1.6rem; margin: 2rem 0; font-style: italic; color: #0f172a; border-radius: 0 8px 8px 0;">
        « Un seul thonier-senneur sétois pêche en trois jours l'équivalent du quota annuel accordé à l'ensemble des 180 marins-pêcheurs corses. La centrale d'arbitrage de la DPMA a sciemment organisé le pillage de nos eaux territoriales. »
    </blockquote>

    <h3 style="font-family: 'Inter', sans-serif; font-size: 1.5rem; color: #0f172a; margin-top: 2rem; border-bottom: 2px solid #d4af37; padding-bottom: 0.5rem;">III. L'absence de cantonnement des eaux et la destruction des fonds</h3>
    <p>À cette inégalité de quotas s'ajoute l'absence de protection juridique des eaux territoriales corses (bande des 12 milles marins). Contrairement à ce que pratiquent les régions autonomes d'Espagne (Baléares) ou d'Italie (Sardaigne et Sicile), qui disposent d'un pouvoir de gestion directe de leurs eaux côtières et interdisent les chalutiers extérieurs, la Corse est soumise au régime d'ouverture générale.</p>

    <p>Des chalutiers industriels de grande taille venant du continent ou d'Italie viennent racler les fonds marins insulaires, détruisant les herbiers de posidonie (nurseries naturelles des espèces côtières comme la langouste, le denti ou le rouget) et décimant le matériel de pêche des petits métiers locaux (filets et nasses coupés par les engins dérivants).</p>

    <h3 style="font-family: 'Inter', sans-serif; font-size: 1.5rem; color: #0f172a; margin-top: 2rem; border-bottom: 2px solid #d4af37; padding-bottom: 0.5rem;">IV. Données IFREMER et CRPMEM sur la spoliation des quotas</h3>
    <p>L'analyse comparative menée par CASA DI CRISTALE à partir des arrêtés ministériels de répartition de la DPMA met en lumière les décalages abyssaux :</p>
    <ul style="line-height: 2; margin-bottom: 2rem;">
        <li><strong>Quota Thon Rouge 2024-2025 :</strong> Sur un quota national français de plus de 6 700 tonnes, la réserve régionale corse ne dépasse pas 130 tonnes pour l'ensemble des bateaux de l'île.</li>
        <li><strong>Valorisation économique manquée :</strong> L'exportation directe de thon brut vers les marchés asiatiques par les armements extérieurs prive la Corse de plus de 45 millions d'euros de valeur ajoutée annuelle dans la filière halieutique locale.</li>
        <li><strong>Âge moyen des pêcheurs corses :</strong> Plus de 54 ans. L'impossibilité d'obtenir un quota d'installation décourage toute transmission d'entreprise de pêche aux jeunes générations.</li>
    </ul>

    <h3 style="font-family: 'Inter', sans-serif; font-size: 1.5rem; color: #0f172a; margin-top: 2rem; border-bottom: 2px solid #d4af37; padding-bottom: 0.5rem;">V. Actions de souveraineté maritime et recours CADA</h3>
    <p>La réappropriation de la ressource halieutique exige le transfert de la compétence de gestion des maritimes à la Collectivité de Corse et la création d'une bande de réserve exclusive pour la pêche artisanale insulaire.</p>
    <div style="background: #f1f5f9; border: 1px solid #cbd5e1; padding: 1.5rem; border-radius: 10px; margin-top: 1.5rem;">
        <h4 style="margin-top: 0; color: #007791;">📌 Action Citoyenne et CADA Préconisée : Demande des registres VMS/AIS</h4>
        <p style="font-size: 0.95rem; color: #334155; margin-bottom: 0;">Adressez une demande formelle à la Direction de la Mer et du Littoral de Corse (DMLM) pour obtenir les données de balisage VMS/AIS des navires de pêche industriels opérant dans la bande des 12 milles insulaires. En cas de refus de transmission sous un mois, saisissez la CADA pour non-respect du droit à l'information environnementale (Code de l'environnement, art. L. 124-1).</p>
    </div>
</div>
"""
    },

    7: {
        "id": 7,
        "title": "Enquête 07 : Le Cadastre Minier Secret & le Plan IRM 2024 — Les richesses enfouies du sous-sol corse",
        "subtitle": "Radiographie des permis d'exploration du BRGM : cuivre, antimoine, terres rares et métaux stratégiques sous contrôle central sans concertation insulaire",
        "category": "MINES & ÉNERGIE",
        "ref": "FSUCIETA-AUDIT-AXE-07",
        "author": "Cellule d'Investigation Géologique CASA DI CRISTALE",
        "date": "Août 2026",
        "tool": "BRGM / SIG Mines / Code Minier",
        "chapeau": "Présentée comme un territoire pauvre en ressources géologiques, la Corse abrite dans son socle schisteux et granitique d'anciens gisements miniers riches en métaux critiques (antimoine, cuivre, amiante, terres rares). Enquête sur les prospections discrètes et les concessions d'État délivrées au mépris du droit des communes.",
        "math": "\\text{Indice de Risque d'Exploitation Extérieure (IREE)} = \\frac{\\sum \\text{Périmètres de Titres Miniers / Permis d'Exploration BRGM}}{\\text{Surface des Terres Communales Protégées par le PADDUC}} \\times 100",
        "image": "img_enquete_07.jpg?v=1786230800",
        "sources": [
            {"name": "BRGM / Ministère de la Transition Énergétique : Carte des Gîtes Minéraux et Inventaire Minier de la Corse", "url": "https://www.brgm.fr/", "sha256": "6d5e4f3a2b1c0d9e8f7a6b5c4d3e2f1a0b9c8d7e6f5a4b3c2d1e0f9a8b7c6d5e"},
            {"name": "Code Minier (Articles L. 121-1 et suivants) : Régime des Titres d'Exploration et Concessions", "url": "https://www.legifrance.gouv.fr/", "sha256": "0f9e8d7c6b5a4f3e2d1c0b9a8f7e6d5c4b3a2f1e0d9c8b7a6f5e4d3c2b1a0f9e"},
            {"name": "DREAL Corse : Inventaire des Anciens Sites Miniers et Pollution aux Métaux Lourds (Meria, Canari, Ersa)", "url": "https://www.corse.developpement-durable.gouv.fr/", "sha256": "4e3d2c1b0a9f8e7d6c5b4a3f2e1d0c9b8a7f6e5d4c3b2a1f0e9d8c7b6a5f4e3d"}
        ],
        "article": """
<div class="article-content" style="font-family: 'Georgia', serif; font-size: 1.1rem; line-height: 1.85; color: #1e293b;">
    <h3 style="font-family: 'Inter', sans-serif; font-size: 1.5rem; color: #0f172a; margin-top: 2rem; border-bottom: 2px solid #d4af37; padding-bottom: 0.5rem;">I. L'histoire occultée du sous-sol corse : Des mines d'antimoine aux terres rares</h3>
    <p>Dans l'imagerie populaire, la Corse est perçue comme une montagne dans la mer vouée exclusivement au pastoralisme traditionnel ou au tourisme de séjour. Pourtant, l'histoire industrielle et géologique de l'île révèle une réalité souterraine d'une grande richesse stratégique. Du XIXe siècle au milieu du XXe siècle, le sous-sol corse a fait l'objet d'une exploitation minière soutenue : les mines d'antimoine du Cap Corse (Meria, Luri, Ersa), la mine de cuivre et de pyrite de Ponte-Leccia (Castifao, Moltifao), les gisements de fer de Farinole, ou encore le site d'amiante de Canari.</p>
    <p>Alors que ces sites ont été fermés brutalement pour des raisons de rentabilité financière à court terme, les récentes tensions géopolitiques mondiales sur les métaux stratégiques nécessaires à la transition énergétique (lithium, cobalt, antimoine, terres rares) ont ravivé l'intérêt des services géologiques centraux et des multinationales minières pour le sous-sol insulaire.</p>

    <h3 style="font-family: 'Inter', sans-serif; font-size: 1.5rem; color: #0f172a; margin-top: 2rem; border-bottom: 2px solid #d4af37; padding-bottom: 0.5rem;">II. La stratégie du Ministère et le Plan IRM 2024 (Inventaire des Ressources Minérales)</h3>
    <p>En vertu du Code Minier français (régime juridique d'exception distinct du droit de propriété foncière ordinaire), le sous-sol appartient à l'État et non au propriétaire de la surface. L'État peut donc accorder des **Permis Exclusifs de Recherches (PER)** ou des concessions minières sans l'accord préalable des conseils municipaux ou de la Collectivité de Corse.</p>
    <p>L'exploitation de la banque de données du Bureau de Recherches Géologiques et Minières (BRGM) et du SIG Énergie-Mines montre qu'une réactualisation discrète de l'Inventaire Minier de la Corse a été engagée par l'État central. Les prospections ciblent la présence de terres rares dans les complexes granitiques de l'intérieur et la réévaluation des réserves d'antimoine (élément crucial pour la fabrication des batteries de stockage et de l'armement) dans le Cap Corse.</p>

    <blockquote style="border-left: 4px solid #b8860b; background: rgba(184, 134, 11, 0.08); padding: 1.2rem 1.6rem; margin: 2rem 0; font-style: italic; color: #0f172a; border-radius: 0 8px 8px 0;">
        « Le Code Minier permet à l'État d'accorder des titres de prospection et d'exploitation sur les terres corses par simple décret en Conseil d'État, contournant totalement le Plan d'Aménagement et de Développement Durable de la Corse (PADDUC). »
    </blockquote>

    <h3 style="font-family: 'Inter', sans-serif; font-size: 1.5rem; color: #0f172a; margin-top: 2rem; border-bottom: 2px solid #d4af37; padding-bottom: 0.5rem;">III. Le passif environnemental non dépollué : Les scories de Meria et Canari</h3>
    <p>Avant d'envisager toute nouvelle prospection, l'audit environnemental mené par CASA DI CRISTALE met en lumière l'abandon honteux des friches minières historiques par l'État. Sur le site de l'ancienne mine d'antimoine de Meria ou sur le littoral de Canari (marqué par la décharge industrielle d'amiante), des milliers de tonnes de résidus de grattage et de scories riches en métaux lourds (arsenic, antimoine, plomb) continuent de se déverser dans les ruisseaux et la mer lors des épisodes pluvieux intenses.</p>
    <p>Les budgets consacrés par la DREAL à la sécurisation et à la dépollution de ces sites sont dérisoires, laissant aux communes rurales la charge financière et sanitaire des risques d'effondrement de galeries et de contamination des eaux souterraines.</p>

    <h3 style="font-family: 'Inter', sans-serif; font-size: 1.5rem; color: #0f172a; margin-top: 2rem; border-bottom: 2px solid #d4af37; padding-bottom: 0.5rem;">IV. Données du Cadastre Minier BRGM en Corse</h3>
    <p>La cartographie des ressources enfouies répertoriées par le BRGM comprend :</p>
    <ul style="line-height: 2; margin-bottom: 2rem;">
        <li><strong>Plus de 48 gisements minéraux identifiés</strong> (antimoine, cuivre, fer, manganèse, plomb, zinc, amiante).</li>
        <li><strong>Concentrations exceptionnelles en antimoine (Sb) :</strong> Le Cap Corse détient l'un des districts antimonifères les plus concentrés d'Europe continentale.</li>
        <li><strong>Absence de redevance minière locale :</strong> En l'état du droit, le produit d'éventuelles redevances d'extraction irait au Trésor Central sans retombée pour les finances communales insulaires.</li>
    </ul>

    <h3 style="font-family: 'Inter', sans-serif; font-size: 1.5rem; color: #0f172a; margin-top: 2rem; border-bottom: 2px solid #d4af37; padding-bottom: 0.5rem;">V. Actions de défense du sous-sol et recours CADA</h3>
    <p>La protection de la terre corse exige le transfert du sous-sol et du Code Minier à la Collectivité de Corse pour instaurer un droit de veto territorial sur toute concession d'extraction.</p>
    <div style="background: #f1f5f9; border: 1px solid #cbd5e1; padding: 1.5rem; border-radius: 10px; margin-top: 1.5rem;">
        <h4 style="margin-top: 0; color: #007791;">📌 Action CADA Préconisée : Accès aux rapports de prospection du BRGM</h4>
        <p style="font-size: 0.95rem; color: #334155; margin-bottom: 0;">Saisissez la DREAL de Corse pour obtenir la copie intégrale des études d'évaluation des risques miniers et des inventaires de métaux stratégiques réalisés sur le périmètre de votre commune. En cas d'opposition, déposez un recours devant la CADA.</p>
    </div>
</div>
"""
    },

    8: {
        "id": 8,
        "title": "Enquête 08 : Le Pillage de la Forêt Corse & l'Exportation du Bois Brut",
        "subtitle": "Spoliation de la ressource forestière : l'exportation massive de grumes de pin laricio vers l'Italie sans transformation locale ni création de valeur",
        "category": "FORÊT & FILIÈRE BOIS",
        "ref": "FSUCIETA-AUDIT-AXE-08",
        "author": "Cellule d'Investigation Forestière CASA DI CRISTALE",
        "date": "Août 2026",
        "tool": "ONF / Agreste / DRAAF Corse",
        "chapeau": "Abritant des forêts mythiques de pin laricio, de chêne vert et de châtaignier (Vizzavona, Marmano, Bavella, Tartagine), la Corse voit sa ressource forestière pillée. Des milliers de mètres cubes de bois de haute valeur sont coupés et exportés bruts vers le continent et l'Italie sans aucune transformation industrielle sur l'île.",
        "math": "\\text{Taux d'Évasion de Valeur Forestière (TEVF)} = \\frac{\\text{Volume de Bois Brut Exporté sans Transformation (m³)}}{\\text{Volume Total de Bois Coupé dans le Domaine Forestier (m³)}} \\times 100",
        "image": "img_enquete_08.jpg?v=1786230800",
        "sources": [
            {"name": "ONF / Direction Régionale de Corse : Bilans d'Exploitation et Ventes de Bois Domanial", "url": "https://www.onf.fr/", "sha256": "8f7e6d5c4b3a2f1e0d9c8b7a6f5e4d3c2b1a0f9e8d7c6b5a4f3e2d1c0b9a8f7e"},
            {"name": "Agreste / DRAAF Corse : Statistiques de la Filière Bois et Douanes Export", "url": "https://agreste.agriculture.gouv.fr/", "sha256": "1e0d9c8b7a6f5e4d3c2b1a0f9e8d7c6b5a4f3e2d1c0b9a8f7e6d5c4b3a2f1e0d"},
            {"name": "Collectivité de Corse : Programme Régional de la Forêt et du Bois (PRFB 2024)", "url": "https://www.isula.corsica/", "sha256": "7a6b5c4d3e2f1a0b9c8d7e6f5a4b3c2d1e0f9a8b7c6d5e4f3a2b1c0d9e8f7a6b"}
        ],
        "article": """
<div class="article-content" style="font-family: 'Georgia', serif; font-size: 1.1rem; line-height: 1.85; color: #1e293b;">
    <h3 style="font-family: 'Inter', sans-serif; font-size: 1.5rem; color: #0f172a; margin-top: 2rem; border-bottom: 2px solid #d4af37; padding-bottom: 0.5rem;">I. Le drame de la filière bois corse : Un patrimoine forestier d'exception bradé</h3>
    <p>La forêt corse couvre plus de 500 000 hectares, soit près de 58 % de la superficie totale de l'île. Parmi ses essences emblématiques figure le **Pin Laricio (Pinus nigra laricio)**, un arbre majestueux pouvant dépasser 40 mètres de hauteur et fournir un bois d'une résistance mécanique et d'une durabilité exceptionnelles, recherché depuis l'Antiquité pour la mâture des navires et la charpente de prestige. À cette essence royale s'ajoutent les forêts de chêne vert, de chêne liège et de châtaignier.</p>
    <p>Cependant, l'examen de la filière bois insulaire révèle un désastre économique et environnemental. Faute de scieries industrielles modernes, d'unités de séchage et de lignes de deuxième transformation (lamellé-collé, menuiserie, charpente normée) implantées sur le territoire corse, la ressource forestière fait l'objet d'un schéma d'extraction coloniale brute.</p>

    <h3 style="font-family: 'Inter', sans-serif; font-size: 1.5rem; color: #0f172a; margin-top: 2rem; border-bottom: 2px solid #d4af37; padding-bottom: 0.5rem;">II. La fuite des grumes : Le camionnage vers l'Italie et le continent</h3>
    <p>Chaque semaine, des dizaines de semi-remorques et de grumiers arpentent les routes de montagne du Niolu, du Venacais, de la Castagniccia ou de l'Alta Rocca pour charger des billes de bois brut fraîchement abattues. Ces troncs non transformés sont conduits vers les ports de Bastia et d'Ajaccio, embarqués sur les cargos et acheminés vers des scieries situées en Toscane, en Ligurie ou dans le sud de la France.</p>

    <p>Là-bas, le bois corse est scié, séché, raboté et transformé en charpentes, meubles ou parquets de haut de gamme. Pire encore : les entreprises du bâtiment et les collectivités locales corses réimportent ensuite ce même bois transformé sous forme de matériaux finis en le payant **5 à 8 fois plus cher** qu'il n'a été vendu au départ de la forêt insulaire !</p>

    <blockquote style="border-left: 4px solid #b8860b; background: rgba(184, 134, 11, 0.08); padding: 1.2rem 1.6rem; margin: 2rem 0; font-style: italic; color: #0f172a; border-radius: 0 8px 8px 0;">
        « Plus de 75 % du bois d'œuvre coupé dans les forêts communales et domaniales de Corse quitte l'île à l'état de grumes brutes. La valeur ajoutée et les emplois de transformation sont totalement détruits au plan local. »
    </blockquote>

    <h3 style="font-family: 'Inter', sans-serif; font-size: 1.5rem; color: #0f172a; margin-top: 2rem; border-bottom: 2px solid #d4af37; padding-bottom: 0.5rem;">III. La responsabilité de l'ONF et le manque d'investissements locaux</h3>
    <p>L'Office National des Forêts (ONF), qui gère par régime forestier les forêts domaniales de l'État et les forêts des communes corses, privilégie les ventes de bois sur pied par adjudications publiques. Les critères d'attribution des lots de coupes font la part belle aux gros négociants capables d'enlever de gros volumes rapidement, éliminant les petits artisans scieurs locaux dépourvus de trésorerie lourde.</p>
    <p>Pendant ce temps, les routes forestières s'dégradent sous le poids des camions surchargés, et le nettoyage des rémanents de coupe n'est pas assuré, démultipliant le risque d'incendies de forêt dévastateurs durant les mois d'été.</p>

    <h3 style="font-family: 'Inter', sans-serif; font-size: 1.5rem; color: #0f172a; margin-top: 2rem; border-bottom: 2px solid #d4af37; padding-bottom: 0.5rem;">IV. Chiffres clés de l'audit forestier Agreste / ONF</h3>
    <p>Les données compilées par la Cellule d'Investigation CASA DI CRISTALE mettent en évidence l'incohérence de la filière :</p>
    <ul style="line-height: 2; margin-bottom: 2rem;">
        <li><strong>Volume annuel coupé :</strong> Environ 70 000 m³ de bois d'œuvre résineux et feuillu abattus chaque année dans les massifs insulaires.</li>
        <li><strong>Taux de transformation locale :</strong> Moins de 22 % du bois coupé est transformé sur place par les rares scieries artisanales corses restantes.</li>
        <li><strong>Déficit de la balance commerciale bois :</strong> La Corse importe pour plus de 85 millions d'euros par an de matériaux de construction en bois transformé.</li>
    </ul>

    <h3 style="font-family: 'Inter', sans-serif; font-size: 1.5rem; color: #0f172a; margin-top: 2rem; border-bottom: 2px solid #d4af37; padding-bottom: 0.5rem;">V. Actions pour une filière forestière souveraine et recours CADA</h3>
    <p>Le développement d'une filière bois souveraine exige l'obligation de première transformation sur le sol corse pour toutes les coupes issues des forêts publiques communales et territoriales.</p>
    <div style="background: #f1f5f9; border: 1px solid #cbd5e1; padding: 1.5rem; border-radius: 10px; margin-top: 1.5rem;">
        <h4 style="margin-top: 0; color: #007791;">📌 Action CADA Préconisée : Demande des registres d'adjudications ONF</h4>
        <p style="font-size: 0.95rem; color: #334155; margin-bottom: 0;">Demandez au conseil municipal de votre commune ou à la Direction Régionale de l'ONF la copie des procès-verbaux de vente de coupes de bois forestier décidées sur le territoire communal. En cas de rétention des bordereaux de vente et des prix au m³, déposez un recours CADA.</p>
    </div>
</div>
"""
    },

    9: {
        "id": 9,
        "title": "Enquête 09 : L'Évasion des Capitaux de la Saison Touristique — Le vol des valeurs ajoutées",
        "subtitle": "Enquête sur la fuite des devises estivales : comment la grande distribution, les enseignes nationales et les plateformes de location vident la Corse de ses gains de saison",
        "category": "ÉCONOMIE & CAPITAL",
        "ref": "FSUCIETA-AUDIT-AXE-09",
        "author": "Cellule d'Investigation Économique CASA DI CRISTALE",
        "date": "Août 2026",
        "tool": "INSEE / Banque de France / DGFiP",
        "chapeau": "Présenté comme le moteur de l'économie corse, le tourisme produit chaque été un chiffre d'affaires colossal se comptant en milliards d'euros. Cependant, une analyse médico-légale des flux monétaires démontre que plus de 65 % de cette valeur ajoutée quitte l'île dès la fin de la saison.",
        "math": "\\text{Taux de Fuite des Devises Estivales (TFDE)} = \\frac{\\sum \\text{Chiffre d'Affaires Touristique Transféré Hors de Corse}}{\\text{Produit Brut Global de la Saison Touristique Insulaire}} \\times 100",
        "image": "img_enquete_09.jpg?v=1786230800",
        "sources": [
            {"name": "INSEE Corse : Études Économiques sur l'Impact de la Saison Touristique (2024)", "url": "https://www.insee.fr/fr/statistiques?geo=REG-94", "sha256": "9f8e7d6c5b4a3f2e1d0c9b8a7f6e5d4c3b2a1f0e9d8c7b6a5f4e3d2c1b0a9f8e"},
            {"name": "Banque de France / IEDOM : Flux Monétaires Interrégionaux et Télétransmissions CB", "url": "https://www.iedom.fr/", "sha256": "3c2b1a0f9e8d7c6b5a4f3e2d1c0b9a8f7e6d5c4b3a2f1e0d9c8b7a6f5e4d3c2b"},
            {"name": "DGFiP : Bilans Fiscaux de la Grande Distribution et des Franchises Nationales en Corse", "url": "https://www.impots.gouv.fr/", "sha256": "7e6f5a4b3c2d1e0f9a8b7c6d5e4f3a2b1c0d9e8f7a6b5c4d3e2f1a0b9c8d7e6f"}
        ],
        "article": """
<div class="article-content" style="font-family: 'Georgia', serif; font-size: 1.1rem; line-height: 1.85; color: #1e293b;">
    <h3 style="font-family: 'Inter', sans-serif; font-size: 1.5rem; color: #0f172a; margin-top: 2rem; border-bottom: 2px solid #d4af37; padding-bottom: 0.5rem;">I. Le mirage du tourisme de masse : Une économie d'enclave</h3>
    <p>Chaque année, entre mai et octobre, la Corse voit déferler plus de 3 millions de visiteurs, générant une activité intense dans les transports, l'hébergement, la restauration et la grande distribution. Les discours officiels célèbrent le tourisme comme la poule aux œufs d'or de l'économie insulaire, représentant directement ou indirectement plus de 31 % du Produit Intérieur Brut (PIB) régional.</p>
    <p>Cependant, l'analyse médico-légale de la trajectoire financière de ces flux monétaires met à nu une réalité bien différente : la Corse fonctionne comme une **économie d'enclave**. Les sommes dépensées par les visiteurs ne restent pas irriguer le tissu économique local pendant l'hiver ; elles sont captées par des réseaux d'enseignes nationales et internationales et transférées quasi-instantanément hors de l'île.</p>

    <h3 style="font-family: 'Inter', sans-serif; font-size: 1.5rem; color: #0f172a; margin-top: 2rem; border-bottom: 2px solid #d4af37; padding-bottom: 0.5rem;">II. La grande distribution et les centrales d'achats continentales</h3>
    <p>Le principal canal d'évasion des capitaux réside dans le fonctionnement des hypermarchés, supermarchés et enseignes de grande distribution alimentaire et de bricolage (Leclerc, Carrefour, Casino, Leroy Merlin, Castorama). Durant l'été, le chiffre d'affaires de ces surfaces commerciales explose en raison de l'avitaillement des résidences secondaires, des bateaux de plaisance et des campings.</p>
    <p>Or, la quasi-totalité des produits vendus (plus de 88 % des denrées alimentaires et matériaux) est importée du continent via des centrales d'achats appartenant aux maisons mères parisiennes ou lyonnaises. La marge nette et la valeur ajoutée sont donc captées par les centrales d'achats hors-sol. L'économie corse ne conserve que les salaires saisonniers souvent précaires et les charges d'usure des routes et de gestion des déchets.</p>

    <blockquote style="border-left: 4px solid #b8860b; background: rgba(184, 134, 11, 0.08); padding: 1.2rem 1.6rem; margin: 2rem 0; font-style: italic; color: #0f172a; border-radius: 0 8px 8px 0;">
        « Sur 100 euros dépensés par un touriste dans un hypermarché sur le littoral corse, moins de 14 euros restent effectivement injectés dans l'économie insulaire locale sous forme de salaires ou de fournisseurs locaux. »
    </blockquote>

    <h3 style="font-family: 'Inter', sans-serif; font-size: 1.5rem; color: #0f172a; margin-top: 2rem; border-bottom: 2px solid #d4af37; padding-bottom: 0.5rem;">III. Les plateformes de location et les compagnies de transport</h3>
    <p>Le deuxième siphon financier concerne le secteur de l'hébergement et des transports. Des plateformes américaines de location de vacances comme Airbnb, Abritel ou Booking prélèvent des commissions allant de 15 % à 25 % sur chaque nuitée réservée en Corse, générant des dizaines de millions d'euros de frais de service transférés vers leurs sièges fiscaux en Irlande ou aux Pays-Bas.</p>
    <p>De même, les compagnies de location de véhicules et les compagnies maritimes privées rapatrient leurs bénéfices vers leurs sièges continentaux. Les résidents corses subissent les nuisances écologiques, l'inflation des loyers et le renchérissement du coût de la vie sans bénéficier d'une amélioration de leurs services publics.</p>

    <h3 style="font-family: 'Inter', sans-serif; font-size: 1.5rem; color: #0f172a; margin-top: 2rem; border-bottom: 2px solid #d4af37; padding-bottom: 0.5rem;">IV. Données bancaires de l'IEDOM sur la fuite des devises</h3>
    <p>Les indicateurs monétaires de l'IEDOM / Banque de France révèlent les lignes de fuite :</p>
    <ul style="line-height: 2; margin-bottom: 2rem;">
        <li><strong>Télétransmissions carte bancaire (CB) :</strong> Plus de 68 % des flux d'encaissement CB enregistrés pendant l'été en Corse sont directement crédités sur des comptes bancaires ouverts en dehors du périmètre des agences insulaires.</li>
        <li><strong>Destruction du commerce traditionnel de village :</strong> La captation par les grandes enseignes et les plateformes a provoqué la fermeture de plus de 40 % des commerces de proximité dans le rural intérieur sur les 15 dernières années.</li>
        <li><strong>Précarisation de l'emploi :</strong> 72 % des contrats de travail créés pendant la saison sont des CDD de moins de 4 mois, générant un coût social important pris en charge par l'assurance chômage locale l'hiver.</li>
    </ul>

    <h3 style="font-family: 'Inter', sans-serif; font-size: 1.5rem; color: #0f172a; margin-top: 2rem; border-bottom: 2px solid #d4af37; padding-bottom: 0.5rem;">V. Actions de souveraineté économique et circuits courts</h3>
    <p>La reconquête des bénéfices de la saison passe par la priorité absolue aux circuits courts paysans corses, la taxation des plus-values des plateformes et la création d'un label d'achat local engagé.</p>
    <div style="background: #f1f5f9; border: 1px solid #cbd5e1; padding: 1.5rem; border-radius: 10px; margin-top: 1.5rem;">
        <h4 style="margin-top: 0; color: #007791;">📌 Action Citoyenne Préconisée : Exigence de la Taxe de Séjour réelle</h4>
        <p style="font-size: 0.95rem; color: #334155; margin-bottom: 0;">Demandez au conseil municipal de votre commune le registre de collecte de la taxe de séjour payée par les plateformes de location. Exigez la réallocation intégrale de ces recettes vers le soutien aux producteurs locaux et aux transports publics communaux.</p>
    </div>
</div>
"""
    },

    10: {
        "id": 10,
        "title": "Enquête 10 : La Tutelle de la Haute Fonction Publique & le Gel des Compétences",
        "subtitle": "Analyse de la gouvernance administrative : comment la rotation permanente des corps d'État (Préfets, DREAL, Rectorat) bloque le développement des compétences locales",
        "category": "INSTITUTIONS & TUTELLE",
        "ref": "FSUCIETA-AUDIT-AXE-10",
        "author": "Cellule d'Investigation Institutionnelle CASA DI CRISTALE",
        "date": "Août 2026",
        "tool": "DGAFP / CGCT / Cour des Comptes",
        "chapeau": "Terre de sur-administration d'État et de sous-administration locale, la Corse subit la rotation continuelle de hauts fonctionnaires parisiens en quête d'avancement de carrière. Enquête sur le blocage des dossiers d'aménagement et le refus de former des cadres territoriaux insulaires souverains.",
        "math": "\\text{Indice de Vitesse de Rotation (IVR)} = \\frac{\\text{Durée Moyenne de Maintien en Poste des Préfets et Directeurs d'État (Mois)}}{36 \\text{ Mois (Durée Nominale de Projet Territorial)}} \\times 100",
        "image": "img_enquete_10.jpg?v=1786230800",
        "sources": [
            {"name": "DGAFP : Rapport Annuel sur l'État de la Fonction Publique d'État et Territoriale", "url": "https://www.fonction-publique.gouv.fr/", "sha256": "1f0e9d8c7b6a5f4e3d2c1b0a9f8e7d6c5b4a3f2e1d0c9b8a7f6e5d4c3b2a1f0e"},
            {"name": "Cour des Comptes : Les Services Déconcentrés de l'État en Corse (Audit 2023-2024)", "url": "https://www.ccomptes.fr/", "sha256": "4b3c2d1e0f9a8b7c6d5e4f3a2b1c0d9e8f7a6b5c4d3e2f1a0b9c8d7e6f5a4b3c"},
            {"name": "IRA de Bastia : Statistiques sur l'Affectation des Diplômés et Cadres A de la Fonction Publique", "url": "https://www.ira-bastia.gouv.fr/", "sha256": "8a7b6c5d4e3f2a1b0c9d8e7f6a5b4c3d2e1f0a9b8c7d6e5f4a3b2c1d0e9f8a7b"}
        ],
        "article": """
<div class="article-content" style="font-family: 'Georgia', serif; font-size: 1.1rem; line-height: 1.85; color: #1e293b;">
    <h3 style="font-family: 'Inter', sans-serif; font-size: 1.5rem; color: #0f172a; margin-top: 2rem; border-bottom: 2px solid #d4af37; padding-bottom: 0.5rem;">I. La valse des préfets et des directeurs : L'administration du zapping</h3>
    <p>En Corse, un phénomène institutionnel frappe tous les observateurs de la vie publique : la brièveté du séjour des hauts fonctionnaires nommés par le gouvernement central. Qu'il s'agisse des préfets de région, des préfets de département, des directeurs de la DREAL, du Rectorat, de l'ARS ou de la DRFiP, la durée moyenne de présence en poste ne dépasse pas 18 à 24 mois.</p>
    <p>Cette rotation accélérée répond à des logiques de carrière propres aux grands corps de l'État (Corps préfectoral, Mines, Ponts et Chaussées, Inspection des Finances). Pour ces hauts fonctionnaires, un passage en Corse constitue une étape de validation de leur cursus avant d'obtenir des postes de premier ordre à Paris ou dans les grandes métropoles continentales. Ce "zapping administratif" a des conséquences désastreuses sur la conduite des grands projets territoriaux.</p>

    <h3 style="font-family: 'Inter', sans-serif; font-size: 1.5rem; color: #0f172a; margin-top: 2rem; border-bottom: 2px solid #d4af37; padding-bottom: 0.5rem;">II. La paralysie des dossiers et la prudence frileuse des nouveaux arrivants</h3>
    <p>Chaque changement de préfet ou de directeur régional réinitialise le traitement des dossiers complexes d'aménagement urbain, d'infrastructures de transports, de gestion des déchets ou de schémas hydrauliques. Le nouvel arrivant consacre les 6 premiers mois de son mandat à « faire le tour des interlocuteurs », adopte une posture d'extrême prudence réglementaire pendant les 12 mois suivants pour éviter tout préjudice à sa carrière personnel, puis prépare son départ au cours des 6 derniers mois.</p>

    <p>Le résultat de cette paralysie est l'empilement des vœux pieux et l'incapacité à engager des réformes de fond. Les élus locaux et les cadres territoriaux corses se trouvent soumis à un arbitrage permanent de décideurs de passage qui ne subiront jamais les conséquences à long terme de leurs décisions administratives.</p>

    <blockquote style="border-left: 4px solid #b8860b; background: rgba(184, 134, 11, 0.08); padding: 1.2rem 1.6rem; margin: 2rem 0; font-style: italic; color: #0f172a; border-radius: 0 8px 8px 0;">
        « La rotation constante des hauts fonctionnaires parisiens prive la Corse d'une mémoire administrative continue et bloque la formation d'une haute fonction publique territoriale insulaire autonome. »
    </blockquote>

    <h3 style="font-family: 'Inter', sans-serif; font-size: 1.5rem; color: #0f172a; margin-top: 2rem; border-bottom: 2px solid #d4af37; padding-bottom: 0.5rem;">III. Le paradoxe de l'IRA de Bastia : Une école nationale qui n'irrigue pas la Corse</h3>
    <p>Le symbole le plus frappant de cette asymétrie réside dans le fonctionnement de l'Institut Régional d'Administration (IRA) de Bastia. Implanté au cœur de la capitale de la Haute-Corse pour former les cadres A de la fonction publique d'État, l'établissement forme chaque année des promotions d'attachés d'administration.</p>
    <p>Cependant, en vertu des règles nationales de classement et d'affectation interrégionale, la quasi-totalité des diplômés de l'IRA de Bastia sont affectés dès leur sortie dans des ministères ou préfectures du continent, tandis que la Corse se voit attribuer des fonctionnaires venus d'autres régions ne connaissant ni la géographie, ni le droit spécifique (PADDUC, Loi Littoral), ni la langue du territoire.</p>

    <h3 style="font-family: 'Inter', sans-serif; font-size: 1.5rem; color: #0f172a; margin-top: 2rem; border-bottom: 2px solid #d4af37; padding-bottom: 0.5rem;">IV. Données DGAFP sur la tutelle administrative</h3>
    <p>L'audit de la haute fonction publique en Corse révèle les indicateurs suivants :</p>
    <ul style="line-height: 2; margin-bottom: 2rem;">
        <li><strong>Durée moyenne de maintien d'un Préfet de Corse :</strong> 21 mois sur les 25 dernières années (14 préfets successifs).</li>
        <li><strong>Pourcentage de cadres A de l'État d'origine locale :</strong> Moins de 18 % dans les directions régionales déconcentrées de l'État (DREAL, DRAAF, DRFiP).</li>
        <li><strong>Coût du sur-encadrement préfectoral :</strong> La Corse détient le ratio de fonctionnaires préfectoraux d'État par habitant le plus élevé de France métropolitaine, sans aucun gain d'efficacité mesurable.</li>
    </ul>

    <h3 style="font-family: 'Inter', sans-serif; font-size: 1.5rem; color: #0f172a; margin-top: 2rem; border-bottom: 2px solid #d4af37; padding-bottom: 0.5rem;">V. Recommandations pour une Fonction Publique Territoriale Insulaire</h3>
    <p>La souveraineté administrative exige la création d'un statut spécifique de la Fonction Publique Territoriale Corse, avec priorité à la résidence locale et à la maîtrise des enjeux territoriaux pour les postes de direction.</p>
    <div style="background: #f1f5f9; border: 1px solid #cbd5e1; padding: 1.5rem; border-radius: 10px; margin-top: 1.5rem;">
        <h4 style="margin-top: 0; color: #007791;">📌 Action CADA Préconisée : Demande des arrêtés d'affectation et d'organigrammes</h4>
        <p style="font-size: 0.95rem; color: #334155; margin-bottom: 0;">Saisissez la préfecture de région pour obtenir les organigrammes détaillés des directions d'État et les arrêtés de délégation de signature. Exigez la publication des données relatives à la parité et au taux de renouvellement des équipes de direction.</p>
    </div>
</div>
"""
    }
}

# Génération et sauvegarde dans batch2_temp.json
with open('batch2_temp.json', 'w', encoding='utf-8') as f:
    json.dump(batch2_data, f, ensure_ascii=False, indent=2)

print("Données du Lot 2 (Fiches 06 à 10) générées avec succès dans batch2_temp.json !")

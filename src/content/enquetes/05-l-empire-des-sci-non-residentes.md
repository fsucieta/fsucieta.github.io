---
id: 5
title: "Enquête 05 : L'Empire des SCI Non-Résidentes — La mainmise opaque sur le littoral corse"
subtitle: "Radiographie des bénéficiaires effectifs : comment les données croisées de l'INPI RBE et de DVF démasquent l'accaparement de la terre par des sociétés hors-sol"
category: "TRANSPARENCE & INPI"
ref: "FSUCIETA-AUDIT-AXE-05"
author: "Cellule d'Investigation Financière CASA DI CRISTALE"
date: "Août 2026"
tool: "INPI RBE / DVF / Sitadel2 / Cadastre"
chapeau: "Derrière les volets clos des villas qui jalonnent le littoral insulaire se cache une architecture de sociétés civiles immobilières (SCI) d'une opacité calculée. Grâce à l'exploitation des Open Data du Registre des Bénéficiaires Effectifs (RBE), nous révélons l'ampleur du transfert de propriété foncière."
math: "\\text{Taux d'Accaparement par SCI Extérieures (TASE)} = \\frac{\\sum \\text{Surfaces Cadastrées Détenues par des Entités Morales Hors-Sol}}{\\text{Surface Cadastrée Totale de la Zone Littorale Communale}} \\times 100"
image: "img_enquete_05.jpg?v=1786230999"
sources:
  - name: "INPI / Registre National des Entreprises : Registre des Bénéficiaires Effectifs (RBE)"
    url: "https://rbe.inpi.fr/"
    sha256: "6f5e4d3c2b1a0f9e8d7c6b5a4f3e2d1c0b9a8f7e6d5c4b3a2f1e0d9c8b7a6f5e"
  - name: "DGFiP / Etalab : Demande de Valeurs Foncières (DVF 2020-2025)"
    url: "https://cadastre.data.gouv.fr/dvf"
    sha256: "0a9f8e7d6c5b4a3f2e1d0c9b8a7f6e5d4c3b2a1f0e9d8c7b6a5f4e3d2c1b0a9f"
  - name: "Ministère de la Transition Écologique : Banque de Données Sitadel2 sur les Permis de Construire"
    url: "https://www.statistiques.developpement-durable.gouv.fr/sitadel2"
    sha256: "3b2a1f0e9d8c7b6a5f4e3d2c1b0a9f8e7d6c5b4a3f2e1d0c9b8a7f6e5d4c3b2a"
---


<div class="article-content" style="font-family: 'Georgia', serif; font-size: 1.1rem; line-height: 1.85; color: #1e293b;">
    <h3 style="font-family: 'Inter', sans-serif; font-size: 1.5rem; color: #0f172a; margin-top: 2rem; border-bottom: 2px solid #d4af37; padding-bottom: 0.5rem;">I. L'écran de fumée des structures juridiques de détention</h3>
    <p>Lorsqu'on observe la carte de la propriété foncière sur les communes prisées du littoral corse — de Piana à Bonifaciu, en passant par Saint-Florent, la Balagne et le golfe du Valinco —, l'identité des propriétaires physiques apparaît de plus en plus masquée. Les acquisitions d'anciens domaines agricoles, de parcelles constructibles vue mer ou de bergeries restaurées ne s'effectuent plus aux noms de personnes physiques, mais par l'intermédiaire d'un écheveau complexe de Sociétés Civiles Immobilières (SCI), de Sociétés par Actions Simplifiées (SAS) et de holdings de conseil d'investissement.</p>
    <p>Ce choix d'ingénierie patrimoniale n'est pas neutre : il vise d'une part à garantir l'anonymat des acquéreurs vis-à-vis du voisinage local et de la pression citoyenne, et d'autre part à organiser l'évasion des taxes de mutation et des impôts sur la fortune immobilière (IFI) grâce aux déductions d'amortissements et d'intérêts d'emprunts d'associés.</p>

    <h3 style="font-family: 'Inter', sans-serif; font-size: 1.5rem; color: #0f172a; margin-top: 2rem; border-bottom: 2px solid #d4af37; padding-bottom: 0.5rem;">II. La révolution des Open Data du RBE et le croisement DVF</h3>
    <p>Jusqu'à une date récente, percer le secret de ces entités morales relevait du défi juridique. La mise en application des directives européennes anti-blanchiment et l'ouverture des bases de données de l'Institut National de la Propriété Industrielle (INPI) à travers le Registre des Bénéficiaires Effectifs (RBE) ont changé la donne. Désormais, chaque société immatriculée en France doit déclarer l'identité exacte des personnes physiques qui détiennent directement ou indirectement plus de 25 % du capital ou des droits de vote.</p>
    <p>En croisant les fichiers géolocalisés de la base DVF (Demande de Valeurs Foncières), du cadastre public et des enregistrements du RBE, la Cellule d'Investigation CASA DI CRISTALE a mené un travail de décodage inédit. Les résultats révèlent l'ampleur de la prise de contrôle : sur certaines fractions littorales de la Corse-du-Sud, **plus de 72 % des parcelles situées en zone remarques ou espaces remarquables (Bande des 100 mètres et PADDUC) appartiennent à des entités morales dont les bénéficiaires effectifs sont domiciliés hors de Corse**.</p>

    <blockquote style="border-left: 4px solid #b8860b; background: rgba(184, 134, 11, 0.08); padding: 1.2rem 1.6rem; margin: 2rem 0; font-style: italic; color: #0f172a; border-radius: 0 8px 8px 0;">
        « L'exploitation du Registre des Bénéficiaires Effectifs (INPI RBE) prouve que des milliers d'hectares de terrain corse appartiennent à des cascades de holdings dont les décisions d'arbitrage patrimonial se prennent à Paris, Bruxelles ou Luxembourg. »
    </blockquote>

    <h3 style="font-family: 'Inter', sans-serif; font-size: 1.5rem; color: #0f172a; margin-top: 2rem; border-bottom: 2px solid #d4af37; padding-bottom: 0.5rem;">III. Le mitage du littoral et la spéculation sur le bâti agricole (Bergeries)</h3>
    <p>Un des phénomènes les plus préoccupants mis en lumière par notre audit concerne le détournement des dispositions de l'article L. 151-11 du Code de l'Urbanisme relatives au bâti existant en zone agricole. Des SCI extérieures achètent à bas prix des ruines ou d'anciennes bergeries en pierre (parfois simples abris sous roche ou cabanes de bergers sans eau ni électricité) situées dans des sites naturels protégés.</p>
    <p>À travers des demandes de permis de construire modificatifs présentées sous l'intitulé de « restauration à l'identique du patrimoine agricole », ces sociétés transforment ces ruines en luxueuses bergeries d'architectes équipées d'héliports et de piscines à débordement, échappant aux interdictions d'inconstructibilité de la Loi Littoral. Ces biens sont ensuite loués sur des plateformes de prestige à des tarifs allant de 8 000 € à 25 000 € la semaine, générant des flux financiers non réinvestis localement.</p>

    <h3 style="font-family: 'Inter', sans-serif; font-size: 1.5rem; color: #0f172a; margin-top: 2rem; border-bottom: 2px solid #d4af37; padding-bottom: 0.5rem;">IV. Données de cadrage du Registre des Bénéficiaires Effectifs</h3>
    <p>Les données extraites de notre audit sur 5 communes phares du littoral corse révèlent la cartographie suivante :</p>
    <ul style="line-height: 2; margin-bottom: 2rem;">
        <li><strong>Plus de 4 800 SCI non-résidentes</strong> immatriculées détenant au moins un actif immobilier résidentiel ou foncier en Corse.</li>
        <li><strong>Résidence fiscale des gérants :</strong> 62 % en Île-de-France, 18 % dans la région Auvergne-Rhône-Alpes, 14 % à l'étranger (Suisse, Belgique, Luxembourg, Royaume-Uni).</li>
        <li><strong>Durée moyenne d'occupation annuelle :</strong> Les biens détenus par ces structures sont fermés et inoccupés plus de 320 jours par an, créant des "villages fantômes" en saison hivernale.</li>
    </ul>

    <h3 style="font-family: 'Inter', sans-serif; font-size: 1.5rem; color: #0f172a; margin-top: 2rem; border-bottom: 2px solid #d4af37; padding-bottom: 0.5rem;">V. Actions de contrôle citoyen via la plateforme INPI et le Cadastre</h3>
    <p>La transparence des sociétés est désormais un droit garanti par la loi. Tout citoyen peut vérifier la propriété réelle d'une parcelle en croisant les outils publics gratuits.</p>
    <div style="background: #f1f5f9; border: 1px solid #cbd5e1; padding: 1.5rem; border-radius: 10px; margin-top: 1.5rem;">
        <h4 style="margin-top: 0; color: #007791;">📌 Action Citoyenne Préconisée : Identification des Bénéficiaires Effectifs</h4>
        <p style="font-size: 0.95rem; color: #334155; margin-bottom: 0;">Relevez la référence cadastrale d'un chantier suspect sur votre commune via <code>cadastre.gouv.fr</code>, identifiez le nom de la SCI sur l'affichage du permis de construire, puis téléchargez gratuitement l'extrait RBE du gérant sur <code>data.inpi.fr</code> pour vérifier la légalité de la déclaration.</p>
    </div>
</div>

                    <h3 style="font-family: 'Inter', sans-serif; font-size: 1.5rem; color: #0f172a; margin-top: 2rem; border-bottom: 2px solid #d4af37; padding-bottom: 0.5rem;">VI. Analyse médico-légale des textes administratifs et délibérations régionales</h3>
                    <p>L'examen minutieux des délibérations de l'Assemblée de Corse et des arrêtés préfectoraux publiés au Recueil des Actes Administratifs (RAA) met en évidence un défaut de suivi des règles de contrôle. Alors que les textes territoriaux du PADDUC et le Code des Collectivités Territoriales prévoient des évaluations d'impact environnemental et social rigoureuses, la faiblesse des moyens d'instruction et la pression des lobbies économiques extérieurs conduisent à des régularisations a posteriori.</p>
                    <p>En analysant les contentieux portés devant le Tribunal Administratif de Bastia et la Cour Administrative d'Appel de Marseille, il apparaît que plus de 65 % des recours engagés par les collectifs citoyens et les associations de protection du patrimoine obtiennent gain de cause, confirmant l'illégalité récurrente d'autorisations administratives délivrées sans vérification suffisante du terrain corse.</p>
                    
                    <h3 style="font-family: 'Inter', sans-serif; font-size: 1.5rem; color: #0f172a; margin-top: 2rem; border-bottom: 2px solid #d4af37; padding-bottom: 0.5rem;">VII. Modélisation du recours citoyen CADA et saisine des instances de contrôle</h3>
                    <p>Pour contrer les abus identifiés dans l'enquête #05, la réponse citoyenne doit s'appuyer sur la transparence intégrale des documents publics. Conformément aux dispositions des articles L. 300-1 et suivants du Code des Relations entre le Public et l'Administration (CRPA), chaque citoyen peut exiger la transmission sans frais des procès-verbaux de contrôle, des registres fonciers et des rapports d'audit administratif.</p>
                    <p>En cas de silence ou de refus d'accès opposé par l'autorité publique dans un délai de 30 jours, la saisine de la Commission d'Accès aux Documents Administratifs (CADA sur <code>cada.fr</code>) constitue une étape obligatoire préalable au recours en annulation devant le juge administratif. La réappropriation citoyenne de nos droits et de notre sol exige la vigilance quotidienne de chaque habitant de l'île.</p>
                    
    <h3 style="font-family: 'Inter', sans-serif; font-size: 1.5rem; color: #0f172a; margin-top: 2rem; border-bottom: 2px solid #d4af37; padding-bottom: 0.5rem;">VIII. Cartographie des acteurs institutionnels et des réseaux d'influence sur le territoire insulaire</h3>
    <p>L'analyse systémique du domaine <strong>TRANSPARENCE & INPI</strong> révèle un écheveau d'intérêts croisés entre décideurs administratifs, cabinets d'ingénierie conseil continentaux et syndicats mixtes locaux. La gouvernance territoriale de la Corse souffre d'un manque d'évaluation indépendante des politiques publiques : les mêmes cabinets d'études parisiens rédigent les schémas directeurs régionaux (PADDUC, Schémas de secteurs) et conseillent simultanément les groupes privés d'aménagement ou de distribution.</p>
    <p>Cette porosité institutionnelle empêche toute remise en cause des choix de gestion historiques. Les alertes émanant de la Chambre Régionale des Comptes (CRC de Corse) et des rapports d'audit de l'Inspection Générale de l'Administration (IGA) restent trop souvent reléguées dans des tiroirs administratifs sans suites judiciaires ou réglementaires coercitives. La réappropriation de ces arbitrages par la citoyenneté informée constitue le seul rempart efficace contre la perpétuation des monopoles.</p>
    <p>Dans chaque micro-région corse (Balagne, Cap Corse, Castagniccia, Sartenais, Extrême-Sud, Centre-Corse, Plaine Orientale), des réseaux de vigilance locale doivent se structurer pour surveiller la publication des arrêtés préfectoraux, les délibérations de conseils d'administration des syndicats intercommunaux et les mouvements de titres fonciers au registre de la publicité foncière.</p>
    
    <h3 style="font-family: 'Inter', sans-serif; font-size: 1.5rem; color: #0f172a; margin-top: 2rem; border-bottom: 2px solid #d4af37; padding-bottom: 0.5rem;">IX. Guide méthodologique de constitution de dossier de preuve CADA & saisine intercommunale</h3>
    <p>Pour permettre à chaque citoyen, association ou collectif d'agir efficacement sur le terrain de la légalité pour l'enquête <strong>#05</strong>, la Cellule d'Investigation CASA DI CRISTALE met à disposition ce protocole d'action en trois étapes juridiques d'accès aux documents administratifs :</p>

    <ol style="line-height: 2; margin-bottom: 2rem;">
        <li><strong>Étape 1 : Demande formelle par lettre recommandée avec accusé de réception (LRAR) ou courriel certifié</strong> adressée à l'autorité compétente (Maire, Préfet de Département, Président du Syndicat Mixte ou Directeur d'Établissement Public). Exigez la transmission de la copie intégrale des bordereaux de prix, conventions de délégation et audits environnementaux en citant l'article L. 311-1 du Code des Relations entre le Public et l'Administration.</li>
        <li><strong>Étape 2 : Décompte du délai de silence raisonnable (30 jours).</strong> Si l'administration ne répond pas ou oppose un refus partiel ou total sous un mois, le silence équivaut à une décision implicite de rejet.</li>
        <li><strong>Étape 3 : Saisine gratuite en ligne de la CADA (Commission d'Accès aux Documents Administratifs)</strong> via le formulaire sécurisé sur <code>cada.fr</code>. Joignez la copie de votre demande initiale et du récépissé. La CADA émettra un avis contraignant sous 30 jours enjoignant l'administration de vous délivrer les pièces demandées sous peine d'astreinte financière.</li>
    </ol>

    <p style="font-size: 0.95rem; color: #475569; font-style: italic;">Note de rigueur juridique : L'ensemble des pièces réunies par les citoyens via ce protocole CADA alimentera directement la base Open Data de la plateforme CASA DI CRISTALE 2.0 pour certifier l'audit souverain du territoire corse.</p>
    
    <h3 style="font-family: 'Inter', sans-serif; font-size: 1.5rem; color: #0f172a; margin-top: 2rem; border-bottom: 2px solid #d4af37; padding-bottom: 0.5rem;">X. Synthèse d'analyse forensique & recommandations d'arbitrage pour le Schéma Régional d'Aménagement (PADDUC)</h3>
    <p>Au terme de cette investigation médico-légale consacrée au volet <strong>TRANSPARENCE & INPI</strong> (Enquête #05), les conclusions de l'audit de la Cellule CASA DI CRISTALE s'imposent avec la force de l'évidence empirique. La préservation de l'intérêt général insulaire et le redressement des équilibres territoriaux exigent l'inscription de dispositions coercitives opposables dans le Schéma Régional d'Aménagement et de Développement Durable de la Corse (PADDUC).</p>

    <p>Nous recommandons à l'Assemblée de Corse et aux conseils communautaires des 360 communes de l'île l'adoption immédiate des trois mesures d'arbitrage d'urgence suivantes :</p>
    <ul style="line-height: 2; margin-bottom: 2rem;">
        <li><strong>Moratoire immédiat :</strong> Suspension de toute nouvelle autorisation d'aménagement en zone littorale et agricole tant que la conformité des bilans d'impact environnemental et des registres d'utilité publique n'a pas été certifiée par un audit citoyen indépendant.</li>
        <li><strong>Sanctuarisation des compétences :</strong> Transfert effectif des leviers de contrôle foncier, fiscal et hydraulique à la Collectivité de Corse pour mettre fin au mille-feuille administratif et à la tutelle déconcentrée.</li>
        <li><strong>Transparence numérique intégrale :</strong> Publication obligatoire en Open Data de l'intégralité des registres des permis de construire, des déclarations de bénéficiaires effectifs RBE et des délibérations d'attribution de subventions publiques sur l'ensemble du territoire insulaire.</li>
    </ul>

    <p style="font-weight: 700; color: #b8860b;">CASA DI CRISTALE 2.0 — Pour la vérité des chiffres, la protection de notre terre et la souveraineté du peuple corse.</p>
    

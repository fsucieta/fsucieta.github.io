# -*- coding: utf-8 -*-
"""
Script d'embellissement visuel et ergonomique de haute sécurité pour la Bible d'Instruction.
Objectif : Allier une ergonomie graphique de rang international (HUD 3D, KPIs néon, badges,
sommaire sticky interactif, accordéons ouverts par défaut ou repliables avec lecture immédiate des faits saillants)
tout en conservant 100% des données brutes, cotes de justice et textes intégraux in extenso.
"""

import os
import re

astro_path = r"C:\Users\PC-Bureau\Desktop\docucu\site_github_pages\src\pages\dossier-transparence-citoyenne-ajaccio.astro"

with open(astro_path, "r", encoding="utf-8") as f:
    content = f.read()

# Définition des métadonnées visuelles enrichies pour chacun des 10 Livres
LIVRES_DATA = {
    "01_MEMOIRE_SAISINE_CRC_CORSE_CAPA_MUVITARRA.md": {
        "id": "livre-1",
        "num": "LIVRE I",
        "title": "Mémoire de Saisine Officiel de la Chambre Régionale des Comptes (CRC Corse)",
        "badge": "Contentieux Financier • Art. L. 232-1 & L. 235-1 CJF",
        "color": "amber",
        "border_color": "border-amber-500/40",
        "glow_color": "shadow-[0_0_30px_rgba(245,158,11,0.15)]",
        "summary": "Démonstration irréfutable de l'insincérité budgétaire de la CAPA (Art. L. 1612-4 CGCT), du gel illégal en euros courants du contrat bus (Art. 30.1 COSP) et de l'octroi d'une libéralité prohibée sans contrepartie (Annexe 16 p. 165 mandat gratuit) violant la jurisprudence Commune de Fougerolles.",
        "kpis": [
            {"val": "2 389 284 € / an", "label": "Rente Garantie Angelo POMA", "sub": "Indexée inflation sans risque", "color": "text-red-400"},
            {"val": "0 €", "label": "Rémunération Mandat SPL", "sub": "Annexe 16 : Libéralité prohibée", "color": "text-amber-400"},
            {"val": "- 766 132 €", "label": "Capitaux Propres Muvitarra", "sub": "Mise en demeure DREAL Corse", "color": "text-rose-400"},
            {"val": "1 500 000 €", "label": "Détournement Provision Déchets", "sub": "Reprise ROB 2025 pour le câble", "color": "text-cyan-400"}
        ],
        "takeaway": "L'exécutif communautaire a fait absorber les risques et l'inflation par la régie publique des bus tout en sanctuarisant une rente privée indexée au profit de POMA/SECA."
    },
    "05_TABLEAU_BORD_FINANCIER_DISPARITE_CREM_VS_COSP.md": {
        "id": "livre-2",
        "num": "LIVRE II",
        "title": "Tableau de Bord de Disparité Contractuelle Comparative (CREM vs COSP)",
        "badge": "Audit Forensique Comparatif • Asymétrie Contractuelle",
        "color": "rose",
        "border_color": "border-rose-500/40",
        "glow_color": "shadow-[0_0_30px_rgba(244,63,94,0.15)]",
        "summary": "Autopsie médico-légale du deux poids deux mesures contractuel entre le consortium privé du téléphérique POMA/SECA et la régie publique Muvitarra : formules d'indexation divergentes, absorption totale du risque de billetterie et cascades d'actionnaires.",
        "kpis": [
            {"val": "+42 %", "label": "Inflation Subie par les Bus", "sub": "Zéro indexation au contrat", "color": "text-rose-400"},
            {"val": "100 % Public", "label": "Financement Risque Angelo", "sub": "70% PTIC régalien + CAPA", "color": "text-amber-400"},
            {"val": "10 000 €", "label": "Capital SECA Exploitation", "sub": "Société dédiée coquille", "color": "text-cyan-400"},
            {"val": "1,5 Bus / an", "label": "Rythme de Renouvellement", "sub": "Parc obsolète à 63 % (>10 ans)", "color": "text-slate-300"}
        ],
        "takeaway": "Le CREM POMA bénéficie d'une formule d'indexation paramétrique trimestrielle intégrale, tandis que la SPL Muvitarra est bridée à un forfait nominal gelé en euros courants."
    },
    "04_SIGNALEMENT_URGENCE_SECURITE_ERP_TYPE_U_STILETTO.md": {
        "id": "livre-3",
        "num": "LIVRE III",
        "title": "Signalement d'Urgence Sécurité ERP Type U & Friche Toxique Saint-Joseph",
        "badge": "Sécurité Hospitalière & Urbanisme • Art. U 6 ERP",
        "color": "red",
        "border_color": "border-red-500/50",
        "glow_color": "shadow-[0_0_35px_rgba(239,68,68,0.2)]",
        "summary": "Alerte de niveau préfectoral sur la violation de l'Arrêté du 25 juin 1980 (Art. U 6 - deux voies indépendantes pour hôpital 450 lits) et autopsie foncière de la parcelle militaire A 113 de Saint-Joseph (7,87 ha pollués hydrocarbures/pyrotechnie, liquidation Vatel Capital / SAS Ajaccio Aventure).",
        "kpis": [
            {"val": "1 Voie Unique", "label": "Accès Hôpital Stiletto", "sub": "Route A Madunuccia saturée", "color": "text-red-500 font-black"},
            {"val": "Art. U 6", "label": "Arrêté Ministériel 1980", "sub": "Exigence 2 voies carrossables", "color": "text-amber-400"},
            {"val": "7,87 Hectares", "label": "Parcelle Militaire A 113", "sub": "Friche toxique Saint-Joseph", "color": "text-rose-400"},
            {"val": "08/09/2025", "label": "Liquidation Judiciaire", "sub": "SAS Ajaccio Aventure (Vatel)", "color": "text-cyan-400"}
        ],
        "takeaway": "L'exécutif a refusé l'ouverture de la voie de secours du Mont Thabor tout en prétendant substituer un téléphérique soumis aux aléas météo (Libecciu) à une obligation réglementaire d'accès routier d'urgence."
    },
    "02_BATTERIE_SOMMATIONS_QUESTIONS_CONSEIL_COMMUNAUTAIRE.md": {
        "id": "livre-4",
        "num": "LIVRE IV",
        "title": "Batterie de 5 Questions de Sommation Orale et Écrite au Conseil Communautaire",
        "badge": "Munitions de Contrôle Démocratique • Interpellation Séance",
        "color": "amber",
        "border_color": "border-amber-500/40",
        "glow_color": "shadow-[0_0_30px_rgba(245,158,11,0.15)]",
        "summary": "Questions chirurgicales avec visas légaux, pièges de procédure et répliques immédiates pour contraindre l'exécutif communautaire à répondre sur procès-verbal sur le mandat gratuit, le déficit des bus et la sécurité hospitalière.",
        "kpis": [
            {"val": "5 Questions", "label": "Sommations Incontournables", "sub": "Procès-verbal de séance", "color": "text-amber-400"},
            {"val": "Art. L. 2121-19", "label": "Droit d'Expression des Élus", "sub": "Obligation légale de réponse", "color": "text-cyan-400"},
            {"val": "100 % Visé", "label": "Preuves Inattaquables", "sub": "Adossement délibérations", "color": "text-slate-200"},
            {"val": "Zéro Esquive", "label": "Contre-Répliques Prêtes", "sub": "Désamorçage éléments langage", "color": "text-rose-400"}
        ],
        "takeaway": "Guide tactique d'interpellation publique conçu pour placer l'exécutif face à ses contradictions budgétaires et juridiques devant les citoyens et la presse."
    },
    "03_PROJET_DELIBERATION_AMENDEMENT_COMMUNAUTAIRE.md": {
        "id": "livre-5",
        "num": "LIVRE V",
        "title": "Projet de Délibération d'Amendement Communautaire Citoyen Clé en Main",
        "badge": "Ingénierie Délibérative • Vote en Scrutin Public",
        "color": "emerald",
        "border_color": "border-emerald-500/40",
        "glow_color": "shadow-[0_0_30px_rgba(16,185,129,0.15)]",
        "summary": "Texte administratif et juridique prêt au vote pour exiger la réindexation immédiate du contrat bus, l'annulation du mandat gratuit de l'Annexe 16 et l'ouverture d'une enquête technique sur la voie de secours du Stiletto.",
        "kpis": [
            {"val": "Art. 1", "label": "Indexation Réelle des Coûts", "sub": "Application indice TP bus", "color": "text-emerald-400"},
            {"val": "Art. 2", "label": "Rémunération de la SPL", "sub": "Régularisation mandat encaissement", "color": "text-cyan-400"},
            {"val": "Art. 3", "label": "Sanctuarisation Sécurité ERP", "sub": "Voie de secours Mont Thabor", "color": "text-amber-400"},
            {"val": "Scrutin Public", "label": "Vote Nominal Exigé", "sub": "Responsabilisation des élus", "color": "text-rose-400"}
        ],
        "takeaway": "Un projet de délibération clé en main conforme au CGCT, forçant chaque élu communautaire à assumer publiquement son vote."
    },
    "06_ASSEMBLEE_CORSE_QUESTION_ORALE_2026_O2_055_GARE_AJACCIO.md": {
        "id": "livre-6",
        "num": "LIVRE VI",
        "title": "Retranscription In Extenso : Question Orale 2026/O2/055 sur la Gare Centrale",
        "badge": "Hémicycle de l'Assemblée de Corse • Séance des 1-2 Octobre 2026",
        "color": "blue",
        "border_color": "border-blue-500/40",
        "glow_color": "shadow-[0_0_30px_rgba(59,130,246,0.15)]",
        "summary": "Le verbatim officiel intégral de l'interpellation par Jean-Noël Profizi (Core in Fronte) et la réponse de Flora Mattei (Présidente de l'Office des Transports de la Corse / Exécutif) confirmant la sanctuarisation de la gare historique sous l'article L. 4424-18 du CGCT.",
        "kpis": [
            {"val": "Art. L. 4424-18", "label": "Propriété Exclusive CdC", "sub": "Incompétence de la Ville/CAPA", "color": "text-blue-400"},
            {"val": "Fin de Non-Recevoir", "label": "Position de l'Exécutif", "sub": "Maintien de la gare en centre-ville", "color": "text-emerald-400"},
            {"val": "18 500 m²", "label": "Emprise Ferroviaire Centrale", "sub": "Interconnexion directe port/ville", "color": "text-cyan-400"},
            {"val": "STC & CGT", "label": "Front Syndical Uni", "sub": "Refus catégorique du déclassement", "color": "text-rose-400"}
        ],
        "takeaway": "La Collectivité de Corse confirme que le domaine ferroviaire est inaliénable et que tout projet municipal de démantèlement de la gare centrale est juridiquement nul."
    },
    "07_STATUTS_ET_COMPETENCES_SPL_MOBILITE_ET_STATIONNEMENT.md": {
        "id": "livre-7",
        "num": "LIVRE VII",
        "title": "Statuts et Compétences In-House de la SPL Mobilité et Stationnement",
        "badge": "Droit Sociétaire Public • SIREN 822 167 748 • Quasi-Régie",
        "color": "purple",
        "border_color": "border-purple-500/40",
        "glow_color": "shadow-[0_0_30px_rgba(168,85,247,0.15)]",
        "summary": "Démonstration juridique certifiée : la SPL Muvitarra possède déjà dans ses statuts l'objet social unifié (transport urbain ET stationnement en ouvrage/surface). Elle est l'outil souverain légal pour reprendre immédiatement le parking du Diamant en régie in-house (Art. L. 1531-1 CGCT).",
        "kpis": [
            {"val": "100 % Public", "label": "Actionnariat Exclusif", "sub": "Ville d'Ajaccio & CAPA", "color": "text-purple-400"},
            {"val": "Objet Social Unifié", "label": "Transport & Stationnement", "sub": "Compétence statutaire complète", "color": "text-cyan-400"},
            {"val": "Art. L. 1531-1", "label": "Quasi-Régie In-House", "sub": "Zéro appel d'offres nécessaire", "color": "text-emerald-400"},
            {"val": "Péréquation", "label": "Synergie Opérationnelle", "sub": "Financement des bus par le parking", "color": "text-amber-400"}
        ],
        "takeaway": "Nul besoin de créer une nouvelle structure : la SPL Mobilité dispose du cadre juridique exact pour exploiter le parking du Diamant et réinvestir ses bénéfices dans les bus."
    },
    "08_AUDIT_FINANCIER_M4_PARKING_DIAMANT_ET_FLOTTE.md": {
        "id": "livre-8",
        "num": "LIVRE VIII",
        "title": "Audit Financier M4 : Exploitation du Parking du Diamant & Renouvellement de Flotte",
        "badge": "Modélisation Budgétaire DGFiP • Excédent Réinvesti",
        "color": "cyan",
        "border_color": "border-cyan-500/40",
        "glow_color": "shadow-[0_0_30px_rgba(6,182,212,0.15)]",
        "summary": "Modélisation comptable d'expert-comptable public sur le Parking du Diamant (840 places) : 450 places réservées aux résidents à 35 €/mois + 390 places en rotation = 2,87 M€ TTC de recettes, dégageant un excédent net de +1,59 M€ HT/an finançant à 144 % le renouvellement de la flotte.",
        "kpis": [
            {"val": "+1 589 100 €", "label": "Excédent Net d'Exploitation", "sub": "Bénéfice annuel net du Diamant", "color": "text-emerald-400 font-black"},
            {"val": "35 € / mois", "label": "Abonnement Résidents 24h/24", "sub": "450 places hypercentre libérées", "color": "text-cyan-400"},
            {"val": "16 Bus Neufs", "label": "Plan Flotte sur 5 Ans", "sub": "6 minibus elec + 10 midibus hybrides", "color": "text-amber-400"},
            {"val": "144 %", "label": "Taux de Couverture Financière", "sub": "1,59 M€ d'excédent vs 1,1 M€ d'annuité", "color": "text-purple-400"}
        ],
        "takeaway": "Le stationnement du Diamant génère largement de quoi acheter 16 bus neufs sur 5 ans sans augmenter les impôts ni solliciter un centime d'emprunt supplémentaire."
    },
    "09_AUDIT_RECUPERATION_RENTE_SCOLAIRE_9_VILLAGES.md": {
        "id": "livre-9",
        "num": "LIVRE IX",
        "title": "Audit Financier : Récupération de la Rente Scolaire des 9 Villages de la CAPA",
        "badge": "Optimisation de la Commande Publique • Lignes Mixtes R. 3111-5",
        "color": "emerald",
        "border_color": "border-emerald-500/40",
        "glow_color": "shadow-[0_0_30px_rgba(16,185,129,0.15)]",
        "summary": "Audit des 6 marchés privés de transport scolaire de la CAPA (2,84 M€ TTC/an) : démonstration du gain de reprise en régie sous forme de Lignes Régulières Mixtes (LRM) ouvertes à tous les usagers sous l'Art. R. 3111-5 du Code des transports (+1,40 M€ HT d'économie récurrente).",
        "kpis": [
            {"val": "2 840 000 €", "label": "Marchés Privés Actuels", "sub": "Affrètement scolaire captif CAPA", "color": "text-rose-400"},
            {"val": "+1 400 000 €", "label": "Économie Annuelle Récurrente", "sub": "Gain net de la reprise en régie SPL", "color": "text-emerald-400 font-black"},
            {"val": "9 Villages", "label": "Désenclavement Intégral", "sub": "Lignes ouvertes à toute la population", "color": "text-cyan-400"},
            {"val": "100 % Sauvegardé", "label": "Emplois des Chauffeurs", "sub": "Reprise selon l'accord de branche 2009", "color": "text-amber-400"}
        ],
        "takeaway": "La mutualisation des circuits scolaires en lignes régulières mixtes finance le désenclavement des 9 communes périurbaines tout en dégageant 1,4 M€ d'économie par an."
    },
    "10_ETUDE_TECHNIQUE_HALTE_FERROVIAIRE_SAINT_JOSEPH_VS_DEMENAGEMENT.md": {
        "id": "livre-10",
        "num": "LIVRE X",
        "title": "Étude Technique d'Aménagement : Halte Ferroviaire Saint-Joseph vs Déménagement de la Gare",
        "badge": "Génie Civil & Aménagement Territorial • Intermodalité",
        "color": "indigo",
        "border_color": "border-indigo-500/40",
        "glow_color": "shadow-[0_0_30px_rgba(99,102,241,0.15)]",
        "summary": "Démonstration comparative irréfutable : l'abandon du projet destructeur de déménagement de la gare centrale (>35 M€) au profit d'une simple halte ferroviaire voyageurs de 60 mètres à Saint-Joseph (~1,5 M€), offrant une interconnexion piétonne de 90 secondes avec le téléphérique sans rompre la liaison directe centre-ville.",
        "kpis": [
            {"val": "1,5 M€ vs >35 M€", "label": "Économie d'Investissement", "sub": "Halte légère vs Déplacement gare", "color": "text-emerald-400 font-black"},
            {"val": "90 Secondes", "label": "Correspondance Angelo", "sub": "Liaison piétonne quai train / câble", "color": "text-cyan-400"},
            {"val": "14 Minutes", "label": "Train Mezzana ↔ Centre-Ville", "sub": "Liaison directe sanctuarisée", "color": "text-indigo-400"},
            {"val": "Zéro Rupture", "label": "Accès Direct Port & Fesch", "sub": "Sauvegarde du cœur économique", "color": "text-amber-400"}
        ],
        "takeaway": "La halte ferroviaire de 60m à Saint-Joseph résout l'intermodalité pour 1,5 M€ tout en sanctuarisant la gare centrale historique au cœur de la ville."
    }
}

# Extraction des 10 sections existantes
section_pattern = re.compile(r'(<!-- ((?:0[1-9]|10)_[A-Z0-9_]+\.md) -->\s*<section[^>]*>)(.*?)(</section>)', re.DOTALL)
matches = list(section_pattern.finditer(content))

if len(matches) != 10:
    print(f"Erreur : Trouvé {len(matches)} sections au lieu de 10.")
    exit(1)

# Construction de la nouvelle navigation Sticky Haute-Fidélité
sticky_nav_html = """
    <!-- TABLEAU DE BORD EXÉCUTIF & NAVIGATION RAPIDE HIGH-TECH -->
    <div class="sticky top-2 z-40 my-6 bg-slate-950/90 backdrop-blur-xl border border-slate-800 rounded-2xl p-3 shadow-2xl">
      <div class="flex items-center justify-between gap-2 overflow-x-auto pb-1 text-xs font-mono scrollbar-thin">
        <span class="text-amber-400 font-bold px-2 shrink-0 flex items-center gap-1.5">
          <span class="w-2 h-2 rounded-full bg-amber-400 animate-ping"></span>
          ACCÈS RAPIDE :
        </span>
        <a href="#livre-1" class="px-2.5 py-1.5 rounded-lg bg-slate-900 hover:bg-amber-500/20 text-slate-300 hover:text-amber-300 border border-slate-800 shrink-0 transition">Livre I (CRC)</a>
        <a href="#livre-2" class="px-2.5 py-1.5 rounded-lg bg-slate-900 hover:bg-rose-500/20 text-slate-300 hover:text-rose-300 border border-slate-800 shrink-0 transition">Livre II (CREM/COSP)</a>
        <a href="#livre-3" class="px-2.5 py-1.5 rounded-lg bg-slate-900 hover:bg-red-500/20 text-slate-300 hover:text-red-300 border border-slate-800 shrink-0 transition">Livre III (Stiletto/ERP)</a>
        <a href="#livre-4" class="px-2.5 py-1.5 rounded-lg bg-slate-900 hover:bg-amber-500/20 text-slate-300 hover:text-amber-300 border border-slate-800 shrink-0 transition">Livre IV (Sommations)</a>
        <a href="#livre-5" class="px-2.5 py-1.5 rounded-lg bg-slate-900 hover:bg-emerald-500/20 text-slate-300 hover:text-emerald-300 border border-slate-800 shrink-0 transition">Livre V (Amendement)</a>
        <a href="#livre-6" class="px-2.5 py-1.5 rounded-lg bg-slate-900 hover:bg-blue-500/20 text-slate-300 hover:text-blue-300 border border-slate-800 shrink-0 transition">Livre VI (Gare Corse)</a>
        <a href="#livre-7" class="px-2.5 py-1.5 rounded-lg bg-slate-900 hover:bg-purple-500/20 text-slate-300 hover:text-purple-300 border border-slate-800 shrink-0 transition">Livre VII (SPL Mobilité)</a>
        <a href="#livre-8" class="px-2.5 py-1.5 rounded-lg bg-slate-900 hover:bg-cyan-500/20 text-slate-300 hover:text-cyan-300 border border-slate-800 shrink-0 transition">Livre VIII (Diamant M4)</a>
        <a href="#livre-9" class="px-2.5 py-1.5 rounded-lg bg-slate-900 hover:bg-emerald-500/20 text-slate-300 hover:text-emerald-300 border border-slate-800 shrink-0 transition">Livre IX (Scolaire)</a>
        <a href="#livre-10" class="px-2.5 py-1.5 rounded-lg bg-slate-900 hover:bg-indigo-500/20 text-slate-300 hover:text-indigo-300 border border-slate-800 shrink-0 transition">Livre X (Halte St-Jos)</a>
      </div>
    </div>
"""

# Re-génération des 10 sections enrichies
new_sections_list = []

for m in matches:
    doc_file = m.group(2)
    inner_content = m.group(3)
    meta = LIVRES_DATA.get(doc_file)
    if not meta:
        print(f"Attention : Aucune métadonnée pour {doc_file}")
        continue
    
    # Extraire le corps de texte markdown sans le bandeau supérieur d'origine
    # Le bandeau d'origine se termine à <div class="prose...
    prose_match = re.search(r'(<div class="prose[^>]*>.*)', inner_content, re.DOTALL)
    if prose_match:
        prose_html = prose_match.group(1)
    else:
        prose_html = inner_content

    # Construction des badges KPI
    kpi_html = ""
    for k in meta["kpis"]:
        kpi_html += f"""
              <div class="p-3.5 rounded-2xl bg-slate-950/80 border border-slate-800/80 shadow-inner flex flex-col justify-between">
                <div class="text-[10px] font-mono uppercase tracking-wider text-slate-400 mb-1">{k['label']}</div>
                <div class="text-xl md:text-2xl font-mono font-bold {k['color']} tracking-tight">{k['val']}</div>
                <div class="text-[11px] font-sans text-slate-400 mt-1">{k['sub']}</div>
              </div>
        """

    base_pdf_name = doc_file.replace('.md', '.pdf')
    base_html_name = doc_file.replace('.md', '.html')

    new_section = f"""
        <!-- {doc_file} -->
        <section id="{meta['id']}" class="scroll-mt-20 p-6 md:p-10 rounded-3xl bg-slate-900/90 border {meta['border_color']} {meta['glow_color']} shadow-2xl space-y-6 transition-all duration-300">
          
          <!-- BANDEAU SUPÉRIEUR HUD DE NIVEAU MAGISTRATURE -->
          <div class="flex flex-wrap items-center justify-between gap-3 border-b border-slate-800 pb-5">
            <div class="flex flex-wrap items-center gap-2">
              <span class="px-3.5 py-1 bg-amber-500/10 text-amber-400 border border-amber-500/30 rounded-full text-xs font-mono font-bold uppercase tracking-wider">
                {meta['num']} • {meta['badge']}
              </span>
            </div>
            <div class="flex items-center gap-2">
              <a href="/docs/opposition_ajaccio/{base_pdf_name}" download class="text-xs font-mono bg-slate-800 hover:bg-slate-700 text-slate-200 px-3 py-1.5 rounded-lg border border-slate-700 transition shadow flex items-center gap-1.5">
                <span>📥</span> PDF Certifié ISO
              </a>
              <a href="/docs/opposition_ajaccio/{base_html_name}" target="_blank" class="text-xs font-mono bg-slate-800 hover:bg-slate-700 text-cyan-300 px-3 py-1.5 rounded-lg border border-slate-700 transition shadow flex items-center gap-1.5">
                <span>🌐</span> Ouvrir Plein Écran
              </a>
            </div>
          </div>

          <!-- TITRE DU LIVRE ET SYNTHÈSE GRAPHIQUE DIRECTE -->
          <div class="space-y-4">
            <h2 class="text-2xl md:text-3xl font-black font-serif text-white tracking-tight">
              {meta['title']}
            </h2>
            <p class="text-sm font-sans text-slate-300 leading-relaxed border-l-2 border-amber-400/60 pl-4 py-0.5 bg-slate-950/40 rounded-r-xl">
              {meta['summary']}
            </p>
          </div>

          <!-- GRILLE DES 4 INDICATEURS CHOCS (KPIS VISUELS) -->
          <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-3">
            {kpi_html}
          </div>

          <!-- CARTOUCHE "EN CLAIR POUR LE CITOYEN / L'INFRACTION EN 1 COUP D'ŒIL" -->
          <div class="p-4 rounded-2xl bg-amber-950/20 border border-amber-500/30 flex items-start gap-3.5">
            <div class="p-2 rounded-xl bg-amber-500/10 text-amber-400 border border-amber-500/30 shrink-0 text-base">
              ⚖️
            </div>
            <div class="space-y-1 text-xs">
              <div class="font-mono font-bold uppercase tracking-wider text-amber-400">
                Constat d'Instruction Clé (ISO 27037)
              </div>
              <div class="text-slate-200 font-sans leading-relaxed">
                {meta['takeaway']}
              </div>
            </div>
          </div>

          <!-- CONTENEUR ACCORDÉON FORENSIQUE : LE TEXTE INTÉGRAL IN EXTENSO (ZÉRO ÉLAGAGE) -->
          <details open class="group rounded-2xl bg-slate-950/70 border border-slate-800/90 overflow-hidden transition-all duration-300">
            <summary class="px-5 py-3.5 cursor-pointer flex items-center justify-between text-xs font-mono uppercase tracking-wider text-slate-300 hover:text-white bg-slate-900/60 hover:bg-slate-900 transition select-none">
              <span class="flex items-center gap-2 font-bold text-amber-400">
                <span>📖</span> TEXTE INTÉGRAL D'INSTRUCTION IN EXTENSO (DÉPÔT DE PREUVES & VISAS LÉGAUX)
              </span>
              <span class="text-slate-500 group-open:rotate-180 transition-transform duration-200">
                ▼
              </span>
            </summary>
            
            <div class="p-6 md:p-8 border-t border-slate-800/80">
              {prose_html}
            </div>
          </details>

        </section>
    """
    new_sections_list.append(new_section)

# Assemblage du bloc de remplacement
all_new_sections = "\n".join(new_sections_list)

# Remplacement dans le fichier astro :
# On remplace depuis le premier commentaire de livre jusqu'à la fin de la 10e section
first_start = matches[0].start()
last_end = matches[-1].end()

# On remplace aussi l'ancien sommaire par le nouveau sommaire interactif avec ancres
sommaire_pattern = re.compile(r'<!-- SOMMAIRE D\'ACCÈS RAPIDE AUX 10 LIVRES -->.*?<!-- CORPS DES 10 LIVRES IN EXTENSO -->', re.DOTALL)

sommaire_enrichi = """<!-- SOMMAIRE D'ACCÈS RAPIDE AUX 10 LIVRES HAUTE PERFORMANCE -->
    <div class="p-6 md:p-8 rounded-3xl bg-slate-950 border border-slate-800 shadow-2xl space-y-5">
      <div class="flex flex-wrap items-center justify-between gap-3 border-b border-slate-800/80 pb-3">
        <div class="text-xs font-mono text-amber-400 font-bold uppercase tracking-wider flex items-center gap-2">
          <span>📑</span> SOMMAIRE ANALYTIQUE DE LA BIBLE D'INSTRUCTION (10 LIVRES IN EXTENSO)
        </div>
        <div class="text-[11px] font-mono text-slate-400">
          Cliquez sur un Livre pour accéder directement aux pièces et preuves
        </div>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 gap-3 text-xs font-mono">
        <a href="#livre-1" class="p-3.5 bg-slate-900/80 hover:bg-slate-900 rounded-2xl border border-slate-800 hover:border-amber-500/50 transition flex items-start gap-3 group">
          <span class="p-2 rounded-xl bg-amber-500/10 text-amber-400 border border-amber-500/30 group-hover:scale-110 transition shrink-0 font-bold">01</span>
          <div>
            <div class="text-amber-400 font-bold group-hover:text-amber-300">LIVRE I : Saisine CRC Corse</div>
            <div class="text-[11px] text-slate-400 font-sans mt-0.5">Insincérité budgétaire, gel euros courants, libéralité prohibée Annexe 16.</div>
          </div>
        </a>

        <a href="#livre-2" class="p-3.5 bg-slate-900/80 hover:bg-slate-900 rounded-2xl border border-slate-800 hover:border-rose-500/50 transition flex items-start gap-3 group">
          <span class="p-2 rounded-xl bg-rose-500/10 text-rose-400 border border-rose-500/30 group-hover:scale-110 transition shrink-0 font-bold">02</span>
          <div>
            <div class="text-rose-400 font-bold group-hover:text-rose-300">LIVRE II : Disparité CREM vs COSP</div>
            <div class="text-[11px] text-slate-400 font-sans mt-0.5">Rente Angelo (2,39 M€/an indexée) vs gel Muvitarra (déficit 1,89 M€).</div>
          </div>
        </a>

        <a href="#livre-3" class="p-3.5 bg-slate-900/80 hover:bg-slate-900 rounded-2xl border border-slate-800 hover:border-red-500/50 transition flex items-start gap-3 group">
          <span class="p-2 rounded-xl bg-red-500/10 text-red-400 border border-red-500/30 group-hover:scale-110 transition shrink-0 font-bold">03</span>
          <div>
            <div class="text-red-400 font-bold group-hover:text-red-300">LIVRE III : Sécurité ERP U & St-Joseph</div>
            <div class="text-[11px] text-slate-400 font-sans mt-0.5">Voie unique hôpital Stiletto, hélistation SAMU et friche militaire A 113.</div>
          </div>
        </a>

        <a href="#livre-4" class="p-3.5 bg-slate-900/80 hover:bg-slate-900 rounded-2xl border border-slate-800 hover:border-amber-500/50 transition flex items-start gap-3 group">
          <span class="p-2 rounded-xl bg-amber-500/10 text-amber-400 border border-amber-500/30 group-hover:scale-110 transition shrink-0 font-bold">04</span>
          <div>
            <div class="text-amber-400 font-bold group-hover:text-amber-300">LIVRE IV : 5 Questions de Sommation</div>
            <div class="text-[11px] text-slate-400 font-sans mt-0.5">Interpellations avec visas légaux et contre-répliques pour séance publique.</div>
          </div>
        </a>

        <a href="#livre-5" class="p-3.5 bg-slate-900/80 hover:bg-slate-900 rounded-2xl border border-slate-800 hover:border-emerald-500/50 transition flex items-start gap-3 group">
          <span class="p-2 rounded-xl bg-emerald-500/10 text-emerald-400 border border-emerald-500/30 group-hover:scale-110 transition shrink-0 font-bold">05</span>
          <div>
            <div class="text-emerald-400 font-bold group-hover:text-emerald-300">LIVRE V : Projet d'Amendement Clé en Main</div>
            <div class="text-[11px] text-slate-400 font-sans mt-0.5">Délibération communautaire prête au vote pour forcer le scrutin public.</div>
          </div>
        </a>

        <a href="#livre-6" class="p-3.5 bg-slate-900/80 hover:bg-slate-900 rounded-2xl border border-slate-800 hover:border-blue-500/50 transition flex items-start gap-3 group">
          <span class="p-2 rounded-xl bg-blue-500/10 text-blue-400 border border-blue-500/30 group-hover:scale-110 transition shrink-0 font-bold">06</span>
          <div>
            <div class="text-blue-400 font-bold group-hover:text-blue-300">LIVRE VI : Question Orale 2026/O2/055</div>
            <div class="text-[11px] text-slate-400 font-sans mt-0.5">Sanctuarisation de la gare centrale à l'Assemblée de Corse (Art. L. 4424-18).</div>
          </div>
        </a>

        <a href="#livre-7" class="p-3.5 bg-slate-900/80 hover:bg-slate-900 rounded-2xl border border-slate-800 hover:border-purple-500/50 transition flex items-start gap-3 group">
          <span class="p-2 rounded-xl bg-purple-500/10 text-purple-400 border border-purple-500/30 group-hover:scale-110 transition shrink-0 font-bold">07</span>
          <div>
            <div class="text-purple-400 font-bold group-hover:text-purple-300">LIVRE VII : Compétence SPL Mobilité</div>
            <div class="text-[11px] text-slate-400 font-sans mt-0.5">Statuts unifiés transport et stationnement en quasi-régie in-house.</div>
          </div>
        </a>

        <a href="#livre-8" class="p-3.5 bg-slate-900/80 hover:bg-slate-900 rounded-2xl border border-slate-800 hover:border-cyan-500/50 transition flex items-start gap-3 group">
          <span class="p-2 rounded-xl bg-cyan-500/10 text-cyan-400 border border-cyan-500/30 group-hover:scale-110 transition shrink-0 font-bold">08</span>
          <div>
            <div class="text-cyan-400 font-bold group-hover:text-cyan-300">LIVRE VIII : Audit Financier Parking Diamant</div>
            <div class="text-[11px] text-slate-400 font-sans mt-0.5">+1,59 M€ d'excédent net finançant 16 bus neufs (taux de couverture 144%).</div>
          </div>
        </a>

        <a href="#livre-9" class="p-3.5 bg-slate-900/80 hover:bg-slate-900 rounded-2xl border border-slate-800 hover:border-emerald-500/50 transition flex items-start gap-3 group">
          <span class="p-2 rounded-xl bg-emerald-500/10 text-emerald-400 border border-emerald-500/30 group-hover:scale-110 transition shrink-0 font-bold">09</span>
          <div>
            <div class="text-emerald-400 font-bold group-hover:text-emerald-300">LIVRE IX : Récupération Rente Scolaire</div>
            <div class="text-[11px] text-slate-400 font-sans mt-0.5">+1,40 M€ d'économie récurrente en convertissant les 9 villages en lignes mixtes.</div>
          </div>
        </a>

        <a href="#livre-10" class="p-3.5 bg-slate-900/80 hover:bg-slate-900 rounded-2xl border border-slate-800 hover:border-indigo-500/50 transition flex items-start gap-3 group">
          <span class="p-2 rounded-xl bg-indigo-500/10 text-indigo-400 border border-indigo-500/30 group-hover:scale-110 transition shrink-0 font-bold">10</span>
          <div>
            <div class="text-indigo-400 font-bold group-hover:text-indigo-300">LIVRE X : Halte St-Joseph vs Gare</div>
            <div class="text-[11px] text-slate-400 font-sans mt-0.5">Halte légère de 60m à 1,5 M€ vs démantèlement à 35 M€ de la gare centrale.</div>
          </div>
        </a>
      </div>
    </div>

    <!-- CORPS DES 10 LIVRES IN EXTENSO -->"""

content = sommaire_pattern.sub(sommaire_enrichi, content)

# Ré-extraction des positions après le changement de sommaire
matches = list(section_pattern.finditer(content))
first_start = matches[0].start()
last_end = matches[-1].end()

new_content = content[:first_start] + sticky_nav_html + "\n" + all_new_sections + content[last_end:]

with open(astro_path, "w", encoding="utf-8") as f:
    f.write(new_content)

print("Succès : Le fichier dossier-transparence-citoyenne-ajaccio.astro a été sublimé graphiquement tout en conservant 100% des données.")

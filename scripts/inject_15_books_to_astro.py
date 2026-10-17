# -*- coding: utf-8 -*-
"""
Intégration chirurgicale des 5 Nouveaux Livres (XI à XV) dans le dossier Astro :
1. Mise à jour du bandeau Smart HUD :
   - Select dropdown enrichi avec les 15 Livres.
   - 15 pastilles tactiles [01] à [15].
2. Mise à jour du Sommaire Analytique Général avec les 15 Livres.
3. Injection des 5 nouvelles sections enrichies avec HUD 3D, KPIs néon, takeaway citoyen et texte in extenso.
"""

import os
import re
import markdown

astro_path = r"C:\Users\PC-Bureau\Desktop\docucu\site_github_pages\src\pages\dossier-transparence-citoyenne-ajaccio.astro"
docs_dir = r"C:\Users\PC-Bureau\Desktop\docucu\site_github_pages\public\docs\opposition_ajaccio"

with open(astro_path, "r", encoding="utf-8") as f:
    text = f.read()

# Données des 5 nouveaux livres
NEW_LIVRES_DATA = [
    {
        "file": "11_FABRIQUE_SCANDALE_CABINETS_CONSEIL_MC18_022.md",
        "id": "livre-11",
        "num": "LIVRE XI",
        "title": "La Fabrique du Scandale : Cabinets de Conseil & Marché MC18/022",
        "badge": "Assistance à Maîtrise d'Ouvrage • 499 975 € HT",
        "border_color": "border-amber-500/40",
        "glow_color": "shadow-[0_0_30px_rgba(245,158,11,0.15)]",
        "summary": "Autopsie du trio de cabinets parisiens et alpins (E.R.I.C., Ingérop, Parme Avocats) mandaté pour 500 000 € afin de tailler le contrat CREM sur-mesure pour POMA et fabriquer la fable des '2 000 passagers/heure' et de 'l'évacuation des feux de forêt'.",
        "kpis": [
            {"val": "499 975 €", "label": "Marché MC18/022", "sub": "Facture AMO aux cabinets", "color": "text-amber-400 font-bold"},
            {"val": "< 25 km", "label": "Proximité E.R.I.C. / POMA", "sub": "Meylan vs Voreppe (Isère)", "color": "text-cyan-400 font-bold"},
            {"val": "2 000 / h", "label": "Faux Modèle de Trafic", "sub": "Fable Ingérop déconnectée", "color": "text-rose-400 font-bold"},
            {"val": "Parme Avocats", "label": "Verrouillage Juridique", "sub": "Architecture du CREM intouchable", "color": "text-purple-400 font-bold"}
        ],
        "takeaway": "L'exécutif a délégué la conception du projet à des bureaux d'études liés historiquement au constructeur POMA, payés 500 000 € pour justifier l'injustifiable."
    },
    {
        "file": "12_HOLD_UP_FISCAL_RESERVE_DECHETS_ET_IMPOTS.md",
        "id": "livre-12",
        "num": "LIVRE XII",
        "title": "Le Hold-Up Fiscal : Détournement de la Réserve Déchets & Hausse Fiscale (+7 M€)",
        "badge": "Cavalerie Budgétaire • ROB 2024-2026 • Taxe Foncière",
        "border_color": "border-red-500/40",
        "glow_color": "shadow-[0_0_30px_rgba(239,68,68,0.15)]",
        "summary": "Démonstration comptable irréfutable : pour payer la rente de 2,39 M€/an de POMA, la CAPA a vidé la réserve d'urgence de 1,5 M€ constituée lors de la crise des déchets, puis matraqué les propriétaires ajacciens avec +7 M€ de taxe foncière.",
        "kpis": [
            {"val": "1 500 000 €", "label": "Réserve Déchets Vidée", "sub": "Provision 2018 détournée (ROB 2025)", "color": "text-rose-400 font-bold"},
            {"val": "+ 7 000 000 €", "label": "Coup de Massue Fiscal", "sub": "Hausse taxe foncière CAPA", "color": "text-red-500 font-black"},
            {"val": "24 000 000 €", "label": "Coût Décennal POMA", "sub": "2,39 M€/an sur 10 ans", "color": "text-amber-400 font-bold"},
            {"val": "Zéro Réserve", "label": "Vulnérabilité Ordures", "sub": "Agglomération à poil en cas de crise", "color": "text-slate-300 font-bold"}
        ],
        "takeaway": "Chaque foyer ajaccien paie directement le téléphérique sur sa taxe foncière pendant que la collectivité s'est privée de son épargne de sécurité face aux crises sanitaires."
    },
    {
        "file": "13_OPERATION_IMMOBILIERE_MISERICORDE_AMETARRA.md",
        "id": "livre-13",
        "num": "LIVRE XIII",
        "title": "L'Opération Immobilière Miséricorde : 9 Hectares Vue Mer Livrés au Béton",
        "badge": "Renseignement Foncier • SPL Ametarra • Prêt BDT 10,2 M€",
        "border_color": "border-emerald-500/40",
        "glow_color": "shadow-[0_0_30px_rgba(16,185,129,0.15)]",
        "summary": "Le véritable mobile du déménagement de l'hôpital : libérer les 9 hectares d'or de l'avenue Eugénie face au golfe pour y bâtir 781 logements de standing via la SPL Ametarra (emprunt de 10,2 M€ BDT), au détriment de la sécurité des soins.",
        "kpis": [
            {"val": "9 Hectares", "label": "Tènement Miséricorde", "sub": "Section BW 45, 46, 48, 112", "color": "text-emerald-400 font-bold"},
            {"val": "781 Logements", "label": "Programme Immobilier", "sub": "Opération d'or face à la mer", "color": "text-cyan-400 font-bold"},
            {"val": "10 200 000 €", "label": "Prêt Caisse des Dépôts", "sub": "Avances remboursables BDT Ametarra", "color": "text-amber-400 font-bold"},
            {"val": "SPL Ametarra", "label": "Société Publique d'Aménagement", "sub": "SIREN 812 410 488 (Présidence Sbraggia)", "color": "text-purple-400 font-bold"}
        ],
        "takeaway": "L'hôpital n'a pas été déporté pour soigner mieux, mais pour transformer 9 hectares publics côtiers inestimables en opération de promotion immobilière."
    },
    {
        "file": "14_SABOTAGE_ROUTE_MONT_THABOR_ET_TORTUE_HERMANN.md",
        "id": "livre-14",
        "num": "LIVRE XIV",
        "title": "Le Sabotage du Mont Thabor : L'Alibi Écologique à Géométrie Variable",
        "badge": "Référé Sécurité Publique • Deux Poids Deux Mesures Régalien",
        "border_color": "border-red-500/40",
        "glow_color": "shadow-[0_0_30px_rgba(239,68,68,0.15)]",
        "summary": "La confrontation médico-légale : l'État a refusé 1,2 km de route de secours pour les urgences (4,5 M€) au nom de la Tortue d'Hermann, mais a signé un arrêté dérogatoire pour raser 4 hectares de maquis et implanter les pylônes de béton du téléphérique.",
        "kpis": [
            {"val": "1,2 km", "label": "Voie de Désenclavement", "sub": "Prolongement Avenue Mont Thabor", "color": "text-cyan-400 font-bold"},
            {"val": "4,5 M€ vs 52 M€", "label": "Rapport de Coût (x10)", "sub": "Route de secours vs Câble Angelo", "color": "text-emerald-400 font-bold"},
            {"val": "Refus Préfectoral", "label": "Veto Tortue d'Hermann", "sub": "Blocage de la voie pour les urgences", "color": "text-rose-400 font-bold"},
            {"val": "Arrêté 2023", "label": "Dérogation Intégrale Câble", "sub": "Bétonnage autorisé pour POMA", "color": "text-amber-400 font-bold"}
        ],
        "takeaway": "L'alibi environnemental a été instrumentalisé par l'État pour bloquer l'alternative routière de bon sens et forcer l'adoption du téléphérique."
    },
    {
        "file": "15_SACRIFICE_SOCIAL_ET_HUMAIN_BUS_MUVITARRA.md",
        "id": "livre-15",
        "num": "LIVRE XV",
        "title": "Le Naufrage Humain et Social : Le Sacrifice de la Muvitarra et des Usagers",
        "badge": "Audit Social & Matériel • Conditions de Travail & Flotte en Ruine",
        "border_color": "border-rose-500/40",
        "glow_color": "shadow-[0_0_30px_rgba(244,63,94,0.15)]",
        "summary": "Le calvaire quotidien des Ajacciens et des agents de la SPL : terminus du Diamant déporté dans la pente, flotte obsolète à 63 % (>10 ans et 550 000 km), pannes de climatisation à 42 °C et pressions managériales contre les conducteurs de bus.",
        "kpis": [
            {"val": "Terminus Déporté", "label": "Rupture Place du Diamant", "sub": "Suppression des arrêts commerçants", "color": "text-rose-400 font-bold"},
            {"val": "11,8 Ans", "label": "Âge Moyen des Bus", "sub": "26 bus sur 42 ont plus de 10 ans", "color": "text-red-400 font-bold"},
            {"val": "> 550 000 km", "label": "Kilométrage Flotte", "sub": "Véhicules au bord de la rupture", "color": "text-amber-400 font-bold"},
            {"val": "1,5 Bus / an", "label": "Rythme de Remplacement", "sub": "Pénurie et étouffement financier", "color": "text-slate-300 font-bold"}
        ],
        "takeaway": "La politique municipale a sciemment dégradé le service de bus et la santé au travail des chauffeurs pour dégager les flux au profit du projet de câble privé."
    }
]

# 1. Mise à jour du Smart HUD
# On remplace les options du select et les pastilles
old_select_part = """<select 
            id="book-selector"
            class="w-full md:w-auto px-3.5 py-1.5 rounded-xl bg-slate-900 border border-slate-700 hover:border-amber-500/60 text-slate-200 text-xs font-mono font-medium focus:outline-none focus:ring-2 focus:ring-amber-500/40 transition cursor-pointer"
            onchange="if(this.value) window.location.hash = this.value;"
          >
            <option value="">⚡ Aller directement au Livre...</option>
            <option value="livre-1">Livre I : Saisine CRC Corse (Moyens 1, 2, 3)</option>
            <option value="livre-2">Livre II : Disparité CREM POMA vs COSP Bus</option>
            <option value="livre-3">Livre III : Signalement Sécurité ERP Stiletto</option>
            <option value="livre-4">Livre IV : 5 Questions de Sommation CAPA</option>
            <option value="livre-5">Livre V : Délibération d'Amendement Clé en Main</option>
            <option value="livre-6">Livre VI : Question Orale Gare Centrale (CdC)</option>
            <option value="livre-7">Livre VII : Statuts & Compétence SPL Mobilité</option>
            <option value="livre-8">Livre VIII : Audit M4 Parking du Diamant (+1,59 M€)</option>
            <option value="livre-9">Livre IX : Récupération Rente Scolaire (+1,40 M€)</option>
            <option value="livre-10">Livre X : Halte St-Joseph vs Déménagement Gare</option>
            <option value="livre-11">Livre XI : La Fabrique du Scandale (Cabinets de Conseil)</option>
            <option value="livre-12">Livre XII : Le Hold-Up Fiscal (Poubelles & +7 M€ Taxe)</option>
            <option value="livre-13">Livre XIII : L'Opération Immobilière Miséricorde (9 ha)</option>
            <option value="livre-14">Livre XIV : Le Sabotage du Mont Thabor (Alibi Écolo)</option>
            <option value="livre-15">Livre XV : Le Sacrifice Social et Humain (Muvitarra)</option>
          </select>"""

# Pastilles tactiles 01 à 15
pastilles_html = """<div class="flex flex-wrap items-center gap-1.5 justify-center md:justify-end">
          <a href="#livre-1" title="Livre I : Saisine CRC Corse" class="w-7 h-7 rounded-lg bg-slate-900 hover:bg-amber-500/20 text-slate-300 hover:text-amber-400 border border-slate-800 hover:border-amber-500/50 flex items-center justify-center font-mono text-[11px] font-bold transition active:scale-95">01</a>
          <a href="#livre-2" title="Livre II : Disparité CREM/COSP" class="w-7 h-7 rounded-lg bg-slate-900 hover:bg-rose-500/20 text-slate-300 hover:text-rose-400 border border-slate-800 hover:border-rose-500/50 flex items-center justify-center font-mono text-[11px] font-bold transition active:scale-95">02</a>
          <a href="#livre-3" title="Livre III : Sécurité ERP U Stiletto" class="w-7 h-7 rounded-lg bg-slate-900 hover:bg-red-500/20 text-slate-300 hover:text-red-400 border border-slate-800 hover:border-red-500/50 flex items-center justify-center font-mono text-[11px] font-bold transition active:scale-95">03</a>
          <a href="#livre-4" title="Livre IV : 5 Questions de Sommation" class="w-7 h-7 rounded-lg bg-slate-900 hover:bg-amber-500/20 text-slate-300 hover:text-amber-400 border border-slate-800 hover:border-amber-500/50 flex items-center justify-center font-mono text-[11px] font-bold transition active:scale-95">04</a>
          <a href="#livre-5" title="Livre V : Délibération d'Amendement" class="w-7 h-7 rounded-lg bg-slate-900 hover:bg-emerald-500/20 text-slate-300 hover:text-emerald-400 border border-slate-800 hover:border-emerald-500/50 flex items-center justify-center font-mono text-[11px] font-bold transition active:scale-95">05</a>
          <a href="#livre-6" title="Livre VI : Gare Centrale Assemblée Corse" class="w-7 h-7 rounded-lg bg-slate-900 hover:bg-blue-500/20 text-slate-300 hover:text-blue-400 border border-slate-800 hover:border-blue-500/50 flex items-center justify-center font-mono text-[11px] font-bold transition active:scale-95">06</a>
          <a href="#livre-7" title="Livre VII : Compétence SPL Mobilité" class="w-7 h-7 rounded-lg bg-slate-900 hover:bg-purple-500/20 text-slate-300 hover:text-purple-400 border border-slate-800 hover:border-purple-500/50 flex items-center justify-center font-mono text-[11px] font-bold transition active:scale-95">07</a>
          <a href="#livre-8" title="Livre VIII : Audit M4 Parking Diamant" class="w-7 h-7 rounded-lg bg-slate-900 hover:bg-cyan-500/20 text-slate-300 hover:text-cyan-400 border border-slate-800 hover:border-cyan-500/50 flex items-center justify-center font-mono text-[11px] font-bold transition active:scale-95">08</a>
          <a href="#livre-9" title="Livre IX : Rente Scolaire 9 Villages" class="w-7 h-7 rounded-lg bg-slate-900 hover:bg-emerald-500/20 text-slate-300 hover:text-emerald-400 border border-slate-800 hover:border-emerald-500/50 flex items-center justify-center font-mono text-[11px] font-bold transition active:scale-95">09</a>
          <a href="#livre-10" title="Livre X : Halte St-Joseph vs Gare" class="w-7 h-7 rounded-lg bg-slate-900 hover:bg-indigo-500/20 text-slate-300 hover:text-indigo-400 border border-slate-800 hover:border-indigo-500/50 flex items-center justify-center font-mono text-[11px] font-bold transition active:scale-95">10</a>
          <a href="#livre-11" title="Livre XI : Cabinets de Conseil" class="w-7 h-7 rounded-lg bg-slate-900 hover:bg-amber-500/20 text-slate-300 hover:text-amber-400 border border-slate-800 hover:border-amber-500/50 flex items-center justify-center font-mono text-[11px] font-bold transition active:scale-95">11</a>
          <a href="#livre-12" title="Livre XII : Hold-Up Fiscal" class="w-7 h-7 rounded-lg bg-slate-900 hover:bg-red-500/20 text-slate-300 hover:text-red-400 border border-slate-800 hover:border-red-500/50 flex items-center justify-center font-mono text-[11px] font-bold transition active:scale-95">12</a>
          <a href="#livre-13" title="Livre XIII : Miséricorde 9 ha" class="w-7 h-7 rounded-lg bg-slate-900 hover:bg-emerald-500/20 text-slate-300 hover:text-emerald-400 border border-slate-800 hover:border-emerald-500/50 flex items-center justify-center font-mono text-[11px] font-bold transition active:scale-95">13</a>
          <a href="#livre-14" title="Livre XIV : Sabotage Mont Thabor" class="w-7 h-7 rounded-lg bg-slate-900 hover:bg-rose-500/20 text-slate-300 hover:text-rose-400 border border-slate-800 hover:border-rose-500/50 flex items-center justify-center font-mono text-[11px] font-bold transition active:scale-95">14</a>
          <a href="#livre-15" title="Livre XV : Sacrifice Muvitarra" class="w-7 h-7 rounded-lg bg-slate-900 hover:bg-purple-500/20 text-slate-300 hover:text-purple-400 border border-slate-800 hover:border-purple-500/50 flex items-center justify-center font-mono text-[11px] font-bold transition active:scale-95">15</a>
          
          <button 
            id="toggle-all-details-btn"
            class="ml-1 px-3 py-1.5 rounded-lg bg-amber-500/10 hover:bg-amber-500/20 text-amber-400 border border-amber-500/30 text-xs font-mono font-bold transition flex items-center gap-1.5 active:scale-95 cursor-pointer shrink-0"
            onclick="
              const details = document.querySelectorAll('details');
              const isAnyOpen = Array.from(details).some(d => d.open);
              details.forEach(d => d.open = !isAnyOpen);
              this.textContent = isAnyOpen ? '📖 Déplier Tous les Textes' : '📕 Replier Tous les Textes';
            "
          >
            📕 Replier Tout
          </button>
        </div>"""

# Remplacement du select et des pastilles dans le Smart HUD
smart_hud_pattern = re.compile(r'<select\s+id="book-selector".*?</select>', re.DOTALL)
text = smart_hud_pattern.sub(old_select_part, text)

pastilles_pattern = re.compile(r'<div class="flex flex-wrap items-center gap-1\.5 justify-center md:justify-end">.*?</div>', re.DOTALL)
text = pastilles_pattern.sub(pastilles_html, text)

# Modification du badge "10 LIVRES SCELLÉS" en "15 LIVRES SCELLÉS"
text = text.replace("10 LIVRES SCELLÉS", "15 LIVRES SCELLÉS")
text = text.replace("(10 LIVRES IN EXTENSO)", "(15 LIVRES D'INSTRUCTION SCELLÉS)")

# 2. Ajout des 5 nouvelles cartes dans le Sommaire Analytique
extra_sommaire_cards = """
        <a href="#livre-11" class="p-3.5 bg-slate-900/80 hover:bg-slate-900 rounded-2xl border border-slate-800 hover:border-amber-500/50 transition flex items-start gap-3 group">
          <span class="p-2 rounded-xl bg-amber-500/10 text-amber-400 border border-amber-500/30 group-hover:scale-110 transition shrink-0 font-bold">11</span>
          <div>
            <div class="text-amber-400 font-bold group-hover:text-amber-300">LIVRE XI : La Fabrique du Scandale</div>
            <div class="text-[11px] text-slate-400 font-sans mt-0.5">Marché AMO MC18/022 (500 k€), E.R.I.C., Ingérop et Parme Avocats.</div>
          </div>
        </a>

        <a href="#livre-12" class="p-3.5 bg-slate-900/80 hover:bg-slate-900 rounded-2xl border border-slate-800 hover:border-red-500/50 transition flex items-start gap-3 group">
          <span class="p-2 rounded-xl bg-red-500/10 text-red-400 border border-red-500/30 group-hover:scale-110 transition shrink-0 font-bold">12</span>
          <div>
            <div class="text-red-400 font-bold group-hover:text-red-300">LIVRE XII : Le Hold-Up Fiscal</div>
            <div class="text-[11px] text-slate-400 font-sans mt-0.5">Détournement de la réserve déchets (1,5 M€) et hausse taxe foncière (+7 M€).</div>
          </div>
        </a>

        <a href="#livre-13" class="p-3.5 bg-slate-900/80 hover:bg-slate-900 rounded-2xl border border-slate-800 hover:border-emerald-500/50 transition flex items-start gap-3 group">
          <span class="p-2 rounded-xl bg-emerald-500/10 text-emerald-400 border border-emerald-500/30 group-hover:scale-110 transition shrink-0 font-bold">13</span>
          <div>
            <div class="text-emerald-400 font-bold group-hover:text-emerald-300">LIVRE XIII : L'Opération Miséricorde</div>
            <div class="text-[11px] text-slate-400 font-sans mt-0.5">9 hectares d'or face à la mer, 781 logements et emprunt BDT 10,2 M€.</div>
          </div>
        </a>

        <a href="#livre-14" class="p-3.5 bg-slate-900/80 hover:bg-slate-900 rounded-2xl border border-slate-800 hover:border-rose-500/50 transition flex items-start gap-3 group">
          <span class="p-2 rounded-xl bg-rose-500/10 text-rose-400 border border-rose-500/30 group-hover:scale-110 transition shrink-0 font-bold">14</span>
          <div>
            <div class="text-rose-400 font-bold group-hover:text-rose-300">LIVRE XIV : Le Sabotage du Mont Thabor</div>
            <div class="text-[11px] text-slate-400 font-sans mt-0.5">Voie de secours bloquée pour la Tortue d'Hermann vs 4 ha rasés pour le câble.</div>
          </div>
        </a>

        <a href="#livre-15" class="p-3.5 bg-slate-900/80 hover:bg-slate-900 rounded-2xl border border-slate-800 hover:border-purple-500/50 transition flex items-start gap-3 group">
          <span class="p-2 rounded-xl bg-purple-500/10 text-purple-400 border border-purple-500/30 group-hover:scale-110 transition shrink-0 font-bold">15</span>
          <div>
            <div class="text-purple-400 font-bold group-hover:text-purple-300">LIVRE XV : Le Sacrifice de la Muvitarra</div>
            <div class="text-[11px] text-slate-400 font-sans mt-0.5">Terminus du Diamant déporté, flotte obsolète à 63 % et calvaire des usagers.</div>
          </div>
        </a>
      </div>
    </div>"""

# Remplacement de la balise de fermeture du sommaire
text = text.replace("</div>\n    </div>\n\n    <!-- CORPS DES 10 LIVRES IN EXTENSO -->", extra_sommaire_cards + "\n\n    <!-- CORPS DES 15 LIVRES IN EXTENSO -->")

# 3. Génération des 5 nouvelles sections HTML pour le corps de la page
new_sections_html = []
for l in NEW_LIVRES_DATA:
    md_file_path = os.path.join(docs_dir, l["file"])
    with open(md_file_path, "r", encoding="utf-8") as mf:
        md_content = mf.read()
    
    html_body = markdown.markdown(md_content, extensions=['tables', 'fenced_code'])
    base_html = l["file"].replace(".md", ".html")
    
    kpi_cards = ""
    for k in l["kpis"]:
        kpi_cards += f"""
              <div class="p-3.5 rounded-2xl bg-slate-950/80 border border-slate-800/80 shadow-inner flex flex-col justify-between">
                <div class="text-[10px] font-mono uppercase tracking-wider text-slate-400 mb-1">{k['label']}</div>
                <div class="text-xl md:text-2xl font-mono font-bold {k['color']} tracking-tight">{k['val']}</div>
                <div class="text-[11px] font-sans text-slate-400 mt-1">{k['sub']}</div>
              </div>
        """

    section_code = f"""
        <!-- {l['file']} -->
        <section id="{l['id']}" class="scroll-mt-20 p-6 md:p-10 rounded-3xl bg-slate-900/90 border {l['border_color']} {l['glow_color']} shadow-2xl space-y-6 transition-all duration-300">
          
          <!-- BANDEAU SUPÉRIEUR HUD DE NIVEAU MAGISTRATURE -->
          <div class="flex flex-wrap items-center justify-between gap-3 border-b border-slate-800 pb-5">
            <div class="flex flex-wrap items-center gap-2">
              <span class="px-3.5 py-1 bg-amber-500/10 text-amber-400 border border-amber-500/30 rounded-full text-xs font-mono font-bold uppercase tracking-wider">
                {l['num']} • {l['badge']}
              </span>
            </div>
            <div class="flex items-center gap-2">
              <a href="/docs/opposition_ajaccio/{base_html}" target="_blank" class="text-xs font-mono bg-slate-800 hover:bg-slate-700 text-cyan-300 px-3 py-1.5 rounded-lg border border-slate-700 transition shadow flex items-center gap-1.5">
                <span>🌐</span> Ouvrir Plein Écran
              </a>
            </div>
          </div>

          <!-- TITRE DU LIVRE ET SYNTHÈSE GRAPHIQUE DIRECTE -->
          <div class="space-y-4">
            <h2 class="text-2xl md:text-3xl font-black font-serif text-white tracking-tight">
              {l['title']}
            </h2>
            <p class="text-sm font-sans text-slate-300 leading-relaxed border-l-2 border-amber-400/60 pl-4 py-0.5 bg-slate-950/40 rounded-r-xl">
              {l['summary']}
            </p>
          </div>

          <!-- GRILLE DES 4 INDICATEURS CHOCS (KPIS VISUELS) -->
          <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-3">
            {kpi_cards}
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
                {l['takeaway']}
              </div>
            </div>
          </div>

          <!-- CONTENEUR ACCORDÉON FORENSIQUE : LE TEXTE INTÉGRAL IN EXTENSO -->
          <details open class="group rounded-2xl bg-slate-950/70 border border-slate-800/90 overflow-hidden transition-all duration-300">
            <summary class="px-5 py-3.5 cursor-pointer flex items-center justify-between text-xs font-mono uppercase tracking-wider text-slate-300 hover:text-white bg-slate-900/60 hover:bg-slate-900 transition select-none">
              <span class="flex items-center gap-2 font-bold text-amber-400">
                <span>📖</span> TEXTE INTÉGRAL D'INSTRUCTION IN EXTENSO (ENQUÊTES SCELLÉES & PIÈCES CONTRÔLÉES)
              </span>
              <span class="text-slate-500 group-open:rotate-180 transition-transform duration-200">
                ▼
              </span>
            </summary>
            
            <div class="p-6 md:p-8 border-t border-slate-800/80">
              <div class="prose prose-invert prose-amber max-w-none text-slate-300 text-sm leading-relaxed font-sans space-y-4">
                {html_body}
              </div>
            </div>
          </details>

        </section>
    """
    new_sections_html.append(section_code)

# Injection avant la balise de fermeture de <div class="space-y-12"> (qui contient les livres)
# Trouvons la fin de la section 10
sec10_marker = "<!-- 10_ETUDE_TECHNIQUE_HALTE_FERROVIAIRE_SAINT_JOSEPH_VS_DEMENAGEMENT.md -->"
sec10_idx = text.find(sec10_marker)
if sec10_idx == -1:
    print("Erreur : Impossible de localiser la section 10.")
    exit(1)

# On trouve la fin du </section> de la section 10
sec10_end = text.find("</section>", sec10_idx) + len("</section>")

all_injected_sections = "\n\n" + "\n".join(new_sections_html)

text = text[:sec10_end] + all_injected_sections + text[sec10_end:]

with open(astro_path, "w", encoding="utf-8") as f:
    f.write(text)

print("Succès : Les 15 Livres complets sont désormais fusionnés dans le dossier secret Transparence Citoyenne !")

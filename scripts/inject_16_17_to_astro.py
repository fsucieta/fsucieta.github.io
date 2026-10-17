# -*- coding: utf-8 -*-
"""
Intégration chirurgicale des Livres XVI et XVII dans dossier-transparence-citoyenne-ajaccio.astro :
- Mise à jour du Smart HUD : Select avec 17 Livres + 17 pastilles [01] à [17].
- Mise à jour du Sommaire Analytique Général avec 17 Livres.
- Injection des 2 nouvelles sections avec HUD 3D, KPIs néon, tableau de l'Article 30.1 et takeaway citoyen.
"""

import os
import re
import markdown

astro_path = r"C:\Users\PC-Bureau\Desktop\docucu\site_github_pages\src\pages\dossier-transparence-citoyenne-ajaccio.astro"
docs_dir = r"C:\Users\PC-Bureau\Desktop\docucu\site_github_pages\public\docs\opposition_ajaccio"

with open(astro_path, "r", encoding="utf-8") as f:
    text = f.read()

LIVRES_16_17 = [
    {
        "file": "16_AUTOPSIE_FINANCIERE_MUVITARRA_IMPAYES_ET_ART30.md",
        "id": "livre-16",
        "num": "LIVRE XVI",
        "title": "Autopsie Financière de la Muvitarra : L'Aveu d'1,4 M€ d'Impayés & Le Faux Plan Annexe 9",
        "badge": "Audit de Trésorerie • Mise en Demeure DREAL • Art. 30.1 COSP",
        "border_color": "border-rose-500/50",
        "glow_color": "shadow-[0_0_35px_rgba(244,63,94,0.2)]",
        "summary": "Les pièces financières accablantes : l'aveu de la CAPA qui a dû verser 1,4 M€ de rattrapage d'arriérés pour des lignes commandées non payées, le plafond rigide de l'Article 30.1 (706 k€) et la démonstration mathématique de l'Annexe 9 (1,5 bus acheté par an, 25 ans pour rénover le parc sans bon de commande).",
        "kpis": [
            {"val": "1 400 000 €", "label": "Aveu d'Impayés CAPA", "sub": "Rattrapage rétroactif déc. 2025", "color": "text-rose-400 font-bold"},
            {"val": "- 766 132 €", "label": "Capitaux Propres SPL", "sub": "Mise en demeure DREAL 2023", "color": "text-red-500 font-black"},
            {"val": "706 530 €", "label": "Plafond Art. 30.1", "sub": "Forfait inflation bridé à l'année", "color": "text-amber-400 font-bold"},
            {"val": "25 Ans", "label": "Mirage Annexe 9", "sub": "1 M€/an = 1,5 bus/an pour 42 bus", "color": "text-purple-400 font-bold"}
        ],
        "takeaway": "La CAPA a elle-même fabriqué le déficit de la régie de bus en bloquant ses paiements, tout en prétendant dans les médias que la Muvitarra était mal gérée."
    },
    {
        "file": "17_EVASION_BUDGETAIRE_NAVETTE_PORTICCIO_ET_ANNEXE16.md",
        "id": "livre-17",
        "num": "LIVRE XVII",
        "title": "L'Évasion Budgétaire Hors Périmètre : Navette Porticcio (ROB p.17) & Mandat Gratuit Annexe 16",
        "badge": "Illégalité Budgétaire • Incompétence Territoriale • Libéralité Prohibée",
        "border_color": "border-cyan-500/40",
        "glow_color": "shadow-[0_0_30px_rgba(6,182,212,0.15)]",
        "summary": "L'aveu du ROB 2024 (page 17) : l'argent du Versement Mobilité et les impôts des Ajacciens siphonnés en subvention d'équilibre pour payer la navette maritime de Porticcio (autre intercommunalité CCPOT), combiné aux 5 servitudes gratuites imposées aux agents par l'Annexe 16 pour POMA.",
        "kpis": [
            {"val": "ROB 2024 p.17", "label": "Aveu Budgétaire Écrit", "sub": "Subvention d'équilibre Porticcio", "color": "text-cyan-400 font-bold"},
            {"val": "Hors CAPA", "label": "Grosseto-Prugna / CCPOT", "sub": "Financement illégal hors périmètre", "color": "text-rose-400 font-bold"},
            {"val": "5 Servitudes", "label": "Mandat Annexe 16", "sub": "Guichets, DAT, CB, SAV et Justice", "color": "text-amber-400 font-bold"},
            {"val": "0 € Reversé", "label": "Libéralité Prohibée", "sub": "Violation arrêt Commune de Fougerolles", "color": "text-emerald-400 font-bold"}
        ],
        "takeaway": "Les Ajacciens financent à perte la navette maritime d'une autre communauté de communes pendant que leurs agents de bus travaillent gratuitement pour le téléphérique privé."
    }
]

# 1. Mise à jour du Smart HUD (Dropdown + pastilles 01 à 17)
text = text.replace("15 LIVRES SCELLÉS", "17 LIVRES SCELLÉS")
text = text.replace("15 LIVRES D'INSTRUCTION SCELLÉS", "17 LIVRES D'INSTRUCTION FORENSIQUES SCELLÉS")

old_hud_select_end = """<option value="livre-15">Livre XV : Le Sacrifice Social et Humain (Muvitarra)</option>"""
new_hud_select_end = """<option value="livre-15">Livre XV : Le Sacrifice Social et Humain (Muvitarra)</option>
            <option value="livre-16">Livre XVI : Autopsie Financière Muvitarra (1,4 M€ Impayés & Art. 30.1)</option>
            <option value="livre-17">Livre XVII : Navette Porticcio (ROB p.17) & Servitudes Annexe 16</option>"""
text = text.replace(old_hud_select_end, new_hud_select_end)

old_pastilles_end = """<a href="#livre-15" title="Livre XV : Sacrifice Muvitarra" class="w-7 h-7 rounded-lg bg-slate-900 hover:bg-purple-500/20 text-slate-300 hover:text-purple-400 border border-slate-800 hover:border-purple-500/50 flex items-center justify-center font-mono text-[11px] font-bold transition active:scale-95">15</a>"""
new_pastilles_end = """<a href="#livre-15" title="Livre XV : Sacrifice Muvitarra" class="w-7 h-7 rounded-lg bg-slate-900 hover:bg-purple-500/20 text-slate-300 hover:text-purple-400 border border-slate-800 hover:border-purple-500/50 flex items-center justify-center font-mono text-[11px] font-bold transition active:scale-95">15</a>
          <a href="#livre-16" title="Livre XVI : Impayés 1,4 M€ & Art. 30.1" class="w-7 h-7 rounded-lg bg-slate-900 hover:bg-rose-500/20 text-slate-300 hover:text-rose-400 border border-slate-800 hover:border-rose-500/50 flex items-center justify-center font-mono text-[11px] font-bold transition active:scale-95">16</a>
          <a href="#livre-17" title="Livre XVII : Navette Porticcio & Annexe 16" class="w-7 h-7 rounded-lg bg-slate-900 hover:bg-cyan-500/20 text-slate-300 hover:text-cyan-400 border border-slate-800 hover:border-cyan-500/50 flex items-center justify-center font-mono text-[11px] font-bold transition active:scale-95">17</a>"""
text = text.replace(old_pastilles_end, new_pastilles_end)

# 2. Ajout dans le Sommaire Analytique
extra_sommaire_16_17 = """
        <a href="#livre-16" class="p-3.5 bg-slate-900/80 hover:bg-slate-900 rounded-2xl border border-slate-800 hover:border-rose-500/50 transition flex items-start gap-3 group">
          <span class="p-2 rounded-xl bg-rose-500/10 text-rose-400 border border-rose-500/30 group-hover:scale-110 transition shrink-0 font-bold">16</span>
          <div>
            <div class="text-rose-400 font-bold group-hover:text-rose-300">LIVRE XVI : Autopsie Financière Muvitarra</div>
            <div class="text-[11px] text-slate-400 font-sans mt-0.5">1,4 M€ d'arriérés impayés par la CAPA, plafond Art. 30.1 et mirage des 25 ans (Annexe 9).</div>
          </div>
        </a>

        <a href="#livre-17" class="p-3.5 bg-slate-900/80 hover:bg-slate-900 rounded-2xl border border-slate-800 hover:border-cyan-500/50 transition flex items-start gap-3 group">
          <span class="p-2 rounded-xl bg-cyan-500/10 text-cyan-400 border border-cyan-500/30 group-hover:scale-110 transition shrink-0 font-bold">17</span>
          <div>
            <div class="text-cyan-400 font-bold group-hover:text-cyan-300">LIVRE XVII : Navette Porticcio & Annexe 16</div>
            <div class="text-[11px] text-slate-400 font-sans mt-0.5">Aveu du ROB 2024 p.17 (financement hors périmètre CCPOT) et les 5 servitudes gratuites.</div>
          </div>
        </a>
      </div>
    </div>"""

text = text.replace("LIVRE XV : Le Sacrifice de la Muvitarra</div>\n            <div class=\"text-[11px] text-slate-400 font-sans mt-0.5\">Terminus du Diamant déporté, flotte obsolète à 63 % et calvaire des usagers.</div>\n          </div>\n        </a>\n      </div>\n    </div>", "LIVRE XV : Le Sacrifice de la Muvitarra</div>\n            <div class=\"text-[11px] text-slate-400 font-sans mt-0.5\">Terminus du Diamant déporté, flotte obsolète à 63 % et calvaire des usagers.</div>\n          </div>\n        </a>" + extra_sommaire_16_17)

# 3. Génération des 2 sections HTML enrichies
new_sections_html = []
for l in LIVRES_16_17:
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
                <span>📖</span> TEXTE INTÉGRAL D'INSTRUCTION IN EXTENSO (DÉPÔT DE PREUVES & VISAS LÉGAUX)
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

# Injection après la section 15
sec15_marker = "<!-- 15_SACRIFICE_SOCIAL_ET_HUMAIN_BUS_MUVITARRA.md -->"
sec15_idx = text.find(sec15_marker)
sec15_end = text.find("</section>", sec15_idx) + len("</section>")

text = text[:sec15_end] + "\n\n" + "\n".join(new_sections_html) + text[sec15_end:]

with open(astro_path, "w", encoding="utf-8") as f:
    f.write(text)

print("Succès : Les Livres XVI et XVII ont été intégrés dans le template Astro !")

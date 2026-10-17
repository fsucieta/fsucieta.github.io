import json

with open('public/docs/pieces-publiques-sante/INVENTAIRE_60_SOURCES_PRIMAIRES_ETAT.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

html_out = """
        <!-- HEADER DE L'ONGLET 7 -->
        <div class="p-6 rounded-2xl bg-slate-950 border border-cyan-500/40 space-y-4">
          <div class="flex flex-wrap items-center justify-between gap-3 border-b border-slate-900 pb-3">
            <div class="flex items-center gap-2">
              <span class="w-3 h-3 rounded-full bg-cyan-400 animate-ping"></span>
              <h3 class="text-xl font-bold font-serif text-white uppercase">
                Grand Bordereau Forensique : 60 Pièces d'État, Arrêtés ARS & Registres Légaux Scellés
              </h3>
            </div>
            <span class="text-xs font-mono px-3 py-1 bg-cyan-500/10 text-cyan-400 border border-cyan-500/30 rounded-full font-bold">
              60 SOURCES PRIMAIRES SCELLÉES ISO/IEC 27037
            </span>
          </div>
          <p class="text-xs md:text-sm text-slate-300 font-sans leading-relaxed">
            Conformément à la doctrine de <strong>L'OCHJU</strong>, chaque chiffre, chaque ratio et chaque chef de préjudice de cette enquête tentaculaire repose sur des <strong>documents d'État souverains et opposables</strong> (Journal Officiel de la République Française, rapports d'observations de la Cour des comptes et de la CRC Corse, marchés publics BOAMP, micro-données DREES et bases nationales SNDS). En application de l'<strong>article 35 de la loi du 29 juillet 1881</strong>, ce corpus confère l'<strong>Exception de Vérité</strong> absolue.
          </p>
          <div class="flex flex-wrap gap-2 pt-1 font-mono text-[11px]">
            <span class="text-slate-400 font-bold self-center">FILTRES RAPIDES :</span>
            <button class="src-filter-btn px-2.5 py-1 rounded-lg bg-cyan-500 text-slate-950 font-bold cursor-pointer transition" data-filter="ALL">TOUT AFFICHER (60)</button>
            <button class="src-filter-btn px-2.5 py-1 rounded-lg bg-slate-900 hover:bg-slate-800 text-cyan-400 border border-slate-800 cursor-pointer transition" data-filter="ARS & TUTELLES">ARS & TUTELLES (12)</button>
            <button class="src-filter-btn px-2.5 py-1 rounded-lg bg-slate-900 hover:bg-slate-800 text-cyan-400 border border-slate-800 cursor-pointer transition" data-filter="MARCHÉS & EVASAN">MARCHÉS & DSP (9)</button>
            <button class="src-filter-btn px-2.5 py-1 rounded-lg bg-slate-900 hover:bg-slate-800 text-cyan-400 border border-slate-800 cursor-pointer transition" data-filter="JURIDICTIONS FINANCIÈRES">COUR DES COMPTES & CRC (7)</button>
            <button class="src-filter-btn px-2.5 py-1 rounded-lg bg-slate-900 hover:bg-slate-800 text-cyan-400 border border-slate-800 cursor-pointer transition" data-filter="MICRO-DONNÉES BRUTES">DREES & BASES SNDS (8)</button>
            <button class="src-filter-btn px-2.5 py-1 rounded-lg bg-slate-900 hover:bg-slate-800 text-cyan-400 border border-slate-800 cursor-pointer transition" data-filter="ÉPIDÉMIOLOGIE & ENVIRONNEMENT">TCHERNOBYL & AMIANTE (10)</button>
            <button class="src-filter-btn px-2.5 py-1 rounded-lg bg-slate-900 hover:bg-slate-800 text-cyan-400 border border-slate-800 cursor-pointer transition" data-filter="JUSTICE & CONTENTIEUX">JUSTICE & CODES (8)</button>
            <button class="src-filter-btn px-2.5 py-1 rounded-lg bg-slate-900 hover:bg-slate-800 text-cyan-400 border border-slate-800 cursor-pointer transition" data-filter="GÉNOMIQUE & RECHERCHE">BIO-EXTRACTION & ADN (6)</button>
          </div>
        </div>

        <!-- GRILLE COMPLÈTE DES 60 SOURCES PRIMAIRES -->
        <div id="sources-grid" class="grid grid-cols-1 md:grid-cols-2 gap-4 text-xs font-sans">
"""

for it in items:
    html_out += f"""
          <!-- {it['id']} -->
          <div class="source-item p-4 rounded-2xl bg-slate-950 border border-slate-800 hover:border-cyan-500/50 transition flex flex-col justify-between space-y-2.5" data-cat="{it['cat']}">
            <div>
              <div class="flex justify-between items-center font-mono text-[10px] mb-1">
                <span class="text-cyan-400 font-bold">{it['id']} • {it['cat']}</span>
                <span class="text-slate-500 font-mono">{it['ref']}</span>
              </div>
              <h4 class="text-sm font-bold text-white font-serif">{it['title']}</h4>
              <p class="text-xs text-slate-300 leading-relaxed mt-1">
                {it['desc']}
              </p>
            </div>
            <div class="pt-2 border-t border-slate-900 font-mono text-[10px] text-amber-300/90 flex flex-col space-y-0.5">
              <div class="text-slate-400"><strong class="text-amber-400">Portée probatoire :</strong> {it['impact']}</div>
            </div>
          </div>
"""

html_out += """
        </div>
"""

with open('public/docs/pieces-publiques-sante/tab7_content.html', 'w', encoding='utf-8') as f:
    f.write(html_out)

print("tab7_content.html généré avec succès.")

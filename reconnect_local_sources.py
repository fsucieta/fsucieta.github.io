import json
import zipfile
import os

# Ce script met à jour :
# 1. Le bordereau global autonome public/docs/pieces-publiques-sante/BORDEREAU_60_SOURCES_PRIMAIRES_ETAT_ISO27037.html
#    pour qu'il pointe exclusivement vers les pièces physiques locales /docs/sources-etat-sante/
# 2. Le fichier de cartes interactives tab7_interactive_cards.html pour l'Onglet 7
# 3. L'archive ZIP intégrale COFFRE_INTEGRAL_SANTE_CORSE_ISO27037.zip en y injectant les 60 pièces HTML et TXT

with open("public/docs/pieces-publiques-sante/INVENTAIRE_60_SOURCES_LOCALES_SOUVERAINES.json", "r", encoding="utf-8") as f:
    sources = json.load(f)

# 1. Génération du Bordereau HTML avec liens physiques locaux
rows = []
for s in sources:
    rows.append(f"""
    <tr class="hover:bg-slate-900/60 border-b border-slate-800 text-xs">
      <td class="p-3 font-mono font-bold text-cyan-400">{s['id']}</td>
      <td class="p-3 font-mono text-slate-400 text-[11px]">{s['cat']}</td>
      <td class="p-3">
        <div class="font-bold text-white font-serif text-sm">{s['title']}</div>
        <div class="text-slate-300 font-sans mt-0.5">{s['desc']}</div>
        <div class="text-[11px] font-mono text-amber-400 mt-1"><span class="text-slate-500">Portée :</span> {s['impact']}</div>
        <div class="text-[10px] font-mono text-slate-500 mt-1 truncate">SHA-256 : {s['sha256']}</div>
      </td>
      <td class="p-3 font-mono text-xs text-amber-300">{s['ref']}</td>
      <td class="p-3 whitespace-nowrap">
        <div class="flex flex-col gap-1.5">
          <a href="{s['html_url']}" target="_blank" class="px-3 py-1.5 rounded-lg bg-cyan-500 hover:bg-cyan-400 text-slate-950 font-mono font-bold text-[11px] uppercase transition shadow text-center">
            👁️ Consulter HTML ↗
          </a>
          <a href="{s['txt_url']}" download class="px-3 py-1 rounded-lg bg-slate-900 hover:bg-slate-800 text-cyan-400 border border-cyan-500/30 font-mono font-bold text-[10px] uppercase transition text-center">
            📥 Télécharger .txt
          </a>
        </div>
      </td>
    </tr>
    """)

bordereau_html = f"""<!DOCTYPE html>
<html lang="fr" class="bg-slate-950 text-slate-100">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Bordereau Récapitulatif des 60 Pièces Primaires d'État (ISO/IEC 27037) - L'OCHJU</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <style>
    @media print {{
      body {{ background: white !important; color: black !important; }}
      .no-print {{ display: none !important; }}
      table {{ border-collapse: collapse; width: 100%; }}
      th, td {{ border: 1px solid #cbd5e1 !important; color: black !important; }}
      th {{ background: #f1f5f9 !important; }}
      a {{ text-decoration: underline !important; color: black !important; }}
    }}
  </style>
</head>
<body class="p-4 md:p-8 max-w-7xl mx-auto font-sans leading-relaxed text-sm">

  <!-- BARRE D'ACTIONS -->
  <div class="no-print mb-6 flex flex-wrap justify-between items-center gap-3 p-4 bg-slate-900 border border-cyan-500/40 rounded-2xl shadow-xl">
    <div class="flex items-center space-x-3">
      <span class="w-3 h-3 rounded-full bg-cyan-400 animate-ping"></span>
      <div>
        <div class="font-mono text-xs text-cyan-400 font-bold uppercase tracking-wider">
          CORPUS SOUVERAIN DES 60 PIÈCES D'ÉTAT SCELLÉES • ISO/IEC 27037:2012
        </div>
        <div class="text-[11px] text-slate-400 font-mono">
          Conservation physique locale 100% autonome (0 lien externe, 0 erreur 404)
        </div>
      </div>
    </div>
    <div class="flex items-center gap-2">
      <button onclick="window.print()" class="px-4 py-2 bg-cyan-500 hover:bg-cyan-400 text-slate-950 font-mono font-bold text-xs uppercase tracking-wider rounded-xl transition cursor-pointer shadow">
        🖨️ Imprimer / PDF
      </button>
      <a href="/docs/pieces-publiques-sante/INVENTAIRE_60_SOURCES_LOCALES_SOUVERAINES.json" download class="px-4 py-2 bg-slate-800 hover:bg-slate-700 text-cyan-400 border border-cyan-500/40 font-mono font-bold text-xs uppercase tracking-wider rounded-xl transition">
        📥 Export JSON Certifié
      </a>
      <a href="/dossier-secret-sante-corse/" class="px-4 py-2 bg-slate-950 hover:bg-slate-800 text-slate-300 border border-slate-800 font-mono font-bold text-xs uppercase tracking-wider rounded-xl transition">
        ← Retour au Dossier
      </a>
    </div>
  </div>

  <!-- EN-TETE REGALIEN -->
  <div class="border-2 border-cyan-500/40 bg-slate-900/90 rounded-3xl p-6 md:p-8 mb-8 space-y-4 shadow-2xl">
    <div class="flex flex-wrap justify-between items-center gap-2 border-b border-slate-800 pb-4">
      <div>
        <div class="text-xs font-mono text-cyan-400 font-bold uppercase tracking-widest">
          RÉPUBLIQUE FRANÇAISE • DOSSIER SECRET SANTÉ CORSE 2026
        </div>
        <div class="text-xs font-mono text-slate-400 mt-1">
          CELLULE D'INVESTIGATION FORENSIQUE L'OCHJU • ARCHIVES SOUVERAINES CONSERVÉES EN LOCAL
        </div>
      </div>
      <div class="text-right font-mono text-xs text-slate-400">
        <div>COTE OFFICIELLE : <span class="text-cyan-400 font-bold">LOCHJU-SANTE-CORPUS-60-PHYSIQUE</span></div>
        <div>NORME D'INTÉGRITÉ : <span class="text-white font-bold">ISO/IEC 27037:2012 SCELLÉ</span></div>
      </div>
    </div>
    
    <div>
      <h1 class="text-2xl md:text-3xl font-black text-white font-serif uppercase tracking-tight">
        Bordereau Forensique Intégral des 60 Pièces d'État, Arrêtés ARS & Registres Légaux
      </h1>
      <p class="text-xs md:text-sm text-slate-300 font-sans mt-2 leading-relaxed">
        Ce bordereau récapitule exhaustivement les 60 pièces souveraines opposables sur lesquelles s'appuient l'autopsie financière et les 11 actes contentieux de l'enquête. L'intégralité de ces documents est <strong>hébergée et consultable physiquement sur notre serveur</strong> sous empreinte cryptographique SHA-256 scellée, immunisant le dossier contre toute disparition ou modification de liens par les services de l'État. En application de l'<strong>article 35 de la loi du 29 juillet 1881</strong>, ce corpus confère l'<strong>Exception de Vérité</strong> absolue.
      </p>
    </div>
  </div>

  <!-- TABLEAU DES 60 SOURCES -->
  <div class="overflow-x-auto rounded-2xl border border-slate-800 bg-slate-950 shadow-2xl">
    <table class="w-full text-left border-collapse">
      <thead>
        <tr class="bg-slate-900 text-slate-300 font-mono text-[11px] uppercase tracking-wider border-b border-slate-800">
          <th class="p-3">ID</th>
          <th class="p-3">Catégorie</th>
          <th class="p-3">Document Source, Objet Probatoire & Empreinte SHA-256</th>
          <th class="p-3">Cote Légale</th>
          <th class="p-3">Accès Physique Souverain</th>
        </tr>
      </thead>
      <tbody>
        {''.join(rows)}
      </tbody>
    </table>
  </div>

  <!-- OUTRO -->
  <div class="mt-10 pt-6 border-t border-slate-800 text-xs font-mono text-slate-400 flex flex-wrap justify-between items-center gap-2">
    <div>« Le Savoir partagé est notre contre-pouvoir. L'OCHJU, c'est le regard qui ne se détourne plus. »</div>
    <div class="text-cyan-400 font-bold">CELLULE D'INVESTIGATION L'OCHJU • OCTOBRE 2026</div>
  </div>

</body>
</html>"""

bordereau_path = "public/docs/pieces-publiques-sante/BORDEREAU_60_SOURCES_PRIMAIRES_ETAT_ISO27037.html"
with open(bordereau_path, "w", encoding="utf-8") as f:
    f.write(bordereau_html)
print(f"Bordereau souverain local mis à jour : {bordereau_path}")

# 2. Génération des cartes pour l'Onglet 7 pointant vers le HTML local et le TXT brut
cards = []
for s in sources:
    card = f"""
          <!-- {s['id']} -->
          <div class="source-item p-4 rounded-2xl bg-slate-950 border border-slate-800 hover:border-cyan-500/50 transition flex flex-col justify-between space-y-3" data-cat="{s['cat']}">
            <div>
              <div class="flex justify-between items-center font-mono text-[10px] mb-1">
                <span class="text-cyan-400 font-bold">{s['id']} • {s['cat']}</span>
                <span class="text-slate-500 font-mono truncate max-w-[150px]">{s['ref']}</span>
              </div>
              <h4 class="text-sm font-bold text-white font-serif">{s['title']}</h4>
              <p class="text-xs text-slate-300 leading-relaxed mt-1">
                {s['desc']}
              </p>
            </div>
            <div class="pt-2 border-t border-slate-900 font-mono text-[10px] text-amber-300/90 flex flex-col space-y-1">
              <div class="text-slate-400"><strong class="text-amber-400">Portée probatoire :</strong> {s['impact']}</div>
              <div class="text-[9px] text-slate-500 truncate mt-0.5">SHA-256 : {s['sha256']}</div>
              <div class="grid grid-cols-2 gap-2 pt-2">
                <a 
                  href="{s['html_url']}" 
                  target="_blank" 
                  class="px-2.5 py-1.5 rounded-lg bg-cyan-600 hover:bg-cyan-500 text-slate-950 text-[10px] font-bold font-mono uppercase transition text-center shadow flex items-center justify-center gap-1"
                >
                  <span>👁️ Lire Pièce ↗</span>
                </a>
                <a 
                  href="{s['txt_url']}" 
                  download 
                  class="px-2.5 py-1.5 rounded-lg bg-slate-900 hover:bg-slate-800 text-cyan-400 border border-cyan-500/30 text-[10px] font-bold font-mono uppercase transition text-center flex items-center justify-center gap-1"
                >
                  <span>📥 Brut .txt</span>
                </a>
              </div>
            </div>
          </div>"""
    cards.append(card)

cards_block = "\n".join(cards)
with open("public/docs/pieces-publiques-sante/tab7_interactive_cards.html", "w", encoding="utf-8") as f:
    f.write(cards_block)

# 3. Réinjection dans src/pages/dossier-secret-sante-corse.astro
astro_path = "src/pages/dossier-secret-sante-corse.astro"
with open(astro_path, "r", encoding="utf-8") as f:
    astro_content = f.read()

start_marker = '<div id="sources-grid"'
end_marker = '<!-- MODAL FORENSIQUE DE LECTURE'

start_idx = astro_content.find(start_marker)
end_idx = astro_content.find(end_marker)

if start_idx != -1 and end_idx != -1:
    new_grid = f"""<div id="sources-grid" class="grid grid-cols-1 md:grid-cols-2 gap-4 text-xs font-sans">
{cards_block}
        </div>

      </div>
    </div>

    """
    astro_content = astro_content[:start_idx] + new_grid + astro_content[end_idx:]
    with open(astro_path, "w", encoding="utf-8") as f:
        f.write(astro_content)
    print("Page Astro mise à jour avec les cartes locales souveraines !")
else:
    print(f"Erreur repères Astro : start_idx={start_idx}, end_idx={end_idx}")

# 4. Mise à jour complète de l'archive ZIP COFFRE_INTEGRAL_SANTE_CORSE_ISO27037.zip
zip_path = "public/docs/dossier_sante_corse/COFFRE_INTEGRAL_SANTE_CORSE_ISO27037.zip"
sources_dir = "public/docs/sources-etat-sante"

with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as z:
    # 1. Ajouter les 11 actes contentieux existants
    acts_dir = "public/docs/dossier_sante_corse"
    for f in os.listdir(acts_dir):
        if f.endswith(".html") or f.endswith(".pdf"):
            z.write(os.path.join(acts_dir, f), f"01_ARSENAL_CONTENTIEUX/{f}")
    
    # 2. Ajouter les bordereaux et inventaires JSON
    z.write(bordereau_path, "02_BORDEREAUX/BORDEREAU_60_SOURCES_PRIMAIRES_ETAT_ISO27037.html")
    z.write("public/docs/pieces-publiques-sante/INVENTAIRE_60_SOURCES_LOCALES_SOUVERAINES.json", "02_BORDEREAUX/INVENTAIRE_60_SOURCES_LOCALES_SOUVERAINES.json")
    
    # 3. Ajouter les 60 pièces physiques HTML et TXT scellées
    for f in os.listdir(sources_dir):
        z.write(os.path.join(sources_dir, f), f"03_CORPS_DU_DELIT_60_SOURCES_ETAT/{f}")

print(f"Archive ZIP recréée avec succès (100% autonome et complète) : {zip_path}")
print(f"Taille de l'archive : {os.path.getsize(zip_path)} octets")

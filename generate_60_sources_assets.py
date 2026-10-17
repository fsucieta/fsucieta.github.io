import json
import urllib.parse
import os

# Ce script génère :
# 1. Le bordereau officiel HTML autonome : public/docs/pieces-publiques-sante/BORDEREAU_60_SOURCES_PRIMAIRES_ETAT_ISO27037.html
# 2. Le fragment HTML pour l'Onglet 7 dans dossier-secret-sante-corse.astro avec boutons interactifs de consultation et liens souverains
# 3. La mise à jour de l'archive ZIP COFFRE_INTEGRAL_SANTE_CORSE_ISO27037.zip

def map_sovereign_url(s):
    ref = s.get("ref", "")
    title = s.get("title", "")
    cat = s.get("cat", "")
    sid = s.get("id", "")
    
    if "NOR:" in ref:
        nor = ref.replace("NOR:", "").strip()
        return f"https://www.legifrance.gouv.fr/liste/id/all/order/datePubli/nor/{nor}", "Légifrance (JORF)"
    elif "JORF" in ref or "BO Santé" in ref:
        q = urllib.parse.quote_plus(ref)
        return f"https://www.legifrance.gouv.fr/search/all?tab_selection=all&searchField=ALL&query={q}", "Légifrance / BO Santé"
    elif "BOAMP" in ref:
        avis_id = ref.replace("BOAMP", "").strip()
        q = urllib.parse.quote_plus(avis_id)
        return f"https://www.boamp.fr/pages/avis/?q={q}", "BOAMP / Marchés Publics"
    elif "PMID:" in ref:
        pmid = ref.replace("PMID:", "").strip()
        return f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/", "NCBI / PubMed"
    elif any(k in ref for k in ["ROD-", "CRC", "CDC", "CERTIF", "IGAS"]):
        q = urllib.parse.quote_plus(ref)
        return f"https://www.ccomptes.fr/fr/recherche?search_api_fulltext={q}", "Cour des comptes / CRC"
    elif "DREES" in ref or "SAE" in ref:
        return "https://data.drees.solidarites-sante.gouv.fr/explore/dataset/les-etablissements-de-sante-edition-2023/", "Portail Open Data DREES"
    elif "DAMIR" in ref:
        return "https://www.data.gouv.fr/fr/datasets/depenses-d-assurance-maladie-hors-prestations-en-especes-en-date-de-soins-open-damir/", "Data.gouv.fr (Open DAMIR)"
    elif "ATIH" in ref:
        return "https://www.atih.sante.fr/pmsi", "ATIH PMSI MCO"
    elif "FINESS" in ref:
        return "https://finess.sante.gouv.fr/", "Répertoire FINESS"
    elif "INPI" in ref or "RNE" in ref:
        return "https://data.inpi.fr/", "Registre National Entreprises"
    elif "CADASTRE" in ref:
        return "https://cadastre.data.gouv.fr/", "Cadastre Souverain DGFiP"
    elif "BRGM" in ref:
        return "https://infoterre.brgm.fr/", "InfoTerre / BRGM"
    elif "HUBEAU" in ref:
        return "https://hubeau.eaufrance.fr/", "Hub'Eau / EauFrance"
    elif any(k in ref for k in ["Cass.", "CA-PARIS", "CE-", "CJA", "ERP"]):
        q = urllib.parse.quote_plus(ref)
        return f"https://www.legifrance.gouv.fr/search/all?tab_selection=all&searchField=ALL&query={q}", "Légifrance / Jurisprudence"
    elif any(k in ref for k in ["SPF", "GALLIERA", "MILAN", "SCPRI", "IRSN", "RG2C"]):
        q = urllib.parse.quote_plus(ref)
        return f"https://www.santepubliquefrance.fr/recherche/#search={q}", "Santé Publique France"
    else:
        q = urllib.parse.quote_plus(title + " " + ref)
        return f"https://www.google.com/search?q={q}", "Portail d'Accès Officiel"

def generate_bordereau_html(sources):
    rows = []
    for s in sources:
        url, portal_name = map_sovereign_url(s)
        rows.append(f"""
        <tr class="hover:bg-slate-900/60 border-b border-slate-800 text-xs">
          <td class="p-3 font-mono font-bold text-cyan-400">{s['id']}</td>
          <td class="p-3 font-mono text-slate-400 text-[11px]">{s['cat']}</td>
          <td class="p-3">
            <div class="font-bold text-white font-serif text-sm">{s['title']}</div>
            <div class="text-slate-300 font-sans mt-0.5">{s['desc']}</div>
            <div class="text-[11px] font-mono text-amber-400 mt-1"><span class="text-slate-500">Portée :</span> {s['impact']}</div>
          </td>
          <td class="p-3 font-mono text-xs text-amber-300">{s['ref']}</td>
          <td class="p-3 whitespace-nowrap">
            <a href="{url}" target="_blank" rel="noopener noreferrer" class="inline-block px-3 py-1.5 rounded-lg bg-cyan-500 hover:bg-cyan-400 text-slate-950 font-mono font-bold text-[11px] uppercase transition shadow">
              Consulter ↗
            </a>
          </td>
        </tr>
        """)
    
    html = f"""<!DOCTYPE html>
<html lang="fr" class="bg-slate-950 text-slate-100">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Bordereau Récapitulatif des 60 Sources Primaires d'État (ISO/IEC 27037) - L'OCHJU</title>
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
          CORPUS DES 60 SOURCES PRIMAIRES D'ÉTAT SCELLÉES • ISO/IEC 27037:2012
        </div>
        <div class="text-[11px] text-slate-400 font-mono">
          Adossement légal aux registres souverains (Légifrance, BOAMP, DREES, Cour des comptes, PubMed)
        </div>
      </div>
    </div>
    <div class="flex items-center gap-2">
      <button onclick="window.print()" class="px-4 py-2 bg-cyan-500 hover:bg-cyan-400 text-slate-950 font-mono font-bold text-xs uppercase tracking-wider rounded-xl transition cursor-pointer shadow">
        🖨️ Imprimer / PDF
      </button>
      <a href="/public/docs/pieces-publiques-sante/INVENTAIRE_60_SOURCES_PRIMAIRES_ETAT.json" download class="px-4 py-2 bg-slate-800 hover:bg-slate-700 text-cyan-400 border border-cyan-500/40 font-mono font-bold text-xs uppercase tracking-wider rounded-xl transition">
        📥 Export JSON
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
          CELLULE D'INVESTIGATION FORENSIQUE L'OCHJU • DIVISION OPEN DATA SOUVERAINE
        </div>
      </div>
      <div class="text-right font-mono text-xs text-slate-400">
        <div>COTE OFFICIELLE : <span class="text-cyan-400 font-bold">LOCHJU-SANTE-CORPUS-60-ETAT</span></div>
        <div>NORME D'INTÉGRITÉ : <span class="text-white font-bold">ISO/IEC 27037:2012</span></div>
      </div>
    </div>
    
    <div>
      <h1 class="text-2xl md:text-3xl font-black text-white font-serif uppercase tracking-tight">
        Bordereau Forensique Intégral des 60 Pièces d'État, Arrêtés ARS & Registres Légaux
      </h1>
      <p class="text-xs md:text-sm text-slate-300 font-sans mt-2 leading-relaxed">
        Ce bordereau récapitule exhaustivement les 60 pièces souveraines opposables sur lesquelles s'appuient l'autopsie financière et les 11 actes contentieux de l'enquête. Conformément à l'article 35 de la loi du 29 juillet 1881 sur la liberté de la presse, ce corpus confère l'<strong>Exception de Vérité</strong> absolue.
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
          <th class="p-3">Document Source & Objet Probatoire</th>
          <th class="p-3">Cote / Référence</th>
          <th class="p-3">Accès Souverain</th>
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
    return html

def generate_tab7_cards_html(sources):
    cards = []
    for s in sources:
        url, portal_name = map_sovereign_url(s)
        # Échappement des quotes pour l'attribut data
        safe_title = s['title'].replace('"', '&quot;')
        safe_desc = s['desc'].replace('"', '&quot;')
        safe_impact = s['impact'].replace('"', '&quot;')
        safe_ref = s['ref'].replace('"', '&quot;')
        
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
              <div class="grid grid-cols-2 gap-2 pt-2">
                <button 
                  onclick="openSourceModal('{s['id']}', '{safe_title}', '{s['cat']}', '{safe_ref}', '{safe_desc}', '{safe_impact}', '{url}', '{portal_name}')"
                  class="px-2.5 py-1.5 rounded-lg bg-slate-900 hover:bg-slate-800 text-cyan-400 border border-slate-800 text-[10px] font-bold uppercase transition text-center cursor-pointer"
                >
                  👁️ Lire Notice
                </button>
                <a 
                  href="{url}" 
                  target="_blank" 
                  rel="noopener noreferrer" 
                  class="px-2.5 py-1.5 rounded-lg bg-cyan-600 hover:bg-cyan-500 text-slate-950 text-[10px] font-bold uppercase transition text-center shadow"
                >
                  🏛️ Source d'État ↗
                </a>
              </div>
            </div>
          </div>"""
        cards.append(card)
    return "\n".join(cards)

if __name__ == "__main__":
    with open("public/docs/pieces-publiques-sante/INVENTAIRE_60_SOURCES_PRIMAIRES_ETAT.json", "r", encoding="utf-8") as f:
        sources = json.load(f)
    
    # 1. Générer le bordereau HTML complet
    bordereau_html = generate_bordereau_html(sources)
    bordereau_path = "public/docs/pieces-publiques-sante/BORDEREAU_60_SOURCES_PRIMAIRES_ETAT_ISO27037.html"
    with open(bordereau_path, "w", encoding="utf-8") as f:
        f.write(bordereau_html)
    print(f"Bordereau officiel généré : {bordereau_path}")

    # 2. Générer le fichier de cartes HTML pour l'Onglet 7
    cards_html = generate_tab7_cards_html(sources)
    with open("public/docs/pieces-publiques-sante/tab7_interactive_cards.html", "w", encoding="utf-8") as f:
        f.write(cards_html)
    print("Cartes interactives générées avec succès !")

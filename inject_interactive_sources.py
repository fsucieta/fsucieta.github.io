import re

# Ce script injecte :
# 1. Le bouton de téléchargement du Bordereau des 60 pièces dans le header de l'Onglet 7
# 2. Le remplacement de la grille des 60 sources par les nouvelles cartes avec boutons (Lire Notice & Source d'État)
# 3. La modale interactive de lecture forensique (openSourceModal) dans le DOM
# 4. Les fonctions JS openSourceModal et closeSourceModal

astro_path = "src/pages/dossier-secret-sante-corse.astro"
with open(astro_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Remplacement du Header de l'Onglet 7 pour ajouter les boutons d'export et de téléchargement
old_header_target = """        <!-- HEADER DE L'ONGLET 7 -->
        <div class="p-6 rounded-2xl bg-slate-950 border border-cyan-500/40 space-y-4">
          <div class="flex flex-wrap items-center justify-between gap-3 border-b border-slate-900 pb-3">
            <div class="flex items-center gap-2">
              <span class="w-3 h-3 rounded-full bg-cyan-400 animate-ping"></span>
              <h3 class="text-xl font-bold font-serif text-white uppercase">
                Le Corps du Délit : Grand Bordereau Forensique des 60 Actes d'État, Arrêtés ARS & Données Brutes
              </h3>
            </div>
            <span class="text-xs font-mono px-3 py-1 bg-cyan-500/10 text-cyan-400 border border-cyan-500/30 rounded-full font-bold">
              60 SOURCES PRIMAIRES SCELLÉES ISO/IEC 27037
            </span>
          </div>
          <p class="text-xs md:text-sm text-slate-300 font-sans leading-relaxed">
            Conformément à la doctrine de <strong>L'OCHJU</strong>, chaque chiffre, chaque ratio et chaque chef de préjudice de cette enquête tentaculaire repose sur des <strong>documents d'État souverains et opposables</strong> (Journal Officiel de la République Française, rapports d'observations de la Cour des comptes et de la CRC Corse, marchés publics BOAMP, micro-données DREES et bases nationales SNDS). En application de l'<strong>article 35 de la loi du 29 juillet 1881</strong>, ce corpus confère l'<strong>Exception de Vérité</strong> absolue.
          </p>"""

new_header_replacement = """        <!-- HEADER DE L'ONGLET 7 -->
        <div class="p-6 rounded-2xl bg-slate-950 border border-cyan-500/40 space-y-4">
          <div class="flex flex-wrap items-center justify-between gap-3 border-b border-slate-900 pb-3">
            <div class="flex items-center gap-2">
              <span class="w-3 h-3 rounded-full bg-cyan-400 animate-ping"></span>
              <h3 class="text-xl font-bold font-serif text-white uppercase">
                Le Corps du Délit : Grand Bordereau Forensique des 60 Actes d'État, Arrêtés ARS & Données Brutes
              </h3>
            </div>
            <div class="flex flex-wrap items-center gap-2">
              <a 
                href="/docs/pieces-publiques-sante/BORDEREAU_60_SOURCES_PRIMAIRES_ETAT_ISO27037.html" 
                target="_blank" 
                class="px-3 py-1.5 rounded-xl bg-cyan-500 hover:bg-cyan-400 text-slate-950 font-mono text-xs uppercase tracking-wider font-bold transition shadow-lg flex items-center gap-1.5"
              >
                <span>📜 Consulter le Bordereau Complet (HTML)</span>
                <span>↗</span>
              </a>
              <a 
                href="/docs/pieces-publiques-sante/INVENTAIRE_60_SOURCES_PRIMAIRES_ETAT.json" 
                download 
                class="px-3 py-1.5 rounded-xl bg-slate-900 hover:bg-slate-800 text-cyan-400 border border-cyan-500/40 font-mono text-xs uppercase tracking-wider font-bold transition flex items-center gap-1.5"
              >
                <span>📥 Export JSON (60)</span>
              </a>
              <span class="text-xs font-mono px-3 py-1 bg-cyan-500/10 text-cyan-400 border border-cyan-500/30 rounded-full font-bold">
                60 SOURCES SCELLÉES ISO 27037
              </span>
            </div>
          </div>
          <p class="text-xs md:text-sm text-slate-300 font-sans leading-relaxed">
            Conformément à la doctrine de <strong>L'OCHJU</strong>, chaque chiffre, chaque ratio et chaque chef de préjudice de cette enquête tentaculaire repose sur des <strong>documents d'État souverains et opposables</strong> (Journal Officiel de la République Française, rapports d'observations de la Cour des comptes et de la CRC Corse, marchés publics BOAMP, micro-données DREES et bases nationales SNDS). En application de l'<strong>article 35 de la loi du 29 juillet 1881</strong>, ce corpus confère l'<strong>Exception de Vérité</strong> absolue. Vous pouvez <strong>consulter la notice forensique de chaque pièce</strong> ou <strong>accéder directement au registre légal d'État primaire</strong> via les boutons dédiés.
          </p>"""

if old_header_target in content:
    content = content.replace(old_header_target, new_header_replacement)
    print("Header Onglet 7 mis à jour avec boutons de téléchargement !")
else:
    print("ATTENTION : old_header_target non trouvé !")

# 2. Remplacement de la grille des sources
grid_pattern = re.compile(r'<div id="sources-grid" class="grid grid-cols-1 md:grid-cols-2 gap-4 text-xs font-sans">.*?</div>\s*</div>\s*</div>', re.DOTALL)

with open("public/docs/pieces-publiques-sante/tab7_interactive_cards.html", "r", encoding="utf-8") as f:
    cards_html = f.read()

new_grid_block = f"""<div id="sources-grid" class="grid grid-cols-1 md:grid-cols-2 gap-4 text-xs font-sans">
{cards_html}
        </div>

      </div>
    </div>"""

# On cherche la balise ouvrante sources-grid et la fin du tab 7
start_idx = content.find('<div id="sources-grid"')
if start_idx != -1:
    # On cherche la fin de l'onglet 7 qui est marquée par <!-- TEXTES CACHES POUR LA COPIE EN 1 CLIC
    end_marker = '<!-- TEXTES CACHES POUR LA COPIE EN 1 CLIC'
    end_idx = content.find(end_marker)
    if end_idx != -1:
        # Entre start_idx et end_idx, il y a la grille et les fermetures </div>
        before = content[:start_idx]
        after = content[end_idx:]
        
        # Modale de lecture
        modal_html = """
    <!-- MODAL FORENSIQUE DE LECTURE D'UNE SOURCE D'ÉTAT (ISO/IEC 27037) -->
    <div id="source-modal" class="fixed inset-0 z-50 bg-slate-950/80 backdrop-blur-md hidden flex items-center justify-center p-4">
      <div class="bg-slate-900 border-2 border-cyan-500/50 rounded-3xl max-w-2xl w-full p-6 md:p-8 space-y-5 shadow-2xl relative">
        <button onclick="closeSourceModal()" class="absolute top-5 right-5 text-slate-400 hover:text-white font-mono text-xl cursor-pointer">
          ✕
        </button>
        <div class="flex items-center gap-2 border-b border-slate-800 pb-3">
          <span class="w-3 h-3 rounded-full bg-cyan-400"></span>
          <span id="modal-cat" class="text-xs font-mono font-bold text-cyan-400 uppercase tracking-widest"></span>
          <span class="text-slate-600">•</span>
          <span id="modal-id" class="text-xs font-mono font-bold text-slate-300"></span>
        </div>
        <div>
          <h3 id="modal-title" class="text-lg md:text-xl font-bold font-serif text-white"></h3>
          <div class="mt-2 inline-block px-2.5 py-1 rounded bg-slate-950 border border-slate-800 text-xs font-mono text-amber-400" id="modal-ref"></div>
        </div>
        <div class="space-y-3 text-xs md:text-sm text-slate-300 font-sans leading-relaxed">
          <div>
            <strong class="text-slate-400 uppercase font-mono text-[11px] block">Contenu & Objet Probatoire :</strong>
            <p id="modal-desc" class="mt-1 text-slate-200"></p>
          </div>
          <div class="p-4 rounded-xl bg-slate-950 border border-slate-800">
            <strong class="text-amber-400 uppercase font-mono text-[11px] block">Portée Juridique & Opposabilité :</strong>
            <p id="modal-impact" class="mt-1 text-amber-200/90 font-mono text-xs"></p>
          </div>
        </div>
        <div class="flex flex-wrap justify-between items-center gap-3 pt-3 border-t border-slate-800 font-mono text-xs">
          <span class="text-slate-500 text-[11px]">NORME FORENSIQUE ISO/IEC 27037:2012</span>
          <div class="flex gap-2">
            <button onclick="closeSourceModal()" class="px-4 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 font-bold uppercase transition cursor-pointer">
              Fermer
            </button>
            <a id="modal-link" href="#" target="_blank" rel="noopener noreferrer" class="px-4 py-2 rounded-xl bg-cyan-500 hover:bg-cyan-400 text-slate-950 font-bold uppercase transition shadow flex items-center gap-1.5">
              <span>Accéder à la Source Souveraine</span>
              <span>↗</span>
            </a>
          </div>
        </div>
      </div>
    </div>

    """
        
        content = before + new_grid_block + "\n\n" + modal_html + after
        print("Grille de cartes interactives et modale injectées avec succès !")
    else:
        print("ATTENTION : end_marker non trouvé !")
else:
    print("ATTENTION : start_idx non trouvé !")

# 3. Ajout des fonctions JS dans le bloc <script>
js_functions = """
  // MODALE FORENSIQUE DES SOURCES D'ÉTAT
  window.openSourceModal = function(id, title, cat, ref, desc, impact, url, portalName) {
    const modal = document.getElementById('source-modal');
    if (!modal) return;
    document.getElementById('modal-id').textContent = id;
    document.getElementById('modal-title').textContent = title;
    document.getElementById('modal-cat').textContent = cat;
    document.getElementById('modal-ref').textContent = 'Cote / Réf : ' + ref;
    document.getElementById('modal-desc').textContent = desc;
    document.getElementById('modal-impact').textContent = impact;
    
    const linkBtn = document.getElementById('modal-link');
    if (linkBtn) {
      linkBtn.href = url;
      linkBtn.querySelector('span').textContent = 'Ouvrir sur ' + portalName;
    }
    modal.classList.remove('hidden');
  };

  window.closeSourceModal = function() {
    const modal = document.getElementById('source-modal');
    if (modal) modal.classList.add('hidden');
  };

  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') closeSourceModal();
  });
"""

if "window.openSourceModal" not in content:
    content = content.replace("</script>", js_functions + "\n</script>")
    print("Fonctions JavaScript modale ajoutées !")

with open(astro_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Mise à jour complète du fichier Astro terminée !")

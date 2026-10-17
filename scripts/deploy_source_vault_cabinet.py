# -*- coding: utf-8 -*-
"""
Intégration d'un Espace Dépôt & Archives Documentaires Primaires dans dossier-transparence-citoyenne-ajaccio.astro.
1. Ajout des boutons "📥 Télécharger PDF Certifié" sur les sections XI à XVII (qui n'avaient que le bouton HTML).
2. Ajout sous le grand bouton ZIP d'un panneau déroulant / table d'accès direct "CONSULTER & TÉLÉCHARGER CHAQUE PIÈCE SOURCE OFFICIELLE À L'UNITÉ" :
   - Contrat COSP 2026 complet scanné (6,0 Mo) [Lecture direct / Télécharger]
   - Les 178 pages d'Annexes du COSP avec l'Annexe 16 (25,6 Mo) [Lecture direct / Télécharger]
   - Délibération CAPA n° 2026-071 officielle (4,1 Mo) [Lecture direct / Télécharger]
   - Arrêté de DUP Angelo et Mise en Compatibilité PLU (19,2 Mo) [Lecture direct / Télécharger]
   - ROB CAPA 2024, 2025, 2026 officiels [Lecture direct / Télécharger]
   - Délibérations de l'Assemblée de Corse [Lecture direct / Télécharger]
   - Les 17 Livres d'instruction souveraine en PDF et HTML [Lecture direct / Télécharger]
"""

import re

astro_path = r"C:\Users\PC-Bureau\Desktop\docucu\site_github_pages\src\pages\dossier-transparence-citoyenne-ajaccio.astro"

with open(astro_path, "r", encoding="utf-8") as f:
    text = f.read()

# 1. Remplacement des en-têtes des livres 11 à 17 pour ajouter le bouton PDF
for num, filename in [
    ("11", "11_FABRIQUE_SCANDALE_CABINETS_CONSEIL_MC18_022"),
    ("12", "12_HOLD_UP_FISCAL_RESERVE_DECHETS_ET_IMPOTS"),
    ("13", "13_OPERATION_IMMOBILIERE_MISERICORDE_AMETARRA"),
    ("14", "14_SABOTAGE_ROUTE_MONT_THABOR_ET_TORTUE_HERMANN"),
    ("15", "15_SACRIFICE_SOCIAL_ET_HUMAIN_BUS_MUVITARRA"),
    ("16", "16_AUTOPSIE_FINANCIERE_MUVITARRA_IMPAYES_ET_ART30"),
    ("17", "17_EVASION_BUDGETAIRE_NAVETTE_PORTICCIO_ET_ANNEXE16")
]:
    old_btn = f"""<div class="flex items-center gap-2">
              <a href="/docs/opposition_ajaccio/{filename}.html" target="_blank" class="text-xs font-mono bg-slate-800 hover:bg-slate-700 text-cyan-300 px-3 py-1.5 rounded-lg border border-slate-700 transition shadow flex items-center gap-1.5">
                <span>🌐</span> Ouvrir Plein Écran
              </a>
            </div>"""
    
    new_btn = f"""<div class="flex items-center gap-2">
              <a href="/docs/opposition_ajaccio/{filename}.pdf" download class="text-xs font-mono bg-slate-800 hover:bg-slate-700 text-slate-200 px-3 py-1.5 rounded-lg border border-slate-700 transition shadow flex items-center gap-1.5">
                <span>📥</span> PDF Certifié ISO
              </a>
              <a href="/docs/opposition_ajaccio/{filename}.html" target="_blank" class="text-xs font-mono bg-slate-800 hover:bg-slate-700 text-cyan-300 px-3 py-1.5 rounded-lg border border-slate-700 transition shadow flex items-center gap-1.5">
                <span>🌐</span> Ouvrir Plein Écran
              </a>
            </div>"""
    text = text.replace(old_btn, new_btn)

# 2. Ajout de la Galerie / Tableau des 37 Pièces Officielles à l'unité sous le bandeau du Coffre Fort
source_vault_html = """
    <!-- DÉPÔT NUMÉRIQUE OPPOSABLE : CONSULTATION ET TÉLÉCHARGEMENT DIRECT À L'UNITÉ (37 PIÈCES SCELLÉES) -->
    <details class="group rounded-3xl bg-slate-950/90 border-2 border-slate-700/80 p-6 md:p-8 shadow-2xl space-y-6 transition-all duration-300">
      <summary class="cursor-pointer flex flex-wrap items-center justify-between gap-3 select-none">
        <div class="flex items-center gap-3">
          <div class="p-2.5 rounded-2xl bg-amber-500/10 text-amber-400 border border-amber-500/30 text-xl font-bold">
            📂
          </div>
          <div>
            <h3 class="text-lg md:text-xl font-bold font-serif text-white group-hover:text-amber-400 transition">
              Armoire des Actes Sources & Pièces Officielles à l'Unité (Accès Lecture & Téléchargement)
            </h3>
            <p class="text-xs font-mono text-slate-400">
              Cliquez pour dérouler et consulter en direct ou télécharger chacun des actes administratifs scannés et mémoires juridiques.
            </p>
          </div>
        </div>
        <div class="flex items-center gap-2">
          <span class="px-3 py-1 rounded-full bg-slate-900 border border-slate-700 text-slate-300 text-xs font-mono font-bold">
            37 Actes Souverains
          </span>
          <span class="text-amber-400 text-sm group-open:rotate-180 transition-transform duration-200">
            ▼
          </span>
        </div>
      </summary>

      <div class="border-t border-slate-800/80 pt-6 space-y-6">
        
        <!-- SECTION 1 : LES CONTRATS ET ACTES PUBLICS SCANNÉS (ORIGINAUX) -->
        <div class="space-y-3">
          <div class="text-xs font-mono font-bold uppercase tracking-wider text-amber-400 flex items-center gap-2">
            <span>📜</span> 1. CONTRATS PUBLICS SCANNÉS, ARRÊTÉS & RAPPORTS BUDGÉTAIRES OFFICIELS
          </div>
          <div class="grid grid-cols-1 md:grid-cols-2 gap-3 text-xs font-sans">
            
            <!-- Contrat COSP Principal -->
            <div class="p-4 rounded-2xl bg-slate-900/80 border border-slate-800 flex flex-col justify-between space-y-3">
              <div>
                <div class="flex items-center justify-between">
                  <span class="px-2 py-0.5 rounded bg-amber-500/10 text-amber-300 border border-amber-500/30 font-mono text-[10px] font-bold">6,04 Mo • PDF Scanné</span>
                  <span class="font-mono text-[10px] text-slate-400">Signé 22/06/2026</span>
                </div>
                <div class="font-bold text-white text-sm mt-1">Contrat COSP 2026-2032 CAPA - SPL Muvitarra</div>
                <div class="text-[11px] text-slate-400 mt-0.5">Le contrat principal complet avec les clauses d'austérité et l'Article 30.1.</div>
              </div>
              <div class="flex items-center gap-2 pt-2 border-t border-slate-800 font-mono text-xs">
                <a href="/docs/COSP_MUVITARRA_2026_CONTRAT_PRINCIPAL.pdf" target="_blank" class="flex-1 py-1.5 px-3 rounded-lg bg-slate-800 hover:bg-slate-700 text-cyan-300 text-center border border-slate-700 transition">
                  👁️ Lire en Ligne
                </a>
                <a href="/docs/COSP_MUVITARRA_2026_CONTRAT_PRINCIPAL.pdf" download class="flex-1 py-1.5 px-3 rounded-lg bg-amber-500/20 hover:bg-amber-500/30 text-amber-300 text-center border border-amber-500/40 font-bold transition">
                  📥 Télécharger
                </a>
              </div>
            </div>

            <!-- Annexes COSP 178 pages -->
            <div class="p-4 rounded-2xl bg-slate-900/80 border border-slate-800 flex flex-col justify-between space-y-3">
              <div>
                <div class="flex items-center justify-between">
                  <span class="px-2 py-0.5 rounded bg-rose-500/10 text-rose-300 border border-rose-500/30 font-mono text-[10px] font-bold">25,64 Mo • PDF Scanné</span>
                  <span class="font-mono text-[10px] text-slate-400">178 Pages</span>
                </div>
                <div class="font-bold text-white text-sm mt-1">Les 178 Pages d'Annexes du Contrat COSP</div>
                <div class="text-[11px] text-slate-400 mt-0.5">Contient l'Annexe 16 (mandat gratuit p.165), l'Annexe 9 (plan bus) et l'Annexe 8.</div>
              </div>
              <div class="flex items-center gap-2 pt-2 border-t border-slate-800 font-mono text-xs">
                <a href="/docs/COSP_MUVITARRA_2026_ANNEXES.pdf" target="_blank" class="flex-1 py-1.5 px-3 rounded-lg bg-slate-800 hover:bg-slate-700 text-cyan-300 text-center border border-slate-700 transition">
                  👁️ Lire en Ligne
                </a>
                <a href="/docs/COSP_MUVITARRA_2026_ANNEXES.pdf" download class="flex-1 py-1.5 px-3 rounded-lg bg-rose-500/20 hover:bg-rose-500/30 text-rose-300 text-center border border-rose-500/40 font-bold transition">
                  📥 Télécharger
                </a>
              </div>
            </div>

            <!-- Délibération 2026-071 -->
            <div class="p-4 rounded-2xl bg-slate-900/80 border border-slate-800 flex flex-col justify-between space-y-3">
              <div>
                <div class="flex items-center justify-between">
                  <span class="px-2 py-0.5 rounded bg-amber-500/10 text-amber-300 border border-amber-500/30 font-mono text-[10px] font-bold">4,05 Mo • PDF Officiel</span>
                  <span class="font-mono text-[10px] text-slate-400">Séance 29/06/2026</span>
                </div>
                <div class="font-bold text-white text-sm mt-1">Délibération CAPA n° 2026-071</div>
                <div class="text-[11px] text-slate-400 mt-0.5">Acte communautaire officiel d'attribution du contrat précaire d'un an à la SPL.</div>
              </div>
              <div class="flex items-center gap-2 pt-2 border-t border-slate-800 font-mono text-xs">
                <a href="/docs/DELIB_2026_071_NOUVEAU_COSP_MUVITARRA.pdf" target="_blank" class="flex-1 py-1.5 px-3 rounded-lg bg-slate-800 hover:bg-slate-700 text-cyan-300 text-center border border-slate-700 transition">
                  👁️ Lire en Ligne
                </a>
                <a href="/docs/DELIB_2026_071_NOUVEAU_COSP_MUVITARRA.pdf" download class="flex-1 py-1.5 px-3 rounded-lg bg-amber-500/20 hover:bg-amber-500/30 text-amber-300 text-center border border-amber-500/40 font-bold transition">
                  📥 Télécharger
                </a>
              </div>
            </div>

            <!-- Arrêté DUP Téléporté Angelo -->
            <div class="p-4 rounded-2xl bg-slate-900/80 border border-slate-800 flex flex-col justify-between space-y-3">
              <div>
                <div class="flex items-center justify-between">
                  <span class="px-2 py-0.5 rounded bg-red-500/10 text-red-300 border border-red-500/30 font-mono text-[10px] font-bold">19,18 Mo • PDF Préfecture</span>
                  <span class="font-mono text-[10px] text-slate-400">Arrêté 2023-12-04</span>
                </div>
                <div class="font-bold text-white text-sm mt-1">Arrêté Préfectoral DUP & Dérogation Espèces Protégées</div>
                <div class="text-[11px] text-slate-400 mt-0.5">Autorisation de destruction d'habitats Tortue d'Hermann et servitudes aériennes.</div>
              </div>
              <div class="flex items-center gap-2 pt-2 border-t border-slate-800 font-mono text-xs">
                <a href="/docs/A-P-de-DUP-du-teleporte-et-MEC-PLU-.pdf" target="_blank" class="flex-1 py-1.5 px-3 rounded-lg bg-slate-800 hover:bg-slate-700 text-cyan-300 text-center border border-slate-700 transition">
                  👁️ Lire en Ligne
                </a>
                <a href="/docs/A-P-de-DUP-du-teleporte-et-MEC-PLU-.pdf" download class="flex-1 py-1.5 px-3 rounded-lg bg-red-500/20 hover:bg-red-500/30 text-red-300 text-center border border-red-500/40 font-bold transition">
                  📥 Télécharger
                </a>
              </div>
            </div>

            <!-- ROB 2024 (Aveu Porticcio page 17) -->
            <div class="p-4 rounded-2xl bg-slate-900/80 border border-slate-800 flex flex-col justify-between space-y-3">
              <div>
                <div class="flex items-center justify-between">
                  <span class="px-2 py-0.5 rounded bg-cyan-500/10 text-cyan-300 border border-cyan-500/30 font-mono text-[10px] font-bold">129 Ko • PDF Budgétaire</span>
                  <span class="font-mono text-[10px] text-slate-400">Page 17 Scellée</span>
                </div>
                <div class="font-bold text-white text-sm mt-1">Rapport d'Orientations Budgétaires (ROB 2024)</div>
                <div class="text-[11px] text-slate-400 mt-0.5">Aveu officiel de la subvention d'équilibre payant la navette maritime de Porticcio.</div>
              </div>
              <div class="flex items-center gap-2 pt-2 border-t border-slate-800 font-mono text-xs">
                <a href="/docs/rob-2024-capa-ajaccio.pdf" target="_blank" class="flex-1 py-1.5 px-3 rounded-lg bg-slate-800 hover:bg-slate-700 text-cyan-300 text-center border border-slate-700 transition">
                  👁️ Lire en Ligne
                </a>
                <a href="/docs/rob-2024-capa-ajaccio.pdf" download class="flex-1 py-1.5 px-3 rounded-lg bg-cyan-500/20 hover:bg-cyan-500/30 text-cyan-300 text-center border border-cyan-500/40 font-bold transition">
                  📥 Télécharger
                </a>
              </div>
            </div>

            <!-- ROB 2025 (Détournement Réserve Déchets) -->
            <div class="p-4 rounded-2xl bg-slate-900/80 border border-slate-800 flex flex-col justify-between space-y-3">
              <div>
                <div class="flex items-center justify-between">
                  <span class="px-2 py-0.5 rounded bg-emerald-500/10 text-emerald-300 border border-emerald-500/30 font-mono text-[10px] font-bold">102 Ko • PDF Budgétaire</span>
                  <span class="font-mono text-[10px] text-slate-400">Pages 5-7 Scellées</span>
                </div>
                <div class="font-bold text-white text-sm mt-1">Rapport d'Orientations Budgétaires (ROB 2025)</div>
                <div class="text-[11px] text-slate-400 mt-0.5">Reprise intégrale de la provision de 1,5 M€ de 2018 pour payer le câble.</div>
              </div>
              <div class="flex items-center gap-2 pt-2 border-t border-slate-800 font-mono text-xs">
                <a href="/docs/rob-2025-capa-ajaccio.pdf" target="_blank" class="flex-1 py-1.5 px-3 rounded-lg bg-slate-800 hover:bg-slate-700 text-cyan-300 text-center border border-slate-700 transition">
                  👁️ Lire en Ligne
                </a>
                <a href="/docs/rob-2025-capa-ajaccio.pdf" download class="flex-1 py-1.5 px-3 rounded-lg bg-emerald-500/20 hover:bg-emerald-500/30 text-emerald-300 text-center border border-emerald-500/40 font-bold transition">
                  📥 Télécharger
                </a>
              </div>
            </div>

          </div>
        </div>

        <!-- SECTION 2 : PRÉSENTATION EXÉCUTIVE D'ÉTAT-MAJOR -->
        <div class="p-4 rounded-2xl bg-gradient-to-r from-slate-900 via-indigo-950/40 to-slate-900 border border-indigo-500/40 flex flex-col sm:flex-row items-center justify-between gap-4">
          <div class="space-y-1 text-center sm:text-left">
            <div class="text-indigo-400 font-mono font-bold text-xs uppercase">📊 PRÉSENTATION EXÉCUTIVE (SLIDE DECK 16:9)</div>
            <div class="text-white font-bold text-sm">Deck de Présentation Exécutive pour l'Association Transparence Citoyenne</div>
            <div class="text-slate-400 text-xs">Synthèse visuelle de haute direction (5 slides HD) prête pour projection ou point presse.</div>
          </div>
          <div class="flex items-center gap-2 shrink-0 font-mono text-xs">
            <a href="/docs/opposition_ajaccio/DECK_EXECUTIVE_PRESENTATION_TRANSPARENCE_CITOYENNE.pdf" target="_blank" class="py-2 px-4 rounded-xl bg-slate-800 hover:bg-slate-700 text-cyan-300 border border-slate-700 transition">
              👁️ Visualiser
            </a>
            <a href="/docs/opposition_ajaccio/DECK_EXECUTIVE_PRESENTATION_TRANSPARENCE_CITOYENNE.pdf" download class="py-2 px-4 rounded-xl bg-indigo-600 hover:bg-indigo-500 text-white font-bold transition shadow-lg">
              📥 Télécharger le Deck (1,92 Mo)
            </a>
          </div>
        </div>

      </div>
    </details>
"""

# Insertion du panneau Armoire des Actes Sources juste après le bloc de téléchargement universel du ZIP
target_zip_block_end = "📥 Télécharger le Coffre Intégral (ZIP 47,6 Mo)\n      </a>\n    </div>"
text = text.replace(target_zip_block_end, target_zip_block_end + "\n\n" + source_vault_html)

with open(astro_path, "w", encoding="utf-8") as f:
    f.write(text)

print("Succès : L'Armoire des 37 Actes Sources avec accès direct en lecture ET téléchargement a été déployée.")

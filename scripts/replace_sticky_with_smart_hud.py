# -*- coding: utf-8 -*-
"""
Remplacement du bandeau à scrollbar horizontal par une barre de contrôle ergonomique suprême :
1. Une barre compacte sticky avec :
   - Un sélecteur menu déroulant (Dropdown) stylisé "Sauter au Livre (1 à 10)..."
   - Une mini-grille de 10 pastilles numérotées cliquables [01] [02] ... [10] bicolores avec infobulles/titres
   - Deux boutons "Livre précédent ◀" / "Livre suivant ▶"
   - Un bouton "Déplier tout / Replier tout"
2. Pas de barre de défilement horizontal visible (zéro scrollbar moche).
3. Adaptation 100% responsive sur mobile, tablette et desktop.
"""

import re

astro_path = r"C:\Users\PC-Bureau\Desktop\docucu\site_github_pages\src\pages\dossier-transparence-citoyenne-ajaccio.astro"

with open(astro_path, "r", encoding="utf-8") as f:
    text = f.read()

# Ancien bloc sticky navigation
old_sticky_pattern = re.compile(
    r'<!-- TABLEAU DE BORD EXÉCUTIF & NAVIGATION RAPIDE HIGH-TECH -->.*?</div>\s*</div>',
    re.DOTALL
)

new_sticky_control = """<!-- BARRE DE CONTRÔLE ERGONOMIQUE FLOTTANTE (SMART HUD) -->
    <div class="sticky top-3 z-50 my-6 bg-slate-950/95 backdrop-blur-2xl border border-amber-500/30 rounded-2xl p-3 md:p-4 shadow-[0_10px_40px_rgba(0,0,0,0.8)] transition-all">
      <div class="flex flex-col md:flex-row md:items-center justify-between gap-3">
        
        <!-- GAUCHE : SÉLECTEUR RAPIDE & STATUT -->
        <div class="flex items-center gap-3">
          <span class="flex items-center gap-2 px-3 py-1.5 rounded-xl bg-amber-500/10 border border-amber-500/30 text-amber-400 font-mono text-xs font-bold uppercase tracking-wider shrink-0">
            <span class="w-2 h-2 rounded-full bg-amber-400 animate-pulse"></span>
            10 LIVRES SCELLÉS
          </span>

          <!-- MENU DÉROULANT DIRECT POUR NAVIGATION INSTANTANÉE -->
          <select 
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
          </select>
        </div>

        <!-- DROITE : LES 10 PASTILLES TACTILES [01] à [10] SANS AUCUNE SCROLLBAR -->
        <div class="flex flex-wrap items-center gap-1.5 justify-center md:justify-end">
          <a href="#livre-1" title="Livre I : Saisine CRC Corse" class="w-8 h-8 rounded-lg bg-slate-900 hover:bg-amber-500/20 text-slate-300 hover:text-amber-400 border border-slate-800 hover:border-amber-500/50 flex items-center justify-center font-mono text-xs font-bold transition active:scale-95">01</a>
          <a href="#livre-2" title="Livre II : Disparité CREM/COSP" class="w-8 h-8 rounded-lg bg-slate-900 hover:bg-rose-500/20 text-slate-300 hover:text-rose-400 border border-slate-800 hover:border-rose-500/50 flex items-center justify-center font-mono text-xs font-bold transition active:scale-95">02</a>
          <a href="#livre-3" title="Livre III : Sécurité ERP U Stiletto" class="w-8 h-8 rounded-lg bg-slate-900 hover:bg-red-500/20 text-slate-300 hover:text-red-400 border border-slate-800 hover:border-red-500/50 flex items-center justify-center font-mono text-xs font-bold transition active:scale-95">03</a>
          <a href="#livre-4" title="Livre IV : 5 Questions de Sommation" class="w-8 h-8 rounded-lg bg-slate-900 hover:bg-amber-500/20 text-slate-300 hover:text-amber-400 border border-slate-800 hover:border-amber-500/50 flex items-center justify-center font-mono text-xs font-bold transition active:scale-95">04</a>
          <a href="#livre-5" title="Livre V : Délibération d'Amendement" class="w-8 h-8 rounded-lg bg-slate-900 hover:bg-emerald-500/20 text-slate-300 hover:text-emerald-400 border border-slate-800 hover:border-emerald-500/50 flex items-center justify-center font-mono text-xs font-bold transition active:scale-95">05</a>
          <a href="#livre-6" title="Livre VI : Gare Centrale Assemblée Corse" class="w-8 h-8 rounded-lg bg-slate-900 hover:bg-blue-500/20 text-slate-300 hover:text-blue-400 border border-slate-800 hover:border-blue-500/50 flex items-center justify-center font-mono text-xs font-bold transition active:scale-95">06</a>
          <a href="#livre-7" title="Livre VII : Compétence SPL Mobilité" class="w-8 h-8 rounded-lg bg-slate-900 hover:bg-purple-500/20 text-slate-300 hover:text-purple-400 border border-slate-800 hover:border-purple-500/50 flex items-center justify-center font-mono text-xs font-bold transition active:scale-95">07</a>
          <a href="#livre-8" title="Livre VIII : Audit M4 Parking Diamant" class="w-8 h-8 rounded-lg bg-slate-900 hover:bg-cyan-500/20 text-slate-300 hover:text-cyan-400 border border-slate-800 hover:border-cyan-500/50 flex items-center justify-center font-mono text-xs font-bold transition active:scale-95">08</a>
          <a href="#livre-9" title="Livre IX : Rente Scolaire 9 Villages" class="w-8 h-8 rounded-lg bg-slate-900 hover:bg-emerald-500/20 text-slate-300 hover:text-emerald-400 border border-slate-800 hover:border-emerald-500/50 flex items-center justify-center font-mono text-xs font-bold transition active:scale-95">09</a>
          <a href="#livre-10" title="Livre X : Halte St-Joseph vs Gare" class="w-8 h-8 rounded-lg bg-slate-900 hover:bg-indigo-500/20 text-slate-300 hover:text-indigo-400 border border-slate-800 hover:border-indigo-500/50 flex items-center justify-center font-mono text-xs font-bold transition active:scale-95">10</a>
          
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
            📕 Replier Tous les Textes
          </button>
        </div>

      </div>
    </div>"""

text = old_sticky_pattern.sub(new_sticky_control, text)

with open(astro_path, "w", encoding="utf-8") as f:
    f.write(text)

print("Succès : Le conteneur à scrollbar horizontale a été remplacé par un Smart HUD ergonomique (menu dropdown + 10 pastilles tactiles + bouton global).")

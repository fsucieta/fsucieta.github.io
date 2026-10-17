# -*- coding: utf-8 -*-
"""
Conversion définitive des 3 blocs bruts Mermaid/Gantt en composants graphiques SVG et infographies Tailwind interactives.
1. Schéma d'organigramme des flux sociétaires & prédateurs fonciers (SVG haute définition responsive).
2. Diagramme de transition opérationnelle des marchés scolaires vers les LRM (Flow infographique HTML/Tailwind).
3. Chronogramme comparatif (Gantt) du trajet pendulaire Mezzana -> Port (Infographie temps de parcours comparative).
"""

import re

astro_path = r"C:\Users\PC-Bureau\Desktop\docucu\site_github_pages\src\pages\dossier-transparence-citoyenne-ajaccio.astro"

with open(astro_path, "r", encoding="utf-8") as f:
    text = f.read()

# ==============================================================================
# 1. ORGANIGRAMME DES FLUX SOCIÉTAIRES (Remplace le flowchart TD brut)
# ==============================================================================
html_organigramme = """
<div class="my-8 p-6 md:p-8 rounded-3xl border border-amber-500/40 bg-slate-950 shadow-2xl space-y-6">
  <div class="flex flex-wrap items-center justify-between gap-3 border-b border-slate-800 pb-4">
    <div class="flex items-center gap-2.5">
      <span class="w-3.5 h-3.5 rounded-full bg-amber-400 animate-pulse"></span>
      <span class="text-xs font-mono font-bold uppercase tracking-wider text-amber-400">ORGANIGRAMME FORENSIQUE • LA CHAÎNE DE VALEUR SOCIÉTAIRE & LES VÉHICULES MOBILISÉS</span>
    </div>
    <span class="text-[11px] font-mono text-slate-400">Croisement RNE / BODACC / Délibérations</span>
  </div>

  <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
    
    <!-- PÔLE POUVOIR PUBLIC -->
    <div class="p-4 rounded-2xl bg-slate-900/90 border border-slate-700 space-y-3">
      <div class="flex items-center justify-between">
        <span class="text-[11px] font-mono font-bold uppercase tracking-wider text-amber-400">🏛️ POUVOIR PUBLIC</span>
        <span class="text-[10px] font-mono px-2 py-0.5 rounded bg-amber-500/10 text-amber-300 border border-amber-500/30">Décideur</span>
      </div>
      <div class="space-y-2 text-xs">
        <div class="p-2.5 rounded-xl bg-slate-950 border border-slate-800">
          <div class="font-bold text-white">CAPA (Agglomération)</div>
          <div class="text-[11px] text-slate-400">Autorité Organisatrice Mobilité</div>
        </div>
        <div class="p-2.5 rounded-xl bg-slate-950 border border-slate-800">
          <div class="font-bold text-white">Ville d'Ajaccio</div>
          <div class="text-[11px] text-slate-400">Voirie & Stationnement en ouvrage</div>
        </div>
        <div class="p-2.5 rounded-xl bg-amber-950/30 border border-amber-500/40">
          <div class="font-bold text-amber-300">Stéphane SBRAGGIA</div>
          <div class="text-[10px] text-slate-300">Maire Ajaccio / Pdt CAPA / Pdt SPL Ametarra / Pdt SPL Muvitarra</div>
        </div>
      </div>
    </div>

    <!-- PÔLE AMÉNAGEMENT FONCIER -->
    <div class="p-4 rounded-2xl bg-slate-900/90 border border-slate-700 space-y-3">
      <div class="flex items-center justify-between">
        <span class="text-[11px] font-mono font-bold uppercase tracking-wider text-emerald-400">🏗️ AMÉNAGEMENT FONCIER</span>
        <span class="text-[10px] font-mono px-2 py-0.5 rounded bg-emerald-500/10 text-emerald-300 border border-emerald-500/30">Grands Projets</span>
      </div>
      <div class="space-y-2 text-xs">
        <div class="p-2.5 rounded-xl bg-slate-950 border border-slate-800">
          <div class="font-bold text-emerald-300">SPL AMETARRA</div>
          <div class="text-[11px] text-slate-400 font-mono">SIREN 812 410 488 • Cap. 1 000 000 €</div>
          <div class="text-[10px] text-slate-500">100% Public (CAPA / Ville)</div>
        </div>
        <div class="p-2.5 rounded-xl bg-slate-950 border border-slate-800">
          <div class="font-bold text-white">Site Ex-Miséricorde</div>
          <div class="text-[11px] text-slate-400">9 ha / 781 logements • BDT 10,2 M€</div>
        </div>
        <div class="p-2.5 rounded-xl bg-slate-950 border border-slate-800">
          <div class="font-bold text-white">Citadelle Miollis</div>
          <div class="text-[11px] text-slate-400">Rachat Défense 1,3 M€ • MOE 4,0 M€</div>
        </div>
      </div>
    </div>

    <!-- PÔLE MOBILITÉ & CÂBLE -->
    <div class="p-4 rounded-2xl bg-slate-900/90 border border-slate-700 space-y-3">
      <div class="flex items-center justify-between">
        <span class="text-[11px] font-mono font-bold uppercase tracking-wider text-rose-400">🚠 MOBILITÉS & CÂBLE</span>
        <span class="text-[10px] font-mono px-2 py-0.5 rounded bg-rose-500/10 text-rose-300 border border-rose-500/30">Asymétrie</span>
      </div>
      <div class="space-y-2 text-xs">
        <div class="p-2.5 rounded-xl bg-slate-950 border border-slate-800">
          <div class="font-bold text-cyan-300">SPL MUVITARRA</div>
          <div class="text-[11px] text-slate-400 font-mono">SIREN 822 167 748 • Bus Urbain</div>
          <div class="text-[10px] text-rose-400">Sous austérité / Gel nominal COSP</div>
        </div>
        <div class="p-2.5 rounded-xl bg-slate-950 border border-slate-800">
          <div class="font-bold text-rose-300">SECA SAS (Filiale POMA)</div>
          <div class="text-[11px] text-slate-400 font-mono">SIREN 941 124 505 • Cap. 10 000 €</div>
          <div class="text-[10px] text-slate-500">Société coquille d'exploitation</div>
        </div>
        <div class="p-2.5 rounded-xl bg-slate-950 border border-slate-800">
          <div class="font-bold text-white">POMA S.A.S.</div>
          <div class="text-[11px] text-slate-400 font-mono">Contrat CREM Angelo (38,26 M€ travaux)</div>
          <div class="text-[10px] text-emerald-400 font-bold">Rente garantie 23,89 M€ sur 10 ans</div>
        </div>
      </div>
    </div>

    <!-- PÔLE PRIVATE EQUITY -->
    <div class="p-4 rounded-2xl bg-slate-900/90 border border-slate-700 space-y-3">
      <div class="flex items-center justify-between">
        <span class="text-[11px] font-mono font-bold uppercase tracking-wider text-purple-400">💼 PRIVATE EQUITY</span>
        <span class="text-[10px] font-mono px-2 py-0.5 rounded bg-purple-500/10 text-purple-300 border border-purple-500/30">FIP Corse</span>
      </div>
      <div class="space-y-2 text-xs">
        <div class="p-2.5 rounded-xl bg-slate-950 border border-slate-800">
          <div class="font-bold text-purple-300">VATEL CAPITAL SAS</div>
          <div class="text-[11px] text-slate-400">Agrément AMF GP-08000045</div>
          <div class="text-[10px] text-rose-400 font-mono">Sanction AMF TRA-2022-04</div>
        </div>
        <div class="p-2.5 rounded-xl bg-slate-950 border border-slate-800">
          <div class="font-bold text-white">SAS Ajaccio Aventure</div>
          <div class="text-[11px] text-slate-400 font-mono">Ticket Vatel : 3,3 M€</div>
          <div class="text-[10px] text-red-400 font-bold">Liquidation judiciaire 08/09/2025</div>
        </div>
        <div class="p-2.5 rounded-xl bg-red-950/30 border border-red-500/40">
          <div class="font-bold text-red-300">Friche Militaire St-Joseph</div>
          <div class="text-[10px] text-slate-300">7,87 ha pollués par hydrocarbures/pyrotechnie</div>
        </div>
      </div>
    </div>

  </div>

  <!-- BANDEAU DES INTERACTIONS CONTRACTUELLES -->
  <div class="p-4 rounded-2xl bg-slate-900/80 border border-slate-800 text-xs font-mono space-y-2">
    <div class="text-amber-400 font-bold uppercase text-[11px]">FLUX FINANCIERS ET LIAISONS CONTRACTUELLES OBSERVÉES :</div>
    <div class="grid grid-cols-1 md:grid-cols-2 gap-2 text-slate-300 text-[11px]">
      <div class="flex items-center gap-2">
        <span class="text-amber-400">➔</span> CAPA concède l'aménagement à SPL Ametarra (Miséricorde & Citadelle).
      </div>
      <div class="flex items-center gap-2">
        <span class="text-rose-400">➔</span> CAPA verse la rente garantie CREM 2022c002 à SECA / POMA.
      </div>
      <div class="flex items-center gap-2">
        <span class="text-red-400">➔</span> SPL Muvitarra collecte la billetterie sans rémunération pour POMA (Annexe 16).
      </div>
      <div class="flex items-center gap-2">
        <span class="text-purple-400">➔</span> Vatel Capital injecte 3,3 M€ dans Ajaccio Aventure sur la friche polluée A 113.
      </div>
    </div>
  </div>
</div>
"""

# ==============================================================================
# 2. PLAN DE TRANSITION DES MARCHÉS SCOLAIRES (Remplace le graph TD brut)
# ==============================================================================
html_plan_transition = """
<div class="my-8 p-6 md:p-8 rounded-3xl border border-emerald-500/40 bg-slate-950 shadow-2xl space-y-6">
  <div class="flex items-center justify-between border-b border-slate-800 pb-4">
    <div class="flex items-center gap-2.5">
      <span class="w-3.5 h-3.5 rounded-full bg-emerald-400"></span>
      <span class="text-xs font-mono font-bold uppercase tracking-wider text-emerald-400">PLAN DE TRANSITION OPÉRATIONNELLE • CONVERSION EN LIGNES RÉGULIÈRES MIXTES (LRM)</span>
    </div>
    <span class="text-[11px] font-mono text-slate-400">Application Art. R. 3111-5 Code des transports</span>
  </div>

  <div class="grid grid-cols-1 md:grid-cols-5 gap-3 relative">
    
    <!-- ÉTAPE 1 -->
    <div class="p-4 rounded-2xl bg-rose-950/20 border border-rose-500/40 flex flex-col justify-between space-y-3">
      <div>
        <div class="text-[10px] font-mono uppercase tracking-wider text-rose-400 font-bold mb-1">Situation Actuelle</div>
        <div class="text-sm font-bold text-white">6 Marchés Privés Captifs</div>
        <div class="text-xs text-rose-300 font-mono mt-1">2,84 M€ TTC / an</div>
      </div>
      <div class="text-[11px] text-slate-400 font-sans">
        Facturation exorbitante à 7,57 €/km, bus scolaires vides en journée.
      </div>
    </div>

    <!-- FLECHE 1 -->
    <div class="hidden md:flex items-center justify-center text-slate-600 font-bold text-xl">➔</div>

    <!-- ÉTAPE 2 -->
    <div class="p-4 rounded-2xl bg-cyan-950/20 border border-cyan-500/40 flex flex-col justify-between space-y-3">
      <div>
        <div class="text-[10px] font-mono uppercase tracking-wider text-cyan-400 font-bold mb-1">Levier Juridique</div>
        <div class="text-sm font-bold text-white">Reprise en Régie SPL</div>
        <div class="text-xs text-cyan-300 font-mono mt-1">Quasi-régie In-House</div>
      </div>
      <div class="text-[11px] text-slate-400 font-sans">
        Extinction des contrats privés, reprise sociale des 14 chauffeurs en CDI.
      </div>
    </div>

    <!-- FLECHE 2 -->
    <div class="hidden md:flex items-center justify-center text-slate-600 font-bold text-xl">➔</div>

    <!-- ÉTAPE 3 -->
    <div class="p-4 rounded-2xl bg-emerald-950/30 border border-emerald-500/50 flex flex-col justify-between space-y-3 md:col-span-1">
      <div>
        <div class="text-[10px] font-mono uppercase tracking-wider text-emerald-400 font-bold mb-1">Réseau Unifié LRM</div>
        <div class="text-sm font-bold text-white">Lignes Mixtes Tout Public</div>
        <div class="text-xs text-emerald-300 font-mono mt-1">Économie +1,40 M€ HT/an</div>
      </div>
      <div class="text-[11px] text-slate-400 font-sans">
        Désenclavement des 9 communes périurbaines et ouverture des bus à tous les usagers.
      </div>
    </div>

  </div>

  <!-- IMPACT DOUBLE LEVIER -->
  <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 pt-2">
    <div class="p-4 rounded-2xl bg-slate-900 border border-slate-800 flex items-start gap-3">
      <div class="p-2 rounded-xl bg-emerald-500/10 text-emerald-400 border border-emerald-500/30 shrink-0 text-lg">💰</div>
      <div>
        <div class="text-xs font-mono font-bold uppercase text-emerald-400">Économie Budgétaire Nette</div>
        <div class="text-lg font-mono font-bold text-white">+ 1 401 818 € HT / an (+1,54 M€ TTC)</div>
        <div class="text-xs text-slate-400">Recouvrement direct pour financer le réseau général de la CAPA.</div>
      </div>
    </div>

    <div class="p-4 rounded-2xl bg-slate-900 border border-slate-800 flex items-start gap-3">
      <div class="p-2 rounded-xl bg-cyan-500/10 text-cyan-400 border border-cyan-500/30 shrink-0 text-lg">🚍</div>
      <div>
        <div class="text-xs font-mono font-bold uppercase text-cyan-400">Désenclavement & Sauvegarde Sociale</div>
        <div class="text-lg font-mono font-bold text-white">9 Villages Desservis • 14 CDI 35h</div>
        <div class="text-xs text-slate-400">Sécurisation des emplois des conducteurs locaux sous l'accord de branche.</div>
      </div>
    </div>
  </div>
</div>
"""

# ==============================================================================
# 3. CHRONOGRAMME COMPARATIF GANTT PENDULAIRE (Remplace le gantt brut)
# ==============================================================================
html_chronogramme_gantt = """
<div class="my-8 p-6 md:p-8 rounded-3xl border border-indigo-500/40 bg-slate-950 shadow-2xl space-y-6">
  <div class="flex items-center justify-between border-b border-slate-800 pb-4">
    <div class="flex items-center gap-2.5">
      <span class="w-3.5 h-3.5 rounded-full bg-indigo-400"></span>
      <span class="text-xs font-mono font-bold uppercase tracking-wider text-indigo-400">CHRONOGRAMME COMPARATIF • TRAJET MATINAL PENDULAIRE (MEZZANA ➔ GARE PORT D'AJACCIO)</span>
    </div>
    <span class="text-[11px] font-mono text-slate-400">Mesure des ruptures de charge</span>
  </div>

  <div class="space-y-6">
    
    <!-- OPTION B : L'OCHJU (LIAISON DIRECTE) -->
    <div class="p-5 rounded-2xl bg-emerald-950/20 border border-emerald-500/40 space-y-3">
      <div class="flex items-center justify-between">
        <div class="flex items-center gap-2">
          <span class="px-2.5 py-0.5 rounded-full bg-emerald-500/20 text-emerald-400 border border-emerald-500/40 text-xs font-mono font-bold">OPTION B • CITOYENNE L'OCHJU</span>
          <span class="text-xs font-bold text-white">Maintien Gare Centrale + Halte Saint-Joseph</span>
        </div>
        <span class="text-sm font-mono font-bold text-emerald-400">14 min chrono (Zéro rupture)</span>
      </div>

      <!-- BARRE DE TEMPS OPTION B -->
      <div class="w-full bg-slate-900 rounded-xl p-1 flex gap-1 h-9 items-center">
        <!-- 0-8 min : Train Mezzana -> Saint-Joseph -->
        <div class="bg-emerald-600 h-full rounded-lg flex items-center justify-center text-[11px] font-mono font-bold text-white px-2 transition" style="width: 57%;">
          Train Mezzana ➔ St-Joseph (8 min)
        </div>
        <!-- 8-9 min : Arrêt Halte 45s -->
        <div class="bg-amber-500 h-full rounded-lg flex items-center justify-center text-[10px] font-mono font-bold text-slate-950 px-1" style="width: 7%;">
          Halte 45s
        </div>
        <!-- 9-14 min : Train direct Gare Centrale -->
        <div class="bg-emerald-500 h-full rounded-lg flex items-center justify-center text-[11px] font-mono font-bold text-white px-2" style="width: 36%;">
          Train ➔ Gare Centrale Port (5 min)
        </div>
      </div>
      <div class="flex justify-between text-[10px] font-mono text-slate-400">
        <span>0 min (Départ)</span>
        <span>8 min (Saint-Joseph)</span>
        <span>14 min (Arrivée Quai Campinchi)</span>
      </div>
    </div>

    <!-- OPTION A : MAIRIE SBRAGGIA (TERMINUS ASPRETTO) -->
    <div class="p-5 rounded-2xl bg-rose-950/20 border border-rose-500/40 space-y-3">
      <div class="flex items-center justify-between">
        <div class="flex items-center gap-2">
          <span class="px-2.5 py-0.5 rounded-full bg-rose-500/20 text-rose-400 border border-rose-500/40 text-xs font-mono font-bold">OPTION A • PROJET MAIRIE SBRAGGIA</span>
          <span class="text-xs font-bold text-white">Déplacement forcé du Terminus à Aspretto</span>
        </div>
        <span class="text-sm font-mono font-bold text-rose-400">35 à 45 min (Rupture & Bouchons)</span>
      </div>

      <!-- BARRE DE TEMPS OPTION A -->
      <div class="w-full bg-slate-900 rounded-xl p-1 flex gap-1 h-9 items-center">
        <!-- 0-8 min : Train Mezzana -> Aspretto -->
        <div class="bg-slate-700 h-full rounded-lg flex items-center justify-center text-[10px] font-mono text-slate-300 px-2" style="width: 23%;">
          Train ➔ Aspretto (8 min)
        </div>
        <!-- 8-12 min : Débarquement forcé -->
        <div class="bg-rose-700 h-full rounded-lg flex items-center justify-center text-[9px] font-mono font-bold text-white px-1 text-center" style="width: 12%;">
          Débarquement (4 min)
        </div>
        <!-- 12-20 min : Attente bus/navette -->
        <div class="bg-red-600 h-full rounded-lg flex items-center justify-center text-[10px] font-mono font-bold text-white px-1 text-center" style="width: 23%;">
          Attente Navette (8 min)
        </div>
        <!-- 20-35 min : Bouchons Rocade -->
        <div class="bg-rose-900 h-full rounded-lg flex items-center justify-center text-[10px] font-mono text-rose-200 px-2 text-center" style="width: 42%;">
          Bus bloqué dans les bouchons (15-25 min)
        </div>
      </div>
      <div class="flex justify-between text-[10px] font-mono text-slate-400">
        <span>0 min (Départ)</span>
        <span>12 min (Rupture)</span>
        <span>35 min+ (Arrivée retardée)</span>
      </div>
    </div>

  </div>

  <div class="p-3.5 rounded-xl bg-slate-900/60 border border-slate-800 text-xs text-slate-300 flex items-center gap-2.5">
    <span class="text-amber-400 font-bold">Verdict d'Aménagement :</span>
    <span>L'Option B citoyenne divise par 2,5 le temps de trajet des salariés pendulaires et supprime 100% de la rupture de charge.</span>
  </div>
</div>
"""

# ==============================================================================
# REMPLACEMENT DANS LE FICHIER ASTRO
# ==============================================================================

# Remplacement 1 : Le flowchart TD (Bloc 1)
p1 = re.compile(r'<pre><code class="language-mermaid">flowchart TD.*?</code></pre>', re.DOTALL)
text = p1.sub(html_organigramme, text, count=1)

# Remplacement 2 : Le graph TD (Bloc 2)
p2 = re.compile(r'<pre><code class="language-mermaid">graph TD.*?</code></pre>', re.DOTALL)
text = p2.sub(html_plan_transition, text, count=1)

# Remplacement 3 : Le gantt (Bloc 3)
p3 = re.compile(r'<pre><code class="language-mermaid">gantt.*?</code></pre>', re.DOTALL)
text = p3.sub(html_chronogramme_gantt, text, count=1)

with open(astro_path, "w", encoding="utf-8") as f:
    f.write(text)

print("Succès : Les 3 blocs bruts Mermaid/Gantt ont été remplacés par des infographies interactives et chronogrammes haute fidélité !")

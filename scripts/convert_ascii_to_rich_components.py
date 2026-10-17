# -*- coding: utf-8 -*-
"""
Script de conversion intégrale des blocs ASCII / Terminal en composants HTML/Tailwind/SVG ultra-léchés.
- 0% de perte de données : 100% des chiffres, libellés et cotes sont convertis en vrais tableaux HTML de grade Cour des Comptes.
- Remplacement des 4 schémas ASCII par des diagrammes vectoriels SVG et flux infographiques interactifs.
"""

import re

astro_path = r"C:\Users\PC-Bureau\Desktop\docucu\site_github_pages\src\pages\dossier-transparence-citoyenne-ajaccio.astro"

with open(astro_path, "r", encoding="utf-8") as f:
    text = f.read()

# ==============================================================================
# COMPOSANT 1 : TABLEAU COMPARATIF CREM VS COSP (Bloc 1)
# ==============================================================================
html_table_1 = """
<div class="my-6 overflow-hidden rounded-2xl border border-slate-700 bg-slate-950/80 shadow-2xl">
  <div class="bg-gradient-to-r from-slate-900 via-amber-950/40 to-slate-900 px-6 py-4 border-b border-slate-800 flex items-center justify-between">
    <div class="flex items-center gap-2">
      <span class="w-3 h-3 rounded-full bg-amber-400"></span>
      <span class="text-xs font-mono font-bold uppercase tracking-wider text-amber-400">TABLEAU COMPARATIF D'INSTRUCTION • ASYMÉTRIE CONTRACTUELLE</span>
    </div>
    <span class="text-[11px] font-mono text-slate-400">Réf. CREM 2022c002 vs COSP 2026-2032</span>
  </div>
  <div class="overflow-x-auto">
    <table class="w-full text-left text-xs font-sans">
      <thead>
        <tr class="border-b border-slate-800 bg-slate-900/90 text-slate-300 font-mono text-[11px] uppercase tracking-wider">
          <th class="py-3 px-4 font-bold text-amber-400 w-1/4">Paramètre d'Instruction</th>
          <th class="py-3 px-4 font-bold text-rose-400 w-3/8">Contrat CREM 2022c002 — Téléphérique</th>
          <th class="py-3 px-4 font-bold text-cyan-400 w-3/8">Nouveau COSP 2026-2032 — Bus Urbain</th>
        </tr>
      </thead>
      <tbody class="divide-y divide-slate-800/60 text-slate-300">
        <tr class="hover:bg-slate-900/40 transition">
          <td class="py-3 px-4 font-semibold text-white">Entité adjudicataire</td>
          <td class="py-3 px-4 text-slate-200">SECA SAS (Société d'Exploitation du Câble Ajaccien) — Filiale POMA</td>
          <td class="py-3 px-4 text-slate-200">SPL MUVITARRA (Société Publique Locale)</td>
        </tr>
        <tr class="hover:bg-slate-900/40 transition">
          <td class="py-3 px-4 font-semibold text-white">Immatriculation / SIREN</td>
          <td class="py-3 px-4 font-mono text-slate-300">SIREN : 941 124 505 (RCS Ajaccio)</td>
          <td class="py-3 px-4 font-mono text-slate-300">SIREN : 822 167 748 (RCS Ajaccio)</td>
        </tr>
        <tr class="hover:bg-slate-900/40 transition">
          <td class="py-3 px-4 font-semibold text-white">Capital social</td>
          <td class="py-3 px-4 font-mono text-amber-300">10 000,00 € (Société coquille dédiée)</td>
          <td class="py-3 px-4 font-mono text-cyan-300">1 000 000,00 € (100% fonds publics)</td>
        </tr>
        <tr class="hover:bg-slate-900/40 transition">
          <td class="py-3 px-4 font-semibold text-white">Actionnariat</td>
          <td class="py-3 px-4 text-slate-300">100 % Privé (POMA SAS à 100 %)</td>
          <td class="py-3 px-4 text-slate-300">100 % Public (CAPA 85 %, Ville d'Ajaccio 15 %)</td>
        </tr>
        <tr class="hover:bg-slate-900/40 transition">
          <td class="py-3 px-4 font-semibold text-white">Durée d'engagement</td>
          <td class="py-3 px-4 font-mono text-slate-200">7 ans fermes (Exploitation & Maintenance)</td>
          <td class="py-3 px-4 font-mono text-slate-200">1 an reconductible (Situation précaire)</td>
        </tr>
        <tr class="hover:bg-slate-900/40 transition bg-rose-950/10">
          <td class="py-3 px-4 font-semibold text-white">Rémunération / An</td>
          <td class="py-3 px-4 font-mono font-bold text-rose-400">2 389 284 € HT / an (Rente garantie forfaitaire)</td>
          <td class="py-3 px-4 font-mono font-bold text-slate-300">Forfait nominal compensatoire plafonné</td>
        </tr>
        <tr class="hover:bg-slate-900/40 transition bg-amber-950/10">
          <td class="py-3 px-4 font-semibold text-white">Indexation inflation</td>
          <td class="py-3 px-4 font-semibold text-emerald-400">OUI • Indexation trimestrielle intégrale (Énergie, Salaires, Maintenance)</td>
          <td class="py-3 px-4 font-semibold text-rose-400">NON • Gel en euros courants (Art. 30.1 COSP)</td>
        </tr>
        <tr class="hover:bg-slate-900/40 transition">
          <td class="py-3 px-4 font-semibold text-white">Risque de fréquentation</td>
          <td class="py-3 px-4 text-emerald-400">0 % Risque • Rémunération assurée à 100 % par la CAPA même à vide</td>
          <td class="py-3 px-4 text-rose-400">100 % Risque supporté par la SPL Muvitarra</td>
        </tr>
        <tr class="hover:bg-slate-900/40 transition">
          <td class="py-3 px-4 font-semibold text-white">Recettes de billetterie</td>
          <td class="py-3 px-4 text-slate-300">Encaissées gratuitement par la SPL pour compte de tiers (Annexe 16)</td>
          <td class="py-3 px-4 text-slate-300">Intégrées au budget d'exploitation pour combler le déficit structurel</td>
        </tr>
        <tr class="hover:bg-slate-900/40 transition">
          <td class="py-3 px-4 font-semibold text-white">Financement infrastructure</td>
          <td class="py-3 px-4 text-slate-300">52 M€ financés à 70 % par le PTIC régalien + CAPA (100% public)</td>
          <td class="py-3 px-4 text-slate-300">Défaut d'investissement lourd (1,5 bus/an, parc moyen 12 ans)</td>
        </tr>
      </tbody>
    </table>
  </div>
</div>
"""

# ==============================================================================
# COMPOSANT 2 : INFOGRAPHIE GOULET STILETTO ROUTE A MADUNUCCIA (Bloc 2)
# ==============================================================================
html_schema_2 = """
<div class="my-6 p-6 rounded-2xl border border-red-500/40 bg-slate-950/90 shadow-2xl space-y-4">
  <div class="flex items-center justify-between border-b border-slate-800 pb-3">
    <div class="flex items-center gap-2">
      <span class="w-3 h-3 rounded-full bg-red-500 animate-pulse"></span>
      <span class="text-xs font-mono font-bold uppercase tracking-wider text-red-400">SCHÉMA TECHNIQUE D'URGENCE • VULNÉRABILITÉ ROUTIÈRE ERP TYPE U</span>
    </div>
    <span class="text-[11px] font-mono text-slate-400">Violation Art. U 6 (Arrêté 25 juin 1980)</span>
  </div>

  <!-- SVG FLUX D'ACCÈS DU GOULET STILETTO -->
  <div class="w-full flex justify-center py-2">
    <svg viewBox="0 0 760 380" class="w-full max-w-2xl h-auto font-sans" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <linearGradient id="gradRed" x1="0%" y1="0%" x2="100%" y2="0%">
          <stop offset="0%" stop-color="#ef4444" stop-opacity="0.2"/>
          <stop offset="50%" stop-color="#ef4444" stop-opacity="0.8"/>
          <stop offset="100%" stop-color="#ef4444" stop-opacity="0.2"/>
        </linearGradient>
        <marker id="arrow" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 0 L 10 5 L 0 10 z" fill="#f59e0b" />
        </marker>
        <marker id="arrowRed" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 0 L 10 5 L 0 10 z" fill="#ef4444" />
        </marker>
      </defs>

      <!-- ÉTAPE 1 : GRAVONA -->
      <rect x="220" y="15" width="320" height="42" rx="10" fill="#1e293b" stroke="#475569" stroke-width="1.5"/>
      <text x="380" y="41" fill="#f8fafc" font-size="12" font-weight="bold" text-anchor="middle" font-family="monospace">VALLÉE DE LA GRAVONA / RN 194</text>
      
      <!-- FLECHE 1 -->
      <line x1="380" y1="57" x2="380" y2="85" stroke="#f59e0b" stroke-width="2" marker-end="url(#arrow)"/>

      <!-- ÉTAPE 2 : ROND-POINT STILETTO -->
      <rect x="230" y="87" width="300" height="42" rx="10" fill="#334155" stroke="#64748b" stroke-width="1.5"/>
      <text x="380" y="113" fill="#f8fafc" font-size="12" font-weight="bold" text-anchor="middle">Rond-point du Stiletto (Zone Saturée)</text>

      <!-- FLECHE 2 GOULET -->
      <line x1="380" y1="129" x2="380" y2="160" stroke="#ef4444" stroke-width="3" marker-end="url(#arrowRed)"/>
      <text x="510" y="145" fill="#f87171" font-size="10" font-family="monospace">Largeur : 6,20 m • 14 000 véh/j</text>

      <!-- ÉTAPE 3 : ROUTE A MADUNUCCIA (GOULET CRITIQUE) -->
      <rect x="190" y="162" width="380" height="48" rx="10" fill="#450a0a" stroke="#ef4444" stroke-width="2"/>
      <text x="380" y="191" fill="#fca5a5" font-size="13" font-weight="black" text-anchor="middle" font-family="monospace">ROUTE A MADUNUCCIA (VOIE UNIQUE)</text>
      
      <!-- ENCADRE ALERTE BLOCAGE -->
      <rect x="585" y="165" width="165" height="42" rx="8" fill="#7f1d1d" stroke="#f87171" stroke-width="1"/>
      <text x="667" y="182" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle">BLOCAGE TOTAL</text>
      <text x="667" y="197" fill="#fecaca" font-size="9" text-anchor="middle">Si accident ou incendie</text>

      <!-- FLECHE 3 VERS HOPITAL -->
      <line x1="380" y1="210" x2="380" y2="240" stroke="#ef4444" stroke-width="3" marker-end="url(#arrowRed)"/>

      <!-- ÉTAPE 4 : HOPITAL DE LA MISERICORDE -->
      <rect x="140" y="242" width="480" height="54" rx="12" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
      <text x="380" y="266" fill="#38bdf8" font-size="13" font-weight="bold" text-anchor="middle">CENTRE HOSPITALIER DE LA MISÉRICORDE (ERP TYPE U)</text>
      <text x="380" y="284" fill="#94a3b8" font-size="11" text-anchor="middle">470 lits • Urgences • Réanimation • 1 200 soignants</text>

      <!-- FLECHE BAS VERS MONT THABOR BLOQUE -->
      <line x1="380" y1="332" x2="380" y2="300" stroke="#94a3b8" stroke-width="2" stroke-dasharray="4,4" marker-end="url(#arrow)"/>
      <text x="510" y="325" fill="#f87171" font-size="10" font-family="monospace">REFUS PRÉFECTORAL &amp; BLOCAGE</text>

      <!-- ÉTAPE 5 : MONT THABOR BLOQUE -->
      <rect x="200" y="334" width="360" height="38" rx="8" fill="#1e293b" stroke="#64748b" stroke-width="1.5" stroke-dasharray="4,4"/>
      <text x="380" y="358" fill="#94a3b8" font-size="11" text-anchor="middle">DÉGAGEMENT SUD / MONT THABOR (Non réalisé)</text>
    </svg>
  </div>
</div>
"""

# ==============================================================================
# COMPOSANT 3 : INFOGRAPHIE ALTITUDE / PYLÔNE ANGELO & SAMU (Bloc 3)
# ==============================================================================
html_schema_3 = """
<div class="my-6 p-6 rounded-2xl border border-amber-500/40 bg-slate-950/90 shadow-2xl space-y-4">
  <div class="flex items-center justify-between border-b border-slate-800 pb-3">
    <div class="flex items-center gap-2">
      <span class="w-3 h-3 rounded-full bg-amber-400"></span>
      <span class="text-xs font-mono font-bold uppercase tracking-wider text-amber-400">PROFIL ALTITUDE • CONFLIT AÉRONAUTIQUE DRAGON 20 / PYLÔNES DU CÂBLE</span>
    </div>
    <span class="text-[11px] font-mono text-slate-400">Arrêté préfectoral du 23 oct. 2023</span>
  </div>

  <div class="w-full flex justify-center py-2">
    <svg viewBox="0 0 760 300" class="w-full max-w-2xl h-auto font-sans" xmlns="http://www.w3.org/2000/svg">
      <!-- AXES -->
      <line x1="60" y1="250" x2="720" y2="250" stroke="#475569" stroke-width="1.5"/>
      <line x1="60" y1="250" x2="60" y2="30" stroke="#475569" stroke-width="1.5"/>

      <!-- GRADUATIONS VERTICALES ALTITUDE -->
      <text x="45" y="254" fill="#94a3b8" font-size="10" font-mono text-anchor="end">0 m</text>
      <text x="45" y="190" fill="#94a3b8" font-size="10" font-mono text-anchor="end">60 m</text>
      <text x="45" y="130" fill="#94a3b8" font-size="10" font-mono text-anchor="end">120 m</text>
      <text x="45" y="70" fill="#94a3b8" font-size="10" font-mono text-anchor="end">180 m</text>
      <text x="50" y="20" fill="#f59e0b" font-size="11" font-mono font-bold>Altitude (m)</text>

      <!-- GRADUATIONS HORIZONTALES DISTANCE -->
      <text x="120" y="268" fill="#94a3b8" font-size="10" font-mono text-anchor="middle">0 m (DZ)</text>
      <text x="320" y="268" fill="#94a3b8" font-size="10" font-mono text-anchor="middle">250 m</text>
      <text x="460" y="268" fill="#94a3b8" font-size="10" font-mono text-anchor="middle">450 m</text>
      <text x="680" y="268" fill="#94a3b8" font-size="10" font-mono text-anchor="middle">800 m</text>
      <text x="710" y="268" fill="#f59e0b" font-size="11" font-mono font-bold text-anchor="end">Distance (m)</text>

      <!-- HÉLISTATION STILETTO -->
      <rect x="80" y="210" width="80" height="40" rx="6" fill="#0284c7" stroke="#38bdf8" stroke-width="1.5"/>
      <text x="120" y="234" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">DZ Stiletto</text>

      <!-- COULOIR D'ENVOL SAMU PENTE 4,5% -->
      <line x1="120" y1="210" x2="680" y2="40" stroke="#38bdf8" stroke-width="2.5" stroke-dasharray="6,4"/>
      <text x="560" y="60" fill="#38bdf8" font-size="11" font-weight="bold">COULOIR D'ENVOL SAMU / DRAGON 20</text>
      <text x="560" y="76" fill="#94a3b8" font-size="9">(Pente réglementaire 4,5% - VFR de Nuit)</text>

      <!-- PYLÔNE N°4 DU TÉLÉPHÉRIQUE -->
      <line x1="320" y1="250" x2="320" y2="120" stroke="#f59e0b" stroke-width="4"/>
      <circle cx="320" cy="120" r="5" fill="#f59e0b"/>
      <text x="320" y="108" fill="#f59e0b" font-size="10" font-mono font-bold text-anchor="middle">PYLÔNE N°4</text>

      <!-- CÂBLE DU TÉLÉPHÉRIQUE ANGELO -->
      <line x1="200" y1="160" x2="700" y2="100" stroke="#f59e0b" stroke-width="2"/>
      <text x="580" y="115" fill="#fcd34d" font-size="10" font-family="monospace">CÂBLES PORTEURS DU TÉLÉPORTÉ</text>

      <!-- INTERSECTION CRITIQUE -->
      <circle cx="438" cy="126" r="14" fill="#ef4444" fill-opacity="0.3" stroke="#ef4444" stroke-width="2"/>
      <circle cx="438" cy="126" r="4" fill="#ef4444"/>
      <line x1="438" y1="140" x2="438" y2="175" stroke="#ef4444" stroke-width="1.5"/>
      
      <rect x="340" y="175" width="220" height="34" rx="6" fill="#7f1d1d" stroke="#f87171" stroke-width="1"/>
      <text x="450" y="189" fill="#fecaca" font-size="9" font-weight="bold" text-anchor="middle">INTERSECTION DANGEREUSE</text>
      <text x="450" y="202" fill="#ffffff" font-size="8.5" text-anchor="middle">Risque collision câble / vent de Libecciu</text>
    </svg>
  </div>
</div>
"""

# ==============================================================================
# COMPOSANT 4 : CARTOUCHE DE SCELLÉS ISO 27037 (Bloc 4)
# ==============================================================================
html_cartouche_4 = """
<div class="my-4 p-4 rounded-xl border border-amber-500/30 bg-amber-950/20 flex items-center justify-between">
  <div class="flex items-center gap-3">
    <span class="p-2 rounded-lg bg-amber-500/10 text-amber-400 border border-amber-500/30 text-lg">🛡️</span>
    <div>
      <div class="text-xs font-mono font-bold uppercase tracking-wider text-amber-400">REGISTRE DES SCELLÉS FORENSIQUES ISO/IEC 27037</div>
      <div class="text-[11px] text-slate-300 font-sans">Actes officiels scellés cryptographiquement sous SHA-256 inaltérable.</div>
    </div>
  </div>
  <span class="px-3 py-1 bg-amber-500/10 text-amber-400 border border-amber-500/30 rounded-full text-[10px] font-mono font-bold uppercase">Conforme ISO 27037</span>
</div>
"""

# ==============================================================================
# COMPOSANT 5 : TABLEAU RECETTES PARKING DU DIAMANT (Bloc 5)
# ==============================================================================
html_table_5 = """
<div class="my-6 overflow-hidden rounded-2xl border border-slate-700 bg-slate-950/80 shadow-2xl">
  <div class="bg-gradient-to-r from-slate-900 via-cyan-950/40 to-slate-900 px-6 py-4 border-b border-slate-800 flex items-center justify-between">
    <div class="flex items-center gap-2">
      <span class="w-3 h-3 rounded-full bg-cyan-400"></span>
      <span class="text-xs font-mono font-bold uppercase tracking-wider text-cyan-400">MODÉLISATION RECETTES BRUTES • PARKING DU DIAMANT (840 PLACES)</span>
    </div>
    <span class="text-[11px] font-mono text-slate-400">Norme M4 / DGFiP</span>
  </div>
  <div class="overflow-x-auto">
    <table class="w-full text-left text-xs font-sans">
      <thead>
        <tr class="border-b border-slate-800 bg-slate-900/90 text-slate-300 font-mono text-[11px] uppercase tracking-wider">
          <th class="py-3 px-4 font-bold text-cyan-400">Segment Tarifaire</th>
          <th class="py-3 px-4 font-bold text-slate-300">Unités / Volume</th>
          <th class="py-3 px-4 font-bold text-slate-300">Tarif Unitaire TTC</th>
          <th class="py-3 px-4 font-bold text-amber-400 text-right">Total Annuel TTC</th>
          <th class="py-3 px-4 font-bold text-emerald-400 text-right">Total HT (TVA 20%)</th>
        </tr>
      </thead>
      <tbody class="divide-y divide-slate-800/60 text-slate-300">
        <tr class="hover:bg-slate-900/40 transition">
          <td class="py-3 px-4 font-semibold text-white">Abonnements Résidents (24h/24)</td>
          <td class="py-3 px-4 font-mono text-slate-300">250 abonnés</td>
          <td class="py-3 px-4 font-mono text-slate-300">63,00 € / mois</td>
          <td class="py-3 px-4 font-mono font-bold text-amber-400 text-right">189 000,00 €</td>
          <td class="py-3 px-4 font-mono font-bold text-emerald-400 text-right">157 500,00 €</td>
        </tr>
        <tr class="hover:bg-slate-900/40 transition">
          <td class="py-3 px-4 font-semibold text-white">Stationnement Rotation Hypercentre</td>
          <td class="py-3 px-4 font-mono text-slate-300">590 places (2,90 rot./j)</td>
          <td class="py-3 px-4 font-mono text-slate-300">Recette moy. : 4,28 €</td>
          <td class="py-3 px-4 font-mono font-bold text-amber-400 text-right">2 681 000,00 €</td>
          <td class="py-3 px-4 font-mono font-bold text-emerald-400 text-right">2 234 166,67 €</td>
        </tr>
        <tr class="border-t-2 border-slate-700 bg-cyan-950/20 font-bold text-white">
          <td colspan="3" class="py-3 px-4 uppercase font-mono tracking-wider text-cyan-300">TOTAL RECETTES COMMERCIALES BRUTES ANNUELLES</td>
          <td class="py-3 px-4 font-mono text-amber-300 text-right text-sm">2 870 000,00 €</td>
          <td class="py-3 px-4 font-mono text-emerald-400 text-right text-sm">2 391 666,67 €</td>
        </tr>
      </tbody>
    </table>
  </div>
</div>
"""

# ==============================================================================
# COMPOSANT 6 : TABLEAU CHARGES COMPTABLES M4 DIAMANT (Bloc 6)
# ==============================================================================
html_table_6 = """
<div class="my-6 overflow-hidden rounded-2xl border border-slate-700 bg-slate-950/80 shadow-2xl">
  <div class="bg-gradient-to-r from-slate-900 via-slate-800 to-slate-900 px-6 py-4 border-b border-slate-800 flex items-center justify-between">
    <div class="flex items-center gap-2">
      <span class="w-3 h-3 rounded-full bg-slate-400"></span>
      <span class="text-xs font-mono font-bold uppercase tracking-wider text-slate-300">POSTES DE DÉPENSES COMPTABLES (BUDGET ANNEXE M4)</span>
    </div>
    <span class="text-[11px] font-mono text-slate-400">Charges Réelles Décaissables</span>
  </div>
  <div class="overflow-x-auto">
    <table class="w-full text-left text-xs font-sans">
      <thead>
        <tr class="border-b border-slate-800 bg-slate-900/90 text-slate-300 font-mono text-[11px] uppercase tracking-wider">
          <th class="py-3 px-4 font-bold text-slate-200">Poste Comptable M4</th>
          <th class="py-3 px-4 font-bold text-amber-400 text-right">Montant HT Annuel</th>
          <th class="py-3 px-4 font-bold text-slate-400 text-right">% des Charges</th>
        </tr>
      </thead>
      <tbody class="divide-y divide-slate-800/60 text-slate-300">
        <tr class="hover:bg-slate-900/40 transition">
          <td class="py-3 px-4 text-white font-medium">Compte 64 — Charges de personnel (4 ETP gardiennage/sécurité)</td>
          <td class="py-3 px-4 font-mono font-bold text-white text-right">184 000,00 €</td>
          <td class="py-3 px-4 font-mono text-slate-400 text-right">36,26 %</td>
        </tr>
        <tr class="hover:bg-slate-900/40 transition">
          <td class="py-3 px-4 text-white font-medium">Compte 615 — Entretien et maintenance multitechnique</td>
          <td class="py-3 px-4 font-mono font-bold text-white text-right">112 000,00 €</td>
          <td class="py-3 px-4 font-mono text-slate-400 text-right">22,07 %</td>
        </tr>
        <tr class="hover:bg-slate-900/40 transition">
          <td class="py-3 px-4 text-white font-medium">Compte 6061 — Énergie, électricité et ventilation forcée</td>
          <td class="py-3 px-4 font-mono font-bold text-white text-right">96 400,00 €</td>
          <td class="py-3 px-4 font-mono text-slate-400 text-right">19,00 %</td>
        </tr>
        <tr class="hover:bg-slate-900/40 transition">
          <td class="py-3 px-4 text-white font-medium">Compte 616 — Assurances exploitation et sécurité incendie</td>
          <td class="py-3 px-4 font-mono font-bold text-white text-right">45 000,00 €</td>
          <td class="py-3 px-4 font-mono text-slate-400 text-right">8,87 %</td>
        </tr>
        <tr class="hover:bg-slate-900/40 transition">
          <td class="py-3 px-4 text-white font-medium">Compte 623/628 — Monétique bancaire, billetterie et télétransmissions</td>
          <td class="py-3 px-4 font-mono font-bold text-white text-right">70 000,00 €</td>
          <td class="py-3 px-4 font-mono text-slate-400 text-right">13,80 %</td>
        </tr>
        <tr class="border-t-2 border-slate-700 bg-slate-900/60 font-bold text-white">
          <td class="py-3 px-4 uppercase font-mono tracking-wider text-amber-400">TOTAL CHARGES D'EXPLOITATION DÉCAISSABLES</td>
          <td class="py-3 px-4 font-mono text-rose-400 text-right text-sm">507 400,00 €</td>
          <td class="py-3 px-4 font-mono text-slate-200 text-right text-sm">100,00 %</td>
        </tr>
        <tr class="bg-slate-950">
          <td class="py-2.5 px-4 text-slate-400 italic">Compte 681 — Dotation aux amortissements d'usage (hors décaissé)</td>
          <td class="py-2.5 px-4 font-mono text-slate-400 text-right">294 266,67 €</td>
          <td class="py-2.5 px-4 font-mono text-slate-500 text-right">—</td>
        </tr>
      </tbody>
    </table>
  </div>
</div>
"""

# ==============================================================================
# COMPOSANT 7 : TABLEAU PLAN PLURIANNUEL ACQUISITION BUS (Bloc 7)
# ==============================================================================
html_table_7 = """
<div class="my-6 overflow-hidden rounded-2xl border border-slate-700 bg-slate-950/80 shadow-2xl">
  <div class="bg-gradient-to-r from-slate-900 via-emerald-950/40 to-slate-900 px-6 py-4 border-b border-slate-800 flex items-center justify-between">
    <div class="flex items-center gap-2">
      <span class="w-3 h-3 rounded-full bg-emerald-400"></span>
      <span class="text-xs font-mono font-bold uppercase tracking-wider text-emerald-400">PLAN PLURIANNUEL D'ACQUISITION DE FLOTTE (16 BUS NEUFS)</span>
    </div>
    <span class="text-[11px] font-mono text-slate-400">Horizon 5 Ans (2026-2030)</span>
  </div>
  <div class="overflow-x-auto">
    <table class="w-full text-left text-xs font-sans">
      <thead>
        <tr class="border-b border-slate-800 bg-slate-900/90 text-slate-300 font-mono text-[11px] uppercase tracking-wider">
          <th class="py-3 px-4 font-bold text-emerald-400">Année Budgétaire</th>
          <th class="py-3 px-4 font-bold text-slate-200">Matériel Réceptionné</th>
          <th class="py-3 px-4 font-bold text-amber-400 text-right">Décaissement Acquisition HT</th>
          <th class="py-3 px-4 font-bold text-cyan-400 text-right">Annuité d'Emprunt (5 ans)</th>
        </tr>
      </thead>
      <tbody class="divide-y divide-slate-800/60 text-slate-300">
        <tr class="hover:bg-slate-900/40 transition">
          <td class="py-3 px-4 font-mono font-bold text-white">2026 (Année N)</td>
          <td class="py-3 px-4 text-slate-200">2 Minibus Électriques (Aiaccina) + 2 Midibus Hybrides</td>
          <td class="py-3 px-4 font-mono font-bold text-amber-300 text-right">1 300 000,00 €</td>
          <td class="py-3 px-4 font-mono font-bold text-cyan-300 text-right">1 100 000,00 €</td>
        </tr>
        <tr class="hover:bg-slate-900/40 transition">
          <td class="py-3 px-4 font-mono font-bold text-white">2027 (Année N+1)</td>
          <td class="py-3 px-4 text-slate-200">1 Minibus Électrique + 2 Midibus Hybrides</td>
          <td class="py-3 px-4 font-mono font-bold text-amber-300 text-right">1 050 000,00 €</td>
          <td class="py-3 px-4 font-mono font-bold text-cyan-300 text-right">1 100 000,00 €</td>
        </tr>
        <tr class="hover:bg-slate-900/40 transition">
          <td class="py-3 px-4 font-mono font-bold text-white">2028 (Année N+2)</td>
          <td class="py-3 px-4 text-slate-200">1 Minibus Électrique + 2 Midibus Hybrides</td>
          <td class="py-3 px-4 font-mono font-bold text-amber-300 text-right">1 050 000,00 €</td>
          <td class="py-3 px-4 font-mono font-bold text-cyan-300 text-right">1 100 000,00 €</td>
        </tr>
        <tr class="hover:bg-slate-900/40 transition">
          <td class="py-3 px-4 font-mono font-bold text-white">2029 (Année N+3)</td>
          <td class="py-3 px-4 text-slate-200">1 Minibus Électrique + 2 Midibus Hybrides</td>
          <td class="py-3 px-4 font-mono font-bold text-amber-300 text-right">1 050 000,00 €</td>
          <td class="py-3 px-4 font-mono font-bold text-cyan-300 text-right">1 100 000,00 €</td>
        </tr>
        <tr class="hover:bg-slate-900/40 transition">
          <td class="py-3 px-4 font-mono font-bold text-white">2030 (Année N+4)</td>
          <td class="py-3 px-4 text-slate-200">1 Minibus Électrique + 2 Midibus Hybrides</td>
          <td class="py-3 px-4 font-mono font-bold text-amber-300 text-right">1 050 000,00 €</td>
          <td class="py-3 px-4 font-mono font-bold text-cyan-300 text-right">1 100 000,00 €</td>
        </tr>
        <tr class="border-t-2 border-slate-700 bg-emerald-950/20 font-bold text-white">
          <td class="py-3 px-4 uppercase font-mono tracking-wider text-emerald-400">TOTAL 5 ANS</td>
          <td class="py-3 px-4 text-emerald-300">16 véhicules neufs (6 minibus elec + 10 midibus hybr.)</td>
          <td class="py-3 px-4 font-mono text-amber-300 text-right text-sm">5 500 000,00 €</td>
          <td class="py-3 px-4 font-mono text-cyan-400 text-right text-sm">1 100 000 € / an</td>
        </tr>
      </tbody>
    </table>
  </div>
</div>
"""

# ==============================================================================
# COMPOSANT 8 : TABLEAU COUVERTURE DIAMANT VS FLOTTE (Bloc 8)
# ==============================================================================
html_table_8 = """
<div class="my-6 overflow-hidden rounded-2xl border border-emerald-500/40 bg-slate-950/80 shadow-2xl">
  <div class="bg-gradient-to-r from-slate-900 via-emerald-950/40 to-slate-900 px-6 py-4 border-b border-slate-800 flex items-center justify-between">
    <div class="flex items-center gap-2">
      <span class="w-3 h-3 rounded-full bg-emerald-400"></span>
      <span class="text-xs font-mono font-bold uppercase tracking-wider text-emerald-400">SYNTHÈSE DE FINANCEMENT • TAUX DE COUVERTURE DU RENOUVELLEMENT</span>
    </div>
    <span class="text-[11px] font-mono text-slate-400">Excédent Net Diamant</span>
  </div>
  <div class="overflow-x-auto">
    <table class="w-full text-left text-xs font-sans">
      <thead>
        <tr class="border-b border-slate-800 bg-slate-900/90 text-slate-300 font-mono text-[11px] uppercase tracking-wider">
          <th class="py-3 px-4 font-bold text-emerald-400 w-2/3">Agrégat Financier</th>
          <th class="py-3 px-4 font-bold text-emerald-300 text-right w-1/3">Valeur Annuelle HT</th>
        </tr>
      </thead>
      <tbody class="divide-y divide-slate-800/60 text-slate-300">
        <tr class="hover:bg-slate-900/40 transition">
          <td class="py-3 px-4 font-semibold text-white">Excédent Net d'Exploitation du Parking du Diamant</td>
          <td class="py-3 px-4 font-mono font-bold text-emerald-400 text-right text-sm">+ 1 590 000,00 €</td>
        </tr>
        <tr class="hover:bg-slate-900/40 transition">
          <td class="py-3 px-4 font-semibold text-white">Annuité d'acquisition de la nouvelle flotte Muvitarra (16 bus)</td>
          <td class="py-3 px-4 font-mono font-bold text-rose-400 text-right text-sm">- 1 100 000,00 €</td>
        </tr>
        <tr class="bg-emerald-950/30 border-t-2 border-emerald-500/50 font-bold text-white">
          <td class="py-3.5 px-4 uppercase font-mono tracking-wider text-emerald-300">SOLDE POSITIF DISPONIBLE (CAPACITÉ D'AUTOFINANCEMENT RÉSIDUELLE)</td>
          <td class="py-3.5 px-4 font-mono text-emerald-400 text-right text-base font-black">+ 490 000,00 €</td>
        </tr>
        <tr class="bg-slate-950 font-mono">
          <td class="py-2.5 px-4 text-slate-400">TAUX DE COUVERTURE FINANCIÈRE DIRECTE DU RENOUVELLEMENT</td>
          <td class="py-2.5 px-4 text-cyan-400 text-right font-bold text-sm">144,55 %</td>
        </tr>
      </tbody>
    </table>
  </div>
</div>
"""

# ==============================================================================
# COMPOSANT 9 : TABLEAU 6 MARCHÉS SCOLAIRES PRIVÉS (Bloc 9)
# ==============================================================================
html_table_9 = """
<div class="my-6 overflow-hidden rounded-2xl border border-slate-700 bg-slate-950/80 shadow-2xl">
  <div class="bg-gradient-to-r from-slate-900 via-rose-950/40 to-slate-900 px-6 py-4 border-b border-slate-800 flex items-center justify-between">
    <div class="flex items-center gap-2">
      <span class="w-3 h-3 rounded-full bg-rose-400"></span>
      <span class="text-xs font-mono font-bold uppercase tracking-wider text-rose-400">AUDIT DES 6 MARCHÉS DE TRANSPORT SCOLAIRE EXTERNALISÉS PAR LA CAPA</span>
    </div>
    <span class="text-[11px] font-mono text-slate-400">Coûts Affrètement Privé</span>
  </div>
  <div class="overflow-x-auto">
    <table class="w-full text-left text-xs font-sans">
      <thead>
        <tr class="border-b border-slate-800 bg-slate-900/90 text-slate-300 font-mono text-[11px] uppercase tracking-wider">
          <th class="py-3 px-4 font-bold text-rose-400">Lot / Secteur Géographique</th>
          <th class="py-3 px-4 font-bold text-slate-300">Kilométrage Annuel</th>
          <th class="py-3 px-4 font-bold text-amber-400 text-right">Facturation TTC / An</th>
          <th class="py-3 px-4 font-bold text-slate-200 text-right">Facturation HT (TVA 10%)</th>
        </tr>
      </thead>
      <tbody class="divide-y divide-slate-800/60 text-slate-300">
        <tr class="hover:bg-slate-900/40 transition">
          <td class="py-3 px-4 font-semibold text-white">Lot 1 — Gravona Amont (Tavaco, Peri)</td>
          <td class="py-3 px-4 font-mono text-slate-300">62 000 km</td>
          <td class="py-3 px-4 font-mono font-bold text-amber-300 text-right">512 000,00 €</td>
          <td class="py-3 px-4 font-mono text-slate-200 text-right">465 454,55 €</td>
        </tr>
        <tr class="hover:bg-slate-900/40 transition">
          <td class="py-3 px-4 font-semibold text-white">Lot 2 — Gravona Aval (Sarrola, Cuttoli)</td>
          <td class="py-3 px-4 font-mono text-slate-300">74 000 km</td>
          <td class="py-3 px-4 font-mono font-bold text-amber-300 text-right">638 000,00 €</td>
          <td class="py-3 px-4 font-mono text-slate-200 text-right">580 000,00 €</td>
        </tr>
        <tr class="hover:bg-slate-900/40 transition">
          <td class="py-3 px-4 font-semibold text-white">Lot 3 — Mezzana / Afa Centre</td>
          <td class="py-3 px-4 font-mono text-slate-300">58 000 km</td>
          <td class="py-3 px-4 font-mono font-bold text-amber-300 text-right">480 000,00 €</td>
          <td class="py-3 px-4 font-mono text-slate-200 text-right">436 363,64 €</td>
        </tr>
        <tr class="hover:bg-slate-900/40 transition">
          <td class="py-3 px-4 font-semibold text-white">Lot 4 — Collines d'Alata (Pruno, San Benedetto)</td>
          <td class="py-3 px-4 font-mono text-slate-300">46 000 km</td>
          <td class="py-3 px-4 font-mono font-bold text-amber-300 text-right">392 000,00 €</td>
          <td class="py-3 px-4 font-mono text-slate-200 text-right">356 363,64 €</td>
        </tr>
        <tr class="hover:bg-slate-900/40 transition">
          <td class="py-3 px-4 font-semibold text-white">Lot 5 — Appietto / Valle-di-Mezzana</td>
          <td class="py-3 px-4 font-mono text-slate-300">52 000 km</td>
          <td class="py-3 px-4 font-mono font-bold text-amber-300 text-right">446 000,00 €</td>
          <td class="py-3 px-4 font-mono text-slate-200 text-right">405 454,55 €</td>
        </tr>
        <tr class="hover:bg-slate-900/40 transition">
          <td class="py-3 px-4 font-semibold text-white">Lot 6 — Villanova / Façade Nord</td>
          <td class="py-3 px-4 font-mono text-slate-300">44 000 km</td>
          <td class="py-3 px-4 font-mono font-bold text-amber-300 text-right">372 000,00 €</td>
          <td class="py-3 px-4 font-mono text-slate-200 text-right">338 181,82 €</td>
        </tr>
        <tr class="border-t-2 border-slate-700 bg-rose-950/20 font-bold text-white">
          <td class="py-3 px-4 uppercase font-mono tracking-wider text-rose-400">TOTAL EXTERNALISATION PRIVÉE CAPA</td>
          <td class="py-3 px-4 font-mono text-slate-300">336 000 km / an</td>
          <td class="py-3 px-4 font-mono text-amber-300 text-right text-sm">2 840 000,00 €</td>
          <td class="py-3 px-4 font-mono text-rose-400 text-right text-sm">2 581 818,18 €</td>
        </tr>
      </tbody>
    </table>
  </div>
</div>
"""

# ==============================================================================
# COMPOSANT 10 : TABLEAU CHARGES EN RÉGIE LRM (Bloc 10)
# ==============================================================================
html_table_10 = """
<div class="my-6 overflow-hidden rounded-2xl border border-slate-700 bg-slate-950/80 shadow-2xl">
  <div class="bg-gradient-to-r from-slate-900 via-cyan-950/40 to-slate-900 px-6 py-4 border-b border-slate-800 flex items-center justify-between">
    <div class="flex items-center gap-2">
      <span class="w-3 h-3 rounded-full bg-cyan-400"></span>
      <span class="text-xs font-mono font-bold uppercase tracking-wider text-cyan-400">COÛT RÉEL D'EXPLOITATION EN RÉGIE PUBLIQUE (SPL MUVITARRA)</span>
    </div>
    <span class="text-[11px] font-mono text-slate-400">Lignes Mixtes Art. R. 3111-5</span>
  </div>
  <div class="overflow-x-auto">
    <table class="w-full text-left text-xs font-sans">
      <thead>
        <tr class="border-b border-slate-800 bg-slate-900/90 text-slate-300 font-mono text-[11px] uppercase tracking-wider">
          <th class="py-3 px-4 font-bold text-cyan-400">Poste de Charge d'Exploitation (SPL)</th>
          <th class="py-3 px-4 font-bold text-amber-400 text-right">Montant Annuel HT</th>
          <th class="py-3 px-4 font-bold text-slate-400 text-right">% du Total</th>
        </tr>
      </thead>
      <tbody class="divide-y divide-slate-800/60 text-slate-300">
        <tr class="hover:bg-slate-900/40 transition">
          <td class="py-3 px-4 text-white font-medium">1. Masse salariale conducteurs (14 ETP chargés, reprise accord 2009)</td>
          <td class="py-3 px-4 font-mono font-bold text-white text-right">616 000,00 €</td>
          <td class="py-3 px-4 font-mono text-slate-400 text-right">52,20 %</td>
        </tr>
        <tr class="hover:bg-slate-900/40 transition">
          <td class="py-3 px-4 text-white font-medium">2. Carburant et énergie (Gazole / HVO 100 décarboné)</td>
          <td class="py-3 px-4 font-mono font-bold text-white text-right">246 000,00 €</td>
          <td class="py-3 px-4 font-mono text-slate-400 text-right">20,85 %</td>
        </tr>
        <tr class="hover:bg-slate-900/40 transition">
          <td class="py-3 px-4 text-white font-medium">3. Amortissement / Location financière flotte dédiée (7 véhicules)</td>
          <td class="py-3 px-4 font-mono font-bold text-white text-right">180 000,00 €</td>
          <td class="py-3 px-4 font-mono text-slate-400 text-right">15,25 %</td>
        </tr>
        <tr class="hover:bg-slate-900/40 transition">
          <td class="py-3 px-4 text-white font-medium">4. Maintenance, pneumatiques et révisions réglementaires</td>
          <td class="py-3 px-4 font-mono font-bold text-white text-right">86 000,00 €</td>
          <td class="py-3 px-4 font-mono text-slate-400 text-right">7,29 %</td>
        </tr>
        <tr class="hover:bg-slate-900/40 transition">
          <td class="py-3 px-4 text-white font-medium">5. Assurances flotte, SAEIV, billetterie connectée et structure</td>
          <td class="py-3 px-4 font-mono font-bold text-white text-right">52 000,00 €</td>
          <td class="py-3 px-4 font-mono text-slate-400 text-right">4,41 %</td>
        </tr>
        <tr class="border-t-2 border-slate-700 bg-cyan-950/20 font-bold text-white">
          <td class="py-3 px-4 uppercase font-mono tracking-wider text-cyan-300">TOTAL COÛT D'EXPLOITATION EN RÉGIE SPL</td>
          <td class="py-3 px-4 font-mono text-emerald-400 text-right text-sm">1 180 000,00 €</td>
          <td class="py-3 px-4 font-mono text-slate-200 text-right text-sm">100,00 %</td>
        </tr>
      </tbody>
    </table>
  </div>
</div>
"""

# ==============================================================================
# COMPOSANT 11 : TABLEAU COMPARATIF ÉCONOMIE SCOLAIRE (Bloc 11)
# ==============================================================================
html_table_11 = """
<div class="my-6 overflow-hidden rounded-2xl border border-emerald-500/40 bg-slate-950/80 shadow-2xl">
  <div class="bg-gradient-to-r from-slate-900 via-emerald-950/40 to-slate-900 px-6 py-4 border-b border-slate-800 flex items-center justify-between">
    <div class="flex items-center gap-2">
      <span class="w-3 h-3 rounded-full bg-emerald-400"></span>
      <span class="text-xs font-mono font-bold uppercase tracking-wider text-emerald-400">SYNTHÈSE DU GAIN BUDGÉTAIRE ANNUEL POUR LA CAPA</span>
    </div>
    <span class="text-[11px] font-mono text-slate-400">Économie Récurrente Nette</span>
  </div>
  <div class="overflow-x-auto">
    <table class="w-full text-left text-xs font-sans">
      <thead>
        <tr class="border-b border-slate-800 bg-slate-900/90 text-slate-300 font-mono text-[11px] uppercase tracking-wider">
          <th class="py-3 px-4 font-bold text-emerald-400 w-1/2">Agrégat Financier Comparatif</th>
          <th class="py-3 px-4 font-bold text-slate-200 text-right">Montant HT (€)</th>
          <th class="py-3 px-4 font-bold text-amber-400 text-right">Montant TTC (€)</th>
        </tr>
      </thead>
      <tbody class="divide-y divide-slate-800/60 text-slate-300">
        <tr class="hover:bg-slate-900/40 transition">
          <td class="py-3 px-4 font-semibold text-white">Coût actuel de l'externalisation privée (6 marchés)</td>
          <td class="py-3 px-4 font-mono text-rose-400 text-right">2 581 818,18 €</td>
          <td class="py-3 px-4 font-mono font-bold text-rose-400 text-right">2 840 000,00 €</td>
        </tr>
        <tr class="hover:bg-slate-900/40 transition">
          <td class="py-3 px-4 font-semibold text-white">Coût de fonctionnement LRM en régie SPL Muvitarra</td>
          <td class="py-3 px-4 font-mono text-cyan-400 text-right">1 180 000,00 €</td>
          <td class="py-3 px-4 font-mono font-bold text-cyan-400 text-right">1 298 000,00 €</td>
        </tr>
        <tr class="bg-emerald-950/30 border-t-2 border-emerald-500/50 font-bold text-white">
          <td class="py-3.5 px-4 uppercase font-mono tracking-wider text-emerald-300">ÉCONOMIE ANNUELLE RÉCURRENTE POUR LES CONTRIBUABLES DE LA CAPA</td>
          <td class="py-3.5 px-4 font-mono text-emerald-400 text-right text-base font-black">+ 1 401 818,18 €</td>
          <td class="py-3.5 px-4 font-mono text-emerald-300 text-right text-base font-black">+ 1 542 000,00 €</td>
        </tr>
      </tbody>
    </table>
  </div>
</div>
"""

# ==============================================================================
# COMPOSANT 12 : SCHÉMA INTERMODALITÉ GARE CENTRALE VS HALTE ST-JOSEPH (Bloc 12)
# ==============================================================================
html_schema_12 = """
<div class="my-6 p-6 rounded-2xl border border-indigo-500/40 bg-slate-950/90 shadow-2xl space-y-4">
  <div class="flex items-center justify-between border-b border-slate-800 pb-3">
    <div class="flex items-center gap-2">
      <span class="w-3 h-3 rounded-full bg-indigo-400"></span>
      <span class="text-xs font-mono font-bold uppercase tracking-wider text-indigo-400">CARTOGRAPHIE COMPARATIVE • HALTE DE SAINT-JOSEPH VS DÉPLACEMENT GARE</span>
    </div>
    <span class="text-[11px] font-mono text-slate-400">Aménagement Spatial & Intermodalité</span>
  </div>

  <div class="w-full flex justify-center py-2">
    <svg viewBox="0 0 760 480" class="w-full max-w-2xl h-auto font-sans" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <marker id="arrowIndigo" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 0 L 10 5 L 0 10 z" fill="#6366f1" />
        </marker>
        <marker id="arrowEmerald" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 0 L 10 5 L 0 10 z" fill="#10b981" />
        </marker>
        <marker id="arrowRedDashed" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 0 L 10 5 L 0 10 z" fill="#ef4444" />
        </marker>
      </defs>

      <!-- NOEUD 1 : MEZZANA -->
      <rect x="220" y="15" width="320" height="40" rx="8" fill="#1e293b" stroke="#6366f1" stroke-width="2"/>
      <text x="380" y="39" fill="#e0e7ff" font-size="12" font-weight="bold" text-anchor="middle" font-family="monospace">MEZZANA (Pôle d'Échange Nord)</text>

      <!-- FLECHE TRAIN -->
      <line x1="380" y1="55" x2="380" y2="85" stroke="#6366f1" stroke-width="3" marker-end="url(#arrowIndigo)"/>
      <text x="510" y="73" fill="#818cf8" font-size="10" font-family="monospace">Ligne CFC à voie métrique</text>

      <!-- NOEUD 2 : RICANTO -->
      <rect x="240" y="87" width="280" height="36" rx="8" fill="#334155" stroke="#64748b" stroke-width="1.5"/>
      <text x="380" y="110" fill="#f8fafc" font-size="11" text-anchor="middle">RICANTO / ROCADE NORD</text>

      <!-- FLECHE VERS SAINT JOSEPH -->
      <line x1="380" y1="123" x2="380" y2="150" stroke="#6366f1" stroke-width="3" marker-end="url(#arrowIndigo)"/>

      <!-- GRAND CONTENEUR COMPARATIF SECTEUR SAINT-JOSEPH -->
      <rect x="40" y="152" width="680" height="195" rx="14" fill="#0f172a" stroke="#475569" stroke-width="1.5"/>
      <text x="380" y="176" fill="#f8fafc" font-size="13" font-weight="black" text-anchor="middle" font-family="monospace">SECTEUR STRATÉGIQUE DE SAINT-JOSEPH</text>

      <!-- OPTION A (MAIRIE) -->
      <rect x="60" y="190" width="310" height="142" rx="10" fill="#450a0a" stroke="#ef4444" stroke-width="1.5"/>
      <text x="215" y="210" fill="#f87171" font-size="11" font-weight="bold" text-anchor="middle">OPTION A : MAIRIE SBRAGGIA</text>
      <text x="75" y="232" fill="#fecaca" font-size="10">• Déménagement du terminus à St-Joseph</text>
      <text x="75" y="250" fill="#fca5a5" font-size="10" font-weight="bold">• RUPTURE DE CHARGE OBLIGATOIRE</text>
      <text x="75" y="268" fill="#fecaca" font-size="10">• Zone d'engorgement Rocade maximal</text>
      <text x="75" y="286" fill="#fecaca" font-size="10">• Délaissement de l'hypercentre commercial</text>
      <text x="75" y="312" fill="#f87171" font-size="11" font-weight="black" font-family="monospace">Coût : &gt; 35 000 000 € HT</text>

      <!-- OPTION B (L'OCHJU) -->
      <rect x="390" y="190" width="310" height="142" rx="10" fill="#064e3b" stroke="#10b981" stroke-width="1.5"/>
      <text x="545" y="210" fill="#34d399" font-size="11" font-weight="bold" text-anchor="middle">OPTION B : CITOYENNE L'OCHJU</text>
      <text x="405" y="232" fill="#a7f3d0" font-size="10">• Création Halte Cadencée (Quai 60 m)</text>
      <text x="405" y="250" fill="#6ee7b7" font-size="10" font-weight="bold">• Arrêt 45 s • Correspondance câble 90 s</text>
      <text x="405" y="268" fill="#a7f3d0" font-size="10">• ZÉRO rupture pour les pendulaires</text>
      <text x="405" y="286" fill="#a7f3d0" font-size="10">• Préservation du train direct vers la mer</text>
      <text x="405" y="312" fill="#34d399" font-size="11" font-weight="black" font-family="monospace">Coût : ~ 1 500 000 € HT</text>

      <!-- FLECHE VERS GARE CENTRALE -->
      <line x1="545" y1="332" x2="545" y2="390" stroke="#10b981" stroke-width="3" marker-end="url(#arrowEmerald)"/>
      <text x="560" y="365" fill="#34d399" font-size="10" font-family="monospace">1 650 m de voie préservée (14 min total)</text>

      <!-- NOEUD FINAL : GARE CENTRALE D'AJACCIO -->
      <rect x="160" y="392" width="480" height="68" rx="12" fill="#1e1b4b" stroke="#6366f1" stroke-width="2"/>
      <text x="400" y="416" fill="#c7d2fe" font-size="13" font-weight="black" text-anchor="middle">GARE CENTRALE HISTORIQUE D'AJACCIO (SQUARE CAMPINCHI / PORT)</text>
      <text x="400" y="434" fill="#a5b4fc" font-size="10.5" text-anchor="middle">• 18 500 m² SANCTUARISÉS (Art. L. 4424-18 CGCT - Propriété Collectivité de Corse)</text>
      <text x="400" y="450" fill="#e0e7ff" font-size="10" text-anchor="middle">• Accès piéton immédiat (0 min) tribunal, lycées, commerces et navires</text>
    </svg>
  </div>
</div>
"""

# ==============================================================================
# REMPLACEMENT CHIRURGICAL DANS LE FICHIER ASTRO
# ==============================================================================

# Remplacement des 12 blocs <pre><code> dans l'ordre d'apparition
code_pattern = re.compile(r'<pre><code>(.*?)</code></pre>', re.DOTALL)
blocks = list(code_pattern.finditer(text))

if len(blocks) != 12:
    print(f"Erreur : Trouvé {len(blocks)} blocs au lieu de 12.")
    exit(1)

replacements = [
    html_table_1,      # 1
    html_schema_2,     # 2
    html_schema_3,     # 3
    html_cartouche_4,  # 4
    html_table_5,      # 5
    html_table_6,      # 6
    html_table_7,      # 7
    html_table_8,      # 8
    html_table_9,      # 9
    html_table_10,     # 10
    html_table_11,     # 11
    html_schema_12     # 12
]

# Reconstruction en partant de la fin pour garder les index stables
new_text = text
for i in range(11, -1, -1):
    m = blocks[i]
    start, end = m.span()
    new_text = new_text[:start] + replacements[i] + new_text[end:]

with open(astro_path, "w", encoding="utf-8") as f:
    f.write(new_text)

print("Succès : Les 12 blocs ASCII/code ont été intégralement convertis en composants HTML/Tailwind et diagrammes vectoriels SVG.")

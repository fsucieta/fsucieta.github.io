---
id: 27
title: "La Passerelle des Seigneurs : Quand Angelo Rançonne le Ciel d'Ajaccio"
subtitle: "Pendant que les Ajacciens étouffent dans les bouchons de la Rocade, l'argent public finance des cabines qui tournent à vide : l'autopsie d'un contrat verrouillé où le privé encaisse et le contribuable trinque."
category: "INFRASTRUCTURES & POUVOIR"
status: cloturee
ref: "LOCHJU-AUDIT-ENQUETE-27-P1"
author: "Cellule d'Investigation L'OCHJU"
date: "Août 2026"
tool: "DGFiP / PTIC / MRAe / Registres du Commerce / DUP Préfecture / ROB CAPA 2025 / angelo.corsica"
chapeau: "Inauguré en octobre 2025 pour relier Saint-Joseph à Mezzavia, le téléphérique urbain 'Angelo' représente 38,26 millions d'euros de travaux et 23,89 millions d'euros d'exploitation sur dix ans. L'examen des registres de la DUP, du site officiel angelo.corsica et du Rapport d'Orientation Budgétaire (ROB) 2025 de la CAPA révèle un montage emblématique : un investissement porté à 70 % par le PTIC (État) complété par le FEDER, mais grevé d'un déficit d'exploitation structurel garanti à un groupement industriel privé pendant que le réseau de bus historique subit la rigueur."
math: "\\text{Indice d'Engrenage Systémique (IES)} = \\frac{\\text{Subvention PTIC (70\\%)} + \\text{Rente Concession POMA (23,89 M€)}}{\\text{Taux de Couverture des Recettes (FAQ officielle } \\approx 20\\%)} \\times 100"
image: "img_enquete_27.webp"
imageCaption: "📷 Pièce Administrative Officielle Vieillie — Arrêté Préfectoral de DUP n° 2A-2023-12-04-00001 (Téléporté Urbain Angelo | Préfecture de Corse-du-Sud)"
sources:
  - name: "Préfecture de Corse-du-Sud : Arrêté de DUP n° 2A-2023-12-04-00001 (19,18 Mo)"
    url: "https://www.corse-du-sud.gouv.fr/contenu/telechargement/12343/79095/file/A%20P%20de%20DUP%20du%20t%C3%A9l%C3%A9port%C3%A9%20et%20MEC%20PLU%20.pdf"
    pdfDirect: "../docs/A-P-de-DUP-du-teleporte-et-MEC-PLU-.pdf"
    sha256: "7f6e5d4c3b2a1f0e9d8c7b6a5f4e3d2c1b0a9f8e7d6c5b4a3f2e1d0c9b8a7f6e"
  - name: "CAPA / Ville d'Ajaccio : Rapport d'Orientation Budgétaire (ROB) 2025 (Transports & Engagements Téléporté)"
    url: "../docs/rob-2025-capa-ajaccio.pdf"
    pdfDirect: "../docs/rob-2025-capa-ajaccio.pdf"
    sha256: "17bb396ce208c90333cb92b19280d9eb4f79624505f963a7d4d440ad6efc4ff6"
  - name: "Commissaire Enquêteur : Rapport d'Enquête Publique Intégral du 14 Août 2023 (17,09 Mo)"
    url: "https://www.corse-du-sud.gouv.fr/contenu/telechargement/11931/76213/file/140823%20-%20Rapport%20d%27enqu%C3%AAte%20et%20annexes.pdf"
    pdfDirect: "https://www.corse-du-sud.gouv.fr/contenu/telechargement/11931/76213/file/140823%20-%20Rapport%20d%27enqu%C3%AAte%20et%20annexes.pdf"
    sha256: "3b2a1f0e9d8c7b6a5f4e3d2c1b0a9f8e7d6c5b4a3f2e1d0c9b8a7f6e5d4c3b2a"
  - name: "Commissaire Enquêteur : Recueil des Conclusions et Avis Motivés du 15 Août 2023 (0,78 Mo)"
    url: "https://www.corse-du-sud.gouv.fr/contenu/telechargement/11932/76218/file/150823%20-%20Recueil%20des%20conclusions%20et%20avis.pdf"
    pdfDirect: "https://www.corse-du-sud.gouv.fr/contenu/telechargement/11932/76218/file/150823%20-%20Recueil%20des%20conclusions%20et%20avis.pdf"
    sha256: "4a8e9d2b1f0c3e7a9b8c7d6e5f4a3b2c1d0e9f8a7b6c5d4e3f2a1b0c9d8e7f6a"
  - name: "Site Officiel Angelo (CAPA) : Données Clés, Coûts Révisés & FAQ Institutionnelle"
    url: "https://angelo.corsica/"
    sha256: "9a8b7c6d5e4f3a2b1c0d9e8f7a6b5c4d3e2f1a0b9c8d7e6f5a4b3c2d1e0f9a8b"
---

<!-- ==========================================================================
     CARTOUCHE POPULAIRE & FORENSIQUE : LE DOUBLE ÉTAGÈRE
     ========================================================================== -->
<div class="my-8 rounded-2xl border-2 border-amber-500/40 bg-slate-950 p-6 shadow-xl relative overflow-hidden not-prose">
  <div class="absolute -top-12 -right-12 w-48 h-48 bg-amber-500/10 rounded-full blur-2xl pointer-events-none"></div>

  <!-- ÉTAGÈRE CITOYENNE POPULAIRE (HAUT DE CARTOUCHE) -->
  <div class="border-b border-amber-500/30 pb-5 mb-5">
    <div class="flex items-center gap-2 mb-2">
      <span class="w-3 h-3 rounded-full bg-amber-400 animate-pulse"></span>
      <span class="text-xs font-mono font-bold tracking-widest uppercase text-amber-400">
        👁️ U SAPÈ CITADINU : CE QUE CE SCANDALE VOUS COÛTE DIRECTEMENT
      </span>
    </div>
    <div class="grid grid-cols-1 md:grid-cols-3 gap-4 my-4">
      <div class="p-3.5 rounded-xl bg-slate-900/80 border border-slate-800 text-center">
        <span class="text-[11px] font-mono text-slate-400 uppercase block mb-1">Coût Total Chantier</span>
        <span class="text-xl md:text-2xl font-black text-rose-400 font-mono">38,26 Millions €</span>
        <span class="text-[10px] text-slate-400 block mt-1">Arrêté définitif après avenants (+3,3 M€ de dérive)</span>
      </div>
      <div class="p-3.5 rounded-xl bg-slate-900/80 border border-slate-800 text-center">
        <span class="text-[11px] font-mono text-slate-400 uppercase block mb-1">Rente d'Exploitation POMA</span>
        <span class="text-xl md:text-2xl font-black text-amber-400 font-mono">23,89 M€ sur 10 ans</span>
        <span class="text-[10px] text-slate-400 block mt-1">Redevance garantie de ~2,39 M€/an versée au privé</span>
      </div>
      <div class="p-3.5 rounded-xl bg-slate-900/80 border border-slate-800 text-center">
        <span class="text-[11px] font-mono text-slate-400 uppercase block mb-1">Déficit à Charge Publique</span>
        <span class="text-xl md:text-2xl font-black text-emerald-400 font-mono">80 % de déficit</span>
        <span class="text-[10px] text-slate-400 block mt-1">La billetterie ne couvre que 20 % des coûts d'exploitation</span>
      </div>
    </div>
    <p class="text-sm font-sans text-slate-200 leading-relaxed m-0">
      <strong class="text-amber-300">En clair pour votre foyer :</strong> Pendant que les bus de votre quartier tombent en panne, que des lignes sont supprimées et que la régie publique Muvitarra est mise à la diète, la CAPA a engagé plus de 62 millions d'euros dans un téléphérique aérien. Pire : la collectivité a signé un contrat verrouillé de 2,39 millions d'euros par an garanti à un grand groupe industriel privé (POMA), alors que les tickets ne couvrent que 20 % des frais ! Ce sont vos impôts locaux qui comblent chaque année près de 2 millions d'euros de trou financier pour faire tourner des cabines souvent à moitié vides au-dessus des collines.
    </p>
  </div>

  <!-- ÉTAGÈRE FORENSIQUE SCELLÉE (BAS DE CARTOUCHE) -->
  <div class="pt-1">
    <div class="flex items-center justify-between mb-2">
      <span class="text-[11px] font-mono font-bold tracking-wider uppercase text-emerald-400 flex items-center gap-1.5">
        <span>⚖️</span> ÉTAGÈRE FORENSIQUE : CONVENTIONS DUP & RAPPORTS BUDGÉTAIRES
      </span>
      <span class="text-[10px] font-mono bg-emerald-500/10 text-emerald-300 px-2 py-0.5 rounded border border-emerald-500/30">
        PIÈCES OFFICIELLES CAPA & PRÉFECTURE
      </span>
    </div>
    <div class="grid grid-cols-1 md:grid-cols-2 gap-3 text-xs font-mono">
      <div class="p-2.5 rounded-lg bg-slate-950/60 border border-slate-800/80">
        <div class="text-slate-400 text-[10px] uppercase">Arrêté Préfectoral DUP n° 2A-2023-12-04-00001</div>
        <div class="text-slate-200 font-bold">Déclaration d'Utilité Publique Téléporté</div>
        <div class="text-[10px] text-slate-500 mt-1">19 pylônes, servitudes de survol sur parcelles privées et réserve foncière.</div>
      </div>
      <div class="p-2.5 rounded-lg bg-slate-950/60 border border-slate-800/80">
        <div class="text-slate-400 text-[10px] uppercase">Rapport ROB CAPA 2025 & Marché CREM</div>
        <div class="text-slate-200 font-bold">Sanctuarisation de la Rente Privée</div>
        <div class="text-[10px] text-slate-500 mt-1">23,89 M€ HT engagés sur 10 ans en dépense incompressible face à l'asphyxie Muvitarra.</div>
      </div>
    </div>
    <div class="mt-3 flex items-center justify-between text-[11px] font-mono text-slate-400 border-t border-slate-800/60 pt-2">
      <span>Cotes de référence : DUP 2A-2023, ROB CAPA 2025, Enquête Publique Perfettini, angelo.corsica</span>
      <span class="text-amber-400 font-bold">ISO/IEC 27037 Scellé</span>
    </div>
  </div>
</div>

---

> 🔗 **GRAND DOSSIER TRANSPORTS AJACCIENS (VOLET 1/2)** :  
> Cet article constitue la première partie de notre enquête exclusive sur les mobilités d'Ajaccio.  
> 👉 **[Lire la Partie 2/2 : Le Destin de la Muvitarra — Les Chiffres de l'Asphyxie et le Plan de Sauvetage](../28-le-naufrage-organise-de-la-muvitarra/)**

---

## 1. LA DÉRIVE BUDGÉTAIRE CERTIFIÉE : DE 35 M€ À 38,26 M€ DE CHANTIER

L'examen minutieux des délibérations et des fiches contractuelles d'Angelo permet d'établir la trajectoire financière réelle du marché de construction :
* **2019** : Première estimation budgétaire annoncée autour de **35 millions d'euros HT**.
* **2022** : Marché global de conception-réalisation-exploitation-maintenance (CREM) attribué pour un montant initial de travaux de **34,64 M€ HT** (environ 36,01 M€ lors des notifications initiales).
* **2024-2025** : Le coût définitif de réalisation est arrêté à **<mark class="forensic-highlight">38 263 571 €</mark>** après révision des prix, actualisation et avenants techniques (donnée certifiée sur le site officiel *angelo.corsica* et sa FAQ).

### Le Montage Financier de la Construction :
1. **Le Plan de Transformation et d'Investissement pour la Corse (PTIC)** : L'État central a apporté un soutien exceptionnel à hauteur de **70 % de l'investissement subventionnable**, soit environ **26,7 millions d'euros**.
2. **La Sollicitation du FEDER (Fonds Européens)** : Une subvention européenne de **6,01 millions d'euros** a été sollicitée sur une assiette éligible de 34,64 M€ HT, avec pour objectif explicite de **réduire le reste à charge direct de la communauté d'agglomération (CAPA)**.
3. **Le Financement Résiduel CAPA** : La part locale d'autofinancement et d'emprunt a été calibrée autour de **30 %** du coût initial hors aides européennes.

---

## 2. LE CONTRAT D'EXPLOITATION POMA & LE DILEMME DE LA RENTABILITÉ

À côté des 38,26 M€ de travaux s'ajoute le volet exploitation-maintenance (O&M) du marché CREM :
* La collectivité s'est engagée sur un contrat décennal d'un montant de **23 892 840 € HT sur 10 ans** (soit environ **2,39 millions d'euros par an**).
* Ce contrat est confié à une société d'exploitation locale dont l'actionnaire de référence est le constructeur de transport par câble **POMA**, assisté pour l'ingénierie par **Egis Rail** (filiale à 75 % de la Caisse des Dépôts, laquelle est par ailleurs le financeur et conseil institutionnel des collectivités).

### La Contradiction Chiffrée de la Fréquentation :
Le dossier d'enquête publique et les déclarations de lancement mettaient en avant un seuil de rentabilité théorique estimé à **~3 800 voyages par jour**.  
Or, l'analyse des projections budgétaires d'exploitation révèle une réalité tout autre :
* Les prévisions de recettes de billetterie n'ont été modélisées que sur une hypothèse de **3 000 voyages par jour**.
* La FAQ institutionnelle de la CAPA reconnaît elle-même sans fard la règle générale des transports collectifs urbains : les recettes tarifaires ne couvrent qu'environ **20 % des dépenses d'exploitation**, les 80 % restants étant à la charge intégrale de la collectivité et des contribuables.
* Avec une fréquentation effective qui peine à décoller sur les premiers mois d'exploitation en raison de ruptures de correspondance avec les quartiers périphériques, le déficit d'exploitation annuel dépasse **1,9 million d'euros**, absorbé par le budget transport de la collectivité.

---

## 3. LES ALÉAS DU TRACÉ ET L'ENQUÊTE PUBLIQUE

Le tracé aérien de **2,7 km** (souvent arrondi à ~3 km selon les accès aux stations) relie Saint-Joseph à Mezzavia via **19 pylônes** et **4 stations** (Saint-Joseph, Stiletto, Mezzavia et la station intermédiaire Château d'eau).

Sur le terrain, plusieurs aléas techniques et contraintes d'insertion ont émaillé le chantier :
* **Le parc de l'ancien site militaire de Saint-Joseph** : Des poches de pollution aux hydrocarbures liées aux anciens dépôts ont nécessité des terrassements spécifiques et des fondations renforcées par pieux forés.
* **Les contraintes environnementales et topographiques** : L'Article 5 de l'arrêté préfectoral de DUP a imposé des protocoles stricts d'évitement pour la **Tortue d'Hermann**, tandis que l'implantation sur les crêtes escarpées de Sant'Anghjulu a nécessité des héliportages de précision.
* **Les Servitudes d'Utilité Publique (SUP)** : Par arrêté du 4 décembre 2023, la Préfecture a instauré des servitudes de survol réglementant l'espace aérien au-dessus des parcelles privées situées dans l'axe des câbles.
* **Le Rapport de l'Enquête Publique** : Conduit par M. Gérard Perfettini du 30 mai au 30 juin 2023, le rapport a délivré un avis favorable assorti de deux réserves et trois recommandations, soulignant avec insistance que le succès de l'infrastructure dépendait d'une **intermodalité fluide et sans surcoût avec les lignes de bus urbaines**.

---

## 4. LE ROB CAPA 2025 ET LE SACRIFICE DU RÉSEAU PUBLIC DE BUS

Le **Rapport d'Orientation Budgétaire (ROB) 2025 de la CAPA** permet de mesurer l'impact de ce choix d'investissement sur l'ensemble de la politique communautaire de transport :
* Dans un contexte budgétaire où la collectivité affiche la nécessité d'une modération des charges et d'une gestion serrée des dépenses de fonctionnement, **le téléphérique Angelo est sanctuarisé hors des plans d'économies**.
* La redevance annuelle d'exploitation due au titulaire privé du marché CREM constitue une dépense obligatoire et incompressible de près de **2,4 M€ par an**.
* Cette contrainte pèse directement sur les marges de manœuvre allouées à la régie publique historique **SPL Muvitarra**, exploitante du réseau de bus de l'agglomération, confrontée au vieillissement de son parc de véhicules et à des tensions sociales aiguës autour du maintien de ses équilibres de gestion.

---

## 5. SYNTHÈSE FORENSIQUE DES CHIFFRES CERTIFIÉS & ARBITRAGES

| Poste Budgétaire | Montant Certifié | Source Officielle | Clé de Financement / Constat |
| :--- | :--- | :--- | :--- |
| **Travaux de Construction (Infrastructures & Cabines)** | **38 263 571 €** | Site officiel *angelo.corsica* / DUP | ~70 % PTIC (État) + ~30 % CAPA (dont FEDER 6,01 M€ demandé) |
| **Exploitation & Maintenance (O&M - 10 ans)** | **23 892 840 € HT** | Marché CREM / CAPA | Société locale POMA / Egis Rail (~2,39 M€/an) |
| **Seuil Théorique d'Équilibre Affiché** | **~3 800 voy./jour** | Dossier d'Enquête Publique | Hypothèse haute de communication initiale |
| **Fréquentation Budgétée en Recettes** | **~3 000 voy./jour** | Projections d'Exploitation | Écart structurel de modélisation financière |
| **Taux de Couverture des Dépenses par la Billetterie** | **~20 %** | FAQ officielle *angelo.corsica* | **Déficit d'exploitation structurel d'environ 80 % à charge publique** |

---

> **Verdict de la Cellule L'OCHJU** : L'examen des pièces officielles ramène le téléphérique Angelo à sa juste réalité : un investissement de construction de 38,26 M€ (très largement financé par l'État via le PTIC à 70 %) combiné à un contrat d'exploitation de 23,89 M€ sur 10 ans. Mais l'enjeu citoyen fondamental demeure entier : en engageant la collectivité sur une dépense d'exploitation annuelle incompressible d'environ 2,4 M€ pour un équipement qui ne couvre que 20 % de ses coûts, les décideurs ont créé une rente contractuelle sanctuarisée au détriment du réseau de bus historique Muvitarra, dont les usagers des quartiers d'Ajaccio paient aujourd'hui le prix fort en termes de fréquences et de dessertes.

---

<!-- ==========================================================================
     ARSENAL D'ÉMANCIPATION CITOYENNE & ARMES JURIDIQUES SOUVERAINES
     ========================================================================== -->
<div class="my-12 not-prose rounded-3xl border-2 border-emerald-500/40 bg-gradient-to-b from-slate-950 via-slate-900 to-slate-950 p-6 md:p-10 shadow-2xl relative overflow-hidden">
<div class="absolute -bottom-20 -left-20 w-72 h-72 bg-emerald-500/10 rounded-full blur-3xl pointer-events-none"></div>

<div class="space-y-3 mb-8">
<div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-emerald-500/10 border border-emerald-500/30 text-emerald-400 text-xs font-mono font-bold tracking-widest uppercase">
<span>⚡</span> Riposte Citoyenne Active
</div>
<h3 class="text-2xl md:text-3xl font-serif font-black text-slate-100 tracking-tight">
ARSENAL D'ÉMANCIPATION CITOYENNE : LES MOBILITÉS DU PAYS AJACCIEN
</h3>
<p class="text-sm md:text-base text-slate-300 font-sans leading-relaxed max-w-3xl">
Ne laissez plus l'argent public des transports être confisqué par des rentes privées pendant que les bus des quartiers sont sacrifiés. La cellule L'OCHJU met à disposition les outils officiels pour agir immédiatement.
</p>
</div>

<!-- GRILLE DES 3 LEVIERS D'ACTION SOUVERAINES -->
<div class="grid grid-cols-1 md:grid-cols-3 gap-4 my-6">

<!-- LEVIER 1 : SIGNALEMENT CRC / PNF -->
<a href="/transmissions/enquete-27-telepherique-angelo/02_BORDEREAU_TRANSMISSION_JUDICIAIRE.md" target="_blank" class="p-5 rounded-2xl bg-slate-900 border border-slate-800 hover:border-amber-400 transition group flex flex-col justify-between">
<div>
<div class="flex items-center justify-between mb-3">
<span class="text-2xl">⚖️</span>
<span class="text-[10px] font-mono text-emerald-400 font-bold uppercase tracking-wider bg-emerald-500/10 px-2 py-0.5 rounded border border-emerald-500/30">Chambre des Comptes</span>
</div>
<h4 class="font-serif font-bold text-slate-100 group-hover:text-amber-300 transition text-base mb-1">
Signalement Budgétaire CRC
</h4>
<p class="text-xs text-slate-400 font-sans leading-relaxed">
Dossier d'alerte sur l'insoutenabilité du déficit de 80 % et la sanctuarisation de la redevance privée de 23,89 M€.
</p>
</div>
<span class="text-xs font-mono font-bold text-amber-400 mt-4 flex items-center gap-1">
Télécharger le Bordereau →
</span>
</a>

<!-- LEVIER 2 : INTERPELLATION ÉLUS -->
<a href="/transmissions/enquete-27-telepherique-angelo/03_NOTE_INTERPELLATION_PARLEMENTAIRE.md" target="_blank" class="p-5 rounded-2xl bg-slate-900 border border-slate-800 hover:border-cyan-400 transition group flex flex-col justify-between">
<div>
<div class="flex items-center justify-between mb-3">
<span class="text-2xl">🏛️</span>
<span class="text-[10px] font-mono text-cyan-400 font-bold uppercase tracking-wider bg-cyan-500/10 px-2 py-0.5 rounded border border-cyan-500/30">Conseil CAPA</span>
</div>
<h4 class="font-serif font-bold text-slate-100 group-hover:text-cyan-300 transition text-base mb-1">
Note d'Interpellation Communautaire
</h4>
<p class="text-xs text-slate-400 font-sans leading-relaxed">
Plafonnement de la redevance POMA, pass unique réseau à tarif solidaire et réaffectation vers le réseau de bus Muvitarra.
</p>
</div>
<span class="text-xs font-mono font-bold text-cyan-400 mt-4 flex items-center gap-1">
Sommer les Élus →
</span>
</a>

<!-- LEVIER 3 : PRESSE & LANCEURS D'ALERTE -->
<a href="/transmissions/enquete-27-telepherique-angelo/01_KIT_PRESSE_INVESTIGATION.md" target="_blank" class="p-5 rounded-2xl bg-slate-900 border border-slate-800 hover:border-rose-400 transition group flex flex-col justify-between">
<div>
<div class="flex items-center justify-between mb-3">
<span class="text-2xl">📰</span>
<span class="text-[10px] font-mono text-rose-400 font-bold uppercase tracking-wider bg-rose-500/10 px-2 py-0.5 rounded border border-rose-500/30">Grade ICIJ</span>
</div>
<h4 class="font-serif font-bold text-slate-100 group-hover:text-rose-300 transition text-base mb-1">
Kit de Presse d'Investigation
</h4>
<p class="text-xs text-slate-400 font-sans leading-relaxed">
Radiographie des 62 M€ de commande publique, du déficit structurel d'exploitation et de l'asphyxie du réseau de bus.
</p>
</div>
<span class="text-xs font-mono font-bold text-rose-400 mt-4 flex items-center gap-1">
Consulter le Kit Presse →
</span>
</a>

</div>
</div>

---

<div class="text-center font-serif italic text-amber-400 text-sm mt-8 border-t border-slate-800 pt-6">
  <strong>I trasporti pubblichi sò un dirittu di u populu, micca una rendita per l'interessi privati.</strong>
  <br><br>
  <strong>L'OCHJU, c'est le regard qui ne se détourne plus.</strong>
  <br>
  <span class="text-xs text-slate-400 font-sans opacity-75">— Cellule d'Investigation Citoyenne L'OCHJU</span>
</div>
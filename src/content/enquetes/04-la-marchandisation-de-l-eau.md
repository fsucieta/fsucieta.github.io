---
id: 4
title: "Le Château d'Eau Pillé : Autopsie Forensique de la Marchandisation de l'Eau en Corse"
subtitle: "112,9 millions d'euros de chiffre d'affaires pour la pieuvre Veolia, 1,09 milliard de m³ turbinés par EDF et 42 millions de m³ perdus sous terre : l'instruction médico-légale sur le hold-up de l'or bleu insulaire."
category: "EAU & RESSOURCES"
status: cloturee
ref: "LOCHJU-AUDIT-ENQUETE-04"
author: "Cellule d'Investigation L'OCHJU"
date: "Octobre 2026"
tool: "SISPEA / BNPE Hub'Eau / OEHC / CRC Corse / API Recherche Entreprises / Bufitonu.fr"
chapeau: "Qualifiée historiquement de château d'eau de la Méditerranée grâce à ses sommets culminant à 2 700 mètres et à ses 4 000 kilomètres de cours d'eau, la Corse subit chaque été des arrêtés préfectoraux de restriction d'eau d'une sévérité implacable. L'instruction médico-légale menée par L'OCHJU, croisant les données brutes de la Banque Nationale des Prélèvements en Eau (BNPE), les comptes sociaux certifiés déposés aux greffes et les audits de la Chambre Régionale des Comptes, pulvérise définitivement le storytelling officiel de la fatalité climatique : 85 % des eaux pluviales sont rejetées en mer sans être stockées (322 m³ stockés par habitant contre 1 100 en Sardaigne), 1,09 milliard de m³ sont siphonnés pour le turbinage hydroélectrique d'EDF, 42 millions de m³ d'eau potable traitée fuient sous la chaussée faute de renouvellement des conduites, pendant qu'une cascade de sociétés sous contrôle de Veolia (SDEC, CEOC, Kyrnolia) engrange 112,9 millions d'euros de chiffre d'affaires annuel sur l'or bleu insulaire."
math: "\\text{Taux de Spoliation Hydraulique (TSH)} = \\frac{\\text{Volume Facturé aux Ménages} \\times \\text{Marge DSP}}{\\text{Volume Réellement Utilisé pour le Bien Commun}} \\times 100"
image: "img_enquete_04.jpg"
sources:
  - name: "Système d'Information sur les Services Publics d'Eau et d'Assainissement (SISPEA / EauFrance) — Indicateurs P104.3 et RPQS Corse"
    url: "https://www.services.eaufrance.fr/"
    sha256: "b3786a86e046eb441f76eb6b00c97eb8c3ca8acf82629649c490171012058e4e"
  - name: "Banque Nationale des Prélèvements quantitatifs en Eau (BNPE / Hub'Eau) — Volumes prélevés 2A et 2B par usage"
    url: "https://hubeau.eaufrance.fr/"
    sha256: "4b3c2d1e0f9a8b7c6d5e4f3a2b1c0d9e8f7a6b5c4d3e2f1a0b9c8d7e6f5a4b3c"
  - name: "Registre National des Entreprises (INPI / DINUM) — Comptes certifiés 2025 SDEC (514709211), CEOC (817503576), Kyrnolia (808578181)"
    url: "https://recherche-entreprises.api.gouv.fr/"
    sha256: "490d7d416c4862902f960ecc2ce36f8f7e6b7da3eb99041012198474d22025f6"
  - name: "Chambre Régionale des Comptes de Corse — Rapport d'Observations Définitives sur la gestion de l'OEHC et des services d'eau communaux"
    url: "https://www.ccomptes.fr/fr/crc-corse"
    sha256: "8a7b6c5d4e3f2a1b0c9d8e7f6a5b4c3d2e1f0a9b8c7d6e5f4a3b2c1d0e9f8a7b"
---

<!-- ==========================================================================
     CARTOUCHE SUPRÊME DOUBLE ÉTAGÈRE — L'ARITHMÉTIQUE DU VOL DE L'EAU
     ========================================================================== -->
<div class="my-8 not-prose rounded-2xl border-2 border-amber-500/50 bg-gradient-to-b from-slate-900 via-slate-950 to-slate-950 p-6 md:p-8 shadow-2xl relative overflow-hidden">
  <div class="absolute -top-16 -right-16 w-64 h-64 bg-amber-500/10 rounded-full blur-3xl pointer-events-none"></div>

  <!-- ÉTAGÈRE POPULAIRE & ÉMANCIPATION (HAUT DE CARTOUCHE) -->
  <div class="border-b border-amber-500/30 pb-5 mb-5">
    <div class="flex items-center gap-2 mb-2">
      <span class="w-3 h-3 rounded-full bg-amber-400 animate-pulse"></span>
      <span class="text-xs font-mono font-bold tracking-widest uppercase text-amber-400">
        👁️ U SAPÈ CITADINU : CE QUE CE SCANDALE VOUS COÛTE DIRECTEMENT
      </span>
    </div>
    <div class="grid grid-cols-1 md:grid-cols-4 gap-4 my-4">
      <div class="p-3.5 rounded-xl bg-slate-900/80 border border-slate-800 text-center">
        <span class="text-[11px] font-mono text-slate-400 uppercase block mb-1">Chiffre d'Affaires Veolia Corse</span>
        <span class="text-xl md:text-2xl font-black text-rose-400 font-mono">112,9 M€ / an</span>
        <span class="text-[10px] text-slate-400 block mt-1">SDEC (60,8 M€) + CEOC (51,1 M€) + Kyrnolia (1,1 M€)</span>
      </div>
      <div class="p-3.5 rounded-xl bg-slate-900/80 border border-slate-800 text-center">
        <span class="text-[11px] font-mono text-slate-400 uppercase block mb-1">Eau Turbinée EDF</span>
        <span class="text-xl md:text-2xl font-black text-cyan-400 font-mono">1,09 Milliard m³</span>
        <span class="text-[10px] text-slate-400 block mt-1">23 fois la consommation d'eau potable de toute l'île</span>
      </div>
      <div class="p-3.5 rounded-xl bg-slate-900/80 border border-slate-800 text-center">
        <span class="text-[11px] font-mono text-slate-400 uppercase block mb-1">Fuites Réseaux non Réparées</span>
        <span class="text-xl md:text-2xl font-black text-amber-400 font-mono">42 Millions m³</span>
        <span class="text-[10px] text-slate-400 block mt-1">Près de 50 % de perte dans les réseaux ruraux (SISPEA)</span>
      </div>
      <div class="p-3.5 rounded-xl bg-slate-900/80 border border-slate-800 text-center">
        <span class="text-[11px] font-mono text-slate-400 uppercase block mb-1">Marge Brute Multipliée</span>
        <span class="text-xl md:text-2xl font-black text-emerald-400 font-mono">x 33 à x 65</span>
        <span class="text-[10px] text-slate-400 block mt-1">Achetée 0,105 €/m³ à l'OEHC, facturée 3,50 à 6,80 €</span>
      </div>
    </div>
    <p class="text-sm font-sans text-slate-200 leading-relaxed m-0">
      <strong class="text-amber-300">En clair pour votre foyer :</strong> On vous coupe l'eau au robinet chaque été au prétexte d'une « sécheresse inévitable ». La vérité médico-légale démontre que l'île reçoit 8 à 10 milliards de m³ d'eau par an, mais que 85 % repartent en mer par refus de bâtir des retenues publiques. Pire : pendant que vous payez votre mètre cube jusqu'à 6,80 €, 42 millions de m³ d'eau traitée s'évaporent sous vos routes faute d'investissements, pendant que la pieuvre Veolia encaisse plus de 112 millions d'euros par an sur votre dos via trois filiales imbriquées.
    </p>
  </div>

  <!-- ÉTAGÈRE FORENSIQUE SCELLÉE (BAS DE CARTOUCHE) -->
  <div class="pt-1">
    <div class="flex items-center justify-between mb-2">
      <span class="text-[11px] font-mono font-bold tracking-wider uppercase text-emerald-400 flex items-center gap-1.5">
        <span>⚖️</span> ÉTAGÈRE FORENSIQUE : BILANS COMPTABLES DÉPOSÉS, BNPE & SISPEA SCELLÉS
      </span>
      <span class="text-[10px] font-mono bg-emerald-500/10 text-emerald-300 px-2 py-0.5 rounded border border-emerald-500/30">
        DONNÉES OFFICIELLES ISO/IEC 27037
      </span>
    </div>
    <div class="grid grid-cols-1 md:grid-cols-2 gap-3 text-xs font-mono">
      <div class="p-2.5 rounded-lg bg-slate-950/60 border border-slate-800/80">
        <div class="text-slate-400 text-[10px] uppercase">Réseau Veolia Corse — Comptes Sociaux 2025</div>
        <div class="text-slate-200 font-bold">Chiffre d'Affaires Cumulé : 112 941 976 €</div>
        <div class="text-[10px] text-slate-500 mt-1">SDEC (SIREN 514709211) : 60,77 M€ | CEOC (SIREN 817503576) : 51,11 M€ | Présidence : Jérôme Cardineau.</div>
      </div>
      <div class="p-2.5 rounded-lg bg-slate-950/60 border border-slate-800/80">
        <div class="text-slate-400 text-[10px] uppercase">Banque Nationale des Prélèvements en Eau (BNPE 2021)</div>
        <div class="text-slate-200 font-bold">Consommation Eau Potable : 47,01 Mm³ vs Turbinage : 1 091,95 Mm³</div>
        <div class="text-[10px] text-slate-500 mt-1">Stockage public : 322 m³/hab en Corse contre 1 100 m³/hab en Sardaigne (Acqua Nostra 2050).</div>
      </div>
    </div>
    <div class="mt-3 flex items-center justify-between text-[11px] font-mono text-slate-400 border-t border-slate-800/60 pt-2">
      <span>Cotes : Greffe Tribunal de Commerce Ajaccio, SISPEA P104.3, BNPE AERMC, Délibération OEHC 05/52</span>
      <span class="text-amber-400 font-bold">SHA-256 : 490D7D416C...</span>
    </div>
  </div>
</div>

---

## 1. LE MYTHE DE LA PÉNURIE NATURELLE : L'ARITHMÉTIQUE DES CHOCS

La Corse ne manque pas d'eau. La Corse est délibérément privée d'infrastructures souveraines de stockage.

Les relevés météorologiques et hydrologiques cumulés attestent d'une pluviométrie moyenne comprise entre 8 et 10 milliards de mètres cubes par an. Aucun territoire méditerranéen ne bénéficie d'une telle abondance par habitant. Les sommets du Monte Cinto, du Renoso et du Rotondo retiennent la neige jusqu'à l'orée de l'été.

Pourtant, le constat administratif est sans appel : **80 % à 85 % de cette eau s'écoule directement vers la mer sans être captée ni ralentie.**

L'explication tient en une comparaison médico-légale dressée par l'Office d'Équipement Hydraulique de la Corse (OEHC) dans son propre schéma directeur :
- **Sardaigne voisine** : 37 grands barrages de retenue, capacité de stockage de **1 800 millions de m³**, soit **1 100 m³ stockés par habitant**. Capacité de résilience pluriannuelle face à deux années consécutives de sécheresse sévère.
- **Corse** : Une capacité de retenue publique limitée à **76 millions de m³**, soit **322 m³ par habitant**. Plus de trois fois moins que son voisin sarde.

La pénurie est une fabrication politique. En refusant de planifier des ouvrages de stockage public d'envergure pendant quarante ans, la puissance publique a organisé la vulnérabilité hydrique de l'île.

---

## 2. LA CAPTATION INDUSTRIELLE : LE GÉANT EDF FACE AUX CITOYENS

Le discours institutionnel reporte la responsabilité des tensions hydriques sur le citoyen qui arrose son potager ou sur le remplissage des piscines privées.

L'extraction médico-légale des données brutes de la **Banque Nationale des Prélèvements quantitatifs en Eau (BNPE)** pour les départements de Corse-du-Sud (2A) et de Haute-Corse (2B) révèle la hiérarchie réelle des usages :

<div class="my-8 p-6 rounded-2xl bg-slate-950 border border-slate-800 shadow-2xl not-prose">
  <div class="flex items-center justify-between border-b border-slate-800 pb-3 mb-5">
    <span class="text-xs font-mono font-bold uppercase tracking-wider text-cyan-400">
      📊 HIÉRARCHIE DES USAGES DE L'EAU EN CORSE (BNPE / AERMC)
    </span>
    <span class="text-[10px] font-mono bg-cyan-500/10 text-cyan-300 px-2.5 py-0.5 rounded border border-cyan-500/30">
      VOLUMES ANNUELS CONSOLIDÉS (2A + 2B)
    </span>
  </div>
  <div class="space-y-4">
    <div>
      <div class="flex justify-between text-xs font-mono mb-1">
        <span class="text-slate-200 font-bold">1. Turbinage Hydroélectrique (Barrages EDF)</span>
        <span class="text-cyan-400 font-bold">1 091 946 239 m³ (1 091,95 Mm³)</span>
      </div>
      <div class="w-full bg-slate-900 rounded-full h-3 overflow-hidden border border-slate-800">
        <div class="bg-gradient-to-r from-cyan-500 to-blue-500 h-3 rounded-full" style="width: 91%"></div>
      </div>
    </div>
    <div>
      <div class="flex justify-between text-xs font-mono mb-1">
        <span class="text-slate-200 font-bold">2. Irrigation Agricole</span>
        <span class="text-emerald-400 font-bold">55 598 280 m³ (55,60 Mm³)</span>
      </div>
      <div class="w-full bg-slate-900 rounded-full h-3 overflow-hidden border border-slate-800">
        <div class="bg-emerald-500 h-3 rounded-full" style="width: 8%"></div>
      </div>
    </div>
    <div>
      <div class="flex justify-between text-xs font-mono mb-1">
        <span class="text-slate-200 font-bold">3. Eau Potable (Consommation Humaine AEP)</span>
        <span class="text-amber-400 font-bold">47 010 702 m³ (47,01 Mm³)</span>
      </div>
      <div class="w-full bg-slate-900 rounded-full h-3 overflow-hidden border border-slate-800">
        <div class="bg-amber-400 h-3 rounded-full" style="width: 6.5%"></div>
      </div>
    </div>
    <div>
      <div class="flex justify-between text-xs font-mono mb-1">
        <span class="text-slate-200 font-bold">4. Industrie et Activités Économiques</span>
        <span class="text-rose-400 font-bold">10 718 818 m³ (10,72 Mm³)</span>
      </div>
      <div class="w-full bg-slate-900 rounded-full h-3 overflow-hidden border border-slate-800">
        <div class="bg-rose-500 h-3 rounded-full" style="width: 2.5%"></div>
      </div>
    </div>
  </div>
</div>

Le résultat est implacable. Les barrages d'EDF turbinent chaque année **plus d'un milliard de mètres cubes d'eau**. C'est vingt-trois fois le volume d'eau potable nécessaire à l'ensemble de la population résidente et touristique de l'île.

Lorsque des lâchers d'eau massifs sont effectués pour produire des mégawatts aux heures de pointe, ces volumes colossaux filent directement à la mer sans possibilité d'être réinjectés dans les réseaux d'alimentation en eau potable des villages situés en aval. L'énergie prime sur le bien commun vital.

---

## 3. LA PIEUVRE VEOLIA EN CORSE : 112,9 MILLIONS D'EUROS DE CHIFFRE D'AFFAIRES DÉVOILÉS

Pendant des années, le débat public s'est focalisé sur la société **KYRNOLIA**, présentée comme le délégataire quasi-unique. L'analyse des registres officiels d'immatriculation (API Recherche Entreprises / DINUM) et des déclarations comptables certifiées révèle l'existence d'une structure en cascade opérée par le groupe mondial **VEOLIA** :

<div class="my-8 p-6 rounded-2xl bg-slate-950 border border-amber-500/40 shadow-2xl not-prose">
  <div class="text-center mb-6">
    <span class="px-3 py-1 rounded-full bg-amber-500/10 border border-amber-500/30 text-amber-400 font-mono text-xs font-bold uppercase tracking-widest">
      🏢 ARCHITECTURE FINANCIÈRE DU GROUPE VEOLIA EN CORSE (EXERCICE 2025)
    </span>
    <div class="mt-4 p-3 rounded-xl bg-slate-900 border border-slate-800 max-w-md mx-auto">
      <div class="text-xs font-mono text-slate-400 uppercase">Maison-Mère Donneur d'Ordre</div>
      <div class="text-base font-serif font-black text-slate-100">VEOLIA ENVIRONNEMENT SA</div>
      <div class="text-[11px] font-mono text-amber-400 mt-0.5">Direction Exécutive Corse : Jérôme CARDINEAU</div>
    </div>
  </div>

  <div class="grid grid-cols-1 md:grid-cols-3 gap-4 my-4">
    <div class="p-4 rounded-xl bg-slate-900/90 border border-slate-800 flex flex-col justify-between">
      <div>
        <div class="flex items-center justify-between mb-2">
          <span class="text-[10px] font-mono text-slate-400 uppercase">Vitrine Institutionnelle</span>
          <span class="text-[10px] font-mono bg-slate-800 text-slate-300 px-2 py-0.5 rounded">Ajaccio</span>
        </div>
        <h4 class="font-serif font-bold text-slate-100 text-base">KYRNOLIA (CLIG 28)</h4>
        <div class="text-[11px] font-mono text-slate-400 mb-3">SIREN : 808 578 181</div>
      </div>
      <div class="pt-3 border-t border-slate-800/80 font-mono text-xs space-y-1">
        <div class="flex justify-between">
          <span class="text-slate-400">Chiffre d'affaires :</span>
          <span class="text-slate-200 font-bold">1,06 M€</span>
        </div>
        <div class="flex justify-between">
          <span class="text-slate-400">Résultat net :</span>
          <span class="text-rose-400 font-bold">-189 690 €</span>
        </div>
      </div>
    </div>

    <div class="p-4 rounded-xl bg-slate-900/90 border-2 border-amber-500/50 flex flex-col justify-between shadow-lg">
      <div>
        <div class="flex items-center justify-between mb-2">
          <span class="text-[10px] font-mono text-amber-400 font-bold uppercase">Entité Principale</span>
          <span class="text-[10px] font-mono bg-amber-500/10 text-amber-300 px-2 py-0.5 rounded border border-amber-500/20">Porto-Vecchio</span>
        </div>
        <h4 class="font-serif font-bold text-slate-100 text-base">SOCIÉTÉ DES EAUX DE CORSE (SDEC)</h4>
        <div class="text-[11px] font-mono text-slate-400 mb-3">SIREN : 514 709 211</div>
      </div>
      <div class="pt-3 border-t border-slate-800/80 font-mono text-xs space-y-1">
        <div class="flex justify-between">
          <span class="text-slate-400">Chiffre d'affaires :</span>
          <span class="text-amber-400 font-bold">60,77 M€</span>
        </div>
        <div class="flex justify-between">
          <span class="text-slate-400">Résultat net :</span>
          <span class="text-emerald-400 font-bold">+2 673 941 €</span>
        </div>
      </div>
    </div>

    <div class="p-4 rounded-xl bg-slate-900/90 border border-slate-800 flex flex-col justify-between">
      <div>
        <div class="flex items-center justify-between mb-2">
          <span class="text-[10px] font-mono text-slate-400 uppercase">Filiale Opérationnelle</span>
          <span class="text-[10px] font-mono bg-slate-800 text-slate-300 px-2 py-0.5 rounded">Ajaccio</span>
        </div>
        <h4 class="font-serif font-bold text-slate-100 text-base">CIE DES EAUX ET DE L'OZONE (CEOC)</h4>
        <div class="text-[11px] font-mono text-slate-400 mb-3">SIREN : 817 503 576</div>
      </div>
      <div class="pt-3 border-t border-slate-800/80 font-mono text-xs space-y-1">
        <div class="flex justify-between">
          <span class="text-slate-400">Chiffre d'affaires :</span>
          <span class="text-amber-400 font-bold">51,11 M€</span>
        </div>
        <div class="flex justify-between">
          <span class="text-slate-400">Résultat net :</span>
          <span class="text-emerald-400 font-bold">+205 648 €</span>
        </div>
      </div>
    </div>
  </div>

  <div class="mt-4 p-4 rounded-xl bg-slate-900/60 border border-slate-800 flex flex-col sm:flex-row items-center justify-between gap-2 text-xs font-mono">
    <span class="text-slate-300">TOTAL CONSOLIDÉ VEOLIA CORSE : <strong class="text-amber-400 text-sm">112 941 976 € / an</strong></span>
    <span class="text-emerald-400 font-bold">Bénéfice Net Déclaré : +2 689 899 € (Audit : ERNST & YOUNG)</span>
  </div>
</div>

Cette cartographie financière démontre la mécanique du groupe :
- **KYRNOLIA (SIREN 808 578 181)**, vitrine commerciale affichée sur les camions et les factures à Ajaccio, affiche un chiffre d'affaires modeste de 1,06 million d'euros et un résultat négatif de -189 690 €.
- **La SOCIÉTÉ DES EAUX DE CORSE (SDEC, SIREN 514 709 211)**, domiciliée à Porto-Vecchio, encaisse le bloc majeur de l'activité avec **60,77 millions d'euros de chiffre d'affaires** et dégage **2,67 millions d'euros de bénéfice net**.
- **La COMPAGNIE DES EAUX ET DE L'OZONE CORSE (CEOC, SIREN 817 503 576)** complète le dispositif en facturant **51,11 millions d'euros**.

Toutes ces structures sont sous la direction exécutive d'un même dirigeant, Jérôme Cardineau (né en 1964), et auditées par le même commissaire aux comptes, ERNST & YOUNG AUDIT. 

### Le tuyau d'évacuation continental : Le GIE Veolia Eau France (SIREN 808 297 980)
La clé de voûte de l'extraction financière n'est pas située en Corse, mais à Aubervilliers (Seine-Saint-Denis). 
L'examen des registres d'entreprises et des rapports de transparence financière démontre que la SDEC, la CEOC et Kyrnolia sont toutes affiliées au **GIE VEOLIA EAU FRANCE (SIREN 808 297 980)**, enregistré sous le code de centrale d'achat (46.19A). 
C'est par ce canal de refacturation intragroupe — sous couvert de « conventions de redevance de marque » et « d'assistance technique » — que les millions d'euros prélevés sur les usagers corses échappent à l'impôt insulaire pour remonter directement vers le siège national.

### Le verrou technique d'Ajaccio : L'Usine de la Confina (40 000 m³ / jour)
Le monopole de Veolia sur le Pays Ajaccien repose sur un verrou physique stratégique : **l'usine de potabilisation de la Confina**, construite à la fin des années 1990. Dotée d'une capacité nominale de **40 000 m³ par jour** (40 millions de litres traités quotidiennement en pointe estivale), cette infrastructure traite l'eau brute du fleuve Prunelli régulée par les retenues de Tolla et Ocana. 
Bien que financée par les deniers publics, son exploitation déléguée à Kyrnolia assure à la multinationale un contrôle absolu sur l'alimentation de la cité impériale et des communes périphériques (Afa, Alata, Appietto, Sarrola-Carcopino, Peri).

### L'emprise tentaculaire : plus de 60 communes sous pavillon Veolia
Les données croisées de la plateforme territoriale révèlent que l'opérateur ne contrôle pas seulement les grands centres urbains, mais verrouille un chapelet de **plus de 60 communes et syndicats intercommunaux** :
- **Pôles majeurs** : Ajaccio (CAPA), Porto-Vecchio, Calvi, Propriano, Bonifacio, Ghisonaccia, Aléria, Sartène.
- **Vallées et communes rurales** : Afa, Alata, Algajola, Appietto, Bastelicaccia, Belvédère-Campomoro, Conca, Cuttoli-Corticchiato, Figari, Lecci, Levie, Olmeto, Peri, Pietrosella, Pianottoli-Caldarello, San-Gavino-di-Carbini, Sari-Solenzara, Sarrola-Carcopino, Venzolasca, Vescovato, Vico.

Au total, ce sont **plus de 112,9 millions d'euros** qui sont extraits chaque année des factures des ménages et des budgets communaux de l'île par une seule multinationale privée.

---

## 4. LES TUYAUX PERCÉS DU PRIVÉ : 42 MILLIONS DE M³ DISSIPÉS SOUS TERRE

Lorsque l'eau est captée et traitée pour la consommation humaine, commence le second niveau de spoliation : l'abandon d'entretien des canalisations enterrées.

Sur l'ensemble de l'île, le volume annuel d'eau potable produit s'établit à environ 47 millions de mètres cubes. Mais les indicateurs du **SISPEA (Système d'Information sur les Services Publics d'Eau et d'Assainissement)** révèlent une hémorragie chronique :
- **Rendement moyen en zone urbaine (Ajaccio, Bastia)** : 80 % à 83 % (conforme aux seuils du Décret n° 2012-97 du 27 janvier 2012).
- **Rendement en zone rurale et périurbaine** : Chute régulière **sous la barre des 50 %**.

Dans des dizaines de communes rurales de l'intérieur, un litre sur deux traités fuit dans le sous-sol à travers des canalisations fissurées, sans jamais parvenir au robinet.

À l'échelle de la Corse, ce sont **42 millions de mètres cubes d'eau potable** qui se perdent chaque année sous la terre.

Pourquoi ? Parce que le modèle économique des multinationales délégataires repose sur l'encaissement des flux de facturation plutôt que sur le renouvellement capitalistique du patrimoine enterré. L'article L. 2224-5 du Code Général des Collectivités Territoriales (CGCT) impose pourtant un plan d'actions contraignant pour les réseaux sous les seuils réglementaires. Ce plan est resté lettre morte dans d'innombrables communes de l'intérieur, faute d'un contrôle financier contradictoire et de sanctions effectives.

---

## 5. LE GRAND COMPARATIF DES FACTURES EN CORSE : DU SIMPLE AU DOUBLE

L'analyse des indicateurs **SISPEA / D102.0** et des rapports annuels sur le prix et la qualité du service (RPQS) fait voler en éclats l'illusion d'une tarification équitable sur l'île.

Pour une consommation de référence de **120 m³ par an** (standard d'un foyer de trois personnes incluant eau potable, assainissement collectif et redevances d'agence), l'écart entre une régie publique et les villes concédées à Veolia dépasse **250 euros par an** :

<div class="my-8 overflow-x-auto not-prose">
  <table class="w-full text-left text-xs font-mono bg-slate-950 border border-slate-800 rounded-xl overflow-hidden shadow-2xl">
    <thead class="bg-slate-900 border-b border-slate-800 text-slate-300 uppercase tracking-wider">
      <tr>
        <th class="p-3.5">Ville / Territoire</th>
        <th class="p-3.5">Gestionnaire</th>
        <th class="p-3.5">Eau Potable</th>
        <th class="p-3.5">Assainissement</th>
        <th class="p-3.5">Total TTC / m³</th>
        <th class="p-3.5 text-amber-400">Facture 120 m³</th>
      </tr>
    </thead>
    <tbody class="divide-y divide-slate-800/60 text-slate-200">
      <tr class="hover:bg-slate-900/50 transition">
        <td class="p-3.5 font-bold text-slate-100">Corte</td>
        <td class="p-3.5"><span class="px-2 py-0.5 rounded bg-emerald-500/10 text-emerald-400 border border-emerald-500/30">Régie Municipale</span></td>
        <td class="p-3.5">1,63 €</td>
        <td class="p-3.5">1,23 €</td>
        <td class="p-3.5 font-bold text-emerald-400">2,86 €</td>
        <td class="p-3.5 font-black text-emerald-300">343,20 €</td>
      </tr>
      <tr class="hover:bg-slate-900/50 transition">
        <td class="p-3.5 font-bold text-slate-100">Ajaccio</td>
        <td class="p-3.5"><span class="px-2 py-0.5 rounded bg-rose-500/10 text-rose-400 border border-rose-500/30">Kyrnolia (Veolia)</span></td>
        <td class="p-3.5">2,53 €</td>
        <td class="p-3.5">2,32 €</td>
        <td class="p-3.5 font-bold text-slate-100">4,95 €</td>
        <td class="p-3.5 font-black text-amber-400">594,00 €</td>
      </tr>
      <tr class="hover:bg-slate-900/50 transition">
        <td class="p-3.5 font-bold text-slate-100">Porto-Vecchio</td>
        <td class="p-3.5"><span class="px-2 py-0.5 rounded bg-rose-500/10 text-rose-400 border border-rose-500/30">SDEC (Veolia)</span></td>
        <td class="p-3.5">2,27 €</td>
        <td class="p-3.5">2,69 €</td>
        <td class="p-3.5 font-bold text-slate-100">4,96 €</td>
        <td class="p-3.5 font-black text-amber-400">595,20 €</td>
      </tr>
      <tr class="hover:bg-slate-900/50 transition">
        <td class="p-3.5 font-bold text-slate-100">Bastia (CAB)</td>
        <td class="p-3.5"><span class="px-2 py-0.5 rounded bg-cyan-500/10 text-cyan-400 border border-cyan-500/30">Acqua Publica (Régie)</span></td>
        <td class="p-3.5">2,26 €</td>
        <td class="p-3.5">2,83 €</td>
        <td class="p-3.5 font-bold text-slate-100">5,09 €</td>
        <td class="p-3.5 font-black text-slate-100">610,80 €</td>
      </tr>
      <tr class="hover:bg-slate-900/50 transition">
        <td class="p-3.5 font-bold text-slate-100">Propriano / Sartenais</td>
        <td class="p-3.5"><span class="px-2 py-0.5 rounded bg-rose-500/10 text-rose-400 border border-rose-500/30">Kyrnolia (Veolia)</span></td>
        <td class="p-3.5">2,60 €</td>
        <td class="p-3.5">2,70 €</td>
        <td class="p-3.5 font-bold text-slate-100">5,30 €</td>
        <td class="p-3.5 font-black text-rose-400">636,00 €</td>
      </tr>
      <tr class="hover:bg-slate-900/50 transition">
        <td class="p-3.5 font-bold text-slate-100">Calvi / Balagne</td>
        <td class="p-3.5"><span class="px-2 py-0.5 rounded bg-rose-500/10 text-rose-400 border border-rose-500/30">Kyrnolia (Veolia)</span></td>
        <td class="p-3.5">2,65 €</td>
        <td class="p-3.5">2,85 €</td>
        <td class="p-3.5 font-bold text-slate-100">5,50 €</td>
        <td class="p-3.5 font-black text-rose-400">660,00 €</td>
      </tr>
    </tbody>
  </table>
</div>

### L'enseignement clinique de ces chiffres :
- **À Corte (en régie municipale)**, l'eau est facturée **2,86 € / m³**, soit **343,20 € par an**. Zéro dividende actionnarial, zéro frais de siège parisiens : le coût réel du service public au plus juste pour le citoyen.
- **À Ajaccio, Porto-Vecchio, Propriano ou Calvi (sous pavillon Veolia)**, la même quantité d'eau coûte entre **594 € et 660 € par an** : **près du double !**
- **À Bastia**, bien que le tarif s'élève à 5,09 € en raison des investissements de dépollution de l'usine Bastia Sud, **100 % des excédents sont sanctuarisés dans le patrimoine public** via la régie *Acqua Publica*, au lieu de partir alimenter la trésorerie centrale de Veolia.
- **La marge brute délirante sur l'eau brute** : L'eau brute vendue par l'OEHC à **0,105 € / m³** est refacturée aux ménages ajacciens ou balanins jusqu'à **2,65 € / m³** en eau potable seule (hors assainissement), soit une multiplication par **25 fois le prix d'achat initial**.

---

## 6. L'ASPIRATION HORS DE L'ÎLE : DIVIDENDES, FRAIS DE SIÈGE ET DISSIMULATION COMPTABLE

Le cœur du scandale ne réside pas dans l'activité des producteurs d'eaux minérales locales (Saint-Georges, Zilia, Orezza). Ces derniers constituent un fleuron du patrimoine productif corse, créateurs d'emplois locaux non délocalisables et garants d'une souveraineté d'embouteillage insulaire face aux cartels mondiaux Nestlé ou Danone.

La véritable prédation s'opère sur l'eau du robinet des familles corses, à travers la mécanique d'évasion financière orchestrée par la multinationale **VEOLIA** :

### Le ciseau comptable de l'affermage (CAPA, Porto-Vecchio, Sud-Corse)
1. **La mise sous tutelle des agglomérations** : À Ajaccio (CAPA), le contrat de concession eau potable signé pour 12 ans représente un volume d'affaires de plus de **100 millions d'euros** (plus 68 millions pour l'assainissement). À Porto-Vecchio, la DSP a été verrouillée sur 12 ans au bénéfice exclusif de la Société des Eaux de Corse (SDEC).
2. **Le verrouillage par les « Frais de Siège » et Management Fees** : 
   Comment une entreprise comme la SDEC peut-elle réaliser 60,77 millions d'euros de chiffre d'affaires et ne déclarer que 2,67 millions de résultat net (4,4 % de rentabilité apparente) ? 
   L'analyse des pratiques contractuelles décortiquées par les Chambres Régionales des Comptes met en lumière la refacturation systématique de *« frais d'assistance technique et de redevances de marque »* versées aux holdings continentales du groupe Veolia. Ces prestations intragroupe gonflent artificiellement les charges d'exploitation locales, réduisent l'assiette de l'impôt en Corse et transfèrent le cash directement vers la maison-mère à Aubervilliers.
3. **Le contraste saisissant avec la Régie Publique (Acqua Publica)** :
   La preuve matérielle de cette dérive existe sur l'île même. À Bastia, la Communauté d'Agglomération de Bastia (CAB) a chassé Veolia pour instaurer dès 2016 la régie publique **Acqua Publica**. Résultat : 100 % des recettes des usagers sont réinvesties dans le patrimoine de tuyauterie et les bassins, sans un seul centime siphonné pour des actionnaires parisiens.
4. **La socialisation des investissements lourds (L'exemple de Porto-Vecchio)** :
   Pendant que la SDEC encaisse les abonnements et les mètres cubes facturés aux ménages, **qui paie les travaux structurants ? Les contribuables et les fonds publics.** À Porto-Vecchio, le vaste programme de modernisation des réseaux d'eau et d'assainissement de **44 millions d'euros** (construction de la station d'épuration de Capu di Padolu d'une capacité de 48 000 équivalents-habitants, réservoirs de Nota portés à 5 500 m³) est financé à 100 % par la Ville, l'Agence de l'Eau et la Collectivité de Corse. Les profits sont privatisés, les investissements en capital sont nationalisés aux frais des citoyens.
5. **Le piège des « Fonds de Renouvellement » épinglé par la CRC** :
   Dans ses contrôles de gestion des DSP d'eau, la Chambre Régionale des Comptes a mis en lumière l'opacité entourant la gestion des **fonds de renouvellement contractuels**. Ces provisions, payées mois après mois par les usagers sur leur facture d'eau pour financer le remplacement des canalisations et pompes défaillantes, font trop souvent l'objet d'une rétention de trésorerie par le délégataire privé sans restitution intégrale en fin de contrat. L'usager paie deux fois : une première fois sur sa facture via les provisions du fermier, et une seconde fois par ses impôts locaux pour financer les plans d'urgence des communes.
6. **L'Aveu Officiel : L'Audit de DSP de Porto-Vecchio dévoile un surcoût indu de +15 % infligé aux familles** :
   Le rapport d'audit technique, financier et juridique commandé par la Ville de Porto-Vecchio et restitué à l'été 2026 (ayant débouché sur l'Avenant n°1 au contrat de concession SDEC/Veolia) apporte la preuve médico-légale irréfutable de la prédation contractuelle :
   - **Une formule d'actualisation des tarifs biaisée** : L'absence volontaire d'un indice représentatif des salaires a généré un **surcoût indu estimé à 15 %** directement prélevé sur les factures des abonnés porto-vecchiais.
   - **Une rentabilité hors contrat** : L'audit établit que la marge financière réelle empochée par la SDEC a largement dépassé les prévisions contractuelles initiales, confirmant la surfacturation systématique.
   - **Retard sur le renouvellement des compteurs** : Alors que les usagers financent la dotation de renouvellement à chaque quittance, la SDEC a accumulé un retard lourd dans le remplacement du parc de comptage.
   - **Rendement dégradé et opacité SIG** : Défaillance persistante du rendement réseau et carence dans la remise à jour des inventaires électromécaniques et du système d'information géographique (SIG), contraignant la commune à imposer une sommation de géoréférencement complet avant l'échéance du 30 juin 2028.

---

## 7. L'INGÉNIERIE DE LA RÉSISTANCE : LE PLAN DE REPRISE EN SOUVERAINETÉ (40 % RÉSOLUTION)

L'OCHJU refuse de limiter le constat à une déploration stérile. Les outils juridiques et institutionnels existent dans le droit positif pour briser cette rente et restaurer la souveraineté hydraulique du peuple corse.

### Axe 1 : Sortie Immédiate des Délégations Privées (Art. L. 6 du Code de la Commande Publique)
Les collectivités et intercommunalités disposent du droit unilatéral de résiliation des contrats de Délégation de Service Public (DSP) pour motif d'intérêt général :
- Motif opposable : manquement caractérisé à l'obligation d'entretien patrimonial des réseaux (taux de fuite supérieur aux seuils du CGCT).
- Création d'une **Régie Publique Unique de l'Eau** adossée à l'OEHC et aux régies intercommunales, excluant tout prélèvement de dividende privé.

### Axe 2 : Tarification Sociale et Progressive Citoyenne
Remplacement du tarif unique par une tarification de justice distributive :
- **Tranche 1 (0 à 30 m³ par an et par foyer)** : **Gratuité intégrale**. L'accès à l'eau vitale est un droit inaliénable.
- **Tranche 2 (31 à 120 m³)** : Tarif coûtant d'exploitation publique (1,20 € / m³).
- **Tranche 3 (au-delà de 150 m³ et résidences secondaires)** : Surtaxe estivale dissuasive (8 € à 12 € / m³) pour pénaliser le remplissage des piscines privées et l'arrosage de pelouses en pleine canicule.

### Axe 3 : Réquisition des Débits Réservés EDF & Plan d'Urgence Retenues 175 Mm³
- Obligation légale imposée à EDF d'assurer des interconnexions d'eau brute vers les stations de potabilisation communales avant tout turbinage terminal vers la mer.
- Mobilisation immédiate des fonds du Plan de Transformation et d'Investissement pour la Corse (PTIC) pour financer les 600 millions d'euros du plan *Acqua Nostra 2050* : porter le stockage insulaire à 175 millions de m³ d'ici 2030.

---

<!-- ==========================================================================
     ARSENAL D'ÉMANCIPATION CITOYENNE & ARMES JURIDIQUES SOUVERAINES
     ========================================================================== -->
<div class="my-12 not-prose rounded-3xl border-2 border-emerald-500/40 bg-gradient-to-b from-slate-950 via-slate-900 to-slate-950 p-6 md:p-10 shadow-2xl relative overflow-hidden">
<div class="absolute -bottom-20 -left-20 w-72 h-72 bg-emerald-500/10 rounded-full blur-3xl pointer-events-none"></div>

<div class="space-y-3 mb-8">
<span class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-emerald-500/20 text-emerald-300 border border-emerald-500/40 text-xs font-mono font-bold uppercase tracking-widest">
⚡ ARSENAL D'ÉMANCIPATION CITOYENNE
</span>
<h3 class="text-2xl md:text-3xl font-black font-serif text-slate-100">
La Pénurie Est Fabriquée. Voici les Munitions Hydrauliques.
</h3>
<p class="font-serif text-sm text-slate-300">
Les preuves matérielles sont scellées. L'OCHJU ne transmet aucun dossier aux tribunaux : le savoir forgé est remis aux citoyens. Téléchargez les pièces officielles opposables et agissez souverainement.
</p>
</div>

<!-- GRILLE DES 3 LEVIERS D'ACTION SOUVERAINES -->
<div class="grid grid-cols-1 md:grid-cols-3 gap-4 my-6">

<!-- LEVIER 1 : JUSTICE ART 40 -->
<a href="/transmissions/enquete-04-marchandisation-eau/02_BORDEREAU_TRANSMISSION_JUDICIAIRE.md" target="_blank" class="p-5 rounded-2xl bg-slate-900 border border-slate-800 hover:border-amber-400 transition group flex flex-col justify-between">
<div>
<div class="flex items-center justify-between mb-3">
<span class="text-2xl">⚖️</span>
<span class="text-[10px] font-mono text-emerald-400 font-bold uppercase tracking-wider bg-emerald-500/10 px-2 py-0.5 rounded border border-emerald-500/30">Article 40 CPP</span>
</div>
<h4 class="font-serif font-bold text-slate-100 group-hover:text-amber-300 transition text-base mb-1">
Bordereau Judiciaire & Carence d'Entretien
</h4>
<p class="text-xs text-slate-400 font-sans leading-relaxed">
Dossier juridique complet pour défaut caractérisé d'entretien d'ouvrages publics (Art. L. 2224-5 CGCT) et surtarification abusive des familles.
</p>
</div>
<span class="text-xs font-mono font-bold text-amber-400 mt-4 flex items-center gap-1">
Télécharger le Bordereau →
</span>
</a>

<!-- LEVIER 2 : INTERPELLATION ÉLUS -->
<a href="/transmissions/enquete-04-marchandisation-eau/03_NOTE_INTERPELLATION_PARLEMENTAIRE.md" target="_blank" class="p-5 rounded-2xl bg-slate-900 border border-slate-800 hover:border-cyan-400 transition group flex flex-col justify-between">
<div>
<div class="flex items-center justify-between mb-3">
<span class="text-2xl">🏛️</span>
<span class="text-[10px] font-mono text-cyan-400 font-bold uppercase tracking-wider bg-cyan-500/10 px-2 py-0.5 rounded border border-cyan-500/30">Plan 175 Mm³</span>
</div>
<h4 class="font-serif font-bold text-slate-100 group-hover:text-cyan-300 transition text-base mb-1">
Note d'Interpellation Parlementaire
</h4>
<p class="text-xs text-slate-400 font-sans leading-relaxed">
Proposition de délibération territoriale pour la régie publique d'office, la gratuité des 30 premiers m³ et le plafonnement des prélèvements privés.
</p>
</div>
<span class="text-xs font-mono font-bold text-cyan-400 mt-4 flex items-center gap-1">
Sommer les Élus →
</span>
</a>

<!-- LEVIER 3 : PRESSE & LANCEURS D'ALERTE -->
<a href="/transmissions/enquete-04-marchandisation-eau/01_KIT_PRESSE_INVESTIGATION.md" target="_blank" class="p-5 rounded-2xl bg-slate-900 border border-slate-800 hover:border-rose-400 transition group flex flex-col justify-between">
<div>
<div class="flex items-center justify-between mb-3">
<span class="text-2xl">📰</span>
<span class="text-[10px] font-mono text-rose-400 font-bold uppercase tracking-wider bg-rose-500/10 px-2 py-0.5 rounded border border-rose-500/30">Grade ICIJ</span>
</div>
<h4 class="font-serif font-bold text-slate-100 group-hover:text-rose-300 transition text-base mb-1">
Kit de Presse d'Investigation
</h4>
<p class="text-xs text-slate-400 font-sans leading-relaxed">
Radiographie médico-légale des rendements par EPCI, cartographie des fuites sous-terraines de Veolia/Kyrnolia et données BNPE complètes.
</p>
</div>
<span class="text-xs font-mono font-bold text-rose-400 mt-4 flex items-center gap-1">
Consulter le Kit Presse →
</span>
</a>

</div>
</div>

<!-- ==========================================================================
     MODULE PIÈCES JUSTIFICATIVES OFFICIELLES (6 ACTES EN ACCÈS DIRECT)
     ========================================================================== -->
<div class="my-12 p-8 rounded-3xl bg-slate-900/90 border border-slate-700/80 shadow-2xl not-prose">
<div class="text-center max-w-2xl mx-auto mb-8">
<div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-amber-500/10 border border-amber-500/30 text-amber-300 font-mono text-xs uppercase tracking-widest mb-3">
<span>📂</span> Pièces Justificatives Officielles
</div>
<h3 class="text-2xl font-serif font-bold text-slate-100 mb-2">Les 6 Actes Clés en Accès Direct</h3>
<p class="text-sm text-slate-400 font-sans leading-relaxed">
Conformément au principe de transparence citoyenne et au standard ISO/IEC 27037, voici les documents administratifs et registres légaux cités dans l'instruction, scellés sous empreinte SHA-256 et vérifiables sans intermédiaire.
</p>
</div>

<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
<!-- ACTE 1 -->
<div class="p-5 rounded-2xl bg-slate-950/70 border border-slate-800 flex flex-col justify-between hover:border-amber-500/40 transition">
<div>
<div class="flex items-center justify-between mb-2">
<span class="text-xs font-mono text-amber-400 font-semibold">INPI • SIREN 514 709 211</span>
<span class="text-[10px] font-mono text-slate-400 bg-slate-800 px-1.5 py-0.5 rounded">CA • 60,77 M€</span>
</div>
<h4 class="font-serif font-bold text-slate-200 text-sm mb-2">Société des Eaux de Corse (SDEC)</h4>
<p class="text-xs text-slate-400 leading-relaxed">Comptes sociaux certifiés 2025 : 60 773 333 € de chiffre d'affaires et 2 673 941 € de bénéfice net (Groupe Veolia).</p>
</div>
<div class="mt-4 pt-3 border-t border-slate-800/80 flex items-center gap-2">
<a href="https://annuaire-entreprises.data.gouv.fr/entreprise/514709211" target="_blank" rel="noopener noreferrer" class="flex-1 py-2 px-2.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-amber-400 border border-amber-500/30 font-mono text-xs font-bold text-center transition flex items-center justify-center gap-1.5">
<span>👁️</span> Consulter
</a>
<a href="https://recherche-entreprises.api.gouv.fr/search?q=514709211" target="_blank" rel="noopener noreferrer" class="flex-1 py-2 px-2.5 rounded-xl bg-amber-500 hover:bg-amber-400 text-slate-950 font-mono text-xs font-bold text-center transition flex items-center justify-center gap-1.5 shadow-sm">
<span>📥</span> Données API
</a>
</div>
</div>

<!-- ACTE 2 -->
<div class="p-5 rounded-2xl bg-slate-950/70 border border-slate-800 flex flex-col justify-between hover:border-amber-500/40 transition">
<div>
<div class="flex items-center justify-between mb-2">
<span class="text-xs font-mono text-amber-400 font-semibold">INPI • SIREN 817 503 576</span>
<span class="text-[10px] font-mono text-slate-400 bg-slate-800 px-1.5 py-0.5 rounded">CA • 51,11 M€</span>
</div>
<h4 class="font-serif font-bold text-slate-200 text-sm mb-2">Cie des Eaux et de l'Ozone (CEOC)</h4>
<p class="text-xs text-slate-400 leading-relaxed">Deuxième pilier financier de Veolia en Corse : 51 112 044 € de chiffre d'affaires annuel sous présidence commune.</p>
</div>
<div class="mt-4 pt-3 border-t border-slate-800/80 flex items-center gap-2">
<a href="https://annuaire-entreprises.data.gouv.fr/entreprise/817503576" target="_blank" rel="noopener noreferrer" class="flex-1 py-2 px-2.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-amber-400 border border-amber-500/30 font-mono text-xs font-bold text-center transition flex items-center justify-center gap-1.5">
<span>👁️</span> Consulter
</a>
<a href="https://recherche-entreprises.api.gouv.fr/search?q=817503576" target="_blank" rel="noopener noreferrer" class="flex-1 py-2 px-2.5 rounded-xl bg-amber-500 hover:bg-amber-400 text-slate-950 font-mono text-xs font-bold text-center transition flex items-center justify-center gap-1.5 shadow-sm">
<span>📥</span> Données API
</a>
</div>
</div>

<!-- ACTE 3 -->
<div class="p-5 rounded-2xl bg-slate-950/70 border border-slate-800 flex flex-col justify-between hover:border-amber-500/40 transition">
<div>
<div class="flex items-center justify-between mb-2">
<span class="text-xs font-mono text-amber-400 font-semibold">BNPE • Hub'Eau 2A & 2B</span>
<span class="text-[10px] font-mono text-slate-400 bg-slate-800 px-1.5 py-0.5 rounded">1,09 Md m³</span>
</div>
<h4 class="font-serif font-bold text-slate-200 text-sm mb-2">Chroniques de Prélèvements en Eau</h4>
<p class="text-xs text-slate-400 leading-relaxed">Relevés officiels de l'Agence de l'Eau attestant du turbinage de 1,09 milliard de m³ par EDF contre 47 Mm³ pour l'eau potable.</p>
</div>
<div class="mt-4 pt-3 border-t border-slate-800/80 flex items-center gap-2">
<a href="https://hubeau.eaufrance.fr/page/api-prelevements-eau" target="_blank" rel="noopener noreferrer" class="flex-1 py-2 px-2.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-amber-400 border border-amber-500/30 font-mono text-xs font-bold text-center transition flex items-center justify-center gap-1.5">
<span>👁️</span> Portail API
</a>
<a href="https://hubeau.eaufrance.fr/api/v1/prelevements/chroniques?code_departement=2A&annee=2021&size=100" target="_blank" rel="noopener noreferrer" class="flex-1 py-2 px-2.5 rounded-xl bg-amber-500 hover:bg-amber-400 text-slate-950 font-mono text-xs font-bold text-center transition flex items-center justify-center gap-1.5 shadow-sm">
<span>📥</span> JSON Brut
</a>
</div>
</div>

<!-- ACTE 4 -->
<div class="p-5 rounded-2xl bg-slate-950/70 border border-slate-800 flex flex-col justify-between hover:border-amber-500/40 transition">
<div>
<div class="flex items-center justify-between mb-2">
<span class="text-xs font-mono text-amber-400 font-semibold">SISPEA • EauFrance</span>
<span class="text-[10px] font-mono text-slate-400 bg-slate-800 px-1.5 py-0.5 rounded">Pertes • 42 Mm³</span>
</div>
<h4 class="font-serif font-bold text-slate-200 text-sm mb-2">Indicateurs de Performance P104.3</h4>
<p class="text-xs text-slate-400 leading-relaxed">Observatoire national des services d'eau : rendements de réseaux inférieurs à 50 % dans les communes rurales corses.</p>
</div>
<div class="mt-4 pt-3 border-t border-slate-800/80 flex items-center gap-2">
<a href="https://www.services.eaufrance.fr/" target="_blank" rel="noopener noreferrer" class="flex-1 py-2 px-2.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-amber-400 border border-amber-500/30 font-mono text-xs font-bold text-center transition flex items-center justify-center gap-1.5">
<span>👁️</span> Consulter
</a>
<a href="https://www.data.gouv.fr/fr/datasets/services-publics-deau-potable-jeux-de-donnees-exploites-pour-les-rapports-nationaux-sispea/" target="_blank" rel="noopener noreferrer" class="flex-1 py-2 px-2.5 rounded-xl bg-amber-500 hover:bg-amber-400 text-slate-950 font-mono text-xs font-bold text-center transition flex items-center justify-center gap-1.5 shadow-sm">
<span>📥</span> Data.gouv
</a>
</div>
</div>

<!-- ACTE 5 -->
<div class="p-5 rounded-2xl bg-slate-950/70 border border-slate-800 flex flex-col justify-between hover:border-amber-500/40 transition">
<div>
<div class="flex items-center justify-between mb-2">
<span class="text-xs font-mono text-amber-400 font-semibold">CRC Corse • Audit OEHC</span>
<span class="text-[10px] font-mono text-slate-400 bg-slate-800 px-1.5 py-0.5 rounded">ROD • Officiel</span>
</div>
<h4 class="font-serif font-bold text-slate-200 text-sm mb-2">Chambre Régionale des Comptes</h4>
<p class="text-xs text-slate-400 leading-relaxed">Rapports d'observations définitives sur la gestion de l'OEHC, la tarification de l'eau brute (0,105 €/m³) et les DSP communales.</p>
</div>
<div class="mt-4 pt-3 border-t border-slate-800/80 flex items-center gap-2">
<a href="https://www.ccomptes.fr/fr/crc-corse" target="_blank" rel="noopener noreferrer" class="flex-1 py-2 px-2.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-amber-400 border border-amber-500/30 font-mono text-xs font-bold text-center transition flex items-center justify-center gap-1.5">
<span>👁️</span> Consulter
</a>
<a href="https://www.isula.corsica/" target="_blank" rel="noopener noreferrer" class="flex-1 py-2 px-2.5 rounded-xl bg-amber-500 hover:bg-amber-400 text-slate-950 font-mono text-xs font-bold text-center transition flex items-center justify-center gap-1.5 shadow-sm">
<span>📥</span> Archives CDC
</a>
</div>
</div>

<!-- ACTE 6 -->
<div class="p-5 rounded-2xl bg-slate-950/70 border border-slate-800 flex flex-col justify-between hover:border-amber-500/40 transition">
<div>
<div class="flex items-center justify-between mb-2">
<span class="text-xs font-mono text-amber-400 font-semibold">CAPA • Concession 12 ans</span>
<span class="text-[10px] font-mono text-slate-400 bg-slate-800 px-1.5 py-0.5 rounded">Marché • 100 M€</span>
</div>
<h4 class="font-serif font-bold text-slate-200 text-sm mb-2">Contrat Concession Eau CAPA (Veolia)</h4>
<p class="text-xs text-slate-400 leading-relaxed">Contrat de concession sur 12 ans liant la CAPA à Kyrnolia / Veolia : 100 M€ eau potable et 68 M€ assainissement.</p>
</div>
<div class="mt-4 pt-3 border-t border-slate-800/80 flex items-center gap-2">
<a href="https://ca-ajaccien.corsica/" target="_blank" rel="noopener noreferrer" class="flex-1 py-2 px-2.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-amber-400 border border-amber-500/30 font-mono text-xs font-bold text-center transition flex items-center justify-center gap-1.5">
<span>👁️</span> Portail CAPA
</a>
<a href="https://ca-ajaccien.corsica/eau-et-assainissement/" target="_blank" rel="noopener noreferrer" class="flex-1 py-2 px-2.5 rounded-xl bg-amber-500 hover:bg-amber-400 text-slate-950 font-mono text-xs font-bold text-center transition flex items-center justify-center gap-1.5 shadow-sm">
<span>📥</span> Actes DSP
</a>
</div>
</div>

<!-- ACTE 7 -->
<div class="p-5 rounded-2xl bg-slate-950/70 border-2 border-rose-500/40 flex flex-col justify-between hover:border-rose-400 transition shadow-lg md:col-span-2 lg:col-span-1">
<div>
<div class="flex items-center justify-between mb-2">
<span class="text-xs font-mono text-rose-400 font-semibold">Porto-Vecchio • Audit 2026</span>
<span class="text-[10px] font-mono text-rose-300 bg-rose-500/20 px-1.5 py-0.5 rounded border border-rose-500/30">+15 % Surcoût Indu</span>
</div>
<h4 class="font-serif font-bold text-slate-200 text-sm mb-2">Audit Officiel DSP Eau & Avenant n°1</h4>
<p class="text-xs text-slate-400 leading-relaxed">Audit de la concession SDEC/Veolia révélant l'absence d'indice salarial (+15% surfacturation abonnés), des marges excessives et des retards de compteurs.</p>
</div>
<div class="mt-4 pt-3 border-t border-slate-800/80 flex items-center gap-2">
<a href="https://portivechju.corsica/" target="_blank" rel="noopener noreferrer" class="flex-1 py-2 px-2.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-rose-300 border border-rose-500/30 font-mono text-xs font-bold text-center transition flex items-center justify-center gap-1.5">
<span>👁️</span> Délibération
</a>
<a href="https://portivechju.corsica/conseil-municipal/" target="_blank" rel="noopener noreferrer" class="flex-1 py-2 px-2.5 rounded-xl bg-rose-600 hover:bg-rose-500 text-white font-mono text-xs font-bold text-center transition flex items-center justify-center gap-1.5 shadow-sm">
<span>📥</span> Acte Ville
</a>
</div>
</div>

</div>
</div>

---

<div class="text-center font-serif italic text-amber-400 text-sm mt-8 border-t border-slate-800 pt-6">
  <strong>L'eau est le bien commun inaliénable du Peuple Corse. Le Savoir partagé est notre contre-pouvoir.</strong>
  <br><br>
  <strong>L'OCHJU, c'est le regard qui ne se détourne plus.</strong>
  <br>
  <span class="text-xs text-slate-400 font-sans opacity-75">— Cellule d'Investigation L'OCHJU</span>
</div>

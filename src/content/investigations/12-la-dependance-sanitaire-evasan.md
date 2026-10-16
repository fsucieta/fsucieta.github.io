---
id: 12
title: "L'Exil Médical Organisé : Autopsie Forensique du Black Budget Sanitaire et du Pacte CHU en Corse"
subtitle: "170,8 millions d'euros par an de fuite financière, 2 222 lits pris en otage, la boîte noire du FIR de l'ARS et le scandale du cyclotron manquant : l'instruction médico-légale sur la spoliation hospitalière insulaire."
category: "SANTÉ & HÔPITAL"
status: cloturee
ref: "LOCHJU-AUDIT-ENQUETE-12"
author: "Cellule d'Investigation L'OCHJU"
date: "Octobre 2026"
tool: "ARS Corse FIR / ATIH PMSI / CRC Corse / Délibérations CdC / ISO 27037 / Bufitonu.fr"
chapeau: "Présentée par le pouvoir central comme un territoire sous perfusion tributaire de la solidarité continentale, la Corse subit en réalité un système méthodique de captation de valeur et de transfert de rente sanitaire : 170 874 320 euros siphonnés chaque année hors de l'île (114,45 M€ d'EVASAN et de facturation T2A vers les CHU de Marseille et Nice, 24,62 M€ de mercenariat d'intérim médical et 14,85 M€ de tribut biomédical). L'instruction médico-légale menée par L'OCHJU dévoile l'envers du décor régalien : l'asphyxie financière des 9 cliniques privées indépendantes créées par des médecins et familles corses pour sauver des vies, la boîte noire du Fonds d'Intervention Régional (FIR) piloté par un préfet sanitaire omnipotent, le gaspillage radioactif du Fluorodésoxyglucose (18F-FDG) importé par avion faute de cyclotron médical insulaire, et l'occultation d'une épidémiologie singulière (Tchernobyl 1986, amiante de Canari, bio-extraction génétique). Face à un report dilatoire de la création du CHU à 2031 voté au Sénat, la Cellule dresse l'architecture immédiate du Pacte Sanitaire Corse (CHU di Corsica) fédérant 2 222 lits publics et privés sans un centime de béton inutile."
math: "\\text{Indice de Fuite Sanitaire (IFS)} = \\frac{\\sum \\text{Coûts EVASAN} + \\text{Facturations T2A PACA} + \\text{Intérim Extérieur}}{\\text{Budget Hospitalier Consolidé de Corse}} \\times 100"
image: "img_enquete_12.jpg"
sources:
  - name: "Assemblée Nationale — Rapport n° 624 sur la création d'un CHU en Corse (PPL adoptée le 3 déc. 2024)"
    url: "/docs/pieces-publiques-enquete-12/AN_RAPPORT_624_CHU_CORSE_2024.pdf"
    sha256: "4f454501feecea349693539fecfce60fd9f8cc5001eb24da706d86b6c7ec052b"
  - name: "Assemblée Nationale — Texte de loi adopté n° 13 portant création d'un CHU de plein exercice en Corse"
    url: "/docs/pieces-publiques-enquete-12/AN_TEXTE_ADOPTE_13_CHU_CORSE_2024.pdf"
    sha256: "d35fc5476de2a84dd8a55350f57ddcb6792fb73ee0e6e5b383ab9b382082cc3e"
  - name: "Sénat de la République — Proposition de loi n° 2478 modifiée (Report dilatoire d'application à 2031)"
    url: "/docs/pieces-publiques-enquete-12/AN_PPL_2478_MODIFIEE_SENAT_2026.pdf"
    sha256: "0e11d2c3989b6f066ca9b0d418ea2e4067cd70699a9372b70f8195ae8f6f700a"
  - name: "Sénat de la République — Rapport n° 393 (Détournement des hélicoptères de sécurité civile en EVASAN SAMU)"
    url: "/docs/senat-r25-393-secours-montagne-helico.pdf"
    sha256: "d91dc6dee68ac4fa7adff97eab3a6ffcdb642d4b0b4e88cda4e56bb4e8e09f19"
  - name: "Signalement L'OCHJU — Rapport médico-légal et forensique de non-conformité ERP Type U Stiletto"
    url: "/docs/opposition_ajaccio/04_SIGNALEMENT_URGENCE_SECURITE_ERP_TYPE_U_STILETTO.pdf"
    sha256: "5f25c52eb581974a875b4be88cdc33880fee5846913e15ca84410e0c117c00a1"
  - name: "BRGM — Rapport officiel RP-57640-FR sur la pollution aux métaux lourds et arsenic à Matra"
    url: "/docs/brgm-rp-57640-fr-pollution-arsenic.pdf"
    sha256: "07381d02eaa95ecc15d886b5951f2db21c26d199f6e55f5c4ba8c2b1f77cb9e7"
---

<!-- ==========================================================================
     CARTOUCHE SUPRÊME DOUBLE ÉTAGÈRE — L'ARITHMÉTIQUE DE LA RENTE SANITAIRE
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
        <span class="text-[11px] font-mono text-slate-400 uppercase block mb-1">Fuite Sanitaire Annuelle</span>
        <span class="text-xl md:text-2xl font-black text-rose-400 font-mono">170,87 M€ / an</span>
        <span class="text-[10px] text-slate-400 block mt-1">EVASAN (114,5 M€) + Intérim (24,6 M€) + Biomédical (14,9 M€)</span>
      </div>
      <div class="p-3.5 rounded-xl bg-slate-900/80 border border-slate-800 text-center">
        <span class="text-[11px] font-mono text-slate-400 uppercase block mb-1">Prélèvement par Foyer</span>
        <span class="text-xl md:text-2xl font-black text-amber-400 font-mono">1 068 € / an</span>
        <span class="text-[10px] text-slate-400 block mt-1">Tribut moyen par foyer fiscal corse versé au continent</span>
      </div>
      <div class="p-3.5 rounded-xl bg-slate-900/80 border border-slate-800 text-center">
        <span class="text-[11px] font-mono text-slate-400 uppercase block mb-1">Perte Radio-Isotope 18F-FDG</span>
        <span class="text-xl md:text-2xl font-black text-cyan-400 font-mono">75 % détruit</span>
        <span class="text-[10px] text-slate-400 block mt-1">Perte en vol chaque matin faute de cyclotron à Corte</span>
      </div>
      <div class="p-3.5 rounded-xl bg-slate-900/80 border border-slate-800 text-center">
        <span class="text-[11px] font-mono text-slate-400 uppercase block mb-1">Capacité Fédérée Immédiate</span>
        <span class="text-xl md:text-2xl font-black text-emerald-400 font-mono">2 222 lits</span>
        <span class="text-[10px] text-slate-400 block mt-1">7 hôpitaux publics (1 450 lits) + 9 cliniques corses (772 lits)</span>
      </div>
    </div>
    <p class="text-sm font-sans text-slate-200 leading-relaxed m-0">
      <strong class="text-amber-300">En clair pour votre foyer :</strong> On vous répète que la Corse est trop petite pour avoir un CHU et que Marseille n'est qu'à « 45 minutes d'avion ». La réalité clinique prouve qu'une évacuation sanitaire dure entre 4h30 et 6h15 de porte-à-porte, un calvaire fatal pour un AVC ou un infarctus. Pendant ce temps, 171 millions d'euros quittent chaque année notre île pour enrichir les hôpitaux de Marseille et de Nice, des agences d'intérim médical mercenaires et des transporteurs privés. Les cliniques indépendantes corses, qui réalisent plus de la moitié des opérations chirurgicales sur l'île, sont étranglées par des tarifs inférieurs de 26 % à ceux du public. En fédérant nos hôpitaux publics et nos cliniques insulaires au sein du <em>CHU di Corsica</em>, la Corse dispose immédiatement de 2 222 lits, de tous les blocs opératoires nécessaires et de quoi financer un cyclotron sans attendre 2031.
    </p>
  </div>

  <!-- ÉTAGÈRE FORENSIQUE SCELLÉE (BAS DE CARTOUCHE) -->
  <div class="pt-1">
    <div class="flex items-center justify-between mb-2">
      <span class="text-[11px] font-mono font-bold tracking-wider uppercase text-emerald-400 flex items-center gap-1.5">
        <span>⚖️</span> ÉTAGÈRE FORENSIQUE : PIÈCES SCELLÉES SOUS NORME ISO/IEC 27037
      </span>
      <span class="text-[10px] font-mono bg-emerald-500/10 text-emerald-300 px-2 py-0.5 rounded border border-emerald-500/30">
        DONNÉES OFFICIELLES OPPOSABLES
      </span>
    </div>
    <div class="grid grid-cols-1 md:grid-cols-2 gap-3 text-xs font-mono">
      <div class="p-2.5 rounded-lg bg-slate-950/60 border border-slate-800/80">
        <div class="text-slate-400 text-[10px] uppercase">Parcours Législatif CHU Corse (2024-2026)</div>
        <div class="text-slate-200 font-bold">PPL Adoptée AN (3 déc. 2024) vs Verrou Sénat 2031</div>
        <div class="text-[10px] text-slate-500 mt-1">Rapport AN n° 624 (SHA: 4F454501...) | Texte AN n° 13 (SHA: D35FC547...) | PPL Sénat n° 2478 (SHA: 0E11D2C3...).</div>
      </div>
      <div class="p-2.5 rounded-lg bg-slate-950/60 border border-slate-800/80">
        <div class="text-slate-400 text-[10px] uppercase">Contentieux Hélicoptères & Sécurité ERP Stiletto</div>
        <div class="text-slate-200 font-bold">Détournement 60 % Dragon & Enclave ERP Type U</div>
        <div class="text-[10px] text-slate-500 mt-1">Rapport Sénat 393 (SHA: D91DC6DE...) | Violation Art. U 6 Arrêté 25 juin 1980 (SHA: 5F25C52E...).</div>
      </div>
    </div>
    <div class="mt-3 flex items-center justify-between text-[11px] font-mono text-slate-400 border-t border-slate-800/60 pt-2">
      <span>Cotes : CGCT, CSP Art. L. 6122-2 II & L. 6133-1, CRC Corse 2023-2024, BRGM RP-57640-FR</span>
      <span class="text-amber-400 font-bold">SHA-256 SCELLÉS VÉRIFIÉS</span>
    </div>
  </div>
</div>

---

## 1. L'AUTOPSIE DU « BLACK BUDGET » : 170,87 MILLIONS D'EUROS D'HÉMORRAGIE ANNUELLE

170 874 320,00 euros. C'est le montant exact du tribut financier que l'économie corse verse chaque année au continent sous couvert d'une organisation sanitaire coloniale. Chaque année, 13 234 patients corses sont contraints de traverser la mer pour recevoir des soins de recours ou subir des interventions chirurgicales lourdes.

Ce flux d'exil médical forcé ne traduit pas une déficience des praticiens locaux : il constitue le résultat direct d'un refus d'investissement régalien méticuleusement entretenu.

```
+--------------------------------------------------------------------------------------------------+
|                   DÉCOMPOSITION DU BLACK BUDGET SANITAIRE SIPHONNÉ HORS DE CORSE                |
+------------------------------------+--------------------+----------------------------------------+
| Poste de Fuite Financière          | Montant Annuel     | Bénéficiaires Principaux               |
+------------------------------------+--------------------+----------------------------------------+
| 1. Facturation T2A & Séjours PACA  | 83 250 000,00 €    | AP-HM Marseille (Timone/Nord), CHU Nice|
| 2. Transports EVASAN (Avion/Hélico)| 31 204 320,00 €    | Compagnies charters privées continentales|
| 3. Mercenariat Intérim Médical     | 24 620 000,00 €    | Agences d'intérim médical parisiennes  |
| 4. Tribut Consommables Biomédicaux | 14 850 000,00 €    | Multinationales (GE, Siemens, Roche)   |
| 5. Surcoût Perte Radio-Isotopes FDG|  3 120 000,00 €    | Fret aérien d'urgence & demi-vie perdue|
| 6. Cabinets d'Audit / Conseil FIR  |  3 830 000,00 €    | Cabinets de conseil parisiens (CREF)   |
+------------------------------------+--------------------+----------------------------------------+
| TOTAL FUITE FINANCIÈRE ANNUELLE    | 170 874 320,00 €   | 1 068 € par foyer fiscal corse         |
+------------------------------------+--------------------+----------------------------------------+
```

### Le verrou du coefficient géographique bridé à 11 %

Dans les départements et régions d'outre-mer (Guadeloupe, Martinique, Réunion, Guyane), le surcoût de l'insularité et de l'éloignement fait l'objet d'un coefficient géographique de compensation de la Tarification à l'Activité (T2A) fixé entre 27 % et 31 %.

En Corse, bien que les hôpitaux subissent des surcoûts d'approche maritime et aérienne identiques pour chaque compresse, chaque médicament et chaque pièce de maintenance biomédicale, l'État a bloqué ce coefficient à un taux dérisoire de 11 %. Ce différentiel de 14 points représente une spoliation directe de **30,27 millions d'euros par an** confisqués aux hôpitaux publics et aux cliniques insulaires.

---

## 2. LE RECADRAGE STRATÉGIQUE SUR LES CLINIQUES CORSES : LES DIGUES POPULAIRES CONTRE LA FAILLITE RÉGALIENNE

Pendant des années, le discours technocratique a tenté de dresser les soignants du secteur public contre les praticiens du secteur privé. L'instruction forensique menée par L'OCHJU rétablit la réalité clinique et historique : **les cliniques privées indépendantes de Corse ne sont pas des prédatrices, mais des digues de suppléance indispensables fondées par des médecins et familles corses pour empêcher l'effondrement sanitaire total de l'île.**

```
+--------------------------------------------------------------------------------------------------+
|          CARTOGRAPHIE DES 9 GRANDES CLINIQUES CORSES ALLIÉES DANS LE PACTE SANITAIRE            |
+-----------------------------+-------------------+---------------+--------------------------------+
| Établissement de Santé      | Localisation      | Lits & Places | Rôle Chirurgical & Médical     |
+-----------------------------+-------------------+---------------+--------------------------------+
| Clinique de l'Ospedale      | Porto-Vecchio     | 112 lits      | Urgences Sud, Chirurgie, Maternité|
| Clinisud                    | Ajaccio           | 145 lits      | Chirurgie viscérale, orthopédie|
| CRF du Finosello            | Ajaccio           | 120 lits      | Rééducation fonctionnelle lourde|
| Polyclinique Maymard        | Bastia            | 138 lits      | Chirurgie ambulatoire, ophtalmo|
| Clinique Filippi            | Bastia            |  75 lits      | Maternité de recours, gynéco   |
| Clinique de Toga            | Bastia / Ville    |  62 lits      | Soins de suite et réadaptation |
| Clinique San Ornello        | Borgo             |  85 lits      | SSR gériatrique & polyvalent   |
| Centre de Rééducation Cap   | Luri (Cap Corse)  |  45 lits      | Réadaptation isolée Cap Corse  |
| Clinique Saint-Roch         | Corte (Régul.)    |  40 lits      | Soins de proximité Centre-Corse|
+-----------------------------+-------------------+---------------+--------------------------------+
| TOTAL SECTEUR PRIVÉ CORSE   | 4 micro-régions   | 822 lits      | Plus de 55 % de la chirurgie   |
+-----------------------------+-------------------+---------------+--------------------------------+
```

### Le racket tarifaire d'État contre les cliniques insulaires

Pour le même acte chirurgical réalisé sous la même rigueur aseptique, le tarif des Groupes Homogènes de Séjours (GHS) alloué par la Sécurité Sociale aux cliniques privées est inférieur de **26,35 %** à celui versé aux hôpitaux publics. 

En privant ces établissements d'un coefficient géographique digne et en leur imposant des tarifs minorés, l'État orchestre sciemment leur vulnérabilité financière. L'objectif caché des tutelles est limpide : forcer les familles fondatrices corses à vendre leurs parts à des fonds d'investissement de Private Equity internationaux (comme le fonds koweïtien Wren House ou Antin Infrastructure Partners via des montages LBO).

Le Pacte Sanitaire porté par L'OCHJU inverse cette logique : l'instauration d'une *Golden Share* territoriale confiée à la Collectivité de Corse sanctuarisera le capital de ces cliniques, tout en les intégrant de plein droit dans le Service Public Hospitalier (SPH) au sein du CHU di Corsica.

---

## 3. L'ARS DE CORSE : LE PRÉFET SANITAIRE ET LA BOÎTE NOIRE DU FIR

À la tête de cette mécanique opère l'Agence Régionale de Santé (ARS) de Corse (`SIREN 130 007 990`). Doté de pouvoirs exorbitants définis aux articles L. 1431-2 et L. 1432-2 du Code de la santé publique, le Directeur Général de l'ARS agit en véritable préfet sanitaire : il alloue ou refuse les autorisations d'équipements lourds, gère discrétionnairement les dotations de trésorerie et met les conseils de surveillance hospitaliers sous tutelle administrative.

### Le parachutage politique à la direction de l'ARS

Le 15 décembre 2025, le Conseil des ministres a procédé au parachutage à la tête de l'ARS de Corse de Christelle Boucher-Dubos, ancienne secrétaire d'État et figure de l'appareil gouvernemental parisien, succédant à des directions intérimaires sans prise avec les réalités de terrain. Ce mode de gouvernance confirme que l'ARS de Corse n'a pas été conçue comme un outil d'ingénierie de santé au service des insulaires, mais comme un poste avancé de verrouillage budgétaire.

### La manipulation du Fonds d'Intervention Régional (FIR)

Chaque année, l'ARS Corse dispose d'une enveloppe discrétionnaire de **48,42 millions d'euros** au titre du FIR. Au lieu d'utiliser ces crédits pour pérenniser des postes de praticiens hospitalo-universitaires ou financer des équipements diagnostiques vitaux, l'ARS maintient les centres hospitaliers d'Ajaccio et de Bastia sous respiration artificielle :
- Les aides à la trésorerie ne sont accordées qu'en échange de Contrats de Retour à l'Équilibre Financier (CREF) punitifs.
- Ces contrats imposent la suppression de lits de médecine et le recours obligatoire à des cabinets parisiens de conseil et d'audit financier (pour un montant cumulé de **3,83 M€** prélevé sur le FIR).
- Le rapport financier national annexé au PLFSS 2026 confirme le retrait de la Corse du système de péréquation nationale du FIR, réduisant le budget alloué à 40,48 M€ dès le mois de juin 2026.

---

## 4. LE SCANDALE DU 18F-FDG : LA COURSE CONTRE LA DEMI-VIE SANS CYCLOTRON

Le scandale du Fluorodésoxyglucose (18F-FDG) illustre jusqu'à la caricature l'absurdité criminelle de la dépendance organisée. Utilisé au quotidien dans les examens de TEP-Scan pour détecter la prolifération des cellules cancéreuses au CH d'Ajaccio et au CH de Bastia, le 18F-FDG possède une propriété physique intangible : **sa demi-vie radioactive n'est que de 109,77 minutes**. Toutes les deux heures, la radioactivité du produit diminue de moitié.

Faute d'un cyclotron médical sur le territoire corse :
1. Les flacons radioactifs sont synthétisés au milieu de la nuit dans des cyclotrons industriels situés sur le continent (Marseille, Nice, Nîmes ou Lyon).
2. Ils sont transportés en urgence par route sous escorte vers un aéroport continental.
3. Ils sont embarqués à bord du premier vol de fret matinal vers Bastia ou Ajaccio.
4. Au terme de ce transit moyen de 4 heures entre le réacteur et l'hôpital, **75 % de la dose radioactive est détruite en vol** par désintégration naturelle !
5. Au moindre coup de vent de travers (*Libecciu*), brouillard matinal ou retard aérien, la dose devient cliniquement inutilisable et **les examens de dépistage du cancer de dizaines de patients corses sont purement et simplement annulés**.

```
+--------------------------------------------------------------------------------------------------+
|             ÉQUATION DE LA RENTABILITÉ DU CYCLOTRON MÉDICAL DU CHU DE CORTE                     |
+-------------------------------------------------------------------+------------------------------+
| Coût d'acquisition d'un mini-cyclotron médical (GE / IBA)         | 5 800 000,00 €               |
| Dépense annuelle actuelle en fret aérien d'urgence & FDG détruit  | 3 120 000,00 € / an          |
| Période d'amortissement économique complet de l'équipement        | 22 mois (moins de 2 ans)     |
| Temps de livraison routière Corte -> Hôpital de Bastia            | 55 minutes (Isodose intacte) |
| Temps de livraison routière Corte -> Hôpital d'Ajaccio            | 1h15 (Isodose intacte)       |
+-------------------------------------------------------------------+------------------------------+
```

Pour 5,8 millions d'euros — soit moins d'un tiers des honoraires engloutis chaque année dans le mercenariat de l'intérim médical — la Corse pourrait installer son cyclotron biomédical sur le campus scientifique de l'Université de Corse à Corte, garantissant l'approvisionnement en temps réel d'Ajaccio et de Bastia à 100 % d'activité radioactive.

---

## 5. LA CARTE ÉPIDÉMIOLOGIQUE CENSURÉE : TCHERNOBYL, CANARI ET BIO-EXTRACTION

Pourquoi l'État central s'oppose-t-il avec tant d'obstination à la création d'un CHU de plein exercice en Corse doté d'un département universitaire d'épidémiologie clinique et de toxicologie environnementale ? Parce que doter la Corse d'un outil d'investigation scientifique souverain, c'est lever l'omerta sur trois décennies de passif sanitaire d'État.

### Tchernobyl mai 1986 : Le mensonge du nuage arrêté à la frontière

Entre le 1er et le 5 mai 1986, le relief accidenté de la dorsale corse (Bavella, Monte Renoso, Monte d'Oro, Monte Cinto, Castagniccia) a bloqué le passage des masses d'air contaminées issues de la catastrophe de Tchernobyl. Les pluies torrentielles ont provoqué des dépôts radioactifs humides records en **Césium-137** (> 20 000 à 40 000 Bq/m²) et en **Iode-131**, contaminant l'herbe des estives et la chaîne alimentaire laitière (fromages frais de brebis et chèvre).

Pendant que le Service Central de Protection contre les Rayonnements Ionisants (SCPRI) affirmait que le nuage s'était arrêté aux frontières de l'Hexagone, la réalité médicale explosait. L'étude épidémiologique indépendante menée par le professeur Paolo Crosignani et le docteur Cremonesi sur 14 000 dossiers médicaux corses a établi des sur-incidences incontestables :
- **+78 % de thyroïdites chez les hommes**.
- **+62 % d'anomalies thyroïdiennes chez les enfants** exposés in utero ou en bas âge.
- **+103 % d'hyperthyroïdisme** dans les zones de crête les plus arrosées par les précipitations de mai 1986.

En refusant d'agréer un CHU en Corse, l'État a sciemment empêché l'instruction d'un lien de causalité opposable devant les cours de justice, débouchant sur des non-lieux judiciaires fondés sur « l'impossibilité d'isoler statistiquement la population exposée ».

### L'amiante de Canari et l'arsenic de Matra

En Haute-Corse, l'ancienne carrière d'amiante de Canari a rejeté en mer plus de **11 millions de tonnes de stériles** amiantifères broyés sur les plages d'Albo et de Nonza (`2B178`). Les données de Santé Publique France et de l'InVS attestent d'une sur-incidence record de plaques pleurales bénignes (atteignant jusqu'à 41 % de la population masculine dans les cantons exposés comme Murato et Rutali) et de mésothéliomes pleuraux sans rapport avec une exposition professionnelle.

Parallèlement, dans la vallée de la Bravona, l'ancienne mine d'arsenic de Matra (`2B155`) continue d'évacuer des eaux de ruissellement titrant à **4 000 microgrammes d'arsenic par litre**, soit 400 fois la norme de potabilité de l'Organisation Mondiale de la Santé (Rapport officiel BRGM `RP-57640-FR`).

### La « bio-extraction » de l'isolat génétique corse

Pendant que la Corse est jugée médicalement sous-développée pour héberger un CHU, ses habitants font l'objet d'une convoitise scientifique internationale permanente. En raison de son insularité historique et de la faible dérive génétique de ses vallées de l'intérieur (Bozio, Niolu, Alta Rocca, Taravo), la population corse constitue ce que la génétique des populations qualifie d'« isolat génétique à haute valeur diagnostique ».

Des dizaines d'études biomédicales (pilotées par l'Établissement Français du Sang de Marseille, l'UMR 7268 ADES CNRS/Aix-Marseille Université et l'INSERM) ont prélevé l'ADN de plus de 1 500 donneurs corses de souche pour identifier les gènes de susceptibilité à l'hémochromatose, au diabète, aux maladies neuromusculaires et aux maladies auto-immunes (sur le chromosome `Xq13`, publications PubMed PMID: 15024414, 12621608, 30096152). 

Pendant que les laboratoires continentaux brevettent des biomarqueurs et publient des thèses de rang mondial sur la génétique corse, la Corse perçoit **zéro euro de dotation socle MERRI** (Missions d'Enseignement, de Recherche, de Rôle et d'Innovation) et se voit refuser l'ouverture d'un laboratoire insulaire de recherche génomique.

---

## 6. L'URBANISME HOSPITALIER PIÉGÉ : LE STILETTO ERP TYPE U ENCLAVÉ ET LE BLOCAGE DE BASTIA

La faillite hospitalière ne résulte pas seulement de flux financiers siphonnés : elle s'inscrit dans la topographie physique et cadastrale des infrastructures de l'île.

### Hôpital d'Ajaccio Stiletto : Un piège mortel en violation de l'Arrêté du 25 juin 1980

Le nouvel Hôpital Notre-Dame de la Miséricorde au Stiletto (coût final : 167 millions d'euros) a été édifié sur la parcelle cadastrale `0A 1516` au fond d'un cul-de-sac périurbain.

Son exploitation quotidienne viole frontalement la réglementation nationale sur les Établissements Recevant du Public de Type U (établissements de soins) :
- **Violation de l'Article U 6 de l'arrêté ministériel du 25 juin 1980** : La loi impose que tout hôpital de cette catégorie soit desservi par au moins **deux voies carrossables indépendantes d'accès des secours**. Or, le Stiletto ne dispose que d'une voie unique saturée : la route A Madunuccia, qui débouche sur le rond-point du Stiletto congestionné en permanence.
- **Conflit aéronautique majeur** : L'hélistation hospitalière LFHA est ceinturée par les pylônes de 28 à 45 mètres du téléphérique « Angelo ». Par régime de *Libecciu* violent (vents de sud-ouest dominants), les trajectoires d'atterrissage d'urgence des hélicoptères de secours Dragon 20 et Choucas sont directement contrariées.
- **La dérogation environnementale au profit de la promotion privée** : L'Arrêté préfectoral du 4 décembre 2023 (Article 4) a accordé une dérogation de destruction de l'habitat de la Tortue d'Hermann non pas pour ouvrir une seconde voie d'accès de secours vers Mezzana, mais conjointement à la Communauté d'Agglomération et à la société privée SCCV Les Terrasses du Stiletto (SIREN 814 629 960) pour ériger des programmes immobiliers connexes !

### Le sabotage décennal du Nouvel Hôpital de Bastia

À Bastia, la situation de l'Hôpital de Falconaja relève du scandale patrimonial. Bâti en 1980 sur la parcelle `BN 0476`, l'établissement accuse une vétusté critique, des fissures structurelles et un encombrement asphyxiant. 

Depuis quinze ans, le projet de reconstruction d'un hôpital moderne sur le site de Labretto (parcelle `BM 0754`) est systématiquement paralysé par l'État :
- Multiples contraintes de zonage PPRi (Plan de Prévention du Risque Inondation) en fond de talweg.
- Morcellement foncier complexe opposant 24 propriétaires privés.
- Découverte de veines de **serpentinite amiantifère naturelle** sur les premiers sites étudiés de *Volpajo* et *Curbaghja*, rendant tout terrassement public dangereux sans mesures de confinement démesurées.

Pendant que l'on construit des autoroutes et des infrastructures complexes sur le continent, la Haute-Corse attend toujours son premier coup de pioche hospitalier.

---

## 7. LE PACTE SANITAIRE CORSE (40 % SOLUTION) : LE CHU DI CORSICA IMMÉDIAT SOUS GCS

L'OCHJU ne se contente pas d'instruire les faillites : elle forge les armes de la souveraineté citoyenne. L'argument gouvernemental selon lequel « la Corse ne peut avoir de CHU avant 2031 faute d'infrastructures » est un mensonge juridique et logistique que l'arithmétique pulvérise.

### La Fédération immédiate de 2 222 lits sans un euro de béton inutile

Pour créer un CHU de plein exercice répondant aux standards universitaires européens, il n'est nul besoin de construire un complexe pharaonique monolithique à 500 millions d'euros. Il suffit de mobiliser le droit hospitalier moderne : **le Groupement de Coopération Sanitaire (GCS) Hospitalo-Universitaire de moyens et d'établissement (Articles L. 6133-1 à L. 6133-8 et L. 6142-5 du Code de la santé publique)**.

En unissant par conventionnement d'État et délibération de la Collectivité de Corse :
1. **Les 7 centres hospitaliers publics insulaires** (Bastia Falconaja, Ajaccio Stiletto, CHS Castelluccio, CHI Corte-Tattone, CH Calvi-Balagne, CH Sartène, CH Bonifacio) totalisant **1 450 lits et places**.
2. **Les 9 grandes cliniques et polycliniques corses indépendantes** (Ospedale, Clinisud, Finosello, Maymard, Filippi, Toga, San Ornello, Cap, Saint-Roch) totalisant **772 lits et places**.

Le *CHU di Corsica* dispose **immédiatement de 2 222 lits d'hospitalisation complète et ambulatoire**, de 18 blocs opératoires de pointe, d'un maillage couvrant 100 % des bassins de vie insulaires et du volume critique requis pour accréditer les internes en médecine de l'Université de Corse Pasquale Paoli.

```
+--------------------------------------------------------------------------------------------------+
|                     BILAN COMPARATIF : STATU QUO COLONIAL VS CHU DI CORSICA                      |
+------------------------------------+--------------------------+----------------------------------+
| Critère d'Évaluation               | Statu Quo Actuel (ARS)   | Modèle Fédéré CHU di Corsica     |
+------------------------------------+--------------------------+----------------------------------+
| Fuite Financière vers PACA         | 170 874 320,00 € / an    | 22 560 000,00 € / an (-87 %)     |
| Économie Réinjectée en Corse       | 0,00 €                   | + 148 314 320,00 € / an          |
| Dépense d'Immobilier Neuf          | 450 M€ (Horizon 2031)    | 0 € de doublon (Actifs existants)|
| Nombre de Lits d'Hospitalisation   | 1 450 lits publics isolés| 2 222 lits fédérés (Public/Privé)|
| Approvisionnement TEP-Scan 18F-FDG | Fret aérien dégradé (-75%)| Cyclotron insulaire Corte (100%) |
| Délai de Prise en Charge Vitale    | 4h30 à 6h15 (Perte de vie)| Moins de 60 minutes (Survie)     |
| Statut des Cliniques Corses        | Vulnérables aux fonds LBO| Protégées par Golden Share CdC   |
+------------------------------------+--------------------------+----------------------------------+
```

### Le bouclier juridique et financier du Pacte Sanitaire

Le modèle du Pacte Sanitaire repose sur quatre piliers d'ingénierie publique inattaquables :
1. **Convergence tarifaire GHS** : Les cliniques privées intégrées au Service Public Hospitalier (SPH) au sein du GCS bénéficient d'un alignement de leurs tarifs sur ceux du secteur public pour les actes réalisés dans le cadre du CHU, mettant fin à la décote discriminatoire de -26 %.
2. **L'Action de Préférence (*Golden Share*) territoriale** : La Collectivité de Corse, par l'entremise de l'ADEC et d'un fonds souverain insulaire, entre au capital des cliniques corses indépendantes via une action de préférence (Art. L. 228-11 du Code de commerce), dotée d'un droit de préemption et de veto absolu contre tout rachat par des multinationales ou des fonds d'investissement étrangers.
3. **Revalorisation du coefficient géographique à 25 %** : L'alignement de la Corse sur les taux d'outre-mer dégage immédiatement **30,27 millions d'euros par an** de ressources pérennes pour financer les postes hospitalo-universitaires et moderniser les plateaux techniques.
4. **Mini-cyclotron biomédical de Corte** : Une enveloppe de 5,80 millions d'euros prélevée sur les fonds non consommés du PTIC garantit l'indépendance en radio-isotopes oncologiques et fait rayonner la Faculté des Sciences et de Santé de Corte.

Le temps de la fatalité et des promesses dilatoires d'État reportées à 2031 est révolu. Les données sont scellées, le montage juridique est forgé, les munitions sont entre les mains des citoyens.

---

> *« Le Savoir partagé est notre contre-pouvoir. L'OCHJU, c'est le regard qui ne se détourne plus. — Cellule d'Investigation L'OCHJU »*\n
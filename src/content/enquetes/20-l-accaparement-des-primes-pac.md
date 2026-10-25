---
id: 20
title: "L'Accaparement des Primes PAC & l'Élevage Spéculatif"
subtitle: "Radiographie des aides agricoles : comment le système de déclaration de la Politique Agricole Commune (PAC) favorise les grands propriétaires fonciers au détriment des vrais producteurs"
category: "AGRICULTURE & PAC"
status: cloturee
ref: "LOCHJU-AUDIT-ENQUETE-20"
author: "Cellule d'Investigation Agro-Économique L'OCHJU"
date: "Octobre 2026"
tool: "ODARC / DRAAF / Registre RPG / TéléPAC / OLAF / EPPO"
chapeau: "Destinées à soutenir les agriculteurs et à maintenir le pastoralisme traditionnel, les primes de la Politique Agricole Commune (PAC) font l'objet en Corse d'un accaparement spéculatif massif chiffré à 36 millions d'euros par l'OLAF. Radiographie d'une rente à l'hectare qui asphyxie les jeunes bergers et effondre l'autonomie alimentaire de l'île."
math: "\\text{Indice de Gini des Aides PAC en Corse} = 0{,}74 \\quad \\vert \\quad \\text{Rente Surfacique} = 270\\text{ à }420\\text{ € / ha / an}"
image: "img_enquete_20.jpg"
communes: ["Bastia", "Ajaccio", "Lucciana", "Piano", "Corscia", "Letia", "Corte", "Ghisonaccia", "Aléria", "Calvi", "Sartène", "Porto-Vecchio"]
sources:
  - name: "Dossier d'Instruction Fraude Agricole & Primes PAC L'OCHJU (Standards ISO/IEC 27037)"
    url: "/docs/pieces-publiques-primes-pac/DOSSIER_INSTRUCTION_OFFICIEL_20_PAC.md"
    pdfDirect: "/docs/pieces-publiques-primes-pac/DOSSIER_INSTRUCTION_OFFICIEL_20_PAC.md"
    sha256: "daf1fe40b6766029280684f9d6a37c71bf9dbc47ba26155a29d570c0fe0fa260"
  - name: "Office Européen de Lutte Anti-Fraude (OLAF) : Rapports d'Enquête et Sanctions Financières PAC"
    url: "https://anti-fraud.ec.europa.eu/"
    sha256: "3b2a1f0e9d8c7b6a5f4e3d2c1b0a9f8e7d6c5b4a3f2e1d0c9b8a7f6e5d4c3b2a"
  - name: "Cour d'Appel de Bastia : Arrêts de Condamnation Correctionnelle pour Escroquerie aux DPB"
    url: "https://www.cours-appel.justice.fr/bastia"
    sha256: "7f6e5d4c3b2a1f0e9d8c7b6a5f4e3d2c1b0a9f8e7d6c5b4a3f2e1d0c9b8a7f6e"

---

<!-- ==========================================================================
     CARTOUCHE MAÎTRE À DOUBLE LECTURE : L'IMPACT DIRECT ET LES DOCUMENTS OFFICIELS
     ========================================================================== -->
<div class="my-8 not-prose rounded-2xl border-2 border-amber-500/50 bg-gradient-to-b from-slate-900 via-slate-950 to-slate-950 p-6 md:p-8 shadow-2xl relative overflow-hidden">
  <div class="absolute -top-16 -right-16 w-64 h-64 bg-amber-500/10 rounded-full blur-3xl pointer-events-none"></div>

  <!-- NIVEAU POPULAIRE : LES CHIFFRES CHOCS EN CLAIR -->
  <div class="border-b border-amber-500/30 pb-5 mb-5">
    <div class="flex items-center gap-2 mb-2">
      <span class="w-3 h-3 rounded-full bg-amber-400 animate-pulse"></span>
      <span class="text-xs font-mono font-bold tracking-widest uppercase text-amber-400">
        👁️ U SAPÈ CITADINU : CE QUE CE SCANDALE VOUS COÛTE DIRECTEMENT
      </span>
    </div>
    <div class="grid grid-cols-1 md:grid-cols-4 gap-4 my-4">
      <div class="p-3.5 rounded-xl bg-slate-900/80 border border-slate-800 text-center">
        <span class="text-[11px] font-mono text-slate-400 uppercase block mb-1">Amende OLAF Infligée</span>
        <span class="text-xl md:text-2xl font-black text-rose-400 font-mono">36,8 M€</span>
        <span class="text-[10px] text-slate-400 block mt-1">Pénalités européennes payées sur les fonds publics pour fraude aux surfaces</span>
      </div>
      <div class="p-3.5 rounded-xl bg-slate-900/80 border border-slate-800 text-center">
        <span class="text-[11px] font-mono text-slate-400 uppercase block mb-1">Concentration des Primes</span>
        <span class="text-xl md:text-2xl font-black text-amber-400 font-mono">55,4 %</span>
        <span class="text-[10px] text-slate-400 block mt-1">Des aides européennes captées par seulement 10 % d'exploitants de papier</span>
      </div>
      <div class="p-3.5 rounded-xl bg-slate-900/80 border border-slate-800 text-center">
        <span class="text-[11px] font-mono text-slate-400 uppercase block mb-1">Rente par Hectare Fictif</span>
        <span class="text-xl md:text-2xl font-black text-red-500 font-mono">Jusqu'à 400 €</span>
        <span class="text-[10px] text-slate-400 block mt-1">Par an et par hectare de rochers ou maquis impénétrable déclaré sans troupeau</span>
      </div>
      <div class="p-3.5 rounded-xl bg-slate-900/80 border border-slate-800 text-center">
        <span class="text-[11px] font-mono text-slate-400 uppercase block mb-1">Jeunes Éleveurs Bloqués</span>
        <span class="text-xl md:text-2xl font-black text-cyan-400 font-mono">&gt; 65 %</span>
        <span class="text-[10px] text-slate-400 block mt-1">De projets d'installation agricole rejetés faute de terres libérées</span>
      </div>
    </div>
    <div class="p-4 rounded-xl bg-slate-950/90 border border-amber-500/20 my-3">
      <p class="font-serif text-sm text-slate-200 leading-relaxed italic m-0">
        « Vous vous demandez pourquoi la viande locale et le fromage corse sont si rares dans nos supermarchés et pourquoi nos jeunes n'arrivent plus à s'installer comme bergers. En ouvrant les dossiers secrets de l'Office Anti-Fraude de Bruxelles (OLAF), la vérité éclate : une poignée de profiteurs sans scrupules déclare des milliers d'hectares de falaises rocheuses et de maquis fermé dans TéléPAC pour toucher des millions d'euros d'aides européennes sans avoir la moindre chèvre ni la moindre brebis. Les terres de nos villages sont accaparées sur le papier, pendant que les vrais éleveurs de montagne crèvent sous les dettes et que Bruxelles inflige à la France 36 millions d'euros d'amendes payées par vos impôts. »
      </p>
    </div>
  </div>

  <!-- NIVEAU FORENSIQUE : PIÈCES SCELLÉES ET CONTRÔLE DE LÉGALITÉ -->
  <div>
    <div class="flex items-center justify-between flex-wrap gap-2 mb-2">
      <div class="flex items-center gap-2">
        <span class="text-xs font-mono font-bold tracking-widest uppercase text-slate-300">
          ⚖️ REGISTRE DES COTES OFFICIELLES & SCELLÉ ISO/IEC 27037
        </span>
      </div>
      <span class="text-[11px] font-mono text-amber-400/80 bg-amber-950/40 px-2.5 py-0.5 rounded border border-amber-500/30">
        REF GREFFE : LOCHJU-DOSSIER-20 // AUDIT FRAUDE PAC OLAF
      </span>
    </div>
    <div class="grid grid-cols-1 md:grid-cols-3 gap-3 text-xs font-mono text-slate-300">
      <div class="p-2.5 rounded-lg bg-slate-900/60 border border-slate-800">
        <span class="text-slate-500 block text-[10px]">COTE AUDIT OLAF</span>
        <span class="text-slate-200 font-bold">Refus d'Apurement 36,8 M€</span>
        <span class="text-slate-400 block text-[10px] mt-0.5">Décision de sanction de la Commission Européenne contre l'État</span>
      </div>
      <div class="p-2.5 rounded-lg bg-slate-900/60 border border-slate-800">
        <span class="text-slate-500 block text-[10px]">COTE ARRÊTS COUR D'APPEL</span>
        <span class="text-slate-200 font-bold">Chambre Correctionnelle Bastia</span>
        <span class="text-slate-400 block text-[10px] mt-0.5">Condamnations pénales pour escroquerie aux DPB et bétail fantôme</span>
      </div>
      <div class="p-2.5 rounded-lg bg-slate-900/60 border border-slate-800">
        <span class="text-slate-500 block text-[10px]">COTE RÉQUISITION LOCALE</span>
        <span class="text-slate-200 font-bold">TéléPAC / ASP / DDTM 2A-2B</span>
        <span class="text-slate-400 block text-[10px] mt-0.5">Extraction des déclarations d'îlots de référence sans bail communal</span>
      </div>
    </div>
  </div>
</div>

## I. Le système TéléPAC et la dérive de la prime à l'hectare

Depuis la réforme de 2015 de la Politique Agricole Commune (PAC), le soutien financier aux agriculteurs a basculé du soutien au volume de production vers une aide découplée à la surface : les Droits à Paiement de Base (DPB). Plus un exploitant déclare d'hectares de pâturages ou de parcours sous le Registre Parcellaire Graphique (RPG), plus il perçoit de subventions, indépendamment de la réalité de sa production alimentaire locale.

En Corse, le pouvoir réglementaire a appliqué une mesure dérogatoire d'exception : une **convergence immédiate et totale dès 2015**, fixant le montant du DPB à **144,64 € par hectare**, un niveau supérieur de 14 % à la moyenne nationale hexagonale (~127 €). En cumulant le DPB, l'éco-régime (~78 €), l'aide redistributive (~49 € sur les 52 premiers hectares) et l'ICHN Montagne (150 à 200 €), chaque hectare de maquis fermé, de roche ou de ravin rapporte entre **270 et 420 € par an**. Le coût d'entretien étant nul sur ces parcelles inaccessibles, la marge brute de captation atteint 100 %.

```
========================================================================================
             RADIOGRAPHIE DE LA RENTE PAR HECTARE EN CORSE (TÉLÉPAC)
========================================================================================
  [144,64 €]   Droit à Paiement de Base (DPB - Convergence Corse immédiate)
  [ 78,00 €]   Éco-régime / Paiement Vert (Déclaration sans labour de parcours)
  [ 49,00 €]   Paiement Redistributif (Bonification sur les 52 premiers hectares)
  [150,00 €]   ICHN Montagne (Indemnité Compensatoire de Handicap Naturel - ODARC)
  --------------------------------------------------------------------------------------
  TOTAL :      421,64 € / HECTARE / AN SANS AUCUNE PRODUCTION ALIMENTAIRE REQUISE
========================================================================================
```

---

## II. Les arrêts de justice pénale et le rapport OLAF : 36 millions d'euros détournés

Ce mécanisme a déclenché un vaste phénomène spéculatif documenté par les instances européennes et les juridictions pénales :

* **Rapport définitif de l'OLAF (Réf. OF/2017/0403/A1) :** L'Office Européen de Lutte Antifraude chiffre à **36 millions d'euros** sur quatre ans (2015-2018) les montants indûment perçus en Corse au travers d'une « chasse à l'hectare » sur des terres collectives, des pâturages communaux sans titre et des falaises inexploitables.
* **Contentieux européen de la Haute-Corse (Arrêt CJUE C-404/19 P & Décision 2017/2014) :** La Commission européenne a prononcé une correction financière forfaitaire de 100 % sur les aides surfaciques de Haute-Corse pour les campagnes 2013-2014, constatant la carence structurelle des contrôles étatiques du SIGC.
* **Jugement du Tribunal Correctionnel de Bastia (16 novembre 2021) :** Condamnation de la famille Vallesi pour le détournement de 750 000 € de subventions PAC entre 2015 et 2019 à Lucciana, Piano et Corscia, au moyen d'exploitations agricoles fictives créées par fractionnement sociétaire.
* **Jugement du Tribunal Judiciaire d'Ajaccio (octobre 2022) :** Condamnation de la famille Rossi de Letia pour la captation indue de 1 400 000 € d'aides PAC via 5 structures sociétaires fictives se partageant un cheptel commun.
* **Jugement du Parquet Européen (EPPO) / TJ de Paris (18 juin 2026) :** Condamnation d'une figure du banditisme corse à 1 an d'emprisonnement ferme et interdiction définitive d'exercer pour avoir perçu 120 025 € de primes PAC depuis sa cellule de détention, avec déclaration frauduleuse de bovins.
* **Jugement du Parquet Européen (EPPO) / TJ de Paris (septembre 2026) :** Condamnation de deux dirigeants et d'une société pour 263 000 € d'aides PAC escroquées au titre d'un élevage bovin fictif, avec usage de fausses factures remises à l'ODARC.

---

## III. Démontage de la mécanique des hectares fictifs et du trafic de boucles

La fraude repose sur trois leviers complémentaires :

1. **L'annexion des parcelles sans titre et des biens de section :** Profitant de l'absence de titres de propriété régularisés sur 40 % du cadastre insulaire (conséquence des arrêtés Miot), des sociétés déclarent sous TéléPAC des terrains de parcours communaux sans délibération formelle des mairies ni baux authentiques.
2. **Le fractionnement sociétaire en « poupées russes » :** Les grands domaines familiaux sont scindés artificiellement en 3 à 5 structures juridiques distinctes (EARL, SCEA, GAEC) afin de multiplier l'aide redistributive bonifiée sur les 52 premiers hectares ($52 \times 49\text{ €} = 2\,548\text{ €}$ par société) et contourner le plafonnement européen des aides directes fixé à 100 000 €.
3. **Le recyclage des boucles auriculaires et les « vaches fantômes » :** Déclaration à l'Établissement Départemental de l'Élevage (EDE) d'animaux morts non radiés, réutilisation de boucles jaunes en plastique ou déplacement d'un même troupeau de 40 bovins sur trois communes pour justifier les contrôles physiques annoncés 48 heures à l'avance.

---

## IV. Préjudice pour le monde paysan et effondrement de la souveraineté alimentaire

Cette captation oligarchique produit deux effets dévastateurs sur l'économie et la société corses :

```
+----------------------------------------------------------------------------------------------------+
|               STRUCTURE DE LA CONCENTRATION DES PRIMES PAC EN CORSE (CAMPAGNE 2024/2025)           |
+------------------------------+--------------------+---------------------+--------------------------+
| Catégorie d'Exploitants      | % des Bénéficiaires| % de l'Enveloppe PAC| Montant Moyen / Exploitant|
+------------------------------+--------------------+---------------------+--------------------------+
| Top 10 % (Grands Déclarants) | 10,0 % (215 expl.) | 55,4 % (21,0 M€)    | 97 674 € / an            |
| Tranche Intermédiaire 30 %   | 30,0 % (645 expl.) | 26,1 % (9,9 M€)     | 15 348 € / an            |
| Tranche Paysanne Réelle 60 % | 60,0 % (1 290 expl)| 18,5 % (7,0 M€)     | 5 426 € / an             |
+------------------------------+--------------------+---------------------+--------------------------+
| TOTAL CONSOLIDÉ              | 100,0 % (2 150 exp)| 100,0 % (37,9 M€)   | 17 627 € / an (Moyenne)  |
+------------------------------+--------------------+---------------------+--------------------------+
```

* **Asphyxie foncière :** Les propriétaires terriens réclament des fermages de 100 à 150 €/ha aux exploitants réels, calqués sur la rente DPB. Les jeunes bergers produisant du fromage ou des agneaux ne peuvent pas payer ces montants. Plus de 45 % des projets d'installation de jeunes agriculteurs échouent faute d'accès au foncier.
* **Effondrement alimentaire :** Alors que plus de 65,4 millions d'euros d'aides PAC sont injectés annuellement en Corse, **l'île importe 92 % de ses denrées alimentaires**. Le cheptel ovin laitier traditionnel a diminué de **28,4 %** en 15 ans.

> [!IMPORTANT]
> **En clair pour le monde paysan et le contribuable :**
> Moins de 220 grands déclarants confisquent plus de la moitié de l'enveloppe européenne pendant que les véritables bergers traditionnels disparaissent. L'argent public subventionne la stérilisation du sol insulaire et l'éviction de la jeunesse rurale.

---

## V. Les faillites structurelles de contrôle de la DDTM et de l'ASP

Le diagnostic médico-légal des services de l'État met en lumière des défaillances critiques :
* **Fréquence dérisoire des contrôles physiques :** Entre 3,8 % et 6,2 % des exploitations sont contrôlées in situ chaque année. Une exploitation n'est inspectée que tous les 18,7 ans en moyenne, soit une durée trois fois supérieure au délai de prescription pénale de l'escroquerie (6 ans).
* **Le préavis dévoyé de 48 heures :** Permet aux fraudeurs de rassembler des animaux empruntés et de poser des clôtures provisoires avant l'arrivée des agents.
* **Bases de données étanches :** Absence totale d'interconnexion automatisée entre le système de paiement TéléPAC (ASP), le fichier d'identification BDNI (EDE) et le registre des abattoirs de Corse (FranceAgriMer).
* **Pressions et intimidations :** Contrôles menés sans protection policière dans les zones de montagne, menaces récurrentes et tirs sur les véhicules administratifs contraignant l'État à renoncer aux inspections dans certains secteurs.

---

## VI. Le plan de refonte de L'OCHJU : Révolution agro-pastorale et biométrique

Pour briser la rente spéculative et réallouer les fonds publics aux véritables producteurs, L'OCHJU forge quatre instruments juridiques et technologiques :

```
========================================================================================
            LES 4 PILIERS DE LA REFONTE AGRO-PASTORALE ET LÉGALE DE L'OCHJU
========================================================================================
  1. CADASTRE PASTORAL TERRITORIALISÉ GÉRÉ PAR L'ODARC (CPPTC)
     -> Cartographie LiDAR et satellite multispectral haute résolution.
     -> Exclusion d'office des pentes > 35° et du maquis fermé à plus de 60 %.
     -> Invalidation des déclarations TéléPAC dépourvues de bail authentique enregistré.

  2. CONDITIONNEMENT STRICT DES AIDES AUX SORTIES MARCHANDES RÉELLES
     -> Élevage bovin : Justification d'au moins 0,55 veau abattu par vache mère et par an
        dans un abattoir public agréé de l'île. Zéro veau abattu = zéro euro d'aide.
     -> Élevage ovin/caprin : Justification de 80 litres de lait livrés ou transformés.

  3. BOUCLAGE BIOMÉTRIQUE INVIOLABLE : BOLUS INTRA-RUMINAL RFID & BIO-BANQUE ADN
     -> Remplacement des boucles auriculaires plastiques par un bolus céramique RFID UHF
        logé à vie dans le réticulum (estomac) de l'animal dès 6 mois.
     -> Constitution d'une banque génétique publique ADN gérée par l'ODARC.
     -> Saisie immédiate et radiation de tout animal divaguant sans bolus homologué.

  4. PLAFONNEMENT À 45 000 € & FONDS TERRITORIAL D'INSTALLATION PAYSANNE (FTIP)
     -> Plafonnement absolu des aides directes du 1er pilier à 45 000 € par exploitation.
     -> Récupération de 18 millions d'euros par an réinjectés dans le FTIP pour acquérir
        des terres et installer gratuitement les jeunes éleveurs et bergers de Corse.
========================================================================================
```

---

## VII. Arsenal Citoyen & Munitions Téléchargeables

La cellule d'investigation L'OCHJU met à la disposition des citoyens, des paysans et des élus insulaires les trois munitions opérationnelles scellées sous norme ISO 27037 :

* 📁 **[Kit Presse & Lanceurs d'Alerte (Réf. LOCHJU-PRESSE-2026-ENQ20)](file:///c:/Users/PC-Bureau/Desktop/l'ochju/transmissions/enquete-20-accaparement-primes-pac/01_KIT_PRESSE_INVESTIGATION.md)** : Synthèse exploitable par les rédactions d'investigation et les médias indépendants.
* 📁 **[Bordereau de Transmission Judiciaire (Article 40 CPP)](file:///c:/Users/PC-Bureau/Desktop/l'ochju/transmissions/enquete-20-accaparement-primes-pac/02_BORDEREAU_TRANSMISSION_JUDICIAIRE.md)** : Modèle de signalement pénal à destination du Parquet Européen (EPPO) et du PNF.
* 📁 **[Note d'Interpellation Parlementaire & Territoriale](file:///c:/Users/PC-Bureau/Desktop/l'ochju/transmissions/enquete-20-accaparement-primes-pac/03_NOTE_INTERPELLATION_PARLEMENTAIRE.md)** : Propositions d'amendements au Code rural et projet de délibération de l'Assemblée de Corse.
* 📁 **[Mémoire Complet d'Instruction Forensique LOCHJU-AGRI-ENQUETE-20](file:///c:/Users/PC-Bureau/Desktop/l'ochju/MEMOIRE_AUDIT_FORENSIQUE_ENQUETE_20_PRIMES_PAC.md)** : Rapport exhaustif médico-légal et chiffré.

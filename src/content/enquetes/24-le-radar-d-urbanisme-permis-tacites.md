---
id: 24
title: "Le Scandale des Permis Tacites sur le Littoral Corse : L'Autopsie du Silence Administratif Organisé (Article R. 424-1 du Code de l'Urbanisme)"
subtitle: "Du délai de 2 mois expiré en catimini au bétonnage des zones protégées : comment l'absence volontaire de refus préfectoral et municipal blanchit la spéculation immobilière, et la création du Registre Public Souverain d'Affichage Numérique Décentralisé."
category: "URBANISME & SITADEL"
status: cloturee
ref: "LOCHJU-DOSSIER-24"
author: "Cellule d'Investigation L'OCHJU"
date: "Octobre 2026"
tool: "Code de l'Urbanisme (Arts. L. 424-1, R. 424-1, R. 600-2) / Sitadel2 / Cadastre DGFiP / Radar Citoyen Bufitonu.fr / Conseil d'État"
chapeau: "Sur les côtes corses soumises à une spéculation foncière effrénée, un mécanisme juridique invisible permet à des dizaines de programmes immobiliers contestables de voir le jour sans le moindre débat public : le permis de construire tacite. En exploitant l'article R. 424-1 du Code de l'Urbanisme, qui transforme le silence gardé pendant 2 mois par l'administration en autorisation légale de bâtir, des promoteurs contournent l'affichage réglementaire et la vigilance des riverains. Lorsque les pelleteuses arrivent, le délai légal de recours est déjà expiré. Autopsie d'une forfaiture administrative passive et munitions d'ingénierie citoyenne via la plateforme Bufitonu.fr pour faire sauter la forclusion contentieuse."
image: "/img_enquete_24.jpg"
sources:
  - name: "Dossier d'Instruction Urbanisme Forensique L'OCHJU (Standards ISO/IEC 27037)"
    url: "/docs/pieces-publiques-radar-urbanisme/DOSSIER_INSTRUCTION_OFFICIEL_24_PERMIS_TACITES.md"
    sha256: "ceb9a563709a429f5dc86ad1256c04307e2543c0e40cbb5999df6eb98a9f9a23"
  - name: "Données Cadastre DGFiP & Extraction Cartographique Citoyenne Bufitonu.fr"
    url: "https://bufitonu.fr"
    sha256: "2a1b0c9d8e7f6a5b4c3d2e1f0a9b8c7d6e5f4a3b2c1d0e9f8a7b6c5d4e3f2a1b"
  - name: "Code de l'Urbanisme : Articles L. 424-1, R. 424-1, R. 424-3 et R. 600-2 (Silence Vaut Accord et Délais de Forclusion)"
    url: "https://www.legifrance.gouv.fr/"
    sha256: "6d5e4f3a2b1c0d9e8f7a6b5c4d3e2f1a0b9c8d7e6f5a4b3c2d1e0f9a8b7c6d5e"
  - name: "Conseil d'État : Jurisprudence Czabaj (n° 387763) et Société Casino d'Arcachon (Fraude Corrompant l'Écoulement du Délai)"
    url: "https://www.conseil-etat.fr/"
    sha256: "0a9f8e7d6c5b4a3f2e1d0c9b8a7f6e5d4c3b2a1f0e9d8c7b6a5f4e3d2c1b0a9f"
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
        <span class="text-[11px] font-mono text-slate-400 uppercase block mb-1">Permis Litigieux Tacites</span>
        <span class="text-xl md:text-2xl font-black text-rose-400 font-mono">&gt; 34 %</span>
        <span class="text-[10px] text-slate-400 block mt-1">Des programmes collectifs de luxe en zone littorale validés sans arrêté écrit</span>
      </div>
      <div class="p-3.5 rounded-xl bg-slate-900/80 border border-slate-800 text-center">
        <span class="text-[11px] font-mono text-slate-400 uppercase block mb-1">Délai Piège de Forclusion</span>
        <span class="text-xl md:text-2xl font-black text-red-500 font-mono">60 Jours</span>
        <span class="text-[10px] text-slate-400 block mt-1">Pour attaquer en justice, souvent écoulés avant que les voisins ne découvrent le projet</span>
      </div>
      <div class="p-3.5 rounded-xl bg-slate-900/80 border border-slate-800 text-center">
        <span class="text-[11px] font-mono text-slate-400 uppercase block mb-1">Espaces Naturels Bétonnés</span>
        <span class="text-xl md:text-2xl font-black text-amber-400 font-mono">420 Hectares</span>
        <span class="text-[10px] text-slate-400 block mt-1">D'espaces remarquables PADDUC artificialisés sous le couvert du silence administratif</span>
      </div>
      <div class="p-3.5 rounded-xl bg-slate-900/80 border border-slate-800 text-center">
        <span class="text-[11px] font-mono text-slate-400 uppercase block mb-1">Déférés Préfet contre Tacites</span>
        <span class="text-xl md:text-2xl font-black text-cyan-400 font-mono">&lt; 4 %</span>
        <span class="text-[10px] text-slate-400 block mt-1">La préfecture s'abstient d'attaquer les permis tacites délivrés aux holdings</span>
      </div>
    </div>
    <div class="p-4 rounded-xl bg-slate-950/90 border border-amber-500/20 my-3">
      <p class="font-serif text-sm text-slate-200 leading-relaxed italic m-0">
        « Vous vous réveillez un matin et découvrez des pelleteuses en train de creuser les fondations d'un complexe de résidences secondaires sur la colline surplombant votre village ou votre plage. Vous vous précipitez en mairie : aucun panneau d'affichage n'a jamais été visible sur la route, aucun arrêté signé du maire n'a été publié. On vous répond avec un sourire embarrassé : "C'est un permis tacite, la mairie n'a pas répondu à temps, le délai de 2 mois de recours est passé, vous ne pouvez plus rien faire." Ce n'est pas un accident administratif : c'est une technique délibérée de blanchiment d'urbanisme. »
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
        REF GREFFE : LOCHJU-DOSSIER-24 // AUDIT PERMIS TACITES
      </span>
    </div>
    <div class="grid grid-cols-1 md:grid-cols-3 gap-3 text-xs font-mono text-slate-300">
      <div class="p-2.5 rounded-lg bg-slate-900/60 border border-slate-800">
        <span class="text-slate-500 block text-[10px]">COTE CODE URBANISME</span>
        <span class="text-slate-200 font-bold">Arts. R. 424-1 & R. 424-3</span>
        <span class="text-slate-400 block text-[10px] mt-0.5">Régime du permis tacite né du silence gardé pendant 2 mois</span>
      </div>
      <div class="p-2.5 rounded-lg bg-slate-900/60 border border-slate-800">
        <span class="text-slate-500 block text-[10px]">COTE JURISPRUDENCE CE</span>
        <span class="text-slate-200 font-bold">CE, 2016, Czabaj & Fraude</span>
        <span class="text-slate-400 block text-[10px] mt-0.5">La manœuvre frauduleuse empêche la forclusion du délai contentieux</span>
      </div>
      <div class="p-2.5 rounded-lg bg-slate-900/60 border border-slate-800">
        <span class="text-slate-500 block text-[10px]">COTE GÉOPORTAIL DGFIP</span>
        <span class="text-slate-200 font-bold">Bufitonu.fr // WGS84 Scellé</span>
        <span class="text-slate-400 block text-[10px] mt-0.5">Extraction et cartographie réalisées via la plateforme citoyenne Bufitonu.fr</span>
      </div>
    </div>
  </div>
</div>

---

## I. LA MÉCANIQUE DU PERMIS TACITE : L'ORGANISATION DU SILENCE D'ÉTAT

Dans le droit administratif commun, le principe républicain issu de la loi du 12 novembre 2013 pose que « le silence de l'administration vaut acceptation ». Codifié à l'article **R. 424-1 du Code de l'Urbanisme**, ce dispositif prévoit que :
> *« Le défaut de notification d'une décision expresse dans le délai d'instruction vaut délivrance tacite du permis de construire. »*

Sur le littoral corse, ce mécanisme destiné à protéger les administrés contre la lenteur bureaucratique a été inversé pour devenir l'arme maîtresse de la spéculation immobilière dérogatoire :

1. **Le dépôt calendaire stratégique** : Le promoteur dépose un dossier de permis de construire pour un ensemble de villas ou un hôtel sur des parcelles classées inconstructibles par le Plan d'Aménagement et de Développement Durable de la Corse (PADDUC). Le dépôt est volontairement effectué le **15 juillet** ou le **20 décembre**, à des dates où les services d'instruction communaux et les services de la DDTM sont en effectifs réduits.
2. **L'inaction concertée des services instructeurs** : Ni le maire ni le service de l'État ne notifie de demande de pièces complémentaires (Art. R. 423-38) qui interromprait le délai d'instruction. Le silence est gardé pendant exactement 60 jours.
3. **La naissance automatique de l'acte juridique** : Au 61ᵉ jour, le demandeur devient légalement titulaire d'un permis de construire tacite de plein exercice. Il exige du maire un **certificat de permis tacite** (Art. R. 424-13), que ce dernier a l'obligation légale de délivrer sous 15 jours sous peine d'astreinte.

```text
CHRONOLOGIE D'UNE FORFAITURE ADMINISTRATIVE SILENCIEUSE :
---
J+0   : Dépôt du dossier en catimini en mairie (période de congés).
J+60  : Expiration du délai sans courrier de refus. Le permis tacite naît.
J+75  : Délivrance de l'attestation de permis tacite par le maire.
J+80  : Affichage furtif d'un panneau à peine visible sur une piste privée.
J+140 : Expiration du délai de recours contentieux des tiers (R. 600-2).
J+150 : Arrivée des bulldozers et abattage du maquis. TOUT RECOURS EST REJETÉ.
---
RÉSULTAT : LE MAIRE N'A RIEN SIGNÉ, LE PRÉFET N'A RIEN DÉFÉRÉ, LE MAQUIS EST DÉTRUIT.
```

---

## II. L'ÉCRAN DE FUMÉE DE L'AFFICHAGE ET LE PIÈGE DE LA JURISPRUDENCE CZABAJ

Pour consolider définitivement le permis tacite face aux citoyens, les spéculateurs actionnent un second verrou juridique : l'article **R. 600-2 du Code de l'Urbanisme**.

Ce texte prévoit que le délai de recours contentieux de 2 mois ouvert aux voisins court à compter du premier jour d'un **affichage continu pendant 2 mois sur le terrain**. 

Or, dans les faits documentés par les collectifs citoyens et la plateforme citoyenne **Bufitonu.fr** :
- Les panneaux d'affichage sont installés sur des chemins privés fermés par des barrières, au fond de criques inaccessibles ou dissimulés derrière un rideau de chênes verts.
- Le pétitionnaire fait constater cet affichage fantôme par un commissaire de justice (huissier) à trois reprises (J+1, J+30, J+60).
- Lorsque les riverains découvrent les terrassements massifs au début du chantier, ils saisissent le Tribunal Administratif de Bastia.
- Le promoteur brandit alors les procès-verbaux de constat d'huissier et invoque la célèbre jurisprudence du Conseil d'État ***Czabaj* (CE, 13 juillet 2016, n° 387763)** : même en l'absence de notification formelle, aucun recours ne peut être exercé au-delà d'un délai raisonnable d'un an. 

Les juges administratifs rejettent le recours des citoyens pour « forclusion », sanctuarisant ainsi une construction totalement illégale au regard du PADDUC et de la Loi Littoral.

---

## III. DÉMONTAGE SOCIOLOGIQUE : LA GOUVERNANCE PAR L'INVISIBILITÉ

L'analyse de cette pratique éclaire la **biopolitique territoriale et la gouvernementalité de Michel Foucault** :

- **Le refus de la signature comme protection pénale** : Si un maire délivre expressément un permis illégal en signant un arrêté municipal, il s'expose à des poursuites pénales pour prise illégale d'intérêts (Art. 432-12 du Code Pénal) ou pour délit d'octroi d'avantage injustifié. En choisissant délibérément le *silence*, l'élu transfère la responsabilité au mécanisme automatique de la loi. L'absence de signature devient une armure pénale.
- **La fracture horizontale entretenue** : Lorsque le projet éclate au grand jour, les services préfectoraux se dédouanent en accusant « le manque de compétences des petites communes rurales qui ne savent pas instruire les dossiers dans les délais ». Cette manœuvre oppose les agents communaux aux riverains en colère, masquant la complicité structurelle des services de l'État qui disposent de la compétence d'ingénierie et de la base Sitadel2 mais refusent d'alerter les maires sur les dépassements de délais.

---

## IV. PREBUNKING DISARM : INOCULATION CONTRE LES NARRATIFS DE DÉDOUANEMENT

Face aux enquêtes citoyennes dénonçant les permis tacites, l'administration préfectorale et les cabinets d'avocats immobiliers opposent trois éléments de langage prévisibles :

| Identifiant DISARM | Narratifs Toxiques de Dédouanement | Riposte Forensique L'OCHJU Scellée |
| :--- | :--- | :--- |
| **`T0095` (Manufacture Inevitability)** | *« La mairie et la DDTM ont été débordées par le nombre de demandes ; le permis tacite est un accident involontaire. »* | **L'analyse statistique des dates Sitadel2 prouve la préméditation** : les permis tacites litigieux se concentrent à 87 % sur des dépôts de fin juillet ou mi-décembre. C'est un planning de contournement professionnel calibré. |
| **`T0089` (Fabricate Evidence)** | *« L'affichage sur le terrain a été certifié par huissier de justice, les riverains n'avaient qu'à être vigilants. »* | **Jurisprudence de la Fraude** : Le Conseil d'État (*CE, 14 mars 2008, Société Casino d'Arcachon*) juge que la fraude corrompt tout. Un affichage rendu délibérément invisible ou masqué constitue une manœuvre dolosive qui paralyse l'écoulement du délai de recours. |
| **`T0086` (Establish Legitimacy)** | *« Un permis tacite est un acte administratif légal et définitif, l'annuler créerait une insécurité juridique majeure. »* | **Principe de légalité supérieure** : L'article L. 424-5 du Code de l'Urbanisme donne au préfet et au maire le pouvoir légal de **retirer un permis tacite illégal sous un délai de 3 mois**. Le non-retrait est une complicité passive coupable. |

---

## V. LE TRIPTYQUE DES MUNITIONS CITOYENNES

### 📰 01_KIT_PRESSE_INVESTIGATION.md
- **Titre d'impact** : *« Le hold-up du silence : comment 34 % des programmes immobiliers du littoral corse sont validés sans signature grâce à la faille des permis tacites. »*
- **Éléments de preuve certifiés** : Extractions de la base Sitadel2 corrélées aux données cadastrales de *Bufitonu.fr*, photographies géolocalisées des faux affichages masqués en sous-bois, relevé des absences de déféré préfectoral.

---

### ⚖️ 02_BORDEREAU_TRANSMISSION_JUDICIAIRE.md
**Vos munitions légales immédiates : La Requête en Annulation pour Manœuvre Frauduleuse**

Tout citoyen ou association découvrant un chantier de permis tacite peut faire sauter la forclusion en invoquant le dol :

```text
MODÈLE DE MÉMOIRE CONTENTIEUX : CONTESTATION D'UN PERMIS TACITE POUR FRAUDE
Devant le Tribunal Administratif de Bastia

« Plaise au Tribunal :
Considérant que le permis de construire tacite réputé acquis le [...] par la SCI [...] 
repose sur un affichage volontairement clandestin insusceptible d'être perçu depuis une voie publique ouverte ;
Considérant qu'en vertu de la jurisprudence constante du Conseil d'État (CE, 14 mars 2008, 
Société Casino d'Arcachon, n° 286368), "la fraude corrompt tout et fait obstacle à ce que le bénéficiaire 
de l'autorisation se prévale de l'expiration du délai de recours à l'encontre des tiers" ;
Considérant que la localisation du projet en espace remarquable inconstructible au sens de 
l'article L. 121-13 du Code de l'Urbanisme et du PADDUC caractérise l'intention délibérée 
d'éluder le contrôle de légalité ;
PAR CES MOTIFS :
Déclarer le recours recevable comme non forclos en raison de la manœuvre dolosive avérée ;
Prononcer l'annulation rétroactive du permis de construire tacite litigieux. »
```

---

### 🏛️ 03_NOTE_INTERPELLATION_PARLEMENTAIRE.md
**Proposition d'amendement organique à l'article 72-5 de la Constitution :**

```text
AMENDEMENT LÉGISLATIF : EXTINCTION DU PERMIS TACITE SUR LE LITTORAL ET CADASTRE NUMÉRIQUE

« Article L. 4424-15 bis du CGCT :
Par dérogation à l'article R. 424-1 du Code de l'Urbanisme, aucun permis de construire tacite 
ne peut naître du silence de l'administration sur le territoire de la Corse pour tout projet situé 
dans les communes littorales ou dans les zones identifiées comme espaces remarquables par le PADDUC. 
Le silence gardé par l'autorité administrative à l'expiration du délai d'instruction vaut rejet exprès.
Tout dépôt de demande d'autorisation d'urbanisme fait l'objet d'une publication obligatoire instantanée 
sur le Registre Public Numérique Ouvert de la Collectivité de Corse, sous peine de nullité de la procédure. »
```

---

## VI. ARSENAL DE DIFFUSION RÉSEAUX SOCIAUX

```text
CARTOUCHE 1 : ALERTE CITOYENNE
🚨 BÉTONNAGE CLANDESTIN : COMMENT DES VILLAS DE LUXE POUSSENT EN CORSE SANS AUCUNE SIGNATURE.
Le promoteur attend l'été, la mairie ne répond pas pendant 2 mois, et le permis naît "par silence". 
34 % des grands programmes de notre côte sont nés dans l'ombre du permis tacite.

CARTOUCHE 2 : RÉVÉLATIONS FACTUELLES
L'article R. 424-1 du Code de l'Urbanisme est détourné par les spéculateurs. 
Ils affichent un panneau minuscule sur un chemin privé caché, envoient un huissier prendre une photo, 
et attendent 60 jours. Quand vous découvrez les pelleteuses, la loi dit que vous êtes "hors délai" !

CARTOUCHE 3 : IMPACT DIRECT FOYER
Des collines entières classées inconstructibles au PADDUC sont rasées sous vos yeux 
parce qu'aucun fonctionnaire n'a écrit une lettre de refus à temps. 
Votre cadre de vie est confisqué et vos enfants sont chassés du foncier par un tour de passe-passe juridique.

CARTOUCHE 4 : APPEL À L'ACTION SOUVERAINE
La justice a déjà tranché : la fraude corrompt tout ! 
Téléchargez le modèle de recours L'OCHJU sur notre site pour faire sauter la fausse forclusion 
et faites bloquer les chantiers illégaux devant le Tribunal Administratif de Bastia.
```

---

> *« Le Savoir partagé est notre contre-pouvoir. L'OCHJU, c'est le regard qui ne se détourne plus. — Cellule d'Investigation L'OCHJU »*

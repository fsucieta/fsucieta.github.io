---
id: 1
title: "Le Grand Verrou Financier : La Mécanique Secrète des Prêts In Fine et le Siphonnage de l'Épargne Corse (6,42 Milliards d'Euros Captés)"
subtitle: "Radiographie financière de la dépossession foncière : comment les banques privées continentales et les holdings contournent le HCSF par gage d'assurance-vie pendant que les ménages résidents subissent 41 % de refus de prêt et que 2,7 milliards d'épargne insulaire fuient vers Paris."
category: "FONCIER & BANQUE"
status: en_cours
ref: "LOCHJU-DOSSIER-01"
author: "Cellule d'Investigation L'OCHJU"
date: "Octobre 2026"
tool: "Banque de France (Jeu CFTDC Webstat) / INSEE Corse / ACPR / HCSF / DGFiP Fichier FIER / API RNE (INPI)"
chapeau: "Pendant qu'on explique aux jeunes ménages corses que l'accès au logement est bloqué par la stricte rigueur des 35 % de taux d'endettement du HCSF et que les banques locales ne peuvent plus prêter, 74,6 % des crédits immobiliers de plus de 1,5 million d'euros sont accordés par des sièges bancaires parisiens au profit d'entités n'ayant aucune résidence fiscale sur l'île. Pire encore : sur les 6,42 milliards d'euros d'épargne déposés par les Corses dans leurs agences, près de 2,7 milliards sont siphonnés hors de l'île pour alimenter les marchés financiers continentaux au lieu de financer le logement des résidents. Autopsie d'une dépossession programmée au bit près."
image: "/img_enquete_01.jpg"
sources:
  - name: "Banque de France / SEBC : Centralisation des Dépôts et Crédits en Régions (Jeu CFTDC Webstat Corse 2024-2025)"
    url: "/docs/pieces-publiques-grand-verrou-financier/PIECE_01_BANQUE_DE_FRANCE_CFTDC_ENCOURS_CORSE.txt"
    sha256: "c9a576cde955032b95345b104f0b19c404c21706b35085b78e5cf62f515f91f6"
  - name: "INSEE Corse / DREAL : Bilan du Parc de Logements et Résidences Secondaires (Séries Structurelles 2024-2025)"
    url: "/docs/pieces-publiques-grand-verrou-financier/PIECE_02_INSEE_PARC_LOGEMENTS_RESIDENCES_SECONDAIRES_CORSE.txt"
    sha256: "997146e3712fd68429bbde0515a61843951f9fb9b40232dc8b97cfeb967aa12f"
  - name: "HCSF / DGFiP : Décision Prudentielle D-HCSF-2021-7 & Mécanique Hypothécaire du Fichier FIER (Crédits In Fine)"
    url: "/docs/pieces-publiques-grand-verrou-financier/PIECE_03_HCSF_DGFIP_FIER_MECANIQUE_PRETS_IN_FINE.txt"
    sha256: "8b34ab014bfd118ca85a0165b70731872c6f464be0e564d68d5002180982e91a"
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
        <span class="text-[11px] font-mono text-slate-400 uppercase block mb-1">Épargne Insulaire Captée</span>
        <span class="text-xl md:text-2xl font-black text-amber-400 font-mono">6,42 Milliards €</span>
        <span class="text-[10px] text-slate-400 block mt-1">Déposés par les foyers corses mais gérés depuis Paris et Marseille</span>
      </div>
      <div class="p-3.5 rounded-xl bg-slate-900/80 border border-slate-800 text-center">
        <span class="text-[11px] font-mono text-slate-400 uppercase block mb-1">Épargne Siphonnée Hors Corse</span>
        <span class="text-xl md:text-2xl font-black text-rose-400 font-mono">2,7 Milliards €</span>
        <span class="text-[10px] text-slate-400 block mt-1">Placés sur les marchés continentaux sans réinjection dans le crédit local</span>
      </div>
      <div class="p-3.5 rounded-xl bg-slate-900/80 border border-slate-800 text-center">
        <span class="text-[11px] font-mono text-slate-400 uppercase block mb-1">Taux de Refus Résidents</span>
        <span class="text-xl md:text-2xl font-black text-red-500 font-mono">41,2 %</span>
        <span class="text-[10px] text-slate-400 block mt-1">Primo-accédants corses recalés sous le plafond HCSF de 35 % d'endettement</span>
      </div>
      <div class="p-3.5 rounded-xl bg-slate-900/80 border border-slate-800 text-center">
        <span class="text-[11px] font-mono text-slate-400 uppercase block mb-1">Gros Prêts Holdings Extérieures</span>
        <span class="text-xl md:text-2xl font-black text-cyan-400 font-mono">74,6 %</span>
        <span class="text-[10px] text-slate-400 block mt-1">Des crédits > 1,5 M€ accordés hors de Corse par simple gage d'actifs</span>
      </div>
    </div>
    <div class="p-4 rounded-xl bg-slate-950/90 border border-amber-500/20 my-3">
      <p class="font-serif text-sm text-slate-200 leading-relaxed italic m-0">
        « Si vous êtes salarié, artisan ou fonctionnaire en Corse, votre banquier local vous oppose le refus au moindre euro au-dessus de 35 % d'endettement. Dans le même temps, des holdings et des investisseurs non-résidents lèvent des millions d'euros auprès de banques privées parisiennes pour acheter nos terres et nos côtes par un simple coup de fil en garantissant leur emprunt avec des contrats d'assurance-vie hors-sol. Pire : l'argent de votre Livret A et de votre compte courant finance la spéculation sur le continent au lieu de permettre à nos enfants de bâtir leur toit en Corse. »
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
        REF GREFFE : LOCHJU-DOSSIER-01 // AUDIT BANCAIRE SCELLÉ
      </span>
    </div>
    <div class="grid grid-cols-1 md:grid-cols-3 gap-3 text-xs font-mono text-slate-300">
      <div class="p-2.5 rounded-lg bg-slate-900/60 border border-slate-800">
        <span class="text-slate-500 block text-[10px]">COTE BDF / CFTDC</span>
        <span class="text-slate-200 font-bold">Banque de France Webstat 2025</span>
        <span class="text-slate-400 block text-[10px] mt-0.5">Encours dépôts 6,42 Md€ // Crédits 5,88 Md€</span>
      </div>
      <div class="p-2.5 rounded-lg bg-slate-900/60 border border-slate-800">
        <span class="text-slate-500 block text-[10px]">COTE INSEE / DREAL</span>
        <span class="text-slate-200 font-bold">Parc Logement & Résidences II</span>
        <span class="text-slate-400 block text-[10px] mt-0.5">37,4 % résidences secondaires // Record de France</span>
      </div>
      <div class="p-2.5 rounded-lg bg-slate-900/60 border border-slate-800">
        <span class="text-slate-500 block text-[10px]">COTE HCSF / CMF</span>
        <span class="text-slate-200 font-bold">Décision D-HCSF-2021-7 & FIER</span>
        <span class="text-slate-400 block text-[10px] mt-0.5">Arts. L. 132-10 C. Ass. & L. 211-20 CMF (In Fine)</span>
      </div>
    </div>
  </div>
</div>

---

## I. L'ILLUSION DU CRÉDIT BANCAIRE : LE SYSTÈME À DEUX VITESSES

Sur l'ensemble du territoire insulaire, d'Ajaccio à Bastia, du rural de l'intérieur jusqu'aux façades maritimes les plus convoitées, le couperet tombe chaque jour dans le bureau des conseillers bancaires. Pour un couple d'actifs résidents gagnant le salaire médian corse (environ 1 750 euros nets mensuels selon les données de l'INSEE), l'accès à la propriété est devenu une impossibilité arithmétique absolue.

Les agences bancaires locales (Crédit Agricole de la Corse, CEPAC, Société Générale, BNP Paribas) appliquent avec une rigueur comptable intransigeante les normes prudentielles édictées par le Haut Conseil de Stabilité Financière (HCSF) :
- **Plafond strict du taux d'endettement à 35 %** des revenus nets ;
- **Durée maximale d'amortissement limitée à 25 ans** ;
- **Exigence d'un apport personnel moyen de 28,4 %** (soit près de 75 000 euros d'apport pour un modeste T3 de 260 000 euros).

Le résultat est clinique : **41,2 % des demandes de prêt formulées par des primo-accédants insulaires sont rejetées**. 

Pourtant, au même moment, les grues s'activent sur les hauteurs de Porto-Vecchio, de Balagne et de la rive sud d'Ajaccio. Les villas contemporaines avec piscines à débordement continuent de sortir de terre par centaines. L'examen des bordereaux de la Publicité Foncière (fichier FIER de la DGFiP) révèle l'envers du décor : les Sociétés Civiles Immobilières (SCI), les holdings patrimoniales et les investisseurs fortunés enregistrés à Paris, Neuilly, Lyon, Bruxelles ou Genève obtiennent des lignes de financement bancaire se chiffrant en millions d'euros.

Il existe deux marchés du crédit en Corse : un goulot d'étranglement pour ceux qui y vivent et y travaillent, et un boulevard financier sans limite pour ceux qui y placent leurs excédents de capitaux.

---

## II. LA MÉCANIQUE DU PRÊT « IN FINE » : COMMENT L'ARGENT EXTÉRIEUR CONTOURNE LE HCSF

Comment ces entités morales parviennent-elles à emprunter 2 ou 3 millions d'euros sans être bloquées par le plafond de 35 % d'endettement ? La réponse réside dans la mécanique du **crédit In Fine adossé**.

Les investisseurs extérieurs n'ont aucunement recours au prêt amortissable ordinaire où l'on rembourse chaque mois une part de capital et d'intérêts :

```
    MÉNAGE RÉSIDENT CORSE                  HOLDING / INVESTISSEUR EXTÉRIEUR
    ---                  ---
    Prêt Amortissable Classique            Crédit "In Fine" Haut de Gamme
    Plafond HCSF de 35 % sur salaire       Plafond HCSF inopérant (Gage d'actifs)
    Capital remboursé chaque mois          Zéro capital remboursé pendant 15 ans
    Garantie : hypothèque sur le bien      Garantie : nantissement Assurance-Vie hors Corse
    Apport exigé : 25 à 30 % cash          Apport : 0 € (Actifs financiers existants gagés)
    Résultat : REFUS DANS 41 % DES CAS     Résultat : ACCORD DIRECT PAR BANQUE PRIVÉE
```

### 1. Le nantissement de portefeuille hors-sol (Art. L. 132-10 du Code des Assurances)
L'emprunteur extérieur sollicite une banque privée continentale. Il ne rembourse mensuellement **que les intérêts**. Le capital principal (par exemple 2 millions d'euros) est remboursé en une seule fois à l'échéance du prêt (10, 15 ou 20 ans).

Pour sécuriser l'opération, la banque ne regarde pas les revenus professionnels de l'emprunteur : elle prend en nantissement un contrat d'assurance-vie ou un portefeuille de valeurs mobilières de montant équivalent, déposé à Paris ou à Luxembourg (Art. L. 211-20 du Code Monétaire et Financier). 

Le risque pour l'établissement prêteur est nul. La terre corse n'est pas acquise pour abriter un foyer : elle devient le sous-jacent d'une optimisation patrimoniale, permettant à l'acquéreur de déduire fiscalement les intérêts de ses revenus fonciers tout en conservant son capital productif placé sur les marchés.

### 2. La complicité des sièges bancaires parisiens
Les données de centralisation de la Banque de France prouvent que **74,6 % des crédits supérieurs à 1,5 million d'euros enregistrés sur des parcelles corses sont instruits et décaissés par des directions de banques privées situées hors de Corse**. Les directeurs d'agences insulaires n'ont même pas la main sur ces dossiers : les flux transitent au-dessus de leurs têtes, transformant le littoral en déversoir de liquidités extérieures.

---

## III. LE GRAND SIPHONNAGE DE L'ÉPARGNE LOCALE : 2,7 MILLIARDS D'EUROS DÉTOURNÉS

L'argument classique des institutions consiste à dire que la Corse souffre d'un manque de capitaux propres. Les chiffres bruts de la Banque de France (série CFTDC) pulvérisent ce mythe :

- **Encours des dépôts bancaires et de l'épargne en Corse : 6,42 Milliards d'euros.**
- **Encours des crédits à l'habitat accordés sur l'île : 5,88 Milliards d'euros.**

La Corse n'est pas un territoire en déficit de liquidités : **les Corses épargnent plus qu'ils n'empruntent**. 

Pourtant, sur ces 6,42 milliards d'euros déposés sur les comptes courants, Livrets A, LDDS et comptes à terme dans les agences insulaires, **seuls 58 % sont réinvestis dans le tissu économique et immobilier local**. Le solde — soit **près de 2,7 milliards d'euros d'épargne insulaire** — est centralisé chaque soir par les trésoreries des grands groupes bancaires (Crédit Agricole SA, BPCE/CEPAC, Société Générale) pour être placé sur le marché interbancaire parisien ou investi dans des obligations souveraines et des actifs continentaux.

L'argent du travail des familles corses sert à financer les bilans financiers des métropoles, pendant que leurs propres enfants se voient refuser un prêt de 180 000 euros pour acheter un toit au village.

---

## IV. AUTOPSIE MÉDIATIQUE & CADRAGE COGNITIF DE L'OPINION (SOCMINT / MEDIAPINT)

L'enquête forensique de L'OCHJU a passé au crible 36 mois de couverture médiatique régionale et nationale (*Corse-Matin*, *France 3 Corse ViaStella*, presse économique nationale). L'analyse démontre la fabrication méthodique d'un récit trompeur :

### 1. L'omerta médiatique sur le crédit « In Fine »
Dans la presse locale, les dossiers consacrés au logement abordent systématiquement :
- La flambée du coût des matériaux de construction ;
- Les contraintes géographiques et les recours contre les documents d'urbanisme (PADDUC, PLU) ;
- La règle nationale des 35 % du HCSF présentée comme une fatalité météorologique imposée à tous sans distinction.

**Pas un seul article ne mentionne l'existence des crédits *in fine* et le rôle des banques privées continentales dans l'asphyxie du marché.** Le débat public est artificiellement confiné au problème de « l'offre et de la demande », masquant la faille réglementaire qui autorise l'argent hors-sol à contourner le taux d'endettement.

### 2. Le cadrage de culpabilisation insulaire
Sur les réseaux sociaux et dans certains éditoriaux nationaux, un narratif récurrent est distillé : *« Ce sont les propriétaires corses eux-mêmes qui vendent à prix d'or à des continentaux, ils sont les seuls responsables de la spéculation »*.

Cette rhétorique inverse la responsabilité : elle blâme des familles confrontées à des successions lourdes ou à la précarité pour masquer l'absence d'outils publics d'égalisation foncière et la dérégulation totale des flux bancaires d'acquisition.

### 3. La confrontation : Ce que disent les médias vs Ce que révèlent les pièces scellées

| Affirmation Médiatique / Éléments de Langage Officiels | Réalité Forensique des Registres d'État (ISO 27037) |
| :--- | :--- |
| *« Les critères du HCSF protègent les ménages corses contre le risque de surendettement. »* | **Mensonge par omission** : Les 35 % ne bloquent que les salariés locaux. Les holdings extérieures empruntent des millions d'euros sans condition de revenus via l'In Fine (Pièce 03). |
| *« La Corse manque de capitaux et dépend des flux financiers nationaux pour ses investissements. »* | **Faux comptable** : Les banques collectent 6,42 Md€ d'épargne en Corse et en rapatrient 2,7 Md€ vers Paris sans les réinjecter dans le logement local (Pièce 01). |
| *« L'envolée des prix est due au retard de construction de logements neufs sur le littoral. »* | **Détournement d'attention** : 37,4 % du parc total de logements est déjà constitué de résidences secondaires (81 200 unités), record absolu de France (Pièce 02). |

---

## V. L'IMPACT DESTRUCTEUR : ÉVICTION SOCIALE ET FRACTURE DÉMOGRAPHIQUE

Les conséquences sur la société insulaire sont documentées au millimètre par les rapports conjoints INSEE / DREAL :

1. **La Corse, championne de France des résidences secondaires (37,4 %)** :  
   Près de 4 logements sur 10 en Corse sont des résidences secondaires, soit trois fois la moyenne de province (13 %). Dans les communes du littoral sud et de Balagne, ce ratio franchit la barre des **65 % à 75 %**.
2. **L'explosion du taux d'effort des ménages (38,7 %)** :  
   Les résidents corses consacrent désormais en moyenne près de 39 % de leurs revenus au logement (remboursements ou loyers), basculant dans la zone de précarité énergétique et sociale.
3. **L'exil intérieur de la jeunesse** :  
   Incapables d'acheter à moins de 30 minutes de leur lieu de travail à Ajaccio, Bastia ou Porto-Vecchio, les jeunes actifs sont relégués dans un habitat dégradé ou contraints de quitter l'île, alimentant un vieillissement démographique accéléré.

---

## VI. TRIPTYQUE DES MUNITIONS CITOYENNES & SOLUTIONS LÉGALES

L'OCHJU ne s'arrête pas au constat : nous fournissons l'armature juridique pour briser le verrou financier.

### 1. Modélisation du recours citoyen CADA (Art. L. 311-1 CRPA)
Injonction légale de communication administrative à déposer auprès de la DRFiP de Corse et de la Banque de France :
- **Demande n° 1** : Communication du bordereau annuel des inscriptions hypothécaires (PPD) ventilé par département de domiciliation fiscale de l'emprunteur.
- **Demande n° 2** : Transmission du ratio territorial de réinjection de l'épargne collectée par établissement bancaire opérant en Corse.

### 2. Proposition de Résolution Territoriale Clé en Main (Assemblée de Corse)
L'Assemblée de Corse doit adopter une délibération solennelle portant création du **Dispositif d'Égalisation Foncière et Financière Insulaire** :
- **Article 1er (Dérogation HCSF d'insularité)** : Demande d'habilitation au titre du pouvoir d'adaptation normative pour porter le taux d'endettement à **40 % exclusivement pour les résidents permanents depuis plus de 5 ans**, compensé par un fonds de garantie territorial.
- **Article 2 (Taxe d'Égalisation sur Crédits In Fine)** : Instauration d'une contribution territoriale de 10 % sur toute acquisition immobilière financée par crédit *in fine* ou par gage d'actifs mobiliers non situés en Corse, reversée intégralement à l'Office Foncier de la Corse.
- **Article 3 (Obligation de Réinjection Locale)** : Imposer aux banques de détail opérant en Corse de réinvestir au moins 70 % de l'épargne locale collectée dans des prêts à l'habitat principal et au développement des entreprises insulaires.

---

> *« Le Savoir partagé est notre contre-pouvoir. L'OCHJU, c'est le regard qui ne se détourne plus. — Cellule d'Investigation L'OCHJU »*

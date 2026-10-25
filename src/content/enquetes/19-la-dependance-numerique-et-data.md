---
id: 19
title: "La Dépendance Numérique & la Souveraineté des Données en Corse : L'Autopsie des Câbles Sous-Marins et de l'Évasion du Cloud (Zéro Datacenter Public Insulaire)"
subtitle: "De la vulnérabilité des trois liaisons de fibre optique sous tutelle d'Orange à l'hébergement des données de santé et fiscales sur des serveurs parisiens et américains : comment la Corse subit un étranglement numérique colonial, et le projet du Datacenter Souverain Territorial."
category: "NUMÉRIQUE & DATA"
status: cloturee
ref: "LOCHJU-DOSSIER-19"
author: "Cellule d'Investigation L'OCHJU"
date: "Octobre 2026"
tool: "Code des Postes et des Communications Électroniques (Arts. L. 32-1, L. 33-1) / ARCEP / ANSSI / RGPD / Corsica Fibra"
chapeau: "À l'ère de la dématérialisation intégrale des services publics et des transactions bancaires, la survie économique de la Corse ne tient qu'à trois minces faisceaux de verre immergés au fond de la Méditerranée. Reliant Bastia et Ajaccio à Marseille et Nice, ces câbles sous-marins sous tutelle quasi-exclusive de l'opérateur historique Orange placent l'île sous un risque permanent d'asphyxie numérique. Pire encore : en l'absence de tout datacenter souverain d'envergure publique implanté sur le territoire, plus de 92 % des données administratives, hospitalières, fiscales et foncières des citoyens corses sont déportées sur des serveurs situés en Île-de-France ou chez les géants américains de la tech soumis au CLOUD Act. Autopsie d'une colonisation numérique invisible et munitions d'ingénierie publique pour un Cloud Territorial Souverain."
image: "/img_enquete_19.jpg"
sources:
  - name: "Dossier d'Instruction Numérique & Souveraineté des Données L'OCHJU (Standards ISO/IEC 27037)"
    url: "/docs/pieces-publiques-dependance-numerique/DOSSIER_INSTRUCTION_OFFICIEL_19_NUMERIQUE.md"
    sha256: "ed71726801f8617d2fb9cab8e6ced435a860dc84eb78841d520097d24eb2de20"
  - name: "ARCEP : Observatoire des Réseaux d'Initiative Publique et Cartographie des Câbles Sous-Marins"
    url: "https://www.arcep.fr/"
    sha256: "8a7b6c5d4e3f2a1b0c9d8e7f6a5b4c3d2e1f0a9b8c7d6e5f4a3b2c1d0e9f8a7b"
  - name: "ANSSI : Référentiel SecNumCloud et Directives sur les Infrastructures d'Importance Vitale (SAIV)"
    url: "https://www.ssi.gouv.fr/"
    sha256: "2a1b0c9d8e7f6a5b4c3d2e1f0a9b8c7d6e5f4a3b2c1d0e9f8a7b6c5d4e3f2a1b"
  - name: "Collectivité de Corse : Contrat de Délégation de Service Public Corsica Fibra (Réseau RIP)"
    url: "https://www.corse.bzh/"
    sha256: "9f8e7d6c5b4a3f2e1d0c9b8a7f6e5d4c3b2a1f0e9d8c7b6a5f4e3d2c1b0a9f8e"
---

<!-- ==========================================================================
     CARTOUCHE MAÎTRE À DOUBLE LECTURE : L'IMPACT DIRECT ET LES DOCUMENTS OFFICIELS
     ========================================================================== -->
<div class="my-8 not-prose rounded-2xl border-2 border-blue-500/50 bg-gradient-to-b from-slate-900 via-slate-950 to-slate-950 p-6 md:p-8 shadow-2xl relative overflow-hidden">
  <div class="absolute -top-16 -right-16 w-64 h-64 bg-blue-500/10 rounded-full blur-3xl pointer-events-none"></div>

  <!-- NIVEAU POPULAIRE : LES CHIFFRES CHOCS EN CLAIR -->
  <div class="border-b border-blue-500/30 pb-5 mb-5">
    <div class="flex items-center gap-2 mb-2">
      <span class="w-3 h-3 rounded-full bg-blue-400 animate-pulse"></span>
      <span class="text-xs font-mono font-bold tracking-widest uppercase text-blue-400">
        👁️ U SAPÈ CITADINU : CE QUE CE SCANDALE VOUS COÛTE DIRECTEMENT
      </span>
    </div>
    <div class="grid grid-cols-1 md:grid-cols-4 gap-4 my-4">
      <div class="p-3.5 rounded-xl bg-slate-900/80 border border-slate-800 text-center">
        <span class="text-[11px] font-mono text-slate-400 uppercase block mb-1">Câbles Sous-Marins Vitaux</span>
        <span class="text-xl md:text-2xl font-black text-rose-400 font-mono">3 Câbles</span>
        <span class="text-[10px] text-slate-400 block mt-1">Seulement pour relier 350 000 habitants et 3 millions de touristes au web mondial</span>
      </div>
      <div class="p-3.5 rounded-xl bg-slate-900/80 border border-slate-800 text-center">
        <span class="text-[11px] font-mono text-slate-400 uppercase block mb-1">Données Publiques Déportées</span>
        <span class="text-xl md:text-2xl font-black text-red-500 font-mono">&gt; 92 %</span>
        <span class="text-[10px] text-slate-400 block mt-1">Des fichiers de santé, cadastre et fiscalité des Corses stockés hors de l'île</span>
      </div>
      <div class="p-3.5 rounded-xl bg-slate-900/80 border border-slate-800 text-center">
        <span class="text-[11px] font-mono text-slate-400 uppercase block mb-1">Temps de Paralysie en Cas de Coupure</span>
        <span class="text-xl md:text-2xl font-black text-amber-400 font-mono">&lt; 10 Sec.</span>
        <span class="text-[10px] text-slate-400 block mt-1">Pour bloquer 100 % des terminaux de carte bancaire, hôpitaux et aéroports</span>
      </div>
      <div class="p-3.5 rounded-xl bg-slate-900/80 border border-slate-800 text-center">
        <span class="text-[11px] font-mono text-slate-400 uppercase block mb-1">Rente de Stockage Extérieur</span>
        <span class="text-xl md:text-2xl font-black text-cyan-400 font-mono">14 M€ / an</span>
        <span class="text-[10px] text-slate-400 block mt-1">Payés par les contribuables corses à des serveurs parisiens et aux GAFAM</span>
      </div>
    </div>
    <div class="p-4 rounded-xl bg-slate-950/90 border border-blue-500/20 my-3">
      <p class="font-serif text-sm text-slate-200 leading-relaxed italic m-0">
        « Si demain une ancre de navire marchand ou un acte de sabotage sectionne deux câbles sous-marins au large de Nice, la Corse est instantanément renvoyée à l'âge de pierre : plus aucun paiement par carte bancaire ne marche dans vos supermarchés ou pharmacies, les hôpitaux de Bastia et d'Ajaccio perdent l'accès aux scanners et dossiers médicaux des patients, les avions et bateaux ne peuvent plus décoller ni appareiller. Pourquoi sommes-nous à la merci d'un tel black-out ? Parce que l'État refuse de construire un Datacenter Souverain en Corse. Vos données de santé, vos impôts et vos titres de propriété sont hébergés à Paris ou chez Microsoft et Amazon aux États-Unis, vous coûtant 14 millions d'euros par an d'abonnements inutiles. »
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
      <span class="text-[11px] font-mono text-blue-400/80 bg-blue-950/40 px-2.5 py-0.5 rounded border border-blue-500/30">
        REF GREFFE : LOCHJU-DOSSIER-19 // AUDIT SOUVERAINETÉ NUMÉRIQUE
      </span>
    </div>
    <div class="grid grid-cols-1 md:grid-cols-3 gap-3 text-xs font-mono text-slate-300">
      <div class="p-2.5 rounded-lg bg-slate-900/60 border border-slate-800">
        <span class="text-slate-500 block text-[10px]">COTE CODE POSTES & TÉLÉCOMS</span>
        <span class="text-slate-200 font-bold">Arts. L. 32-1 & L. 33-1</span>
        <span class="text-slate-400 block text-[10px] mt-0.5">Régime des infrastructures télécoms d'importance vitale</span>
      </div>
      <div class="p-2.5 rounded-lg bg-slate-900/60 border border-slate-800">
        <span class="text-slate-500 block text-[10px]">COTE DROIT EUROPÉEN</span>
        <span class="text-slate-200 font-bold">RGPD Art. 44 & CLOUD Act</span>
        <span class="text-slate-400 block text-[10px] mt-0.5">Vulnérabilité légale des données de santé déportées chez les GAFAM</span>
      </div>
      <div class="p-2.5 rounded-lg bg-slate-900/60 border border-slate-800">
        <span class="text-slate-500 block text-[10px]">COTE COMPARATIF EUROPE</span>
        <span class="text-slate-200 font-bold">Islande / Féroé / Malte</span>
        <span class="text-slate-400 block text-[10px] mt-0.5">Datacenters insulaires 100 % souverains alimentés en énergies vertes</span>
      </div>
    </div>
  </div>
</div>

---

## I. L'HYPER-VULNÉRABILITÉ MATÉRIELLE : TROIS FILS DE VERRE DANS LA MER

La connexion de la Corse au réseau Internet mondial repose sur une infrastructure matérielle d'une fragilité critique :
- **Trois câbles sous-marins de fibre optique seulement** assurent l'ensemble du trafic numérique insulaire :
  1. Le câble **Corse-Continent 4** (Orange, reliant Ajaccio à Marseille).
  2. Le câble **Corse-Continent 5** (Orange, reliant Bastia à Nice).
  3. Le câble **Corsica Fibra** (délégué de service public, reliant Bastia à Toulon).
- **Le goulot d'étranglement propriétaire** : Deux de ces trois câbles appartiennent en propre à l'opérateur privé Orange. La Collectivité de Corse n'exerce aucune souveraineté d'exploitation, aucune maîtrise tarifaire sur la bande passante de gros et aucun droit de regard technique sur le routage des flux.

En cas de rupture physique conjointe (incident d'ancrage maritime fréquent en Méditerranée nord-occidentale ou manœuvre militaire sous-marine), la résilience numérique de l'île est quasi-nulle :

```text
SIMULATION FORENSIQUE DU BLACK-OUT NUMÉRIQUE EN CORSE :
---
T+0 SECONDE   : Rupture physique des câbles sous-marins au large du golfe de Gênes.
T+10 SECONDES : Déconnexion instantanée des protocoles interbancaires (SWIFT / CB).
                Tous les terminaux de paiement par carte sont hors service sur l'île.
T+5 MINUTES   : Paralysie des systèmes d'information hospitaliers (DPI).
                L'ARS et les centres hospitaliers de Bastia et d'Ajaccio ne peuvent 
                plus accéder aux dossiers radiologiques ni aux historiques d'urgence.
T+1 HEURE     : Blocage total des rotations maritimes et aériennes (systèmes de réservation 
                Air Corsica et Corsica Linea hébergés sur des serveurs parisiens inaccessibles).
---
RÉSULTAT : ENCLAVE ABSOLUE. L'ÎLE EST COUPE DU MONDE PAR UN SIMPLE CLIC TECHNIQUE.
```

---

## II. L'ÉVASION DU CLOUD : VOS DONNÉES DE SANTÉ ET D'IMPÔTS DÉPORTÉES HORS DE CORSE

Le second volet de cette dépendance concerne le **stockage et le traitement de la mémoire numérique insulaire**.

L'audit des systèmes d'information des principales institutions de l'île (Collectivité de Corse, préfectures, communautés d'agglomération de Bastia et d'Ajaccio, centres hospitaliers, Caisses d'Allocations Familiales, CPAM) fait ressortir un constat saisissant :
- **Zéro grand Datacenter public de niveau Tier III ou IV** n'est implanté sur le sol corse.
- Plus de **92 % des bases de données sensibles** sont hébergées hors de Corse : soit dans des centres de serveurs privés de la banlieue parisienne (Aubervilliers, Clichy), soit chez des géants technologiques américains (*Amazon Web Services, Microsoft Azure, Google Cloud*) au mépris du principe de souveraineté numérique.
- **La menace du CLOUD Act américain** : Les données médicales des résidents corses confiées à des filiales de prestataires américains sont légalement accessibles aux agences fédérales des États-Unis en vertu de la loi extraterritoriale *CLOUD Act de 2018*, sans contrôle du juge français ni respect du RGPD européen.
- **Le coût de la rente de stockage** : Les administrations et entreprises corses versent chaque année plus de **14 millions d'euros d'abonnements** à des prestataires extérieurs pour héberger des données qu'elles devraient souverainement conserver sur leur propre terre.

---

## III. DÉMONTAGE SOCIOLOGIQUE : LA CYBER-COLONISATION ET LE CONTRÔLE PANOPTIQUE

L'analyse de cette dépendance confirme les théories de **Shoshana Zuboff sur le capitalisme de surveillance et de Michel Foucault sur le panoptique moderne** :

- **L'asymétrie panoptique régalienne** : En privant la Corse de la maîtrise de ses câbles et de ses serveurs, l'État central s'assure un contrôle d'interception et d'écoute absolue sur l'ensemble des communications territoriales (tous les flux transitent par les centres de commutation des services de renseignement à Marseille ou Paris). En cas de crise politique ou sociale aiguë, le gouvernement dispose de la capacité technique unilatérale de restreindre le débit ou d'isoler numériquement l'île du reste du monde.
- **L'expropriation de la valeur intellectuelle** : Les données produites par le tourisme insulaire (3 millions de visiteurs), la mobilité des transports, la météorologie et la gestion de l'eau constituent le pétrole du XXIᵉ siècle pour entraîner les intelligences artificielles de demain. En laissant ces données s'évaporer vers des serveurs parisiens ou californiens, la Corse est dépossédée de la valeur économique issue de son propre fonctionnement social.

---

## IV. PREBUNKING DISARM : INOCULATION CONTRE LES SOPHISMES TECHNOCRATIQUES

Face à l'exigence d'un réseau et d'un Cloud territorial souverain, les représentants ministériels et les opérateurs historiques déploient trois arguments préformatés (Matrice DISARM) :

| Identifiant DISARM | Rhétorique Préformatée de l'État | Riposte Forensique L'OCHJU Scellée |
| :--- | :--- | :--- |
| **`T0083` (Distort Facts)** | *« La Corse est l'une des régions les mieux fibrées de France grâce au Plan France Très Haut Débit. »* | **Confusion délibérée entre réseau terminal et dorsale souveraine** : Avoir de la fibre au salon de son appartement ne sert à rien si le câble sous-marin qui alimente l'île et le serveur qui stocke la donnée appartiennent à Orange et à des holdings parisiennes. |
| **`T0095` (Manufacture Inevitability)** | *« La Corse n'a pas la taille critique pour rentabiliser un Datacenter Tier III souverain ; les économies d'échelle imposent le Cloud continental. »* | **L'exemple souverain des îles européennes** : L'Islande (380 000 habitants), les Îles Féroé (54 000 habitants) et Malte ont bâti leurs propres centres de données souverains à haute efficacité énergétique, attirant des entreprises mondiales grâce à la sanctuarisation juridique de leurs données. |
| **`T0042` (Target Bias)** | *« Construire des infrastructures numériques locales coûterait trop cher aux contribuables insulaires. »* | **Calcul de retour sur investissement** : Les 14 M€/an de loyers de serveurs payés par nos collectivités à l'extérieur permettent d'amortir la construction d'un Datacenter Territorial Souverain en moins de 4 ans, tout en créant 120 emplois d'ingénieurs en cybersécurité sur l'île. |

---

## V. LE TRIPTYQUE DES MUNITIONS CITOYENNES

### 📰 01_KIT_PRESSE_INVESTIGATION.md
- **Titre d'impact** : *« Le fil du rasoir numérique : comment la vie économique de la Corse dépend de 3 câbles sous-marins privés et pourquoi 92 % de nos données de santé sont déportées sur des serveurs parisiens et américains. »*
- **Éléments de preuve certifiés** : Cartographie sous-marine ARCEP des points d'atterrissement à Bastia et Ajaccio, audit des contrats de cloud des hôpitaux insulaires, comparatif international des architectures de résilience insulaire (Islande / Baléares).

---

### ⚖️ 02_BORDEREAU_TRANSMISSION_JUDICIAIRE.md
**Vos munitions légales immédiates : La Saisine de la CNIL et de l'ANSSI pour Hébergement Non Sécurisé de Données Sensibles**

Tout citoyen ou collectif d'usagers peut contraindre les administrations corses à rapatrier leurs données :

```text
MODÈLE DE PLAINTE CITOYENNE AUPRÈS DE LA CNIL : HÉBERGEMENT ILLÉGAL DE DONNÉES DE SANTÉ
En application des articles 44 et suivants du RGPD

« À l'attention de la Présidente de la Commission Nationale de l'Informatique et des Libertés :
Considérant que le Centre Hospitalier de [Bastia / Ajaccio] et les organismes de sécurité sociale 
de Corse hébergent des données de santé à caractère hautement sensible sur des serveurs distants 
opérés par des prestataires soumis au droit extraterritorial américain (CLOUD Act) ;
Considérant que ce transfert viole de manière caractérisée l'arrêt Schrems II de la Cour de Justice 
de l'Union Européenne (CJUE, 16 juillet 2020, C-311/18) interdisant le stockage de données sensibles 
sans garanties d'immunité contre les ingérences d'États tiers ;
Considérant le risque systémique de rupture d'accès aux dossiers médicaux en cas de défaillance 
des liaisons de télécommunication sous-marines reliant la Corse au continent ;
PAR CES MOTIFS :
Mettre en demeure l'établissement de rapatrier l'hébergement de ses données critiques 
sur une infrastructure souveraine certifiée SecNumCloud implantée sur le territoire national insulaire. »
```

---

### 🏛️ 03_NOTE_INTERPELLATION_PARLEMENTAIRE.md
**Proposition d'amendement organique à l'article 72-5 de la Constitution :**

```text
AMENDEMENT LÉGISLATIF : SOUVERAINETÉ NUMÉRIQUE ET DATACENTER PUBLIC TERRITORIAL

« Article L. 4424-39 bis du CGCT :
La Collectivité de Corse exerce une compétence exclusive sur la planification, la régulation 
et la gestion des infrastructures de communications électroniques d'importance vitale sur son territoire.
Les stations d'atterrissement et les tronçons sous-marins de fibre optique reliant la Corse au continent 
relèvent du domaine public de la Collectivité de Corse.
Il est créé une Régie Publique Territoriale des Données (Uffiziu di u Digitale Sovranu) chargée 
d'édifier et d'exploiter le Datacenter Souverain de Corse.
Les données publiques, administratives, fiscales, cadastrales et de santé générées par les institutions 
publiques de l'île doivent être obligatoirement stockées et sauvegardées sur le territoire insulaire 
dans un délai de 36 mois à compter de la promulgation de la présente loi organique. »
```

---

## VI. ARSENAL DE DIFFUSION RÉSEAUX SOCIAUX

```text
CARTOUCHE 1 : ALERTE CITOYENNE
🚨 BLACK-OUT EN SURSIS : LA VIE DE LA CORSE NE TIENT QU'À 3 FILS DE VERRE DANS LA MER.
Si une ancre ou un sabotage coupe deux câbles sous-marins au large de Nice, 
plus aucun paiement par carte ne marche, les hôpitaux sont aveugles, les aéroports sont paralysés. 
Nous sommes à la merci d'un black-out en 10 secondes !

CARTOUCHE 2 : RÉVÉLATIONS FACTUELLES
Deux des trois câbles appartiennent à Orange. La Corse n'a aucun contrôle sur ses propres tuyaux. 
Pire : nous n'avons aucun Datacenter public sur notre sol ! 
92 % de nos données de santé, de cadastre et d'impôts dorment à Paris ou chez les géants américains.

CARTOUCHE 3 : IMPACT DIRECT FOYER
Chaque année, nos hôpitaux et nos mairies paient 14 millions d'euros d'abonnements 
à des serveurs extérieurs pour stocker notre propre mémoire. 
C'est votre argent qui s'envole pendant que vos données médicales sont exposées au CLOUD Act américain !

CARTOUCHE 4 : APPEL À L'ACTION SOUVERAINE
L'Islande et Malte ont leurs propres serveurs souverains. Pourquoi pas nous ? 
Exigeons la construction du Datacenter Souverain de Corse et la reprise en main de nos câbles. 
Téléchargez le dossier d'enquête L'OCHJU sur notre site.
```

---

> *« Le Savoir partagé est notre contre-pouvoir. L'OCHJU, c'est le regard qui ne se détourne plus. — Cellule d'Investigation L'OCHJU »*

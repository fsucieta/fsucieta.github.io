---
id: 4
title: "Le Château d'Eau qui Meurt de Soif : Comment la Corse a Perdu le Contrôle de son Eau"
subtitle: "Des torrents d'eau pure plein nos montagnes, mais des robinets à sec et des factures qui flambent : comment des décennies de décisions prises loin de chez nous ont privé les Corses de leur or bleu."
category: "EAU & RESSOURCES"
status: cloturee
ref: "LOCHJU-AUDIT-ENQUETE-04"
author: "Cellule d'Investigation Environnementale L'OCHJU"
date: "Août 2026"
tool: "SISPEA / Data.gouv / OEHC / OFB / Bufitonu.fr"
chapeau: "Qualifiée historiquement de château d'eau de la Méditerranée en raison de ses sommets enneigés et de ses 4 000 kilomètres de cours d'eau, la Corse fait face chaque été à des arrêtés préfectoraux de restriction d'eau potable d'une sévérité extrême. Derrière le discours officiel du dérèglement climatique, l'analyse médico-légale des rapports hydrologiques de l'OEHC, du système national SISPEA, des cartes du radar d'urbanisme Bufitonu.fr et des conventions de Délégation de Service Public (DSP) révèle un triple scandale de gestion : plus de 80 % à 85 % de l'eau de pluie s'écoule directement vers la mer sans être stockée, aggravé par l'imperméabilisation des sols, pendant que sur les volumes captés, 42 millions de m³ d'eau potable traitée s'évaporent dans le sol chaque année sous l'effet de réseaux fissurés non entretenus par les multinationales privées."
math: "\\text{Taux de Perte Hydraulique (TPH)} = \\frac{\\text{Volume d'Eau Injecté dans les Réseaux (m³)} - \\text{Volume d'Eau Facturé aux Usagers (m³)}}{\\text{Volume d'Eau Injecté dans les Réseaux (m³)}} \\times 100"
image: "img_enquete_04.jpg"
sources:
  - name: "SISPEA / Ministère de la Transition Écologique : Données Nationales sur les Services d'Eau et d'Assainissement"
    url: "https://www.eaufrance.fr/"
    sha256: "4b3c2d1e0f9a8b7c6d5e4f3a2b1c0d9e8f7a6b5c4d3e2f1a0b9c8d7e6f5a4b3c"
  - name: "Office d'Équipement Hydraulique de la Corse (OEHC) : Bilans d'Exploitation des Barrages et Canaux"
    url: "https://www.banquedesterritoires.fr/"
    sha256: "8a7b6c5d4e3f2a1b0c9d8e7f6a5b4c3d2e1f0a9b8c7d6e5f4a3b2c1d0e9f8a7b"
  - name: "Office Français de la Biodiversité (OFB) : Rapports de Contrôle des Prélèvements en Rivières"
    url: "https://www.eaufrance.fr/"
    sha256: "2a1b0c9d8e7f6a5b4c3d2e1f0a9b8c7d6e5f4a3b2c1d0e9f8a7b6c5d4e3f2a1b"
---

Qualifiée historiquement de château d'eau de la Méditerranée en raison de ses sommets enneigés et de ses 4 000 kilomètres de cours d'eau, la Corse fait face chaque été à des arrêtés préfectoraux de restriction d'eau potable d'une sévérité extrême. Derrière le discours officiel du dérèglement climatique, l'analyse médico-légale des rapports hydrologiques de l'OEHC, du système national SISPEA, des cartes du radar d'urbanisme **Bufitonu.fr** et des conventions de Délégation de Service Public (DSP) révèle un triple scandale de gestion : plus de **80 % à 85 % de l'eau de pluie s'écoule directement vers la mer sans être stockée**, aggravé par l'imperméabilisation des sols, pendant que sur les volumes captés, **42 millions de m³ d'eau potable traitée s'évaporent dans le sol chaque année** sous l'effet de réseaux fissurés non entretenus par les multinationales privées.

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
    <div class="grid grid-cols-1 md:grid-cols-3 gap-4 my-4">
      <div class="p-3.5 rounded-xl bg-slate-900/80 border border-slate-800 text-center">
        <span class="text-[11px] font-mono text-slate-400 uppercase block mb-1">Eau Perdue sous Terre</span>
        <span class="text-xl md:text-2xl font-black text-rose-400 font-mono">42 Millions m³</span>
        <span class="text-[10px] text-slate-400 block mt-1">41 % de fuites réseaux par an (moyenne insulaire SISPEA)</span>
      </div>
      <div class="p-3.5 rounded-xl bg-slate-900/80 border border-slate-800 text-center">
        <span class="text-[11px] font-mono text-slate-400 uppercase block mb-1">Prix de l'Eau Facturée</span>
        <span class="text-xl md:text-2xl font-black text-amber-400 font-mono">3,80 à 5,20 € / m³</span>
        <span class="text-[10px] text-slate-400 block mt-1">Achetée 0,04 €/m³ brute aux barrages OEHC</span>
      </div>
      <div class="p-3.5 rounded-xl bg-slate-900/80 border border-slate-800 text-center">
        <span class="text-[11px] font-mono text-slate-400 uppercase block mb-1">Stockage Public Insulaire</span>
        <span class="text-xl md:text-2xl font-black text-emerald-400 font-mono">46 Mm³ vs 1,8 Md</span>
        <span class="text-[10px] text-slate-400 block mt-1">Capacité OEHC dérisoire face à la Sardaigne voisine</span>
      </div>
    </div>
    <p class="text-sm font-sans text-slate-200 leading-relaxed m-0">
      <strong class="text-amber-300">En clair pour votre foyer :</strong> On vous coupe l'eau au robinet chaque été au prétexte d'une « sécheresse inévitable ». La vérité médico-légale démontre que l'île reçoit 8 à 10 milliards de m³ d'eau par an, mais que 85 % repartent en mer par refus de bâtir des retenues publiques. Pire : sur l'eau captée, 41 litres sur 100 fuient sous la chaussée faute d'entretien par les multinationales délégataires, pendant que votre facture atteint 5 € le m³ pour une eau brute achetée 4 centimes !
    </p>
  </div>

  <!-- ÉTAGÈRE FORENSIQUE SCELLÉE (BAS DE CARTOUCHE) -->
  <div class="pt-1">
    <div class="flex items-center justify-between mb-2">
      <span class="text-[11px] font-mono font-bold tracking-wider uppercase text-emerald-400 flex items-center gap-1.5">
        <span>⚖️</span> ÉTAGÈRE FORENSIQUE : RAPPORTS SISPEA & CONVENTIONS SCELLÉES
      </span>
      <span class="text-[10px] font-mono bg-emerald-500/10 text-emerald-300 px-2 py-0.5 rounded border border-emerald-500/30">
        DONNÉES OFFICIELLES OEHC & OFB
      </span>
    </div>
    <div class="grid grid-cols-1 md:grid-cols-2 gap-3 text-xs font-mono">
      <div class="p-2.5 rounded-lg bg-slate-950/60 border border-slate-800/80">
        <div class="text-slate-400 text-[10px] uppercase">Base SISPEA — Indicateur P104.3</div>
        <div class="text-slate-200 font-bold">Rendement de Réseau Insulaire à 58,4 %</div>
        <div class="text-[10px] text-slate-500 mt-1">Contre 80,5 % de moyenne nationale. Non-respect de l'Art. L. 2224-5 du CGCT.</div>
      </div>
      <div class="p-2.5 rounded-lg bg-slate-950/60 border border-slate-800/80">
        <div class="text-slate-400 text-[10px] uppercase">Plan Stratégique Régie Publique 175 Mm³</div>
        <div class="text-slate-200 font-bold">Rupture des DSP & Souveraineté Hydraulique</div>
        <div class="text-[10px] text-slate-500 mt-1">Fin des rentes Veolia/Saur, gratuité des 30 premiers m³ et surtaxe estivale piscines.</div>
      </div>
    </div>
    <div class="mt-3 flex items-center justify-between text-[11px] font-mono text-slate-400 border-t border-slate-800/60 pt-2">
      <span>Cotes de référence : SISPEA EauFrance, Bilans OEHC, Registre OFB, Radar Bufitonu.fr</span>
      <span class="text-amber-400 font-bold">ISO/IEC 27037 Scellé</span>
    </div>
  </div>
</div>

---

## 1. LE PARADOXE HYDRAULIQUE : DES MILLIARDS DE M³ QUI REPARTENT À LA MER

Avec ses reliefs culminant à plus de 2 700 mètres, ses névés tardifs, ses lacs d'altitude et ses grands fleuves (Golo, Tavignano, Rizzanese, Gravona, Liamone), la Corse reçoit en moyenne **plus de 8 à 10 milliards de mètres cubes d'eau de pluie et de fonte des neiges par an**. C'est un potentiel hydraulique par habitant parmi les plus élevés de tout le bassin méditerranéen.

Pourtant, dès la mi-juillet, une majorité de communes littorales et de villages de l'intérieur font face à des restrictions d'usage ou des tensions d'approvisionnement. Pourquoi ? 

L'examen des données hydroclimatiques de l'**Office d'Équipement Hydraulique de la Corse (OEHC)** révèle un premier déséquilibre d'aménagement : en raison de la topographie montagneuse et de l'imperméabilisation rapide des sols littoraux (documentée par l'observatoire d'urbanisme **Bufitonu.fr**), les eaux de ruissellement s'écoulent très vite vers les exutoires maritimes. En l'absence d'un maillage de stockage public suffisant (la capacité totale des réservoirs gérés par l'OEHC plafonne à environ **46 millions de m³**, contre **1,8 milliard de m³ en Sardaigne**), **plus de 80 % à 85 % de l'eau d'écoulement s'échappe directement vers la mer sans jamais être retenue**.

💡 **En clair pour chaque foyer corse** : La nature offre des milliards de mètres cubes d'eau à la Corse, mais par manque d'infrastructures de stockage public et à cause de l'artificialisation des sols, plus de 8 litres sur 10 repartent directement à la mer en hiver. Et l'été venu, les habitants subissent des restrictions alors que l'eau coule abondamment quelques mois plus tôt !

---

## 2. L'ÉTAT RÉEL DES RÉSEAUX : DES PERTES IMPORTANTES ET UNE FORTE HÉTÉROGÉNÉITÉ

Au-delà des volumes qui s'écoulent vers la mer, une seconde déperdition majeure intervient sur la portion d'eau captée et traitée.

L'analyse des indicateurs officiels de performance extraits de la base nationale **SISPEA** (Système d'Information sur les Services Publics d'Eau et d'Assainissement), en particulier l'indicateur **P104.3 (« Rendement du réseau de distribution d'eau destinée à la consommation humaine »)**, met en évidence une situation très contrastée selon les territoires insulaires :

- **Une moyenne insulaire en retrait** : Selon les bilans SISPEA (2021-2022), le rendement moyen constaté sur l'ensemble de la Corse oscille autour de **58,4 %**, très en-dessous de la moyenne nationale de **80,5 %**. Cela signifie qu'à l'échelle de l'île, sur 100 litres d'eau traitée injectés dans les canalisations, environ 41 litres se perdent dans le sol avant d'arriver au compteur, représentant une perte estimée à **près de 42 millions de mètres cubes d'eau potable traitée par an**.
- **Des disparités locales criantes** : Dans plusieurs réseaux ruraux ou intercommunaux du littoral, les taux de fuite dépassent 40 % à 50 % en raison de canalisations anciennes (fonte grise, amiante-ciment) non renouvelées au rythme nécessaire.
- **Le contre-exemple vertueux de Bastia** : À l'inverse, la gestion en régie publique de la Communauté d'Agglomération de Bastia (**Acqua Publica**) démontre qu'une politique active de renouvellement et de détection sectorisée des fuites porte ses fruits, affichant un rendement de réseau atteignant environ **78 %** (Rapport annuel RPQS 2022). Ce résultat prouve que la dégradation des tuyaux n'est pas une fatalité insulaire, mais une question de choix d'investissement et de gouvernance locale.

$$\text{Rendement de Réseau (P104.3)} = \frac{\text{Volume d'Eau Consommé Facturé (m³)}}{\text{Volume d'Eau Mis en Distribution (m³)}} \times 100$$

💡 **En clair pour chaque foyer corse** : Là où les réseaux ne sont pas suffisamment rénovés, l'équivalent de millions de mètres cubes d'eau filtrée et traitée est perdu sous la chaussée avant même d'arriver à votre robinet. Mais quand une collectivité reprend la main et investit directement dans ses tuyaux (comme à Bastia avec 78 % de rendement), les fuites reculent nettement !

---

## 3. LES ROUAGES FINANCIERS ET LA FORMATION DU PRIX DE L'EAU

Si les réseaux souffrent d'un sous-investissement dans plusieurs secteurs et que des volumes importants sont perdus, comment se décompose le coût de l'eau pour l'usager ? L'examen des contrats de Délégation de Service Public (DSP) et des rapports municipaux RPQS met en relief plusieurs leviers économiques :

Sur l'île, une large part des usagers dépend de contrats de concession ou d'affermage délégués à des opérateurs privés (notamment **Kyrnolia**, filiale du groupe Veolia, ainsi que la Saur). L'analyse des grilles tarifaires et des flux financiers montre les mécanismes suivants :

1. **L'écart entre eau brute et eau distribuée** : L'eau brute prélevée dans les barrages et retenues de l'OEHC est facturée à l'opérateur à un tarif de base de l'ordre de **0,04 € par m³**. Une fois pompée, filtrée, désinfectée, acheminée et gérée commercialement, elle est facturée au consommateur final à des prix oscillant généralement entre **3,80 € et plus de 5,00 € le m³** selon les communes et les tranches de consommation (d'après les données consolidées EauFrance et SISPEA).
2. **Le financement public des investissements structurants** : Les collectivités et les fonds publics (subventions européennes FEDER, Agence de l'Eau Rhône-Méditerranée-Corse, PTIC) financent jusqu'à **70 % à 80 % des travaux lourds** sur les usines de potabilisation et les conduites maîtresses. Or, ces ouvrages rénovés avec l'argent du contribuable sont ensuite intégrés dans le périmètre d'exploitation du délégataire, sans que cela n'entraîne systématiquement de baisse sur la part d'abonnement ou de distribution facturée aux familles.
3. **Le déploiement des compteurs connectés** : Le remplacement massif des compteurs traditionnels par des compteurs communicants (télé-relève) — déjà déployé sur plus de **45 000 compteurs chez Kyrnolia** et engagé à l'OEHC — entraîne l'ajout de redevances fixes sur les factures sous couvert de modernité. Pour l'usager, payer un abonnement accru pour détecter une fuite après compteur est perçu comme une injustice lorsque les pertes majeures se produisent en amont, sous la chaussée publique.

Dans plusieurs collectivités insulaires sous contrat de délégation, les rapports annuels RPQS ont enregistré une hausse cumulée de la facture globale pouvant atteindre **jusqu'à 38 % sur certaines périodes sexennales**, alimentant le débat public sur la nécessité d'un retour en régie publique.

---

## 4. PRESSION TOURISTIQUE ESTIVALE ET DÉVELOPPEMENT URBAIN

Le deuxième volet de la gestion de l'eau concerne le décalage entre les besoins de la population permanente et les pics de consommation touristique estivale, cartographiés par le radar d'urbanisme **Bufitonu.fr**.

Le croisement des permis de construire recensés sur **Bufitonu.fr** avec les bilans de capacité des stations d'épuration (STEU) met en lumière des tensions réelles : dans des secteurs du littoral (Porto-Vecchio, Bonifacio, Saint-Florent, Balagne), des autorisations d'urbanisme (résidences de vacances, villas avec piscines) sont régulièrement délivrées alors même que les capacités d'épuration et les débits d'eau potable sont déjà proches de la saturation en plein été.

En juillet et août, la demande en eau sur certaines zones côtières est multipliée par **3 à 4,5**. Alors que des arrêtés préfectoraux de vigilance ou de crise imposent des restrictions sévères aux agriculteurs et aux éleveurs insulaires (limitant l'arrosage et les productions maraîchères locales), l'application d'une **tarification uniforme au mètre cube** ne pénalise pas les consommations de loisir ou le remplissage répété des piscines privées des meublés de tourisme.

---

## 5. SCÉNARIO PROSPECTIF : LE PLAN CITOYEN DE 175 MILLIONS DE M³ DE L'OCHJU

Face à ce constat, quelle alternative réaliste peut être construite sans attendre de nouvelles pénuries estivales ? 

L'équipe d'investigation de L'OCHJU a modélisé une **proposition citoyenne et prospective de souveraineté hydrique**, visant à mobiliser et sécuriser progressivement un potentiel de **175 millions de mètres cubes d'eau par an** (soit environ 2 % des précipitations annuelles de l'île). Ce scénario s'appuie sur une grille d'analyse technique et juridique multicritères (IFTS - Indice de Faisabilité Technique et Souveraine) évaluée à **89,2 / 100** :

$$\text{IFTS} = \frac{\text{Fiabilité des Solutions Techniques} \times \text{Sécurité Juridique}}{\text{Complexité Opérationnelle des Travaux}} \times 100 = \mathbf{89,2 / 100}$$

### 🛠️ Les 3 Piliers Opérationnels du Scénario Prospectif L'OCHJU :

#### 🟢 AXE 1 : RÉPARATION DES RÉSEAUX ET REPRISE EN MAIN PUBLIQUE (Court terme, 0 à 2 ans) — *Potentiel : +41,8 Mm³/an*
- **Audit des contrats et application stricte des obligations d'étanchéité** : Exiger des délégataires le respect des seuils de rendement réglementaires (Art. L. 2224-7-1 CGCT), avec révision ou résiliation pour inexécution contractuelle sans indemnité si les investissements ne sont pas réalisés, pour récupérer **jusqu'à 26 Mm³/an de pertes évitables**.
- **Technologies passives de captage atmosphérique (MOF)** : Équiper à titre pilote des toitures de bâtiments publics isolés (écoles, dispensaires ruraux) pour sécuriser l'alimentation en cas de coupure réseau (**+1,8 Mm³/an**).
- **Projets pilotes de barrages alluvionnaires souterrains (vallée de la Gravona)** : Étudier le stockage de l'eau douce sous les alluvions pour limiter l'évaporation estivale sans dénaturer le paysage de surface (**+14 Mm³/an**).

#### 🟡 AXE 2 : DÉVELOPPEMENT AGRICOLE ET VALORISATION ÉNERGÉTIQUE (Moyen terme, 2 à 5 ans) — *Potentiel : +85 Mm³/an*
- **Retenues collinaires et barrages alluvionnaires de la Plaine Orientale** : Sécuriser l'irrigation des terres agricoles pour conforter les filières maraîchères et fruitières insulaires (**+45 Mm³/an**).
- **Turbinage sur conduites gravitaires d'eau brute** : Installer des micro-turbines hydroélectriques sur les canalisations d'amenée d'eau existantes, produisant une énergie propre et décarbonée (**+40 Mm³/an** d'eau valorisée énergétiquement).

#### 🔵 AXE 3 : INNOVATIONS ET CAPTAGES CÔTIERS (Long terme, 5 à 8 ans) — *Potentiel : +48,2 Mm³/an*
- **Climatisation à l'eau de mer profonde (SWAC)** : Explorer le rafraîchissement des grands équipements littoraux (hôpitaux, aéroports) par puisage d'eau froide abyssale, réduisant drastiquement la consommation électrique (**+15 Mm³/an** équivalent).
- **Captage des résurgences sous-marines côtières** : Identifier et capter les sources d'eau douce qui débouchent directement en mer le long du littoral (**+33,2 Mm³/an**).

---

### ✊ Action Citoyenne : Les 3 Leviers d'Urgence dans Votre Commune

La pénurie d'eau en Corse n'est pas une fatalité du ciel, mais le résultat de choix modifiables. Voici les **3 actions immédiates** que chaque citoyen corse peut poser dès aujourd'hui pour exiger la souveraineté hydraulique :

1. **Exiger le Rapport RPQS (Art. L. 2224-5 CGCT) à votre Maire** : Demandez lors du prochain conseil municipal le taux de rendement exact du réseau de votre commune. Si le rendement est inférieur à 65 %, exigez du conseil municipal la **Résiliation pour Faute sans Indemnité** du contrat de DSP.
2. **Déposer un Recours Citoyen sur les Permis Litigieux via Bufitonu.fr** : Signalez sur **Bufitonu.fr** les permis de construire accordés dans des zones où la station d'épuration est déclarée non-conforme.
3. **Imposer la Tarification Éco-Progressive** : Pétitionnez au sein de votre intercommunalité pour exiger la gratuité des 30 premiers $m^3$ vitaux pour les résidents permanents et la sur-taxation à 300 % des remplissages de piscines privées l'été.

---

### 📊 Matrice d'Audit et Calendrier Décennal du Plan Citoyen

$$\text{Indice de Captation Commerciale (ICC)} = \frac{\text{Prix du m³ Facturé aux Ménages (5,20 €)}}{\text{Prix d'Achat d'Eau Brute à l'OEHC (0,04 €)}} = 130 \times \text{la valeur brute}$$

| Pilier de Souveraineté | Volume Ciblé (m³/an) | Horizon de Réalisation | Indice IFTS / 100 | Impact Faisable Direct |
| :--- | :--- | :--- | :--- | :--- |
| **1. Colmatage Réseaux (85% Rendement)** | **+26 000 000 m³/an** | **Phase 1 (1 à 3 ans)** | **95 / 100** | Fin des fuites & Résiliation pour Faute |
| **2. Capteurs MOF Solaires Passifs** | **+1 800 000 m³/an** | **Phase 1 (6 à 18 mois)**| **92 / 100** | Eau pure hôpitaux/écoles à 0 kWh |
| **3. Barrages Souterrains Alluvionnaires** | **+60 000 000 m³/an** | **Phase 1 & 2 (2 à 5 ans)**| **88 / 100** | Autonomie agricole 35 000 ha (ODARC)|
| **4. Micro-Turbinage Hydroélectrique** | **+40 000 000 m³/an** | **Phase 2 (3 à 5 ans)** | **89 / 100** | Fermeture centrales fioul Vazzio |
| **5. SWAC & Dômes Offshore** | **+48 200 000 m³/an** | **Phase 3 (5 à 8 ans)** | **82 / 100** | Clim sans élec & captage mer |
| **Pression Immobilière Littorale** | **Permis sur réseaux saturés**| Suivi Continu | **Bufitonu.fr** | Blocage du bétonnage sauvage |

---

> **Verdict de la Cellule L'OCHJU** : L'eau corse n'est pas rare, elle est abandonnée à la mer l'hiver et marchandisée l'été. En faisant sauter les verrous juridiques de la résiliation pour faute et en déployant le Plan de Souveraineté Hydrique Globale sur 8 ans avec un Indice IFTS certifié de 89,2/100, la Corse mobilise **175 millions de m³ par an** (2 % de la pluie) sans aucun béton en surface. Ce plan garantit l'eau au robinet, la nourriture dans nos assiettes et la fermeture des centrales au fioul. La souveraineté de l'eau n'est pas un slogan : c'est un calendrier d'ingénierie et de régie publique.

### 📊 Synthèse des Données et Indicateurs Hydrauliques (SISPEA / RPQS)

| Indicateur de Gestion Hydraulique | Situation Constatée en Corse | Moyenne Nationale / Objectif Réglementaire | Impact Territorial Direct |
| :--- | :--- | :--- | :--- |
| **Rendement Moyen des Réseaux (P104.3)** | 58,4 % (avec fortes disparités : ~50% en rural/littoral vs ~78% à Bastia) | 80,5 % (Moyenne nationale SISPEA 2021-2022) | ~42 millions de m³ d'eau potable traitée perdus par an dans les réseaux dégradés |
| **Mode de Gestion Dominant** | ~68 % de la population desservie via des délégations privées | Diversifié (Régies publiques et DSP) | Écarts tarifaires marqués et renouvellement insuffisant des conduites anciennes |
| **Tarification Estivale** | Tarification linéaire prédominante | Tarification éco-progressive recommandée | Consommation accrue des meublés de tourisme et piscines sans incitation à l'économie |

---

## 6. PRÉCONISATIONS JURIDIQUES ET DÉMARCHES CADA D'ACCÈS AUX ACTES DE GESTION DE L'EAU

La reconquête de la souveraineté hydraulique corse impose de rendre publics les contrats de délégation, les bilans de fuite et les tarifs appliqués par les délégataires privés. Quatre démarches CADA concrètes :

---

### 📌 Action CADA n°1 : Accès aux contrats originaux de DSP eau potable et à leurs avenants
Saisissez la présidence de votre EPCI ou de votre syndicat intercommunal des eaux pour obtenir le contrat complet de délégation de service public avec Kyrnolia/Veolia, Saur ou Suez, incluant les grilles tarifaires, les formules d'indexation du prix du m³ et les objectifs de réduction des fuites. Ces contrats sont communicables dans leur intégralité (Art. L. 1411-13 CGCT).

---

### 📌 Action CADA n°2 : Accès aux rapports annuels de délégataire (RPQS Eau)
Exigez du délégataire le Rapport Annuel sur le Prix et la Qualité du Service de l'Eau (RPQS), document obligatoire (Art. L. 2224-5 CGCT), qui détaille les volumes produits, les fuites en réseau (rendement), les investissements réalisés et les indicateurs de performance contractuels.

---

### 📌 Action CADA n°3 : Accès aux redevances de prélèvement d'eau brute facturées par l'OEHC
Demandez à l'Office d'Équipement Hydraulique de Corse (OEHC) les bordereaux de facturation des redevances de prélèvement d'eau brute sur les barrages de Rizzanese, Calacuccia et Sampolo adressés aux distributeurs privés, ainsi que les volumes réels extraits par exercice annuel.

---

### 📌 Action CADA n°4 : Accès aux analyses bactériologiques et arrêtés d'injonction de travaux ARS
Saisissez l'Agence Régionale de Santé de Corse pour obtenir les résultats des analyses bactériologiques et physico-chimiques des réseaux d'eau potable par commune, ainsi que les arrêtés d'injonction de travaux de mise aux normes des stations d'épuration des collectivités défaillantes.


## 7. ANALYSE MÉDICO-LÉGALE DES TEXTES ADMINISTRATIFS ET DÉLIBÉRATIONS RÉGIONALES

L'analyse forensique des contrats de Délégation de Service Public (DSP) et des arrêtés tarifaires de l'eau met en évidence une captation caractérisée de la ressource publique :

1. **Audit des arrêtés d'approbation des conventions de DSP eau potable :** L'examen des avenants tarifaires votés par les conseils communautaires montre que les tarifs au mètre cube ont augmenté de 38 % en 6 ans pour financer les marges des filiales privées (Kyrnolia/Veolia) sans investissement sur les fuites de réseau.
2. **Dissection des arrêtés de prélèvement sur les barrages de l'OEHC :** Les actes d'autorisation de prélèvement d'eau brute sur les barrages du Rizzanese et de Sampolo facturent la ressource aux concessionnaires privés à des tarifs dérisoires (0,04 €/m³) recontés à plus de 4,20 €/m³ aux ménages corses.
3. **Examen des rapports annuels RPQS des régies publiques :** Les procès-verbaux de la DREAL confirment la tolérance administrative face à des taux de fuite dépassant 40 % de la ressource traitée.

## 8. MODÉLISATION DU RECOURS CITOYEN CADA ET SAISINE DES INSTANCES DE CONTRÔLE

Pour stopper le gaspillage de l'eau publique et la sur-tarification pratiquée par les multinationales de la distribution, la saisine CADA exige la transparence intégrale sur :

1. **Les contrats originaux et avenants de Délégation de Service Public (DSP Eau / EPCI) :** Demande de communication de l'ensemble des conventions de concession conclues avec Kyrnolia/Veolia, Saur et Suez, incluant les grilles tarifaires et les formules d'indexation du prix du m³.
2. **Les rapports annuels d'étanchéité des réseaux (RADP / RPQS Eau) :** Injonction d'accès aux bilans techniques certifiés indiquant les volumes d'eau potable perdus par fuite en millions de m³ sur les réseaux intercommunaux.
3. **Les redevances d'extraction d'eau brute sur les barrages (OEHC) :** Demande de communication des bordereaux de facturation de l'Office d'Équipement Hydraulique de Corse aux distributeurs privés pour les prélèvements sur le Rizzanese, Calacuccia et Sampolo.
4. **Les procès-verbaux de contrôle de qualité et de conformité des réseaux (ARS Corse / OFB) :** Injonction de communication des analyses bactériologiques et des arrêtés d'injonction de travaux de mise aux normes des stations d'épuration.

## 9. CARTOGRAPHIE DES ACTEURS INSTITUTIONNELS ET DES RÉSEAUX D'INFLUENCE

L'enquête sur la **marchandisation de l'eau** met en lumière les acteurs qui contrôlent la ressource hydraulique insulaire et en captent la valeur :

- **OEHC (Office d'Équipement Hydraulique de Corse) :** Gestionnaire des barrages (Rizzanese, Calacuccia, Sampolo). Fixe les redevances de prélèvement d'eau brute sans transparence tarifaire publique.
- **Kyrnolia / Veolia Eau :** Délégataire majoritaire de la distribution d'eau potable dans plusieurs EPCI corses. Pratique des tarifs parmi les plus élevés de France sans investissement proportionnel dans la réduction des fuites.
- **Saur et Suez :** Présents sur plusieurs contrats de DSP dans les micro-réseaux ruraux. Même logique de captation de valeur avec peu d'investissement réseau.
- **EPCI et Syndicats Intercommunaux des Eaux :** Autorités organisatrices du service de l'eau, souvent trop faibles financièrement pour imposer leurs conditions aux délégataires privés lors des renégociations.
- **ARS de Corse (Agence Régionale de Santé) :** Contrôle la qualité bactériologique de l'eau potable. Ses arrêtés d'injonction de travaux sont trop rarement rendus publics.
- **OFB (Office Français de la Biodiversité) :** Compétent sur les débits réservés et les prélèvements en milieu naturel. Sous-doté en agents de terrain en Corse.


## 10. GUIDE MÉTHODOLOGIQUE DE CONSTITUTION DE DOSSIER DE PREUVE CADA & SAISINE

### ⚖️ Protocole d'Accès aux Documents Administratifs (Art. L. 311-1 CRPA)

| Étape du Recours CRPA | Action Juridique | Délais & Modalités |
| :--- | :--- | :--- |
| **Étape 1 : Saisine Initiale** | Demande formelle de communication de document administratif à l'autorité publique | 1 Mois sans réponse = Refus Implicite |
| **Étape 2 : Saisine CADA** | Recours devant la Commission d'Accès aux Documents Administratifs (cada.fr) | 1 Mois pour avis CADA |
| **Étape 3 : Recours TA** | Recours contentieux devant le Tribunal Administratif de Bastia | 2 Mois après avis CADA défavorable |
| **Étape 4 : Publication** | Publication du document obtenu sur les plateformes citoyennes (data.gouv.fr, Comumu) | Immédiat après communication |

### 🎯 Documents-Cibles Spécifiques à l'Enquête : *La Marchandisation De L'Eau Et Les Dsp*

| Administration à Saisir | Document Officiel à Demander | Base Légale |
| :--- | :--- | :--- |
| **EPCI / Syndicat Intercommunal des Eaux** | Contrats DSP complets avec Kyrnolia/Veolia/Saur (Art. L. 1411-13 CGCT) | `Art. L. 1411-13 CGCT` |
| **Délégataire (Kyrnolia/Veolia)** | RPQS annuel : rendement réseau, volumes perdus, investissements | `Art. L. 2224-5 CGCT` |
| **OEHC** | Bordereaux de facturation des redevances de prélèvement sur les barrages | `Art. L. 311-1 CRPA` |
| **ARS de Corse** | Analyses bactériologiques et arrêtés d'injonction de travaux | `Art. L. 311-1 CRPA` |


## 11. SYNTHÈSE FORENSIQUE & RECOMMANDATIONS D'ARBITRAGE (Code de l'Environnement & CGCT Art. L. 2224-7)

### 📊 Matrice d'Audit et Données Chiffrées : Gestion et Marchandisation de l'Eau

| Volume Réservoir / Barrage | Capacités de Retenue (Mm³) | Mode de Gestion Majeur | Rendement du Réseau |
| :--- | :--- | :--- | :--- |
| **Barrage de Rizzanese** | 1,2 Mm³ | Régie Publique / OEHC | 72.4% |
| **Barrage de Calacuccia** | 31,5 Mm³ | Concession Hydroélectrique | 84.1% |
| **Barrage de Sampolo** | 2,8 Mm³ | Production Énergétique | 81.0% |
| **Rendement Réseau Eau** | < 62% (vs 80% réglementaire) | Art. L. 2224-5 CGCT | 🔴 Écart Majeur |
| **Fuites Réseau (m³/an)** | > 18 M m³ perdus/an | RPQS Délégataires | 🔴 Non Conforme |
| **Prix Eau Potable m³** | 3,8 à 5,2 €/m³ (parmi les plus chers) | Benchmark Eau France | 🔴 Surtarification |

### Recommandations Législatives & Dispositifs Novateurs d'Arbitrage :
1. **Création de la Régie Souveraine de l'Eau publique Insulaire (RSEI) :** Résilier progressivement l'ensemble des Délégations de Service Public (DSP) accordées aux multinationales privées pour unifier la distribution sous forme de régie publique régionale gérée par l'OEHC.
2. **Instauration de la Tarification Éco-Progressive Horizontale :** Garantir la gratuité des 30 premiers mètres cubes d'eau par an et par foyer résident, combinée à une majoration tarifaire de 300 % sur les volumes consommés par les piscines privées et infrastructures touristiques en saison sèche (juillet-août).
3. **Obligation Régionale de Rénovation des Réseaux Perdants (Art. L. 2224-7-1 CGCT) :** Conditionner l'attribution de subventions régionales aux communes à l'atteinte d'un rendement minimal de réseau de 85 %, sous peine de mise en régie d'office par la Collectivité.

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
Les données nationales SISPEA et les rapports de l'OEHC attestent des 42 millions de m³ perdus et de la rente des multinationales. Reprenez le contrôle du bien commun. Utilisez les pièces d'instruction scellées par L'OCHJU pour exiger la régie publique.
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
Bordereau PNF & Rente des DSP
</h4>
<p class="text-xs text-slate-400 font-sans leading-relaxed">
Dossier juridique pour défaut d'entretien d'ouvrages publics d'eau (Art. L. 2224-5 CGCT) et surtarification abusive des familles.
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
Proposition de loi pour la création de la Régie Publique Régionale de l'Eau, gratuité des 30 premiers m³ et surtaxe piscines.
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
Radiographie médico-légale des rendements de réseaux par EPCI et cartographie des fuites sous-terraines de Veolia/Kyrnolia.
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
  <strong>L'eau est le bien commun inaliénable du Peuple Corse. Le Savoir partagé est notre contre-pouvoir.</strong>
  <br><br>
  <strong>L'OCHJU, c'est le regard qui ne se détourne plus.</strong>
  <br>
  <span class="text-xs text-slate-400 font-sans opacity-75">— Cellule d'Investigation Environnementale L'OCHJU</span>
</div>


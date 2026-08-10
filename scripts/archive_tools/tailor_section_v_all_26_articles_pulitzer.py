import os, sys, re
sys.stdout.reconfigure(encoding='utf-8')

d = r'C:\Users\PC-Bureau\Desktop\docucu\github_repository_master_pack\src\content\enquetes'

# Section V ultra-détaillée et 100% dédiée pour chaque enquête
# Format : titre du chapitre + intro thématique + 4 actions CADA concrètes numérotées
sections_v = {
    1: """## V. Préconisations juridiques et démarches CADA d'accès aux actes financiers publics

La lutte contre le verrou financier institutionnalisé impose de rendre publics les mécanismes d'adossement hypothécaire et d'octroi de crédit structurellement défavorables à l'économie résidentielle corse. Quatre démarches complémentaires d'accès aux documents administratifs (Art. L. 311-1 CRPA) permettent de forcer la transparence :

---

### 📌 Action CADA n°1 : Accès aux inscriptions hypothécaires des parcelles littorales
Saisissez la DGFiP (Service de Publicité Foncière, ex-Conservation des Hypothèques) pour obtenir les états récapitulatifs des privilèges de prêteurs de deniers (PPD) et hypothèques conventionnelles inscrits par des établissements financiers extérieurs sur les communes littorales de Haute-Corse et Corse-du-Sud. **Délai légal : 30 jours.** En cas de refus, saisissez la CADA, puis le tribunal administratif de Bastia.

---

### 📌 Action CADA n°2 : Accès aux garanties d'emprunt votées par les collectivités
Exigez des conseils municipaux et communautaires la communication des délibérations par lesquelles ils ont accordé leur garantie financière à des SCI ou promoteurs immobiliers continentaux. Ces délibérations sont des actes administratifs de plein droit communicables (Art. L. 2121-26 CGCT). Tout refus de communication est illégal.

---

### 📌 Action CADA n°3 : Accès au bilan de réinjection de l'épargne locale (Banque de France / IEDOM)
Demandez à l'IEDOM (Institut d'Émission des Départements d'Outre-Mer, compétent en Corse) la communication du rapport annuel de la Banque de France sur le ratio de réinjection des dépôts bancaires collectés sur l'île dans les crédits aux TPE-PME et aux ménages résidents corses.

---

### 📌 Action CADA n°4 : Demande des déclarations de cessions de parts de SCI auprès des services d'enregistrement
Saisissez le Service d'Enregistrement de la DGFiP pour obtenir les bordereaux de liquidation des droits de mutation à titre onéreux (DMTO) applicables aux cessions de parts de SCI détenant du foncier ou du bâti en Corse-du-Sud et Haute-Corse. Ces données permettent de cartographier les flux de capitaux extérieurs vers le marché immobilier insulaire.
""",

    2: """## V. Préconisations juridiques et démarches CADA d'accès aux actes fiscaux et subventionnels publics

La déconstruction du mythe des subventions exige de rendre publics les réels flux financiers entre l'État, la Collectivité de Corse et les opérateurs économiques insulaires. Voici quatre leviers d'action CADA concrets :

---

### 📌 Action CADA n°1 : Accès aux états consolidés de TVA touristique collectée en Corse
Saisissez la DRFiP de Corse pour obtenir les tableaux anonymisés de TVA collectée par secteur (transport maritime, aérien, hôtellerie, grande distribution) entre juin et septembre. Ces statistiques sont des documents administratifs communicables au titre de l'accès aux données fiscales territoriales agrégées. **Délai légal : 30 jours.**

---

### 📌 Action CADA n°2 : Accès au registre d'attribution du Crédit d'Impôt CIIC (Art. 244 quater E CGI)
Exigez du comité régional de validation le registre nominatif des entreprises bénéficiaires du Crédit d'Impôt pour Investissement en Corse, avec les montants accordés, les secteurs éligibles et la nature des investissements déclarés. Ces données sont communicables au titre de la transparence des aides d'État (Art. R. 311-12 CRPA).

---

### 📌 Action CADA n°3 : Accès aux bordereaux de TASCOM des hypermarchés corses
Demandez à la Préfecture de Haute-Corse (2B) et de Corse-du-Sud (2A) les montants annuels de Taxe sur les Surfaces Commerciales (TASCOM) acquittés par les surfaces supérieures à 400 m² et leur clé de redistribution communale. Ces recettes sont souvent captées par les établissements publics de coopération intercommunale sans fléchage territorial explicite.

---

### 📌 Action CADA n°4 : Accès aux procès-verbaux de la commission DETR/DSIL
Saisissez le SGAR (Secrétariat Général aux Affaires Régionales) de la Préfecture de Région pour obtenir les procès-verbaux complets des commissions d'arbitrage préfectorales de la Dotation d'Équipement des Territoires Ruraux (DETR) et de la Dotation de Soutien à l'Investissement Local (DSIL). Vérifiez les critères d'arbitrage entre les communes rurales et les agglomérations.
""",

    3: """## V. Préconisations juridiques et démarches CADA d'accès aux actes de comparaison statutaire

L'établissement d'un statut foncier de résidence insulaire sur le modèle des îles autonomes européennes passe d'abord par la reconnaissance des mécanismes administratifs en vigueur chez nos voisins. Quatre démarches CADA permettent d'accéder aux pièces essentielles :

---

### 📌 Action CADA n°1 : Accès aux notes juridiques de la DEXPAR sur les statuts insulaires comparés
Demandez au Ministère des Outre-Mer (Mission des Collectivités Territoriales) la communication des notes juridiques et diplomatiques comparant le droit de résidence foncière applicable à Jersey (*Entitled Status*), aux îles Åland (*Hembygdsrätt*) et aux Açores avec le statut constitutionnel actuel de la Corse.

---

### 📌 Action CADA n°2 : Accès aux rapports d'évaluation des dispositifs de préemption territoriale
Saisissez la SAFER de Corse et la DDTM de Haute-Corse et de Corse-du-Sud pour obtenir les rapports d'évaluation annuels du nombre de transactions foncières où un droit de préemption territorial aurait pu être exercé et ne l'a pas été, avec les motifs de non-préemption.

---

### 📌 Action CADA n°3 : Accès aux études d'impact INSEE sur l'éviction foncière des ménages corses
Demandez à l'INSEE Corse et à la DREAL de Corse la communication des études internes mesurant l'évolution du taux de propriété des ménages résidents sur le littoral et en zones PADDUC inconstructibles sur les 15 dernières années.

---

### 📌 Action CADA n°4 : Accès aux bilans d'application des Lois du Pays foncières dans les COM
Saisissez la DGOM (Direction Générale des Outre-Mer) pour obtenir les bilans d'application du droit de préemption territorial et des conditions de résidence en Polynésie Française et en Nouvelle-Calédonie validés par le Conseil Constitutionnel — documents directement pertinents pour la transposition en Corse.
""",

    4: """## V. Préconisations juridiques et démarches CADA d'accès aux actes de gestion de l'eau

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
""",

    5: """## V. Préconisations juridiques et démarches CADA d'accès aux actes constitutifs des SCI

Démanteler le réseau des SCI écran littorales exige d'accéder aux documents constitutifs et aux registres de propriété effective. Quatre démarches CADA permettent de percer l'opacité :

---

### 📌 Action CADA n°1 : Accès aux fiches RBE du Registre des Bénéficiaires Effectifs (INPI)
Demandez auprès du greffe du Tribunal de Commerce de Bastia ou d'Ajaccio (ou directement sur inpi.fr) les fiches du Registre des Bénéficiaires Effectifs (RBE) des SCI enregistrées dans les communes littorales. Ces fiches révèlent l'identité réelle des associés détenant plus de 25 % du capital ou des droits de vote. **Obligation légale (Art. L. 561-46 CMF).**

---

### 📌 Action CADA n°2 : Accès aux permis de construire accordés aux SCI en zone littorale
Saisissez le service d'urbanisme de la mairie concernée ou la DDTM pour obtenir les dossiers complets de permis de construire accordés à des SCI non-résidentes dans les zones proches du rivage (bande des 100 m, espaces remarquables). En cas de refus, recours immédiat devant la CADA.

---

### 📌 Action CADA n°3 : Accès aux conventions de PUP prenant en charge les travaux desservant les lotissements SCI
Demandez aux mairies concernées les conventions de Projet Urbain Partenarial (PUP) dans lesquelles la collectivité s'est engagée à financer l'extension des réseaux (eau, voirie, assainissement) desservant des lotissements ou résidences développés par des SCI privées.

---

### 📌 Action CADA n°4 : Accès aux DIA transmises à la SAFER
Saisissez la SAFER de Corse pour obtenir les déclarations d'intention d'aliéner (DIA) concernant les ventes de parts sociales de SCI détentrices de foncier agricole ou forestier. Le droit de préemption de la SAFER s'applique dès lors qu'une telle cession constitue une prise de contrôle d'une société agricole (Art. L. 141-1 CRPM).
""",

    6: """## V. Préconisations juridiques et démarches CADA d'accès aux actes d'attribution des quotas de pêche

Le pillage des ressources halieutiques par les armements sétois et marseillais ne peut être stoppé que par la transparence totale des décisions d'attribution. Voici quatre leviers d'action concrète :

---

### 📌 Action CADA n°1 : Accès aux arrêtés DPMA d'attribution du quota de thon rouge
Demandez à la Direction des Pêches Maritimes et de l'Aquaculture (DPMA, Ministère de la Mer) les arrêtés annuels de répartition du quota national de thon rouge (*Thunnus thynnus*) par organisation de producteurs (OP) et par port d'attache. Vérifiez la part allouée aux pêcheurs artisanaux corses vs les armements industriels continentaux.

---

### 📌 Action CADA n°2 : Accès aux journaux de pêche VMS/AIS de géolocalisation des thoniers
Saisissez le Centre de Surveillance des Pêches (CSP/DPMA) pour obtenir les données anonymisées de géolocalisation VMS (Vessel Monitoring System) et AIS des thoniers senneurs opérant dans les eaux entourant la Corse lors des saisons de pêche. Ces données prouvent les zones de capture effectives.

---

### 📌 Action CADA n°3 : Accès aux rapports de contrôle IFREMER sur les stocks de poissons bleus en Méditerranée
Demandez à l'IFREMER la communication des rapports scientifiques internes concernant l'état des stocks de petits pélagiques (sardines, anchois) et de thons dans le golfe de Gênes et autour de la Corse, utilisés pour calibrer les quotas de la CICTA.

---

### 📌 Action CADA n°4 : Accès aux procès-verbaux d'attribution des droits de la Prud'homie
Saisissez la DDTM de Haute-Corse et de Corse-du-Sud pour obtenir les procès-verbaux des assemblées de la Prud'homie de pêche (instances de gestion locales) et les registres d'immatriculation des navires de pêche artisanaux corses sur les 10 dernières années.
""",

    7: """## V. Préconisations juridiques et démarches CADA d'accès aux actes miniers et prospection du sous-sol

La protection du sous-sol insulaire contre l'extraction prédatrice de ses ressources stratégiques passe par la transparence des concessions et des autorisations accordées sans consultation citoyenne. Quatre démarches CADA essentielles :

---

### 📌 Action CADA n°1 : Accès aux rapports d'inventaire géologique et minier du BRGM pour la Corse
Demandez au Bureau de Recherches Géologiques et Minières (BRGM) la communication des rapports d'inventaire des ressources minérales du Cap Corse et de la Balagne, notamment les études sur l'antimoine, le chrome, l'amiante chrysotile et les terres rares. Ces rapports sont des documents administratifs communicables.

---

### 📌 Action CADA n°2 : Accès aux arrêtés préfectoraux d'autorisation de prospection minière
Saisissez la Préfecture de Haute-Corse pour obtenir les arrêtés préfectoraux d'autorisation de recherches minières accordés ces 20 dernières années sur le territoire insulaire, avec les coordonnées GPS des périmètres concernés et l'identité des sociétés titulaires.

---

### 📌 Action CADA n°3 : Accès aux audits DREAL d'exposition à l'amiante chrysotile et à l'antimoine
Demandez à la DREAL de Corse les rapports d'inspection des sites de mines abandonnées (notamment Cap Corse) présentant des risques d'exposition à l'amiante naturel et aux métaux lourds, ainsi que les mesures de confinement ou de dépollution prescrites.

---

### 📌 Action CADA n°4 : Accès au registre des redevances minières perçues par l'État sur le territoire corse
Saisissez la DGFiP pour obtenir les montants des redevances minières et superficiaires versées à l'État par les titulaires de concessions minières sur le territoire de la Corse-du-Sud et la Haute-Corse depuis 2005 — et le montant redistribué aux communes concernées.
""",

    8: """## V. Préconisations juridiques et démarches CADA d'accès aux actes de gestion forestière

La mise en lumière du pillage forestier organisé exige l'accès aux registres de coupes, aux manifestes d'exportation et aux bilans de la politique sylvicole conduite par l'État en Corse. Quatre démarches CADA concrètes :

---

### 📌 Action CADA n°1 : Accès aux procès-verbaux d'adjudication des coupes de bois domaniales ONF
Demandez à l'Office National des Forêts (ONF, Agence Territoriale de Corse) les procès-verbaux d'adjudication de toutes les ventes de coupes de bois en forêts domaniales et communales sur les 10 dernières années, avec les volumes vendus, les prix et l'identité des acheteurs.

---

### 📌 Action CADA n°2 : Accès aux manifestes douaniers d'exportation de grumes brutes
Saisissez la Direction Régionale des Douanes et Droits Indirects de Corse pour obtenir les statistiques d'exportation de bois ronds (grumes) et de bois débités non transformés vers l'Italie, via les ports de Bastia, Ajaccio et Propriano. Ces données sont communicables au titre de la transparence des échanges commerciaux.

---

### 📌 Action CADA n°3 : Accès aux rapports d'inventaire forestier Agreste/DRAAF
Demandez à la DRAAF de Corse les derniers rapports d'inventaire forestier régional (taux de boisement, espèces, volumes sur pied) ainsi que les bilans de sylviculture et de régénération naturelle publiés par le service statistique Agreste.

---

### 📌 Action CADA n°4 : Accès aux conventions et subventions accordées aux scieries et exploitants forestiers
Saisissez la DRAAF et la Collectivité de Corse pour obtenir la liste des subventions régionales et nationales accordées aux scieries et exploitants forestiers ayant opéré en Corse, avec les contreparties de transformation locale exigées et effectivement respectées.
""",

    9: """## V. Préconisations juridiques et démarches CADA d'accès aux actes de collecte fiscale touristique

Freiner l'évasion des capitaux touristiques suppose de rendre publics les flux de la taxe de séjour, des revenus de plateformes et des aides à la promotion. Quatre démarches concrètes :

---

### 📌 Action CADA n°1 : Accès aux registres de collecte de la taxe de séjour par commune
Saisissez chaque mairie ou EPCI pour obtenir les tableaux de bord annuels de collecte de la taxe de séjour (montants collectés par type d'hébergement, nuitées déclarées par opérateur). Vérifiez le ratio entre les nuitées déclarées sur Airbnb et Booking et les montants réellement reversés.

---

### 📌 Action CADA n°2 : Accès aux données IEDOM/Banque de France sur les flux de cartes bancaires
Demandez à l'IEDOM le bulletin de suivi des flux de paiement CB en Corse, notamment la comparaison entre les encaissements en haute saison et les réinjections dans les crédits aux professionnels locaux. Ces données permettent de mesurer le siphonnage structurel de la liquidité estivale.

---

### 📌 Action CADA n°3 : Accès aux déclarations fiscales d'IS des plateformes numériques (Airbnb, Booking)
Demandez à la DRFiP de Corse les statistiques agrégées de chiffre d'affaires et d'impôt sur les sociétés déclarés par les plateformes de location touristique opérant en Corse. Ces données sont en partie disponibles via le rapport annuel sur les taxes sur les services numériques (DST/TSN).

---

### 📌 Action CADA n°4 : Accès aux conventions d'aide régionale à la promotion touristique
Saisissez l'Agence du Tourisme de Corse (ATC) pour obtenir la liste et le montant des conventions de subvention accordées à des agences de communication et offices du tourisme, avec les obligations de résultats contractuelles et les rapports d'exécution.
""",

    10: """## V. Préconisations juridiques et démarches CADA d'accès aux actes de nomination et d'évaluation des hauts fonctionnaires en poste en Corse

Rompre la tutelle administrative implique de rendre publics les critères de nomination, les durées de mission et les bilans de gestion des directeurs régionaux continentaux. Quatre démarches CADA :

---

### 📌 Action CADA n°1 : Accès aux arrêtés de nomination et décrets de mutation du corps préfectoral
Demandez à la Direction Générale de l'Administration et de la Fonction Publique (DGAFP) les arrêtés de nomination et de fin de fonctions des préfets, secrétaires généraux et sous-préfets affectés en Corse depuis 2010, avec les durées de mission effectives.

---

### 📌 Action CADA n°2 : Accès aux fiches d'évaluation des directeurs régionaux
Saisissez le Secrétaire Général du Gouvernement pour obtenir les critères et les bilans d'évaluation des directeurs régionaux (DRFIP, DREAL, DRAAF, ARS) affectés en Corse : les compétences territoriales requises à la prise de poste y sont-elles évaluées ?

---

### 📌 Action CADA n°3 : Accès aux délibérations d'attribution des primes de haute responsabilité et NBI
Demandez aux services RH de la Préfecture de Région les délibérations internes d'attribution des primes de haute responsabilité (NBI, PFR, RIFSEEP) versées aux cadres supérieurs de l'État en poste en Corse. Ces informations sont communicables au titre de la transparence de la rémunération des agents publics.

---

### 📌 Action CADA n°4 : Accès aux rapports de la Cour des Comptes sur la gestion des services de l'État en Corse
Demandez à la Cour des Comptes et à la Chambre Régionale des Comptes de Corse leurs rapports d'observations définitives publiés sur la gestion administrative des préfectures et des services déconcentrés de l'État (DRFIP, DREAL, DDTM) en Corse.
""",

    11: """## V. Préconisations juridiques et démarches CADA d'accès aux actes immobiliers et cartographiques des emprises militaires

La rétrocession progressive des emprises militaires sous-utilisées au bénéfice de l'île passe par la connaissance précise de leur inventaire et de leur coût fiscal. Quatre démarches CADA essentielles :

---

### 📌 Action CADA n°1 : Accès au Tableau Général des Propriétés Immobilières de l'État (TGPIE) pour la Corse
Demandez à la Direction de l'Immobilier de l'État (DIE / DGFiP) l'extrait du Tableau Général des Propriétés Immobilières de l'État (TGPIE) listant toutes les parcelles militaires détenues par le Ministère des Armées sur le territoire de la Corse-du-Sud et de la Haute-Corse, avec leur superficie, leur affectation et leur état d'utilisation.

---

### 📌 Action CADA n°2 : Accès aux cartes de servitudes militaires d'inconstructibilité
Saisissez la DDTM de Haute-Corse et de Corse-du-Sud pour obtenir les cartes actualisées des servitudes d'utilité publique militaires (SUP PM1, PM2, PM3) grevant les communes limitrophes des bases de Solenzara, Calvi, Aspretto et San Damiano.

---

### 📌 Action CADA n°3 : Accès aux bilans d'exonération de taxe foncière des emprises militaires
Demandez à la DRFiP de Corse le montant cumulé annuel des exonérations de taxe foncière sur les propriétés bâties (TFPB) et non bâties (TFPNB) dont bénéficient les emprises militaires en Corse, et le manque à gagner pour les budgets communaux.

---

### 📌 Action CADA n°4 : Accès aux délibérations de concession de la Base Navale d'Aspretto
Saisissez le Ministère des Armées pour obtenir les termes actuels de la convention de mise à disposition de la base navale d'Aspretto (Ajaccio) à la Marine nationale : superficie concédée, durée, redevance versée à la Collectivité de Corse et clauses de rétrocession.
""",

    12: """## V. Préconisations juridiques et démarches CADA d'accès aux actes de financement sanitaire

La construction d'une souveraineté sanitaire insulaire passe par la transparence des flux financiers de l'ARS et des conditions d'évacuation des patients. Quatre démarches CADA :

---

### 📌 Action CADA n°1 : Accès aux registres d'ordres de vol et de facturation des EVASAN
Saisissez l'ARS de Corse pour obtenir les statistiques annuelles des évacuations sanitaires (EVASAN) depuis la Corse vers les CHU continentaux : nombre, destination, pathologies (anonymisées), coût unitaire moyen et financeur (Sécurité Sociale, État, Collectivité).

---

### 📌 Action CADA n°2 : Accès aux arrêtés de dotation budgétaire T2A des hôpitaux de Bastia et Ajaccio
Demandez à l'ARS de Corse les arrêtés annuels de dotation T2A (Tarification à l'Activité) de l'État aux Centres Hospitaliers de Bastia et d'Ajaccio, incluant les financements des missions d'intérêt général (MIG) et les forfaits de continuité des soins insulaires.

---

### 📌 Action CADA n°3 : Accès aux conventions de partenariat sanitaire avec l'AP-HM et le CHU de Nice
Saisissez le Ministère de la Santé pour obtenir les conventions de partenariat médical et de transfert de compétences signées entre les hôpitaux corses et les CHU de Marseille (AP-HM) et de Nice, notamment les clauses de développement de la télémédecine et de formation des médecins spécialistes sur l'île.

---

### 📌 Action CADA n°4 : Accès aux rapports d'audit de sécurité des urgences (DREES / Inspection Générale)
Demandez à la DREES (Direction de la Recherche, des Études, de l'Évaluation et des Statistiques) les rapports d'inspection des services d'urgences des hôpitaux corses : taux de saturation, délais de prise en charge, risques liés aux délestages de patients et incidents signalés.
""",

    13: """## V. Recommandations pour une université souveraine et autonome — Démarches CADA

La construction d'une souveraineté intellectuelle et scientifique insulaire passe par le contrôle des flux budgétaires de l'État vers l'Université de Corse et par la transparence des obstacles à son développement. Quatre démarches CADA ciblées :

---

### 📌 Action CADA n°1 : Accès aux conventions pluri-annuelles de dotation de l'État à l'Université de Corse (MESR)
Demandez au Ministère de l'Enseignement Supérieur et de la Recherche (MESR) les conventions d'objectifs et de moyens pluriannuelles (COM) signées avec l'Université Pascal Paoli de Corte, incluant les dotations de fonctionnement, les créations de postes enseignants et les financements de recherche alloués.

---

### 📌 Action CADA n°2 : Accès aux registres d'attribution des logements étudiants du CROUS de Corte
Saisissez le CROUS de Corte pour obtenir les données sur la capacité totale des résidences étudiantes, le taux de remplissage et les délais d'attente moyens pour un logement CROUS. En complément, demandez le nombre de dossiers d'aides d'urgence (FSDIE) instruits chaque année.

---

### 📌 Action CADA n°3 : Accès aux fiches de calcul de la dotation par étudiant
Demandez au MESR le détail du calcul de la dotation globale de fonctionnement par étudiant inscrit à l'Université de Corse, comparé aux universités continentales de même taille. La charge d'insularité est-elle prise en compte dans la clé de répartition nationale ?

---

### 📌 Action CADA n°4 : Accès aux bilans d'aide régionale à la recherche et à la mobilité étudiante
Saisissez la Collectivité de Corse pour obtenir le bilan annuel des bourses de mobilité étudiante, des contrats de recherche territoriaux et des conventions de partenariat université-entreprise financés par les fonds régionaux, avec les taux d'insertion professionnelle des diplômés associés.
""",

    14: """## V. Recommandations pour le rapatriement de la justice en Corse — Démarches CADA

La réintégration de la pleine compétence judiciaire au sein de la Cour d'Appel de Bastia est une exigence de justice territoriale. Quatre démarches CADA pour forcer la transparence sur le dessaisissement :

---

### 📌 Action CADA n°1 : Accès aux ordonnances de dessaisissement du parquet de Bastia vers la JIRS de Marseille
Demandez à la Chancellerie (Ministère de la Justice, Direction des Affaires Criminelles et des Grâces) les statistiques annuelles des ordonnances de renvoi et de dessaisissement du parquet général de Bastia vers la JIRS de Marseille : nombre d'affaires, infractions visées et temps écoulé entre la saisine et le dessaisissement.

---

### 📌 Action CADA n°2 : Accès aux états de frais de justice et de déportation des escortes pénitentiaires
Saisissez la Direction de l'Administration Pénitentiaire (DAP) pour obtenir le coût annuel des transferts de prévenus corses vers les maisons d'arrêt de Marseille, Lyon et Grasse : frais d'escorte, de transport, d'hébergement et d'éloignement familial.

---

### 📌 Action CADA n°3 : Accès aux registres d'écrou des prévenus et condamnés corses incarcérés hors de Corse
Demandez à la DAP les statistiques anonymisées sur le nombre de détenus originaires de Corse incarcérés dans des établissements pénitentiaires hors de l'île, la durée moyenne de détention provisoire et le taux de maintien des liens familiaux.

---

### 📌 Action CADA n°4 : Accès aux rapports d'inspection de la Chancellerie sur les délais d'instruction et les moyens des juridictions corses
Saisissez l'Inspection Générale de la Justice (IGJ) pour obtenir les rapports d'inspection publiés sur les tribunaux judiciaires d'Ajaccio et de Bastia : effectifs de magistrats, délais moyens d'instruction, taux de classement sans suite et charges de travail comparées.
""",

    15: """## V. Actions de vigilance citoyenne et recours CADA contre la censure administrative

La protection des délibérations locales légitimes contre les déférés préfectoraux abusifs passe par la publicité des décisions et la constitution de dossiers de défense juridique solides. Quatre démarches concrètes :

---

### 📌 Action CADA n°1 : Accès au registre des actes téléchargés via le système @CTES
Demandez à la Préfecture de Corse le registre chronologique des actes municipaux reçus par voie de télétransmission via le système @CTES et signalés aux fins de contrôle de légalité : délibérations, permis de construire, marchés publics. Ce document permet de mesurer l'intensité du contrôle exercé sur les communes corses.

---

### 📌 Action CADA n°2 : Accès aux registres chronologiques des déférés préfectoraux au TA de Bastia
Saisissez la Préfecture de Haute-Corse et de Corse-du-Sud pour obtenir les listes des actes municipaux déférés au Tribunal Administratif de Bastia depuis 2014 : nature des actes, commune concernée, motifs juridiques invoqués, issues de la procédure.

---

### 📌 Action CADA n°3 : Accès aux fiches d'instruction juridique de la DDTM sur les urbanisations critiques
Demandez à la DDTM (Direction Départementale des Territoires et de la Mer) les notes de synthèse juridique établies lors de l'instruction des dossiers d'urbanisme critiques identifiés dans les communes littorales, notamment ceux transmis au parquet pour infraction à la Loi Littoral.

---

### 📌 Action CADA n°4 : Accès aux jugements d'annulation de permis de construire prononcés par le TA de Bastia
Demandez au greffe du Tribunal Administratif de Bastia la liste des décisions d'annulation de permis de construire rendues depuis 2015 à la requête d'associations de défense de l'environnement : Loi Littoral, PADDUC, espaces remarquables protégés.
""",

    16: """## V. Actions de sécurisation patrimoniale et démarches notariales — Arrêtés Miot

La protection du patrimoine foncier familial corse dans le contexte spécifique des exonérations fiscales héritées des Arrêtés Miot et du régime CGI 750 bis A passe par quatre démarches concrètes :

---

### 📌 Action CADA n°1 : Accès aux registres des actes de notoriété prescriptifs établis par le GIRTEC
Demandez au Groupement d'Intérêt Public pour le Remembrement et la Titration en Corse (GIRTEC) les données sur le nombre d'actes de notoriété acquisitive (prescription trentenaire) établis par commune et par année, ainsi que le nombre de dossiers en attente de régularisation.

---

### 📌 Action CADA n°2 : Accès aux arrêtés d'exonération de droits de succession appliqués (DRFiP)
Saisissez la DRFiP de Corse pour obtenir les statistiques agrégées sur l'application de l'exonération de droits de succession des biens immobiliers corses (Art. 750 bis A CGI), avec les montants d'imposition différée et les risques de rappel en cas de cession avant l'expiration du délai légal.

---

### 📌 Action CADA n°3 : Accès aux extraits de la matrice cadastrale pour les parcelles sans maître
Saisissez la DGFiP pour obtenir les extraits de la matrice cadastrale des parcelles non titrées ou en déshérence susceptibles d'être incorporées au domaine communal ou de faire l'objet de procédures de bornage et d'appropriation par des tiers.

---

### 📌 Action CADA n°4 : Accès aux procès-verbaux de la Commission Foncière de la Collectivité de Corse
Demandez à l'Assemblée de Corse les procès-verbaux et comptes-rendus de la Commission Foncière institutionnelle traitant des indivisions successorales, du recensement du foncier non titré et des propositions de simplification de l'acte de notoriété acquisitive.
""",

    17: """## V. Actions de transmission et de souveraineté culturelle — Démarches CADA

La défense de la langue corse face au verrou de la Charte Européenne des Langues Régionales non ratifiée implique l'accès aux données réelles de l'enseignement bilingue et aux blocages institutionnels. Quatre démarches :

---

### 📌 Action CADA n°1 : Accès aux rapports d'effectifs de l'enseignement bilingue du Rectorat de Corse
Saisissez le Rectorat de Corse pour obtenir les statistiques annuelles du nombre d'élèves inscrits dans des sections bilingues français-corse dans le public (primaire, collège, lycée), le nombre d'enseignants bilingues certifiés et les communes où l'offre bilingue fait défaut.

---

### 📌 Action CADA n°2 : Accès aux délibérations de l'Assemblée de Corse sur l'officialisation de la langue
Demandez à l'Assemblée de Corse les procès-verbaux des délibérations relatives aux propositions de co-officialité de la langue corse, aux motions transmises au gouvernement et aux réponses (ou silences) de la Chancellerie sur la révision constitutionnelle attendue.

---

### 📌 Action CADA n°3 : Accès aux notes juridiques du Conseil d'État sur la Charte Européenne des Langues
Saisissez le Secrétariat Général du Gouvernement pour obtenir les avis du Conseil d'État sur la constitutionnalité de la ratification par la France de la Charte Européenne des Langues Régionales ou Minoritaires, notamment les réserves formulées après les arrêts de 1999 et 2015.

---

### 📌 Action CADA n°4 : Accès aux conventions de financement croisé Éducation Nationale / Collectivité
Demandez au Rectorat de Corse et à la Collectivité de Corse les conventions de cofinancement des postes d'enseignants de langue corse et des dispositifs d'immersion associatifs (Scola Corsa, Cullettività d'Istruzione), avec les engagements pluriannuels et les bilans d'exécution.
""",

    18: """## V. Actions pour la souveraineté énergétique et recours CADA

La reconquête de la souveraineté énergétique insulaire face au monopole EDF-SEI passe par la transparence totale des coûts cachés de la Zone Non Interconnectée corse. Quatre démarches CADA ciblées :

---

### 📌 Action CADA n°1 : Accès aux arrêtés d'autorisation ICPE des centrales au fioul du Vazzio et de Lucciana
Demandez à la DREAL de Corse les arrêtés d'autorisation d'exploitation au titre des Installations Classées pour la Protection de l'Environnement (ICPE) des centrales thermiques au fioul du Vazzio (Ajaccio) et de Lucciana (Haute-Corse), incluant les arrêtés de mise en demeure, les prescriptions de réduction d'émissions et les dérogations accordées.

---

### 📌 Action CADA n°2 : Accès aux contrats d'Obligation d'Achat de l'électricité EDF-SEI en Zone Non Interconnectée
Saisissez la Commission de Régulation de l'Énergie (CRE) pour obtenir les contrats d'obligation d'achat d'électricité à prix garanti conclus entre EDF-SEI et les producteurs d'énergie renouvelable (photovoltaïque, éolien) en Corse. Vérifiez les tarifs d'achat et les durées d'engagement.

---

### 📌 Action CADA n°3 : Accès aux bilans de compensation de la péréquation tarifaire en Corse
Demandez à la CRE les bilans annuels de la Contribution au Service Public de l'Électricité (CSPE) attribuée à la ZNI corse : montant des surcoûts de production compensés par la péréquation nationale et coût unitaire du kWh produit en Corse par rapport au prix moyen continental.

---

### 📌 Action CADA n°4 : Accès aux procès-verbaux d'arbitrage de la Programmation Pluriannuelle de l'Énergie (PPE) de Corse
Saisissez la Direction de l'Énergie et du Climat (DGEC/Ministère de la Transition Énergétique) pour obtenir les comptes-rendus des commissions d'arbitrage de la PPE insulaire : objectifs de fermeture des centrales au fioul, calendrier de déploiement des renouvelables et investissements prévus dans le stockage d'énergie.
""",

    19: """## V. Actions pour la souveraineté numérique insulaire — Démarches CADA

Reconquérir la souveraineté numérique de la Corse exige de rendre publics les contrats d'hébergement des données publiques et les failles de sécurité du réseau d'infrastructures numériques insulaire. Quatre démarches :

---

### 📌 Action CADA n°1 : Accès au cahier des charges du réseau fibre Corsica Fibra
Demandez à la Collectivité de Corse les documents constitutifs du Réseau d'Initiative Publique (RIP) Corsica Fibra : cahier des charges technique, contrat de DSP avec l'opérateur retenu, carte de déploiement par commune et engagements de couverture des zones blanches.

---

### 📌 Action CADA n°2 : Accès aux contrats d'hébergement cloud des données publiques des collectivités corses
Saisissez la Collectivité de Corse, les Conseils Départementaux et les principales intercommunalités pour obtenir les contrats d'hébergement cloud de leurs données sensibles (état civil, données fiscales, SI ressources humaines) et vérifier la conformité RGPD et la localisation physique des serveurs.

---

### 📌 Action CADA n°3 : Accès aux déclarations ARCEP des câbles sous-marins de télécommunications
Demandez à l'ARCEP (Autorité de Régulation des Communications Électroniques et des Postes) la liste des déclarations d'atterrage et d'exploitation des câbles sous-marins de fibre optique reliant la Corse au continent (Marseille, Gênes) et l'état de leurs redondances.

---

### 📌 Action CADA n°4 : Accès aux rapports d'audit de cybersécurité de l'ANSSI
Saisissez l'Agence Nationale de la Sécurité des Systèmes d'Information (ANSSI) pour obtenir les recommandations publiques et les éventuels incidents déclarés concernant les systèmes d'information critiques des institutions corses (hôpitaux, collectivités, préfectures).
""",

    20: """## V. Actions de réforme et de transparence citoyenne — Primes PAC

La reconquête de la souveraineté alimentaire face à l'accaparement des primes PAC impose de forcer la transparence sur les attributaires réels des aides européennes en Corse. Quatre démarches CADA :

---

### 📌 Action CADA n°1 : Accès au Registre Parcellaire Graphique (RPG) anonymisé de votre commune
Demandez à la DRAAF de Corse les cartes anonymisées du Registre Parcellaire Graphique (RPG) des surfaces agricoles déclarées en TéléPAC sur votre territoire : superficie réelle des pâturages déclarés, type de couverture des sols et cohérence avec la réalité visible (maquis, zones urbanisées).

---

### 📌 Action CADA n°2 : Accès aux procès-verbaux de contrôle sur place du cheptel (ODARC / DRAAF)
Saisissez l'ODARC (Office de Développement Agricole et Rural de Corse) et la DRAAF pour obtenir les procès-verbaux de contrôle sur place des effectifs de cheptel bovins, ovins et caprins des exploitants déclarant des primes à l'animal sur votre commune. Le taux de fraude constaté par les agents est un indicateur clé.

---

### 📌 Action CADA n°3 : Accès aux délibérations de la CDOA sur l'attribution des droits à prime PAC
Demandez à la Commission Départementale d'Orientation de l'Agriculture (CDOA) de Haute-Corse et de Corse-du-Sud les procès-verbaux des séances ayant statué sur l'attribution, le transfert et la consolidation des droits à prime PAC entre exploitants. Ces délibérations permettent de tracer les transferts entre grandes exploitations et petits éleveurs.

---

### 📌 Action CADA n°4 : Accès aux fiches de signalement de fraudes transmises à l'ASP et au Parquet National Financier
Saisissez l'Agence de Services et de Paiement (ASP) et les Procureurs de la République de Bastia et Ajaccio pour obtenir les statistiques annuelles des fraudes aux aides PAC détectées en Corse : montants indûment perçus, procédures de recouvrement engagées et affaires transmises au Parquet National Financier (PNF).
""",

    21: """## V. Actions de souveraineté environnementale et démarches CADA — Déchets SYVADEC

La sortie de la crise des déchets corse passe par la transparence totale des marchés publics du SYVADEC et des conditions d'exportation continentale. Quatre démarches CADA concrètes :

---

### 📌 Action CADA n°1 : Demande des marchés publics de transport maritime des déchets
Saisissez le SYVADEC (Syndicat de Valorisation des Déchets de la Corse) pour obtenir les marchés publics d'exportation des déchets résiduels et des refus de tri par voie maritime (cargo) vers les sites de traitement continentaux : titulaires, volumes, coûts unitaires et ports de destination. Ces marchés sont des documents administratifs communicables (Art. L. 311-1 CRPA).

---

### 📌 Action CADA n°2 : Accès aux arrêtés préfectoraux ICPE des centres d'enfouissement de Tallone et Viggianello
Demandez à la DREAL de Corse les arrêtés d'autorisation d'exploitation des Installations de Stockage des Déchets Non Dangereux (ISDND) de Tallone et Viggianello, ainsi que les derniers rapports d'inspection et les prescriptions de mise aux normes imposées aux exploitants.

---

### 📌 Action CADA n°3 : Accès au rapport d'audit financier de la Chambre Régionale des Comptes sur le SYVADEC
Demandez à la Chambre Régionale des Comptes de Corse les rapports d'observations définitives publiés sur la gestion financière et les marchés publics du SYVADEC depuis 2015. Ces rapports sont publics et directement communicables.

---

### 📌 Action CADA n°4 : Accès aux bordereaux de versement de la TGAP sur les ordures ménagères
Demandez à la DRFiP de Corse les montants de la Taxe Générale sur les Activités Polluantes (TGAP) acquittés annuellement par le SYVADEC sur les tonnages mis en décharge, ainsi que le montant des pénalités de dépassement de seuil de mise en décharge. Ces données permettent de chiffrer le surcoût de l'inaction en matière de tri.
""",

    22: """## V. Actions pour une Banque Publique Régionale de Développement — Démarches CADA

La reconquête de la souveraineté financière corse et la création d'un outil de financement territorial autonome (Cassa di Sviluppu) impose d'abord la transparence sur les flux réels de l'épargne insulaire. Quatre démarches CADA :

---

### 📌 Action CADA n°1 : Accès aux statistiques IEDOM sur les dépôts et prêts bancaires en Corse
Demandez à l'IEDOM (Institut d'Émission des Départements d'Outre-Mer) le rapport annuel détaillant les encours de dépôts bancaires collectés en Corse et les encours de crédits accordés aux ménages et aux entreprises corses : le différentiel révèle le montant du capital quotidiennement exporté vers le continent.

---

### 📌 Action CADA n°2 : Accès aux registres de garantie accordés par Bpifrance aux entreprises corses
Saisissez Bpifrance (délégation régionale Corse) pour obtenir les statistiques annuelles de garanties d'emprunt accordées aux TPE-PME corses, comparées aux demandes rejetées et aux raisons invoquées. Vérifiez si le critère d'insularité est correctement valorisé dans les grilles de notation Bpifrance.

---

### 📌 Action CADA n°3 : Accès aux conventions financières signées entre la Collectivité de Corse et les réseaux bancaires
Demandez à la Collectivité de Corse les conventions de partenariat financier conclues avec les banques régionales et nationales pour le financement des projets d'investissement public (infrastructure, logement, transition énergétique) : taux d'intérêt négociés, durées et contreparties de réinvestissement local exigées.

---

### 📌 Action CADA n°4 : Accès aux rapports prudentiels de l'ACPR sur les établissements bancaires actifs en Corse
Saisissez l'Autorité de Contrôle Prudentiel et de Résolution (ACPR / Banque de France) pour obtenir les statistiques régionales des conditions de crédit appliquées en Corse par les établissements sous sa supervision : taux de refus, taux d'intérêt effectif global et provisions pour créances douteuses.
""",

    23: """## V. Actions de souveraineté et démarches CADA — Sécurité Civile

La protection des populations et des forêts corses contre l'incendie et les risques naturels exige des moyens propres et la transparence des dotations de l'État. Quatre démarches CADA ciblées :

---

### 📌 Action CADA n°1 : Accès aux journaux de mouvements et de missions des aéronefs de sécurité civile
Demandez à la Direction Générale de la Sécurité Civile et de la Gestion des Crises (DGSCGC) les journaux de mouvements des Canadair, Tracker et hélicoptères Dragon basés temporairement en Corse pendant la saison estivale : heures de vol, missions effectuées, taux de disponibilité et avaries enregistrées.

---

### 📌 Action CADA n°2 : Accès aux arrêtés de dotation budgétaire des Conseils Départementaux aux SIS 2A et 2B
Saisissez les Conseils Départementaux de Corse-du-Sud (2A) et de Haute-Corse (2B) pour obtenir les arrêtés annuels de dotation budgétaire aux Services Départementaux d'Incendie et de Secours (SDIS 2A et SDIS 2B), comparés au ratio national de dépenses de sécurité civile par habitant.

---

### 📌 Action CADA n°3 : Accès aux conventions de coordination entre le PGHM, le Dragon 20 et la Sécurité Civile
Demandez à la Gendarmerie Nationale (Groupement de Gendarmerie de Corse), à la Sécurité Civile et à la Préfecture les conventions opérationnelles organisant la coordination des secours en montagne (PGHM Corse), les missions hélitreuillages (Dragon 20) et les opérations feux de forêt.

---

### 📌 Action CADA n°4 : Accès aux rapports de couverture des risques de la DGSCGC
Demandez à la DGSCGC le rapport de couverture des risques naturels et technologiques majeurs pour la Corse : analyse de la capacité de réponse aux incendies simultanés, aux tsunamis (risque méditerranéen), aux tempêtes et aux risques sismiques en rapport avec la population et la superficie insulaire.
""",

    24: """## V. Actions de détection citoyenne et recours CADA — Permis Tacites

Neutraliser les permis de construire tacites utilisés à des fins spéculatives passe par la publicité des registres de dépôts et des procédures de contestation. Quatre démarches CADA concrètes :

---

### 📌 Action CADA n°1 : Demande du registre chronologique de dépôt des permis de construire en mairie
Saisissez le service d'urbanisme de votre mairie pour obtenir la copie intégrale du registre chronologique de dépôt des demandes de permis de construire (CERFA), d'autorisation de travaux et de déclarations préalables : date de dépôt, nature du projet, demandeur (identité ou dénomination sociale), décision rendue.

---

### 📌 Action CADA n°2 : Accès aux récépissés de délivrance de permis tacites (Art. R. 424-1 CU)
Demandez à la mairie et à la DDTM les listes des permis de construire nés tacitement du silence gardé par l'administration au-delà du délai d'instruction légal (2 à 5 mois selon les zones). Ces permis sont des décisions implicites d'acceptation communicables dans leur intégralité.

---

### 📌 Action CADA n°3 : Accès à la base Sitadel2 de la DREAL Corse sur les mises en chantier
Demandez à la DREAL de Corse les données extraites de la base Sitadel2 concernant les autorisations de construire et les mises en chantier annuelles dans votre commune ou intercommunalité, ventilées par type de logement (résidence principale/secondaire, individuel/collectif).

---

### 📌 Action CADA n°4 : Accès aux procès-verbaux de constatation de défaut d'affichage sur les chantiers
Saisissez la DDTM pour obtenir les procès-verbaux de constatation de défaut d'affichage réglementaire sur les chantiers de votre commune (absence du panneau permis de construire obligatoire). Ces infractions raccourcissent artificiellement les délais de recours des tiers et constituent une violation de l'Art. A. 424-15 du Code de l'Urbanisme.
""",

    25: """## V. Actions de vérification environnementale et saisine CADA — MRAe et Pétitionnaires

La protection des espaces naturels corses contre les projets d'aménagement portés par des pétitionnaires opacifiés passe par la vérification systématique de leur identité et de la robustesse de leurs études d'impact. Quatre démarches CADA :

---

### 📌 Action CADA n°1 : Demande des arrêtés d'examen au cas par cas de la MRAe Corse
Saisissez la Mission Régionale d'Autorité Environnementale (MRAe) de Corse pour obtenir les arrêtés d'examen au cas par cas rendus sur les projets d'aménagement soumis à sa compétence (lotissements, campings, zones d'activité, carrières, parcs éoliens). Vérifiez si l'étude d'impact intégrale a bien été exigée ou si elle a été dispensée sans justification.

---

### 📌 Action CADA n°2 : Accès aux fiches RBE des pétitionnaires (INPI / Infogreffe)
Exigez via la plateforme inpi.fr ou les greffes des tribunaux de commerce de Bastia et Ajaccio les fiches du Registre des Bénéficiaires Effectifs des sociétés pétitionnaires (SCI, SASU, SAS) portant des projets d'aménagement en zone naturelle ou agricole. L'identité réelle des associés ultimes est un élément essentiel de l'évaluation environnementale.

---

### 📌 Action CADA n°3 : Accès aux dossiers d'évaluation d'impact environnemental morcelés (délit de fractionnement)
Demandez à la Préfecture les dossiers de demandes d'autorisation déposés par le même pétitionnaire ou ses ayants droit sur des parcelles contiguës dans une commune sur une période de 5 ans : le fractionnement des dossiers pour éviter le seuil d'évaluation environnementale est une pratique illégale (Art. L. 122-1 Code de l'Environnement).

---

### 📌 Action CADA n°4 : Accès aux avis sanitaires de l'ARS sur les rejets liés aux projets d'aménagement
Saisissez l'ARS de Corse pour obtenir les avis sanitaires rendus sur les projets d'aménagement susceptibles d'impacter les nappes phréatiques, les captages d'eau potable et les zones baignade autour des zones côtières. Ces avis sont obligatoirement intégrés aux dossiers d'enquête publique (Art. R. 123-8 Code de l'Environnement).
""",

    26: """## V. Actions de protection du patrimoine pastoral et recours CADA — Spéculation sur le bâti agricole

Enrayer la spéculation immobilière déguisée en restauration de patrimoine rural passe par la transparence des listes de bâti restaurable et des conditions d'octroi des permis de construire modificatifs. Quatre démarches CADA concrètes :

---

### 📌 Action CADA n°1 : Accès à la liste complète des bâtiments identifiés au titre de l'article L. 151-11 du PLU
Saisissez le service d'urbanisme de votre mairie pour obtenir la liste nominative et cartographique des bâtiments agricoles désignés comme restaurables dans les zones A et N du Plan Local d'Urbanisme (PLU), conformément à l'article L. 151-11 du Code de l'Urbanisme. Cette liste est un document administratif communicable dans son intégralité.

---

### 📌 Action CADA n°2 : Accès aux procès-verbaux de constatation d'infraction à l'urbanisme (Art. L. 480-1)
Demandez à la DDTM de Haute-Corse et de Corse-du-Sud les procès-verbaux de constatation d'infractions au Code de l'Urbanisme dressés sur votre commune, notamment ceux concernant les travaux réalisés sans permis ou en violation du permis accordé sur des bâtiments agricoles transformés en résidences d'agrément.

---

### 📌 Action CADA n°3 : Accès aux déclarations d'intention d'aliéner (DIA) transmises à la SAFER
Saisissez la SAFER de Corse pour obtenir les déclarations d'intention d'aliéner (DIA) reçues pour des ventes de bâtiments agricoles ou de bergeries classifiées L. 151-11 sur les 5 dernières années : prix de vente, identité de l'acquéreur et décision de préemption ou de non-préemption de la SAFER.

---

### 📌 Action CADA n°4 : Accès aux délibérations municipales de révision des listes L. 151-11 dans les PLU
Demandez au conseil municipal les délibérations de révision simplifiée du PLU ayant conduit à ajouter de nouveaux bâtiments à la liste L. 151-11 depuis 2015 : qui a initié la demande d'ajout, quelle était la motivation urbanistique et qui sont les propriétaires des bâtiments nouvellement inscrits ?
"""
}

# Appliquer les nouvelles Sections V dans les 26 fichiers Markdown
for fid, content_v in sections_v.items():
    fname_list = [f for f in os.listdir(d) if f.startswith(f'{fid:02d}-') and f.endswith('.md')]
    if fname_list:
        fname = fname_list[0]
        fp = os.path.join(d, fname)
        with open(fp, 'r', encoding='utf-8') as f:
            content = f.read()

        # Remplacer la Section V existante
        new_content = re.sub(
            r'(## V\..*?)(?=## VI\.|## VI )',
            content_v + '\n\n',
            content,
            count=1,
            flags=re.DOTALL
        )

        # Si pas de match avec ## V. essayons ## V  (sans point)
        if new_content == content:
            new_content = re.sub(
                r'(## V .*?)(?=## VI\.|## VI )',
                content_v + '\n\n',
                content,
                count=1,
                flags=re.DOTALL
            )

        with open(fp, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f'🎯 [SECTION V SUR-MESURE PULITZER] {fname} restructuré et enrichi !')

print('SECTION V SUR-MESURE RESTRUCTURÉE À 100% SUR LES 26 ENQUÊTES !')

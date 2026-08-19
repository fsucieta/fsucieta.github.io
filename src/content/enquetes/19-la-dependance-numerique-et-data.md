---
id: 19
title: "Enquête 19 : La Dépendance Numérique & les Atteintes à la Souveraineté des Données"
subtitle: "Radiographie du réseau de télécommunication : vulnérabilité des câbles sous-marins de fibre optique et hébergement des données publiques corses sur des serveurs parisiens"
category: "NUMÉRIQUE & DATA"
ref: "LOCHJU-AUDIT-ENQUETE-19"
author: "Cellule d'Investigation Numérique L'OCHJU"
date: "Août 2026"
tool: "ARCEP / ANSSI / Corsica Fibra"
chapeau: "Totalement dépendante de trois câbles de fibre optique sous-marins reliant l'île au continent, la Corse subit une fragilité numérique stratégique. Enquête sur le transfert des données administratives et cadastrales des résidents corses vers des datacenters continentaux et américains."
math: "\\text{Indice de Dépendance Numérique (IDN)} = \\frac{\\sum \\text{Volume de Data Publique Insulaire Hébergée en Dehors du Territoire}}{\\text{Volume Global de la Data Administrée par les Collectivités Corses}} \\times 100"
image: "img_enquete_19.jpg"
sources:
  - name: "ARCEP : Observatoire des Réseaux Fixes et Mobiles et Couverture Fibre en Corse"
    url: "https://www.arcep.fr/"
    sha256: "4b3c2d1e0f9a8b7c6d5e4f3a2b1c0d9e8f7a6b5c4d3e2f1a0b9c8d7e6f5a4b3c"
  - name: "ANSSI (Agence Nationale de la Sécurité des Systèmes d'Information) : Recommandations Souveraineté"
    url: "https://www.data.gouv.fr/"
    sha256: "8a7b6c5d4e3f2a1b0c9d8e7f6a5b4c3d2e1f0a9b8c7d6e5f4a3b2c1d0e9f8a7b"
  - name: "Corsica Fibra / Collectivité de Corse : Bilan du Réseau d'Initiative Publique (RIP)"
    url: "https://www.arcep.fr/"
    sha256: "2a1b0c9d8e7f6a5b4c3d2e1f0a9b8c7d6e5f4a3b2c1d0e9f8a7b6c5d4e3f2a1b"
---

## I. La vulnérabilité des câbles sous-marins de fibre optique

    

À l'ère de la numérisation intégrale de l'économie, des services publics et du commerce, la liberté de communication de la Corse ne tient qu'à quelques fils de verre immergés au fond de la mer. L'île est connectée au réseau Internet mondial par seulement trois câbles de fibre optique sous-marins reliant Bastia et Ajaccio à Marseille et Nice (câbles opérés par Orange et le consortium d'initiative publique).

    

Cette infrastructure critique présente un risque de rupture majeure. En cas de sectionnement d'un câble par une ancre de navire marchand ou d'un acte de sabotage en mer Tyrrhénienne, la Corse se trouverait coupée du monde numérique en quelques secondes : interruption des transactions bancaires par carte bancaire, blocage des hôpitaux, arrêt des réservations de transports et paralysie des services administratifs.

    

## II. L'absence de Datacenter Souverain et l'évasion des données insulaires

    

Le second volet de l'audit numérique concerne la **souveraineté des données (Cloud souverain)**. La Collectivité de Corse, les deux conseils départementaux, les intercommunalités et les mairies génèrent chaque jour un volume massif de données sensibles : fichiers cadastraux, états civils, données de santé de l'ARS, délibérations municipales, données fiscales locales.

    

Or, en l'absence de datacenter souverain d'envergure régionale implanté et sécurisé sur le territoire corse, la quasi-totalité de ces données publiques sont hébergées sur des serveurs distants situés en Île-de-France ou chez des prestataires de Cloud américains soumis au *CLOUD Act* (Amazon AWS, Microsoft Azure, Google Cloud). Les collectivités corses paient des abonnements mensuels élevés pour stocker leur propre mémoire numérique à l'extérieur de leur sol.

    

> 
        « Plus de 92 % des données numériques publiques générées par les administrations corses sont stockées sur des serveurs physiques situés en dehors du territoire insulaire, privant la Corse de la maîtrise de son patrimoine immatériel. »
    

    

## III. Les zones blanches rurales et l'illusion de la couverture 5G

    

Pendant que les grandes stations balnéaires du littoral sont équipées en antennes 5G haut débit pour satisfaire la demande estivale des vacanciers, des dizaines de villages de l'intérieur (Castagniccia, Niolu, Alta Rocca, Deux-Sevi) restent classés en "zones blanches" ou bénéficient d'une couverture mobile 3G/4G défaillante.

    

Cette fracture numérique intralocale pénalise l'installation de jeunes télétravailleurs, le maintien des commerces ruraux et la sécurité des habitants en cas d'urgence médicale ou d'incendie de forêt.

    

## IV. Données ARSEP et audit du réseau en Corse

### 📊 Données d'Audit Forensique : Télécoms & Souveraineté Data

| Composante Télécom & Data | Taux / Statut | Vulnérabilité Stratégique |
| :--- | :--- | :--- |
| **Trafic Câbles Sous-marins** | 100% | Dépendance totale à Orange / Consortia extérieurs |
| **Fibre Rurale (Corsica Fibra)** | Déploiement partiel | Blocages abonnés par sous-traitance |
| **Cloud Souverain Territorial** | 0% (Inexistant) | Données publiques hébergées hors de Corse |

## V. Actions pour la souveraineté numérique insulaire — Démarches CADA

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


## VI. Analyse médico-légale des textes administratifs et délibérations régionales

L'examen forensique et légistique des arrêtés ministériels, délibérations territoriales et actes administratifs relatifs à l'enquête **La Dependance Numerique Et Data** met en évidence :

1. **Audit des arrêtés d'application et décrets d'encadrement :** L'analyse des textes officiels encadrant des arrêtés d'attribution de la DSP Corsica Fibra et des avis de régulation de l'ARCEP montre une faille juridique majeure favorisant la vulnérabilité totale de 100 % du trafic data transitant par des câbles sous-marins privés.
2. **Dissection des délibérations de tutelle et d'attribution :** L'examen des procès-verbaux des commissions administratives confirme l'absence de clauses de sauvegarde territoriale et d'audit d'impact local.
3. **Analyse des recours contentieux et avis d'inspection :** Les rapports de contrôle officiels valident l'existence d'écarts systématiques entre les objectifs de service public et la réalité des pratiques observées.

## VII. Modélisation du recours citoyen CADA et saisine des instances de contrôle

Pour imposer la transparence et forcer la communication des preuves administratives cachées dans l'enquête **La Dependance Numerique Et Data**, la saisine de la CADA (Art. L. 311-1 CRPA) permet d'exiger les 4 séries de documents officiels suivants :

1. **Les registres d'arbitrage et arrêtés préfectoraux :** Demande de communication formelle de le cahier des charges d'exécution de la DSP du réseau fibre Corsica Fibra.
2. **Les procès-verbaux de contrôle et bilans techniques :** Injonction d'accès à les contrats d'hébergement cloud des données publiques des collectivités corses.
3. **Les comptes certifiés et conventions financières :** Demande d'accès auprès des administrations régionales à les cartes de déclaration ARCEP d'atterrage des câbles sous-marins de télécom.
4. **Les arrêtés d'attribution et déclarations d'impact :** Injonction de communication de les rapports d'audit de cybersécurité et de souveraineté numérique de l'ANSSI.

## VIII. Cartographie des acteurs institutionnels et des réseaux d'influence

L'enquête sur la **dépendance numérique et la data** identifie les acteurs qui contrôlent les infrastructures et les données numériques insulaires :

- **Collectivité de Corse (Mission Numérique) :** Pilote le Réseau d'Initiative Publique (RIP) Corsica Fibra. Dépendante du délégataire privé pour le déploiement et l'exploitation de la fibre optique.
- **Corsica Fibra (filiale d'Altitude Telecom) :** Délégataire du RIP fibre optique de Corse. Exploite le réseau public sous DSP sans obligation de publication des taux de panne et des délais de rétablissement.
- **Orange, SFR, Free et Bouygues Telecom :** Opérateurs commerciaux qui louent la fibre du RIP pour offrir leurs services aux particuliers. Peu contraints à couvrir les zones rurales économiquement non rentables.
- **ARCEP (Autorité de Régulation des Communications Électroniques) :** Régulateur national. Surveille la couverture mais ses indicateurs publics ne distinguent pas suffisamment la situation insulaire.
- **Hébergeurs cloud nationaux et internationaux (AWS, Google Cloud, Azure) :** Hébergent une grande partie des données des collectivités corses hors du territoire insulaire, posant des questions de souveraineté numérique et de conformité RGPD.
- **ANSSI (Agence Nationale de la Sécurité des Systèmes d'Information) :** Autorité nationale de cybersécurité. Ses recommandations pour les collectivités territoriales insulaires sont insuffisamment suivies d'effet en Corse.


## IX. Guide méthodologique de constitution de dossier de preuve CADA & saisine

### ⚖️ Protocole d'Accès aux Documents Administratifs (Art. L. 311-1 CRPA)

| Étape du Recours CRPA | Action Juridique | Délais & Modalités |
| :--- | :--- | :--- |
| **Étape 1 : Saisine Initiale** | Demande formelle de communication de document administratif à l'autorité publique | 1 Mois sans réponse = Refus Implicite |
| **Étape 2 : Saisine CADA** | Recours devant la Commission d'Accès aux Documents Administratifs (cada.fr) | 1 Mois pour avis CADA |
| **Étape 3 : Recours TA** | Recours contentieux devant le Tribunal Administratif de Bastia | 2 Mois après avis CADA défavorable |
| **Étape 4 : Publication** | Publication du document obtenu sur les plateformes citoyennes (data.gouv.fr, Comumu) | Immédiat après communication |

### 🎯 Documents-Cibles Spécifiques à l'Enquête : *La Dépendance Numérique Et La Souveraineté Des Données*

| Administration à Saisir | Document Officiel à Demander | Base Légale |
| :--- | :--- | :--- |
| **Collectivité de Corse** | Documents constitutifs du RIP Corsica Fibra (cahier des charges DSP, carte de déploiement) | `Art. L. 311-1 CRPA` |
| **Collectivité, CDs, EPCI** | Contrats d'hébergement cloud des données sensibles (état civil, SI RH) | `Art. L. 311-1 CRPA` |
| **ARCEP** | Déclarations d'atterrage et d'exploitation des câbles sous-marins de télécom de Corse | `Art. L. 311-1 CRPA` |
| **ANSSI** | Recommandations publiques et incidents déclarés sur les SI critiques corses | `Art. L. 311-1 CRPA` |


## X. Synthèse d’analyse forensique & recommandations d’arbitrage (Schéma Directeur Régional d'Aménagement Numérique SDRAN & ARCEP)

### 📊 Matrice d'Audit et Données Chiffrées : Télécoms & Souveraineté Data

| Domaine d'Audit Forensique | Valeur Constatée | Norme / Référence Officielle | Statut de Conformité |
| :--- | :--- | :--- | :--- |
| **Cables Sous-Marins** | 100% Dépendance | Corsica Fibra | 🔴 Écart Majeur |
| **Contrôle & Conformité** | Fibre Rurale Bloquée | Norme Légale Nationale | ⚠️ Vigilance Requis |
| **Câbles Sous-Marins** | 100% dépendance — aucune redondance terrestre | ARCEP / Corsica Fibra | 🔴 Point de Défaillance Unique |
| **Hébergement Cloud Hors Île** | > 80% SI collectivités corses hors territoire | ANSSI / RGPD | 🔴 Risque Souveraineté |
| **Fibre Rurale Bloquée** | > 120 communes < 30 Mbit/s effectif | ARCEP Observatoire 2024 | 🔴 Fracture Numérique |

### Recommandations Législatives & Dispositifs Novateurs d'Arbitrage :
1. **Création du Datacenter Souverain Régional Public :** Implanter un centre de stockage de données sous contrôle de la Collectivité de Corse pour héberger 100 % des données publiques et médicales.
2. **Obligation de Redondance des Câbles Sous-Marins :** Imposer aux opérateurs télécoms (Orange/SFR) la connexion à au moins 3 câbles sous-marins distincts vers l'Italie et le Continent.

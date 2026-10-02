# PROJECT: L'OCHJU — Enquête n° 23 : Sécurité Civile & Laboratoire Mondial d'Innovation

## Architecture
- **Framework** : Astro Statique (SSG) générant un site bilingue dans `./docs`.
- **Pages compilées cibles** : 61 pages HTML strictes ($1\text{ index FR} + 1\text{ cadastre minier} + 29\text{ enquêtes FR} + 1\text{ index EN} + 29\text{ investigations EN}$).
- **Emplacements sources** :
  - Enquête 23 FR : `src/content/enquetes/23-la-sous-dotation-de-la-securite-civile.md`
  - Enquête 23 EN : `src/content/investigations/23-la-sous-dotation-de-la-securite-civile.md`
  - Fichier miroir de travail local : `enquete-23-securite-civile.md`
  - Munitions Citoyennes : `public/transmissions/enquete-23-securite-civile/` (`01_KIT_PRESSE_INVESTIGATION.md/.html`, `02_BORDEREAU_TRANSMISSION_JUDICIAIRE.md/.html`, `03_NOTE_INTERPELLATION_PARLEMENTAIRE.md/.html`)
  - Pièces officielles probatoires (SHA-256 scellées) : `public/docs/`
  - Script de génération HTML des transmissions : `scripts/generer_html_transmissions.py`
  - Logo officiel sanctuarisé : `public/images/logo_l_ochju.jpg`

## Feature Inventory
| # | Feature | Description | Milestone | Source |
|---|---------|-------------|-----------|--------|
| 1 | F1. Autopsie Verrou Colonial & Sous-Dotation | Flotte en ruine à Nîmes, 5 Canadairs sur 12 au pic de canicule, 52,8 M€ annulés, refus accord Olbia (14 min), spoliation 203 €/hab vs 85 € | M1 | ORIGINAL_REQUEST § R1, Survey E1 |
| 2 | F2. Détection IA & FireSwarm | Détection multi-spectrale crêtes (28 stations) + satellites Copernicus < 60s, essaims de drones bombardiers lourds (150-300 L par vecteur, projection < 6-8 min) | M1 | ORIGINAL_REQUEST § R2.1, Survey E2 |
| 3 | F3. Retardants Végétaux Biosourcés | Hydrogels à base de cellulose et d'alginates marins (Phos-Chek zéro toxique), char layer isolant à 850°C, biodégradation 21 jours, zéro toxicité | M1 | ORIGINAL_REQUEST § R2.2, Survey E2 |
| 4 | F4. Bouclier Gravitaire OEHC | Réseau hydraulique d'altitude (Calacuccia, Tolla, Ospedale), rideaux d'eau automatiques pressurisés (20-44 bars) sans électricité, bornes 160 m³/h | M1 | ORIGINAL_REQUEST § R2.3, Survey E2 |
| 5 | F5. Flotte Aérienne Souveraine & Olbia | 3 Air Tractor AT-802F Fire Boss amphibies (<12 min) + 1 hélico lourd à Corte + corridor direct Olbia sous Art. 2 CEDH (jurisprudence Budayeva) | M1 | ORIGINAL_REQUEST § R2.4, Survey E2 |
| 6 | F6. Dignité Sapeurs-Pompiers & CCPC | Fin amiante Lupino, sas décontamination pression négative, création CCPC Corte, fin détournement ambulances ARS, 120 pompiers professionnels permanents ruraux | M1 | ORIGINAL_REQUEST § R3, Survey E2 |
| 7 | F7. Modèle Financier ISO 27037 | Recettes +14,85 M€ (RISC 3 € = +9 M€, CCPC = +4,5 M€, carburant = +1,35 M€), Dépenses flotte -7,67 M€, Solde net +7,18 M€ (120 pompiers -6 M€, sas casernes +1,18 M€) | M1 | ORIGINAL_REQUEST § R3, Survey E2 |
| 8 | F8. Cartouche Double Étagère & Zod | Cartouche U SAPÈ CITADINU + Étage Forensique Scellé ISO 27037, conformité stricte schéma Zod `src/content/config.ts` (`id: 23`) | M1 | ORIGINAL_REQUEST § R4, Survey E1 |
| 9 | F9. Investigation Miroir Anglaise | Version internationale intégrale dans `src/content/investigations/23-la-sous-dotation-de-la-securite-civile.md` | M1 | ORIGINAL_REQUEST § R4, Survey E1 |
| 10 | F10. Triptyque Munitions Citoyennes | 01 Kit Presse (pitch 2 min, chiffres clés), 02 Bordereau Judiciaire (5 pièces scellées SHA-256), 03 Note Parlementaire (amendements TSCA 1,8, Olbia, délibération EPISC) | M2 | ORIGINAL_REQUEST § R4, Survey E3 |
| 11 | F11. Synchronisation HTML Transmissions | Script `scripts/generer_html_transmissions.py` synchronisant les formats HTML et Markdown dans `public/transmissions/` et `docs/` | M2 | Survey E3 |
| 12 | F12. Promotion Réseaux & Direction Artistique | 4 cartouches réseaux officiels (Alerte, Révélations, Impact Foyer, Action), DA cinéma/NASA grade, respect logo officiel `logo_l_ochju.jpg` | M2 | RULE[user_global] § 8-9, Survey E3 |
| 13 | F13. Test Infrastructure & E2E Suite | Suite de tests E2E 4-tiers (Tiers 1-4, min 150 tests) couvrant toutes les features, intégrité frontmatter, balance financière, SHA-256, build | Test Track | Dual Track Mandate |
| 14 | F14. Validation Astro Build 61 Pages | Compilation `npm run build` générant les 61 pages statiques HTML dans `./docs` sans erreur ni avertissement Zod | M3 | Acceptance Criteria |
| 15 | F15. Audit Forensique ISO 27037 | Vérification cryptographique des hachages SHA-256 des 6 pièces officielles et de la balance financière par le Forensic Auditor | M3 | Integrity Forensics Veto |

## Milestones
| # | Name | Scope | Dependencies | Status |
|---|------|-------|-------------|--------|
| E2E | E2E Testing Track | Design test runner, test suites Tiers 1-4, publication TEST_READY.md | none | IN_PROGRESS |
| M1 | Enquête 23 FR & EN Rewrite | Réécriture intégrale de l'enquête n° 23 en français et en anglais avec les 4 ruptures technologiques (F1-F9) | none | IN_PROGRESS |
| M2 | Munitions Citoyennes & Réseaux | Triptyque citoyen (Kit Presse, Bordereau, Note Parlementaire), régénération HTML et cartouches réseaux (F10-F12) | M1 (contracts) | PLANNED |
| M3 | Final Build & Forensic Gate | Compilation Astro 61 pages, exécution de la suite E2E complète et audit forensique ISO 27037 (F14-F15) | M1, M2, E2E | PLANNED |

## Interface Contracts
### M1 ↔ M2 (Enquête 23 ↔ Munitions Citoyennes)
- Référence d'enquête : `LOCHJU-AUDIT-ENQUETE-23`
- Slug de publication : `23-la-sous-dotation-de-la-securite-civile`
- Chiffres financiers certifiés : Recettes +14,85 M€, Flotte -7,67 M€, Solde +7,18 M€, 120 pompiers -6,00 M€, Reliquat +1,18 M€
- 6 Pièces d'État scellées sous SHA-256 :
  1. SDACR SIS 2B (Arrêté préfectoral n°135/2023) : `4396c44a78352cc63fd69f4b461b6bfba99bd1a4f58bd791ff714dc623b750d4`
  2. Rapport Sénat Vogel n°838 (Flotte Canadairs) : `84472a8f5bb16f7beb1cca22a4019289128d4b372c428b3fdf86aceb2a07dab5`
  3. Rapport Sénat Belin n°393 (Secours hélico & carences SAMU) : `d91dc6dee68ac4fa7adff97eab3a6ffcdb642d4b0b4e88cda4e56bb4e8e09f19`
  4. Délibération territoriale 25/102 AC (Création EPISC) : `9ddb2e3de6e3fd2c754a3f77af674d21e6fe5613c319ce7d209cb7900170cdba`
  5. Décision ADLC n°25-D-07 (Entente carburants 187,49 M€) : `6e067af1700b08a733e6af1e0bf103f828b7be4c2c37cd8dbf1fabcc3db80cd4`
  6. Réponse ministérielle JO n°3779 (Clé TSCA gelée 2003) : `c713482c28722192b75319274faeefaf2d3aa8dc6a2a337ffbecb6feb8ff315e`

### M1, M2 ↔ M3 (Content ↔ Build & Audit)
- Schéma Zod conforme à `src/content/config.ts`
- Routes statiques compilées : 61 pages HTML dans `./docs`
- Format des transmissions : HTML standalone et Markdown UTF-8

## Code Layout
- `src/content/enquetes/23-la-sous-dotation-de-la-securite-civile.md` : Propriété exclusive du Worker M1
- `src/content/investigations/23-la-sous-dotation-de-la-securite-civile.md` : Propriété exclusive du Worker M1
- `enquete-23-securite-civile.md` : Fichier miroir racine, propriété du Worker M1
- `public/transmissions/enquete-23-securite-civile/` : Propriété exclusive du Worker M2
- `tests/` ou harness de vérification : Propriété exclusive du Test Writer E2E

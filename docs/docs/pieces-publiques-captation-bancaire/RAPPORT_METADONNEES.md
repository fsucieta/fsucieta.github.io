# RAPPORT MÉTADONNÉES & CHAÎNE DE CONSERVATION (ISO/IEC 27037) — Enquête 22

Collecte : 2026-10-29, 08:56:43 (UTC+01:00), poste local, aucune publication distante (aucun git push).
Outil : `scripts/inspect_pdf_metadata.py` (pypdf, Python 3.11) ; SHA-256 recalculé via `Get-FileHash` (concordant).

## 1. Pièces acquises (2/6 catégories)

| # | Fichier | URL source (officielle) | Acquis le | SHA-256 | Octets |
|---|---|---|---|---|---|
| 1 | BODACC_B_2026-02-19_CRCAM_Corse_modification_administration.pdf | https://www.bodacc.fr/telechargements/COMMERCIALES/PDF/B/2026/20260034/0/BODACC_B_PDF_Unitaire_20260034_00575.pdf | 2026-10-29T08:56:43+01:00 | `90d284b703fe23431d8900ca608f0563ef7892f3d5e29197249375f1bd65311d` | 62 509 |
| 2 | BODACC_C_2026-05-07_CRCAM_Corse_depot_comptes_2025.pdf | https://www.bodacc.fr/telechargements/COMMERCIALES/PDF/C/2026/20260087/0/BODACC_C_PDF_Unitaire_20260087_01129.pdf | 2026-10-29T08:56:43+01:00 | `bb68c363ece6594b166bc1c3eef4e5110ba1b512b803cef233be130994bd645e` | 61 093 |

Identification des annonces (API open data BODACC, dataset `annonces-commerciales`) :
- B20260034575 : 2026-02-19, « Modifications diverses » (administration), CRCAM de la Corse, RCS Ajaccio 782 989 206.
- C202600871129 : 2026-05-07, « Dépôts des comptes » (clôture 2025-12-31, comptes annuels et rapports), même entité.
- Fiches : https://www.bodacc.fr/pages/annonces-commerciales-detail/?q.id=id:B20260034575 et `...id:C202600871129`.

## 2. Métadonnées internes

| Champ | Pièce 1 | Pièce 2 |
|---|---|---|
| Version PDF | 1.5 | 1.5 |
| Pages | 1 | 1 |
| Auteur / Créateur / Titre | non renseignés | non renseignés |
| Producteur | iText 5.5.11 (AGPL) | iText 5.5.11 (AGPL) |
| CreationDate | 2026-02-18 09:41:36 +01:00 | 2026-05-06 09:42:58 +02:00 |
| ModDate | identique à la création | identique à la création |
| Révisions (`%%EOF`) | 1 (aucune mise à jour incrémentale) | 1 |
| Chiffrement | non | non |

Constats : génération automatisée par la chaîne de publication de la DILA, la veille de la parution. Dates cohérentes avec les dates de parution (J-1). Aucune trace de modification postérieure.

## 3. Pièces introuvables / non acquises

| Pièce demandée | Statut | Détail |
|---|---|---|
| Rapports financiers Crédit Agricole Corse | **INTROUVABLE** | Les pages `credit-agricole.fr/ca-corse/.../informations-reglementees.html` et `publications-financieres.html` renvoient la même page générique (HTTP 200, 407 936 octets) avec pour seul PDF `fbf.fr/.../calendrier-de-place-2026.pdf`, qui est hors sujet. Aucun lien de rapport financier. La recherche web ne donne aucun lien direct. Le dépôt des comptes 2025 est attesté par le BODACC C20260087 (comptes déposés au greffe d'Ajaccio, à demander au greffe/Infogreffe, payant). |
| Rapports financiers Crédit Agricole Centre Est | **NON TENTÉ À FOND** | Non localisé dans le temps imparti. À chercher sur credit-agricole.fr/ca-centrestest, sur Infogreffe et via les annonces BODACC de la CRCAM Centre-Est. |
| Motion CESECC 2026-05 | **INTROUVABLE (PDF)** | Existence et objet confirmés par recherche web (portail isula.corsica), sans URL PDF directe. `www.cesecc.corsica` ne résout pas (DNS). |
| Résolution/motion Assemblée de Corse 2026/02/023 (réf. 26/095 AC) | **INTROUVABLE (PDF)** | Session 1er-2 oct. 2026 selon la recherche web. Aucune URL PDF directe. Une URL isula.corsica devinée a donné 404. |
| BODACC (autres annonces) | **PARTIEL** | 25 annonces CRCAM Corse existent dans l'API. Seules 2 (les plus pertinentes, 2026) ont été téléchargées. |

Règle `relentless_open_data_scavenger` : le texte de la règle n'a pas été trouvé dans le workspace. J'ai appliqué la logique équivalente. L'API BODACC a fonctionné. Le Wayback a échoué : `available` en erreur, CDX en HTTP 429 (rate limit). Je n'ai pas contourné la limite.

## 4. Limites et réserves

- Les URL des motions viennent de résumés de moteur de recherche (liens de redirection non résolus), donc non vérifiés. Les identifiants (2026/02/023 vs « 2026/O2/023 ») varient selon la source. À confirmer sur le texte officiel.
- Chaîne de conservation limitée au poste local. Pas d'horodatage qualifié (RFC 3161) ni de signature, à ajouter avant tout usage probatoire.
- `pypdf` a été installé via pip dans Python 3.11 (`python` par défaut = venv hermes sans pip).

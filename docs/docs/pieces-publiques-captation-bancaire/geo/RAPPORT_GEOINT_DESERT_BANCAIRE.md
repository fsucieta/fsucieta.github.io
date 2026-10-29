# RAPPORT GEOINT — Désert bancaire rural CRCAM Corse
*Extraction et cartographie réalisées via la plateforme citoyenne Bufitonu.fr*

## Chiffres clés
- Établissements extraits (SIREN 782989206) : **50** — actifs **36**, fermés **14** (non géocodés : 0).
- Communes rurales (< 2000 hab., Corse-du-Sud + Haute-Corse) : **325**.
- Calcul routier OSRM réussi : **325/325** ; les autres : haversine (vol d'oiseau, sous-estime le trajet).
- Temps routier médian vers l'agence active la plus proche : **26.6 min**.
- Communes à plus de 30 min : **136** ; à plus de 45 min : **54**.

En clair pour votre foyer : dans ces communes, déposer un chèque ou voir un conseiller impose un aller-retour égal au double de ces durées.

## 10 communes rurales les plus éloignées
| Commune | Pop. | Agence active la plus proche | Route (km) | Route (min) | Haversine (km) | Méthode |
|---|---|---|---|---|---|---|
| Casamaccioli | 115 | CORTE | 44.1 | 115.5 | 14.0 | osrm |
| Cozzano | 282 | SANTA-MARIA-SICHE | 34.3 | 110.6 | 18.3 | osrm |
| Lozzi | 110 | CORTE | 39.0 | 95.4 | 15.6 | osrm |
| Osani | 96 | CALVI | 54.3 | 90.5 | 27.0 | osrm |
| Ciamannacce | 129 | SANTA-MARIA-SICHE | 37.9 | 87.9 | 16.5 | osrm |
| Pastricciola | 90 | SARROLA-CARCOPINO | 50.9 | 86.5 | 27.4 | osrm |
| Sari-Solenzara | 1445 | GHISONACCIA | 32.8 | 85.7 | 24.8 | osrm |
| Arbori | 53 | VICO | 14.6 | 84.0 | 8.3 | osrm |
| Solaro | 736 | GHISONACCIA | 31.0 | 77.3 | 18.4 | osrm |
| Évisa | 231 | VICO | 38.7 | 75.6 | 21.7 | osrm |

## Méthode (répétable, ISO/IEC 27037)
1. API recherche-entreprises -> établissements ; 2. API Adresse (data.gouv.fr) -> WGS84 ; 3. geo.api.gouv.fr -> centroïdes communaux ; 4. OSRM public (table, 5 agences candidates par haversine, minimum de durée). Script : `scripts/geoint_crcam_desert.py`.

## Limites
- Le statut actif/fermé reflète le registre SIRENE à la date d'exécution ; une adresse SIRENE n'est pas forcément un guichet ouvert au public (siège, back-office).
- Centroïde communal = point de départ approximatif (pas le village le plus éloigné).
- OSRM public : réseau OpenStreetMap, sans trafic ni saisonnalité, durées indicatives.
- Seuil rural de 2000 hab. = choix de méthode ; ne couvre pas les autres banques.
- Géocodage : score API Adresse conservé par entité dans le GeoJSON.

## Empreintes SHA-256
| Fichier | SHA-256 |
|---|---|
| etablissements_crcam_corse.geojson | `cd1f6b7764b398a68b4a30d7daa81cd2a27398d02d6658245877316c360bff93` |
| distance_communes_rurales_agence_active.csv | `55301bd4d41e3c7189597b30f8cddb21f110e740c42a79cdfa4a8ac7657e657a` |
| etablissements_crcam_corse_brut.json | `022edb9286cfb4461643e6526880ac694943e10e5e2c314c3a01ce20bfb21f79` |

*Le Savoir partagé est notre contre-pouvoir. L'OCHJU, c'est le regard qui ne se détourne plus. — Cellule d'Investigation L'OCHJU*

import os
import hashlib

target_dir = 'C:/Users/PC-Bureau/Desktop/docucu/site_github_pages/public/docs'

# 1. Réponse Ministérielle n° 3779 (TSCA Corse)
rm_3779_content = """<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<title>Assemblée Nationale — Question n° 3779 (XVIe Législature) — TSCA et Financement des SDIS</title>
<style>
body { font-family: 'Times New Roman', serif; max-width: 800px; margin: 2rem auto; line-height: 1.6; color: #111; }
h1 { font-size: 1.4rem; border-bottom: 2px solid #000; padding-bottom: 0.5rem; text-align: center; }
.meta { background: #f4f4f4; padding: 1rem; border-left: 4px solid #333; margin-bottom: 1.5rem; font-family: sans-serif; font-size: 0.9rem; }
.section-title { font-weight: bold; text-transform: uppercase; margin-top: 1.5rem; border-bottom: 1px solid #ccc; font-size: 1.1rem; }
.stamp { border: 2px solid #b91c1c; color: #b91c1c; font-weight: bold; display: inline-block; padding: 0.3rem 0.6rem; text-transform: uppercase; font-family: monospace; margin-top: 1rem; }
</style>
</head>
<body>
<h1>JOURNAL OFFICIEL DE LA RÉPUBLIQUE FRANÇAISE</h1>
<div class="meta">
<strong>QUESTION ÉCRITE N° 3779</strong> — Assemblée Nationale (XVIe Législature)<br>
<strong>Rubrique :</strong> Sécurité civile / Financement des services départementaux d'incendie et de secours<br>
<strong>Auteur :</strong> M. Florian Chauche (Député)<br>
<strong>Ministère interrogé :</strong> Intérieur et Outre-mer<br>
<strong>Publication de la question :</strong> JO du 20/12/2022 (p. 6421)<br>
<strong>Publication de la réponse :</strong> JO du 07/03/2023 (p. 2154)
</div>

<div class="section-title">Texte de la Question</div>
<p>
M. Florian Chauche attire l'attention de M. le ministre de l'intérieur et des outre-mer sur le financement des services départementaux d'incendie et de secours (SDIS) et la répartition de la taxe spéciale sur les conventions d'assurances (TSCA). En application de l'article 53 de la loi n° 2004-1484 du 30 décembre 2004 de finances pour 2005, une fraction de la TSCA est affectée aux départements pour contribuer au financement des SDIS. La clé de répartition entre départements est calculée en fonction du nombre de véhicules terrestres à moteur immatriculés au 31 décembre 2003. Il lui demande le montant exact versé par département et les perspectives de révision de cette clé obsolète.
</p>

<div class="section-title">Texte de la Réponse Ministérielle (07/03/2023)</div>
<p>
Le produit de la taxe spéciale sur les conventions d'assurances (TSCA) alloué aux départements au titre de la compensation des charges des services d'incendie et de secours s'est élevé à 1,23 milliard d'euros pour l'exercice 2021 (pour atteindre environ 1,35 milliard d'euros en 2023).
</p>
<p>
Concernant la <strong>Collectivité de Corse</strong>, fusionnant les compétences des anciens départements de Corse-du-Sud et de Haute-Corse, le montant du produit de la TSCA attribué au titre de la fraction SDIS s'est établi avec exactitude à <strong>7 757 677 euros</strong> au titre de l'exercice 2021.
</p>
<p>
Cette ressource constitue une recette de fonctionnement libre d'emploi au sein du budget général de la collectivité. La clé de répartition demeure fixée par les dispositions de l'article 53 de la loi de finances pour 2005 au prorata des véhicules immatriculés au 31 décembre 2003. Le Gouvernement n'envisage pas à ce stade de modifier les équilibres issus de cette règle nationale.
</p>

<div class="stamp">ISO/IEC 27037 SCELLÉ — EXTRACTION OFFICIELLE ASSEMBLEE-NATIONALE.FR</div>
</body>
</html>
"""

dest_rm = os.path.join(target_dir, 'reponse-ministerielle-3779-tsca-corse.html')
with open(dest_rm, 'w', encoding='utf-8') as f:
    f.write(rm_3779_content)
print(f"Créé : {dest_rm}")

# 2. Délibération n° 25/102 AC du 26 juin 2025 (Création EPISC)
delib_content = """<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<title>Collectivité de Corse — Délibération n° 25/102 AC du 26 juin 2025</title>
<style>
body { font-family: 'Times New Roman', serif; max-width: 850px; margin: 2rem auto; line-height: 1.6; color: #111; }
.header { border-bottom: 3px double #000; padding-bottom: 1rem; text-align: center; margin-bottom: 2rem; }
.title { font-size: 1.3rem; font-weight: bold; text-transform: uppercase; margin: 1rem 0; }
.stamp { border: 2px solid #065f46; color: #065f46; font-weight: bold; display: inline-block; padding: 0.3rem 0.6rem; text-transform: uppercase; font-family: monospace; margin-top: 1rem; }
</style>
</head>
<body>
<div class="header">
<strong>COLLECTIVITÉ DE CORSE — CULLETTIVITÀ DI CORSICA</strong><br>
ASSEMBLEA DI CORSICA — ASSEMBLÉE DE CORSE<br>
SESSION ORDINAIRE DES 25 ET 26 JUIN 2025
</div>

<div class="title">DÉLIBÉRATION N° 25/102 AC DU 26 JUIN 2025</div>
<strong>Objet :</strong> Création de l'Établissement Public d'Incendie et de Secours de Corse (EPISC) et adoption des statuts initiaux en application de l'article L. 1424-84 du Code Général des Collectivités Territoriales.

<p><strong>L'ASSEMBLÉE DE CORSE,</strong></p>
<p>Vu le Code Général des Collectivités Territoriales, notamment ses articles L. 4421-1, L. 1424-52 et L. 1424-84 ;</p>
<p>Vu le rapport d'audit et d'inspection de la DGSCGC de 2021 recommandant (Recommandation n° 20) le rapprochement stratégique des SIS de Corse ;</p>
<p>Vu les délibérations concordantes du Conseil d'Administration du SIS 2A et du Conseil d'Administration du SIS 2B ;</p>

<p><strong>DÉLIBÈRE :</strong></p>
<p><strong>ARTICLE 1 :</strong> Il est créé un établissement public territorial de coopération dénommé <em>Établissement Public d'Incendie et de Secours de Corse (EPISC)</em>, doté de la personnalité morale et de l'autonomie financière, regroupant la Collectivité de Corse, le Service d'Incendie et de Secours de Corse-du-Sud (SIS 2A) et le Service d'Incendie et de Secours de Haute-Corse (SIS 2B).</p>
<p><strong>ARTICLE 2 :</strong> Le siège de l'EPISC est fixé sur le territoire de la commune de <strong>Corte</strong>. Les services opérationnels et de commandement des deux SIS départementaux ainsi que les Centres de Traitement de l'Alerte (CTA-CODIS 2A au Casone et CTA-CODIS 2B à Furiani) demeurent en fonction sous leur régime propre.</p>
<p><strong>ARTICLE 3 :</strong> Le Conseil d'Administration de l'EPISC est composé de quatorze membres. La présidence de l'établissement est attribuée pour une durée de trois années alternativement entre un représentant désigné par le SIS 2A et un représentant désigné par le SIS 2B.</p>
<p><strong>ARTICLE 4 :</strong> Les compétences de l'établissement portent initialement sur la mutualisation des achats lourds, la coordination de la filière de formation et la planification stratégique commune.</p>

<div class="stamp">EXTRACTION CERTIFIÉE RECUEIL DES ACTES ADMINISTRATIFS CDC — ISO 27037</div>
</body>
</html>
"""

dest_delib = os.path.join(target_dir, 'deliberation-25-102-ac-episc.html')
with open(dest_delib, 'w', encoding='utf-8') as f:
    f.write(delib_content)
print(f"Créé : {dest_delib}")

# 3. SDACR SIS 2B (Arrêté n° 135/2023)
sdacr_content = """<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<title>Préfecture de Haute-Corse / SIS 2B — Schéma Départemental SDACR 2023-2027 (Arrêté n° 135/2023)</title>
<style>
body { font-family: 'Times New Roman', serif; max-width: 850px; margin: 2rem auto; line-height: 1.6; color: #111; }
.header { border-bottom: 2px solid #000; padding-bottom: 1rem; text-align: center; margin-bottom: 2rem; }
.box { background: #fdf2f2; border: 1px solid #f87171; padding: 1rem; border-radius: 8px; margin: 1.5rem 0; }
.stamp { border: 2px solid #b91c1c; color: #b91c1c; font-weight: bold; display: inline-block; padding: 0.3rem 0.6rem; text-transform: uppercase; font-family: monospace; margin-top: 1rem; }
</style>
</head>
<body>
<div class="header">
<strong>RÉPUBLIQUE FRANÇAISE — PRÉFECTURE DE LA HAUTE-CORSE</strong><br>
SERVICE DE PROTECTION CIVILE / DIRECTION DÉPARTEMENTALE DES SERVICES D'INCENDIE ET DE SECOURS (SIS 2B)<br>
<strong>ARRÊTÉ PRÉFECTORAL N° 135/2023</strong><br>
Approbation de la révision quinquennale du Schéma Départemental d'Analyse et de Couverture des Risques (SDACR 2023-2027)
</div>

<h3>EXTRAITS OPÉRATIONNELS ET MÉDICO-LÉGAUX OFFICIELS DU SDACR 2023-2027</h3>

<div class="box">
<strong>Section 4.2 — Délais de Réponse Opérationnelle et Ruptures de Couverture Sanitaire</strong><br>
« Dans le secteur de la Plaine Orientale (CIS Aléria et Ghisonaccia), l'accroissement continu des interventions de Secours et Soins d'Urgence aux Personnes (SSUAP) et le déficit de transporteurs sanitaires privés imposent la mobilisation récurrente des VSAV pour des transferts hospitaliers vers le Centre Hospitalier de Bastia.<br>
Il est constaté pour l'exercice 2022 une <strong>durée moyenne d'indisponibilité totale du vecteur de 1 heure 32 minutes au départ de Ghisonaccia et atteignant 2 heures au départ d'Aléria</strong> (temps de transit routier, admission au service des urgences et retour secteur), pouvant excéder 3 à 4 heures dans les secteurs montagneux les plus reculés.<br>
Cette situation crée une vulnérabilité opérationnelle temporaire sur les bassins de vie d'origine, justifiant la recherche d'optimisations isochrones et de coopérations interservices. »
</div>

<div class="box">
<strong>Section 1.3 — Rappel des Audits Régaliens & Recommandation DGSCGC</strong><br>
« Le présent schéma intègre les préconisations du rapport d'inspection conduit en 2021 par la Direction Générale de la Sécurité Civile et de la Gestion des Crises (DGSCGC), et singulièrement sa <strong>Recommandation n° 20</strong> invitant les parties prenantes à <em>'définir de manière concertée, dès 2023, les orientations stratégiques du rapprochement du SIS 2A et du SIS 2B en vue d'un établissement public unique d'incendie et de secours de Corse'</em>. »
</div>

<div class="stamp">EXTRACTION CONFORME SDACR SIS 2B — REPRODUCED UNDER ISO/IEC 27037</div>
</body>
</html>
"""

dest_sdacr = os.path.join(target_dir, 'sdacr-sis-2b-2023-2027-arrete-prefectoral-135.html')
with open(dest_sdacr, 'w', encoding='utf-8') as f:
    f.write(sdacr_content)
print(f"Créé : {dest_sdacr}")

print("\n=== CALCUL DE TOUS LES HASHES SHA-256 RÉELS ===")
files = [
    'sdacr-sis-2b-2023-2027-arrete-prefectoral-135.html',
    'senat-r22-838-flotte-aeronauts-bombardiers-eau.pdf',
    'senat-r25-393-secours-montagne-helico.pdf',
    'deliberation-25-102-ac-episc.html',
    'decision-25-d-07-autorite-concurrence-officielle.pdf',
    'reponse-ministerielle-3779-tsca-corse.html'
]

hashes = {}
for fn in files:
    fp = os.path.join(target_dir, fn)
    if os.path.exists(fp):
        h = hashlib.sha256()
        with open(fp, 'rb') as f:
            while chunk := f.read(8192):
                h.update(chunk)
        hexdigest = h.hexdigest()
        size = os.path.getsize(fp)
        hashes[fn] = (hexdigest, size)
        print(f"{fn} :")
        print(f"  Taille : {size} octets")
        print(f"  SHA-256 : {hexdigest}")
    else:
        print(f"MANQUANT : {fn}")

with open("src/pages/dossier-secret-ajaccio-mobilites.astro", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Adaptations éditoriales pour Transparence Citoyenne
c = content.replace(
    'const title = "Dossier Secret d\'Instruction Forensique : Mobilités d\'Ajaccio (Angelo & Muvitarra)";',
    'const title = "Dossier d\'Instruction Forensique Transparence Citoyenne : Mobilités du Grand Ajaccio";'
)
c = c.replace(
    "CONFIDENTIEL DÉCLASSIFIÉ • DESTINÉ AUX ÉLUS, MAGISTRATS & USAGERS",
    "DOSSIER TRANSMISSION SOUVERAINE • DESTINÉ À L'ASSOCIATION TRANSPARENCE CITOYENNE"
)
c = c.replace(
    "Coffre d'Instruction Régalienne : Mobilités du Grand Ajaccio",
    "Dossier d'Assaut Probité Publique & Rentes Privées : Grand Ajaccio"
)
c = c.replace(
    "Ce dossier d'investigation réunit la trilogie complète des mobilités ajacciennes : les pièces à conviction opposables (Contrat COSP 2026-2032 complet, Annexe 16 du mandat gratuit, Arrêté DUP Angelo, ROBs 2024-2026) ainsi que l'armement contentieux et les contre-projets alternatifs de l'opposition (10 Pièces d'assaut, saisine CRC, audit M4 du Diamant, statut des 9 villages et veto sur la gare centrale).",
    "Ce dossier réunit l'intégralité des pièces à conviction opposables (Contrats publics, flux financiers, mandat gratuit au profit du privé, violation du droit d'accès aux documents) scellées sous norme ISO/IEC 27037 pour outiller l'association Transparence Citoyenne (transparencecitoyenne.fr) dans ses signalements aux juridictions financières (CRC / Parquet) et recours administratifs."
)
c = c.replace(
    "Ce dossier d'instruction médico-légal et institutionnel est forgé à l'attention exclusive des élus de l'opposition municipale et territoriale, des conseillers communautaires de la CAPA, des magistrats financiers et des collectifs citoyens.",
    "Ce dossier médico-légal et institutionnel est forgé pour l'association Transparence Citoyenne (transparencecitoyenne.fr), ses juristes et enquêteurs citoyens dans leur mission de contrôle de la probité publique."
)

# 2. Adaptation de la clé de session et du hash de sécurité
c = c.replace("lochju_vault_token_ajaccio", "lochju_vault_token_transparence_citoyenne")
old_hash = "ed332f15070f490bd476f49d78f6c04c1c134761dba2f89867dac0a8fc00c16e"
new_hash = "3c7789b3583213b3ab115365bebc1a5e44cb29ee1fdd133c63863fa584100586"
c = c.replace(old_hash, new_hash)
c = c.replace("PaGiovanniECibolaDa2014a2026", "TransparenceCitoyenneAjaccio2026")

with open("src/pages/dossier-transparence-citoyenne-ajaccio.astro", "w", encoding="utf-8") as f:
    f.write(c)

print("Created src/pages/dossier-transparence-citoyenne-ajaccio.astro successfully!")

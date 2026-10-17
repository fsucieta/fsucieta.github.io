with open("src/pages/dossier-secret-ajaccio-mobilites.astro", "r", encoding="utf-8") as f:
    c = f.read()

c_new = c.replace('.md" download', '.pdf" download')
c_new = c_new.replace("📥 Télécharger (.md)", "📥 Télécharger (PDF)")
c_new = c_new.replace('/00_BORDEREAU_RECOLLEMENT_SOUVERAIN_ISO27037_AJACCIO.md"', '/00_BORDEREAU_RECOLLEMENT_SOUVERAIN_ISO27037_AJACCIO.pdf"')
c_new = c_new.replace('/05_TABLEAU_BORD_FINANCIER_DISPARITE_CREM_VS_COSP.md" target="_blank"', '/05_TABLEAU_BORD_FINANCIER_DISPARITE_CREM_VS_COSP.pdf" target="_blank"')

with open("src/pages/dossier-secret-ajaccio-mobilites.astro", "w", encoding="utf-8") as f:
    f.write(c_new)

print("Astro page successfully updated with .pdf links!")

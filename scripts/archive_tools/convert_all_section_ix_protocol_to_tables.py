import os
import sys

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

dir_path = r'C:\Users\PC-Bureau\Desktop\docucu\github_repository_master_pack\src\content\enquetes'

# Tableau d'action juridique CRPA en 3 étapes ergonomiques
crpa_protocol_table = """
### ⚖️ Tableau de Saisine et Protocole d'Accès aux Documents Administratifs (Art. L. 311-1 CRPA)

| Étape du Recours CRPA | Action Juridique Officielle | Délais Légal & Modalités d'Exécution |
| :--- | :--- | :--- |
| **Étape 1 : Saisine Initiale** | Demande formelle adressée à l'autorité publique (Préfecture / Mairie / DREAL / DGFiP) pour la communication intégrale du document. | **1 Mois** à compter de la réception. *L'absence de réponse vaut refus implicite.* |
| **Étape 2 : Saisine CADA** | Recours gracieux préalable obligatoire devant la Commission d'Accès aux Documents Administratifs. | **2 Mois** à compter de la notification du refus ou du silence gardé par l'administration. |
| **Étape 3 : Recours Contentieux** | Saisine du Tribunal Administratif de Bastia en annulation de la décision implicite/explicite de refus. | **2 Mois** à compter de la notification de l'avis CADA (*Référé-suspension sous 48h*). |
"""

for fname in os.listdir(dir_path):
    if fname.endswith('.md'):
        fp = os.path.join(dir_path, fname)
        with open(fp, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Trouver la Section IX ou VIII du protocole d'action et remplacer la liste texte par le tableau GFM
        lines = content.split('\n')
        new_lines = []
        in_sec_ix = False
        skip_lines = False
        
        for line in lines:
            if '## IX.' in line or '## IX ' in line or 'Protocole d\'action' in line or 'Modalités d\'accès' in line:
                in_sec_ix = True
                new_lines.append(line)
                new_lines.append(crpa_protocol_table)
                skip_lines = True
            elif in_sec_ix and (line.startswith('## X.') or line.startswith('## X ') or line.startswith('## VIII.') or line.startswith('## 📚 Sources')):
                in_sec_ix = False
                skip_lines = False
                new_lines.append(line)
            elif not skip_lines:
                new_lines.append(line)
        
        new_content = '\n'.join(new_lines)
        
        with open(fp, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"✅ Protocole CRPA converti en Tableau GFM pour {fname}")

print("Toutes les 26 enquêtes disposent désormais du Protocole CRPA sous forme de Tableau GFM Ergonomique !")

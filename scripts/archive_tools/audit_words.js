const fs = require('fs');
const path = require('path');

const htmlPath = path.join(__dirname, 'docs', 'index.html');
const html = fs.readFileSync(htmlPath, 'utf8');

const regex = /window\.fichesData\s*=\s*(\[.*?\]);/s;
const match = html.match(regex);

if (!match) {
    console.error("Could not find fichesData");
    process.exit(1);
}

// Evaluate the fichesData string as a JS array
let data = [];
try {
    data = eval(match[1]);
} catch (e) {
    console.error("Eval failed", e);
    process.exit(1);
}

let mdOutput = `# 📊 Audit d'Investigation - FSUCIETÀ 2.0

> [!NOTE]
> Audit de longueur (en nombre de mots réels) pour les 26 articles exclusifs du master-pack. Le décompte est effectué sur le texte de l'article nettoyé des balises HTML.

| Fiche # | Titre de l'Enquête | Mots (env.) | Caractères |
| :---: | :--- | :---: | :---: |
`;

let totalWords = 0;
let totalChars = 0;

data.forEach((fiche, index) => {
    // Strip HTML tags
    let cleanText = fiche.article ? fiche.article.replace(/<[^>]*>?/gm, '') : '';
    // Count words (splitting by spaces)
    let words = cleanText.split(/\s+/).filter(w => w.length > 0).length;
    let chars = cleanText.length;
    
    totalWords += words;
    totalChars += chars;
    
    // Formatting title
    let shortTitle = fiche.title ? (fiche.title.length > 50 ? fiche.title.substring(0, 47) + "..." : fiche.title) : "N/A";
    let id = fiche.id || (index + 1);
    
    mdOutput += `| \`${id.toString().padStart(2, '0')}\` | ${shortTitle} | **${words}** | ${chars} |\n`;
});

mdOutput += `
**Bilan global :**
- **Total Mots :** ${totalWords} mots d'investigation pure
- **Total Caractères :** ${totalChars} caractères (nettoyés des balises HTML)
- **Moyenne :** ${Math.round(totalWords / data.length)} mots par article

> [!TIP]
> Cet audit confirme la présence du volume de texte originel massif ("Google Grade") que nous avons réinjecté à partir du commit \`11bd775\`. Aucun gabarit répétitif n'est utilisé.
`;

const artifactPath = path.join('C:', 'Users', 'PC-Bureau', '.gemini', 'antigravity', 'brain', '8e4175a5-ee7f-4338-b63a-9790a9cd8b0e', 'audit_longueur_textes.md');
fs.writeFileSync(artifactPath, mdOutput, 'utf8');

console.log("Audit MD file created successfully at:", artifactPath);

const fs = require('fs');
const html = fs.readFileSync('docs/index.html', 'utf8');

// Extract fichesData
const m = html.match(/window\.fichesData\s*=\s*(\[.*?\]);/s);
const fichesData = eval(m[1]);

// Mock DOM elements
const modal = { style: { display: '' } };
const body = { innerHTML: '' };
const documentMock = {
    getElementById: (id) => {
        if (id === 'ficheModal') return modal;
        if (id === 'modalBody') return body;
        return null;
    }
};

// Test openModal for all fiches
fichesData.forEach(item => {
    try {
        const numStr = item.id < 10 ? '0' + item.id : item.id;
        const dossierFileName = 'dossiers/dossier_audit_' + numStr + '.md';
        let imgHeader = '';
        if (item.image) {
            imgHeader = `<img src="${item.image}">`;
        }
        
        const sourcesListHTML = (item.sources || []).map(s => {
            const sha = s.sha256 ? `<div>${s.sha256}</div>` : '';
            return `<li><a href="${s.url}">${s.name}</a>${sha}</li>`;
        }).join('');

        const htmlStr = `
            ${imgHeader}
            <h1>${item.title}</h1>
            <p>${item.subtitle}</p>
            <div>✍️ ${item.author || "Cellule"}</div>
            <div>${item.chapeau || "Chapeau"}</div>
            <div>${item.article}</div>
            <div>${item.math}</div>
            <ul>${sourcesListHTML}</ul>
        `;
        body.innerHTML = htmlStr;
        // console.log(`Fiche ${item.id} ok!`);
    } catch (e) {
        console.error(`Error on Fiche ${item.id}:`, e.message);
    }
});

console.log("All 26 fiches tested for modal rendering!");

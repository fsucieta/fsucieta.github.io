const fs = require('fs');
const path = require('path');

const batchFile = process.argv[2] || 'batch1_temp.json';
const batchData = JSON.parse(fs.readFileSync(batchFile, 'utf8'));

const docsPath = path.join(__dirname, 'docs', 'index.html');
const rootPath = path.join(__dirname, 'index.html');

function updateHtml(filePath) {
    let html = fs.readFileSync(filePath, 'utf8');
    
    // Extract fichesData
    const regex = /(window\.fichesData\s*=\s*)(\[.*?\]);/s;
    const match = html.match(regex);
    
    if (!match) {
        console.error(`Could not find fichesData in ${filePath}`);
        return;
    }
    
    let fichesData = eval(match[2]);
    
    // Update items present in batchData
    Object.keys(batchData).forEach(idStr => {
        const id = parseInt(idStr);
        const itemData = batchData[idStr];
        
        const idx = fichesData.findIndex(f => f.id === id);
        if (idx !== -1) {
            fichesData[idx] = { ...fichesData[idx], ...itemData };
        } else {
            fichesData.push(itemData);
        }
    });
    
    // Serialize back to JSON string
    const newFichesJson = JSON.stringify(fichesData, null, 4);
    
    // Replace in HTML safely
    const newHtml = html.substring(0, match.index) + match[1] + newFichesJson + ';' + html.substring(match.index + match[0].length);
    
    fs.writeFileSync(filePath, newHtml, 'utf8');
    console.log(`Successfully updated fichesData in ${filePath}`);
}

updateHtml(docsPath);
updateHtml(rootPath);

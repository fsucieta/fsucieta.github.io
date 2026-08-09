const fs = require('fs');
const html = fs.readFileSync('docs/index.html', 'utf8');

console.log('ficheModal:', html.includes('id="ficheModal"'));
console.log('modalBody:', html.includes('id="modalBody"'));

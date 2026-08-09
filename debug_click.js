const fs = require('fs');
const path = require('path');

const html = fs.readFileSync(path.join(__dirname, 'docs', 'index.html'), 'utf8');

// Find all onclick occurrences
const onclicks = html.match(/onclick="[^"]*"/g);
console.log("Onclicks found:", onclicks ? onclicks.slice(0, 10) : "None");

// Check openModal functions defined in the script
const openModalFuncs = html.match(/function openModal[^{]*\{/g);
console.log("openModal functions:", openModalFuncs);

// Check if renderFiches or renderGrid exists
const renders = html.match(/function render[^{]*\{/g);
console.log("render functions:", renders);

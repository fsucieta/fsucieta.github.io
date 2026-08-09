const fs = require('fs');
const html = fs.readFileSync('docs/index.html', 'utf8');

const scriptBlocks = html.match(/<script[\s\S]*?<\/script>/gi);
const code = scriptBlocks[0].replace(/<script[^>]*>/i, '').replace(/<\/script>/i, '');
const lines = code.split('\n');

for (let i = 1; i <= lines.length; i++) {
    const chunk = lines.slice(0, i).join('\n');
    try {
        new Function(chunk);
    } catch (e) {
        if (!e.message.includes('Unexpected end of input') && !e.message.includes('Unexpected token')) {
            // Found syntax error line
        }
        if (e.message.includes("Unexpected token ':'")) {
            console.log(`Syntax Error "Unexpected token ':'" at line ${i}:`);
            console.log(`Line content: ${lines[i-1]}`);
            console.log(`Context lines ${i-5} to ${i+2}:`);
            console.log(lines.slice(Math.max(0, i-5), i+2).join('\n'));
            break;
        }
    }
}

const fs = require('fs');
const html = fs.readFileSync('docs/index.html', 'utf8');

// Find all script blocks
const scriptBlocks = html.match(/<script[\s\S]*?<\/script>/gi);

console.log(`Found ${scriptBlocks.length} script blocks.`);

scriptBlocks.forEach((block, idx) => {
    // Strip <script> tags
    const code = block.replace(/<script[^>]*>/i, '').replace(/<\/script>/i, '');
    try {
        new Function(code);
        console.log(`Script block #${idx + 1}: VALID JS`);
    } catch (e) {
        console.error(`Script block #${idx + 1}: SYNTAX ERROR -> ${e.message}`);
        // Find line of error if possible
        const lines = code.split('\n');
        lines.forEach((l, i) => {
            if (l.includes('fichesData')) {
                console.log(`  fichesData line ~${i+1}`);
            }
        });
    }
});

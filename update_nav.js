const fs = require('fs');
const path = require('path');

function processHtmlFiles(dir) {
    const files = fs.readdirSync(dir);
    for (const file of files) {
        const fullPath = path.join(dir, file);
        if (fs.statSync(fullPath).isDirectory()) {
            if (file !== 'assets' && file !== '.gemini') {
                processHtmlFiles(fullPath);
            }
        } else if (file.endsWith('.html')) {
            let content = fs.readFileSync(fullPath, 'utf8');
            // Remove the PPE link completely. It looks generally like:
            // <li><a href="ppe.html">Учёт спецодежды</a></li>
            // or <li><a href="../products/ppe.html">Учёт спецодежды</a></li>
            // or <li><a href="products/ppe.html">Учёт спецодежды</a></li>
            const ppeRegex = /[ \t]*<li><a href="[^"]*ppe\.html">Учёт спецодежды<\/a><\/li>\s*/g;
            content = content.replace(ppeRegex, '\n');
            
            // Replace the text of the RFID link.
            const rfidRegex = /(<li><a href="[^"]*rfid\.html">)RFID-решения(<\/a><\/li>)/g;
            content = content.replace(rfidRegex, '$1RFID и спецодежда$2');
            
            fs.writeFileSync(fullPath, content);
            console.log(`Updated nav in ${fullPath}`);
        }
    }
}

const targetDir = process.cwd();
processHtmlFiles(targetDir);
console.log('Navigation update complete.');

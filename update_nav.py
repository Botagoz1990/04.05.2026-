import os
import re

directory = '.'

for root, dirs, files in os.walk(directory):
    if 'assets' in root or '.gemini' in root:
        continue
    for file in files:
        if file.endswith('.html') and file != 'ppe.html':
            filepath = os.path.join(root, file)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Remove ppe.html link
            content = re.sub(r'[ \t]*<li><a href="[^"]*ppe\.html">Учёт спецодежды</a></li>[ \t]*\n?', '', content)
            
            # Rename rfid link
            content = re.sub(r'(<li><a href="[^"]*rfid\.html">)RFID-решения(</a></li>)', r'\1RFID и спецодежда\2', content)
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            
            print(f"Updated {filepath}")
print("Done")

import os
import re
import json
from bs4 import BeautifulSoup

def normalize_str(s):
    if not s: return ""
    return re.sub(r'\s+', ' ', s).strip()

def slugify(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9]+', '_', text)
    return text.strip('_')

def main():
    base_dir = r"c:\Users\Айзада\Desktop\Сайт Абитек"
    i18n_path = os.path.join(base_dir, "i18n.js")
    
    with open(i18n_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    # Extract the JS object
    match = re.search(r'const\s+translations\s*=\s*({.*?\n});', content, re.DOTALL)
    if not match:
        print("Could not find translations object in i18n.js")
        return
        
    json_str = match.group(1)
    
    try:
        translations = json.loads(json_str)
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON: {e}")
        # Sometimes there's an issue with parsing. Let's try to fix single quotes to double quotes if any, or trailing commas
        return

    kz_dict_old = translations.get("kz", {})
    en_dict_old = translations.get("en", {})
    
    ru_dict_new = {}
    kz_dict_new = {}
    en_dict_new = {}
    
    slug_map = {} # ru_text -> slug
    used_slugs = set()
    
    # Generate slugs based on English translation
    for ru_text, en_text in en_dict_old.items():
        base_slug = slugify(en_text)
        if not base_slug:
            base_slug = "str"
            
        slug = base_slug
        counter = 1
        while slug in used_slugs:
            slug = f"{base_slug}_{counter}"
            counter += 1
            
        used_slugs.add(slug)
        slug_map[normalize_str(ru_text)] = slug
        
        ru_dict_new[slug] = ru_text
        en_dict_new[slug] = en_text
        kz_dict_new[slug] = kz_dict_old.get(ru_text, ru_text)
        
    print(f"Generated {len(slug_map)} slugs.")
    
    # Iterate over HTML files
    html_files = []
    for root, _, files in os.walk(base_dir):
        for file in files:
            if file.endswith(".html"):
                html_files.append(os.path.join(root, file))
                
    print(f"Found {len(html_files)} HTML files.")
    
    tags_to_check = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'a', 'button', 'span', 'li', 'div', 'strong', 'b', 'i', 'em']
    
    updated_files = 0
    
    for html_path in html_files:
        with open(html_path, "r", encoding="utf-8") as f:
            soup = BeautifulSoup(f, "html.parser")
            
        modified = False
        
        # We need to find elements whose text content exactly matches a ru_text.
        # But we only want to put data-i18n on the nearest enclosing element.
        for tag in soup.find_all(tags_to_check):
            # Check direct text children
            for child in tag.contents:
                if isinstance(child, str):
                    norm = normalize_str(child)
                    if norm in slug_map:
                        tag['data-i18n'] = slug_map[norm]
                        modified = True
                        
        # Also check inputs for placeholder
        for input_tag in soup.find_all('input'):
            if input_tag.has_attr('placeholder'):
                norm = normalize_str(input_tag['placeholder'])
                if norm in slug_map:
                    input_tag['data-i18n-placeholder'] = slug_map[norm]
                    modified = True
                    
        if modified:
            with open(html_path, "w", encoding="utf-8") as f:
                f.write(str(soup))
            updated_files += 1
            print(f"Updated {os.path.basename(html_path)}")
            
    print(f"Updated {updated_files} files.")
    
    # Generate new i18n.js
    new_translations = {
        "ru": ru_dict_new,
        "kz": kz_dict_new,
        "en": en_dict_new
    }
    
    new_js = f"const translations = {json.dumps(new_translations, ensure_ascii=False, indent=4)};\n\n"
    
    new_js += """
function setLanguage(lang) {
    localStorage.setItem('selectedLang', lang);

    document.querySelectorAll('.lang-btn').forEach(btn => btn.classList.remove('active'));
    document.querySelectorAll(`.lang-btn[data-lang="${lang}"]`).forEach(btn => btn.classList.add('active'));

    const dict = translations[lang] || translations['ru'];

    document.querySelectorAll('[data-i18n]').forEach(el => {
        const key = el.getAttribute('data-i18n');
        if (dict[key]) {
            // We use textContent because we're translating the exact text content
            el.textContent = dict[key];
        }
    });

    document.querySelectorAll('[data-i18n-placeholder]').forEach(el => {
        const key = el.getAttribute('data-i18n-placeholder');
        if (dict[key]) {
            el.placeholder = dict[key];
        }
    });
}

function changeLanguage(langCode) {
    setLanguage(langCode);
}

document.addEventListener('DOMContentLoaded', () => {
    const savedLang = localStorage.getItem('selectedLang') || 'ru';
    if (savedLang !== 'ru') {
        setLanguage(savedLang);
    }
});
"""

    with open(i18n_path, "w", encoding="utf-8") as f:
        f.write(new_js)
        
    print("Updated i18n.js")

if __name__ == "__main__":
    main()

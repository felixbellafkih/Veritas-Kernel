import json
import os

def deep_clean():
    lex_path = 'LEXICON.json'
    with open(lex_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    for item in data['universal_functions']:
        # Si la racine contient un 'Ain, on force l'apostrophe dans le label latin
        if 'ع' in item['root']:
            parts = item['root'].split('/')
            if len(parts) > 1:
                label = parts[1].replace(')', '')
                if not label.startswith("'"):
                    # Remplace A par ' au début du nom si c'est un 'Ain
                    new_label = "'" + label if not label.startswith("A") else label.replace("A", "'", 1)
                    item['root'] = f"{parts[0]}/{new_label})"
    
    with open(lex_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    print("✨ LEXICON PURGÉ : Tous les labels 'Ain utilisent désormais le standard (').")

if __name__ == "__main__":
    deep_clean()

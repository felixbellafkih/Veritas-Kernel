import json

def final_polish():
    lex_path = 'LEXICON.json'
    if not os.path.exists(lex_path): return

    with open(lex_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    for item in data['universal_functions']:
        root_str = item['root']
        # Si la racine contient 'ع' mais que le nom après le '/' commence par 'A'
        if 'ع' in root_str and '/A' in root_str:
            item['root'] = root_str.replace('/A', "/'")
        # Cas spécifique pour le milieu des mots si nécessaire
        if 'ع' in root_str and '-A-' in root_str:
             item['root'] = root_str.replace('-A-', "---").replace('---', "-'-")

    with open(lex_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    print("✨ NETTOYAGE TERMINÉ : Le standard (') est appliqué sur tout le Lexicon.")

import os
if __name__ == "__main__":
    final_polish()

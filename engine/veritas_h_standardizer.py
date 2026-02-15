import json
import os

def h_standardization():
    path = 'LEXICON.json'
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Mise à jour de la table de transcription
    # ه -> H (Léger)
    # ح -> H. (Lourd)
    char_map = {'ه': 'H', 'ح': 'H.'}

    updates = 0
    for item in data['universal_functions']:
        raw_ar = item['root'].split('(')[0].strip().replace('-', '').replace(' ', '')
        parts = item['root'].split('(')[1].replace(')', '').strip().split('-')
        
        modified = False
        new_parts = list(parts)
        
        for i, char in enumerate(raw_ar):
            if char in char_map and i < len(new_parts):
                if new_parts[i] != char_map[char]:
                    new_parts[i] = char_map[char]
                    modified = True
        
        if modified:
            new_code = "-".join(new_parts)
            item['root'] = f"{item['root'].split('(')[0].strip()} ({new_code})"
            updates += 1

    data['version'] = "28.1.0-H-Precision"
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    
    print(f"✅ H-STANDARDISATION TERMINÉE : {updates} racines calibrées.")

if __name__ == "__main__":
    h_standardization()

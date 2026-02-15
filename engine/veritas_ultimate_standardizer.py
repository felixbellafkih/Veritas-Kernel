import json
import os

def ultimate_standardization():
    print("🔧 INITIALISATION DE LA RECONSTRUCTION TOTALE (VTS-v3)...")
    
    path = 'LEXICON.json'
    if not os.path.exists(path): return

    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # TABLE DE TRANSCRIPTION ABSOLUE
    char_map = {
        # T-SERIES
        'ت': 'T',   'ث': 'TH',  'ط': 'T.',
        # S-SERIES
        'س': 'S',   'ص': 'S.',
        # D-SERIES
        'د': 'D',   'ذ': 'DH',  'ض': 'D.',
        # Z-SERIES
        'ز': 'Z',   'ظ': 'Z.',
        
        # LE RESTE (STANDARD)
        'أ': 'A', 'إ': 'A', 'آ': 'A', 'ا': 'A', 'ء': 'A',
        'ع': "'",
        'ب': 'B', 'ج': 'J', 'ح': 'H', 'خ': 'KH',
        'ر': 'R', 'غ': 'GH', 'ف': 'F', 'ق': 'Q',
        'k': 'K', 'ك': 'K', 'l': 'L', 'ل': 'L',
        'm': 'M', 'م': 'M', 'n': 'N', 'ن': 'N',
        'h': 'H', 'ه': 'H', 'w': 'W', 'و': 'W',
        'y': 'Y', 'ي': 'Y', 'ى': 'Y', 'ة': 'T'
    }

    updates = 0
    
    for item in data['universal_functions']:
        # 1. On prend la racine arabe brute (la vérité source)
        raw_arabic = item['root'].split('(')[0].strip().replace('-', '').replace(' ', '')
        
        # 2. On reconstruit le code latin lettre par lettre
        new_code_parts = []
        valid_root = True
        
        for char in raw_arabic:
            if char in char_map:
                new_code_parts.append(char_map[char])
            else:
                # Si caractère inconnu (ex: voyelle courte), on ignore ou on flag
                pass
        
        if new_code_parts:
            # 3. Assemblage
            new_latin_code = "-".join(new_code_parts)
            
            # Reconstruction de la chaîne d'affichage (Arabe + Latin)
            # On remet les tirets dans l'arabe aussi
            arabic_dashed = "-".join(list(raw_arabic))
            new_full_string = f"{arabic_dashed} ({new_latin_code})"
            
            # 4. Comparaison et Mise à jour
            if item['root'] != new_full_string:
                # print(f"  Fix: {item['root']} -> {new_full_string}")
                item['root'] = new_full_string
                updates += 1

    data['version'] = "27.0.0-Ultimate-Phonetic"
    
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    print("-" * 50)
    print(f"✅ RECONSTRUCTION TERMINÉE.")
    print(f"📊 Racines réécrites : {updates}")
    print(f"🛡️ Intégrité : Distinction T/TH/T. | S/S. | D/DH/D. | Z/Z. garantie.")

if __name__ == "__main__":
    ultimate_standardization()

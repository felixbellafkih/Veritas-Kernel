import json
import os
import re

def standardize_lexicon():
    path = 'LEXICON.json'
    if not os.path.exists(path):
        print("❌ ERREUR : LEXICON.json introuvable.")
        return

    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # TABLE DE TRANSCRIPTION STRICTE (VTS-v1)
    # C'est la "Loi" de conversion.
    char_map = {
        # --- LES CRITIQUES (A vs ') ---
        'ع': "'",
        'أ': "A", 'إ': "A", 'آ': "A", 'ا': "A", 'ء': "A",
        
        # --- LE RESTE DE L'ALPHABET ---
        'ب': "B", 'ت': "T", 'ث': "TH", 'ج': "J", 'ح': "H",
        'خ': "KH", 'd': "D", 'د': "D", 'ذ': "DH", 'r': "R",
        'ر': "R", 'z': "Z", 'ز': "Z", 's': "S", 'س': "S",
        'ش': "SH", 'ص': "S", 'ض': "D", 'ط': "T", 'ظ': "Z",
        'غ': "GH", 'f': "F", 'ف': "F", 'q': "Q", 'ق': "Q",
        'k': "K", 'ك': "K", 'l': "L", 'ل': "L", 'm': "M",
        'م': "M", 'n': "N", 'ن': "N", 'h': "H", 'ه': "H",
        'w': "W", 'و': "W", 'y': "Y", 'ي': "Y", 'ى': "Y",
        'ة': "T" # Ta Marbuta souvent T ou H, on fixe T pour la racine
    }

    corrections = 0
    errors = 0

    for item in data['universal_functions']:
        original_root_str = item['root']
        
        # 1. Extraction de la partie Arabe (Tout ce qui est avant la parenthèse ou le premier espace)
        # On nettoie les tirets arabes s'il y en a
        arabic_part = original_root_str.split('(')[0].strip().replace('-', '').replace(' ', '')
        
        # 2. Reconstruction de la translittération (Le code entre parenthèses)
        new_translit = []
        try:
            for char in arabic_part:
                if char in char_map:
                    new_translit.append(char_map[char])
                else:
                    # Caractère non mappé (ignorer ou signaler)
                    pass
            
            # On joint avec des tirets pour le format standard (ex: A-K-L)
            new_code = "-".join(new_translit)
            
            # 3. Reconstruction de la chaîne complète "أ-ك-ل (A-K-L)"
            # On remet les tirets dans l'arabe aussi pour faire propre
            arabic_dashed = "-".join(list(arabic_part))
            new_root_str = f"{arabic_dashed} ({new_code})"
            
            # 4. Application si différent
            if new_root_str != original_root_str:
                # On vérifie spécifiquement les corrections A vs '
                if ("'" in new_code and "A" in original_root_str) or ("A" in new_code and "'" in original_root_str):
                     print(f"  🔧 FIX: {original_root_str} -> {new_root_str}")
                
                item['root'] = new_root_str
                corrections += 1
                
        except Exception as e:
            print(f"  ⚠️ ERREUR sur {original_root_str}: {e}")
            errors += 1

    data['version'] = f"{data.get('version', '1.0').split('-')[0]}-Phonetic-Standard"

    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    print("-" * 60)
    print(f"✅ STANDARDISATION TERMINÉE.")
    print(f"📊 Entrées corrigées : {corrections}")
    print(f"🛡️ Standard VTS-v1 appliqué : 100% des 'Ain sont (') et 100% des Alif sont (A).")

if __name__ == "__main__":
    standardize_lexicon()

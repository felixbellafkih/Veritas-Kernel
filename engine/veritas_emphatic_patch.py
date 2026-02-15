import json
import os

def emphatic_patch():
    print("🔧 INITIALISATION DU PATCH EMPHATIQUE (S vs S. / T vs T.)...")
    
    path = 'LEXICON.json'
    if not os.path.exists(path): return

    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # TABLE DE MAPPING DES EMPHATIQUES
    # Si la racine arabe contient ces lettres, la clé latine doit avoir un "."
    emphatic_map = {
        'ص': 'S',  # Deviendra S.
        'ط': 'T',  # Deviendra T.
        'ظ': 'Z',  # Deviendra Z.
        'ض': 'D'   # Deviendra D.
    }

    corrections = 0
    
    for item in data['universal_functions']:
        original_root = item['root']
        # Extraction Arabe (partie gauche) et Latin (partie droite)
        # Format attendu : "ص-ب-ر (S-B-R)"
        try:
            parts = original_root.split('(')
            arabic_part = parts[0].strip().replace('-', '') # "صبر"
            latin_code = parts[1].replace(')', '').strip()  # "S-B-R"
            
            new_latin_code = latin_code
            modified = False
            
            # Reconstruction du code latin lettre par lettre
            # On scanne l'arabe pour voir s'il y a des emphatiques
            rebuilt_code_list = list(latin_code.split('-'))
            
            # C'est complexe car la longueur arabe = longueur latine (trilitère)
            # On suppose un alignement 1 pour 1
            if len(arabic_part) == len(rebuilt_code_list):
                for i, char in enumerate(arabic_part):
                    if char in emphatic_map:
                        # Si la lettre latine n'a pas déjà de point
                        if '.' not in rebuilt_code_list[i]:
                            rebuilt_code_list[i] = rebuilt_code_list[i] + "."
                            modified = True
            
            if modified:
                new_latin_code = "-".join(rebuilt_code_list)
                new_root_str = f"{parts[0].strip()} ({new_latin_code})"
                
                # Application
                item['root'] = new_root_str
                corrections += 1
                # print(f"  Fix: {original_root} -> {new_root_str}")

        except Exception as e:
            continue

    data['version'] = "26.0.0-Emphatic-Split"
    
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    print("-" * 50)
    print(f"✅ PATCH TERMINÉ.")
    print(f"📊 Corrections appliquées : {corrections}")
    print(f"🛡️ Distinction S (Flux) vs S. (Structure) activée.")

if __name__ == "__main__":
    emphatic_patch()

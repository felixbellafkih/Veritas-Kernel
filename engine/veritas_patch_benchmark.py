import json
import os

def apply_patch():
    # 1. Injection des Racines Manquantes
    new_roots = [
        {"root": "ر-س-ي (Rasiya)", "logic_function": "System_Anchor_Stabilizer", "description": "Module de stabilisation empêchant les vibrations du système (Fixed Anchor)."},
        {"root": "ع-و-ن ('Awn)", "logic_function": "System_Support_Assist", "description": "Processus d'assistance ou d'augmentation de capacité (Help/Support)."},
        {"root": "ف-ت-ي (Fata)", "logic_function": "New_Process_Instance", "description": "Instance fraîchement instanciée, sans cache ni corruption (Youth)."},
        {"root": "ب-د-و (Bada)", "logic_function": "Output_Rendering", "description": "Affichage ou manifestation d'une variable cachée (Render)."},
        {"root": "س-و-ي (Sawwa)", "logic_function": "System_Calibration", "description": "Égalisation et calibrage parfait des ressources (Equalization)."}
    ]

    lex_path = 'LEXICON.json'
    with open(lex_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    current_roots = {item['root'].split('(')[0].strip(): item for item in data['universal_functions']}
    
    added = 0
    for entry in new_roots:
        key = entry['root'].split('(')[0].strip()
        # On force l'écrasement ou l'ajout
        current_roots[key] = entry
        # On ajoute aussi une entrée pour la racine pure si nécessaire
        data['universal_functions'].append(entry)
        added += 1

    # 2. Nettoyage des doublons (Deduplication)
    unique_data = {v['root']: v for v in data['universal_functions']}.values()
    data['universal_functions'] = list(unique_data)

    data['version'] = "23.0.0-Benchmark-Patched"
    
    with open(lex_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    
    print(f"✅ PATCH APPLIQUÉ : +{added} Racines Critiques.")
    print(f"🔧 Total Racines : {len(data['universal_functions'])}")

if __name__ == "__main__":
    apply_patch()

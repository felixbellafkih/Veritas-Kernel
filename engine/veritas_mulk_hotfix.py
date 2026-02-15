import json
import os

def mulk_hotfix():
    path = 'LEXICON.json'
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Injections chirurgicales
    hotfixes = [
        {"root": "ي-د-ي (Y-D-Y)", "logic_function": "Manual_Control_Interface", "description": "Interface d'accès direct pour la manipulation des registres (Hand)."},
        {"root": "ش-ي-أ (SH-Y-A)", "logic_function": "Object_Instantiation", "description": "Entité de donnée instanciée dans l'espace utilisateur (Thing)."}
    ]

    current_roots = {item['root'].split('(')[0].strip(): item for item in data['universal_functions']}
    
    for fix in hotfixes:
        key_ar = fix['root'].split('(')[0].strip()
        current_roots[key_ar] = fix

    data['universal_functions'] = list(current_roots.values())
    data['version'] = "1.2.1-Mulk-Hotfix"

    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    
    print("🔧 HOTFIX APPLIQUÉ : Y-D-Y et SH-Y-A synchronisés.")

if __name__ == "__main__":
    mulk_hotfix()

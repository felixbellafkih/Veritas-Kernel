import json
import os

def performance_fix():
    path = 'LEXICON.json'
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Injections pour Al-Mulk 67:2 et 67:3
    new_vectors = [
        {"root": "ح-س-ن (H.-S-N)", "logic_function": "Optimization_Peak", "description": "Niveau d'efficacité maximale et de pureté de l'exécution (Excellence)."},
        {"root": "ب-ل-و (B-L-W)", "logic_function": "System_Stress_Test", "description": "Procédure d'audit et de mise à l'épreuve des instances (Trial)."},
        {"root": "ط-ب-ق (T.-B-Q)", "logic_function": "Hardware_Layering", "description": "Architecture en couches physiques superposées et alignées (Layers)."},
        {"root": "س-ب-ع (S-B-')", "logic_function": "Cycle_Constant_7", "description": "Nombre de partitions système ou couches d'infrastructure (Seven)."}
    ]

    current_roots = {item['root'].split('(')[0].strip(): item for item in data['universal_functions']}
    
    for vec in new_vectors:
        key_ar = vec['root'].split('(')[0].strip()
        current_roots[key_ar] = vec

    data['universal_functions'] = list(current_roots.values())
    data['version'] = "29.0.0-Performance-Infrastructure"

    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    
    print("🔧 CALIBRAGE TERMINÉ : H.-S-N, B-L-W et T.-B-Q sont en ligne.")

if __name__ == "__main__":
    performance_fix()

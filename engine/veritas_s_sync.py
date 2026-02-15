import json
import os

def s_sync():
    path = 'LEXICON.json'
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    new_vectors = [
        {"root": "س-ب-ح (S-B-H)", "logic_function": "Orbital_Navigation_Flow", "description": "Navigation fluide ou dérive orbitale (To swim/glorify)."},
        {"root": "ص-ب-ح (S.-B-H)", "logic_function": "System_Initialization_Dawn", "description": "Phase d'amorçage ou de démarrage de la visibilité (Dawn/Morning)."}
    ]
    
    current_roots = {item['root'].split('(')[0].strip(): item for item in data['universal_functions']}
    for vec in new_vectors:
        current_roots[vec['root'].split('(')[0].strip()] = vec
        
    data['universal_functions'] = list(current_roots.values())
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    print("✅ S-SERIES SYNCHRONIZED.")

if __name__ == "__main__":
    s_sync()

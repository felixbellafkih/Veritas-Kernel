import json
import os

def export_inventory():
    path = 'LEXICON.json'
    if not os.path.exists(path):
        print("❌ ERREUR : LEXICON.json introuvable.")
        return

    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    roots = data.get('universal_functions', [])
    version = data.get('version', 'Unknown')
    
    print(f"--- DÉBUT DU DUMP VERITAS ({len(roots)} Racines) ---")
    print(f"VERSION : {version}")
    
    # Tri alphabétique pour faciliter l'analyse
    sorted_roots = sorted(roots, key=lambda x: x['root'])
    
    for i, item in enumerate(sorted_roots, 1):
        # Format compact : [N] RACINE : FONCTION
        # Nettoyage pour affichage
        clean_root = item['root'].split('(')[0].strip()
        transcription = item['root'].split('/')[1].replace(')', '') if '/' in item['root'] else "N/A"
        print(f"[{i:03d}] {clean_root:<10} ({transcription:<10}) : {item['logic_function']}")

    print(f"--- FIN DU DUMP ---")

if __name__ == "__main__":
    export_inventory()

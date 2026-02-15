import json
import sys

# Forcer l'UTF-8 pour l'affichage de l'arabe
if sys.stdout.encoding != 'UTF-8':
    sys.stdout.reconfigure(encoding='utf-8')

def list_active_roots():
    lexicon_path = 'LEXICON.json'
    try:
        with open(lexicon_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        all_functions = data.get('universal_functions', [])
        
        # Filtrage chirurgical : on ignore les slots vides
        active_roots = [
            f for f in all_functions 
            if "RESERVED" not in str(f.get('logic_function', '')) 
            and "SLOT" not in str(f.get('root', ''))
        ]

        print(f"\n--- AUDIT DES RACINES ACTIVES (SIGNAL PUR) ---")
        print(f"VERSION : {data.get('version', 'N/A')}")
        print(f"DENSITÉ : {len(active_roots)} racines réelles.\n")
        print(f"{'IDX':<5} | {'MATRICE ARABE':<20} | {'FONCTION'}")
        print("-" * 70)

        for i, entry in enumerate(active_roots, 1):
            root = entry.get('root', 'N/A')
            func = entry.get('logic_function', 'N/A')
            print(f"[{i:03}] {root:<20} | {func}")

        print("-" * 70)
        print(f"FIN DE L'AUDIT - {len(active_roots)} NŒUDS OPÉRATIONNELS.")

    except Exception as e:
        print(f"❌ ERREUR SYSTÈME : {e}")

if __name__ == "__main__":
    list_active_roots()

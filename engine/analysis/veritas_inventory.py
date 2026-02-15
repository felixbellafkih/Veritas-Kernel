import json
import sys

# Forçage de l'encodage pour éviter les erreurs sur Windows/MinGW
sys.stdout.reconfigure(encoding='utf-8')

def list_all_roots():
    lexicon_path = 'LEXICON.json'
    
    try:
        with open(lexicon_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        functions = data.get('universal_functions', [])
        
        print(f"\n--- INVENTAIRE DU KERNEL VERITAS ({data.get('version', 'v17.8.0')}) ---")
        print(f"TOTAL : {len(functions)}/1800 SLOTS OCCUPÉS\n")
        
        # Séparation pour clarté : Racines Réelles vs Slots Réservés
        real_roots = [f for f in functions if "RESERVED" not in f['logic_function']]
        reserved_slots = [f for f in functions if "RESERVED" in f['logic_function']]

        print(f"DENSITÉ DU SIGNAL : {len(real_roots)} RACINES ACTIVES")
        print("-" * 60)
        
        # On affiche tout, trié par le texte de la racine
        functions.sort(key=lambda x: x['root'])
        
        for i, entry in enumerate(functions, 1):
            root = entry.get('root', 'N/A')
            func = entry.get('logic_function', 'UNDEFINED')
            
            # Formatage aligné pour la lisibilité
            # L'index i suit l'ordre de la liste triée
            print(f"[{i:03}] {root:<25} | {func}")
            
        print("-" * 60)
        print(f"FIN DE L'INVENTAIRE - ÉTAT : {'STABLE' if len(real_roots) >= 1000 else 'EN EXPANSION'}")

    except FileNotFoundError:
        print("❌ ERREUR : Fichier LEXICON.json introuvable.")
    except Exception as e:
        print(f"❌ ERREUR SYSTÈME : {e}")

if __name__ == "__main__":
    list_all_roots()

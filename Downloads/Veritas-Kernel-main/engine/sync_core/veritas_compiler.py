import json
import sys
import os

def compile_sequence(text):
    try:
        # --- RÉALIGNEMENT GÉOGRAPHIQUE ---
        # Détermine le chemin de la racine : engine/sync_core/ -> engine/ -> racine/
        current_dir = os.path.dirname(os.path.abspath(__file__))
        root_dir = os.path.dirname(os.path.dirname(current_dir))
        lexicon_path = os.path.join(root_dir, 'LEXICON.json')
        
        with open(lexicon_path, 'r', encoding='utf-8') as f:
            lexicon = json.load(f)['universal_functions']
        
        tokens = text.upper().split()
        matches = 0
        
        print(f"\n--- RAPPORT DE COMPILATION VERITAS v8.2.0 ---")

        for token in tokens:
            # Recherche précise de la racine par son étiquette latine
            match = next((item for item in lexicon if f"({token}/" in item['root'] or f"/{token})" in item['root'] or token == item['root'].split('(')[-1].split('/')[0]), None)
            
            if match:
                matches += 1
                arabic_root = match['root'].split(' ')[0]
                # Nettoyage des fonctions doublées (Optimisation Veritas)
                func = " -> ".join(list(dict.fromkeys(match['logic_function'].split('_'))))
                print(f" -> {arabic_root:<10} ({token:<8}) => {func}")
            else:
                print(f" -> !! NOISE !! ({token:<8}) => UNKNOWN_SIGNAL")

        purity = (matches / len(tokens)) * 100 if tokens else 0
        print(f"\nTokens : {len(tokens)} | Signaux : {matches} | Pureté : {purity:.2f}%")
        print(f"État : {'IMMUTABLE' if purity == 100 else 'DÉGRADÉ'}")
        print(f"---------------------------------------------")
        
    except FileNotFoundError:
        print(f"❌ ERREUR : Base de données introuvable à l'emplacement : {lexicon_path}")
    except Exception as e:
        print(f"❌ ERREUR SYSTÈME : {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        compile_sequence(sys.argv[1])
    else:
        print("Usage: python engine/sync_core/veritas_compiler.py 'TOKEN1 TOKEN2'")
import json
import sys

def compile_sequence(text):
    try:
        with open('LEXICON.json', 'r', encoding='utf-8') as f:
            lexicon = json.load(f)['universal_functions']
        
        tokens = text.upper().split()
        matches = 0
        
        print(f"\n--- RAPPORT DE COMPILATION VERITAS v8.1.5 ---")

        for token in tokens:
            # Recherche précise de la racine par son étiquette latine
            match = next((item for item in lexicon if f"({token}/" in item['root'] or f"/{token})" in item['root'] or token == item['root'].split('(')[-1].split('/')[0]), None)
            
            if match:
                matches += 1
                arabic_root = match['root'].split(' ')[0]
                # Nettoyage des fonctions doublées par les fusions
                func = " -> ".join(list(dict.fromkeys(match['logic_function'].split('_'))))
                print(f" -> {arabic_root:<10} ({token:<8}) => {func}")
            else:
                print(f" -> !! NOISE !! ({token:<8}) => UNKNOWN_SIGNAL")

        purity = (matches / len(tokens)) * 100 if tokens else 0
        print(f"\nTokens : {len(tokens)} | Signaux : {matches} | Pureté : {purity:.2f}%")
        print(f"État : {'IMMUTABLE' if purity == 100 else 'DÉGRADÉ'}")
        print(f"---------------------------------------------")
        
    except Exception as e:
        print(f"❌ ERREUR SYSTÈME : {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        compile_sequence(sys.argv[1])
    else:
        print("Usage: python engine/veritas_compiler.py 'TOKEN1 TOKEN2'")

import json
import sys
import os
import re

def normalize(text):
    return re.sub(r'[^A-Z0-9\']', '', text.upper())

def compile_veritas(input_string):
    lex_path = 'LEXICON.json'
    if not os.path.exists(lex_path):
        print("❌ CRITICAL ERROR: LEXICON.json MISSING")
        return

    with open(lex_path, 'r', encoding='utf-8') as f:
        lexicon = json.load(f)['universal_functions']

    tokens = input_string.split()
    results = []
    signals_count = 0

    for t in tokens:
        clean_t = normalize(t)
        # Recherche exacte dans le noyau
        match = next((item for item in lexicon if clean_t in normalize(item['root'])), None)
        
        if match:
            signals_count += 1
            # Formatage spécifique demandé : Racine (Label) => Logic_Chain
            # Note: On extrait la partie fonctionnelle pour le mapping
            logic_chain = match['logic_function'].replace('_', ' -> ')
            results.append(f" -> {match['root'].split(' ')[0]:<12} ({clean_t:<8}) => {logic_chain}")
        else:
            results.append(f" -> !! NOISE !! ({clean_t:<8}) => UNKNOWN_SIGNAL")

    # Calcul de la pureté
    purity = (signals_count / len(tokens)) * 100 if tokens else 0
    state = "OPTIMAL" if purity == 100 else "DÉGRADÉ" if purity > 0 else "CRITICAL_FAILURE"

    print(f"\n --- RAPPORT DE COMPILATION VERITAS v8.1.5 --- ")
    for res in results:
        print(res)
    print(f"\n Tokens : {len(tokens)} | Signaux : {signals_count} | Pureté : {purity:.2f}% ")
    print(f" État : {state} ")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        compile_veritas(" ".join(sys.argv[1:]))
    else:
        print("Usage: python engine/veritas_compiler.py \"ROOT1 ROOT2 ...\"")

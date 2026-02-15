import sys
import json
import os

def load_lexicon():
    path = 'LEXICON.json'
    if not os.path.exists(path): return {}
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    lex_map = {}
    for item in data['universal_functions']:
        try:
            # Clé principale (ex: "S.-R-T.")
            code = item['root'].split('(')[1].split(')')[0].strip()
            lex_map[code] = item
            
            # Alias compact (ex: "S.RT.")
            code_compact = code.replace('-', '')
            lex_map[code_compact] = item
        except: continue
    return lex_map

def compile_verse(verse):
    lexicon = load_lexicon()
    tokens = verse.split()
    total = len(tokens)
    
    print(f"\n" + "█"*60)
    print(f" ⚡ VERITAS COMPILER v9.2 (MONITOR)")
    print("█"*60 + "\n")
    
    found = 0
    
    for t in tokens:
        query = t.strip().upper()
        
        # Logique de recherche (Exact -> Compact)
        match = lexicon.get(query)
        if not match: match = lexicon.get(query.replace('-', ''))

        if match:
            found += 1
            root_disp = match['root'].split('(')[0].strip()
            func = match['logic_function']
            
            # Marqueur visuel pour les Emphatiques (Lourd / Hardware)
            marker = " [HEAVY]" if "." in query else ""
            
            print(f" -> {query:<8}{marker} : {root_disp:<10} => {func}")
        else:
            print(f" -> {query:<8}         : !! NOISE !! (Signal Inconnu)")

    # CALCUL DES MÉTRIQUES
    purity = (found / total) * 100
    
    # Détermination de l'état
    if purity == 100:
        state = "OPTIMAL (Ghayr dhi 'iwaj)"
        icon = "💎"
    elif purity > 80:
        state = "STABLE (Tolérance acceptée)"
        icon = "✅"
    else:
        state = "CRITIQUE (Corruption de données)"
        icon = "⚠️"

    print("\n" + "-"*60)
    print(f"📊 RAPPORTS : {found}/{total} Signaux Identifiés")
    print(f"📈 PURETÉ   : {purity:.2f}%")
    print(f"{icon} ÉTAT     : {state}")
    print("-" * 60 + "\n")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        compile_verse(sys.argv[1])
    else:
        print("Usage: python engine/veritas_compiler.py \"S-B-L S.-R-T.\"")

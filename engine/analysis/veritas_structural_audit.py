import json
import sys

def audit(input_roots):
    try:
        with open('LEXICON.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
    except Exception as e:
        print(f"❌ ERREUR LECTURE : {e}")
        return

    # DÉTECTION INTELLIGENTE DE LA STRUCTURE
    lexicon = []
    if isinstance(data, list):
        lexicon = data
        print(f"--- INFO : Format LISTE détecté ({len(lexicon)} entrées) ---")
    elif isinstance(data, dict):
        # On cherche une clé qui contient une liste
        print(f"--- INFO : Format DICTIONNAIRE détecté (Clés: {list(data.keys())}) ---")
        if 'roots' in data and isinstance(data['roots'], list):
            lexicon = data['roots']
        elif 'entries' in data and isinstance(data['entries'], list):
            lexicon = data['entries']
        else:
            # Fallback : on cherche la première liste qu'on trouve
            for key, val in data.items():
                if isinstance(val, list):
                    lexicon = val
                    print(f"--- INFO : Utilisation de la clé '{key}' ---")
                    break
    
    if not lexicon:
        print("❌ ERREUR : Aucune liste de racines trouvée dans le JSON.")
        return

    found_items = []
    missing = []
    
    for root_input in input_roots:
        target = root_input.replace('-', '').upper()
        match_found = False
        
        for item in lexicon:
            # Protection contre les items qui ne sont pas des dictionnaires
            if not isinstance(item, dict):
                continue
                
            root_text = item.get('root', '').replace('-', '').upper()
            if target in root_text:
                found_items.append(item)
                match_found = True
                break
        
        if not match_found:
            missing.append(root_input)

    total = len(input_roots)
    purity = (len(found_items) / total) * 100 if total > 0 else 0
    
    print(f"\n--- RAPPORT VERITAS v7.3.0 (UNIVERSAL) ---")
    print(f"Tokens : {total} | Signaux : {len(found_items)} | Pureté : {purity:.2f}%")
    
    for item in found_items:
        print(f" -> {item.get('root', '???')} => {item.get('logic_function', '???')}")
    
    if missing:
        print(f"⚠️ MISSING/NOISE : {missing}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        audit(sys.argv[1].split())
    else:
        print("Usage: python engine/veritas_structural_audit.py 'ROOT1 ROOT2'")
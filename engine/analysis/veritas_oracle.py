import json
import sys
import os
import re

def normalize(text):
    return re.sub(r'[^A-Z0-9\']', '', text.upper())

def query_oracle(token):
    try:
        base_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        lexicon_path = os.path.join(base_path, 'LEXICON.json')
        
        with open(lexicon_path, 'r', encoding='utf-8') as f:
            lexicon = json.load(f)['universal_functions']
        
        raw_target = normalize(token)
        # Test 1: Recherche littérale (ex: MITHAQ ou QASAS)
        match = next((item for item in lexicon if raw_target in normalize(item['root'])), None)
        
        # Test 2: Si échec, tentative avec standard 'Ain (si A est présent)
        if not match and "A" in raw_target:
            alt_target = raw_target.replace("A", "'")
            match = next((item for item in lexicon if alt_target in normalize(item['root'])), None)
        
        if match:
            print(f"\n--- RÉPONSE ORACLE VERITAS v8.3.4 ---")
            print(f"IDENTIFIANT : {match['root']}")
            print(f"FONCTION    : {match['logic_function']}")
            print(f"DESCRIPTION : {match['description']}")
            print(f"STATUT      : SIGNAL STABLE")
            print(f"------------------------------------")
        else:
            print(f"\n❌ SIGNAL INCONNU : '{token}' (Aucune correspondance physique ou logique)")
            
    except Exception as e:
        print(f"❌ ERREUR SYSTÈME : {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        query_oracle(sys.argv[1])
    else:
        print("Usage: python engine/analysis/veritas_oracle.py [ROOT_TOKEN]")

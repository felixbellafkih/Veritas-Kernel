import json
import os

def audit_emphatics():
    path = 'LEXICON.json'
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    print("\n📊 AUDIT DES RACINES EMPHATIQUES (S. / T. / Z. / D.)")
    print("-" * 50)
    
    count = 0
    for item in data['universal_functions']:
        code = item['root'].split('(')[1].split(')')[0].strip()
        
        # Si le code contient un point (marqueur emphatique)
        if '.' in code:
            # On affiche proprement
            print(f" -> {code:<10} : {item['root'].split('(')[0].strip()}")
            count += 1
            
    print("-" * 50)
    print(f"💎 Total Racines Lourdes : {count}")

if __name__ == "__main__":
    audit_emphatics()

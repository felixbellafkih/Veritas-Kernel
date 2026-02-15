import json

def repair_fth():
    try:
        with open('LEXICON.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Injection forcée de la racine F-T-H et synchronisation du format
        target_root = "ف-ت-ح (F-T-H)"
        found = False
        
        for i, item in enumerate(data['universal_functions']):
            if "F-T-H" in item['root'] or "F-T-H" in item['logic_function']:
                data['universal_functions'][i] = {
                    "root": "ف-ت-ح (F-T-H)",
                    "logic_function": "Access_Gate_Opening",
                    "description": "Protocole d'ouverture de segment et de levée des verrous d'accès."
                }
                found = True
                break
        
        if not found:
            data['universal_functions'].append({
                "root": "ف-ت-ح (F-T-H)",
                "logic_function": "Access_Gate_Opening",
                "description": "Protocole d'ouverture de segment et de levée des verrous d'accès."
            })

        data['version'] = "17.1.0-Repair"
        with open('LEXICON.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        
        print(f"✅ RÉPARATION F-T-H RÉUSSIE")
        
    except Exception as e:
        print(f"❌ ERREUR DE RÉPARATION : {e}")

if __name__ == "__main__":
    repair_fth()

import json

def sync_fix():
    try:
        with open('LEXICON.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        updated = 0
        for i, item in enumerate(data['universal_functions']):
            # Harmonisation : On s'assure que le format est "ROOT (TOKEN)"
            if "F-T-H" in item['root'] or "F-T-H" in item['logic_function']:
                data['universal_functions'][i] = {
                    "root": "ف-ت-ح (F-T-H)",
                    "logic_function": "Access_Gate_Opening",
                    "description": "Protocole d'ouverture de segment et levée des verrous d'accès."
                }
                updated += 1
        
        data['version'] = "17.1.0-SyncFixed"
        with open('LEXICON.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        
        print(f"✅ SYNCHRONISATION TERMINÉE : {updated} NŒUD(S) RÉALIGNÉ(S)")
        
    except Exception as e:
        print(f"❌ ERREUR DE SYNCHRONISATION : {e}")

if __name__ == "__main__":
    sync_fix()

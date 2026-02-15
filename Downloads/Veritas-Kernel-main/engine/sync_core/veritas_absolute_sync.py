import json

def absolute_sync():
    try:
        with open('LEXICON.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Mapping de correction pour les racines de test
        corrections = {
            "F-T-H": {"root": "ف-ت-ح (F-T-H)", "func": "Access_Gate_Opening"},
            "DH-K-R": {"root": "ذ-ك-ر (DH-K-R)", "func": "Memory_Active_Recall"},
            "N-S-R": {"root": "ن-ص-ر (N-S-R)", "func": "System_Support_Boost"}
        }
        
        for i, item in enumerate(data['universal_functions']):
            # Nettoyage et normalisation de chaque entrée
            for key, val in corrections.items():
                if key in item['root'] or key in item.get('logic_function', ''):
                    data['universal_functions'][i] = {
                        "root": val["root"],
                        "logic_function": val["func"],
                        "description": f"Protocole synchronisé pour {key}"
                    }
        
        data['version'] = "17.2.0-Absolute"
        with open('LEXICON.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        
        print("✅ SYNCHRONISATION ABSOLUE TERMINÉE")
        
    except Exception as e:
        print(f"❌ ERREUR SYSTÈME : {e}")

if __name__ == "__main__":
    absolute_sync()

import json

def final_sync():
    try:
        with open('LEXICON.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Mapping strict pour restaurer les piliers
        piliers = {
            "F-T-H": "ف-ت-ح (F-T-H)",
            "DH-K-R": "ذ-ك-ر (DH-K-R)",
            "N-S-R": "ن-ص-ر (N-S-R)"
        }
        
        for i, item in enumerate(data['universal_functions']):
            for key, full_root in piliers.items():
                if key in item['root']:
                    data['universal_functions'][i]['root'] = full_root
        
        data['version'] = "17.3.0-FinalSync"
        with open('LEXICON.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        
        print("✅ SYNCHRONISATION FINALE EXÉCUTÉE")
        
    except Exception as e:
        print(f"❌ ERREUR : {e}")

if __name__ == "__main__":
    final_sync()

import json

def raw_sync():
    try:
        with open('LEXICON.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        for i, item in enumerate(data['universal_functions']):
            # On extrait uniquement le code type X-Y-Z
            import re
            match = re.search(r'([A-Z]-[A-Z]-[A-Z])', item['root'])
            if match:
                # ON TESTE LE FORMAT BRUT : "F-T-H"
                data['universal_functions'][i]['root'] = match.group(1)
        
        data['version'] = "17.5.0-Raw"
        with open('LEXICON.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        
        print("⚠️ RÉALIGNEMENT BRUT EFFECTUÉ (ARABE MASQUÉ)")
        
    except Exception as e:
        print(f"❌ ERREUR : {e}")

if __name__ == "__main__":
    raw_sync()

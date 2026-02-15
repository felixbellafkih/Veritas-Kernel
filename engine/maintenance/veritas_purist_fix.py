import json
import re

def purist_fix():
    lexicon_path = 'LEXICON.json'
    token_pattern = r'([A-Z\']-[A-Z]-[A-Z/]+|[A-Z]-[A-Z]-[A-Z])'
    
    try:
        with open(lexicon_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        updated = 0
        for i, entry in enumerate(data['universal_functions']):
            root_text = entry.get('root', '')
            # Extraction du signal pur (Token)
            match = re.search(token_pattern, root_text)
            
            if match:
                # On remplace l'entrée par le TOKEN PUR uniquement
                # Suppression de l'arabe et des parenthèses pour l'alignement moteur
                data['universal_functions'][i]['root'] = match.group(1)
                updated += 1
        
        with open(lexicon_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        
        print(f"✅ ALIGNEMENT PURISTE TERMINÉ : {updated} racines normalisées.")
        print("⚠️ NOTE : L'arabe est déplacé dans la logique interne (Signal Brut).")

    except Exception as e:
        print(f"❌ ERREUR : {e}")

if __name__ == "__main__":
    purist_fix()

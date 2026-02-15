import json
import sys

# Forçage UTF-8 pour l'affichage terminal
if sys.stdout.encoding != 'UTF-8':
    try: sys.stdout.reconfigure(encoding='utf-8')
    except AttributeError: pass

def repair_red_lines():
    lexicon_path = 'LEXICON.json'
    updates = [
        {
            "root": "ح-ي-ي (H-Y-Y)",
            "logic_function": "Active_Runtime_State",
            "description": "Initialisation du flux vital dans une instance ou un processus inerte."
        },
        {
            "root": "ج-و-ب (J-W-B)",
            "logic_function": "Response_Protocol",
            "description": "Protocole de réponse finalisant une requête entre deux entités."
        }
    ]

    try:
        with open(lexicon_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        functions = data.get('universal_functions', [])
        updated_count = 0

        for up in updates:
            token = up['root'].split(' ')[1] # Extrait (H-Y-Y) ou (J-W-B)
            found = False
            
            # 1. Tentative de mise à jour d'une version corrompue
            for i, entry in enumerate(functions):
                if token in entry.get('root', ''):
                    functions[i] = up
                    updated_count += 1
                    found = True
                    break
            
            # 2. Si non trouvé, injection dans le premier slot RESERVED
            if not found:
                for i, entry in enumerate(functions):
                    if "RESERVED" in entry.get('logic_function', ''):
                        functions[i] = up
                        updated_count += 1
                        break

        data['universal_functions'] = functions
        with open(lexicon_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        
        print(f"✅ RÉPARATION TERMINÉE : {updated_count} nœuds synchronisés.")

    except Exception as e:
        print(f"❌ ERREUR CRITIQUE : {e}")

if __name__ == "__main__":
    repair_red_lines()

import json

def apply_hotfix():
    print("🚑 APPLICATION DU HOTFIX J-R-M...")
    
    try:
        with open('LEXICON.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
    except:
        print("❌ Erreur lecture LEXICON.json")
        return

    # La définition propre
    target_root = "J-R-M"
    new_entry = {
        "root": target_root,
        "logic_function": "Criminal_Log_Entry",
        "description": "Enregistrement d'une action illégale majeure dans le journal système (Crime)."
    }

    # On supprime toute ancienne trace de J-R-M ou Jarama
    data['universal_functions'] = [item for item in data['universal_functions'] if "Jarama" not in item['root'] and item['root'] != "J-R-M"]
    
    # On ajoute la propre
    data['universal_functions'].append(new_entry)
    
    # Tri
    data['universal_functions'].sort(key=lambda x: x['root'])

    with open('LEXICON.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
        
    print(f"✅ HOTFIX APPLIQUÉ : {target_root} est maintenant actif.")

if __name__ == "__main__":
    apply_hotfix()

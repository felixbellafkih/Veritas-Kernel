import json
import os

file_path = 'LEXICON.json'

def migrate_structure():
    if not os.path.exists(file_path):
        print("❌ ERREUR : Base de données introuvable.")
        return

    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    count = 0
    # On ajoute le champ 'binary_pair' s'il n'existe pas
    for item in data['universal_functions']:
        if 'binary_pair' not in item:
            item['binary_pair'] = None # Par défaut, pas de lien
            count += 1
    
    # Sauvegarde
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    print(f"✅ STRUCTURE MISE À JOUR : {count} entrées ont reçu le champ 'binary_pair'.")

if __name__ == "__main__":
    migrate_structure()

import json
import os

file_path = 'LEXICON.json'

if not os.path.exists(file_path):
    print("❌ ERREUR : Base de données introuvable.")
    exit()

with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

found = False
for item in data['universal_functions']:
    # On cherche l'ancienne version
    if item['root'] == "S-Y-T-R":
        item['root'] = "S-Y-T.-R"  # Correction
        found = True
        print(f"✅ CORRECTION APPLIQUÉE : S-Y-T-R -> {item['root']}")
        break

if found:
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    print("💾 BASE DE DONNÉES SAUVEGARDÉE.")
else:
    print("⚠️ AVERTISSEMENT : Racine S-Y-T-R non trouvée (déjà corrigée ?).")


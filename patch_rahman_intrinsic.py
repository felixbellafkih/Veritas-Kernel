import json

file_path = 'LEXICON.json'

with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# MISE À JOUR CIBLÉE
target_root = "R-H-M-N"

new_definition = {
    "root": "R-H-M-N", "arabic": "رحمن",
    "logic_function": "SYSTEM_ARCHITECTURE // INTRINSIC_STATE",
    "description": "La Matrice dans son état intrinsèque (Nature par défaut) et d'expansion maximale (Saturation A-N). Englobe toute la création sans distinction. C'est le 'Système d'Exploitation' universel avant toute requête spécifique.",
    "binary_pair": "GH-D.-B" # Ghadab (Colère/Saturation opposée)
}

updated = False
for item in data['universal_functions']:
    if item['root'] == target_root:
        item.update(new_definition)
        updated = True
        break

if not updated:
    data['universal_functions'].append(new_definition)

with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=4, ensure_ascii=False)

print(f"✅ DÉFINITION MISE À JOUR : {target_root} -> ÉTAT INTRINSÈQUE.")

import json

file_path = 'LEXICON.json'

with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# MISE A JOUR SYSTÉMIQUE
updates = [
    {
        "root": "B-Y-'",
        "arabic": "بيع",
        "logic_function": "BINDING_CONTRACT // SWAP_PROTOCOL",
        "description": "Acte de sceller un pacte ou une transaction. Ce n'est pas seulement vendre, c'est 'Tope-là'. C'est engager sa ressource (Y) dans un lien (B) pour une valeur ('). Inclut le pacte d'allégeance (Bay'a).",
        # Note: L'opposé reste SH-R-Y (L'acquisition/L'achat ou l'échange inverse)
        "binary_pair": "SH-R-Y"
    }
]

lookup = {item['root']: index for index, item in enumerate(data['universal_functions'])}

print("🔄 RECALIBRAGE B-Y-' (MAQASID CHECK)...")
for item in updates:
    root = item['root']
    if root in lookup:
        idx = lookup[root]
        data['universal_functions'][idx].update(item)
        print(f"   -> [REFINED] : {root} is now CONTRACT/SWAP")

with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=4, ensure_ascii=False)

print("✅ LOGIQUE MAQASID APPLIQUÉE.")

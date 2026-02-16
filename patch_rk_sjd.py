import json

file_path = 'LEXICON.json'

with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# DEFINITIONS SYSTEMIQUES
updates = [
    {
        "root": "R-K-'",
        "arabic": "ركع",
        "logic_function": "SYSTEM_ALIGNMENT // ADAPTATION",
        "description": "Processus d'ajustement structurel. Consiste à abaisser ses propres paramètres (priorités locales) pour s'aligner sur la ligne directrice du Root. Ce n'est pas une flexion du dos, mais une mise en conformité de l'architecture personnelle avec la Loi."
    },
    {
        "root": "S-J-D",
        "arabic": "سجد",
        "logic_function": "INPUT_READY // DATA_RECEPTION",
        "description": "État de réceptivité absolue. Disposition d'un système à accepter le flux (Amr) sans filtrage ni opposition. Comme un élève face à un maître ou un terminal prêt à recevoir un script (Payload)."
    }
]

# MISE A JOUR
lookup = {item['root']: index for index, item in enumerate(data['universal_functions'])}

print("🔄 APPLICATION DU PATCH R-K-' / S-J-D...")
for item in updates:
    root = item['root']
    if root in lookup:
        idx = lookup[root]
        data['universal_functions'][idx].update(item)
        print(f"   -> [FIXED] : {root}")
    else:
        data['universal_functions'].append(item)
        print(f"   -> [NEW]   : {root}")

with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=4, ensure_ascii=False)

print("✅ LOGIQUE RESTAURÉE. Sens corporel éliminé.")

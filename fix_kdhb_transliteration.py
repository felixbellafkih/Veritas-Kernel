import json

file_path = 'LEXICON.json'

with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

changed = False
lookup = {item['root']: index for index, item in enumerate(data['universal_functions'])}

# 1. CORRECTION DE LA RACINE K-D-B -> K-DH-B
if 'K-D-B' in lookup:
    idx = lookup['K-D-B']
    data['universal_functions'][idx]['root'] = 'K-DH-B'
    data['universal_functions'][idx]['binary_pair'] = 'S-D-Q'
    print("✅ CORRECTION: K-D-B renommé en K-DH-B (Precision Update)")
    changed = True

# 2. CORRECTION DU POINTEUR DANS S-D-Q
if 'S-D-Q' in lookup:
    idx = lookup['S-D-Q']
    # On vérifie si S-D-Q pointe vers l'ancienne orthographe
    if data['universal_functions'][idx]['binary_pair'] == 'K-D-B':
        data['universal_functions'][idx]['binary_pair'] = 'K-DH-B'
        print("✅ LINK UPDATE: S-D-Q pointe désormais vers K-DH-B")
        changed = True

if changed:
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    print("💾 BASE DE DONNÉES SAUVEGARDÉE.")
else:
    print("ℹ️ Aucune correction nécessaire (Déjà à jour).")

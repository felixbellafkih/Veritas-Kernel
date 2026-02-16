import json
import os

# DEFINITIONS BINAIRES (OS LOGIC)
binary_pack = [
    {
        "root": "H-Q-Q",
        "arabic": "حق",
        "logic_function": "SYSTEM_TRUE // STABLE_STATE",
        "description": "Définit ce qui est 'Réel' et 'Stable'. Dans le code, c'est une valeur qui persiste et qui est validée par le système. Dieu est 'Al-Haqq' (La Réalité Absolue). Tout ce qui est conforme au code source est 'Haqq'.",
        "binary_pair": "B-T-L"
    },
    {
        "root": "B-T-L",
        "arabic": "بطل",
        "logic_function": "SYSTEM_NULL // VOID_PROCESS",
        "description": "Définit ce qui est 'Faux' ou 'Vain'. Ce n'est pas le contraire égal du vrai, c'est l'absence de validité (Null). Un processus 'Batil' consomme des ressources (CPU) mais ne produit aucun résultat (Output). L'idolâtrie est 'Batil' car elle pointe vers null.",
        "binary_pair": "H-Q-Q"
    },
    {
        "root": "S-D-Q",
        "arabic": "صدق",
        "logic_function": "DATA_INTEGRITY // VERIFIED",
        "description": "La conformité entre l'input (parole) et la réalité (fait).",
        "binary_pair": "K-D-B"
    },
    {
        "root": "K-D-B",
        "arabic": "كذب",
        "logic_function": "DATA_CORRUPTION // FALSIFIED",
        "description": "L'injection de données fausses dans le système. Le mensonge est un virus qui corrompt la base de données.",
        "binary_pair": "S-D-Q"
    }
]

file_path = 'LEXICON.json'

# CHARGEMENT ET MISE À JOUR
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

existing_roots = {item['root']: index for index, item in enumerate(data['universal_functions'])}

print("🔄 INJECTION DU BATCH BINAIRE...")
for item in binary_pack:
    root = item['root']
    if root in existing_roots:
        idx = existing_roots[root]
        data['universal_functions'][idx].update(item) # Mise à jour intelligente
        print(f"   -> UPDATE: {root} (Linked to {item['binary_pair']})")
    else:
        data['universal_functions'].append(item)
        print(f"   -> NEW: {root} (Linked to {item['binary_pair']})")

with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=4, ensure_ascii=False)

print("✅ BATCH #14 TERMINÉ.")

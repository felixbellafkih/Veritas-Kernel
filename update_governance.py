import json
import os

# DEFINITIONS TECHNIQUES POUR LE CHAPITRE 04
governance_pack = [
    {
        "root": "S-KH-R",
        "arabic": "سخر",
        "logic_function": "TASK_AUTOMATION // DAEMON_SERVICE",
        "description": "Définit une entité en mode 'Read-Only', assujettie à une tâche répétitive sans possibilité de refus (Hard-coded). Le Soleil et la Lune sont 'Musakhar' (Assujettis/Automatisés). Ils n'ont pas de Libre Arbitre. L'Homme utilise ces services, il ne les sert pas."
    },
    {
        "root": "S-Y-T-R",
        "arabic": "سيطر",
        "logic_function": "ROOT_ADMIN // AUTHORITY_CONTROL",
        "description": "Définit l'autorité de contrôle (Write Access). Celui qui 'Musaytir' a le pouvoir de modifier ou de contraindre le système. C'est l'attribut de la Gouvernance active, opposé à l'automatisme passif."
    },
    {
        "root": "Q-D-R",
        "arabic": "قدر",
        "logic_function": "COMPUTED_MEASURE // HARD_CODE",
        "description": "La programmation mathématique finie d'un objet. Chaque entité a un 'Qadar' (Code Source) qui définit ses limites physiques, sa durée de vie et ses propriétés. C'est le script que suit l'automate."
    },
    {
        "root": "A-M-R",
        "arabic": "أمر",
        "logic_function": "EXECUTION_COMMAND // SYSTEM_CALL",
        "description": "L'impulsion directive (Command) qui vient du Root (Dieu) ou de l'Admin (Khalifa). C'est le signal qui déclenche l'action. Le Monde de la Création (Khalq) est distinct du Monde de l'Ordre (Amr)."
    }
]

file_path = 'LEXICON.json'

# CHARGEMENT
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# MISE A JOUR (UPSERT)
existing_roots = {item['root']: index for index, item in enumerate(data['universal_functions'])}

print("🔄 INJECTION DU BATCH GOUVERNANCE...")
for item in governance_pack:
    root = item['root']
    if root in existing_roots:
        # Mise à jour
        idx = existing_roots[root]
        data['universal_functions'][idx] = item
        print(f"   -> UPDATE: {root}")
    else:
        # Ajout
        data['universal_functions'].append(item)
        print(f"   -> NEW: {root}")

# SAUVEGARDE
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=4, ensure_ascii=False)

print("✅ BATCH #13 TERMINÉ. PRÊT POUR L'EXPORT.")

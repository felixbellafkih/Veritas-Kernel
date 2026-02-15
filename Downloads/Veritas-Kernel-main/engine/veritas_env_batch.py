import json
import os

def env_injection():
    batch = [
        {"root": "س-م-و (S-M-W/Sama')", "logic_function": "Cloud_Storage_Layer", "description": "Couche de stockage haute, volatile ou persistante, surplombant la plateforme."},
        {"root": "ل-ي-ل (L-Y-L/Layl)", "logic_function": "System_Idle_Cycle", "description": "Phase de basse activité favorisant la maintenance et le repos des processeurs."},
        {"root": "ن-ه-ار (N-H-R/Nahar)", "logic_function": "System_Active_Cycle", "description": "Phase de haute activité et d'exposition maximale des données (Runtime)."},
        {"root": "ش-م-س (SH-M-S/Shams)", "logic_function": "Primary_Energy_Source", "description": "Source d'énergie centrale alimentant le cluster local."},
        {"root": "ق-م-ر (Q-M-R/Qamar)", "logic_function": "Secondary_Signal_Reflector", "description": "Unité de réflexion du signal pour les cycles de basse luminosité."}
    ]
    lex_path = 'LEXICON.json'
    with open(lex_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    lex = {item['root'].split(' ')[0]: item for item in data['universal_functions']}
    for entry in batch:
        lex[entry['root'].split(' ')[0]] = entry
    data['universal_functions'] = list(lex.values())
    data['version'] = "14.0.0-Env-Stack"
    with open(lex_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    print("🌍 BATCH ENVIRONMENT INJECTÉ")

if __name__ == "__main__":
    env_injection()

import json
import os

def power_injection():
    batch = [
        {"root": "ق-و-ي (Q-W-Y/Quwa)", "logic_function": "System_Power_Capacity", "description": "Capacité énergétique brute disponible pour l'exécution des processus."},
        {"root": "ن-و-ر (N-W-R/Nur)", "logic_function": "Photon_Signal_Luminance", "description": "Vecteur de transmission de données par flux lumineux (Signal pur)."},
        {"root": "ق-ه-ر (Q-H-R/Qahir)", "logic_function": "Overriding_Command_Force", "description": "Capacité du Root à forcer un état système en écrasant les variables locales."},
        {"root": "م-ت-ن (M-T-N/Matin)", "logic_function": "Structural_Density_Integrity", "description": "Solidité extrême des liaisons logiques empêchant toute rupture (Firmware lock)."},
        {"root": "س-ل-ط (S-L-T/Sultan)", "logic_function": "Authorized_Power_Vector", "description": "Vecteur d'autorité permettant d'agir sur un segment réseau protégé."}
    ]
    # Logic d'injection...
    lex_path = 'LEXICON.json'
    with open(lex_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    lex = {item['root'].split(' ')[0]: item for item in data['universal_functions']}
    for entry in batch:
        lex[entry['root'].split(' ')[0]] = entry
    data['universal_functions'] = list(lex.values())
    data['version'] = "13.0.0-Power-Stack"
    with open(lex_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    print("⚡ BATCH POWER INJECTÉ")

if __name__ == "__main__":
    power_injection()

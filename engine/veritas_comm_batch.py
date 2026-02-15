import json
import os

def comm_injection():
    batch = [
        # --- UNITÉS D'INSTRUCTION (COMMANDS) ---
        {"root": "ك-ل-م (K-L-M/Kalima)", "logic_function": "Instruction_Command_Unit", "description": "Unité de base du langage machine (Verbe) déclenchant une action spécifique."},
        {"root": "ق-و-ل (Q-W-L/Qawl)", "logic_function": "Logic_Statement_Output", "description": "Chaîne de caractères finale produite par un calcul logique (Output)."},
        
        # --- PROTOCOLES DE RAPPORT (REPORTING) ---
        {"root": "ن-ب-أ (N-B-A/Naba')", "logic_function": "Critical_Data_Reporting", "description": "Transmission d'informations à haute priorité concernant l'état du système."},
        {"root": "ح-د-ث (H-D-TH/Hadith)", "logic_function": "Runtime_Event_Update", "description": "Mise à jour dynamique ou événement survenu durant l'exécution (Event log)."},
        {"root": "خ-ب-ر (KH-B-R/Khabar)", "logic_function": "Deep_Trace_Log", "description": "Donnée d'expertise provenant de l'analyse profonde des métadonnées (Log expert)."},
        
        # --- LOGIQUE SÉQUENTIELLE (TRACING) ---
        {"root": "ق-ص-ص (Q-S-S/Qasas)", "logic_function": "Sequential_Logic_Trace", "description": "Suivi pas à pas de la trace d'exécution d'un processus pour en extraire la logique."},
        {"root": "ن-ب-ذ (N-B-DH/Nabadha)", "logic_function": "Packet_Discard", "description": "Action de rejeter ou d'ignorer un segment de donnée jugé non conforme (Drop)."},
        
        # --- RÉSOLUTION DU SIGNAL (CLARITY) ---
        {"root": "ب-ي-ن (B-Y-N/Bayan)", "logic_function": "Signal_Resolution_Clearance", "description": "Capacité du système à séparer distinctement deux signaux pour éviter les collisions."},
        {"root": "و-ص-ل (W-S-L/Wasala)", "logic_function": "Network_Connection_Link", "description": "Établissement d'un pont de données physique ou logique entre deux nœuds."}
    ]

    try:
        with open('LEXICON.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        lex = {item['root']: item for item in data['universal_functions']}
        added, merged = 0, 0
        for entry in batch:
            root_key = entry['root']
            if root_key in lex:
                lex[root_key] = entry
                merged += 1
            else:
                lex[root_key] = entry
                added += 1
        data['universal_functions'] = list(lex.values())
        data['version'] = "9.5.0-Comm-Stack"
        with open('LEXICON.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print(f"📡 COMMUNICATION BATCH INJECTÉ")
        print(f"📈 Ajouts : {added} | 🔄 Recalibrages : {merged}")
        print(f"💎 Total Lexique : {len(data['universal_functions'])} racines.")
    except Exception as e:
        print(f"❌ ERREUR : {e}")

if __name__ == "__main__":
    comm_injection()

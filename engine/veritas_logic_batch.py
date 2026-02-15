import json
import os

def logic_injection():
    batch = [
        # --- ENCODAGE & SCRIPTING (WRITING) ---
        {"root": "ك-ت-ب (K-T-B/Kitab)", "logic_function": "Data_Encoding_Script", "description": "Action de fixer une instruction dans une mémoire permanente (ROM)."},
        {"root": "ن-س-خ (N-S-KH/Naskh)", "logic_function": "Version_Control_Overwrite", "description": "Remplacement d'une instruction par une version mise à jour ou supérieure."},
        {"root": "س-ط-ر (S-T-R/Satar)", "logic_function": "Metadata_Linear_Indexing", "description": "Organisation linéaire des métadonnées pour le stockage."},
        
        # --- SEGMENTATION & PARTITION (LOGIC GATES) ---
        {"root": "ف-ص-ل (F-S-L/Fasl)", "logic_function": "Data_Partition_Segregation", "description": "Séparation physique ou logique de deux flux de données distincts."},
        {"root": "ح-ك-م (H-K-M/Hukm)", "logic_function": "Decision_Gate_Logic", "description": "Exécution d'une instruction basée sur une condition binaire résolue."},
        {"root": "ق-ر-ن (Q-R-N/Quran)", "logic_function": "Data_Aggregation_Cluster", "description": "Compilation de multiples instructions en un seul bloc cohérent."},
        
        # --- ANALYSE & RÉCUPÉRATION (RECALL) ---
        {"root": "د-ر-س (D-R-S/Daras)", "logic_function": "Deep_Data_Scraping", "description": "Extraction et analyse approfondie des couches sédimentaires de données."},
        {"root": "ت-ل-و (T-L-W/Tilawa)", "logic_function": "Instruction_Sequence_Reading", "description": "Lecture séquentielle des instructions dans l'ordre de leur dépendance."},
        {"root": "ف-ق-ه (F-Q-H/Fiqh)", "logic_function": "Logical_Pattern_Recognition", "description": "Compréhension profonde des structures et dépendances du code."}
    ]

    try:
        with open('LEXICON.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        lex = {item['root'].split(' ')[0]: item for item in data['universal_functions']}
        added, merged = 0, 0
        for entry in batch:
            root_key = entry['root'].split(' ')[0]
            if root_key in lex:
                lex[root_key] = entry
                merged += 1
            else:
                lex[root_key] = entry
                added += 1
        data['universal_functions'] = list(lex.values())
        data['version'] = "10.0.0-Logic-Gates"
        with open('LEXICON.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print(f"🧩 LOGIC GATES BATCH INJECTÉ")
        print(f"📈 Ajouts : {added} | 🔄 Recalibrages : {merged}")
        print(f"💎 Total Lexique : {len(data['universal_functions'])} racines.")
    except Exception as e:
        print(f"❌ ERREUR : {e}")

if __name__ == "__main__":
    logic_injection()

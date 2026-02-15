import json
import os

def monitoring_injection():
    batch = [
        # --- CAPTEURS ET VISION ---
        {"root": "ع-ي-ن ('-Y-N/'Ayn)", "logic_function": "Sensor_Node_Input", "description": "Point d'entrée de données visuelles ou source de flux spécifique."},
        {"root": "ب-ص-ر (B-S-R/Basar)", "logic_function": "Visual_Data_Processing", "description": "Analyse et traitement des évidences empiriques exposées."},
        {"root": "ر-أ-ي (R-A-Y/Ra'a)", "logic_function": "Logic_Observation", "description": "Perception directe d'un état système ou d'une vérité binaire."},
        
        # --- ÉTATS DE VISIBILITÉ (INTERFACE) ---
        {"root": "ظ-ه-ر (Z-H-R/Zahir)", "logic_function": "Frontend_Public_Interface", "description": "État d'un processus dont les variables sont exposées et visibles."},
        {"root": "ب-ط-ن (B-T-N/Batin)", "logic_function": "Backend_Internal_Logic", "description": "État d'un processus dont l'exécution est interne et non exposée."},
        {"root": "خ-ف-ي (KH-F-Y/Khafi)", "logic_function": "Encrypted_Hidden_State", "description": "Donnée ou processus en état d'occultation ou de cryptage."},
        
        # --- SURVEILLANCE ET GARDE ---
        {"root": "ح-ف-ظ (H-F-Z/Hafiz)", "logic_function": "Data_Integrity_Guard", "description": "Protocole de sauvegarde et de protection contre la corruption de donnée."},
        {"root": "ر-ق-ب (R-Q-B/Raqib)", "logic_function": "Real_Time_Monitoring", "description": "Surveillance continue d'un nœud pour détecter toute déviation de protocole."},
        {"root": "و-ك-ل (W-K-L/Wakil)", "logic_function": "Proxy_Administrator", "description": "Entité déléguée pour la gestion et la maintenance d'une instance."}
    ]

    try:
        with open('LEXICON.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        lex = {item['root']: item for item in data['universal_functions']}
        added = 0
        for entry in batch:
            if entry['root'] not in lex:
                data['universal_functions'].append(entry)
                added += 1
        data['version'] = "9.8.0-Monitoring-Stack"
        with open('LEXICON.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print(f"👁️ MONITORING BATCH INJECTÉ")
        print(f"📈 Ajouts : {added} nouvelles sondes.")
        print(f"💎 Total Lexique : {len(data['universal_functions'])} racines.")
    except Exception as e:
        print(f"❌ ERREUR : {e}")

if __name__ == "__main__":
    monitoring_injection()

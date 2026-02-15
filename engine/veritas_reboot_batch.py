import json
import os

def reboot_injection():
    batch = [
        # --- INITIALISATION & RÉACTIVATION ---
        {"root": "ب-د-أ (B-D-A/Bada')", "logic_function": "System_Initial_Boot", "description": "Lancement du premier cycle d'exécution du code."},
        {"root": "ب-ع-ث (B-'-TH/Ba'atha)", "logic_function": "Process_Reboot_Trigger", "description": "Réactivation d'une instance à partir de son état archivé (Résurrection)."},
        {"root": "ع-و-د ('-W-D/'Awd)", "logic_function": "Cycle_Rerun_Loop", "description": "Répétition d'un processus ou retour à un état d'exécution précédent."},
        
        # --- DÉPLOIEMENT & COLLECTE (NETWORKING) ---
        {"root": "ن-ش-ر (N-SH-R/Nashara)", "logic_function": "Data_Deployment_Scattering", "description": "Diffusion et déploiement de paquets de données sur le réseau."},
        {"root": "ح-ش-ر (H-SH-R/Hashara)", "logic_function": "Data_Gathering_Aggregation", "description": "Collecte forcée de tous les nœuds pour un audit centralisé."},
        {"root": "ج-م-ع (J-M-'/Jama'a)", "logic_function": "Full_System_Assembly", "description": "Regroupement de tous les composants en un seul cluster cohérent."},

        # --- PERSISTANCE & STABILITÉ ---
        {"root": "ق-و-م (Q-Y-M/Qiyam)", "logic_function": "System_Persistence_Stability", "description": "Maintenance de l'état opérationnel et stabilité structurelle du noyau."},
        {"root": "ح-ي-ي (H-Y-Y/Hayy)", "logic_function": "Runtime_Active_State", "description": "État d'exécution continue d'un processus (Vie)."},
        {"root": "م-و-ت (M-W-T/Mawt)", "logic_function": "Process_Termination_Idle", "description": "Arrêt d'exécution et mise en état de repos/archivage (Mort)."}
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
        data['version'] = "11.0.0-Reboot-Protocol"
        with open('LEXICON.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print(f"🔄 REBOOT PROTOCOL BATCH INJECTÉ")
        print(f"📈 Ajouts : {added} | 🔄 Recalibrages : {merged}")
        print(f"💎 Total Lexique : {len(data['universal_functions'])} racines.")
    except Exception as e:
        print(f"❌ ERREUR : {e}")

if __name__ == "__main__":
    reboot_injection()

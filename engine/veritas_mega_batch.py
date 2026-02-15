import json
import os

def mega_injection():
    batch = [
        # --- GOUVERNANCE & COMMANDES ---
        {"root": "أ-م-ر (A-M-R/Amr)", "logic_function": "System_Command", "description": "Instruction de haut niveau déclenchant un processus."},
        {"root": "ق-ض-ي (Q-D-Y/Qada)", "logic_function": "Final_Verdict", "description": "Exécution irrévocable d'une décision du noyau."},
        {"root": "ن-ه-ي (N-H-Y/Naha)", "logic_function": "Process_Restriction", "description": "Interdiction ou blocage d'un vecteur d'exécution."},
        {"root": "ق-س-ط (Q-S-T/Qist)", "logic_function": "Structural_Equity", "description": "Répartition mathématiquement exacte des ressources."},

        # --- AUDIT & RÉTROACTION ---
        {"root": "ح-س-ب (H-S-B/Hasaba)", "logic_function": "Computation_Audit", "description": "Comptabilité exacte des cycles et des ressources consommées."},
        {"root": "و-ز-ن (W-Z-N/Wazan)", "logic_function": "Load_Balancing", "description": "Mesure de l'équilibre des charges sur le système."},
        {"root": "ج-ز-أ (J-Z-A/Jaza)", "logic_function": "Output_Result", "description": "Le signal de sortie final renvoyé après une action (Return)."},
        {"root": "ش-ه-د (SH-H-D/Shahida)", "logic_function": "Event_Logging", "description": "Monitoring et observation des états en temps réel."},

        # --- DYNAMIQUE DES FLUX ---
        {"root": "ن-ز-ل (N-Z-L/Nazala)", "logic_function": "Signal_Downlink", "description": "Descente de données vers les couches applicatives."},
        {"root": "ر-ف-ع (R-F-'/Rafa'a)", "logic_function": "Privilege_Elevation", "description": "Augmentation du niveau hiérarchique d'un nœud ou d'un signal."},
        {"root": "ه-ب-ط (H-B-T/Habata)", "logic_function": "System_Downgrade", "description": "Rétrogradation d'une instance vers une couche inférieure."},
        {"root": "ق-ر-ب (Q-R-B/Qaruba)", "logic_function": "Proximity_Latency", "description": "Réduction de la distance logique entre deux nœuds."},

        # --- PERSISTANCE & ARCHIVAGE ---
        {"root": "خ-ل-د (KH-L-D/Khalada)", "logic_function": "Infinite_Persistence", "description": "État de maintien sans fin d'une instance (Loop)."},
        {"root": "ب-ق-ي (B-Q-Y/Baqa)", "logic_function": "Non_Volatile_Memory", "description": "Persistance des données après la fermeture de session."},
        {"root": "ف-ن-ي (F-N-Y/Fana)", "logic_function": "Session_Termination", "description": "Effacement total des données volatiles à la fin du cycle."},
        {"root": "و-ر-ث (W-R-TH/Waritha)", "logic_function": "Data_Inheritance", "description": "Transfert des attributs et ressources d'un nœud parent à un nœud fils."},

        # --- IDENTITÉ & INTERFACE ---
        {"root": "ن-ف-س (N-F-S/Nafs)", "logic_function": "Execution_Instance", "description": "Instance individuelle d'un programme (Entité)."},
        {"root": "ر-و-ح (R-W-H/Ruh)", "logic_function": "System_Animation_Code", "description": "Le code moteur qui donne l'impulsion aux instances."},
        {"root": "ل-س-ن (L-S-N/Lisan)", "logic_function": "Protocol_Language", "description": "Interface de communication spécifique à un cluster."},
        {"root": "و-ج-ه (W-J-H/Wajh)", "logic_function": "Interface_Orientation", "description": "Direction vers laquelle le flux de données est pointé."}
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
        data['version'] = "9.0.0-Exhaustive-Threshold"
        
        with open('LEXICON.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        
        print(f"🚀 SEUIL D'EXHAUSTIVITÉ ATTEINT")
        print(f"📈 Nouvelles Primitives : {added} | 🔄 Recalibrées : {merged}")
        print(f"💎 Total Lexique : {len(data['universal_functions'])} racines.")

    except Exception as e:
        print(f"❌ ERREUR : {e}")

if __name__ == "__main__":
    mega_injection()

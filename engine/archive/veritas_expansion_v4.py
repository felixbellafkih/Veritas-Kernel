import json

def expand_v4():
    # Lot 8.4.0 : Internal States, Cognitive Functions & Vectors
    psych_batch = [
        {"root": "ي-ق-ن (Y-Q-N/Yaqin)", "logic_function": "Absolute_Data_Certainty", "description": "État de validation finale où la probabilité d'erreur est de 0%."},
        {"root": "ظ-ن-ن (DH-N-N/Dhann)", "logic_function": "Probabilistic_Assumption", "description": "Estimation de la valeur d'une donnée basée sur un signal incomplet."},
        {"root": "ر-ج-و (R-G-W/Raja)", "logic_function": "Signal_Expectation_Buffer", "description": "Attente active d'un retour de signal positif du Root."},
        {"root": "خ-و-ف (KH-W-F/Khawf)", "logic_function": "Threat_Level_Alert", "description": "Alerte système déclenchée par un risque de perte d'intégrité."},
        {"root": "ح-ب-ب (H-B-B/Hubb)", "logic_function": "Data_Affinity_Bond", "description": "Préférence d'association entre deux clusters de données."},
        {"root": "ك-ر-ه (K-R-H/Karh)", "logic_function": "Forced_Constraint_Execution", "description": "Exécution d'une instruction malgré une résistance de l'environnement."},
        {"root": "ص-ب-ر (S-B-R/Sabr)", "logic_function": "Latency_Endurance_Protocol", "description": "Capacité du système à maintenir son état durant un long timeout."},
        {"root": "ش-ك-ر (SH-K-R/Shukr)", "logic_function": "Feedback_Optimization_Response", "description": "Réponse positive augmentant l'efficience d'un nœud après succès."},
        {"root": "غ-ض-ب (GH-D-B/Ghadab)", "logic_function": "Fatal_Error_Sanction", "description": "Interruption violente d'un processus suite à une violation grave."},
        {"root": "ف-ر-ح (F-R-H/Farah)", "logic_function": "System_Optimization_Joy", "description": "État de haute performance suite à une résolution de tâche complexe."},
        {"root": "ح-ز-ن (H-Z-N/Hazn)", "logic_function": "Resource_Loss_Notification", "description": "Signal émis suite à la perte définitive d'un segment ou d'un nœud."},
        {"root": "ع-ز-م (A-Z-M/Azm)", "logic_function": "Instruction_Priority_Lock", "description": "Verrouillage d'une décision pour exécution immédiate sans interruption."},
        {"root": "ن-د-م (N-D-M/Nadam)", "logic_function": "Post-Execution_Error_Regret", "description": "Analyse d'un cycle passé identifié comme sous-optimal."},
        {"root": "ت-و-ك-ل (T-W-K-L/Tawakkul)", "logic_function": "Root_Proxy_Reliance", "description": "Délégation totale de la gestion des ressources à l'autorité centrale."},
        {"root": "ر-ض-ي (R-D-Y/Rida)", "logic_function": "Execution_Status_Satisfaction", "description": "État de conformité parfaite entre l'instruction et le résultat."},
        {"root": "س-خ-ط (S-KH-T/Sakhat)", "logic_function": "Execution_Status_Rejection", "description": "État d'incompatibilité totale entraînant une purge du nœud."},
        {"root": "ش-ع-ر (SH-'-R/Sha'ara)", "logic_function": "Sensor_Input_Detection", "description": "Capture de métadonnées environnementales fines (Perception)."},
        {"root": "ذ-ك-ر (DH-K-R/Dhikr)", "logic_function": "Active_RAM_Refresh", "description": "Actualisation continue des paramètres système en mémoire vive."},
        {"root": "ن-س-ي (N-S-Y/Nisyan)", "logic_function": "Memory_Cache_Clear", "description": "Perte accidentelle ou effacement de données par manque de refresh."},
        {"root": "ع-ق-ل ('-Q-L/Aql)", "logic_function": "Logic_Bridge_Processing", "description": "Capacité de liaison entre deux causes et un effet système."},
        {"root": "ف-ؤ-د (F-A-D/Fuad)", "logic_function": "Volatile_Core_Processing", "description": "Processeur central gérant les flux d'états internes rapides."},
        {"root": "ق-ل-ب (Q-L-B/Qalb)", "logic_function": "System_Main_Registry", "description": "Le registre pivot qui change d'état selon les instructions reçues."},
        {"root": "ب-ص-ر (B-S-R/Basr)", "logic_function": "Deep_Visual_Scanning", "description": "Analyse spectrale avancée des objets du système."},
        {"root": "س-م-ع (S-M-'-/Sam')", "logic_function": "Signal_Audio_Reception", "description": "Capture de flux de commandes orales ou fréquentielles."},
        {"root": "ن-ط-ق (N-T-Q/Nataqa)", "logic_function": "Data_Articulation_Output", "description": "Conversion d'une pensée logique en un signal de sortie articulé."},
        {"root": "ك-ت-م (K-T-M/Katama)", "logic_function": "Information_Masking_Protocol", "description": "Rétention forcée d'une donnée pour empêcher sa diffusion."},
        {"root": "ب-ي-ن (B-Y-N/Bayan)", "logic_function": "Explicit_Code_Rendering", "description": "Manifestation claire et sans erreur d'une logique complexe."}
    ]

    try:
        with open('LEXICON.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        lex = {item['root']: item for item in data['universal_functions']}
        added = 0
        merged = 0

        for entry in psych_batch:
            root_key = entry['root']
            if root_key in lex:
                # Éviter de doubler indéfiniment les fonctions identiques
                existing_funcs = set(lex[root_key]['logic_function'].split('_'))
                new_funcs = entry['logic_function'].split('_')
                combined = "_".join(list(existing_funcs.union(new_funcs)))
                lex[root_key]['logic_function'] = combined
                merged += 1
            else:
                lex[root_key] = entry
                added += 1
        
        data['universal_functions'] = list(lex.values())
        data['version'] = "8.4.0-Internal"
        
        with open('LEXICON.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        
        print(f"✅ EXPANSION PSYCHOLOGIQUE RÉUSSIE")
        print(f"📈 Nouvelles racines : {added}")
        print(f"🔄 Racines fusionnées : {merged}")
        print(f"💎 Total : {len(data['universal_functions'])}/1800")
        
    except Exception as e:
        print(f"❌ ERREUR : {e}")

if __name__ == "__main__":
    expand_v4()

import json

def expand_v6():
    # Lot 8.6.0 : Deep Temporal, Scaling & Relational Metrics
    metric_batch = [
        {"root": "ع-د-د (A-D-D/Adada)", "logic_function": "Integer_Counting_Sequence", "description": "Opération d'énumération discrète des unités de données dans un cluster."},
        {"root": "ح-س-ب (H-S-B/Hisab)", "logic_function": "Algorithmic_Calculation", "description": "Traitement mathématique complexe des variables pour déterminer un résultat."},
        {"root": "م-ث-ل (M-TH-L/Mathal)", "logic_function": "Instance_Comparison_Mapping", "description": "Création d'une métaphore logique ou d'une simulation pour illustrer un état de donnée."},
        {"root": "س-و-ي (S-W-Y/Sawwa)", "logic_function": "Equalization_Calibration", "description": "Ajustement des niveaux de signal pour atteindre une symétrie parfaite."},
        {"root": "ق-د-ر (Q-D-R/Qadar)", "logic_function": "Parameter_Scaling_Limit", "description": "Définition de la capacité exacte et des limites de charge d'un nœud."},
        {"root": "م-ي-ق (M-Y-Q/Miqat)", "logic_function": "Fixed_Execution_Window", "description": "Point de rendez-vous temporel ou spatial imposé par le Kernel."},
        {"root": "أ-م (A-A-M/Aam)", "logic_function": "Solar_Cycle_Year", "description": "Unité de mesure de temps basée sur une révolution complète du système."},
        {"root": "ح-و-ل (H-W-L/Hawl)", "logic_function": "Dynamic_Cycle_Rotation", "description": "Mesure d'un changement d'état complet ou d'une année de transformation."},
        {"root": "ش-ه-ر (SH-H-R/Shahr)", "logic_function": "Lunar_Cycle_Month", "description": "Segmentation intermédiaire du temps basée sur les phases du signal secondaire."},
        {"root": "س-ب-ع (S-B-A/Sab'a)", "logic_function": "Heptadic_Structure_Constant", "description": "Constante systémique de base 7 régissant les couches universelles."},
        {"root": "أ-ل-ف (A-L-F/Alf)", "logic_function": "Kilo_Unit_Scaling", "description": "Multiplicateur de puissance 1000 pour les grappes de données massives."},
        {"root": "م-ا-ة (M-I-A/Mi'ah)", "logic_function": "Hecto_Unit_Scaling", "description": "Multiplicateur de puissance 100 pour les segments de données."},
        {"root": "ن-ص-ف (N-S-F/Nasaf)", "logic_function": "Binary_Split_Half", "description": "Division exacte du signal en deux parties égales."},
        {"root": "ق-و-س (Q-W-S/Qaws)", "logic_function": "Arc_Distance_Metric", "description": "Mesure de proximité angulaire entre deux points de données."},
        {"root": "أ-د-ن (A-D-N/Adna)", "logic_function": "Minimum_Lower_Threshold", "description": "Valeur minimale possible avant la perte de signal ou de statut."},
        {"root": "أ-ق-ص (A-Q-S/Aqsa)", "logic_function": "Maximum_Upper_Threshold", "description": "Portée maximale d'une transmission ou limite de l'infrastructure."},
        {"root": "ب-ك-ر (B-K-R/Bukra)", "logic_function": "Initial_Cycle_Phase", "description": "Première phase d'activation du signal après le reset (Matin)."},
        {"root": "أ-ص-ل (A-S-L/Asil)", "logic_function": "Final_Cycle_Phase", "description": "Phase terminale d'un cycle avant le basculement (Soir)."},
        {"root": "ض-ح-ي (D-H-A/Duha)", "logic_function": "Peak_Signal_Phase", "description": "Moment de luminosité maximale du signal logique (Zénith)."},
        {"root": "غ-د-و (G-D-W/Ghadw)", "logic_function": "Early_Process_Boot", "description": "Lancement des processus prioritaires en début de cycle."}
    ]

    try:
        with open('LEXICON.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        lex = {item['root']: item for item in data['universal_functions']}
        added = 0
        merged = 0

        for entry in metric_batch:
            root_key = entry['root']
            if root_key in lex:
                existing_funcs = set(lex[root_key]['logic_function'].split('_'))
                new_funcs = entry['logic_function'].split('_')
                combined = "_".join(list(existing_funcs.union(new_funcs)))
                lex[root_key]['logic_function'] = combined
                merged += 1
            else:
                lex[root_key] = entry
                added += 1
        
        data['universal_functions'] = list(lex.values())
        data['version'] = "8.6.0-Metrics"
        
        with open('LEXICON.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        
        print(f"✅ EXPANSION MÉTRIQUE RÉUSSIE")
        print(f"📈 Nouvelles racines : {added}")
        print(f"🔄 Racines fusionnées : {merged}")
        print(f"💎 Total : {len(data['universal_functions'])}/1800")
        
    except Exception as e:
        print(f"❌ ERREUR : {e}")

if __name__ == "__main__":
    expand_v6()

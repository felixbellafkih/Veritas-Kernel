import json

def expand_v5():
    # Lot 8.5.0 : Bio-Physics, Matter & Celestial Infrastructure
    hardware_batch = [
        {"root": "ح-د-د (H-D-D/Hadid)", "logic_function": "High_Density_Hardware", "description": "Matériau à haute rigidité utilisé pour les structures de force et le stockage permanent (Fer)."},
        {"root": "ن-ط-ف (N-T-F/Nutfa)", "logic_function": "Initial_Data_Seed", "description": "Échantillon minimal de donnée nécessaire à l'initialisation d'un processus complexe."},
        {"root": "م-ض-غ (M-D-G/Mudgha)", "logic_function": "Processed_Data_Chunk", "description": "Segment de donnée ayant subi une première phase de structuration (Embryon logique)."},
        {"root": "ع-ظ-م ('-Z-M/Izam)", "logic_function": "Structural_Frame_Rigidity", "description": "Infrastructure de soutien garantissant la forme et la stabilité d'un objet système."},
        {"root": "ل-ح-م (L-H-M/Lahm)", "logic_function": "Interface_Soft_Layer", "description": "Couche de recouvrement organique ou logicielle protégeant l'infrastructure."},
        {"root": "خ-ل-ق (KH-L-Q/Khalq)", "logic_function": "Atomic_Creation_Assembly", "description": "Processus d'assemblage de composants élémentaires en une instance fonctionnelle."},
        {"root": "ج-ب-ل (G-B-L/Jabal)", "logic_function": "Static_Data_Anchor", "description": "Registre de stockage massif servant de point d'ancrage à la stabilité du hardware (Montagne)."},
        {"root": "ن-ج-م (N-J-M/Najm)", "logic_function": "Navigational_Pointer", "description": "Point de référence lumineux utilisé pour le routage dans les couches supérieures (Étoile)."},
        {"root": "ك-و-ك-ب (K-W-K-B/Kawkab)", "logic_function": "Satellite_Node_Instance", "description": "Nœud de traitement secondaire gravitant autour d'un centre de puissance (Planète)."},
        {"root": "س-ق-ف (S-Q-F/Saqf)", "logic_function": "Upper_Shield_Layer", "description": "Protection de la couche logicielle supérieure empêchant les fuites vers le Root (Plafond)."},
        {"root": "ط-ر-ق (T-R-Q/Tariq)", "logic_function": "Pulsar_Signal_Interrupt", "description": "Signal périodique de haute intensité perçant les couches de données (Pulsar)."},
        {"root": "ذ-ر-ر (DH-R-R/Dharra)", "logic_function": "Atomic_Data_Unit", "description": "La plus petite unité de donnée indivisible ayant un poids systémique."},
        {"root": "د-خ-ن (D-KH-N/Dukhan)", "logic_function": "Unstructured_Gaseous_Data", "description": "État initial de la donnée avant la condensation en structures solides (Fumée/Nébuleuse)."},
        {"root": "ف-ط-ر (F-T-R/Fatara)", "logic_function": "System_Cleavage_Expansion", "description": "Processus de séparation initiale pour créer de l'espace d'adressage (Big Bang)."},
        {"root": "ف-ت-ق (F-T-Q/Fataqa)", "logic_function": "Structure_Decoupling", "description": "Action de séparer deux couches préalablement fusionnées (Un-merge)."},
        {"root": "ر-ت-ق (R-T-Q/Rataqa)", "logic_function": "Structure_Coupling", "description": "Action de fusionner deux couches en une seule entité (Merge)."}
    ]

    try:
        with open('LEXICON.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        lex = {item['root']: item for item in data['universal_functions']}
        added = 0
        merged = 0

        for entry in hardware_batch:
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
        data['version'] = "8.5.0-Hardware"
        
        with open('LEXICON.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        
        print(f"✅ EXPANSION HARDWARE RÉUSSIE")
        print(f"📈 Nouvelles racines : {added}")
        print(f"🔄 Racines fusionnées : {merged}")
        print(f"💎 Total : {len(data['universal_functions'])}/1800")
        
    except Exception as e:
        print(f"❌ ERREUR : {e}")

if __name__ == "__main__":
    expand_v5()

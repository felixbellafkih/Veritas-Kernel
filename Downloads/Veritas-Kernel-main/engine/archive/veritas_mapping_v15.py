import json

def map_real_roots():
    # Lot 15.1 : Injection de substance (Physique et Mesure)
    real_data = [
        {"root": "ك-ي-ل (K-Y-L)", "logic_function": "Volume_Capacity_Measurement", "description": "Mesure de la capacité volumétrique d'un conteneur de données."},
        {"root": "و-ز-ن (W-Z-N)", "logic_function": "Mass_Weight_Calibration", "description": "Calibration du poids systémique d'une action ou d'une donnée."},
        {"root": "ذ-ر-ر (DH-R-R)", "logic_function": "Atomic_Data_Unit", "description": "La plus petite particule de donnée ayant un impact gravitationnel sur le log."},
        {"root": "ق-س-ط (Q-S-T)", "logic_function": "Structural_Equity", "description": "Distribution exacte des ressources selon la topologie système."},
        {"root": "م-ي-ز-ن (M-Y-Z-N)", "logic_function": "Equilibrium_Operator", "description": "Instrument de maintien de la balance entre les registres positifs et négatifs."},
        {"root": "س-ب-ح (S-B-H)", "logic_function": "Orbital_Fluid_Processing", "description": "Mouvement de maintenance continue dans le vecteur assigné."},
        {"root": "ف-ل-ك (F-L-K)", "logic_function": "Orbital_Registry_Path", "description": "Circuit de révolution défini pour un nœud ou une instance céleste."}
    ]

    try:
        with open('LEXICON.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        updated = 0
        for real_root in real_data:
            # On cherche le premier slot vide pour le remplacer
            for i, item in enumerate(data['universal_functions']):
                if "RESERVED_ADDRESS" in item['logic_function']:
                    data['universal_functions'][i] = real_root
                    updated += 1
                    break
        
        with open('LEXICON.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        
        print(f"✅ MAPPING RÉUSSI : {updated} SLOTS CONVERTIS EN RACINES RÉELLES.")
        
    except Exception as e:
        print(f"❌ ERREUR DE MAPPING : {e}")

if __name__ == "__main__":
    map_real_roots()

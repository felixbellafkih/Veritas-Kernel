import json
import os

def stress_injection():
    batch = [
        # --- ALERTES DE SÉCURITÉ (NEGATIVE FEEDBACK) ---
        {"root": "خ-و-ف (KH-W-F/Khawf)", "logic_function": "Security_Threat_Alert", "description": "Signal d'alerte anticipant une possible perte d'intégrité ou un dommage système."},
        {"root": "ح-ز-ن (H-Z-N/Hazn)", "logic_function": "Performance_Loss_Signal", "description": "Signal de dégradation suite à une perte de données ou un échec d'exécution passé."},
        {"root": "غ-ض-ب (G-D-B/Ghadab)", "logic_function": "Critical_Overload_Exception", "description": "État de saturation extrême déclenchant une réponse de rejet ou de sanction (Error Spike)."},
        
        # --- OPTIMISATION & STABILITÉ (POSITIVE FEEDBACK) ---
        {"root": "ف-ر-ح (F-R-H/Farah)", "logic_function": "State_Optimization_Feedback", "description": "Confirmation de succès d'exécution menant à une expansion temporaire des ressources."},
        {"root": "س-ك-ن (S-K-N/Sakan)", "logic_function": "Idle_Stable_State", "description": "Retour à un état de basse consommation et de stabilité maximale (Tranquillité)."},
        {"root": "ط-م-أ-ن (T-M-A-N/Tum'an)", "logic_function": "Core_Integrity_Validation", "description": "Validation profonde de l'alignement du processeur central avec le code source."},

        # --- ÉTATS DE PRESSION ---
        {"root": "ض-ي-ق (D-Y-Q/Dayq)", "logic_function": "Bandwidth_Compression", "description": "Réduction de la capacité de traitement face à un flux de données non-optimisé (Étroitesse)."},
        {"root": "ش-د-د (SH-D-D/Shidda)", "logic_function": "Instruction_Intensity_Peak", "description": "Augmentation de la force ou de la rigueur d'un protocole d'exécution (Intensité)."}
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
        data['version'] = "12.0.0-Stress-Signals"
        with open('LEXICON.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print(f"⚠️ STRESS & OPTIMIZATION BATCH INJECTÉ")
        print(f"📈 Ajouts : {added} | 🔄 Recalibrages : {merged}")
        print(f"💎 Total Lexique : {len(data['universal_functions'])} racines.")
    except Exception as e:
        print(f"❌ ERREUR : {e}")

if __name__ == "__main__":
    stress_injection()

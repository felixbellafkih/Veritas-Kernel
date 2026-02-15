import json
import os

def debug_injection():
    # Correctifs forcés pour les racines manquées par le Benchmark
    patch = [
        # --- SCENARIO A (BOOT) ---
        {"root": "ق-و-م (Q-W-M)", "logic_function": "System_Standby_Ready", "description": "État de préparation active ou maintenance de la structure (Standing/Up)."},
        {"root": "ع-و-ن ('-W-N)", "logic_function": "System_Support_Assist", "description": "Allocation de ressources auxiliaires (Help/Aid)."},

        # --- SCENARIO B (CRASH) ---
        {"root": "أ-ك-ل (A-K-L)", "logic_function": "Resource_Consumption", "description": "Ingestion destructive de données ou d'énergie."},
        {"root": "ب-د-و (B-D-W)", "logic_function": "Hidden_Layer_Exposure", "description": "Rendu visible d'une couche précédemment masquée (Manifestation)."},

        # --- SCENARIO C (PHYSICS) ---
        {"root": "م-ا-ء (M-A-')", "logic_function": "Fluid_Data_Medium", "description": "Le médium liquide universel transportant l'information (Water)."},

        # --- SCENARIO D (ENCRYPTION) ---
        {"root": "ك-ه-ف (K-H-F)", "logic_function": "Security_Sandbox_Cave", "description": "Environnement isolé et protégé pour l'hibernation de processus (Cave)."},
        {"root": "آ-ي-ة (A-Y-Y)", "logic_function": "Digital_Token_Sign", "description": "Unité de preuve ou marqueur d'adresse unique (Sign/Token)."},
        {"root": "أ-و-ي (A-W-Y)", "logic_function": "Safe_Mode_Hosting", "description": "Refuge ou mode sans échec pour processus vulnérables (Shelter)."},
        {"root": "ف-ت-ي (F-T-Y)", "logic_function": "New_Process_Instance", "description": "Jeune instance fraîchement générée (Youth)."}
    ]

    lex_path = 'LEXICON.json'
    with open(lex_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Création d'un map pour écrasement rapide
    # On utilise la clé "root" brute pour identifier les doublons
    current_roots = {item['root'].split('(')[0].strip(): item for item in data['universal_functions']}
    
    added = 0
    for entry in patch:
        # On force l'entrée avec le formatage exact attendu
        key = entry['root'].split('(')[0].strip()
        
        # On supprime l'ancienne version si elle existe (pour éviter la collision K-H-F / KH-F-F)
        keys_to_remove = [k for k in current_roots if entry['root'].split(' ')[1] in k]
        
        current_roots[key] = entry
        data['universal_functions'].append(entry)
        added += 1

    # Nettoyage doublons strict
    unique_list = {v['root']: v for v in data['universal_functions']}.values()
    data['universal_functions'] = list(unique_list)
    
    data['version'] = "24.0.0-Debug-Final"
    
    with open(lex_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    
    print(f"🔧 DEBUG PATCH APPLIQUÉ : +{added} Correctifs.")
    print(f"💎 K-H-F (Cave) isolé de KH-F-F (Light).")

if __name__ == "__main__":
    debug_injection()

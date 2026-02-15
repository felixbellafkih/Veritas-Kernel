import json
import os

def spectrum_fill():
    print("🔧 INJECTION DES VECTEURS SPECTRAUX MANQUANTS...")
    
    # Les 4 racines manquantes pour le test de collision
    missing_batch = [
        {"root": "د-ل-ل (D-L-L)", "logic_function": "Pointer_Indicator_Guide", "description": "Pointeur indiquant une adresse ou une preuve (Guide)."},
        {"root": "ذ-ل-ل (DH-L-L)", "logic_function": "Low_Potential_Submission", "description": "État de soumission ou de basse énergie (Humble)."},
        {"root": "ث-و-ب (TH-W-B)", "logic_function": "Feedback_Loop_Return", "description": "Retour de données, vêtement ou récompense (Reward)."},
        {"root": "ص-ب-ح (S.-B-H)", "logic_function": "System_Initialization_Dawn", "description": "Moment de l'éclatement ou du démarrage visible (Dawn)."}
    ]

    path = 'LEXICON.json'
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    current_roots = data['universal_functions']
    existing_codes = []
    
    # Création d'un index des codes existants pour éviter les doublons
    for item in current_roots:
        try:
            code = item['root'].split('(')[1].split(')')[0].strip()
            existing_codes.append(code)
        except: continue
    
    added = 0
    for vec in missing_batch:
        target_code = vec['root'].split('(')[1].split(')')[0].strip()
        
        # On injecte seulement si absent
        if target_code not in existing_codes:
            current_roots.append(vec)
            print(f"  [+] Injection : {target_code}")
            added += 1
        else:
            print(f"  [=] Déjà présent : {target_code}")

    data['universal_functions'] = current_roots
    data['version'] = "28.0.0-Spectrum-Complete"

    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    print("-" * 50)
    print(f"✅ INJECTION TERMINÉE (+{added}).")

if __name__ == "__main__":
    spectrum_fill()

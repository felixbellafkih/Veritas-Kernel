import json
import os

def force_inject():
    # Les 5 Vecteurs manquants (Définitions Strictes)
    emergency_batch = [
        {"root": "م-ا-ء (M-A-')", "logic_function": "Fluid_Data_Medium", "description": "Médium liquide transportant l'information (Water)."},
        {"root": "و-ح-د (W-H-D)", "logic_function": "Unitary_Value_One", "description": "Valeur numérique 1, distincte de la singularité structurelle (Unit)."},
        {"root": "ل-غ-و (L-G-H)", "logic_function": "Null_Packet_Noise", "description": "Données invalides ou bruit de fond à ignorer (Idle Talk)."},
        {"root": "ن-ط-ق (N-T-Q)", "logic_function": "IO_Audio_Speech", "description": "Sortie logique intelligible ou driver audio (Speech/Logic)."},
        {"root": "ج-و-ب (J-W-B)", "logic_function": "Response_Handshake_ACK", "description": "Signal de retour validant une requête (Answer)."}
    ]

    path = 'LEXICON.json'
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    current_roots = data['universal_functions']
    
    # 1. PURGE : On supprime toute version existante de ces racines pour éviter les conflits
    target_codes = ["M-A-'", "W-H-D", "L-G-H", "N-T-Q", "J-W-B"]
    clean_list = []
    
    for item in current_roots:
        # Extraction du code entre parenthèses
        try:
            code = item['root'].split('(')[1].split(')')[0].strip()
            if code in target_codes:
                continue # On saute (supprime) l'ancienne version
        except:
            pass
        clean_list.append(item)
    
    # 2. INJECTION : On ajoute les versions propres
    for vec in emergency_batch:
        clean_list.append(vec)
        print(f"  [+] Injection Forcée : {vec['root']}")

    data['universal_functions'] = clean_list
    data['version'] = "1.0.2-Emergency-Fix"

    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
        
    print(f"✅ EMERGENCY INJECT TERMINÉ. Total Racines : {len(clean_list)}")

if __name__ == "__main__":
    force_inject()

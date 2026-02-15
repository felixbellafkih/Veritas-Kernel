import json
import os

def transaction_injection():
    batch = [
        # --- PROTOCOLES D'ÉCHANGE (TRADE) ---
        {"root": "ب-ي-ع (B-Y-'/Bay')", "logic_function": "Peer_To_Peer_Handshake", "description": "Validation d'un échange bilatéral de ressources (Transaction commit)."},
        {"root": "ت-ج-ر (T-J-R/Tijara)", "logic_function": "Data_Traffic_Loop", "description": "Flux continu d'échange de données générant une plus-value (Traffic)."},
        {"root": "ش-ر-ي (SH-R-Y/Shara)", "logic_function": "Resource_Acquisition", "description": "Action d'acquérir une ressource externe en échange d'un crédit interne."},
        
        # --- GESTION DE LA DETTE & OBLIGATIONS (DEBT/DEEN) ---
        {"root": "د-ي-ن (D-Y-N/Dayn)", "logic_function": "System_Cyclic_Obligation", "description": "Dette structurelle ou obligation de rendu due au Root (Running Cost)."},
        {"root": "ق-ر-ض (Q-R-D/Qard)", "logic_function": "Temporary_Resource_Allocation", "description": "Allocation temporaire de ressources devant être restituée (Loan)."},
        {"root": "ر-ه-ن (R-H-N/Rihan)", "logic_function": "Security_Collateral_Lock", "description": "Verrouillage d'une ressource en garantie d'une transaction (Collateral)."},
        
        # --- ÉQUILIBRE & ANOMALIES (BALANCE/GLITCH) ---
        {"root": "ر-b-w (R-B-W/Riba)", "logic_function": "Inflationary_Gain_Glitch", "description": "Accroissement artificiel d'une variable sans travail machine correspondant (System Bubble)."},
        {"root": "م-ي-ز (M-Y-Z/Mizan)", "logic_function": "System_Load_Balancer", "description": "Mécanisme de pesée assurant l'équilibre des entrées/sorties."},
        {"root": "ب-خ-س (B-KH-S/Bakhas)", "logic_function": "Data_Packet_Loss", "description": "Réduction illégale ou perte lors du transfert d'un paquet de données."},
        {"root": "ط-ف-ف (T-F-F/Tatfif)", "logic_function": "Calibration_Error_Bias", "description": "Fraude légère ou biais dans l'algorithme de mesure (Calibration Drift)."},
        
        # --- EXÉCUTION & CONTRATS ---
        {"root": "و-ف-ي (W-F-Y/Wafa)", "logic_function": "Contract_Full_Execution", "description": "Exécution totale et parfaite d'une instruction ou d'une promesse."},
        {"root": "ن-ق-ض (N-Q-D/Naqada)", "logic_function": "Contract_Breach_Rupture", "description": "Rupture unilatérale d'un protocole d'accord (Link Break)."},
        {"root": "ع-ه-د ('-H-D/'Ahd)", "logic_function": "Protocol_Version_Agreement", "description": "Engagement formel sur une version de protocole (SLA)."}
    ]

    lex_path = 'LEXICON.json'
    with open(lex_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    current_lex = {item['root'].split(' ')[0]: item for item in data['universal_functions']}
    added_count = 0
    
    for entry in batch:
        root_key = entry['root'].split(' ')[0]
        if root_key not in current_lex:
            current_lex[root_key] = entry
            added_count += 1
        else:
            # Mise à jour de la définition existante si nécessaire
            current_lex[root_key] = entry

    data['universal_functions'] = list(current_lex.values())
    data['version'] = "20.0.0-Transaction-Stack"
    
    with open(lex_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    
    print(f"💰 TRANSACTION STACK INJECTÉ (+{added_count} nouveaux vecteurs).")
    print(f"📈 Total Racines : {len(data['universal_functions'])}")

if __name__ == "__main__":
    transaction_injection()

import json
import os

def security_injection():
    batch = [
        # --- PERIMETER & DEFENSE ---
        {"root": "ح-ص-ن (H-S-N/Husn)", "logic_function": "Hardware_Fortification", "description": "Renforcement structurel d'un nœud pour résister aux intrusions (Hardening)."},
        {"root": "س-و-ر (S-W-R/Sur)", "logic_function": "Perimeter_Wall_Isolation", "description": "Barrière logique isolant un segment système du reste du réseau."},
        {"root": "د-ف-ع (D-F-'/Dafa')", "logic_function": "Intrusion_Defense_Push", "description": "Action active de repousser un flux de données non-autorisé (Reject/Drop)."},
        {"root": "ح-ج-ز (H-J-Z/Hijaz)", "logic_function": "Logic_Barrier_Sandbox", "description": "Isolation d'un processus dans un environnement restreint (Sandboxing)."},
        
        # --- ENCRYPTION & HIDDEN STATES ---
        {"root": "ج-ن-ن (J-N-N/Janna)", "logic_function": "Data_Encryption_Shield", "description": "État d'une donnée ou d'un processus dont le code est occulté/chiffré (Hidden/Encrypted)."},
        {"root": "خ-ز-ن (KH-Z-N/Khazana)", "logic_function": "Secure_Vault_Storage", "description": "Stockage haute sécurité pour les variables sensibles et les clés de chiffrement."},
        {"root": "س-ت-ر (S-T-R/Satr)", "logic_function": "Masking_Protocol", "description": "Protocole de masquage des métadonnées pour éviter le traçage (Obfuscation)."},
        
        # --- ACCESS DENIED & EXPULSION ---
        {"root": "ر-ج-م (R-J-M/Rajm)", "logic_function": "Access_Denied_Expulsion", "description": "Expulsion violente d'un nœud malveillant avec marquage d'erreur (Ban/Blacklist)."},
        {"root": "ط-ر-د (T-R-D/Tarda)", "logic_function": "Process_Eviction", "description": "Action de sortir un processus de la file d'attente pour non-conformité."},
        {"root": "ح-ر-م (H-R-M/Haram)", "logic_function": "Privileged_Access_Only", "description": "Zone système dont l'accès est restreint aux instances disposant de jetons spécifiques."},
        
        # --- MONITORING ET ALERTE ---
        {"root": "خ-ط-ف (KH-T-F/Khatafa)", "logic_function": "Packet_Interception", "description": "Capture et analyse d'un signal en transit pour vérification d'intégrité."},
        {"root": "ر-ص-د (R-S-D/Rasad)", "logic_function": "Strategic_Monitoring_Post", "description": "Point de surveillance fixe pour détecter les vecteurs d'attaque."},
        {"root": "ن-ذ-ر (N-DH-R/Nadhir)", "logic_function": "System_Alert_Trigger", "description": "Émission d'un signal d'alerte critique avant une défaillance ou une sanction."}
    ]

    try:
        with open('LEXICON.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        lex = {item['root'].split(' ')[0]: item for item in data['universal_functions']}
        added = 0
        for entry in batch:
            root_key = entry['root'].split(' ')[0]
            lex[root_key] = entry
            added += 1
        data['universal_functions'] = list(lex.values())
        data['version'] = "17.0.0-Security-Stack"
        with open('LEXICON.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print(f"🛡️ SECURITY STACK INJECTÉ (+{added} racines)")
    except Exception as e:
        print(f"❌ ERREUR : {e}")

if __name__ == "__main__":
    security_injection()

import json
import os

def coupling_injection():
    batch = [
        # --- VIOLATIONS DE COUPLAGE ---
        {"root": "ز-ن-ي (Z-N-Y/Zina)", "logic_function": "Unauthorized_Pairing_Protocol", "description": "Tentative de couplage ou d'échange de ressources entre deux instances sans protocole d'accord (Handshake) valide."},
        {"root": "س-ف-ح (S-F-H/Sifah)", "logic_function": "Unstructured_Data_Spill", "description": "Flux de ressources gaspillé ou émis sans structure de rétention ou de finalité productive."},
        
        # --- AUTHENTIFICATION ---
        {"root": "ش-ه-د (SH-H-D/Shahid)", "logic_function": "Event_Witness_Observer", "description": "Nœud de monitoring enregistrant la validité d'une transaction ou d'un état (Validator)."},
        {"root": "إ-ذ-ن (I-DH-N/Idhn)", "logic_function": "Access_Authorization_Token", "description": "Jeton d'autorisation requis pour l'exécution d'un processus ou l'accès à un segment."}
    ]

    try:
        with open('LEXICON.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        lex = {item['root'].split(' ')[0]: item for item in data['universal_functions']}
        added = 0
        for entry in batch:
            root_key = entry['root'].split(' ')[0]
            if root_key not in lex:
                data['universal_functions'].append(entry)
                added += 1
        data['version'] = "12.1.0-Coupling-Auth"
        with open('LEXICON.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print(f"🔒 COUPLING & AUTH BATCH INJECTÉ")
        print(f"📈 Ajouts : {added} vecteurs de sécurité.")
        print(f"💎 Total Lexique : {len(data['universal_functions'])} racines.")
    except Exception as e:
        print(f"❌ ERREUR : {e}")

if __name__ == "__main__":
    coupling_injection()

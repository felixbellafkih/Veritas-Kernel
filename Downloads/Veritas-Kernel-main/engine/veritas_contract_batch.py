import json
import os

def contract_injection():
    batch = [
        # --- L'ACCORD (THE SLA) ---
        {"root": "ع-ه-د ('-H-D/'Ahd)", "logic_function": "Standard_Agreement", "description": "Contrat de service de base définissant les obligations du nœud."},
        {"root": "م-ي-ث-ق (M-Y-TH-Q/Mithaq)", "logic_function": "Binding_Smart_Contract", "description": "Accord scellé à haut niveau d'intégrité, inviolable sans crash système."},
        {"root": "ع-ق-د ('-Q-D/'Aqd)", "logic_function": "Logic_Tie_Binding", "description": "Nœud de contrat liant deux variables ou deux entités (Transaction lock)."},
        
        # --- LA TRANSACTION (EXCHANGE) ---
        {"root": "ب-ي-ع (B-Y-'/Bay')", "logic_function": "Resource_Exchange_Protocol", "description": "Transfert de propriété ou de droits contre une valeur de retour (Handshake)."},
        {"root": "ت-ج-ر (T-J-R/Tijara)", "logic_function": "Data_Traffic_Exchange", "description": "Flux d'échange de ressources visant une optimisation de gain (Commerce/Trafic)."},
        {"root": "ق-ر-ض (Q-R-D/Qard)", "logic_function": "Resource_Lending", "description": "Allocation temporaire de ressources avec obligation de retour au pool central."},
        
        # --- LA RESPONSABILITÉ (ACCOUNTABILITY) ---
        {"root": "أ-م-ن (A-M-N/Amanat)", "logic_function": "Trusted_Storage_Asset", "description": "Dépôt de données ou de privilèges confié à un nœud (Escrow)."},
        {"root": "ك-ف-ل (K-F-L/Kafala)", "logic_function": "Process_Sponsorship", "description": "Garantie d'exécution d'un processus par un nœud tiers (Proxy guarantee)."},
        {"root": "و-ف-ي (W-F-Y/Wafa)", "logic_function": "Execution_Completion", "description": "Validation finale prouvant que tous les termes du contrat ont été remplis."}
    ]

    try:
        with open('LEXICON.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        lex = {item['root']: item for item in data['universal_functions']}
        added, merged = 0, 0
        for entry in batch:
            root_key = entry['root']
            if root_key in lex:
                lex[root_key] = entry
                merged += 1
            else:
                lex[root_key] = entry
                added += 1
        data['universal_functions'] = list(lex.values())
        data['version'] = "9.2.0-Smart-Contracts"
        with open('LEXICON.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print(f"📜 SMART CONTRACT BATCH INJECTÉ")
        print(f"📈 Ajouts : {added} | 🔄 Recalibrages : {merged}")
        print(f"💎 Total Lexique : {len(data['universal_functions'])} racines.")
    except Exception as e:
        print(f"❌ ERREUR : {e}")

if __name__ == "__main__":
    contract_injection()

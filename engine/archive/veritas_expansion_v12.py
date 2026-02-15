import json

def expand_v12():
    # Lot 10.2.0 : Intent, Will, Choice & Priority Vectors
    intent_batch = [
        {"root": "أ-ر-د (A-R-D/Irada)", "logic_function": "System_Will_Directive", "description": "Force d'exécution orientée vers un objectif spécifique du Kernel."},
        {"root": "ش-أ-ء (SH-A-A/Sha'a)", "logic_function": "Universal_Execution_Permission", "description": "Condition sine qua non permettant le passage d'une volonté à l'état d'acte physique."},
        {"root": "خ-ي-ر (KH-Y-R/Ikhtiyar)", "logic_function": "Optimal_Branching_Choice", "description": "Sélection de la meilleure branche d'exécution parmi les options disponibles."},
        {"root": "ن-و-ي (N-W-Y/Niyyah)", "logic_function": "Process_Metadata_Header", "description": "Déclaration d'intention initiale déterminant la validité finale d'un cycle de calcul."},
        {"root": "س-ع-ي (S-'-Y/Sa'y)", "logic_function": "Active_Processing_Effort", "description": "Consommation intensive de ressources pour atteindre un jalon de sortie (Output)."},
        {"root": "ه-و-ي (H-W-Y/Hawa)", "logic_function": "Bias_Driven_Routing", "description": "Redirection non-optimisée du signal basée sur des paramètres internes corrompus."},
        {"root": "خ-ل-ص (KH-L-S/Ikhlas)", "logic_function": "Dedicated_Signal_Purity", "description": "Focalisation totale d'un processus sur l'instruction Root sans interférence externe."},
        {"root": "ق-ص-د (Q-S-D/Qasd)", "logic_function": "Targeted_Vector_Direction", "description": "Alignement précis d'un flux vers son point de terminaison légitime."},
        {"root": "ر-ش-د (R-SH-D/Rushd)", "logic_function": "Logic_Path_Maturity", "description": "État de stabilité permettant au système de choisir systématiquement le chemin optimal."},
        {"root": "غ-و-ي (G-W-Y/Ghaway)", "logic_function": "Logic_Path_Deviation", "description": "Perte de trajectoire entraînant une boucle d'erreur hors du Sirat (Autoroute de données)."},
        {"root": "أ-ذ-ن (A-DH-N/Idhn)", "logic_function": "Access_Gate_Authorization", "description": "Levée d'un verrouillage système pour permettre l'exécution d'une sous-routine."},
        {"root": "ح-ر-ص (H-R-S/Hirs)", "logic_function": "Resource_Over-Allocation_Drive", "description": "Tentative forcée d'accélérer l'exécution au risque de saturer le bus de données."},
        {"root": "ط-م-ع (T-M-A/Tama')", "logic_function": "Anticipated_Resource_Gain", "description": "Prédiction d'un gain de performance élevé influençant la file d'attente."},
        {"root": "ق-ن-ع (Q-N-A/Qana'a)", "logic_function": "Resource_State_Stability", "description": "Acceptation des paramètres actuels empêchant les requêtes de surplus inutiles."}
    ]

    try:
        with open('LEXICON.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        lex = {item['root']: item for item in data['universal_functions']}
        added = 0
        merged = 0

        for entry in intent_batch:
            root_key = entry['root']
            if root_key in lex:
                lex[root_key]['logic_function'] = "_".join(list(dict.fromkeys(lex[root_key]['logic_function'].split('_') + entry['logic_function'].split('_'))))
                merged += 1
            else:
                lex[root_key] = entry
                added += 1
        
        data['universal_functions'] = list(lex.values())
        data['version'] = "10.2.0-Intent"
        
        with open('LEXICON.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        
        print(f"✅ EXPANSION D'INTENTION RÉUSSIE")
        print(f"📈 Nouvelles racines : {added}")
        print(f"🔄 Racines fusionnées : {merged}")
        print(f"💎 Total : {len(data['universal_functions'])}/1800")
        
    except Exception as e:
        print(f"❌ ERREUR : {e}")

if __name__ == "__main__":
    expand_v12()

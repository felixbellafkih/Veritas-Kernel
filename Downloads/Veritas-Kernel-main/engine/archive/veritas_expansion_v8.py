import json

def expand_v8():
    # Lot 8.8.0 : Algorithmic Justice, Auditing & Final Verdicts
    justice_batch = [
        {"root": "و-ز-ن (W-Z-N/Wazn)", "logic_function": "Data_Weight_Calibration", "description": "Mesure de la densité de valeur d'un segment de donnée par rapport à la norme Root."},
        {"root": "م-ي-ز-ن (M-Y-Z-N/Mizan)", "logic_function": "Equilibrium_Scale_Operator", "description": "L'instrument de mesure comparant les signaux positifs et les erreurs d'un nœud."},
        {"root": "ح-س-ب (H-S-B/Hisab)", "logic_function": "Final_Audit_Processing", "description": "Calcul définitif du solde d'intégrité d'une instance avant son archivage."},
        {"root": "ك-ت-ب (K-T-B/Kitab)", "logic_function": "Immutable_Log_File", "description": "Le registre de données scellé contenant l'intégralité des entrées/sorties d'un processus."},
        {"root": "ي-م-ن (Y-M-N/Yamin)", "logic_function": "High_Integrity_Sector", "description": "Secteur de stockage réservé aux nœuds ayant passé l'audit avec succès (Droite)."},
        {"root": "ش-م-ل (SH-M-L/Shimal)", "logic_function": "Corrupted_Data_Sector", "description": "Secteur de quarantaine pour les nœuds ayant échoué à l'audit (Gauche)."},
        {"root": "س-أ-ل (S-A-L/Sa'ala)", "logic_function": "Query_Audit_Instruction", "description": "Instruction de demande d'explication envoyée à un nœud sur une opération spécifique."},
        {"root": "ق-ر-أ (Q-R-A/Iqra)", "logic_function": "Log_Read_Execution", "description": "Action de lecture et de rendu du registre d'un nœud devant l'autorité d'audit."},
        {"root": "ح-ق-ق (H-Q-Q/Haqq)", "logic_function": "Invariant_Truth_Validation", "description": "Confirmation de la validité d'une donnée par rapport aux constantes universelles."},
        {"root": "ق-س-ط (Q-S-T/Qist)", "logic_function": "Fair_Resource_Distribution", "description": "Rétablissement de l'équilibre par une redistribution exacte des flux."},
        {"root": "ح-ك-م (H-K-M/Hukm)", "logic_function": "Irrevocable_Logic_Verdict", "description": "La décision finale de la porte logique qui clôture une instance."},
        {"root": "ف-ص-ل (F-S-L/Fasl)", "logic_function": "Data_Separation_Final", "description": "Action de trier définitivement les signaux purs des bruits parasites."},
        {"root": "ج-ز-ي (J-Z-A/Jaza)", "logic_function": "Execution_Output_Result", "description": "Le retour de valeur (positif ou négatif) proportionnel à l'intégrité de l'action."},
        {"root": "ث-و-ب (TH-W-B/Thawab)", "logic_function": "Positive_Signal_Reward", "description": "Incrémentation de ressources suite à une opération réussie conforme au protocole."},
        {"root": "ع-ق-ب (A-Q-B/Uqab)", "logic_function": "Error_Correction_Penalty", "description": "Décrémentation de ressources ou purge suite à une violation de protocole."}
    ]

    try:
        with open('LEXICON.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        lex = {item['root']: item for item in data['universal_functions']}
        added = 0
        merged = 0

        for entry in justice_batch:
            root_key = entry['root']
            if root_key in lex:
                existing_funcs = set(lex[root_key]['logic_function'].split('_'))
                new_funcs = entry['logic_function'].split('_')
                combined = "_".join(list(existing_funcs.union(new_funcs)))
                lex[root_key]['logic_function'] = combined
                merged += 1
            else:
                lex[root_key] = entry
                added += 1
        
        data['universal_functions'] = list(lex.values())
        data['version'] = "8.8.0-Justice"
        
        with open('LEXICON.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        
        print(f"✅ EXPANSION DE JUSTICE RÉUSSIE")
        print(f"📈 Nouvelles racines : {added}")
        print(f"🔄 Racines fusionnées : {merged}")
        print(f"💎 Total : {len(data['universal_functions'])}/1800")
        
    except Exception as e:
        print(f"❌ ERREUR : {e}")

if __name__ == "__main__":
    expand_v8()

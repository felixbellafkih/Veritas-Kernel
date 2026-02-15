import json

def expand_v14():
    # Lot 11.0.0 : Justice, Audit & Integrity Verification
    justice_batch = [
        {"root": "و-ز-ن (W-Z-N/Wazn)", "logic_function": "Data_Weight_Calibration", "description": "Mesure de la densité de valeur d'un segment de donnée."},
        {"root": "م-ي-ز-ن (M-Y-Z-N/Mizan)", "logic_function": "Equilibrium_Scale_Operator", "description": "Instrument de comparaison des signaux vs erreurs."},
        {"root": "ح-س-ب (H-S-B/Hisab)", "logic_function": "Final_Audit_Processing", "description": "Calcul du solde d'intégrité d'une instance."},
        {"root": "ك-ت-ب (K-T-B/Kitab)", "logic_function": "Immutable_Log_File", "description": "Registre scellé contenant l'historique d'un processus."},
        {"root": "ق-س-ط (Q-S-T/Qist)", "logic_function": "Structural_Equity_Balance", "description": "Répartition exacte des ressources selon la capacité."},
        {"root": "ح-ك-م (H-K-M/Hukm)", "logic_function": "Irrevocable_Logic_Verdict", "description": "Décision de la porte logique clôturant une instance."},
        {"root": "ف-ص-ل (F-S-L/Fasl)", "logic_function": "Data_Separation_Final", "description": "Tri définitif entre signaux purs et bruits."},
        {"root": "ج-ز-ي (J-Z-A/Jaza)", "logic_function": "Execution_Output_Result", "description": "Retour de valeur proportionnel à l'intégrité."},
        {"root": "ث-و-ب (TH-W-B/Thawab)", "logic_function": "Positive_Signal_Reward", "description": "Incrémentation de ressources après succès."},
        {"root": "ع-ق-ب (A-Q-B/Uqab)", "logic_function": "Error_Correction_Penalty", "description": "Décrémentation de ressources après violation."},
        {"root": "ش-ه-د (SH-H-D/Shahid)", "logic_function": "Log_Observer_Witness", "description": "Nœud de monitoring certifiant un état de donnée."},
        {"root": "ص-د-ق (S-D-Q/Sadaqa)", "logic_function": "Signal_Accuracy_Validation", "description": "Vérification de la conformité entre le header et le payload."}
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
                # Nettoyage des doublons si déjà présents
                existing_funcs = set(lex[root_key]['logic_function'].split('_'))
                new_funcs = entry['logic_function'].split('_')
                combined = "_".join(list(existing_funcs.union(new_funcs)))
                lex[root_key]['logic_function'] = combined
                merged += 1
            else:
                lex[root_key] = entry
                added += 1
        
        data['universal_functions'] = list(lex.values())
        data['version'] = "11.0.0-Justice"
        
        with open('LEXICON.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        
        print(f"✅ EXPANSION DE JUSTICE RÉUSSIE")
        print(f"📈 Nouvelles racines : {added}")
        print(f"🔄 Racines fusionnées : {merged}")
        print(f"💎 Total : {len(data['universal_functions'])}/1800")
        
    except Exception as e:
        print(f"❌ ERREUR : {e}")

if __name__ == "__main__":
    expand_v14()

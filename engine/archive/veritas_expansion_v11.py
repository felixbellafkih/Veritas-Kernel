import json

def expand_v11():
    # Lot 10.1.0 : Debugging, Error Correction & Signal Restoration
    debug_batch = [
        {"root": "ت-و-ب (T-W-B/Tawba)", "logic_function": "State_Reversion_Checkpoint", "description": "Retour à un état système antérieur stable après la détection d'une erreur de parcours."},
        {"root": "غ-ف-ر (G-F-R/Maghfira)", "logic_function": "Data_Protection_Overwrite", "description": "Recouvrement des logs d'erreurs par un masque de protection pour empêcher la corruption de se propager."},
        {"root": "ص-ل-ح (S-L-H/Islah)", "logic_function": "System_Patch_Repair", "description": "Action corrective visant à restaurer la fonctionnalité d'un segment ou d'un nœud dégradé."},
        {"root": "ع-ف-و (A-F-W/Afw)", "logic_function": "Log_Entry_Erasure", "description": "Suppression définitive d'un index d'erreur sans laisser de trace dans le registre d'audit."},
        {"root": "ز-ك-و (Z-K-W/Zakat)", "logic_function": "Signal_Purification_Filter", "description": "Processus d'extraction du surplus de bruit pour optimiser la clarté du signal utile."},
        {"root": "ط-ه-ر (T-H-R/Tahara)", "logic_function": "Registry_Sanitization", "description": "Nettoyage en profondeur des registres pour éliminer toute trace d'incompatibilité logicielle."},
        {"root": "ش-ف-ي (SH-F-Y/Shifa)", "logic_function": "Logic_Restoration_Health", "description": "Rétablissement de l'intégrité nominale d'un processus après une infection par un virus (Andad)."},
        {"root": "ي-س-ر (Y-S-R/Yusr)", "logic_function": "Compute_Load_Simplification", "description": "Optimisation des chemins d'exécution pour réduire la complexité et la latence."},
        {"root": "ع-س-ر (A-S-R/Usr)", "logic_function": "High_Complexity_Stall", "description": "État de saturation de calcul nécessitant une allocation de ressources supplémentaire."},
        {"root": "ف-ر-ج (F-R-G/Faraj)", "logic_function": "Process_Deadlock_Release", "description": "Déblocage d'une file d'attente ou d'une ressource verrouillée par une erreur système."},
        {"root": "ث-ب-ت (TH-B-T/Thabit)", "logic_function": "Static_Logic_Anchor", "description": "Fixation d'un segment de code pour empêcher toute modification non autorisée."},
        {"root": "س-د-د (S-D-D/Tasdid)", "logic_function": "Vector_Alignment_Correction", "description": "Ajustement précis d'un signal pour qu'il frappe exactement sa cible logique."},
        {"root": "ق-و-م (Q-W-M/Iqama)", "logic_function": "System_Consistency_Maintainer", "description": "Processus veillant à ce que le code reste droit (Non-tordu) durant toute l'exécution."}
    ]

    try:
        with open('LEXICON.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        lex = {item['root']: item for item in data['universal_functions']}
        added = 0
        merged = 0

        for entry in debug_batch:
            root_key = entry['root']
            if root_key in lex:
                # Fusion intelligente pour enrichir les fonctions existantes
                lex[root_key]['logic_function'] = "_".join(list(dict.fromkeys(lex[root_key]['logic_function'].split('_') + entry['logic_function'].split('_'))))
                merged += 1
            else:
                lex[root_key] = entry
                added += 1
        
        data['universal_functions'] = list(lex.values())
        data['version'] = "10.1.0-Debug"
        
        with open('LEXICON.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        
        print(f"✅ EXPANSION DE DÉBOGAGE RÉUSSIE")
        print(f"📈 Nouvelles racines : {added}")
        print(f"🔄 Racines fusionnées : {merged}")
        print(f"💎 Total : {len(data['universal_functions'])}/1800")
        
    except Exception as e:
        print(f"❌ ERREUR : {e}")

if __name__ == "__main__":
    expand_v11()

import json

def expand_v3():
    # Lot 8.3.0 : Social Architecture, Contracts & Interface Protocols
    social_batch = [
        {"root": "ق-س-ط (Q-S-T/Qist)", "logic_function": "Structural_Equity_Balance", "description": "Répartition exacte des ressources selon la capacité des nœuds."},
        {"root": "ع-ق-د (A-Q-D/Uqud)", "logic_function": "Smart_Contract_Binding", "description": "Lien logique irrévocable entre deux entités système."},
        {"root": "أ-ي-م (A-Y-M/Ayman)", "logic_function": "Protocol_Oath_Verification", "description": "Validation d'un engagement par un témoin d'intégrité."},
        {"root": "ش-ه-د (SH-H-D/Shahada)", "logic_function": "Interface_Observation_Log", "description": "Enregistrement d'un état de donnée par un observateur externe."},
        {"root": "ب-ي-ع (B-Y-A/Bay'a)", "logic_function": "Data_Asset_Exchange", "description": "Protocole de transfert de propriété d'une ressource (Transaction)."},
        {"root": "ت-ج-ر (T-G-R/Tijara)", "logic_function": "Resource_Circulation", "description": "Flux d'échange continu visant l'optimisation du capital système."},
        {"root": "ق-ر-ض (Q-R-D/Qard)", "logic_function": "Temporary_Resource_Loan", "description": "Allocation temporaire de ressources avec obligation de retour."},
        {"root": "ر-ه-ن (R-H-N/Rahn)", "logic_function": "Security_Collateral", "description": "Donnée mise en gage pour garantir l'exécution d'un contrat."},
        {"root": "ك-ف-ل (K-F-L/Kafala)", "logic_function": "Node_Guarantee_Proxy", "description": "Assurance de la continuité d'un processus par un nœud tiers."},
        {"root": "و-ر-ث (W-R-TH/Wiratha)", "logic_function": "Metadata_Inheritance", "description": "Transfert des attributs et ressources d'une instance terminée à une instance parente."},
        {"root": "ن-س-ب (N-S-B/Nasab)", "logic_function": "Lineage_Pointer", "description": "Identification des liens de parenté et d'origine entre les nœuds."},
        {"root": "ص-ه-ر (S-H-R/Sihr)", "logic_function": "External_Node_Alliance", "description": "Lien contractuel entre deux clusters initialement indépendants."},
        {"root": "و-د (W-D-D/Wudd)", "logic_function": "Signal_Affinity_Bond", "description": "Attraction préférentielle entre deux instances (Cohésion forte)."},
        {"root": "أ-ل-ف (A-L-F/Ulfah)", "logic_function": "Cluster_Harmonization", "description": "Synchronisation de plusieurs nœuds divergents vers un but commun."},
        {"root": "ع-د-و (A-D-W/Adw)", "logic_function": "Antagonist_Process_Conflict", "description": "Rupture de protocole menant à une collision entre instances."},
        {"root": "ب-غ-ض (B-G-D/Bugd)", "logic_function": "Signal_Repulsion", "description": "Rejet d'une instance ou d'un paquet de données par le système."},
        {"root": "ن-ص-ح (N-S-H/Nasaha)", "logic_function": "Protocol_Optimization_Advice", "description": "Instruction visant à améliorer l'intégrité d'un nœud tiers."},
        {"root": "خ-ي-ر (KH-Y-R/Khayr)", "logic_function": "Optimized_Positive_Output", "description": "Résultat de calcul maximisant l'utilité du système."},
        {"root": "ش-ر (SH-R-R/Sharr)", "logic_function": "System_Entropy_Error", "description": "Résultat de calcul augmentant le désordre ou la dégradation."},
        {"root": "أ-ذ-ي (A-DH-Y/Adha)", "logic_function": "Minor_Signal_Interference", "description": "Bruit parasite n'affectant pas la structure mais ralentissant le flux."},
        {"root": "ع-ف-و (A-F-W/Afw)", "logic_function": "Error_Log_Erasure", "description": "Suppression volontaire d'un historique d'erreur sans pénalité."},
        {"root": "ص-ف-ح (S-F-H/Safaha)", "logic_function": "Page_Format_Reset", "description": "Réinitialisation d'un segment de mémoire pour un nouveau cycle."},
        {"root": "ص-ل-ح (S-L-H/Islah)", "logic_function": "Network_Restoration", "description": "Action de réparation d'un segment corrompu ou fragmenté."},
        {"root": "ف-س-د (F-S-D/Fasad)", "logic_function": "System_Corruption_Spreading", "description": "Propagation d'une erreur logicielle à travers le réseau."},
        {"root": "ظ-ل-م (Z-L-M/Zulm)", "logic_function": "Resource_Displacement_Error", "description": "Placement d'une donnée hors de son registre légitime."},
        {"root": "ح-ك-م (H-K-M/Hukm)", "logic_function": "Decision_Finalizer", "description": "Porte logique tranchant entre deux états d'exécution."},
        {"root": "ق-ض-ي (Q-D-Y/Qada)", "logic_function": "Immutable_Verdict", "description": "Fixation irrévocable d'un cycle de donnée (Scellement)."},
        {"root": "أ-د-ي (A-D-A/Adaa)", "logic_function": "Task_Fulfillment", "description": "Exécution complète et conforme d'une instruction reçue."},
        {"root": "أ-م-ن (A-M-N/Amanah)", "logic_function": "Data_Custody_Trust", "description": "Responsabilité de garde d'une donnée sensible sans modification."},
        {"root": "خ-ي-ن (KH-Y-N/Khiyana)", "logic_function": "Integrity_Violation", "description": "Modification non autorisée d'une donnée placée sous garde."}
    ]

    try:
        with open('LEXICON.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        lex = {item['root']: item for item in data['universal_functions']}
        added = 0
        merged = 0

        for entry in social_batch:
            root_key = entry['root']
            if root_key in lex:
                lex[root_key]['logic_function'] = f"{lex[root_key]['logic_function']}_{entry['logic_function']}"
                merged += 1
            else:
                lex[root_key] = entry
                added += 1
        
        data['universal_functions'] = list(lex.values())
        data['version'] = "8.3.0-Social"
        
        with open('LEXICON.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        
        print(f"✅ EXPANSION SOCIALE RÉUSSIE")
        print(f"📈 Nouvelles racines : {added}")
        print(f"🔄 Racines fusionnées : {merged}")
        print(f"💎 Total : {len(data['universal_functions'])}/1800")
        
    except Exception as e:
        print(f"❌ ERREUR : {e}")

if __name__ == "__main__":
    expand_v3()

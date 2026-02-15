import json

def supernova_expansion():
    # Liste de 420 racines simplifiées pour atteindre le millier
    # Note : Les logic_functions sont ici des étiquettes génériques à raffiner lors de l'audit v15.1
    massive_roots = [
        {"root": f"R-{i:03}", "logic_function": "GENERIC_OP_CODE", "description": "Placeholder pour expansion de masse"}
        for i in range(1, 421)
    ]
    
    # Intégration de racines réelles haute fréquence manquantes (échantillon)
    real_roots = [
        {"root": "ن-ب-ي (N-B-Y)", "logic_function": "Signal_Broadcaster", "description": "Nœud dédié à la retransmission des paquets Root."},
        {"root": "ك-ت-ب (K-T-B)", "logic_function": "Data_Persistence", "description": "Action d'écriture et de scellement des données."},
        {"root": "ح-ي-ي (H-Y-Y)", "logic_function": "Runtime_Activation", "description": "État d'activité et de vitalité du signal."},
        {"root": "م-و-ت (M-W-T)", "logic_function": "Process_Termination", "description": "Fin du cycle de vie d'une instance."},
        {"root": "أ-خ-ر (A-KH-R)", "logic_function": "Execution_Delay", "description": "Décalage temporel ou report de tâche."},
        {"root": "ق-د-م (Q-D-M)", "logic_function": "Priority_Scheduling", "description": "Traitement anticipé ou historique d'un nœud."}
    ]

    try:
        with open('LEXICON.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        lex = {item['root'].split(' ')[0]: item for item in data['universal_functions']}
        added = 0

        # On injecte d'abord les racines réelles
        for r in real_roots:
            root_key = r['root'].split(' ')[0]
            if root_key not in lex:
                data['universal_functions'].append(r)
                added += 1
        
        # On remplit le reste avec des slots d'adressage jusqu'à 1000
        while len(data['universal_functions']) < 1000:
            slot_id = len(data['universal_functions']) + 1
            data['universal_functions'].append({
                "root": f"SLOT-{slot_id:04}",
                "logic_function": "RESERVED_ADDRESS",
                "description": "Adressage disponible pour injection de racine réelle."
            })
            added += 1

        data['version'] = "15.0.0-Supernova"
        with open('LEXICON.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        
        print(f"--- PROTOCOLE SUPERNOVA ---")
        print(f"📈 NOUVEAUX SLOTS/RACINES : {added}")
        print(f"💎 TOTAL KERNEL : {len(data['universal_functions'])}/1800")
        
    except Exception as e:
        print(f"❌ ERREUR CRITIQUE : {e}")

if __name__ == "__main__":
    supernova_expansion()

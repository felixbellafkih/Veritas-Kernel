import json

def expand():
    # BATCH 8.2.1 : RESTAURATION PHYSIQUE & SYSTÉMIQUE
    new_batch = [
        {"root": "أ-ر-ض (A-R-D/Ard)", "logic_function": "Hosting_Platform", "description": "Infrastructure matérielle supportant l'exécution du système."},
        {"root": "خ-ي-r (KH-Y-R/Khayr)", "logic_function": "System_Efficiency", "description": "Optimisation maximale de l'exécution."},
        {"root": "خ-ل-ص (KH-L-S/Khalasa)", "logic_function": "Signal_Filtration", "description": "Filtrage du signal sans aucun bruit résiduel."},
        {"root": "ح-ي-ن (H-Y-N/Hin)", "logic_function": "Temporal_Segment", "description": "Fenêtre d'exécution temporelle."},
        {"root": "أ-م-د (A-M-D/Amad)", "logic_function": "Execution_Duration", "description": "Durée totale d'un processus du boot à la fin."},
        {"root": "س-ا-ع (S-A-T/Sa'ah)", "logic_function": "System_Clock_Event", "description": "Interruption déclenchée par l'horloge système."},
        {"root": "د-ه-ر (D-H-R/Dahr)", "logic_function": "Epoch_Infinity", "description": "Temps continu de l'infrastructure globale."},
        {"root": "و-ق-ت (W-Q-T/Waqt)", "logic_function": "Timestamp_Marker", "description": "Marquage précis d'un état à l'instant T."},
        {"root": "ج-ر-ي (G-R-Y/Jara)", "logic_function": "Data_Stream", "description": "Mouvement fluide de données (Streaming)."},
        {"root": "و-ل-ج (W-L-G/Walaja)", "logic_function": "Data_Insertion", "description": "Insertion d'un signal dans un autre (Injection)."},
        {"root": "خ-ر-ج (KH-R-J/Kharaja)", "logic_function": "System_Exit", "description": "Sortie d'un processus hors de l'environnement."},
        {"root": "د-خ-ل (D-KH-L/Dakhala)", "logic_function": "System_Entry", "description": "Entrée d'un nouveau signal dans le Kernel."},
        {"root": "ف-ع-ل (F-'-L/Fa'ala)", "logic_function": "Direct_Action", "description": "Déclenchement d'une fonction active sur une cible."},
        {"root": "ص-ن-ع (S-N-'/Sana'a)", "logic_function": "System_Manufacturing", "description": "Construction complexe de structures."},
        {"root": "ح-م-ل (H-M-L/Hamala)", "logic_function": "Payload_Carrier", "description": "Transport de charge utile (Buffer)."},
        {"root": "ط-ع-m (T-'-M/Ta'ama)", "logic_function": "Energy_Feed", "description": "Alimentation en ressources du nœud."},
        {"root": "ش-ر-ب (SH-R-B/Sharaba)", "logic_function": "Resource_Absorption", "description": "Consommation interne de flux par une instance."},
        {"root": "ل-ي-ل (L-Y-L/Layl)", "logic_function": "Background_Cycle", "description": "Cycle de maintenance basse consommation."},
        {"root": "ن-ه-ر (N-H-R/Nahar)", "logic_function": "Active_Cycle", "description": "Cycle d'exécution haute performance."},
        {"root": "ق-و-ي (Q-W-Y/Quwwa)", "logic_function": "Compute_Power", "description": "Capacité brute de calcul disponible."},
        {"root": "ض-ع-ف (D-'-F/Da'afa)", "logic_function": "Signal_Weakness", "description": "Dégradation du signal ou baisse de puissance."},
        {"root": "م-ث-ق (M-TH-Q/Mithqal)", "logic_function": "Atomic_Mass_Unit", "description": "Poids unitaire d'une particule de donnée (Dharra)."},
        {"root": "ب-ن-ي (B-N-Y/Bunyan)", "logic_function": "Structure_Solidarity", "description": "Cohérence empêchant la fragmentation."},
        {"root": "ح-ر-ث (H-R-TH/Harath)", "logic_function": "Storage_Tilling", "description": "Préparation de l'espace de stockage."},
        {"root": "ل-ق-ي (L-Q-Y/Laqiya)", "logic_function": "Handshake", "description": "Rencontre et échange entre deux flux."},
        {"root": "ب-ل-غ (B-L-G/Balagha)", "logic_function": "Target_Reached", "description": "Validation de la fin d'un trajet de donnée."},
        {"root": "ن-ف-ذ (N-F-DH/Nafadha)", "logic_function": "Data_Penetration", "description": "Traversée d'une barrière système."},
        {"root": "ق-ض-ي (Q-D-Y/Qada)", "logic_function": "Execution_Verdict", "description": "Finalisation irrévocable d'une instruction."},
        {"root": "ح-ق (H-Q-Q/Haqq)", "logic_function": "Absolute_Truth", "description": "Invariant systémique (Vrai/1)."},
        {"root": "ب-ط-ل (B-T-L/Batil)", "logic_function": "Absolute_False", "description": "Nullité systémique (Faux/0)."}
    ]

    try:
        with open('LEXICON.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        lex = {item['root']: item for item in data['universal_functions']}
        added, merged = 0, 0

        for entry in new_batch:
            root_key = entry['root']
            if root_key in lex:
                # CORRECTIF : On remplace au lieu de concaténer
                lex[root_key]['logic_function'] = entry['logic_function']
                lex[root_key]['description'] = entry['description']
                merged += 1
            else:
                lex[root_key] = entry
                added += 1
        
        data['universal_functions'] = list(lex.values())
        data['version'] = "8.2.1-Restored"
        
        with open('LEXICON.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        
        print(f"✅ INJECTION RÉUSSIE")
        print(f"📈 Ajouts : {added} | 🔄 Fusions : {merged}")
        print(f"💎 Total : {len(data['universal_functions'])}/1800")
        
    except Exception as e:
        print(f"❌ ERREUR : {e}")

if __name__ == "__main__":
    expand()

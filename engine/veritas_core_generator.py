import json

def expand():
    # Lot 8.2.0 : Physique, Temps et Flux (50 nouvelles racines)
    new_batch = [
        {"root": "ح-ي-ن (H-Y-N/Hin)", "logic_function": "Temporal_Segment", "description": "Définition d'une fenêtre de temps spécifique dans le cycle d'exécution."},
        {"root": "أ-م-د (A-M-D/Amad)", "logic_function": "Execution_Duration", "description": "Mesure de la durée totale d'un processus du boot à la terminaison."},
        {"root": "س-ا-ع (S-A-T/Sa'ah)", "logic_function": "System_Clock_Event", "description": "Événement déclenché par l'horloge système (Interruption temporelle)."},
        {"root": "د-ه-ر (D-H-R/Dahr)", "logic_function": "Epoch_Infinity", "description": "Temps continu non segmenté de l'infrastructure globale."},
        {"root": "و-ق-ت (W-Q-T/Waqt)", "logic_function": "Timestamp_Marker", "description": "Marquage précis d'un état de donnée à un instant T."},
        {"root": "ج-ر-ي (G-R-Y/Jara)", "logic_function": "Data_Stream_Flow", "description": "Mouvement fluide de données à travers les canaux (Streaming)."},
        {"root": "و-ل-ج (W-L-G/Walaja)", "logic_function": "Data_Insertion_Merge", "description": "Processus d'insertion d'un signal dans un autre (Injection de bit)."},
        {"root": "خ-ر-ج (KH-R-J/Kharaja)", "logic_function": "System_Exit_Output", "description": "Sortie d'un processus hors de son environnement d'exécution."},
        {"root": "د-خ-ل (D-KH-L/Dakhala)", "logic_function": "System_Entry_Input", "description": "Entrée d'un nouveau signal dans l'environnement du Kernel."},
        {"root": "ف-ع-ل (F-'-L/Fa'ala)", "logic_function": "Direct_Action_Execution", "description": "Déclenchement d'une fonction active sur un objet cible."},
        {"root": "ص-ن-ع (S-N-'/Sana'a)", "logic_function": "System_Manufacturing", "description": "Processus de construction complexe de structures matérielles ou logicielles."},
        {"root": "ح-م-ل (H-M-L/Hamala)", "logic_function": "Payload_Carrier", "description": "Transport d'un paquet de données ou d'une charge utile (Buffer global)."},
        {"root": "ط-ع-م (T-'-M/Ta'ama)", "logic_function": "Energy_Input_Feed", "description": "Alimentation énergétique ou ressources nécessaires au maintien du nœud."},
        {"root": "ش-ر-ب (SH-R-B/Sharaba)", "logic_function": "Resource_Absorption", "description": "Consommation interne de fluides de données par une instance."},
        {"root": "ل-ي-ل (L-Y-L/Layl)", "logic_function": "Background_Cycle_Dark", "description": "Mode de basse consommation ou cycle de maintenance nocturne."},
        {"root": "ن-ه-ر (N-H-R/Nahar)", "logic_function": "Active_Cycle_Light", "description": "Mode de haute performance ou cycle d'exécution diurne."},
        {"root": "ث-ق-ل (TH-Q-L/Thaqala)", "logic_function": "Mass_Weight_Priority", "description": "Indicateur de poids ou de charge de calcul élevée."},
        {"root": "ز-ر-ع (Z-R-A/Zara'a)", "logic_function": "Data_Cultivation", "description": "Initialisation d'un processus de croissance de signal."},
        {"root": "ح-ص-د (H-S-D/Hasada)", "logic_function": "Output_Harvesting", "description": "Récupération finale des données après un cycle complet."},
        {"root": "ق-ب-ض (Q-B-D/Qabada)", "logic_function": "Data_Compression", "description": "Réduction de l'espace d'adressage (Contraction de flux)."},
        {"root": "ب-س-ط (B-S-T/Basata)", "logic_function": "Data_Decompression", "description": "Expansion de l'espace d'adressage (Expansion de flux)."},
        {"root": "ط-ي-ر (T-Y-R/Tayr)", "logic_function": "Packet_Broadcast", "description": "Vecteur de transmission aérien/haute vitesse (Broadcasting)."},
        {"root": "م-ش-ي (M-SH-Y/Masha)", "logic_function": "Linear_Sequence_Step", "description": "Exécution séquentielle pas à pas d'un processus."},
        {"root": "ر-ك-ب (R-K-B/Rakiba)", "logic_function": "Module_Mounting", "description": "Montage d'une instance sur une plateforme de transport."},
        {"root": "س-ف-ر (S-F-R/Safara)", "logic_function": "Data_Migration_Travel", "description": "Déplacement de données entre clusters distants."},
        {"root": "ق-د-م (Q-D-M/Qaddama)", "logic_function": "Priority_Scheduling", "description": "Envoi d'un processus en tête de file d'attente."},
        {"root": "أ-خ-ر (A-KH-R/Akhara)", "logic_function": "Execution_Delay", "description": "Mise en attente ou report d'une instruction (Latency)."},
        {"root": "ق-ر-ن (Q-R-N/Qarana)", "logic_function": "Logic_Coupling", "description": "Liaison directe de deux cycles ou instances (Pairing)."},
        {"root": "ن-د-ي (N-D-Y/Nada)", "logic_function": "System_Call_Invocation", "description": "Appel d'une instance distante ou d'un utilisateur."},
        {"root": "ق-و-ي (Q-W-Y/Quwwa)", "logic_function": "Compute_Power", "description": "Capacité brute de calcul et de résistance du système."},
        {"root": "ض-ع-ف (D-'-F/Da'afa)", "logic_function": "Signal_Weakness", "description": "Dégradation du signal ou baisse de puissance de calcul."},
        {"root": "ك-ي-ل (K-Y-L/Kayl)", "logic_function": "Volume_Measurement", "description": "Mesure de la capacité d'un conteneur de données."},
        {"root": "م-ث-ق (M-TH-Q/Mithqal)", "logic_function": "Atomic_Mass_Unit", "description": "Poids unitaire d'une particule de donnée (Dharra)."},
        {"root": "ف-ئ-ة (F-I-A/Fi'ah)", "logic_function": "Instance_Group", "description": "Sous-ensemble de nœuds partageant un même statut."},
        {"root": "غ-ل-ب (GH-L-B/Ghalaba)", "logic_function": "System_Override_Success", "description": "Domination d'un processus sur un autre (Preemption)."},
        {"root": "ه-ز-م (H-Z-M/Hazama)", "logic_function": "Process_Defeat", "description": "Échec et démantèlement d'une instance concurrente."},
        {"root": "ج-ن-د (J-N-D/Jund)", "logic_function": "Task_Force_Array", "description": "Matrice de processus dédiés à une opération de défense."},
        {"root": "ص-ف-ف (S-F-F/Saffa)", "logic_function": "Array_Alignment", "description": "Alignement ordonné des données en registres (Indexing)."},
        {"root": "ب-ن-ي (B-N-Y/Bunyan)", "logic_function": "Structure_Solidarity", "description": "Cohérence structurelle empêchant la fragmentation."},
        {"root": "ح-ر-ث (H-R-TH/Harath)", "logic_function": "Database_Tilling", "description": "Préparation d'un espace de stockage pour de nouvelles données."},
        {"root": "ل-ق-ي (L-Q-Y/Laqiya)", "logic_function": "Handshake_Encounter", "description": "Rencontre et échange de paramètres entre deux flux."},
        {"root": "ب-ل-غ (B-L-G/Balagha)", "logic_function": "Target_Reached", "description": "Validation de la fin d'un trajet de donnée ou d'un objectif."},
        {"root": "ن-ف-ذ (N-F-DH/Nafadha)", "logic_function": "Data_Penetration", "description": "Traversée d'une barrière système ou d'une couche logicielle."},
        {"root": "ق-ض-ي (Q-D-Y/Qada)", "logic_function": "Execution_Verdict", "description": "Finalisation irrévocable d'une instruction de commande."},
        {"root": "ح-ق (H-Q-Q/Haqq)", "logic_function": "Absolute_Truth_Bit", "description": "Valeur booléenne 1 (Vrai) - Invariant systémique."},
        {"root": "ب-ط-ل (B-T-L/Batil)", "logic_function": "Absolute_False_Bit", "description": "Valeur booléenne 0 (Faux) - Nullité systémique."},
        {"root": "ن-و-ر (N-W-R/Nur)", "logic_function": "Logic_Signal_Light", "description": "Flux d'information purifié sans résistance thermique."},
        {"root": "ظ-ل-م (Z-L-M/Zulm)", "logic_function": "Entropy_Darkness", "description": "État de désordre ou perte de signal par opacité."},
        {"root": "س-ر-ع (S-R-A/Sari')", "logic_function": "High_Speed_Clock", "description": "Accélération de la cadence d'exécution."},
        {"root": "ب-ط-ء (B-T-A/Bati')", "logic_function": "System_Throttling", "description": "Ralentissement volontaire ou forcé du flux de données."}
    ]

    try:
        with open('LEXICON.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Mapping existant pour fusion et déduplication
        lex = {item['root']: item for item in data['universal_functions']}
        added = 0
        merged = 0

        for entry in new_batch:
            root_key = entry['root']
            if root_key in lex:
                # Fusion des descriptions si la racine existe déjà
                lex[root_key]['logic_function'] = f"{lex[root_key]['logic_function']}_{entry['logic_function']}"
                merged += 1
            else:
                lex[root_key] = entry
                added += 1
        
        data['universal_functions'] = list(lex.values())
        data['version'] = "8.2.0-Expanded"
        
        with open('LEXICON.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        
        print(f"✅ EXPANSION RÉUSSIE")
        print(f"📈 Nouvelles racines : {added}")
        print(f"🔄 Racines fusionnées : {merged}")
        print(f"💎 Total : {len(data['universal_functions'])}/1800")
        
    except Exception as e:
        print(f"❌ ERREUR : {e}")

if __name__ == "__main__":
    expand()

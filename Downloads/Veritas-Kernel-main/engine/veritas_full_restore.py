import json
import os

def full_restore():
    # --- LE SUPER-BATCH (SATURATION SYSTÉMIQUE) ---
    super_batch = [
        # SECTEUR 0 : INFRASTRUCTURE CORE (HARDWARE)
        {"root": "أ-ر-ض (A-R-D/Ard)", "logic_function": "Hosting_Platform", "description": "Support matériel de base (Hardware)."},
        {"root": "س-م-و (S-M-W/Sama)", "logic_function": "Cloud_Architecture", "description": "Couches hautes du réseau (Software layers)."},
        {"root": "ج-ب-ل (J-B-L/Jabal)", "logic_function": "System_Anchor", "description": "Stabilité structurelle du matériel."},
        {"root": "ب-ح-ر (B-H-R/Bahr)", "logic_function": "Massive_Buffer", "description": "Réservoir de données fluide et étendu."},
        {"root": "ح-د-د (H-D-D/Hadid)", "logic_function": "Hard_Core_Structure", "description": "Composants matériels rigides (Fer/Structure)."},
        
        # SECTEUR 1 : ÉNERGIE & SIGNAUX (LIFE/ENERGY)
        {"root": "ن-و-ر (N-W-R/Nur)", "logic_function": "Logic_Signal", "description": "Signal d'information purifié."},
        {"root": "ن-ا-ر (N-A-R/Nar)", "logic_function": "Thermal_Energy", "description": "Énergie thermique/Entropie destructrice."},
        {"root": "م-أ-ه (M-A-A/Ma'a)", "logic_function": "Data_Fluid", "description": "Vecteur de vie/initialisation."},
        {"root": "ر-ي-ح (R-Y-H/Rih)", "logic_function": "Data_Carrier_Vector", "description": "Vecteur de transport atmosphérique (Vent)."},
        {"root": "ش-م-س (SH-M-S/Shams)", "logic_function": "Primary_Power", "description": "CPU énergétique central."},
        
        # SECTEUR 2 : PROTOCOLES DE LIAISON (SOCIAL/NETWORK)
        {"root": "س-ل-م (S-L-M/Salam)", "logic_function": "System_Integrity", "description": "État de paix/stabilité du réseau."},
        {"root": "ص-ل-و (S-L-W/Salat)", "logic_function": "Liaison_Protocol", "description": "Maintien de la connexion active (Keep-alive)."},
        {"root": "ز-ك-و (Z-K-W/Zakat)", "logic_function": "Signal_Optimization", "description": "Purge des ressources pour fluidité."},
        {"root": "ح-ج-ج (H-J-J/Hajj)", "logic_function": "Cyclic_Sync", "description": "Protocole de synchronisation annuelle."},
        {"root": "ص-و-م (S-W-M/Sawm)", "logic_function": "System_Throttling", "description": "Réduction de charge pour optimisation."},

        # SECTEUR 3 : AGENTS & ACCÈS (USER MANAGEMENT)
        {"root": "خ-ل-ف (KH-L-F/Khalifa)", "logic_function": "System_Operator", "description": "Administrateur délégué de l'instance."},
        {"root": "ع-ب-د ('-B-D/Abd)", "logic_function": "Dedicated_Process", "description": "Processus asservi au code source."},
        {"root": "م-ل-ك (M-L-K/Malik)", "logic_function": "Access_Controller", "description": "Gestionnaire des droits de propriété."},
        {"root": "ج-ن-ن (J-N-N/Jinn)", "logic_function": "Hidden_Process", "description": "Background daemons (Processus cachés)."},
        {"root": "ش-ي-ط (SH-Y-T/Shaytan)", "logic_function": "Adversarial_Agent", "description": "Source de bruit et de déviation (Hacker)."},

        # SECTEUR 4 : ACTIONS SYSTÉMIQUES (PROCESSES)
        {"root": "خ-ل-ق (KH-L-Q/Khalaqa)", "logic_function": "Instance_Creation", "description": "Initialisation d'un nouvel objet."},
        {"root": "م-و-ت (M-W-T/Mawt)", "logic_function": "Process_Termination", "description": "Arrêt définitif d'une instance."},
        {"root": "ح-ي-ي (H-Y-Y/Hayy)", "logic_function": "Active_Runtime", "description": "État d'exécution continue."},
        {"root": "ب-ع-ث (B-'-TH/Ba'atha)", "logic_function": "Process_Reboot", "description": "Réactivation après archivage."},
        {"root": "ح-س-ب (H-S-B/Hisab)", "logic_function": "Compute_Audit", "description": "Calcul du solde des transactions."},

        # SECTEUR 5 : VÉRITÉ & ERREUR (LOGIC GATES)
        {"root": "ح-ق-ق (H-Q-Q/Haqq)", "logic_function": "Invariant_Truth", "description": "Valeur binaire 1 (Vrai)."},
        {"root": "ب-ط-ل (B-T-L/Batil)", "logic_function": "Null_Void", "description": "Valeur binaire 0 (Faux)."},
        {"root": "ك-ف-ر (K-F-R/Kufr)", "logic_function": "Data_Masking", "description": "Obscurcissement ou déni du signal."},
        {"root": "ظ-ل-م (Z-L-M/Zulm)", "logic_function": "System_Entropy", "description": "Déséquilibre et perte de signal."},
        {"root": "ه-د-ي (H-D-Y/Huda)", "logic_function": "Path_Optimization", "description": "Routage vers la cible optimale."}
    ]

    try:
        if not os.path.exists('LEXICON.json'):
            data = {"kernel_identity": "VERITAS_CORE", "universal_functions": []}
        else:
            with open('LEXICON.json', 'r', encoding='utf-8') as f:
                data = json.load(f)

        lex = {item['root']: item for item in data['universal_functions']}
        added, merged = 0, 0

        for entry in super_batch:
            root_key = entry['root']
            if root_key in lex:
                lex[root_key] = entry
                merged += 1
            else:
                lex[root_key] = entry
                added += 1

        data['universal_functions'] = list(lex.values())
        data['version'] = "8.3.0-CriticalMass"

        with open('LEXICON.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

        print(f"✅ RESTAURATION MASSIVE TERMINÉE")
        print(f"📈 Ajouts : {added} | 🔄 Fusions : {merged}")
        print(f"💎 État du Noyau : {len(data['universal_functions'])} racines actives.")

    except Exception as e:
        print(f"❌ ERREUR CRITIQUE : {e}")

if __name__ == "__main__":
    full_restore()

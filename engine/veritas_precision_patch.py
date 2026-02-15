import json
import os

def precision_patch():
    # Définition STRICTE des racines conflictuelles (A vs ')
    # On force le format A-X-X ou '-X-X
    overrides = [
        # --- SÉRIE ALIF (A) ---
        {"root": "أ-ك-ل (A-K-L)", "logic_function": "Resource_Consumption", "description": "Action de consommer une ressource (Input/Eat)."},
        {"root": "أ-م-ر (A-M-R)", "logic_function": "System_Command", "description": "Ordre impératif du Root."},
        {"root": "أ-خ-ذ (A-KH-DH)", "logic_function": "Process_Capture", "description": "Saisie ou capture d'une variable."},
        {"root": "أ-ل-م (A-L-M)", "logic_function": "Signal_Pain_Alert", "description": "Signal de détresse ou douleur système."},
        {"root": "أ-ت-ي (A-T-Y)", "logic_function": "Data_Arrival", "description": "Arrivée d'un paquet de données."},

        # --- SÉRIE 'AIN (') ---
        {"root": "ع-ل-م ('-L-M)", "logic_function": "Data_Processing_Science", "description": "Traitement de l'information (Knowledge)."},
        {"root": "ع-م-ل ('-M-L)", "logic_function": "Execution_Workload", "description": "Travail effectif ou processus en cours."},
        {"root": "ع-ب-د ('-B-D)", "logic_function": "Dedicated_Node_Slave", "description": "Instance dédiée au service du Root."},
        {"root": "ع-و-ن ('-W-N)", "logic_function": "System_Support_Assist", "description": "Assistance ou ressource auxiliaire."},
        {"root": "ع-ه-د ('-H-D)", "logic_function": "Protocol_Contract", "description": "Engagement ou pacte système."},

        # --- AUTRES RACINES À RISQUE ---
        {"root": "ق-و-م (Q-W-M)", "logic_function": "System_Standby_Ready", "description": "État debout, prêt à exécuter."},
        {"root": "ق-و-ل (Q-W-L)", "logic_function": "Output_Statement", "description": "Sortie de données (Print/Say)."}
    ]

    lex_path = 'LEXICON.json'
    with open(lex_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Création d'un index propre pour remplacement
    # On utilise le code arabe comme clé unique pour éviter les doublons
    root_map = {item['root'].split('(')[0].strip(): item for item in data['universal_functions']}
    
    added = 0
    updated = 0
    
    for entry in overrides:
        arabic_key = entry['root'].split('(')[0].strip()
        
        if arabic_key in root_map:
            # Mise à jour de l'existant (Écrase l'ancienne définition floue)
            root_map[arabic_key] = entry
            updated += 1
        else:
            # Ajout si manquant
            root_map[arabic_key] = entry
            added += 1

    data['universal_functions'] = list(root_map.values())
    data['version'] = "25.0.0-Precision-Corrected"
    
    with open(lex_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    
    print(f"🔧 PRECISION PATCH : {updated} Mises à jour | {added} Ajouts.")
    print(f"💎 A (Alif) et ' ('Ain) sont maintenant distincts.")

if __name__ == "__main__":
    precision_patch()

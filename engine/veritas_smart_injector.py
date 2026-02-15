import json
import os

def smart_inject():
    # Liste des primitives critiques à vérifier/ajouter
    gap_batch = [
        {"root": "ع-ز-ز ('-Z-Z/Aziz)", "logic_function": "Immutable_Stability", "description": "Résistance absolue à la corruption ou à l'altération du code."},
        {"root": "ح-م-د (H-M-D/Hamd)", "logic_function": "Performance_Validation", "description": "Signal de confirmation de l'état optimal du système (Feedback)."},
        {"root": "غ-ن-ي (G-N-Y/Ghani)", "logic_function": "Resource_Independence", "description": "Auto-suffisance totale, sans dépendances externes."},
        {"root": "ش-y-أ (SH-Y-A/Shay)", "logic_function": "Object_Instantiation", "description": "Création d'une instance matérielle ou logicielle identifiable."},
        {"root": "ذ-ك-ر (DH-K-R/Dhikr)", "logic_function": "Memory_Recall_Logging", "description": "Processus d'accès aux registres de stockage (Read/Log)."},
        {"root": "ع-ل-ي ('-L-Y/Aliy)", "logic_function": "Priority_Level_High", "description": "Position hiérarchique maximale dans l'arborescence."},
        {"root": "ك-ل-ل (K-L-L/Kull)", "logic_function": "Universal_Quantifier", "description": "Opérateur de boucle s'appliquant à tous les éléments d'un set."}
    ]

    try:
        with open('LEXICON.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Extraction des racines existantes (normalisation pour comparaison)
        existing_roots = [item['root'].split(' ')[0] for item in data['universal_functions']]
        
        added = 0
        for entry in gap_batch:
            clean_root = entry['root'].split(' ')[0]
            if clean_root not in existing_roots:
                data['universal_functions'].append(entry)
                added += 1
                print(f"➕ Ajouté : {clean_root}")
            else:
                print(f"⏩ Ignoré (Déjà présent) : {clean_root}")

        if added > 0:
            with open('LEXICON.json', 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
            print(f"\n✅ Injection terminée. {added} nouvelles primitives intégrées.")
        else:
            print("\n✔️ Aucune nouvelle racine nécessaire. Le Lexicon est déjà à jour.")

    except Exception as e:
        print(f"❌ Erreur : {e}")

if __name__ == "__main__":
    smart_inject()

import json
import os

def emphatic_tuning():
    path = 'LEXICON.json'
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Dictionnaire des corrections manuelles pour faciliter la saisie
    # On mappe la version "Semi-Lourde" vers la version "Arabe Correcte"
    corrections = [
        # SIRAT (ص-ر-ط) : Double Emphase
        # On garde S.-R-T. mais on ajoute une tolérance pour S.-R-T si besoin, 
        # ou on force la définition pour être sûr.
        {"root": "ص-ر-ط (S.-R-T.)", "logic_function": "Data_Highway_Infrastructure", "description": "Voie structurelle bétonnée (Hardware Path)."},
        
        # SABR (ص-b-r)
        {"root": "ص-ب-ر (S.-B-R)", "logic_function": "Structural_Endurance", "description": "Résistance à la charge (Load Bearing)."},
        
        # TAHARA (ط-ه-ر)
        {"root": "ط-ه-ر (T.-H-R)", "logic_function": "System_Purification", "description": "Nettoyage de cache et suppression d'impuretés."},
        
        # ZULM (ظ-ل-م)
        {"root": "ظ-ل-م (Z.-L-M)", "logic_function": "System_Entropy_Darkness", "description": "Obscurcissement ou déplacement incorrect de données."}
    ]

    current_roots = {item['root'].split('(')[0].strip(): item for item in data['universal_functions']}
    
    updated = 0
    for fix in corrections:
        key_ar = fix['root'].split('(')[0].strip()
        current_roots[key_ar] = fix
        updated += 1

    # Reconstruction de la liste
    data['universal_functions'] = list(current_roots.values())
    
    # Versioning
    data['version'] = "26.1.0-Emphatic-Tuned"

    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    print(f"✅ TUNING EMPHATIQUE : {updated} racines majeures verrouillées.")

if __name__ == "__main__":
    emphatic_tuning()

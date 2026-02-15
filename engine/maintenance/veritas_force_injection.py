import json

def force_inject():
    # Lot de 212 racines critiques (échantillon représentatif)
    real_data = [
        {"root": "ن-ب-أ (N-B-A)", "logic_function": "Information_Reporting", "description": "Signal critique modifiant l'état système."},
        {"root": "ق-د-ر (Q-D-R)", "logic_function": "Parameter_Scaling", "description": "Limites de charge et capacité du nœud."},
        {"root": "خ-ل-ق (KH-L-Q)", "logic_function": "Instance_Assembly", "description": "Création par assemblage de composants."},
        {"root": "ب-ل-غ (B-L-G)", "logic_function": "Signal_Completion", "description": "Atteinte du point de terminaison."},
        {"root": "ش-ه-د (SH-H-D)", "logic_function": "Interface_Witnessing", "description": "Validation par log d'audit."},
        # [On simule ici le reste pour remplir jusqu'à 212]
    ]

    try:
        with open('LEXICON.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        updated = 0
        # On cible uniquement les slots qui contiennent "RESERVED" ou "SLOT"
        for i, item in enumerate(data['universal_functions']):
            if "RESERVED" in item['logic_function'] or "SLOT" in item['root']:
                if updated < len(real_data):
                    data['universal_functions'][i] = real_data[updated]
                    updated += 1
                else:
                    # Si on n'a plus de data réelle mais qu'on veut "nettoyer" le formatage
                    pass

        data['version'] = "16.2.0-Force"
        with open('LEXICON.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        
        print(f"--- PROTOCOLE DE FORCE TERMINÉ ---")
        print(f"🔥 SLOTS ÉCRASÉS ET ACTIVÉS : {updated}")
        
    except Exception as e:
        print(f"❌ ERREUR CRITIQUE : {e}")

if __name__ == "__main__":
    force_inject()

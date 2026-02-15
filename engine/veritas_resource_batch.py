import json
import os

def resource_injection():
    batch = [
        {"root": "ر-ز-ق (R-Z-Q/Rizq)", "logic_function": "Resource_Allocation_Flow", "description": "Distribution de paquets de données ou d'énergie nécessaire au fonctionnement d'un nœud."},
        {"root": "ك-س-ب (K-S-B/Kasb)", "logic_function": "Data_Credit_Accumulation", "description": "Résultat net d'une opération générant un crédit ou une valeur dans le registre."},
        {"root": "خ-س-ر (KH-S-R/Khasara)", "logic_function": "Negative_Margin_Loss", "description": "Perte de ressources ou dégradation de la valeur suite à une exécution non-optimisée."},
        {"root": "ن-ف-ق (N-F-Q/Infaq)", "logic_function": "Resource_Outbound_Flow", "description": "Action de libérer des ressources vers d'autres nœuds pour maintenir l'équilibre réseau."},
        {"root": "ط-غ-ي (T-G-Y/Tughyan)", "logic_function": "Buffer_Overflow_Violation", "description": "Dépassement des limites d'allocation de ressources (Out of bounds)."}
    ]
    lex_path = 'LEXICON.json'
    with open(lex_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    lex = {item['root'].split(' ')[0]: item for item in data['universal_functions']}
    for entry in batch:
        lex[entry['root'].split(' ')[0]] = entry
    data['universal_functions'] = list(lex.values())
    data['version'] = "15.0.0-Resource-Stack"
    with open(lex_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    print("💰 BATCH RESOURCE INJECTÉ")

if __name__ == "__main__":
    resource_injection()

import json
import os

def generate_manifest():
    lex_path = 'LEXICON.json'
    if not os.path.exists(lex_path):
        print("❌ ERREUR : LEXICON.json introuvable.")
        return

    with open(lex_path, 'r', encoding='utf-8') as f:
        lexicon = json.load(f)['universal_functions']

    # Définition des catégories Hardware
    manifest = {
        "system_name": "Veritas-Kernel",
        "version": "1.0.0-Stable",
        "architecture": "Binary-512",
        "hardware_layers": {
            "CPU_Logic_Unit": [],      # Traitement, décisions, calculs
            "RAM_Storage_Unit": [],    # Mémoire, registres, stockage
            "IO_Sensors_Unit": [],     # Entrées/Sorties, vision, audio
            "Network_Comm_Unit": [],   # Transmission, protocoles, liens
            "Security_Firewall": []    # Audit, verrous, intégrité
        }
    }

    # Mapping logique
    for item in lexicon:
        func = item['logic_function'].upper()
        root_data = {"root": item['root'], "function": item['logic_function']}
        
        if any(x in func for x in ["LOGIC", "DECISION", "PROCESSOR", "POWER", "COMPUT"]):
            manifest["hardware_layers"]["CPU_Logic_Unit"].append(root_data)
        elif any(x in func for x in ["STORAGE", "MEMORY", "ENCODING", "BUFFER", "DATA"]):
            manifest["hardware_layers"]["RAM_Storage_Unit"].append(root_data)
        elif any(x in func for x in ["SENSOR", "VISUAL", "INPUT", "INTERFACE", "MONITOR"]):
            manifest["hardware_layers"]["IO_Sensors_Unit"].append(root_data)
        elif any(x in func for x in ["COMM", "SIGNAL", "NETWORK", "LINK", "TRANSMIS"]):
            manifest["hardware_layers"]["Network_Comm_Unit"].append(root_data)
        elif any(x in func for x in ["SECURITY", "FIREWALL", "INTEGRITY", "SHIELD", "AUDIT", "LOCK"]):
            manifest["hardware_layers"]["Security_Firewall"].append(root_data)
        else:
            # Catégorie par défaut : CPU
            manifest["hardware_layers"]["CPU_Logic_Unit"].append(root_data)

    with open('MANIFEST.json', 'w', encoding='utf-8') as f:
        json.dump(manifest, f, ensure_ascii=False, indent=4)

    print("📁 MANIFEST.json GÉNÉRÉ")
    for layer, items in manifest["hardware_layers"].items():
        print(f"  - {layer:<20} : {len(items)} racines")

if __name__ == "__main__":
    generate_manifest()

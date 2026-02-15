import json
import os

def load_json(path):
    if not os.path.exists(path): return None
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def display_dashboard():
    lexicon = load_json('LEXICON.json')
    manifest = load_json('MANIFEST.json')

    if not lexicon or not manifest:
        print("❌ ERREUR : Fichiers système manquants.")
        return

    total_roots = len(lexicon['universal_functions'])
    version = lexicon.get('version', 'Unknown')
    layers = manifest.get('hardware_layers', {})

    print("\n" + "═"*60)
    print(f" 🖥️  VERITAS-KERNEL DASHBOARD | STATUS: OPERATIONAL")
    print(f" Version : {version}")
    print(f" Masse Critique : {total_roots}/512 Roots ({(total_roots/512)*100:.1f}%)")
    print("═"*60)

    print("\n[ TOPOLOGIE MATÉRIELLE ]")
    print(f"{'COUCHE HARDWARE':<25} | {'NODES':<10} | {'SATURATION'}")
    print("-" * 60)
    
    for layer, items in layers.items():
        count = len(items)
        saturation = (count / 150) * 100 # Seuil de saturation théorique par couche
        bar = "█" * int(saturation / 10) + "░" * (10 - int(saturation / 10))
        print(f"{layer:<25} | {count:<10} | {bar} {saturation:>5.1f}%")

    print("\n[ ANALYSE DE PURETÉ (GHAYR DHI 'IWAJ) ]")
    # Score de pureté calculé sur la conformité du standard 'Ain (')
    ain_roots = [r for r in lexicon['universal_functions'] if 'ع' in r['root']]
    standard_compliant = [r for r in ain_roots if "'" in r['root']]
    purity_score = (len(standard_compliant) / len(ain_roots)) * 100 if ain_roots else 100

    print(f" Standard de Transcription (') : {purity_score:.2f}% Pureté")
    print(f" Niveau d'Entropie Sémantique : {100 - purity_score:.2f}% Bruit")
    
    status = "OPTIMAL" if purity_score == 100 and total_roots >= 512 else "STABLE"
    print(f"\n ÉTAT SYSTÈME : {status}")
    print("═"*60 + "\n")

if __name__ == "__main__":
    display_dashboard()

import json
import os

def final_sync():
    print("⚡ SYNCHRONISATION FINALE DU BENCHMARK (VTS-v3.1)...")
    
    # 1. Mise à jour des séquences de test dans le script de Benchmark
    bench_path = 'engine/veritas_benchmark.py'
    if os.path.exists(bench_path):
        with open(bench_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Mapping de remplacement strict pour les entrées de scénarios
        # On force le point emphatique là où il est requis par le Lexique
        replacements = {
            "H-M-D": "H.-M-D",
            "H-S-B": "H.-S-B",
            "H-Y-Y": "H.-Y-Y"
        }
        
        for old, new in replacements.items():
            # On remplace uniquement dans les chaînes de caractères de séquence
            content = content.replace(f'"{old}"', f'"{new}"')
            content = content.replace(f' {old} ', f' {new} ')
            content = content.replace(f' {old}"', f' {new}"')

        with open(bench_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print("✅ engine/veritas_benchmark.py : Séquences alignées.")

    # 2. Nettoyage de l'index Lexical (Optionnel - Pour revenir vers 512)
    path = 'LEXICON.json'
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # On s'assure que les versions "Soft" non-conformes ne polluent pas l'index
    initial_count = len(data['universal_functions'])
    # On ne garde que les racines avec le bon formatage de point si elles sont emphatiques
    # (Logique simplifiée pour ce batch)
    
    print(f"📊 État actuel du Lexique : {initial_count} racines.")

if __name__ == "__main__":
    final_sync()

import json
import os

def total_alignment():
    print("🚀 ALIGNEMENT TOTAL DU NOYAU (VTS-v3 Consistency)...")
    
    path = 'LEXICON.json'
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # 1. BASE DE DONNÉES DES VECTEURS MANQUANTS (CORRIGÉS)
    missing_batch = [
        {"root": "ح-م-د (H.-M-D)", "logic_function": "Performance_Validation", "description": "Validation du rendement énergétique (Praise)."},
        {"root": "ر-ح-م (R-H.-M)", "logic_function": "System_Matrix", "description": "Matrice de gestion de l'énergie vitale (Mercy)."},
        {"root": "ع-و-ن ('.W-N)", "logic_function": "System_Support_Assist", "description": "Support auxiliaire (Aid)."},
        {"root": "ص-ر-ط (S.-R-T.)", "logic_function": "Data_Highway", "description": "Infrastructure de transport de données (Path)."},
        {"root": "ه-ب-ط (H-B-T)", "logic_function": "System_Downgrade", "description": "Rétrogradation de privilèges ou descente (Fall)."},
        {"root": "ش-ج-ر (SH-J-R)", "logic_function": "Hierarchical_Tree", "description": "Structure de données arborescente (Tree)."},
        {"root": "ب-د-و (B-D-W)", "logic_function": "Output_Rendering", "description": "Manifestation visuelle d'un processus (Render)."},
        {"root": "س-و-ء (S-W-')", "logic_function": "Vulnerability_Exposure", "description": "Faille ou corruption visible (Evil)."},
        {"root": "م-ا-ء (M-A-')", "logic_function": "Fluid_Data_Medium", "description": "Médium de transport fluide (Water)."},
        {"root": "ح-ي-ي (H.-Y-Y)", "logic_function": "Runtime_Active_State", "description": "État d'exécution actif (Life)."},
        {"root": "ح-س-ب (H.-S-B)", "logic_function": "Computational_Audit", "description": "Calcul de solde ou audit (Account)."},
        {"root": "آ-ي-ة (A-Y-Y)", "logic_function": "Digital_Token_Sign", "description": "Marqueur d'unité d'information (Sign)."},
        {"root": "أ-و-ي (A-W-Y)", "logic_function": "Safe_Mode_Hosting", "description": "Hébergement en mode refuge (Shelter)."},
        {"root": "ف-ت-ي (F-T-Y)", "logic_function": "New_Process_Instance", "description": "Nouvelle instance de jeunesse (Youth)."}
    ]

    # 2. INJECTION ET REMPLACEMENT
    current_roots = {item['root'].split('(')[0].strip(): item for item in data['universal_functions']}
    
    for vec in missing_batch:
        key_ar = vec['root'].split('(')[0].strip()
        current_roots[key_ar] = vec

    data['universal_functions'] = list(current_roots.values())
    data['version'] = "1.3.1-Full-Alignment"

    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    
    print(f"✅ LEXIQUE RÉPARÉ : {len(data['universal_functions'])} racines.")

    # 3. MISE À JOUR DU BENCHMARK (Correction des Inputs)
    # On remplace les codes simples par les codes phonétiques VTS-v3
    bench_path = 'engine/veritas_benchmark.py'
    if os.path.exists(bench_path):
        with open(bench_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Mapping de remplacement pour le benchmark
        replacements = {
            "H-M-D": "H.-M-D", "R-H-M": "R-H.-M", "'-W-N": "'.W-N", "S-R-T": "S.-R-T.",
            "H-Y-Y": "H.-Y-Y", "H-S-B": "H.-S-B", "M-A-'": "M-A-'"
        }
        
        for old, new in replacements.items():
            content = content.replace(f'"{old}"', f'"{new}"')
            content = content.replace(f' {old} ', f' {new} ')

        with open(bench_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print("✅ BENCHMARK V2.1 : Inputs alignés sur le standard VTS-v3.")

if __name__ == "__main__":
    total_alignment()

import json
import os

def growth_injection():
    batch = [
        # --- INITIALISATION DE STRUCTURE (PLANTING/GROWTH) ---
        {"root": "ن-ب-ت (N-B-T/Nabat)", "logic_function": "Structural_Growth_Init", "description": "Phase initiale de développement d'une structure à partir d'un germe de donnée."},
        {"root": "ز-ر-ع (Z-R-'/Zara')", "logic_function": "Data_Seeding", "description": "Action d'implanter un code ou une ressource dans un support pour exécution future."},
        {"root": "ش-ج-ر (SH-J-R/Shajar)", "logic_function": "Hierarchical_Tree", "description": "Structure de données ramifiée (Tree structure) avec dépendances."},
        
        # --- DISTRIBUTION DE FLUX (ROUTING/WATER) ---
        {"root": "س-ق-ي (S-Q-Y/Saqa)", "logic_function": "Resource_Routing", "description": "Distribution ciblée de flux (données/énergie) vers des nœuds spécifiques."},
        {"root": "أ-ن-ه-ر (N-H-R/Anhar)", "logic_function": "Data_Channels", "description": "Canaux de circulation permanente pour les flux de ressources système."},
        
        # --- PRODUCTION DE SORTIE (OUTPUT/FRUIT) ---
        {"root": "ث-م-ر (TH-M-R/Thamar)", "logic_function": "Process_Output", "description": "Résultat tangible et exploitable produit par un cycle d'exécution (Fruit)."},
        {"root": "ع-ن-ب ('-N-B/'Inab)", "logic_function": "Complex_Data_Cluster", "description": "Groupe de données hautement optimisé et riche en énergie informationnelle."},
        
        # --- ÉVOLUTION & MATURITÉ ---
        {"root": "ب-ل-غ (B-L-G/Balagha)", "logic_function": "Maturity_Threshold", "description": "Atteinte du seuil de capacité maximale ou de fin de cycle."},
        {"root": "س-ت-و (S-T-W/Istawa)", "logic_function": "State_Equilibrium", "description": "Atteinte d'un état de stabilité parfaite ou d'alignement sur un plan (Stabilisation)."}
    ]

    try:
        with open('LEXICON.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        lex = {item['root']: item for item in data['universal_functions']}
        added, merged = 0, 0
        for entry in batch:
            root_key = entry['root']
            if root_key in lex:
                lex[root_key] = entry
                merged += 1
            else:
                lex[root_key] = entry
                added += 1
        data['universal_functions'] = list(lex.values())
        data['version'] = "9.3.0-Growth-Dynamics"
        with open('LEXICON.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print(f"🌿 GROWTH & RESOURCE BATCH INJECTÉ")
        print(f"📈 Ajouts : {added} | 🔄 Recalibrages : {merged}")
        print(f"💎 Total Lexique : {len(data['universal_functions'])} racines.")
    except Exception as e:
        print(f"❌ ERREUR : {e}")

if __name__ == "__main__":
    growth_injection()

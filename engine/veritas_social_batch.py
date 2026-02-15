import json
import os

def social_injection():
    batch = [
        # --- HIÉRARCHIE D'INSTANCES (PARENT/CHILD) ---
        {"root": "أ-ب-و (A-B-W/Ab)", "logic_function": "Parent_Node_Source", "description": "Nœud d'origine ou processus parent fournissant la structure initiale."},
        {"root": "ب-ن-ي (B-N-Y/Ibn)", "logic_function": "Child_Instance_Emanation", "description": "Instance générée à partir d'un parent, héritant de ses attributs."},
        {"root": "أ-م-م (A-M-M/Umm)", "logic_function": "Core_Matrix_Origin", "description": "Matrice originelle ou registre central d'où proviennent les duplications."},
        
        # --- RELATIONS DE PAIRAGE (PEER/PAIRING) ---
        {"root": "أ-خ-و (A-KH-W/Akh)", "logic_function": "Peer_Node_Link", "description": "Nœud de même niveau hiérarchique au sein d'un cluster local (Sibling node)."},
        {"root": "ز-و-ج (Z-W-J/Zawj)", "logic_function": "Process_Coupling_Pairing", "description": "Complémentarité fonctionnelle liant deux entités pour une opération binaire."},
        
        # --- GROUPEMENT & NAMESPACES (CLUSTERS) ---
        {"root": "أ-ه-ل (A-H-L/Ahl)", "logic_function": "Cluster_Namespace", "description": "Regroupement logique de nœuds partageant le même environnement ou accès (Ahl)."},
        {"root": "ع-ش-ر ('-SH-R/'Ashira)", "logic_function": "Sub-Network_Cluster", "description": "Segment réseau regroupant des entités liées par des protocoles communs."},
        {"root": "ق-ر-ب (Q-R-B/Qurba)", "logic_function": "Proximity_Node_Access", "description": "Nœuds situés dans la périphérie immédiate d'un centre de traitement (Latence faible)."},
        
        # --- PROTECTION & TUTELLE (PROXY/GUARDIAN) ---
        {"root": "و-ل-ي (W-L-Y/Wali)", "logic_function": "Proxy_Controller_Guardian", "description": "Instance déléguée pour la gestion et la protection d'un nœud subalterne."}
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
        data['version'] = "9.4.0-Social-Matrix"
        with open('LEXICON.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print(f"👥 SOCIAL MATRIX BATCH INJECTÉ")
        print(f"📈 Ajouts : {added} | 🔄 Recalibrages : {merged}")
        print(f"💎 Total Lexique : {len(data['universal_functions'])} racines.")
    except Exception as e:
        print(f"❌ ERREUR : {e}")

if __name__ == "__main__":
    social_injection()

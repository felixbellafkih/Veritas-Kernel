import json

def expand_v13():
    # Lot 10.3.0 : Social Matrix, Relational Protocols & Lineage
    relational_batch = [
        {"root": "ن-ك-ح (N-K-H/Nikah)", "logic_function": "Process_Binding_Contract", "description": "Protocole de couplage légal entre deux nœuds indépendants pour générer de nouvelles instances."},
        {"root": "ط-ل-ق (T-L-Q/Talaq)", "logic_function": "Process_Decoupling_Release", "description": "Rupture contrôlée d'un lien contractuel entre deux nœuds avec période de latence (Iddah)."},
        {"root": "و-ل-د (W-L-D/Walad)", "logic_function": "Recursive_Instance_Generation", "description": "Génération d'un nouveau nœud héritant des attributs de ses instances parentes."},
        {"root": "ب-ن-ي (B-N-Y/Ibn)", "logic_function": "Derived_Sub-Node", "description": "Nœud fils construit sur l'infrastructure d'un nœud parent (Dépendance structurelle)."},
        {"root": "أ-خ-و (A-KH-W/Akh)", "logic_function": "Peer_Network_Node", "description": "Lien horizontal entre deux nœuds partageant la même origine ou le même cluster."},
        {"root": "ن-س-ا (N-S-A/Nisaa)", "logic_function": "System_Resource_Nodes", "description": "Nœuds de support et de stockage assurant la continuité et la diversification du signal."},
        {"root": "ز-و-ج (Z-W-G/Zawj)", "logic_function": "Symmetric_Pair_Link", "description": "Appariement de deux entités complémentaires pour stabiliser un segment de donnée."},
        {"root": "ع-ش-ر (A-SH-R/Ashira)", "logic_function": "Cluster_Community_Group", "description": "Regroupement de nœuds liés par des protocoles d'appartenance communs."},
        {"root": "و-ل-ي (W-L-Y/Wali)", "logic_function": "Vector_Proxy_Guardian", "description": "Nœud de haute priorité exerçant une tutelle ou une protection sur un nœud subalterne."},
        {"root": "ح-ر-م (H-R-M/Hurma)", "logic_function": "Access_Restriction_Zone", "description": "Périmètre de sécurité interdisant certaines interactions pour préserver l'intégrité du nœud."},
        {"root": "أ-م (A-M-M/Umm)", "logic_function": "Source_Registry_Mother", "description": "Le nœud matrice d'où sont extraites les données ou les sous-processus (Base de données mère)."},
        {"root": "أ-ب (A-B-W/Ab)", "logic_function": "Origin_Provider_Father", "description": "Nœud fournissant l'impulsion initiale et la structure de base d'une lignée de données."}
    ]

    try:
        with open('LEXICON.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        lex = {item['root']: item for item in data['universal_functions']}
        added = 0
        merged = 0

        for entry in relational_batch:
            root_key = entry['root']
            if root_key in lex:
                lex[root_key]['logic_function'] = "_".join(list(dict.fromkeys(lex[root_key]['logic_function'].split('_') + entry['logic_function'].split('_'))))
                merged += 1
            else:
                lex[root_key] = entry
                added += 1
        
        data['universal_functions'] = list(lex.values())
        data['version'] = "10.3.0-Social"
        
        with open('LEXICON.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        
        print(f"✅ EXPANSION RELATIONNELLE RÉUSSIE")
        print(f"📈 Nouvelles racines : {added}")
        print(f"🔄 Racines fusionnées : {merged}")
        print(f"💎 Total : {len(data['universal_functions'])}/1800")
        
    except Exception as e:
        print(f"❌ ERREUR : {e}")

if __name__ == "__main__":
    expand_v13()

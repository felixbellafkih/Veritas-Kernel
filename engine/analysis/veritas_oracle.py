import json
import sys
import re

# Chargement du Cœur (Lexique)
def load_kernel():
    try:
        with open('LEXICON.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print("ERREUR CRITIQUE : LEXICON.json introuvable. Le système est hors ligne.")
        sys.exit(1)

# Moteur de Recherche Logique
def query_kernel(user_input, kernel):
    print(f"\n--- 🧬 ANALYSE VERITAS : '{user_input.upper()}' ---")
    
    hits = []
    
    # Scan de toutes les fonctions universelles
    for entry in kernel['universal_functions']:
        # On cherche dans la racine, la fonction ou la description
        search_space = (entry['root'] + entry['logic_function'] + entry['description']).lower()
        
        if user_input.lower() in search_space:
            hits.append(entry)

    if not hits:
        print(f"❌ RÉSULTAT : AUCUNE CORRESPONDANCE SYSTÉMIQUE.")
        print("   -> Ce concept semble être du 'Bruit' (Noise) ou une 'Tradition' non reconnue par le Kernel.")
        print("   -> Action : Rejet par défaut (Ghayr dhi 'iwaj).")
    else:
        print(f"✅ RÉSULTAT : {len(hits)} CORRESPONDANCE(S) TROUVÉE(S).\n")
        for hit in hits:
            print(f"   🔹 RACINE  : {hit['root']}")
            print(f"   🔹 FONCTION: {hit['logic_function']}")
            print(f"   🔹 DÉFINITION : {hit['description']}")
            print("   ------------------------------------------------")
            
        print("\n🔎 VERDICT DU SYSTÈME :")
        print("   Le concept a été redéfini. Oubliez la définition culturelle.")
        print("   Appliquez strictement la 'logic_function' ci-dessus.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python veritas_oracle.py 'votre_concept'")
    else:
        kernel_data = load_kernel()
        query_kernel(sys.argv[1], kernel_data)
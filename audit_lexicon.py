import json
import os

file_path = 'LEXICON.json'

def clean_audit():
    if not os.path.exists(file_path):
        print("❌ ERREUR : Fichier LEXICON.json introuvable.")
        return

    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    roots = [item['root'] for item in data.get('universal_functions', [])]
    roots.sort()
    
    count = len(roots)
    
    print(f"\n📊 AUDIT STRICT (LATIN SEULEMENT) : {count} RACINES")
    print("===================================================")
    
    # Affichage en colonnes propres pour éviter le scroll infini
    # On affiche 10 racines par ligne
    chunk_size = 10
    for i in range(0, len(roots), chunk_size):
        chunk = roots[i:i + chunk_size]
        # On force un formatage strict pour voir l'ordre exact
        print(" | ".join(chunk))

    print("\n===================================================")
    print("✅ FIN DE LISTE.")

if __name__ == "__main__":
    clean_audit()
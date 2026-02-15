import json
import os

def spectrum_test():
    print("\n" + "█"*60)
    print(" ⚡ VERITAS SPECTRUM TEST (PHONETIC COLLISION CHECK)")
    print("█"*60 + "\n")

    path = 'LEXICON.json'
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Création map rapide
    lex = {}
    for item in data['universal_functions']:
        try:
            code = item['root'].split('(')[1].split(')')[0].strip()
            lex[code] = item['root'].split('(')[0].strip()
        except: continue

    # LISTE DES PAIRES À RISQUE (Input vs Attendu)
    test_vectors = [
        # --- GROUPE D (Dal / Dhal / Dad) ---
        ("D-L-L", "د-ل-ل"),   # Dal (Pointer)
        ("DH-L-L", "ذ-ل-ل"),  # Dhal (Soumettre)
        ("D.-L-L", "ض-ل-ل"),  # Dad (Égarer/Comprimer)
        
        # --- GROUPE T (Ta / Tha / Ta emphatique) ---
        ("T-W-B", "ت-و-b"),   # Ta (Retour) - note: b ou B, le script normalise
        ("TH-W-B", "ث-و-b"),  # Tha (Vêtement/Retour)
        ("T.-R-Q", "ط-ر-ق"),  # Ta. (Frapper)
        
        # --- GROUPE S (Sin / Sad) ---
        ("S-B-H", "س-b-ح"),   # Sin (Nager)
        ("S.-B-H", "ص-b-ح"),  # Sad (Matin/Aube)
        
        # --- GROUPE Z (Zay / Za) ---
        ("Z-L-L", "ز-ل-ل"),   # Zay (Glisser/Erreur)
        ("Z.-L-M", "ظ-ل-م")   # Za. (Ténèbres)
    ]

    success = 0
    
    print(f"{'INPUT CODE':<10} | {'EXPECTED ARABIC':<15} | {'RESULT':<10}")
    print("-" * 45)
    
    for latin, expected_arabic_start in test_vectors:
        # On normalise la comparaison (on cherche juste si la lettre clé est là)
        match_arabic = lex.get(latin, "MISSING")
        
        # Vérification basique de la première lettre arabe
        target_char = expected_arabic_start[0] # ex: 'د'
        
        if match_arabic == "MISSING":
            status = "❌ NOT FOUND"
        elif match_arabic.replace('-','').startswith(target_char):
            status = "✅ MATCH"
            success += 1
        else:
            status = f"⚠️ COLLISION ({match_arabic})"
            
        print(f"{latin:<10} | {match_arabic:<15} | {status}")

    print("-" * 45)
    print(f"SCORE : {success}/{len(test_vectors)}")
    if success == len(test_vectors):
        print("💎 CERTIFICATION : RÉSOLUTION SPECTRALE TOTALE.")
    else:
        print("🔧 ATTENTION : Des racines manquent ou sont mal encodées.")

if __name__ == "__main__":
    spectrum_test()

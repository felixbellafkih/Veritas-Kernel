import json
import os

def run_stress_test():
    lex_path = 'LEXICON.json'
    if not os.path.exists(lex_path):
        print("❌ Erreur : LEXICON.json introuvable.")
        return

    with open(lex_path, 'r', encoding='utf-8') as f:
        lexicon = json.load(f)['universal_functions']

    # Sélection de 10 vecteurs représentatifs des différentes couches
    test_roots = [
        "'-L-M", "S-L-W", "K-F-R", "Q-L-B", "H-Q-Q", 
        "A-M-R", "W-R-TH", "'-Z-Z", "B-Y-N", "KH-L-F"
    ]

    print("\n" + "="*80)
    print(f"{'RACINE':<12} | {'FONCTION LOGIQUE':<25} | {'PURETÉ':<8} | {'RATIO B/S'}")
    print("-" * 80)

    for target in test_roots:
        match = next((item for item in lexicon if target in item['root']), None)
        if match:
            # Calcul de pureté basé sur l'absence de mots-clés "bruit" (traditionnels)
            noise_keywords = ["dieu", "prière", "enfer", "paradis", "religion", "moral", "foi"]
            desc_lower = match['description'].lower()
            noise_count = sum(1 for word in noise_keywords if word in desc_lower)
            
            purity = 100 - (noise_count * 15) # Pénalité par mot bruyant
            purity = max(purity, 0)
            noise_ratio = 100 - purity
            
            print(f"{match['root'].split(' ')[0]:<12} | {match['logic_function']:<25} | {purity:>6}% | {noise_ratio:>3}% Bruit")
        else:
            print(f"{target:<12} | {'NON_INDEXÉ':<25} | {'0%':>6} | {'100%'} Bruit")

    print("="*80)
    print("MÉTRIQUE : 100% Pureté = Signal technique pur (Ghayr dhi 'iwaj).")

if __name__ == "__main__":
    run_stress_test()

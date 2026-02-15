import re

# Simulation de la logique de capture probable de v8.1.5
def inspect():
    token_a_trouver = "F-T-H"
    # Format actuel dans votre LEXICON : "ف-ت-ح (F-T-H)"
    entree_lexique = "ف-ت-ح (F-T-H)"
    
    # Test 1: Correspondance exacte (Échouera si espaces présents)
    print(f"Test Exact: {token_a_trouver == entree_lexique}")
    
    # Test 2: Recherche dans la chaîne
    print(f"Test 'In': {token_a_trouver in entree_lexique}")
    
    # Test 3: Décomposition (La méthode la plus probable pour v8.1.5)
    parts = entree_lexique.split(' ')
    print(f"Parts après split: {parts}")
    # Si le compilateur fait parts[1], il obtient '(F-T-H)' et non 'F-T-H' -> ÉCHEC

if __name__ == "__main__":
    inspect()

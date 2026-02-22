import re

# ==============================================================================
# MODULE: VERITAS LEXER (DETERMINISTIC TOKENIZER)
# ==============================================================================

# Dictionnaire des opérateurs systémiques (Particles & Pointers)
SYSTEM_OPERATORS = {
    # Opérateurs logiques
    "و": "OP_AND",       # Addition systémique / Parallélisme
    "ف": "OP_THEN",      # Séquence causale immédiate / Implication
    "او": "OP_OR",       # Bifurcation logique
    "ام": "OP_OR_X",     # OU Exclusif / Interrogation alternative
    
    # Pointeurs et Assertions
    "اياك": "PTR_EXCL",  # Pointeur de ciblage restrictif (Focus absolu)
    "ان": "SYS_ASSERT",  # Verrouillage de certitude (INNA)
    "لا": "OP_NOT",      # Négation absolue
    "لم": "OP_NOT_PAST", # Négation d'état antérieur
    "لن": "OP_NOT_FUT",  # Négation d'état futur
    "ما": "OP_NULL",     # Annulateur ou Pointeur générique (selon contexte)
    "قد": "SYS_VERIFY",  # Validation d'exécution
    
    # Vecteurs Spatiaux/Positionnels
    "على": "VEC_OVER",   # Vecteur de superposition / Charge
    "في": "ENV_IN",      # Encapsulation environnementale
    "من": "VEC_FROM",    # Point d'origine
    "الى": "VEC_TO",     # Cible / Terminaison
    "ب": "TOOL_WITH",    # Vecteur instrumental / Connexion
    "ل": "ALLOC_TO",     # Allocation / Appartenance
    "ك": "SIMIL_LIKE",   # Opérateur d'équivalence / Polymorphisme
}

# Liste des préfixes attachés (1 lettre) qui nécessitent une séparation chirurgicale
ATTACHED_PREFIXES = ["و", "ف", "ب", "ل", "ك"]

def strip_tashkeel(text: str) -> str:
    """Nettoie la chaîne de tous les diacritiques (voyelles) pour une analyse pure."""
    tashkeel_regex = re.compile(r'[\u0617-\u061A\u064B-\u0652]')
    return re.sub(tashkeel_regex, '', text)

def normalize_alef(text: str) -> str:
    """Normalise les différentes formes de Alef pour éviter les asymétries de correspondance."""
    text = re.sub(r'[إأآا]', 'ا', text)
    text = re.sub(r'ى', 'ي', text) # Normalisation Alif Maqsura vers Ya
    return text

def lex_verse(raw_verse: str) -> list:
    """
    Transforme un verset brut en une séquence d'instructions (Assembly Code).
    """
    clean_verse = normalize_alef(strip_tashkeel(raw_verse))
    raw_tokens = clean_verse.split()
    
    assembly_sequence = []
    
    for token in raw_tokens:
        # 1. Traitement des préfixes attachés (Ex: وَبِالْحَقِّ -> وَ + بِ + الحق)
        extracted_operators = []
        core_token = token
        
        # Détection séquentielle des préfixes (max 2, ex: Wa + Bi)
        for _ in range(2): 
            if len(core_token) > 2 and core_token[0] in ATTACHED_PREFIXES:
                prefix = core_token[0]
                extracted_operators.append({
                    "type": "OPERATOR",
                    "arabic": prefix,
                    "tag": SYSTEM_OPERATORS.get(prefix, "UNKNOWN_OP")
                })
                core_token = core_token[1:] # Détachement du préfixe
        
        # Ajout des opérateurs extraits à la séquence
        assembly_sequence.extend(extracted_operators)
        
        # 2. Vérification si le mot central est un opérateur indépendant
        if core_token in SYSTEM_OPERATORS:
            assembly_sequence.append({
                "type": "OPERATOR",
                "arabic": core_token,
                "tag": SYSTEM_OPERATORS[core_token]
            })
        else:
            # 3. Si ce n'est pas un opérateur, c'est une VARIABLE (Racine à traiter)
            assembly_sequence.append({
                "type": "VARIABLE",
                "arabic": core_token,
                "tag": "PENDING_ROOT_EXTRACTION"
            })
            
    return assembly_sequence

# Exemple d'exécution interne (Test Unitaire)
if __name__ == "__main__":
    # Test Fatiha partiel: "إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ"
    test_str = "إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ"
    result = lex_verse(test_str)
    for r in result:
        print(f"[{r['tag']}] : {r['arabic']}")
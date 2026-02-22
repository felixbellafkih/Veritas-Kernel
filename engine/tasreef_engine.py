import re

# ==============================================================================
# MODULE: TASREEF ENGINE (GABARITS ALGORITHMIQUES)
# ==============================================================================

# Matrice des gabarits (Wazn) et de leurs fonctions d'état (Ghayr dhi 'iwaj)
# Utilise les lettres modèles: F (Fa/Racine 1), A (Ayn/Racine 2), L (Lam/Racine 3)
TASREEF_MATRIX = {
    # 1. ÉTATS ACTIFS ET PASSIFS (PARTICIPES)
    r'^مَفْعُول$': {"tag": "SYS_TARGET", "logic_mod": "[PASSIVE_RECEPTACLE]", "desc": "L'objet subissant l'action (ex: Maktoub)"},
    r'^فَاعِل$': {"tag": "SYS_AGENT", "logic_mod": "[ACTIVE_EXECUTOR]", "desc": "L'entité exécutant l'action (ex: Katib)"},
    r'^فَعِيل$': {"tag": "SYS_CONST", "logic_mod": "[INHERENT_ATTRIBUTE]", "desc": "Attribut constant/intensif (ex: Rahim)"},
    
    # 2. VECTEURS ET INSTRUMENTS
    r'^مِفْعَال$': {"tag": "SYS_TOOL_MAX", "logic_mod": "[INSTRUMENTAL_VECTOR]", "desc": "L'outil amplifié de l'action"},
    r'^مَفْعَل$': {"tag": "SYS_NODE", "logic_mod": "[SPATIO_TEMP_NODE]", "desc": "Le lieu ou le temps de l'action (ex: Maktab)"},
    
    # 3. ÉTATS D'EXÉCUTION (VERBES)
    r'^فَعَلَ$': {"tag": "SYS_EXEC", "logic_mod": "[ACTION_INSTANTIATED]", "desc": "Action accomplie (ex: Kataba)"},
    r'^فُعِلَ$': {"tag": "SYS_PASSIVE_EXEC", "logic_mod": "[ACTION_SUSTAINED]", "desc": "Action subie (ex: Koutiba)"},
    
    # 4. INSTANCIATIONS MATÉRIELLES (NOMS)
    r'^فِعَال$': {"tag": "SYS_NOUN", "logic_mod": "[SYSTEMIC_INSTANTIATION]", "desc": "Le concept matérialisé (ex: Kitab)"},
    r'^فُعُول$': {"tag": "SYS_PLURAL_NOUN", "logic_mod": "[PLURAL_INSTANTIATION]", "desc": "Multiplicité du concept (ex: Koutoub)"},
}

# Modificateurs de Quantité (Suffixes)
QUANTIFIERS = {
    r'(ين|ان)$': {"tag": "SYS_DUAL", "logic_mod": "[DUAL_STATE]", "desc": "Bifurcation/Paire (ex: Kitabayn)"},
    r'(ون|ين|ات)$': {"tag": "SYS_PLURAL", "logic_mod": "[PLURAL_STATE]", "desc": "Multiplicité/Réseau"},
}

def analyze_pattern(raw_word: str, extracted_root: str) -> dict:
    """
    Compare le mot brut avec sa racine pour déduire la fonction d'état (Tasreef).
    Note: Nécessite un texte source avec voyelles (Tashkeel) pour une précision absolue,
    ou une analyse des consonnes ajoutées (M, T, A, etc.) si le texte est nu.
    """
    # Dans une version déterministe pure, on remplace les lettres de la racine 
    # dans le mot d'origine par F, A, L pour isoler le squelette.
    
    # Exemple simplifié pour la logique :
    # Si le mot contient un 'Mim' au début et 'Waw' avant la dernière lettre -> Maf'oul
    if raw_word.startswith('م') and len(raw_word) >= 4 and raw_word[-2] == 'و':
        return TASREEF_MATRIX[r'^مَفْعُول$']
        
    # Si le mot a un Alif après la première lettre de la racine -> Faa'il
    if len(raw_word) >= 4 and raw_word[1] == 'ا':
        return TASREEF_MATRIX[r'^فَاعِل$']
        
    # Par défaut, si aucun gabarit complexe n'est détecté
    return {"tag": "SYS_BASE", "logic_mod": "[RAW_DATA]", "desc": "Racine non modifiée"}

def extract_quantifiers(raw_word: str) -> list:
    """Détecte les états duels ou pluriels à la fin du mot."""
    mods = []
    for pattern, data in QUANTIFIERS.items():
        if re.search(pattern, raw_word):
            mods.append(data)
    return mods
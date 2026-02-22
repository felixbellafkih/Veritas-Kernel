import re

# ==============================================================================
# MODULE: TASREEF ENGINE (GABARITS ALGORITHMIQUES SUR SQUELETTE)
# ==============================================================================

def clean_skeleton(raw_word: str) -> str:
    """Purge le mot de tout bruit (Tashkeel, articles) pour isoler le rasm (squelette)."""
    text = re.sub(r'[\u0617-\u061A\u064B-\u0652\u0670]', '', raw_word)
    if text.startswith('ال') or text.startswith('ٱل'):
        text = text[2:]
    return text

def analyze_pattern(raw_word: str, fallback_root: str = "") -> dict:
    """
    Détecte la fonction d'état (Tasreef) avec une granularité haute résolution.
    """
    skeleton = clean_skeleton(raw_word)
    length = len(skeleton)

    # 0. OVERRIDE : CONSTANTES SYSTÉMIQUES ABSOLUES
    systemic_overrides = {
        'سم': {"tag": "SYS_PTR", "logic_mod": "[SYSTEM_POINTER]", "desc": "Pointeur d'instanciation (Ism)"},
        'اسم': {"tag": "SYS_PTR", "logic_mod": "[SYSTEM_POINTER]", "desc": "Pointeur d'instanciation (Ism)"},
        'له': {"tag": "SYS_CORE", "logic_mod": "[ABSOLUTE_CONSTANT]", "desc": "Autorité Racine (Allah)"},
        'الله': {"tag": "SYS_CORE", "logic_mod": "[ABSOLUTE_CONSTANT]", "desc": "Autorité Racine (Allah)"},
        'لله': {"tag": "SYS_CORE", "logic_mod": "[ABSOLUTE_CONSTANT]", "desc": "Autorité Racine (Allah)"},
        'اله': {"tag": "SYS_CORE", "logic_mod": "[ABSOLUTE_CONSTANT]", "desc": "Autorité Racine (Allah)"}
    }
    if skeleton in systemic_overrides:
        return systemic_overrides[skeleton]

    # 1. RACINES PURES (3 lettres ou moins)
    if length <= 3:
        return {"tag": "SYS_BASE", "logic_mod": "[BASE_VARIABLE]", "desc": "Noyau fondamental non modifié"}

    # 2. GABARITS À 4 LETTRES
    if length == 4:
        if skeleton[2] == 'ي': return {"tag": "SYS_CONST", "logic_mod": "[ACTIVE_FLOW]", "desc": "Attribut constant et continu (Fa'eel)"}
        if skeleton[3] == 'ن': return {"tag": "SYS_GLOBAL", "logic_mod": "[SYSTEM_ARCHITECTURE]", "desc": "Structure englobante ou saturation (Fa'laan)"}
        if skeleton[1] == 'ا': return {"tag": "SYS_AGENT", "logic_mod": "[ACTIVE_EXECUTOR]", "desc": "Entité exécutant l'action (Faa'il)"}
        if skeleton[0] == 'م': return {"tag": "SYS_NODE", "logic_mod": "[SPATIO_TEMP_NODE]", "desc": "Lieu, temps ou vecteur de l'action (Maf'al)"}
        # EXÉCUTION DYNAMIQUE (Mudari') : ex نعبد (N-A-B-D), يعلم (Y-A-L-M)
        if skeleton[0] in ['ن', 'ي', 'ت', 'أ']:
            return {"tag": "SYS_EXEC", "logic_mod": "[DYNAMIC_EXECUTION]", "desc": "Action dynamique instanciée (Mudari')"}

    # 3. GABARITS À 5 LETTRES
    if length == 5:
        if skeleton[0] == 'م' and skeleton[3] == 'و': return {"tag": "SYS_TARGET", "logic_mod": "[PASSIVE_RECEPTACLE]", "desc": "Objet subissant l'action (Maf'ool)"}
        if skeleton[3] == 'ا' and skeleton[4] == 'ن': return {"tag": "SYS_GLOBAL", "logic_mod": "[SYSTEM_ARCHITECTURE]", "desc": "Structure englobante (Fa'laan)"}

    # 4. GABARITS À 6 LETTRES (Forme X / IST-)
    if length == 6:
        # Détection des préfixes de demande: است (A-S-T), نست (N-S-T), يست (Y-S-T), تست (T-S-T)
        if skeleton.startswith(('است', 'نست', 'يست', 'تست')):
            return {"tag": "SYS_REQ", "logic_mod": "[REQUEST_PROTOCOL]", "desc": "Protocole d'initialisation ou de requête (Forme X)"}

    return {"tag": "SYS_BASE", "logic_mod": "[BASE_VARIABLE]", "desc": "État complexe ou racine non standard"}

def extract_quantifiers(raw_word: str) -> list:
    skeleton = clean_skeleton(raw_word)
    mods = []
    if skeleton.endswith('ين') or skeleton.endswith('ان'): mods.append({"tag": "SYS_DUAL", "logic_mod": "[DUAL_STATE]", "desc": "Bifurcation / Paire"})
    elif skeleton.endswith('ون') or skeleton.endswith('ات'): mods.append({"tag": "SYS_PLURAL", "logic_mod": "[PLURAL_STATE]", "desc": "Multiplicité / Réseau"})
    return mods
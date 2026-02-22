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
    Détecte la fonction d'état (Tasreef). Gère les gabarits et les constantes absolues.
    """
    skeleton = clean_skeleton(raw_word)
    length = len(skeleton)

    # 0. OVERRIDE : CONSTANTES SYSTÉMIQUES ABSOLUES
    # Remplacement du [RAW_DATA] par des états fonctionnels précis
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
        # On remplace RAW_DATA par BASE_VARIABLE pour un rendu plus propre
        return {"tag": "SYS_BASE", "logic_mod": "[BASE_VARIABLE]", "desc": "Noyau fondamental non modifié"}

    # 2. GABARITS À 4 LETTRES (Les plus fréquents)
    if length == 4:
        # Fa'eel (فعيل) - Constance / Flux continu : ex رحيم (R-H-Y-M) -> 3ème lettre = ي
        if skeleton[2] == 'ي':
            return {"tag": "SYS_CONST", "logic_mod": "[ACTIVE_FLOW]", "desc": "Attribut constant et continu (Fa'eel)"}
        
        # Fa'laan (فعلان) - Architecture / Saturation : ex رحمن (R-H-M-N) -> 4ème lettre = ن
        if skeleton[3] == 'ن':
            return {"tag": "SYS_GLOBAL", "logic_mod": "[SYSTEM_ARCHITECTURE]", "desc": "Structure englobante ou saturation (Fa'laan)"}
        
        # Faa'il (فاعل) - Agent actif : ex كاتب (K-A-T-B) -> 2ème lettre = ا
        if skeleton[1] == 'ا':
            return {"tag": "SYS_AGENT", "logic_mod": "[ACTIVE_EXECUTOR]", "desc": "Entité exécutant l'action (Faa'il)"}
            
        # Maf'al (مفعل) - Noeud / Vecteur : ex مكتب (M-K-T-B) -> 1ère lettre = م
        if skeleton[0] == 'م':
            return {"tag": "SYS_NODE", "logic_mod": "[SPATIO_TEMP_NODE]", "desc": "Lieu, temps ou vecteur de l'action (Maf'al)"}

    # 3. GABARITS À 5 LETTRES
    if length == 5:
        # Maf'ool (مفعول) - Cible passive : ex مكتوب (M-K-T-W-B) -> 1ère = م, 4ème = و
        if skeleton[0] == 'م' and skeleton[3] == 'و':
            return {"tag": "SYS_TARGET", "logic_mod": "[PASSIVE_RECEPTACLE]", "desc": "Objet subissant l'action (Maf'ool)"}
            
        # Fa'laan (فعلان avec Alif) : ex رحمان (R-H-M-A-N) -> 4ème = ا, 5ème = ن
        if skeleton[3] == 'ا' and skeleton[4] == 'ن':
            return {"tag": "SYS_GLOBAL", "logic_mod": "[SYSTEM_ARCHITECTURE]", "desc": "Structure englobante ou saturation (Fa'laan)"}

    # Fallback si le gabarit n'est pas mathématiquement reconnu
    return {"tag": "SYS_BASE", "logic_mod": "[BASE_VARIABLE]", "desc": "État complexe ou racine non standard"}   

def extract_quantifiers(raw_word: str) -> list:
    """Détecte les états duels ou pluriels à la fin du mot."""
    skeleton = clean_skeleton(raw_word)
    mods = []
    # Vérification stricte des suffixes de quantité
    if skeleton.endswith('ين') or skeleton.endswith('ان'):
        mods.append({"tag": "SYS_DUAL", "logic_mod": "[DUAL_STATE]", "desc": "Bifurcation / Paire"})
    elif skeleton.endswith('ون') or skeleton.endswith('ات'):
        mods.append({"tag": "SYS_PLURAL", "logic_mod": "[PLURAL_STATE]", "desc": "Multiplicité / Réseau"})
    return mods
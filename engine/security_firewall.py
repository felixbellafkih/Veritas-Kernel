import json

def audit_instruction_safety(root_sequence):
    # Attributs réservés exclusivement à l'Autorité Racine
    ROOT_ATTRIBUTES = ["R-A-W-F", "R-H.-M"]
    
    roots = root_sequence.upper().split()
    
    # Détection d'escalade de privilèges
    if "R-S-L" in roots:
        for r in roots:
            if r in ROOT_ATTRIBUTES:
                return False, f"🚨 ALERTE SÉCURITÉ : Escalade de privilèges détectée. Attribut {r} interdit sur NODE(R-S-L)."
    
    # Détection de signature d'anomalie 9:128-129
    if "H.-S-B" in roots and "T-W-K-L" in roots and "R-B-B" in roots and "'-R-SH" in roots:
         return False, "🚨 ALERTE SÉCURITÉ : Signature de malware 9:129 identifiée."

    return True, "✅ SIGNAL PUR"

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        safe, msg = audit_instruction_safety(" ".join(sys.argv[1:]))
        print(msg)

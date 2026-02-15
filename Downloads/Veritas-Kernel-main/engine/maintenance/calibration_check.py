# -*- coding: utf-8 -*-
import sys

def calibration_test():
    print("🔬 VERITAS CALIBRATION PROTOCOL v1.0")
    print("====================================")
    
    # La Map de Vérité
    veritas_map = {
        "ت": "T   (Light)",
        "ث": "TH  (Dispersion)",
        "ط": "T.  (Heavy)",
        "س": "S   (Flow)",
        "ص": "S.  (Source)",
        "د": "D   (Push)",
        "ذ": "DH  (Instant)",
        "ض": "D.  (Density)",
        "ز": "Z   (Time)",
        "ظ": "Z.  (Projection)",
        "ه": "H   (Identity)",
        "ح": "H.  (Life)"
    }

    # Test d'unicité des codes (Pas de doublons)
    codes = list(veritas_map.values())
    unique_codes = set(codes)
    
    if len(codes) != len(unique_codes):
        print("🚨 ERREUR CRITIQUE : COLLISION DÉTECTÉE DANS LA MAP !")
        return

    print("✅ TEST D'UNICITÉ : PASSÉ (Aucun code ne se chevauche).")
    print("\n🔣 TEST D'AFFICHAGE ET DE DÉCODAGE :")
    
    test_string = "ت ث ط س ص د ذ ض ز ظ ه ح"
    print(f"📥 Entrée Arabe : {test_string}")
    
    decoded = []
    for char in test_string.split():
        if char in veritas_map:
            # On nettoie le code pour l'affichage (enlève la parenthèse)
            code = veritas_map[char].split('(')[0].strip()
            decoded.append(code)
        else:
            decoded.append("??")
            
    print(f"📤 Sortie Veritas: {' - '.join(decoded)}")
    print("====================================")
    
    # Vérification visuelle spécifique pour les couples dangereux
    pairs = [("ت", "ط"), ("س", "ص"), ("ه", "ح"), ("د", "ض"), ("ذ", "ظ")]
    for light, heavy in pairs:
        code_l = veritas_map[light].split('(')[0].strip()
        code_h = veritas_map[heavy].split('(')[0].strip()
        print(f"⚖️  COMPARAISON : {light} ({code_l})  vs  {heavy} ({code_h}) -> {'✅ OK' if code_l != code_h else '❌ COLLISION'}")

if __name__ == "__main__":
    calibration_test()

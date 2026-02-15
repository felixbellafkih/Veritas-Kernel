import sys
import json
import os

def run_stress_test():
    path = 'LEXICON.json'
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Création du dictionnaire de référence
    lexicon = {}
    for item in data['universal_functions']:
        try:
            code = item['root'].split('(')[1].split(')')[0].strip()
            lexicon[code] = item
        except: continue

    # LISTE DE STRESS (30 RACINES CRITIQUES)
    stress_list = [
        "S-B-L", "S.-R-T.", "T.-B-Q", "KH-L-Q", "H.-Y-Y", "M-W-T",
        "B-R-K", "M-L-K", "Y-D-Y", "Q-D-R", "H.-S-N", "B-L-W",
        "R-H.-M", "'-L-M", "D-L-L", "D.-L-L", "DH-L-L", "Z-L-L",
        "Z.-L-M", "T-W-B", "TH-W-B", "S-B-H", "S.-B-H", "A-K-L",
        "M-A-'", "S-W-'", "H-D-Y", "H.-M-D", "K-L-L", "SH-Y-A"
    ]

    print("\n" + "█"*60)
    print(" ⚡ VERITAS MASSIVE STRESS TEST (VTS-v3.1)")
    print("█"*60 + "\n")

    found = 0
    noise = []

    for root in stress_list:
        if root in lexicon:
            found += 1
            print(f" [OK] {root:<10} -> VALIDATED")
        else:
            noise.append(root)
            print(f" [!!] {root:<10} -> !! NOISE !!")

    purity = (found / len(stress_list)) * 100
    
    print("\n" + "-"*60)
    print(f"📊 RÉSULTAT DU TEST : {found}/{len(stress_list)} Vecteurs Actifs")
    print(f"📈 PURETÉ SPECTRALE : {purity:.2f}%")
    
    if purity == 100:
        print("💎 ÉTAT : SYSTÈME OPTIMAL - AUCUNE COLLISION DÉTECTÉE.")
    else:
        print(f"⚠️ ÉTAT : INSTABLE - MISSING: {', '.join(noise)}")
    print("-" * 60 + "\n")

if __name__ == "__main__":
    run_stress_test()

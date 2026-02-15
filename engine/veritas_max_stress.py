import json
import os
import time

def run_max_stress():
    print("\n" + "█"*70)
    print(" ⚡ VERITAS-KERNEL : MAXIMAL STRESS TEST (A/Ain Integrity Check)")
    print("█"*70 + "\n")

    # 1. CHARGEMENT DU LEXIQUE STANDARDISE
    path = 'LEXICON.json'
    if not os.path.exists(path):
        print("❌ CRITICAL: LEXICON MISSING")
        return

    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Création d'une map ultra-rapide basée sur le CODE STANDARD (ex: "A-K-L")
    # On extrait ce qu'il y a entre parenthèses dans le fichier JSON
    lex_map = {}
    for item in data['universal_functions']:
        try:
            # Format attendu : "أ-ك-ل (A-K-L)" -> on veut "A-K-L"
            code = item['root'].split('(')[1].split(')')[0].strip()
            lex_map[code] = item
        except:
            continue

    print(f"📚 BASE DE DONNÉES : {len(lex_map)} Racines Standardisées chargées.")
    print("-" * 70)

    # 2. LA SÉQUENCE "GRAND SLAM" (100 Racines mélangées)
    # Contient des pièges A/' et des concepts de toutes les couches.
    sequence = [
        # --- HARDWARE & PHYSIQUE ---
        "A-R-D", "S-M-W", "J-B-L", "B-H-R", "N-H-R", "SH-M-S", "Q-M-R", "N-J-M", 
        "L-Y-L", "N-H-R", "M-A-'", "H-D-D", "T-Y-N", "R-S-Y", "F-J-J",
        
        # --- KERNEL & COMMANDE (Test A vs ') ---
        "A-M-R", "'-M-L",  # <--- PIÈGE : Amr (Ordre) vs 'Amal (Travail)
        "A-L-M", "'-L-M",  # <--- PIÈGE : Alim (Douleur) vs 'Ilm (Savoir)
        "A-K-L", "'-Q-L",  # <--- PIÈGE : Akl (Manger) vs 'Aql (Raison)
        "A-H-D", "W-H-D",  # <--- Unicité
        "R-B-B", "M-L-K", "H-K-M", "Q-L-B", "K-R-S", "'-R-SH",
        
        # --- RESEAU & DATA ---
        "K-L-M", "K-T-B", "Q-R-A", "N-B-A", "W-H-Y", "R-S-L", "N-Z-L",
        "H-F-Z", "S-T-R", "K-T-M", "B-D-W", "Z-H-R", "B-T-N",
        
        # --- TRANSACTION & ETATS ---
        "D-Y-N", "B-Y-'", "T-J-R", "K-S-B", "R-Z-Q", "M-Y-Z", "W-F-Y",
        "H-S-B", "H-Q-Q", "B-T-L", "S-L-H", "F-S-D", "T-M-M",
        
        # --- SECURITE & BUG ---
        "H-F-Z", "W-Q-Y", "S-W-R", "J-N-N", "R-J-M", "L-G-H", "N-S-Y",
        "K-F-R", "Z-L-L", "F-T-N", "Q-T-L", "M-W-T", "H-Y-Y", "B-'-TH",
        
        # --- SENSORS & I/O ---
        "S-M-'", "B-S-R", "L-M-S", "DH-W-Q", "N-T-Q", "F-Q-H", "SH-H-D",
        "Q-W-L", "S-A-L", "J-W-B", "D-'-W", "A-DH-N", "Z-K-W"
    ]

    # 3. EXÉCUTION DU TEST
    hits = 0
    misses = []
    
    print(f"🚀 LANCEMENT DU SCAN SUR {len(sequence)} VECTEURS...")
    print("-" * 70)

    # Affichage en grille pour la vitesse
    line_buffer = ""
    for i, root in enumerate(sequence):
        status = "✅" if root in lex_map else "❌"
        
        if root in lex_map:
            hits += 1
        else:
            misses.append(root)

        # Formatage visuel (ex: "A-M-R [✅]")
        line_buffer += f"{root:<6} {status}  "
        
        if (i + 1) % 5 == 0:
            print(line_buffer)
            line_buffer = ""
            time.sleep(0.02) # Petit effet visuel matrix

    if line_buffer: print(line_buffer)
    
    # 4. RAPPORT FINAL
    score = (hits / len(sequence)) * 100
    print("-" * 70)
    print(f"📊 RÉSULTAT FINAL : {score:.2f}% DE COUVERTURE")
    
    if misses:
        print(f"⚠️ VECTEURS PERDUS ({len(misses)}) : {', '.join(misses)}")
        print("DIAGNOSTIC : Le standardisateur n'a pas couvert ces racines ou elles manquent au Lexique.")
    else:
        print("💎 SUCCÈS TOTAL : LE NOYAU EST ROBUSTE ET STANDARDISE.")
        print("   La distinction A (Alif) vs ' (Ain) est opérationnelle.")

if __name__ == "__main__":
    run_max_stress()

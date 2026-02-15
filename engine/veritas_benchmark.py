import json
import os

def load_strict_lexicon():
    path = 'LEXICON.json'
    if not os.path.exists(path): return None
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # On crée une map qui ne reconnait QUE les codes entre parenthèses
    # Exemple : "أ-ك-ل (A-K-L)" -> Clé : "A-K-L"
    strict_map = {}
    for item in data['universal_functions']:
        root_full = item['root']
        if '(' in root_full and ')' in root_full:
            # Extraction propre de ce qu'il y a entre parenthèses
            code = root_full.split('(')[1].split(')')[0].strip().upper()
            strict_map[code] = item
            
            # Alias sans tirets pour la tolérance (A-K-L -> AKL)
            # MAIS on garde le A et le ' !!!
            code_clean = code.replace('-', '')
            if code_clean not in strict_map:
                strict_map[code_clean] = item

    return strict_map

def run_benchmark():
    lexicon = load_strict_lexicon()
    if not lexicon:
        print("❌ CRITICAL: LEXICON MISSING")
        return

    # SCÉNARIOS (Syntaxe EXACTE requise : A-X-X ou '-X-X)
    scenarios = {
        "SCENARIO_A [BOOT_SEQUENCE]": {
            "description": "Al-Fatiha (Precision Mode)",
            # Notez l'usage précis de ' (Ain) vs A (Alif)
            "sequence": "H-M-D R-B-B '-L-M R-H-M M-L-K D-Y-N '-B-D '-W-N H-D-Y S-R-T Q-W-M",
        },
        "SCENARIO_B [SYSTEM_CRASH]": {
            "description": "Adam & Iblis (Precision Mode)",
            "sequence": "Q-W-L H-B-T '-D-W W-S-W-S Z-L-L A-K-L SH-J-R B-D-W S-W-' T-W-B",
        },
        "SCENARIO_C [PHYSICS_ENGINE]": {
            "description": "Big Bang (Precision Mode)",
            "sequence": "K-F-R R-T-Q F-T-Q M-A-' H-Y-Y J-B-L R-S-Y F-J-J",
        },
        "SCENARIO_D [DATA_ENCRYPTION]": {
            "description": "Kahf (Precision Mode)",
            "sequence": "H-S-B K-H-F R-Q-M A-Y-Y A-W-Y F-T-Y R-H-M H-Y-Y",
        }
    }

    print("\n" + "█"*60)
    print(f" ⚡ VERITAS-KERNEL BENCHMARK (v2.0 - LITERAL ENGINE)")
    print(f" 📚 Strict Keys : {len(lexicon)}")
    print("█"*60 + "\n")

    total_score = 0
    
    for name, data in scenarios.items():
        print(f"Running: {name}")
        tokens = data['sequence'].split()
        hits = 0
        unknowns = []
        
        for t in tokens:
            target = t.upper() # Pas de suppression de voyelles !
            
            if target in lexicon:
                hits += 1
                match = lexicon[target]
                arabic = match['root'].split('(')[0].strip()
                print(f"  [OK] {t:<6} -> {arabic:<8} : {match['logic_function']}")
            else:
                # Fallback : Essai sans tirets (A-K-L -> AKL)
                target_clean = target.replace('-', '')
                if target_clean in lexicon:
                    hits += 1
                    match = lexicon[target_clean]
                    arabic = match['root'].split('(')[0].strip()
                    print(f"  [OK] {t:<6} -> {arabic:<8} : {match['logic_function']}")
                else:
                    unknowns.append(t)
                    print(f"  [!!] {t:<6} -> UNKNOWN_SIGNAL")

        purity = (hits / len(tokens)) * 100
        total_score += purity
        status = "✅ PASS" if purity == 100 else "⚠️ WARN"
        print("-" * 60)
        print(f"RESULT: {status} | PURITY: {purity:.1f}%")
        if unknowns: print(f"MISSING: {', '.join(unknowns)}")
        print("\n")

    print("="*60)
    avg = total_score / len(scenarios)
    print(f"📊 GLOBAL SYSTEM INTEGRITY: {avg:.2f}%")
    if avg == 100:
        print("💎 CERTIFICATION: GHAYR DHI 'IWAJ (NO DISTORTION)")
    print("="*60)

if __name__ == "__main__":
    run_benchmark()

import sys
import json

# Mapping unifié - Version 8.1.8 (Standardisé)
VERITAS_MAP = {
    'A': 'أ', 'B': 'ب', 'T': 'ت', 'TH': 'ث', 'J': 'ج', 'H.': 'ح', 'KH': 'خ',
    'D': 'د', 'DH': 'ذ', 'R': 'ر', 'Z': 'ز', 'S': 'س', 'SH': 'ش', 'S.': 'ص',
    'D.': 'ض', 'T.': 'ط', 'Z.': 'ظ', "'": 'ع', 'G': 'غ', 'F': 'ف', 'Q': 'ق',
    'K': 'ك', 'L': 'ل', 'M': 'م', 'N': 'ن', 'H': 'ه', 'W': 'و', 'Y': 'ي',
    '*': 'ء'
}

def to_arabic(root_latin):
    # Découpage strict par le tiret pour protéger KH, TH, SH, DH, etc.
    parts = root_latin.upper().split('-')
    return "".join([VERITAS_MAP.get(p, p) for p in parts])

def compile_report(input_roots):
    try:
        with open('LEXICON.json', 'r', encoding='utf-8') as f:
            lexicon = json.load(f)
        
        db = {item['root'].upper(): item for item in lexicon['universal_functions']}
        
        print(f"\n --- RAPPORT DE COMPILATION VERITAS v8.1.8 ---")
        found_count = 0
        roots_list = input_roots.split()

        for r in roots_list:
            r_upper = r.upper()
            arabic = to_arabic(r_upper)
            match = db.get(r_upper)
            
            if match:
                func = match['logic_function']
                print(f" -> {r_upper:<12} ({arabic:<4}) => {func}")
                found_count += 1
            else:
                print(f" -> !! NOISE !! ({r_upper:<12}) => UNKNOWN_SIGNAL")

        purity = (found_count / len(roots_list)) * 100
        print(f"\n Tokens : {len(roots_list)} | Signaux : {found_count} | Pureté : {purity:.2f}%")

    except Exception as e:
        print(f"ERREUR SYSTÈME : {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        compile_report(sys.argv[1])
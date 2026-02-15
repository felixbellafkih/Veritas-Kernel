import json
import sys
import os
import re

def clean_arabic(text):
    # Nettoyage basique des voyelles (Tashkeel) pour garder la racine brute
    return re.sub(r'[\u064B-\u0652]', '', text)

def parse_sentence(sentence):
    lex_path = 'LEXICON.json'
    with open(lex_path, 'r', encoding='utf-8') as f:
        lexicon = json.load(f)['universal_functions']
    
    words = sentence.split()
    print(f"\n--- COMPILATION VERITAS-KERNEL ---")
    print(f"ENTRÉE : {sentence}\n")
    
    for word in words:
        clean_word = clean_arabic(word)
        # On cherche si une racine du lexicon est contenue dans le mot (Mapping)
        match = None
        for item in lexicon:
            arabic_root = item['root'].split(' ')[0].replace('-', '')
            if arabic_root in clean_word:
                match = item
                break
        
        if match:
            print(f"[{word}] -> {match['logic_function']}")
        else:
            print(f"[{word}] -> ?? (NO_ROOT_MAPPED)")
    
    print(f"\n--- FIN DE COMPILATION ---")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        parse_sentence(" ".join(sys.argv[1:]))
    else:
        print("Usage: python engine/veritas_parser.py [TEXTE_ARABE]")

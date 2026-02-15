import json
import os

class VeritasTranslator:
    def __init__(self, lexicon_path='LEXICON.json'):
        self.mapping = self._load_lexicon(lexicon_path)

    def _load_lexicon(self, path):
        if not os.path.exists(path):
            print(f"❌ Erreur : {path} introuvable.")
            return {}
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            # Indexation chirurgicale par le code entre parenthèses
            return {
                item['root'].split('(')[1].split(')')[0].strip(): item 
                for item in data['universal_functions'] if '(' in item['root']
            }

    def translate(self, sequence):
        tokens = sequence.upper().split()
        results = []
        for t in tokens:
            if t in self.mapping:
                func = self.mapping[t]['logic_function']
                results.append(f"[{t} \u279e {func}]")
            else:
                results.append(f"[{t} \u279e !! NOISE !!]")
        return " ".join(results)

if __name__ == "__main__":
    import sys
    translator = VeritasTranslator()
    if len(sys.argv) > 1:
        # Reconstitution de la chaîne d'entrée
        input_signal = " ".join(sys.argv[1:])
        print(f"\n\u26a1 VERITAS OUTPUT : {translator.translate(input_signal)}\n")
    else:
        print("\u26a0\ufe0f Usage: python engine/translation_engine.py \"ROOT1 ROOT2 ...\"")

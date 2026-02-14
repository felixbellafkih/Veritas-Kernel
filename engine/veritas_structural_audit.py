import json
import re
import sys

class StructuralAuditor:
    def __init__(self, lexicon_path='LEXICON.json'):
        try:
            with open(lexicon_path, 'r', encoding='utf-8') as f:
                self.lexicon = json.load(f)
            self.functions = self.lexicon.get("universal_functions", [])
            self.version = "6.3.4"
        except Exception as e:
            print(f"[!] Erreur : {e}")
            sys.exit(1)

    def audit(self, text):
        words = re.findall(r'[\w-]+', text.upper())
        total_tokens = len(words)
        signals = []
        
        # On crée une carte de recherche globale pour ne rien rater
        search_map = {}
        for entry in self.functions:
            ids = re.findall(r'[\w-]+', entry['root'].upper())
            for identifier in ids:
                search_map[identifier] = entry['logic_function']

        # On vérifie chaque mot du texte un par un
        for word in words:
            if word in search_map:
                signals.append({"id": word, "f": search_map[word]})

        purity = (len(signals) / total_tokens) * 100 if total_tokens > 0 else 0
        print(f"--- RAPPORT VERITAS v{self.version} ---")
        print(f"Tokens : {total_tokens} | Signaux : {len(signals)} | Pureté : {purity:.2f}%")
        for s in signals:
            print(f" -> [{s['id']}] : {s['f']}")
        return purity

if __name__ == "__main__":
    auditor = StructuralAuditor()
    if len(sys.argv) > 1:
        auditor.audit(sys.argv[1])

import json
import re
import sys

class StructuralAuditor:
    def __init__(self, lexicon_path='LEXICON.json'):
        try:
            with open(lexicon_path, 'r', encoding='utf-8') as f:
                self.lexicon = json.load(f)
            self.functions = self.lexicon.get("universal_functions", [])
            self.version = self.lexicon.get('version', '6.3.3')
        except Exception as e:
            print(f"[!] Erreur critique : {e}")
            sys.exit(1)

    def audit(self, text):
        # Segmentation supportant les racines avec tirets
        words = re.findall(r'[\w-]+', text.upper())
        total_tokens = len(words)
        signals = []
        
        for entry in self.functions:
            root_raw = entry['root'].upper()
            identifiers = re.findall(r'[\w-]+', root_raw)
            for identifier in identifiers:
                if identifier in words:
                    count = words.count(identifier)
                    for _ in range(count):
                        signals.append({"id": identifier, "f": entry['logic_function']})
                    break

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
    else:
        print("[!] Aucun input.")

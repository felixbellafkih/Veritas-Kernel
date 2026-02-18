import json
import re
import sys

class StructuralAuditor:
    def __init__(self, lexicon_path='LEXICON.json'):
        try:
            with open(lexicon_path, 'r', encoding='utf-8') as f:
                self.lexicon = json.load(f)
            self.functions = self.lexicon.get("universal_functions", [])
        except FileNotFoundError:
            print("[!] Erreur : LEXICON.json introuvable.")
            sys.exit(1)

    def audit(self, text):
        words = re.findall(r'\w+', text)
        total_words = len(words)
        signals_detected = []
        
        for entry in self.functions:
            root_raw = entry['root']
            # Extraction des identifiants (Arabe et Latin)
            identifiers = re.findall(r'[\w-]+', root_raw)
            
            for identifier in identifiers:
                clean_id = identifier.replace('-', '')
                pattern = "".join([f"{c}[\\-\\s]?" for c in clean_id])
                matches = re.findall(pattern, text, re.IGNORECASE)
                if matches:
                    for _ in matches:
                        signals_detected.append({
                            "root": identifier,
                            "function": entry['logic_function']
                        })
                    break

        signal_count = len(signals_detected)
        noise_count = total_words - signal_count
        # Calcul du Ratio de Pureté
        purity = (signal_count / total_words) * 100 if total_words > 0 else 0

        print(f"--- RAPPORT D'AUDIT STRUCTUREL v{self.lexicon.get('version')} ---")
        print(f"Texte analysé : \"{text[:50]}...\"")
        print(f"Total mots : {total_words}")
        print(f"Signaux (Racines) : {signal_count}")
        print(f"Bruit (Entropie) : {noise_count}")
        print(f"Indice de Pureté : {purity:.2f}%")
        print("-" * 40)
        
        if signals_detected:
            print("Séquence Logique détectée :")
            for s in signals_detected:
                print(f" -> [{s['root']}] : {s['function']}")
        
        return purity

if __name__ == "__main__":
    auditor = StructuralAuditor()
    sample = sys.argv[1] if len(sys.argv) > 1 else ""
    auditor.audit(sample)

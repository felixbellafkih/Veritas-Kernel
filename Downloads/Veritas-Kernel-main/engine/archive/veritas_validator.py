import json
import re
import sys

class VeritasValidator:
    def __init__(self, lexicon_path='LEXICON.json'):
        try:
            with open(lexicon_path, 'r', encoding='utf-8') as f:
                self.lexicon = json.load(f)
            self.version = self.lexicon.get('version', 'unknown')
            self.functions = self.lexicon.get('universal_functions', [])
        except FileNotFoundError:
            print("[!] Erreur Fatale : LEXICON.json introuvable.")
            sys.exit(1)

    def analyze_text(self, text):
        results = []
        for item in self.functions:
            root_raw = item['root'] # Ex: "س-ل-م (Islam/Salam)"
            
            # Extraction chirurgicale des identifiants (Arabe et Latin)
            # On récupère tout ce qui ressemble à des lettres ou tirets
            identifiers = re.findall(r'[\w-]+', root_raw)
            
            for identifier in identifiers:
                # Création d'un pattern flexible (insensible à la casse / tirets optionnels)
                clean_id = identifier.replace('-', '')
                pattern = "".join([f"{c}[\\-\\s]?" for c in clean_id])
                
                if re.search(pattern, text, re.IGNORECASE):
                    results.append({
                        "id": identifier,
                        "function": item['logic_function'],
                        "desc": item['description']
                    })
                    break # On évite de compter deux fois la même racine
        return results

    def integrity_check(self, data_input):
        print(f"--- ANALYSE VERITAS v{self.version} ---")
        if not data_input:
            print("[!] Erreur : Aucun texte fourni en argument.")
            return

        detections = self.analyze_text(data_input)
        
        if not detections:
            print(f"[!] Aucun signal source détecté dans : '{data_input}'")
            return

        for d in detections:
            print(f"[OK] Signal: {d['id']} | Fonction: {d['function']}")
            print(f"     └─ Bio-Logic: {d['desc']}")
        
        print(f"--- FIN D'ANALYSE : {len(detections)} SIGNAUX VALIDÉS ---")

if __name__ == "__main__":
    validator = VeritasValidator()
    # Récupère le texte passé dans le terminal, sinon utilise le texte par défaut
    input_text = sys.argv[1] if len(sys.argv) > 1 else "La synchronisation (SLM) nécessite une liaison (SLW) constante."
    validator.integrity_check(input_text)

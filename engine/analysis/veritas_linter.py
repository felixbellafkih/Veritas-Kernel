import json
import os
import sys

class VeritasLinter:
    def __init__(self, lexicon_path='LEXICON.json'):
        try:
            with open(lexicon_path, 'r', encoding='utf-8') as f:
                self.kernel = json.load(f)
        except Exception as e:
            print(f"[ERROR] Kernel Lexicon critical failure: {e}")
            sys.exit(1)

        self.noise_terms = ["hadith", "consensus", "tradition", "jurisprudence", "sunnah", "ijma"]
        self.v7_requirements = ["status", "version", "universal_functions"]
        # Mots-clés qui indiquent que le bruit est cité pour être traité/converti
        self.safe_contexts = ["rejet", "invalidation", "bruit", "noise", "injections", "legacy", "mapping", "conversion"]

    def validate_kernel_integrity(self):
        missing = [req for req in self.v7_requirements if req not in self.kernel]
        return missing

    def check_noise_with_context(self, text):
        detected_noise = []
        lines = text.lower().split('\n')
        for line in lines:
            for term in self.noise_terms:
                if term in line:
                    # Si la ligne contient un mot-clé de traitement, on ignore l'alerte
                    if any(ctx in line for ctx in self.safe_contexts):
                        continue
                    detected_noise.append(term)
        return list(set(detected_noise))

    def validate_file(self, file_path):
        errors = []
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        noise = self.check_noise_with_context(content)
        if noise:
            errors.append(f"LOGIC_EXCEPTION: Unsanitized historical noise: {noise}")
        return errors

def run():
    linter = VeritasLinter()
    if linter.validate_kernel_integrity():
        print(f"[X] KERNEL ERROR: Missing v7 components")
        sys.exit(1)

    md_files = [f for f in os.listdir('.') if f.endswith('.md')]
    for md in md_files:
        issues = linter.validate_file(md)
        if issues:
            print(f"[X] {md} : FAILED -> {issues}")
            sys.exit(1)
        print(f"[V] {md} : CONFORME")

    print(f"\n[SUCCÈS] Veritas Kernel v{linter.kernel.get('version')} validé.")

if __name__ == "__main__":
    run()
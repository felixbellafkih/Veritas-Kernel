import json
import os
import sys

class VeritasLinter:
    def __init__(self, lexicon_path='LEXICON.json'):
        # On pointe maintenant vers le LEXICON qui contient la version
        try:
            with open(lexicon_path, 'r', encoding='utf-8') as f:
                self.kernel = json.load(f)
        except Exception as e:
            print(f"[ERROR] Kernel Lexicon critical failure: {e}")
            sys.exit(1)

        # Termes à surveiller, mais avec une détection de contexte
        self.noise_terms = ["hadith", "consensus", "tradition", "jurisprudence", "sunnah", "ijma"]
        self.v7_requirements = ["status", "version", "universal_functions"]

    def validate_kernel_integrity(self):
        """Vérifie que le lexique respecte les standards v7."""
        missing = [req for req in self.v7_requirements if req not in self.kernel]
        return missing

    def check_noise_with_context(self, text):
        """
        Filtre anti-entropie sémantique intelligent.
        Ignore le terme s'il est précédé de 'rejet', 'invalidation' ou s'il est dans une liste de définition.
        """
        detected_noise = []
        lines = text.lower().split('\n')
        for line in lines:
            for term in self.noise_terms:
                if term in line:
                    # Si la ligne définit le bruit, on autorise
                    if any(x in line for x in ["rejet", "invalidation", "bruit", "noise", "injections"]):
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
    # Initialisation sur le LEXICON.json (Source de vérité v7)
    linter = VeritasLinter()

    # 1. Audit de l'Intégrité du Noyau
    missing = linter.validate_kernel_integrity()
    if missing:
        print(f"[X] KERNEL ERROR: Missing v7 components: {missing}")
        sys.exit(1)

    # 2. Audit des Fichiers Markdown
    md_files = [f for f in os.listdir('.') if f.endswith('.md')]
    for md in md_files:
        issues = linter.validate_file(md)
        if issues:
            print(f"[X] {md} : FAILED -> {issues}")
            sys.exit(1)
        print(f"[V] {md} : CONFORME (Logic Gate Passed)")

    version = linter.kernel.get('version', '7.0.0')
    print(f"\n[SUCCÈS] Veritas Kernel v{version} validé.")

if __name__ == "__main__":
    run()
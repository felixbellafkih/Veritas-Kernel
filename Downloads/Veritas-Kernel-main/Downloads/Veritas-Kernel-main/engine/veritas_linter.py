import json
import os
import sys

class VeritasLinter:
    def __init__(self, manifest_path='VERITAS_KERNEL_MANIFEST.json'):
        try:
            with open(manifest_path, 'r', encoding='utf-8') as f:
                self.manifest = json.load(f)
        except Exception as e:
            print(f"[ERROR] Manifest critical failure: {e}")
            sys.exit(1)
            
        self.noise_terms = ["hadith", "consensus", "tradition", "jurisprudence", "sunnah", "ijma"]
        self.v6_constraints = ["Adjacency_Constraint_Mandatory", "Islah_Cycle_Verification"]

    def validate_manifest_integrity(self):
        """Vérifie que le manifeste respecte les standards v6."""
        constraints = self.manifest.get("integrity_constraints", [])
        missing = [c for c in self.v6_constraints if c not in constraints]
        return missing

    def check_noise(self, text):
        """Filtre anti-entropie sémantique."""
        return [term for term in self.noise_terms if term in text.lower()]

    def validate_file(self, file_path):
        errors = []
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        noise = self.check_noise(content)
        if noise:
            errors.append(f"LOGIC_EXCEPTION: Historical noise detected: {noise}")
        return errors

def run():
    linter = VeritasLinter()
    
    # 1. Audit du Manifeste
    missing = linter.validate_manifest_integrity()
    if missing:
        print(f"[X] MANIFEST ERROR: Missing v6 core logic: {missing}")
        sys.exit(1)

    # 2. Audit des Fichiers Markdown
    md_files = [f for f in os.listdir('.') if f.endswith('.md')]
    for md in md_files:
        issues = linter.validate_file(md)
        if issues:
            print(f"[X] {md} : FAILED -> {issues}")
            sys.exit(1)
        print(f"[V] {md} : CONFORME")

    print(f"\n[SUCCÈS] Kernel {linter.manifest.get('version')} validé (Pure Logic Mode).")

if __name__ == "__main__":
    run()

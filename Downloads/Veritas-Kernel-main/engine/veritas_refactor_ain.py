import json
import os
import re

def refactor_ain(file_path):
    if not os.path.exists(file_path):
        return
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Regex pour identifier les blocs de racines : ع-X-X (A-X-X/Name)
    # On traite les trois positions possibles du 'Ain
    
    # Position 1 : ع-X-X (A- -> '-
    content = re.sub(r'ع-([^-]*)-([^-]*) \(A-', r"ع-\1-\2 ('-", content)
    # Position 2 : X-ع-X (X-A- -> X-'-
    content = re.sub(r'([^-]*)-ع-([^-]*) \(([^-]*)-A-', r"\1-ع-\2 (\3-'-", content)
    # Position 3 : X-X-ع (X-X-A -> X-X-'
    content = re.sub(r'([^-]*)-([^-]*)-ع \(([^-]*)-([^-]*)-A', r"\1-\2-ع (\3-\4-'", content)
    
    # Correction des noms après le slash (ex: /Abad -> /'abad)
    content = re.sub(r'ع([^-]*)-([^-]*) \(([^\/]*)/A', r"ع\1-\2 (\3/'", content)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"✅ Refactoring terminé pour : {file_path}")

# Liste des fichiers à traiter
targets = [
    'LEXICON.json',
    'engine/veritas_core_generator.py',
    'engine/veritas_full_restore.py',
    'engine/veritas_mega_batch.py',
    'engine/veritas_cognitive_batch.py',
    'engine/veritas_smart_injector.py'
]

for t in targets:
    refactor_ain(t)

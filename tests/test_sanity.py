import unittest
import json
import os
import sys

# Ajout du dossier parent au path pour importer les modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from data.repository import LexiconRepository

class TestVeritasKernel(unittest.TestCase):
    
    def setUp(self):
        """Initialisation avant chaque test."""
        self.repo = LexiconRepository('LEXICON.json')
        self.roots = self.repo.get_all_roots()

    def test_json_structure(self):
        """Vérifie que le JSON est lisible et contient une liste."""
        self.assertGreater(len(self.roots), 0, "❌ ERREUR: Le Lexicon est vide !")
        print(f"\n✅ STRUCTURE: {len(self.roots)} racines chargées.")

    def test_no_duplicates(self):
        """Vérifie qu'il n'y a pas de racines en double."""
        seen = set()
        duplicates = []
        for item in self.roots:
            root = item['root']
            if root in seen:
                duplicates.append(root)
            seen.add(root)
        
        if duplicates:
            self.fail(f"❌ DOUBLONS DÉTECTÉS : {duplicates}")
        else:
            print("✅ INTÉGRITÉ: Aucun doublon détecté.")

    def test_mandatory_fields(self):
        """Vérifie que chaque entrée a ses champs obligatoires."""
        errors = []
        for item in self.roots:
            if not item.get('root'): errors.append(f"ID manquant dans {item}")
            if not item.get('arabic'): errors.append(f"Arabe manquant pour {item.get('root')}")
            if not item.get('logic_function'): errors.append(f"Fonction manquante pour {item.get('root')}")
        
        if errors:
            self.fail(f"❌ CHAMPS MANQUANTS : {errors}")
        else:
            print("✅ CONTENU: Toutes les racines sont complètes.")

if __name__ == '__main__':
    unittest.main()

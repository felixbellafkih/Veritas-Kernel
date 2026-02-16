import json
import os
import re

class LexiconRepository:
    def __init__(self, filepath='LEXICON.json'):
        self.filepath = filepath
        self.data = []
        self.latin_index = {}
        self.arabic_index = {}
        self._load_data()

    def _load_data(self):
        """Charge et indexe les données au démarrage."""
        if not os.path.exists(self.filepath):
            print(f"⚠️ WARNING: {self.filepath} not found.")
            return

        try:
            with open(self.filepath, 'r', encoding='utf-8') as f:
                content = json.load(f)
                self.data = content.get('universal_functions', [])
                
            # Création des index pour recherche rapide
            for item in self.data:
                root = item.get('root', '').strip().upper()
                arabic = item.get('arabic', '').strip()
                
                if root:
                    self.latin_index[root] = item
                if arabic and arabic != "---":
                    self.arabic_index[arabic] = item
                    
        except Exception as e:
            print(f"❌ ERROR loading Lexicon: {e}")

    def get_all_roots(self):
        """Retourne la liste complète."""
        return self.data

    def get_count(self):
        """Retourne le nombre total de racines."""
        return len(self.data)

    def find_root(self, query):
        """
        Cherche une racine (Latin ou Arabe).
        Gère automatiquement la conversion majuscule et l'auto-correction (S vs S.).
        """
        if not query:
            return None
            
        query = query.strip()
        
        # Détection Latin vs Arabe
        if re.search(r'[a-zA-Z]', query):
            q_upper = query.upper()
            # 1. Essai direct
            result = self.latin_index.get(q_upper)
            # 2. Essai avec correction phonétique (S->S., etc.)
            if not result:
                q_fix = q_upper.replace('S', 'S.').replace('D', 'D.').replace('T', 'T.').replace('H', 'H.').replace('Z', 'Z.')
                result = self.latin_index.get(q_fix)
            return result
        else:
            # Recherche Arabe exacte
            return self.arabic_index.get(query)


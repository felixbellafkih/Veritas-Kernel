import json
import os
import re
from core.logger import logger  # <--- CONNEXION AU LOGGER

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
            logger.error(f"DATABASE MISSING: {self.filepath} not found.")
            return

        try:
            with open(self.filepath, 'r', encoding='utf-8') as f:
                content = json.load(f)
                self.data = content.get('universal_functions', [])
                
            # Indexation
            for item in self.data:
                root = item.get('root', '').strip().upper()
                arabic = item.get('arabic', '').strip()
                
                if root:
                    self.latin_index[root] = item
                if arabic and arabic != "---":
                    self.arabic_index[arabic] = item
            
            logger.info(f"DATABASE LOADED: {len(self.data)} roots indexed from {self.filepath}")
                    
        except Exception as e:
            logger.error(f"DATABASE CORRUPTION: {e}")

    def get_all_roots(self):
        return self.data

    def get_count(self):
        return len(self.data)

    def find_root(self, query):
        if not query:
            return None 
        query = query.strip()
        
        # Logique de recherche (Latin vs Arabe)
        if re.search(r'[a-zA-Z]', query):
            q_upper = query.upper()
            result = self.latin_index.get(q_upper)
            if not result:
                q_fix = q_upper.replace('S', 'S.').replace('D', 'D.').replace('T', 'T.').replace('H', 'H.').replace('Z', 'Z.')
                result = self.latin_index.get(q_fix)
            return result
        else:
            return self.arabic_index.get(query)

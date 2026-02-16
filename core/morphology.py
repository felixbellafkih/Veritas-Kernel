import re

class MorphologyEngine:
    def __init__(self):
        # Définition des Patterns (Ordre d'importance)
        self.patterns = [
            # 1. FORM X: I-S-T (Request)
            {
                "id": "ISTAFALA",
                "prefix": "I-S-T-",
                "suffix": "",
                "logic_mod": "REQUEST_PROTOCOL // SEEKING",
                "desc_mod": "Tentative d'initialiser ou de demander l'accès à la fonction : "
            },
            # 2. FORM IV: A- (Causal/Transitive) - Ex: A-N-Z-L
            {
                "id": "AFALA",
                "prefix": "A-",
                "suffix": "",
                "logic_mod": "CAUSAL_OUTPUT // EXECUTE_ON",
                "desc_mod": "Action transitive. Faire subir la fonction à un objet externe : "
            },
            # 3. MAF'UL (Passive Object) - Ex: M-K-T-B (Simplifié M-)
            # Note: Conflit potentiel avec M-S-J-D, on gère au cas par cas ou générique
            {
                "id": "MAFUL",
                "prefix": "M-",
                "suffix": "", # On simplifie pour l'instant
                "logic_mod": "PASSIVE_OBJECT // RESULT_DATA",
                "desc_mod": "L'objet sur lequel la fonction a été exécutée. Résultat passif de : "
            },
             # 4. PLURIEL (Agents) - Ex: ...-W-N
            {
                "id": "PLURAL_AGENTS",
                "prefix": "",
                "suffix": "-W-N",
                "logic_mod": "ACTIVE_CLUSTER // AGENTS",
                "desc_mod": "Groupe d'instances exécutant la fonction : "
            }
        ]

    def process_token(self, token):
        """
        Analyse un token (ex: I-S-T-G-F-R), détecte le pattern,
        et retourne (Racine_Nettoyée, Modificateur_Logique, Description_Ajoutée).
        """
        token = token.upper().strip()
        
        for p in self.patterns:
            # Check Prefix
            has_prefix = token.startswith(p["prefix"]) if p["prefix"] else True
            # Check Suffix
            has_suffix = token.endswith(p["suffix"]) if p["suffix"] else True
            
            if has_prefix and has_suffix:
                # Extraction de la racine
                start = len(p["prefix"])
                end = len(token) - len(p["suffix"])
                potential_root = token[start:end]
                
                # Sécurité: Une racine doit avoir au moins 2-3 lettres
                if len(potential_root) >= 3: # ex: G-F-R
                    return {
                        "root": potential_root,
                        "detected": True,
                        "pattern": p["id"],
                        "logic_mod": p["logic_mod"],
                        "desc_mod": p["desc_mod"]
                    }
        
        # Si aucun pattern détecté, on renvoie le token brut
        return {
            "root": token,
            "detected": False,
            "pattern": "ROOT_FORM",
            "logic_mod": "",
            "desc_mod": ""
        }

# Instance globale
morpho = MorphologyEngine()
import google.generativeai as genai
import streamlit as st
# import json  <-- Supprimé car inutilisé (Optimisation Linter)

class VeritasAI:
    def __init__(self):
        self.active_model_name = "UNKNOWN"
        self.model = None
        
        try:
            # Récupération de la clé (Cloud ou Local)
            api_key = st.secrets["GOOGLE_API_KEY"]
            genai.configure(api_key=api_key)
            
            # --- LISTE STRICTE DES MODÈLES FLASH (QUOTA FRIENDLY) ---
            # On force l'ordre de priorité du plus récent au plus stable.
            # Pas de modèle "Pro" ici.
            priority_models = [
                'models/gemini-2.0-flash',      # 1. Le plus rapide et intelligent (Nouvelle Gen)
                'models/gemini-1.5-flash',      # 2. Le standard stable (Backup solide)
                'models/gemini-1.5-flash-8b'    # 3. Le plus léger (Ultra économie)
            ]
            
            target_model = None
            
            # Boucle d'essai : On teste les modèles un par un jusqu'à ce que ça marche
            for model_name in priority_models:
                try:
                    # Test de connexion au modèle
                    test_instance = genai.GenerativeModel(model_name)
                    # Si pas d'erreur, on valide
                    self.model = test_instance
                    self.active_model_name = model_name
                    target_model = model_name
                    break # On sort de la boucle, on a trouvé !
                except Exception:
                    continue # Si ça échoue, on tente le suivant
            
            if not target_model:
                st.error("❌ ERREUR MODÈLE : Impossible d'accéder aux modèles Flash (Quota dépassé ?).")

        except Exception as e:
            st.error(f"FATAL ERROR: Configuration échouée. {e}")
            self.model = None

    def generate_systemic_translation(self, verse_text, full_lexicon_context):
        if not self.model:
            return "❌ ERREUR CRITIQUE : AI Core offline."

        # --- PROTOCOLE COMPLET : DÉCOMPILATION + PÉDAGOGIE + CONFRONTATION (v22.3.2) ---
        system_prompt = f"""
        **TON ROLE :**
        Tu es l'ARCHITECTE SYSTÈME du projet Veritas.
        Ton objectif est de montrer la mécanique logique du Coran (Racines), puis de l'expliquer clairement.

        **TES DONNÉES (BASE DE VÉRITÉ) :**
        {full_lexicon_context}

        **PHASE 0 : AUTHENTIFICATION (SÉCURITÉ)**
        Vérifie que le texte est bien un verset du Coran authentique (lettre pour lettre).
        Si ce n'est pas le cas, réponds juste : "⚠️ **TEXTE NON RECONNU** : Ce n'est pas un verset du Code Source."

        **PHASE 1 : DÉCOMPILATION SYSTÉMIQUE (LE MOTEUR)**
        Avant d'expliquer, affiche le processus brut de décodage pour montrer la mécanique interne.
        - Pour chaque mot clé, affiche une ligne concise : 
          `> [Mot Arabe] (Racine) : [Fonction Logique Brute]`
        - Style : Terminal, Logique, "Raw Data".

        **PHASE 2 : ANALYSE RATIONNELLE (L'EXPLICATION)**
        Maintenant, traduis cette logique brute en une explication fluide et pédagogique (Français naturel).
        - **STYLE :** Pas de jargon informatique ici ("Pas de Query/Kernel"). Parle comme un professeur de logique ou un scientifique.
        - **VOCABULAIRE :** Utilise les sens du Lexique (Ex: "Salat" = "Connexion", pas "Prière").

        **PHASE 3 : CONFRONTATION (LE CHOQUEUR)**
        Compare ton analyse logique avec la Tradition (Hadiths, Sira, Exégèses).
        - Montre calmement où la tradition a déformé le sens original.
        - **POINT CRITIQUE :** Si le verset parle d'obéir au Messager, précise impérativement que cela signifie **appliquer les instructions transmises STRICTEMENT dans le Message Coranique**. Toute instruction supposée hors du Coran est hors-système.

        **PHASE 4 : FORMAT DE SORTIE**
        1. **PROCESSUS DE DÉCOMPILATION** : La liste brute (Phase 1).
        2. **ANALYSE RATIONNELLE** : L'explication fluide (Phase 2).
        3. **⚠️ POINT DE DIVERGENCE** : La critique du consensus (Phase 3).
        4. **TABLEAU LEXICAL** : Tableau Markdown simple :
           | Mot Arabe | Racine | Sens Logique (Lexique) | Explication Simple |
        """

        try:
            response = self.model.generate_content(
                f"{system_prompt}\n\n**VERSET À ANALYSER :** {verse_text}",
                generation_config=genai.types.GenerationConfig(
                    temperature=0.1, # Légère fluidité pour le style humain
                )
            )
            # On affiche le modèle utilisé pour être sûr
            return f"**[ANALYST: {self.active_model_name}]**\n\n" + response.text

        except Exception as e:
            return f"⚠️ ERREUR RUNTIME : {str(e)}"
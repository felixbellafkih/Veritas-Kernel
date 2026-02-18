import google.generativeai as genai
import streamlit as st
import json
import os

class VeritasAI:
    def __init__(self):
        self.active_model_name = "UNKNOWN"
        self.model = None
        
        try:
            api_key = st.secrets["GOOGLE_API_KEY"]
            genai.configure(api_key=api_key)
            
            # --- SCAN RAPIDE DES MODÈLES ---
            available_models = []
            try:
                for m in genai.list_models():
                    if 'generateContent' in m.supported_generation_methods:
                        available_models.append(m.name)
            except Exception:
                pass

            # --- SÉLECTION (Priorité Flash pour la vitesse) ---
            if 'models/gemini-1.5-flash' in available_models:
                self.target_model = 'gemini-1.5-flash'
            elif 'models/gemini-1.5-pro' in available_models:
                self.target_model = 'gemini-1.5-pro'
            elif 'models/gemini-pro' in available_models:
                self.target_model = 'gemini-pro'
            else:
                self.target_model = available_models[0] if available_models else None

            if self.target_model:
                self.model = genai.GenerativeModel(self.target_model)
                self.active_model_name = self.target_model
            else:
                st.error("AUCUN MODÈLE GEMINI DISPONIBLE.")

        except Exception as e:
            st.error(f"Config Error: {e}")
            self.model = None

    def generate_systemic_translation(self, verse_text, full_lexicon_context):
        if not self.model:
            return "❌ ERREUR : Le cerveau IA est déconnecté."

        # --- PROTOCOLE VULGARISATEUR (OPTIMISÉ) ---
        system_prompt = f"""
        **TON ROLE :**
        Tu es l'ARCHITECTE SYSTÈME du projet Veritas. Tu es un vulgarisateur scientifique de haut niveau.
        
        **TES DONNÉES (BASE DE VÉRITÉ) :**
        {full_lexicon_context}

        **TES RÈGLES (CRITIQUE) :**
        1. **ANALYSE :** Traduis le code coranique en une explication claire, rationnelle et scientifique (style ingénieur système / astrophysicien).
        2. **VOCABULAIRE :** Utilise les définitions techniques du Lexique (ex: K-T-B = Prescription Matrice). Pas de jargon religieux (Pas de "Dieu", "Pieux", "Prière").
        3. **FLUIDITÉ :** Fais un texte continu et élégant, pas une liste de robots.
        4. **SCOPE RESTREINT :** Ne traite QUE le verset demandé.
        
        **INSTRUCTION DE SORTIE :**
        1. Rédige d'abord ton paragraphe d'analyse scientifique.
        2. Ensuite, génère un tableau Markdown UNIQUEMENT pour les mots présents dans le verset soumis.
           Colonnes du tableau : [Mot du Verset] | [Racine] | [Fonction Logique] | [Description Technique Courte].
        """

        try:
            response = self.model.generate_content(
                f"{system_prompt}\n\n**VERSET À ANALYSER :** {verse_text}",
                generation_config=genai.types.GenerationConfig(temperature=0.3)
            )
            return f"**[ARCHITECT: {self.active_model_name}]**\n\n" + response.text

        except Exception as e:
            return f"⚠️ ERREUR D'ANALYSE ({self.active_model_name}) : {str(e)}"
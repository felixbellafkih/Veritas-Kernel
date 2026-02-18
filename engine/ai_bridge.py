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
            
            # --- SÉLECTION DU MODÈLE (ROBUSTE) ---
            target_model = None
            
            # 1. Priorité : Gemini Flash Latest (Stable & Gratuit)
            try:
                test_model = genai.GenerativeModel('models/gemini-flash-latest')
                self.model = test_model
                self.active_model_name = 'models/gemini-flash-latest'
                target_model = self.active_model_name
            except:
                pass
            
            # 2. Secours : Gemini 2.0 Flash Lite (Rapide)
            if not target_model:
                try:
                    test_model = genai.GenerativeModel('models/gemini-2.0-flash-lite-001')
                    self.model = test_model
                    self.active_model_name = 'models/gemini-2.0-flash-lite-001'
                    target_model = self.active_model_name
                except:
                    pass

            # 3. Dernier recours : Gemini 2.0 Flash Standard
            if not target_model:
                try:
                    test_model = genai.GenerativeModel('models/gemini-2.0-flash')
                    self.model = test_model
                    self.active_model_name = 'models/gemini-2.0-flash'
                    target_model = self.active_model_name
                except:
                    pass

            if not target_model:
                st.error("AUCUN MODÈLE ACCESSIBLE (Échec sur Flash Latest, Lite et 2.0).")

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
            return f"**[ANALYST: {self.active_model_name}]**\n\n" + response.text

        except Exception as e:
            return f"⚠️ ERREUR RUNTIME : {str(e)}"
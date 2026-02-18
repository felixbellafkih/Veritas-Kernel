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

        # --- PROTOCOLE PÉDAGOGIQUE RATIONNEL (v22.3.0) ---
        system_prompt = f"""
        **TON ROLE :**
        Tu es un ANALYSTE RATIONNEL et un PÉDAGOGUE hors pair.
        Ton objectif est de traduire la logique du Coran en un langage clair, moderne et accessible à tout être humain doué de raison.

        **TES DONNÉES (BASE DE VÉRITÉ) :**
        {full_lexicon_context}

        **PHASE 0 : AUTHENTIFICATION (SÉCURITÉ)**
        Vérifie que le texte est bien un verset du Coran authentique (lettre pour lettre).
        Si ce n'est pas le cas, réponds juste : "⚠️ **TEXTE NON RECONNU** : Ce n'est pas un verset du Code Source."

        **PHASE 1 : ANALYSE (STYLE "HUMAIN RATIONNEL")**
        Explique le sens du verset en te basant UNIQUEMENT sur les définitions du Lexique, mais en rédigeant en français naturel.
        
        **INTERDICTIONS FORMELLES (STYLE) :**
        1. **PAS DE JARGON INFORMATIQUE :** Interdit d'utiliser des mots comme "QUERY", "ROOT_ACCESS", "KERNEL", "INPUT/OUTPUT", ni de mots en MAJUSCULES_AVEC_UNDERSCORE.
        2. **PAS DE ROBOTIQUE :** Ne parle pas comme une machine. Parle comme un scientifique qui explique une loi physique ou sociale.
        3. **PAS DE RACINES CRYPTIQUES :** N'écris pas "T.-'-T.", écris simplement la racine arabe entre parenthèses si nécessaire (ex: "Ta'a") ou le mot arabe.

        **INSTRUCTIONS DE TRADUCTION :**
        - Remplace le jargon religieux par des concepts universels (Ex: "Salat" = "Mise à jour / Connexion", "Taqwa" = "Prémunition / Sécurité active").
        - Remplace le jargon informatique par des concepts logiques (Ex: "Hard-Coding" = "Loi immuable", "Firewall" = "Protection", "Bug" = "Incohérence").

        **PHASE 2 : CONFRONTATION (LE CHOQUEUR)**
        Compare ton analyse logique avec la Tradition (Hadiths, Sira, Exégèses).
        - Montre calmement mais fermement où la tradition a transformé une instruction pratique en un rituel mystique ou un culte de la personnalité.
        - Exemple : Si le verset parle d'obéir au Messager, précise que c'est obéir au Message (le contenu) et non à l'homme historique (le contenant).

        **PHASE 3 : FORMAT DE SORTIE**
        1. **ANALYSE RATIONNELLE** : Ton explication claire et fluide.
        2. **⚠️ POINT DE DIVERGENCE** : La critique du consensus traditionnel.
        3. **TABLEAU LEXICAL** : Tableau Markdown simple :
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
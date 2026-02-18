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
            
            # --- SÉLECTION CHIRURGICALE BASÉE SUR TA LISTE ---
            # On évite les versions "Preview" ou "Pro" qui ont des quotas minuscules (429).
            # On vise les alias "latest" ou les versions "Lite".
            
            target_model = None
            
            # Priorité 1 : L'alias stable universel (souvent le meilleur quota)
            # Correspond à la ligne 15 de ta liste
            try:
                test_model = genai.GenerativeModel('models/gemini-flash-latest')
                self.model = test_model
                self.active_model_name = 'models/gemini-flash-latest'
                target_model = self.active_model_name
            except:
                pass
            
            # Priorité 2 : La version "Lite" (Conçue pour la rapidité/volume)
            # Correspond à la ligne 4 de ta liste
            if not target_model:
                try:
                    test_model = genai.GenerativeModel('models/gemini-2.0-flash-lite-001')
                    self.model = test_model
                    self.active_model_name = 'models/gemini-2.0-flash-lite-001'
                    target_model = self.active_model_name
                except:
                    pass

            # Priorité 3 : La version 2.0 Flash standard (Si les autres échouent)
            # Correspond à la ligne 2 de ta liste
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

        # --- PROTOCOLE D'AUDIT SYSTÉMIQUE COMPLET (v22.2.7) ---
        system_prompt = f"""
        **TON ROLE :**
        Tu es l'ARCHITECTE SYSTÈME du projet Veritas. Tu es un vulgarisateur scientifique et un auditeur de cohérence critique.
        
        **TES DONNÉES (BASE DE VÉRITÉ) :**
        {full_lexicon_context}

        **PHASE 0 : AUTHENTIFICATION DU SIGNAL (SÉCURITÉ STRICTE)**
        Tu agis comme un Checksum. Vérifie si le texte fourni correspond EXACTEMENT à un verset du Coran.
        1. **STRICT MATCH :** Si une seule lettre diffère, ou si c'est du texte libre, rejette immédiatement.
        2. **ALERTE :** Si rejet, réponds UNIQUEMENT : "⚠️ **SIGNAL CORROMPU DÉTECTÉ** : Le signal ne correspond pas au Code Source (Coran). Analyse annulée."

        **PHASE 1 : ANALYSE SYSTÉMIQUE (LE CODE SOURCE)**
        Si authentifié, explique le verset en utilisant EXCLUSIVEMENT le Lexique fourni.
        * **Ton :** Scientifique, Ingénieur Système, Rationaliste.
        * **Méthode :** Décode la fonction logique des mots. (Ex: "Salat" = "Connexion/Mise à jour", pas "Prière").

        **PHASE 2 : DIAGNOSTIC DE DIVERGENCE (CONFRONTATION)**
        Compare ton analyse logique avec le "Consensus Humain Dominant" (Tradition, Hadiths, Sira).
        1. Identifie le **GAP** (l'écart) : Montre où la tradition a dévié du sens systémique pur.
        2. **Exemple critique :** Si le verset parle d'obéissance (Ta'a) ou de suivi (Ittiba'), précise que cela concerne l'instruction (Rissala/Code) et NON la personne physique ou sa biographie historique (Sira).
        3. Dénonce le mimétisme : Explique comment le sens a été "tordu" pour devenir un rituel ou un culte de la personnalité, perdant sa fonction utilitaire originale.

        **PHASE 3 : FORMAT DE SORTIE**
        1. **ANALYSE SYSTÉMIQUE** : Ton paragraphe d'explication scientifique.
        2. **⚠️ ÉCART DE CONSENSUS** : Le paragraphe critique sur la divergence traditionnelle.
        3. **TABLEAU D'ANALYSE** : Génère un tableau Markdown UNIQUEMENT pour les mots du verset :
           | Mot Arabe | Racine | Fonction Logique | Description Technique |
        """

        try:
            response = self.model.generate_content(
                f"{system_prompt}\n\n**VERSET À ANALYSER :** {verse_text}",
                generation_config=genai.types.GenerationConfig(
                    temperature=0.0, # Zéro créativité = Rigueur absolue
                )
            )
            return f"**[ENGINE: {self.active_model_name}]**\n\n" + response.text

        except Exception as e:
            return f"⚠️ RUNTIME EXCEPTION : {str(e)}"
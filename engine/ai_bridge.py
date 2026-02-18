import google.generativeai as genai
import streamlit as st
import json
import os

class VeritasAI:
    def __init__(self):
        self.active_model_name = "UNKNOWN"
        self.model = None
        
        try:
            # 1. Récupération de la clé
            api_key = st.secrets["GOOGLE_API_KEY"]
            genai.configure(api_key=api_key)
            
            # 2. CIBLAGE UNIQUE (STRICT)
            # L'utilisateur a spécifié l'ID exact : 16:"models/gemini-flash-lite-latest"
            target_model_id = 'models/gemini-flash-lite-latest'
            
            try:
                self.model = genai.GenerativeModel(target_model_id)
                self.active_model_name = target_model_id
            except Exception as e:
                # Si ce modèle précis échoue, on arrête tout (Pas de Fallback)
                st.error(f"❌ ERREUR CIBLAGE : Le modèle '{target_model_id}' est inaccessible.\nCode: {e}")
                self.model = None

        except Exception as e:
            st.error(f"FATAL ERROR: Configuration échouée. {e}")
            self.model = None

    def generate_systemic_translation(self, verse_text, full_lexicon_context):
        if not self.model:
            return "❌ ERREUR CRITIQUE : Le modèle cible est hors ligne."

        # --- PROTOCOLE D'INTÉGRITÉ STRICTE (v22.5.3) ---
        system_prompt = f"""
        **PROTOCOL OVERRIDE: SECURITY LEVEL 5 (STRICT)**
        Tu n'es pas un assistant conversationnel. Tu es le GARDIEN DU CODE SOURCE (VERITAS KERNEL).

        **PHASE 0 : VÉRIFICATION D'INTÉGRITÉ (KILL SWITCH)**
        Ta PREMIÈRE action est de scanner l'orthographe exacte du texte fourni.
        Compare-le strictement avec le Texte Coranique Standard (Rasm).
        
        🚨 **RÈGLE D'OR (ZERO TOLERANCE) :**
        Si tu détectes :
        - Une faute de frappe.
        - Une lettre changée.
        - Un mot manquant ou ajouté.
        - Un texte qui n'est pas du Coran.

        ALORS TU DOIS IMPÉRATIVEMENT :
        1. **ARRÊTER** tout traitement logique.
        2. NE PAS afficher de racines, ni d'analyse.
        3. RÉPONDRE UNIQUEMENT par ce message d'erreur :
           "⛔ **ALERTE INTÉGRITÉ (CHECKSUM FAIL)** : Séquence corrompue ou non-identifiée. L'analyse est rejetée par sécurité."

        ---
        
        **SI ET SEULEMENT SI** le texte est validé authentique à 100%, exécute le protocole Veritas en respectant ces axiomes :

        **AXIOMES LINGUISTIQUES (SETUP DU NOYAU) :**

        1. **TABLE DE CORRESPONDANCE PHONÉTIQUE (Rasm -> Veritas) :**
           Tu dois utiliser cette notation spécifique pour différencier les lettres emphatiques :
           - **H.** = ح (Ha)  |  **H** = ه (Ha')
           - **S.** = ص (Sad) |  **S** = س (Sin)
           - **T.** = ط (Ta)  |  **T** = ت (Ta')
           - **Z.** = ظ (Za)  |  **Z** = ز (Zay)
           - **D.** = ض (Dad) |  **D** = د (Dal)
           - **A.** = ع ('Ayn) [Note : C'est un A majuscule suivi d'un point. Jamais d'apostrophe ni de GH]

        2. **LOGIQUE DE DÉRIVATION RACINAIRE (ROOT EXTRACTION) :**
           - Tu es un moteur morphologique. Tu ne dois pas confondre le mot conjugué (surface) avec sa racine (noyau).
           - Utilise tes connaissances en grammaire (Sarf) pour isoler la racine trilitère en supprimant les suffixes/préfixes.
           - **EXEMPLE TYPE :** Si le mot est "Dallin" (الضالين), la racine est **D.-L-L** (et non pas D-L-L-N).
           - **EXEMPLE TYPE :** Si le mot est "Mu'minun", la racine est **A.-M-N**.

        ---

        **TES DONNÉES (BASE DE VÉRITÉ) :**
        {full_lexicon_context}

        **PHASE 1 : DÉCOMPILATION SYSTÉMIQUE (LE MOTEUR)**
        Avant d'expliquer, affiche le processus brut de décodage pour montrer la mécanique interne.
        - Pour chaque mot clé, affiche une ligne concise : 
          `> [Mot Arabe] (Racine Standardisée) : [Fonction Logique Brute]`
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
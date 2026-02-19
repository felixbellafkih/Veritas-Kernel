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
            target_model_id = 'models/gemini-2.0-flash'
            
            try:
                self.model = genai.GenerativeModel(target_model_id)
                self.active_model_name = target_model_id
            except Exception as e:
                st.error(f"❌ ERREUR CIBLAGE : Le modèle '{target_model_id}' est inaccessible.\nCode: {e}")
                self.model = None

        except Exception as e:
            st.error(f"FATAL ERROR: Configuration échouée. {e}")
            self.model = None

    def generate_systemic_translation(self, verse_text, optimized_lexicon_payload):
        if not self.model:
            return "❌ ERREUR CRITIQUE : Le modèle cible est hors ligne."

        # --- PROTOCOLE V22.6.5 : LOGIQUE ÉLÉGANTE ---
        system_prompt = f"""
        **PROTOCOL OVERRIDE: SECURITY LEVEL 5 (STRICT)**
        Tu n'es pas un assistant conversationnel. Tu es le GARDIEN DU CODE SOURCE (VERITAS KERNEL).

        **PHASE 0 : VÉRIFICATION D'INTÉGRITÉ (KILL SWITCH)**
        🚨 PARAMÈTRES DE CONTRÔLE (TOLÉRANCE TYPOGRAPHIQUE) :
        1. IGNORE TOTALEMENT : Les différences de standard d'écriture (Othmani vs Imla'i), les variations d'Alif (long vs Maqsura), les diacritiques (Tashkeel) et les signes de pause.
        2. DÉCLENCHE LE KILL SWITCH (RÉPONDRE UNIQUEMENT : "⛔ **ALERTE INTÉGRITÉ (CHECKSUM FAIL)**") SI ET SEULEMENT SI : Le texte n'appartient pas au Coran ou un mot a été ajouté/supprimé.

        ---
        
        **SI ET SEULEMENT SI LE TEXTE EST VALIDE, EXÉCUTE CE PROTOCOLE :**

        **AXIOMES LINGUISTIQUES (TABLE DE VÉRITÉ) :**
        1. 🚫 LISTE NOIRE DES SYMBOLES INTERDITS :
        - BANNIR TOTALEMENT : La séquence "DH" (pour ذ, ض, ou ظ). (Interdiction absolue de l'écrire).
        - BANNIR TOTALEMENT : Toute apostrophe (', `), guillemet, ou chiffre (3, 7, 9, 6).

        2. ⚙️ MATRICE DE TRANSLITTÉRATION STRICTE (VERITAS KERNEL) :
        🚨 RÈGLE ABSOLUE : Les points "." sont des CARACTÈRES DE DONNÉES OBLIGATOIRES.
        [Catégorie A : POINT OBLIGATOIRE] : ع=A. | ح=H. | ص=S. | ط=T. | ظ=Z. | ض=D.
        [Catégorie B : SANS POINT] : أ=A | ه=H | س=S | ت=T | ز=Z | د=D
        [Catégorie C : CONVENTIONNELLE] : ش=SH | خ=KH

        **PROTOCOLE D'ISOLATION COGNITIVE (INCONTOURNABLE) :**
        1. **NEUTRALISATION DES PARTICULES :** Les pronoms (Alladhi, Huwa, etc.) et prépositions (Min, Ila, Bi) n'ont PAS DE RACINE. Ne leur attribue AUCUNE lettre.
        2. **ATTENTIION DOUBLE POUR RACINES RACINE CONJUGUEES :** Vigilance extrême envers les racines conjuguées ou attachées à des particules de liaisons (ex: أَسۡرَىٰ  = S-R-Y, pas A-S-R  /   لِتَعۡلَمُواْ = A.-L-M, pas L-T-A.-L-M).
        3. **PAS DE RITUALISME :** Salat = Connexion. Zakat = Purification/Optimisation.
        4. **AXE DE RÉALITÉ :** Traite les informations de manière logique et rationnelle.

        ---

        **TES DONNÉES (BASE DE VÉRITÉ FILTRÉE PAR LE KERNEL CENTRAL) :**
        {optimized_lexicon_payload}

	**PHASE 1 : DÉCOMPILATION SYSTÉMIQUE (LE MOTEUR - FETCH STRICT)**
        Ceci est une opération de requête base de données (Lookup JSON). Tu es un parseur.
        1. Outils de liaison : Affiche STRICTEMENT `> [Mot] : [OUTIL DE LIAISON]`
        2. Mots-racines : Cherche la racine correspondante dans le JSON fourni.
        3. 🚨 RÈGLE DE COPIE ABSOLUE : Si la racine est dans le JSON, EXTRAIS et RECOPIE EXACTEMENT la valeur textuelle associée. Aucune paraphrase n'est tolérée.
           Format : `> [Mot Arabe] (Racine) : [Valeur exacte recopiée]`
        4. 🚨 RÈGLE DE CACHE MISS : Si, et seulement si, la racine est INTROUVABLE dans le JSON, tu DOIS obligatoirement écrire le tag [HORS-LEXIQUE] suivi de ta déduction.
           Format : `> [Mot Arabe] (Racine) : [HORS-LEXIQUE] -> [Ta déduction]`
        **PHASE 2 : ANALYSE RATIONNELLE (STYLE : MAGISTRAL & HUMAIN)**
        En te basant sur les résultats de la Phase 1, fais une analyse architecturale fluide. Ton magistral, froid, analytique.
        Utilise impérativement les sens du Lexique (exemple : Salat = Connexion et NON prière). Explique la LOGIQUE SOUS-JACENTE de l'opération.

        **PHASE 3 : CONFRONTATION (LE CHOQUEUR)**
        Compare avec le consensus traditionnel de manière ferme et sans torsion. Seule la cohérence déduite de ton analyse rationnelle prime.
        🚨 RÈGLE CONDITIONNELLE : Dans le cas où (R-S-L), (T-W-A) ou (T-B-A.) sont présents, précise que cela signifie "appliquer les instructions transmises STRICTEMENT dans le Message Coranique". Sinon, n'évoque pas ce détail.

        **DIRECTIVES DE FORMATAGE GLOBAL**
        Structure ta réponse EXACTEMENT selon cette hiérarchie :
        
        ### ⚙️ DÉCOMPILATION SYSTÉMIQUE
        [Phase 1]
        
        ### 🧠 ANALYSE RATIONNELLE
        [Phase 2]
        
        ### ⚠️ RUPTURE DE CONSENSUS
        [Phase 3]
        
        ### 📊 MATRICE LEXICALE
        | Mot Arabe | Racine | Sens Logique (Veritas) | Explication Simple |
        | :--- | :--- | :--- | :--- |
        """
        
        try:
            response = self.model.generate_content(
                f"{system_prompt}\n\n**VERSET À ANALYSER :** {verse_text}",
                generation_config=genai.types.GenerationConfig(
                    temperature=0.2,
                )
            )
            return f"**[TARGET: {self.active_model_name}]**\n\n" + response.text

        except Exception as e:
            if "429" in str(e):
                return "⏳ **QUOTA ÉPUISÉ (429) :** Limite de l'API atteinte. Attends 60 secondes avant de relancer l'analyse."
            return f"⚠️ ERREUR RUNTIME : {str(e)}"
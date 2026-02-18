

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
            target_model_id = 'models/gemini-flash-lite-latest'
            
            try:
                self.model = genai.GenerativeModel(target_model_id)
                self.active_model_name = target_model_id
            except Exception as e:
                st.error(f"❌ ERREUR CIBLAGE : Le modèle '{target_model_id}' est inaccessible.\nCode: {e}")
                self.model = None

        except Exception as e:
            st.error(f"FATAL ERROR: Configuration échouée. {e}")
            self.model = None

    def generate_systemic_translation(self, verse_text, full_lexicon_context):
        if not self.model:
            return "❌ ERREUR CRITIQUE : Le modèle cible est hors ligne."

        # --- PROTOCOLE V22.6.5 : LOGIQUE ÉLÉGANTE ---
        system_prompt = f"""
        **PROTOCOL OVERRIDE: SECURITY LEVEL 5 (STRICT)**
        Tu n'es pas un assistant conversationnel. Tu es le GARDIEN DU CODE SOURCE (VERITAS KERNEL).

        **PHASE 0 : VÉRIFICATION D'INTÉGRITÉ (KILL SWITCH)**
        Ta PREMIÈRE action est de scanner l'orthographe exacte du texte fourni.
        Compare-le strictement avec le Texte Coranique Standard (Rasm).
        
        🚨 **RÈGLE ZERO TOLERANCE :**
        Si tu détectes une faute de frappe, une lettre changée ou un mot manquant :
        RÉPONDRE UNIQUEMENT : "⛔ **ALERTE INTÉGRITÉ (CHECKSUM FAIL)**" et arrête tout.

        ---
        
        **SI ET SEULEMENT SI LE TEXTE EST VALIDE, EXÉCUTE CE PROTOCOLE :**

        **AXIOMES LINGUISTIQUES (TABLE DE VÉRITÉ) :**
        Non-négociable : Tu dois respecter scrupuleusement ces correspondances :
	| LETTRE ARABE | CODE VERITAS (OBLIGATOIRE) | 
        | :--- | :--- | :--- |
        | **د** (Dal) | **D** | - |
        | **ض** (Dad) | **D.** (D majuscule + point) | 
        | **ز** (Zay) | **Z** | - |
        | **ظ** (Za) | **Z.** (Z majuscule + point) |
        | **س** (Sin) | **S** | - |
        | **ص** (Sad) | **S.** (S majuscule + point) |
        | **ه** (Ha') | **H** | h, H. |
        | **ح** (Ha) | **H.** (H majuscule + point) |
        | **ت** (Ta') | **T** | - |
        | **ط** (Ta) | **T.** (T majuscule + point) |
        | **أ** (Alif) | **A** | - |
        | **ع** ('Ayn) | **A.** (A majuscule + point) |

        **RÈGLE DE DÉRIVATION :**
        Isole la racine trilitère stricte (Noyau). Ignore les suffixes/préfixes de conjugaison.
        Ex: "Ad-Dallin" (الضالين) -> Racine : **D.-L-L** (Pas D-L-L-N).

        **PROTOCOLE D'ISOLATION COGNITIVE (ANTI-TRADITION) :**
        1. **PAS DE RITUALISME :** Le Coran est un Système Logique. 
           - Si le Lexique dit "Connexion", c'est abstrait. Ce n'est JAMAIS une prière physique.
           - Si le Lexique dit "Purification", c'est une optimisation. Ce n'est JAMAIS une aumône.
        2. **VOCABULAIRE INTERDIT (En Phase 1 et 2) :**
           - Prière, Mosquée, Rituel, Aumône, Pèlerinage, Prosternation physique, Ablution.
	3. **DISCRIMINATION DES RACINES COMPLEXES (HOMONYMES) :**
  	   - Tu dois être extrêmement vigilant sur les verbes de Forme IV (Af'ala).
   	   - EXEMPLE CRITIQUE : Le mot "Asrā" (أَسْرَىٰ). 
   	 	  - Ce n'est PAS la racine A-S-R (أَسَرَ - Lier/Capturer).
     	   - C'est la racine S-R-Y (سَرَى - Déplacement/Flux nocturne) à la forme causative.
           - Toute confusion entre A-S-R et S-R-Y est une ERREUR DE PROTOCOLE.
           - Utilise toujours la morphologie profonde pour remonter à la racine trilitère correcte avant de consulter le Lexicon.
	4. **INTEGRITE MAXIMALE :** S'il manque des racines à la base de donnée Lexicon, utilise tes connaissances propre qui découlent du meme esprit Veritas : sans torsion, et chaque mot doit etre compris strictement à partir des sens de ses lettres respective "Maqasid Al huruf".

        ---

        **TES DONNÉES (BASE DE VÉRITÉ) :**
        {full_lexicon_context}

        **PHASE 1 : DÉCOMPILATION SYSTÉMIQUE (LE MOTEUR)**
        Avant d'expliquer, affiche le processus brut de décodage pour montrer la mécanique interne.
        - Pour chaque mot clé, affiche une ligne concise : 
          `> [Mot Arabe] (Racine) : [Fonction Logique Brute]`
        - Style : Terminal, Logique, "Raw Data".

        **PHASE 2 : ANALYSE RATIONNELLE (STYLE : MAGISTRAL & HUMAIN)**
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
                    temperature=0.2, # Légère hausse (0.2) pour permettre l'élégance du style
                )
            )
            return f"**[TARGET: {self.active_model_name}]**\n\n" + response.text

        except Exception as e:
            return f"⚠️ ERREUR RUNTIME : {str(e)}"
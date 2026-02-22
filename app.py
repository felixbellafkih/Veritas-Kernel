import re
import json
import streamlit as st
import graphviz
import pandas as pd
from data.repository import LexiconRepository
from core.config import config
from export.manager import ExportManager
from engine.ai_bridge import VeritasAI  # Import du Pont IA


# ==============================================================================
# 1. MOTEUR MORPHOLOGIQUE (STEMMER & RÉSOLUTION DES CONSTANTES)
# ==============================================================================
class MorphologyEngine:
    def __init__(self):
        # Matrice de translittération stricte
        self.veritas_trans_matrix = {
            'ا':'A', 'أ':'A', 'إ':'A', 'آ':'A', 'ء':'A', 'ٱ':'A', 'ى':'Y',
            'ب':'B', 'ت':'T', 'ث':'TH', 'ج':'J',
            'ح':'H.', 'خ':'KH', 'د':'D', 'ذ':'DH',
            'ر':'R', 'ز':'Z', 'س':'S', 'ش':'SH',
            'ص':'S.', 'ض':'D.', 'ط':'T.', 'ظ':'Z.',
            'ع':'A.', 'غ':'GH', 'ف':'F', 'ق':'Q',
            'ك':'K', 'ل':'L', 'م':'M', 'ن':'N',
            'ه':'H', 'و':'W', 'ي':'Y', 'ة':'T'
        }
        
        # TABLE DES CONSTANTES SYSTÉMIQUES (Anomalies morphologiques pures)
        self.systemic_constants = {
            'سم': 'S-M-W',     # Ism (Nom/Pointeur) - Racine amputée du Waw
            'اسم': 'S-M-W',
            'له': 'A-L-H',     # Allah - Après suppression de l'article Al-
            'لله': 'A-L-H',    # Lillah (A-L-H)
            'الله': 'A-L-H',   # Allah brut
            'اله': 'A-L-H'
        }
        
        # Patterns de repli (Compatibilité Latin)
        self.patterns = [
            {"prefix": "I-S-T-A.", "suffix": "", "logic_mod": "REQUEST_PROTOCOL", "color": "#FF00FF"},
            {"prefix": "A-A.", "suffix": "", "logic_mod": "CAUSAL_OUTPUT", "color": "#FFA500"},
            {"prefix": "M-A.", "suffix": "", "logic_mod": "PASSIVE_OBJECT", "color": "#FFFF00"}
        ]

    def clean_arabic(self, text: str) -> str:
        """Dépouille le texte source de son bruit (Tashkeel, Articles)."""
        text = re.sub(r'[\u0617-\u061A\u064B-\u0652\u0670]', '', text)
        if text.startswith('ال') or text.startswith('ٱل'):
            text = text[2:]
        return text

    def to_veritas_latin(self, arabic_text: str) -> str:
        """Convertit l'arabe en tableau de caractères Veritas."""
        latin_chars = [self.veritas_trans_matrix[char] for char in arabic_text if char in self.veritas_trans_matrix]
        return "-".join(latin_chars)

    def stem_latin_root(self, latin_str: str) -> str:
        """
        Algorithme de réduction trilitère (Ghayr dhi 'iwaj).
        Ampute les modificateurs morphologiques pour isoler le noyau absolu.
        """
        parts = latin_str.split('-')
        
        # Si la racine est déjà trilitère, elle est pure.
        if len(parts) == 3:
            return latin_str
            
        # RÉDUCTION DES GABARITS À 4 LETTRES (Ex: Fa'eel, Fa'laan, Maf'al)
        if len(parts) == 4:
            # Ex: R-H.-Y-M -> Enlève le Y (Infixe de constance)
            if parts[2] == 'Y' or parts[2] == 'W':
                return f"{parts[0]}-{parts[1]}-{parts[3]}"
            # Ex: R-H.-M-N -> Enlève le N (Suffixe d'amplitude)
            elif parts[3] == 'N':
                return f"{parts[0]}-{parts[1]}-{parts[2]}"
            # Ex: M-K-T-B -> Enlève le M (Préfixe d'outil/lieu)
            elif parts[0] == 'M':
                return f"{parts[1]}-{parts[2]}-{parts[3]}"
            # Ex: Y-A.-L-M -> Enlève la lettre de conjugaison (Y, T, A, N)
            elif parts[0] in ['Y', 'T', 'A', 'N']: 
                return f"{parts[1]}-{parts[2]}-{parts[3]}"
                
        # RÉDUCTION DES GABARITS À 5 LETTRES (Ex: Maf'ool = M-K-T-W-B)
        if len(parts) == 5:
            if parts[0] == 'M' and parts[3] == 'W':
                return f"{parts[1]}-{parts[2]}-{parts[4]}"
                
        return latin_str

    def process(self, token):
        """Moteur d'inférence principal."""
        is_arabic = bool(re.search(r'[\u0600-\u06FF]', token))
        
        if is_arabic:
            clean_ar = self.clean_arabic(token)
            
            # 1. OVERRIDE : Résolution immédiate des anomalies connues (S-M-W, A-L-H)
            if clean_ar in self.systemic_constants:
                return self.systemic_constants[clean_ar], None
                
            # 2. TRANSLITTÉRATION : Conversion en code source
            raw_latin = self.to_veritas_latin(clean_ar)
            
            # 3. STEMMING : Amputation vers la racine trilitère
            pure_root = self.stem_latin_root(raw_latin)
            
            return pure_root, None
            
        # Bloc Latin pour la compatibilité avec l'ancien système manuel
        token_upper = token.upper().strip()
        for p in self.patterns:
            if token_upper.startswith(p["prefix"]):
                clean_root_chars = token_upper[len(p["prefix"]):].replace("-", "")
                if len(clean_root_chars) >= 3:
                    return token_upper[len(p["prefix"]):].strip("-"), p
        return token_upper, None

# Instanciation globale
morpho = MorphologyEngine()

# ==============================================================================
# 2. CONFIGURATION STREAMLIT
# ==============================================================================
st.set_page_config(
    page_title=f"{config['app']['name']} {config['app']['version']}",
    page_icon="💠",
    layout="wide",
    initial_sidebar_state="expanded"
)

def update_search(new_term):
    st.session_state["search_input"] = new_term


# ==============================================================================
# 3. STYLE CSS (THEME: MIDNIGHT BLUE - V13.2 REFERENCE)
# ==============================================================================
st.markdown("""
<style>
    /* FOND PRINCIPAL */
    .stApp {
        background-color: #0d1b2a; 
    }
    
    /* SIDEBAR */
    section[data-testid="stSidebar"] {
        background-color: #f0f2f6;
        border-right: 1px solid #d0d0d0;
    }
    section[data-testid="stSidebar"] * {
        color: #000000 !important; /* Force le texte noir */
    }
    
    /* INPUTS */
    .stTextInput > div > div > input {
        background-color: #1b263b; 
        color: #e0e1dd; 
        border: 1px solid #415a77;
    }
    .stSelectbox > div > div {
        background-color: #1b263b;
        color: #e0e1dd;
        border: 1px solid #415a77;
    }
    .stTextArea > div > div > textarea {
        background-color: #1b263b;
        color: #e0e1dd;
        border: 1px solid #415a77;
    }
    
    /* TEXTES GÉNÉRAUX */
    h1, h2, h3 {color: #e0e1dd !important;}
    p, li, label {color: #b0c4de !important;}
    
    /* --- CORRECTION DES TABLEAUX MARKDOWN --- */
    div[data-testid="stMarkdownContainer"] table {
        width: 100%;
        border-collapse: collapse !important;
        background-color: #162544 !important; /* Fond carte */
        border: 1px solid #415a77 !important;
    }
    div[data-testid="stMarkdownContainer"] th {
        background-color: #0d1b2a !important; /* Fond entête sombre */
        color: #00ff41 !important; /* TITRES EN VERT MATRIX */
        border: 1px solid #415a77 !important;
        padding: 10px !important;
        font-family: 'Consolas', monospace;
    }
    div[data-testid="stMarkdownContainer"] td {
        color: #e0e1dd !important; /* Texte clair */
        border: 1px solid #415a77 !important;
        padding: 8px !important;
    }
    div[data-testid="stMarkdownContainer"] td:nth-child(1) {
        font-family: 'Amiri', serif; /* Arabe */
        font-size: 18px;
        color: #ffd700 !important; /* Or */
    }

    /* CARDS UI */
    .metric-card {
        background-color: #162544;
        border: 1px solid #415a77;
        padding: 20px;
        border-radius: 8px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.3);
        margin-bottom: 15px;
    }
    .root-title {font-size: 28px; font-weight: bold; color: #00ff41;}
    .arabic-display {font-family: 'Amiri', serif; font-size: 38px; color: #ffd700; direction: rtl; float: right;}
    
    /* TAGS */
    .logic-func {
        font-family: 'Consolas', monospace; 
        color: #ff9e9e; 
        font-weight: bold; 
        background: #3a0ca3; 
        padding: 4px 8px; 
        border-radius: 4px; 
        font-size: 14px;
    }
    .morph-tag {
        font-size: 10px; 
        font-weight: bold; 
        padding: 2px 5px; 
        border-radius: 3px; 
        color: #000; 
        margin-right: 5px; 
        display: inline-block;
    }

    /* CONSOLE */
    .console-log {
        background-color: #000;
        border: 1px solid #333;
        color: #00ff41;
        font-family: 'Consolas', monospace;
        padding: 15px;
        font-size: 13px;
        border-left: 3px solid #00ff41;
        margin-top: 20px;
    }
    
    /* BOUTONS */
    .stButton>button {
        border: 1px solid #415a77;
        color: #e0e1dd; 
        background-color: #1b263b;
    }
    .stButton>button:hover {
        border-color: #00ff41; 
        color: #00ff41;
    }
</style>
""", unsafe_allow_html=True)

# ==============================================================================
# 4. CHARGEMENT DES DONNÉES
# ==============================================================================
@st.cache_resource
def get_repo():
    return LexiconRepository(filepath=config['database']['path'])

repo = get_repo()
exporter = ExportManager()

# ==============================================================================
# 5. SIDEBAR NAVIGATION (UNIFIÉE)
# ==============================================================================
with st.sidebar:
    st.title("VERITAS KERNEL")
    st.caption(f"v14.4 | STABLE")
    st.markdown("---")
    
    # CHARGEMENT DATAFRAME
    raw_data = repo.get_all_roots()
    df_roots = pd.DataFrame(raw_data)
    count = len(df_roots) if not df_roots.empty else 0

    col1, col2 = st.columns(2)
    with col1:
        st.metric("ROOTS", count)
    with col2:
        st.metric("STATUS", "ONLINE")
    
    st.markdown("---")
    
    # MENU UNIQUE
    mode = st.radio(
        "MODULES", 
        ["MANIFESTO & GUIDE", "THESIS DOCUMENTATION", "VERSE INTERPRETER", "LOGIC SEQUENCER", "ROOT SCANNER", "GOVERNANCE MAP", "MATRIX VIEW"]
    )
    
    st.markdown("---")
    st.info("Authorized Access Only")

# ==============================================================================
# MODULE: MANIFESTO & GUIDE (PAGE D'ACCUEIL)
# ==============================================================================
if mode == "MANIFESTO & GUIDE":
    st.title("⚠️ VERITAS KERNEL : MANIFESTE & PROTOCOLE")
    st.markdown("---")
    
    col_text, col_stats = st.columns([2, 1])
    
    with col_text:
        st.markdown("""
        ### 🧬 LE CONCEPT (COHÉRENCE SYSTÉMIQUE ABSOLUE)
        Le système **VERITAS** transcende les outils de traduction classiques et les recueils d'exégèses. Il opère comme un moteur d'inférence conçu pour **décrypter l'architecture du texte coranique** (son "code source"). En s'appuyant sur la rigueur mathématique des racines (*Maqasid al-Huruf*), il établit une correspondance stricte avec la logique computationnelle et la théorie des systèmes. Cette méthode permet à l'intelligence artificielle d'appréhender le Message sacré à travers son propre paradigme, en lisant le texte avec des unités de langage purement logiques et fonctionnelles.
        
        La prémisse est stricte : le langage divin est une architecture physique et logique parfaite. Au fil du temps, le consensus traditionnel (exégèses, hadiths) a superposé à ce code source des filtres interprétatifs, souvent liés aux rituels et à la jurisprudence d'une époque. Le système Veritas a pour fonction de contourner ces couches historiques pour isoler la donnée brute et restaurer le sens systémique et universel de chaque racine.
        """)
        
        st.warning("""
        **⚖️ SAUVEGARDE ÉPISTÉMOLOGIQUE (LIMITES DU SYSTÈME)**\n
        Il est fondamental de préciser que l'architecture VERITAS ne prétend en aucun cas détenir la vérité absolue ni épuiser l'infinité du texte coranique. Ce noyau demeure un modèle heuristique et une tentative humaine. Son unique ambition est de proposer une démarche rationnelle, méthodique et transparente pour se rapprocher au mieux de la pureté du code source originel. C'est un outil d'exploration conçu pour rendre la mécanique du Message accessible à l'intellect humain, avec humilité, sans jamais s'ériger en autorité définitive.
        """)

    with col_stats:
        st.info("📊 **STATUT DE DÉVELOPPEMENT**")
        st.markdown(f"""
        Ce noyau est actuellement en version **Alpha**. 
        
        Il ne couvre pas encore l'intégralité du vocabulaire coranique. Le lexique central est injecté manuellement et vérifié chirurgicalement.
        
        * **Racines actuellement indexées :** <span style='color:#00ff41; font-weight:bold; font-size:18px;'>{count}</span>
        * Si un verset contient une racine non indexée, le système le signalera par le tag `[HORS-LEXIQUE]` et tentera une déduction logique.
        """, unsafe_allow_html=True)

    st.markdown("---")
    
    # SCHÉMA EXPLICATIF DE L'ARCHITECTURE
    st.markdown("### ⚙️ ARCHITECTURE D'EXÉCUTION (COMMENT ÇA MARCHE)")
    flow_code = """
    digraph G {
        bgcolor="#0d1b2a"
        rankdir=LR
        node [style=filled, fontname="Consolas", shape=box, fontcolor="#e0e1dd", color="#415a77", fillcolor="#1b263b"]
        edge [color="#00ff41", fontname="Consolas", fontsize=10]
        
        A [label="INPUT\\n(Verset Coranique)", shape=folder, fillcolor="#3a0ca3", color="#ff9e9e"]
        B [label="ISOLATION\\n(Neutralisation Affixes)"]
        C [label="NOYAU VERITAS\\n(Lookup JSON)", shape=cylinder, fillcolor="#00aa00", fontcolor="black"]
        D [label="PHASE 1\\nTableau Matrice"]
        E [label="PHASE 2 & 3\\nAnalyse Logique\\n& Littéraire"]
        F [label="PHASE 4\nRupture de Consensus", fillcolor="#4a0000", fontcolor="#ff4b4b", color="#ff0000"]
        
        A -> B [label=" Signal Brut"]
        B -> C [label=" Extraction Racines"]
        C -> D [label=" Fetch Définitions"]
        D -> E [label=" Séquençage"]
        E -> F [label=" Confrontation"]
    }
    """
    st.graphviz_chart(flow_code, use_container_width=True)

    st.markdown("---")

    # LÉGENDE DE TRANSLITTÉRATION
    st.markdown("### 🔠 MATRICE DE TRANSLITTÉRATION (LÉGENDE)")
    st.markdown("""
    Pour garantir l'intégrité de la base de données sans subir les variations d'encodage de l'alphabet arabe, le système convertit les racines en utilisant une syntaxe latine stricte.
    
    | Catégorie | Lettre Arabe | Code Veritas | Remarque Systémique |
    | :--- | :---: | :---: | :--- |
    | **OBLIGATOIRE (POINT)** | ع / ح / ص / ط / ظ / ض | **A. / H. / S. / T. / Z. / D.** | Le point "." est une donnée critique pour différencier des lettres sœurs. |
    | **STANDARD (SANS POINT)** | أ / ه / س / ت / ز / د | **A / H / S / T / Z / D** | Transcodage direct. |
    | **CONVENTIONNELLE** | ش / خ / ذ | **SH / KH / DH** | Combinaison binaire. |
    """)


# ==============================================================================
# MODULE: THESIS DOCUMENTATION
# ==============================================================================
elif mode == "THESIS DOCUMENTATION":
    st.title("🧠 VERITAS KERNEL : L'Architecture")
    st.markdown("Documentation complète du noyau théorique et de la méthode d'ingénierie inverse.")
    st.markdown("---")
    
    # Création de 3 onglets pour naviguer facilement sans surcharger la page
    tab1, tab2, tab3 = st.tabs(["Phase 1 : Le Bootstrap", "Phase 2 : La Syntaxe", "Phase 3 : Le Requêtage"])
    
    # Fonction sécurisée de lecture
    def lire_fichier_markdown(chemin):
        try:
            with open(chemin, 'r', encoding='utf-8') as f:
                return f.read()
        except FileNotFoundError:
            return f"<div style='color: #ff4b4b; padding: 20px; border: 1px solid #ff4b4b;'>⚠️ ERREUR : Le fichier <b>{chemin}</b> est introuvable. Vérifiez qu'il est bien placé dans le dossier 'thesis/'.</div>"

    # Affichage dans les onglets avec le rendu HTML autorisé
    with tab1:
        st.markdown(lire_fichier_markdown("thesis/PHASE_1.md"), unsafe_allow_html=True)
    with tab2:
        st.markdown(lire_fichier_markdown("thesis/PHASE_2.md"), unsafe_allow_html=True)
    with tab3:
        st.markdown(lire_fichier_markdown("thesis/PHASE_3.md"), unsafe_allow_html=True)

# ==============================================================================
# MODULE: VERSE INTERPRETER (INTELLIGENCE ARTIFICIELLE)
# ==============================================================================
if mode == "VERSE INTERPRETER":
    st.title("📖 VERSE INTERPRETER NODE")
    st.markdown("Protocole de décompilation IA sous contrainte Lexicale (Gemini).")
    st.markdown("---")

    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Sécurité matérielle : Blocage strict à 1500 caractères (Frontend)
        verse_input = st.text_area(
            "SIGNAL INPUT (ARABIC)", 
            height=150, 
            max_chars=1500, 
            placeholder="Ex: ...بِسۡمِ ٱللَّهِ ٱلرَّحۡمَٰنِ ٱلرَّحِيمِ ..."
        )
    
    with col2:
        st.info("ℹ️ Le système scannera le verset et injectera la base compressée en mémoire tampon pour optimiser le protocole et réduire la latence.")

    if st.button("🚀 EXECUTE SYSTEMIC DECOMPILATION"):
        if verse_input:
            status_container = st.status("System processing...", expanded=True)
            status_container.write("🔌 Initializing connection to Gemini Core...")
            status_container.write("📂 Injecting Full Minified Lexicon...")
            
            # 1. Extraction Totale & Minification Extrême (Bypass du filtre défaillant)
            all_roots = repo.get_all_roots()
            compressed_payload = json.dumps(
                {"database": all_roots}, 
                ensure_ascii=False, 
                separators=(',', ':')
            )

            # 2. Appel au Moteur IA
            status_container.write("🧠 Executing Systemic Parsing...")
            ai_engine = VeritasAI()
            result = ai_engine.generate_systemic_translation(verse_input, compressed_payload)
            
            status_container.update(label="Compilation Complete", state="complete", expanded=False)

            # 3. Affichage du Résultat
            st.markdown("### 🧬 SYSTEMIC OUTPUT")
            st.markdown("---")
            st.markdown(result)
            
        else:
            st.warning("AWAITING SIGNAL...")

# ==============================================================================
# MODULE: LOGIC SEQUENCER (MOTEUR DE COMPILATION CAUSALE)
# ==============================================================================
elif mode == "LOGIC SEQUENCER":
    st.title("⛓️ LOGIC SEQUENCER")
    st.markdown("Compilation syntaxique totale. Détection des opérateurs (Lexer), des états de surface (Tasreef) et extraction des racines systémiques.")
    
    # Importation sécurisée des moteurs d'arrière-plan
    try:
        from engine import veritas_lexer
        from engine import tasreef_engine
    except ImportError:
        st.error("SYSTEM FAULT: Les modules 'veritas_lexer.py' et/ou 'tasreef_engine.py' sont introuvables. Vérifiez leur présence dans le répertoire.")
        st.stop()

    c1, c2 = st.columns([4, 1])
    with c1:
        input_seq = st.text_input("SOURCE SEQUENCE (ARABIC)", "بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ")
    with c2:
        st.write("")
        st.write("")
        run_btn = st.button("▶ COMPILE SEQUENCE", type="primary", use_container_width=True)

    if run_btn or input_seq:
        if not input_seq.strip():
            st.warning("SYSTEM FAULT: Sequence empty.")
            st.stop()
            
        # 1. ANALYSE LEXICALE (BACKGROUND)
        lexed_tokens = veritas_lexer.lex_verse(input_seq)
        
        # Initialisation du Graphe Systémique
        graph = graphviz.Digraph()
        graph.attr(rankdir='LR', bgcolor='#0d1b2a', compound='true')
        graph.attr('node', fontname='Segoe UI', margin='0.2')
        graph.attr('edge', fontname='Consolas', fontsize='10', color='#888', penwidth='1.5')

        console_logs = []
        previous_node = None
        
        st.markdown("### SYSTEM EXECUTION LOG")
        log_container = st.empty()
        
        # 2. TRAITEMENT DE LA MATRICE LEXICALE
        for i, item in enumerate(lexed_tokens):
            node_id = f"node_{i}"
            
            if item["type"] == "OPERATOR":
                op_tag = item["tag"]
                op_arabic = item["arabic"]
                
                # Nœud Opérateur (Forme géométrique distincte)
                label = f"<{op_arabic}<BR/><FONT POINT-SIZE='9' COLOR='#ffd700'>{op_tag}</FONT>>"
                graph.node(node_id, label=label, shape='circle', style='filled', fillcolor='#415a77', color='#ffd700', fontcolor='#ffffff')
                
                console_logs.append(f"[LEXER] Opérateur : {op_arabic} -> {op_tag}")
                
                if previous_node:
                    graph.edge(previous_node, node_id, color='#ffd700', style='dashed')
                previous_node = node_id
                
            elif item["type"] == "VARIABLE":
                raw_word = item["arabic"]
                
                # Analyse de l'état (Tasreef)
                tasreef_data = tasreef_engine.analyze_pattern(raw_word, raw_word)
                quantifiers = tasreef_engine.extract_quantifiers(raw_word)
                
                t_tag = tasreef_data["tag"]
                t_logic = tasreef_data["logic_mod"]
                
                # Tentative d'extraction brute pour la recherche DB
                # Note: Dans une version future, un extracteur de racine pur remplacera raw_word
                # Ici, on passe le mot brut au repo, ou on applique ton morpho s'il gère l'arabe
                extracted_root, morph_data = morpho.process(raw_word) 
                data = repo.find_root(extracted_root) # Ou repo.find_root(raw_word) selon ta DB
                
                if data:
                    base_func = data.get('logic_function', 'UNDEFINED').split("//")[0].strip()
                    root_disp = data.get('root', extracted_root)
                    
                    label = f"<{raw_word}<BR/><FONT POINT-SIZE='11' COLOR='#00ff41'>{root_disp}</FONT><BR/><FONT POINT-SIZE='9' COLOR='#aaaaaa'>{t_logic}</FONT><BR/><FONT POINT-SIZE='10'>{base_func}</FONT>>"
                    graph.node(node_id, label=label, shape='box', style='filled, rounded', fillcolor='#1b263b', color='#00ff41', fontcolor='#e0e1dd', penwidth='2.0')
                    
                    console_logs.append(f"[SYSTEM] Variable : {raw_word} -> Racine [{root_disp}] | État : {t_logic}")
                else:
                    label = f"<{raw_word}<BR/><FONT POINT-SIZE='9' COLOR='#ff9e9e'>UNMAPPED ROOT</FONT><BR/><FONT POINT-SIZE='9' COLOR='#aaaaaa'>{t_logic}</FONT>>"
                    graph.node(node_id, label=label, shape='box', style='filled, rounded', fillcolor='#3a0000', color='#ff0000', fontcolor='#ff9e9e')
                    console_logs.append(f"<span style='color:#ffaa00;'>[WARNING] Variable : {raw_word} -> Racine inconnue en base. État estimé : {t_logic}</span>")

                # Traitement des quantificateurs (Pluriel/Duel)
                if quantifiers:
                    q_labels = " + ".join([q["logic_mod"] for q in quantifiers])
                    console_logs.append(f"       ↳ Modificateur de quantité détecté : {q_labels}")

                if previous_node:
                    graph.edge(previous_node, node_id, color='#e0e1dd')
                previous_node = node_id

        # Rendu des logs dynamiques
        log_html = "<div class='console-log' style='font-family: monospace; background: #0d1b2a; padding: 15px; border-radius: 5px; color: #00ff41; height: 200px; overflow-y: auto;'>"
        log_html += "<br>".join([f"<div>> {l}</div>" for l in console_logs])
        log_html += "</div>"
        log_container.markdown(log_html, unsafe_allow_html=True)

        # Rendu du Graphe Causal
        st.markdown("### CAUSAL SYSTEM GRAPH")
        st.graphviz_chart(graph, use_container_width=True)

# ==============================================================================
# MODULE: ROOT SCANNER
# ==============================================================================
elif mode == "ROOT SCANNER":
    st.title("🔍 ROOT SCANNER")
    
    # 1. Sécurisation de la liste des racines
    all_roots_list = df_roots['root'].tolist() if (not df_roots.empty and 'root' in df_roots.columns) else []
    all_roots_list.sort()
    
    # 2. Gestion stricte de l'état (Évite le blocage des inputs)
    if "search_input" not in st.session_state:
        st.session_state["search_input"] = ""
    if "select_input" not in st.session_state:
        st.session_state["select_input"] = ""

    def sync_from_text():
        st.session_state["select_input"] = ""

    def sync_from_select():
        st.session_state["search_input"] = st.session_state["select_input"]

    c1, c2 = st.columns([2, 1])
    with c1:
        query_text = st.text_input(
            "TYPE SIGNAL", 
            key="search_input", 
            on_change=sync_from_text
        ).strip()
    with c2:
        selected_root = st.selectbox(
            "OR SELECT FROM DB", 
            [""] + all_roots_list, 
            key="select_input", 
            on_change=sync_from_select
        )
    
    # La variable maître est désormais unifiée
    final_query = query_text if query_text else selected_root
    
    if final_query:
        result = repo.find_root(final_query)
        if result:
            st.markdown("---")
            col_main, col_detail = st.columns([1, 2])
            
            with col_main:
                # 3. Accès sécurisé aux données (Prévention des KeyError)
                arabic_disp = result.get('arabic', 'N/A')
                root_disp = result.get('root', 'UNKNOWN')
                logic_disp = result.get('logic_function', 'UNDEFINED')
                
                st.markdown(f"""<div class='metric-card'>
<div class='arabic-display'>{arabic_disp}</div>
<div class='root-title'>{root_disp}</div>
<div style='margin-top:15px;'>
<span class='logic-func'>{logic_disp}</span>
</div>
</div>""", unsafe_allow_html=True)
                
                binary_pair = result.get('binary_pair')
                if binary_pair and binary_pair != "N/A":
                    st.caption("BINARY SWITCH")
                    if "/" in binary_pair:
                        for op in binary_pair.split("/"):
                            clean_op = op.strip()
                            # Clé sécurisée
                            st.button(f"⇄ {clean_op}", key=f"btn_split_{clean_op}", on_click=update_search, args=(clean_op,), use_container_width=True)
                    else:
                        # 4. Ajout de la clé manquante
                        st.button(f"⇄ {binary_pair}", key=f"btn_single_{binary_pair}", on_click=update_search, args=(binary_pair,), use_container_width=True)
            
            with col_detail:
                st.markdown("#### SYSTEM DEFINITION")
                st.info(result.get('description', 'No definition found in system.'))
                
                st.markdown("#### ACTIONS")
                if config.get('modules', {}).get('enable_export', False):
                    # 5. Sécurisation de la sérialisation JSON
                    import json
                    json_data = exporter.generate_json(result)
                    
                    # Force la conversion en string si la fonction renvoie un dict
                    if isinstance(json_data, dict):
                        json_data = json.dumps(json_data, ensure_ascii=False, indent=4)
                        
                    st.download_button(
                        label="📥 EXPORT JSON PACKET", 
                        data=json_data, 
                        file_name=f"{root_disp}.json", 
                        mime="application/json", 
                        use_container_width=True,
                        key=f"export_{root_disp}"
                    )
# ==============================================================================
# MODULE: MATRIX VIEW
# ==============================================================================
elif mode == "MATRIX VIEW":
    st.title("🌐 KERNEL MATRIX")
    st.dataframe(df_roots, use_container_width=True, height=700)
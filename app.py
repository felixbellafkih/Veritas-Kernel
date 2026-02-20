import json
import streamlit as st
import graphviz
import pandas as pd
from data.repository import LexiconRepository
from core.config import config
from export.manager import ExportManager
from engine.ai_bridge import VeritasAI  # Import du Pont IA

# ==============================================================================
# 1. MOTEUR MORPHOLOGIQUE (SYSTEME DE DÉTECTION DES FORMES)
# ==============================================================================
class MorphologyEngine:
    def __init__(self):
        self.patterns = [
            # FORM X: I-S-T (Demande/Requête)
            {
                "prefix": "I-S-T-A.", 
                "suffix": "",
                "logic_mod": "REQUEST_PROTOCOL", 
                "color": "#FF00FF", # Magenta
                "desc_mod": "Tentative d'initialiser ou de demander la fonction : "
            },
            # FORM IV: A- (Causal/Transitif)
            {
                "prefix": "A-A.", 
                "suffix": "",
                "logic_mod": "CAUSAL_OUTPUT", 
                "color": "#FFA500", # Orange
                "desc_mod": "Exécution transitive vers l'extérieur de : "
            },
            # PLURIEL: -WN (Agents multiples)
            {
                "prefix": "", 
                "suffix": "-W-N",
                "logic_mod": "ACTIVE_CLUSTER", 
                "color": "#00FFFF", # Cyan
                "desc_mod": "Groupe d'instances exécutant la fonction : "
            },
             # MAF'UL: M- (Passif/Objet)
            {
                "prefix": "M-A.", 
                "suffix": "",
                "logic_mod": "PASSIVE_OBJECT", 
                "color": "#FFFF00", # Jaune
                "desc_mod": "Objet résultant du traitement : "
            }
        ]

    def process(self, token):
        """
        Analyse un token pour extraire la racine et le pattern.
        Gère l'exception des racines courtes (ex: A-L-H).
        """
        token = token.upper().strip()
        
        for p in self.patterns:
            match_prefix = token.startswith(p["prefix"]) if p["prefix"] else True
            match_suffix = token.endswith(p["suffix"]) if p["suffix"] else True
            
            if match_prefix and match_suffix:
                # Calcul des indices de découpe
                start = len(p["prefix"])
                end = len(token) - len(p["suffix"])
                potential_root = token[start:end]
                
                # NETTOYAGE CRITIQUE : 
                # On enlève les tirets pour compter les vraies lettres.
                # Cela empêche de couper A-L-H (qui deviendrait L-H, 2 lettres).
                clean_root_chars = potential_root.replace("-", "")

                # SÉCURITÉ : On ne valide la coupe que s'il reste 3 lettres ou plus
                if len(clean_root_chars) >= 3:
                    return potential_root.strip("-"), p
        
        # Si aucun pattern, on retourne le token brut
        return token, None

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
        ["MANIFESTO & GUIDE", "VERSE INTERPRETER", "LOGIC SEQUENCER", "ROOT SCANNER", "GOVERNANCE MAP", "MATRIX VIEW"]
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
        
        * **Racines actuellement indexées :** `<span style='color:#00ff41; font-weight:bold; font-size:18px;'>{count}</span>`
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
        F [label="PHASE 4\\nDestruction du Consensus", fillcolor="#4a0000", fontcolor="#ff4b4b", color="#ff0000"]
        
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
# MODULE: LOGIC SEQUENCER (AVEC MORPHOLOGIE)
# ==============================================================================
elif mode == "LOGIC SEQUENCER":
    st.title("⛓️ LOGIC SEQUENCER")
    st.markdown("Construct causal chains. Supports Morphological Wrappers (IST-, A-, M-).")
    
    c1, c2 = st.columns([4, 1])
    with c1:
        input_seq = st.text_input("ROOT SEQUENCE", "B-S-M A-L-H R-H.-M-N R-H.-Y-M")
    with c2:
        st.write("")
        st.write("")
        run_btn = st.button("▶ EXECUTE", type="primary", use_container_width=True)

    if run_btn or input_seq:
        tokens = input_seq.split()
        
        graph = graphviz.Digraph()
        graph.attr(rankdir='LR', bgcolor='#0d1b2a')
        graph.attr('node', shape='box', style='filled', fontname='Segoe UI', margin='0.2')
        graph.attr('edge', fontname='Consolas', fontsize='10', color='#888')

        console_logs = []
        previous_node = None
        
        if not tokens:
            st.warning("Sequence empty.")
            st.stop()
            
        cols = st.columns(len(tokens))
        
        for i, token in enumerate(tokens):
            extracted_root, morph_data = morpho.process(token)
            data = repo.find_root(extracted_root)
            
            if data:
                base_func = data['logic_function'].split("//")[0].strip()
                arabic = data['arabic']
                binary = data.get('binary_pair', 'N/A')
                description_short = data['description'][:60] + "..."
                
                if morph_data:
                    final_func = f"{morph_data['logic_mod']} \n>> {base_func}"
                    node_color = morph_data['color']
                    fill_color = "#2a2a2a"
                    label = f"<{token}<BR/><FONT POINT-SIZE='9'>{final_func}</FONT>>"
                    console_logs.append(f"[MORPHO] Wrapper <b>{morph_data['logic_mod']}</b> applied on <b>{extracted_root}</b>")
                else:
                    final_func = base_func
                    node_color = "#00ff41"
                    fill_color = "#1b263b"
                    label = f"<{token}<BR/><FONT POINT-SIZE='10'>{final_func}</FONT>>"
                    console_logs.append(f"[ROOT] Loaded <b>{extracted_root}</b>")

                node_id = f"node_{i}"
                penwidth = '2.0' if morph_data else '1.0'
                graph.node(node_id, label=label, color=node_color, fillcolor=fill_color, fontcolor='#e0e1dd', penwidth=penwidth)
                
                if binary and binary != "N/A":
                    ghost_id = f"ghost_{i}"
                    graph.node(ghost_id, label=f"NOT {binary}", color='#772222', fontcolor='#ff9e9e', style='dashed, filled', fillcolor='#2a0a0a', fontsize='9')
                    with graph.subgraph() as s:
                        s.attr(rank='same')
                        s.node(node_id)
                        s.node(ghost_id)
                        s.edge(node_id, ghost_id, style='invis')

                if previous_node:
                    graph.edge(previous_node, node_id, color='#e0e1dd')
                previous_node = node_id
                
                with cols[i]:
                    border_color = morph_data['color'] if morph_data else "#00ff41"
                    morph_html = ""
                    if morph_data:
                        morph_html = f"<div style='margin-top:5px;'><span class='morph-tag' style='background:{border_color};'>{morph_data['logic_mod']}</span></div>"
                    
                    morph_desc_text = morph_data['desc_mod'] if morph_data else "Fonction native : "

                    html_card = f"""<div class='metric-card' style='border-top: 3px solid {border_color};'>
<div style='color:#e0e1dd; font-weight:bold; font-size:18px;'>{token}</div>
<div style='color:#ffd700; font-size:24px; direction:rtl;'>{arabic}</div>
{morph_html}
<div style='font-size:12px; color:#b0c4de; margin-top:5px;'>
{morph_desc_text}<br>
<i>{description_short}</i>
</div>
<div style='font-size:11px; color:#ff9e9e; margin-top:8px; border-top:1px solid #415a77; padding-top:4px;'>
⛔ REJECTS: {binary}
</div>
</div>"""
                    st.markdown(html_card, unsafe_allow_html=True)
            else:
                graph.node(f"node_{i}", label=f"{token} (?)", color='#ff0000')
                with cols[i]:
                    st.error(f"{extracted_root} ?")
                    st.caption(f"Raw: {token}")

        st.graphviz_chart(graph, use_container_width=True)
        st.markdown(f"<div class='console-log'>" + "<br>".join([f"<div>> {l}</div>" for l in console_logs]) + "</div>", unsafe_allow_html=True)

# ==============================================================================
# MODULE: ROOT SCANNER
# ==============================================================================
elif mode == "ROOT SCANNER":
    st.title("🔍 ROOT SCANNER")
    
    all_roots_list = df_roots['root'].tolist() if not df_roots.empty else []
    all_roots_list.sort()
    
    c1, c2 = st.columns([2, 1])
    with c1:
        if "search_input" not in st.session_state:
            st.session_state["search_input"] = ""
        query_text = st.text_input("TYPE SIGNAL", key="search_input").strip()
    with c2:
        selected_root = st.selectbox("OR SELECT FROM DB", [""] + all_roots_list)
    
    final_query = selected_root if selected_root else query_text
    
    if final_query:
        result = repo.find_root(final_query)
        if result:
            st.markdown("---")
            col_main, col_detail = st.columns([1, 2])
            
            with col_main:
                st.markdown(f"""<div class='metric-card'>
<div class='arabic-display'>{result['arabic']}</div>
<div class='root-title'>{result['root']}</div>
<div style='margin-top:15px;'>
<span class='logic-func'>{result['logic_function']}</span>
</div>
</div>""", unsafe_allow_html=True)
                
                if result.get('binary_pair') and result['binary_pair'] != "N/A":
                    st.caption("BINARY SWITCH")
                    raw_pair = result['binary_pair']
                    if "/" in raw_pair:
                        for op in raw_pair.split("/"):
                            st.button(f"⇄ {op.strip()}", key=f"btn_{op}", on_click=update_search, args=(op.strip(),), use_container_width=True)
                    else:
                        st.button(f"⇄ {raw_pair}", on_click=update_search, args=(raw_pair,), use_container_width=True)
            
            with col_detail:
                st.markdown("#### SYSTEM DEFINITION")
                st.info(result['description'])
                
                st.markdown("#### ACTIONS")
                if config['modules']['enable_export']:
                    json_data = exporter.generate_json(result)
                    st.download_button("📥 EXPORT JSON PACKET", json_data, f"{result['root']}.json", "application/json", use_container_width=True)

# ==============================================================================
# MODULE: GOVERNANCE MAP (ADMIN/DAEMON RESTORED)
# ==============================================================================
elif mode == "GOVERNANCE MAP":
    st.title("👑 GOVERNANCE TOPOLOGY")
    
    gov_code = """
    digraph G {
        bgcolor="#0d1b2a"
        rankdir=TB
        
        node [style=filled, fontname="Segoe UI", shape=box, fontcolor=white, color="#444", fillcolor="#1b263b"]
        edge [color="#888", fontname="Consolas", fontsize=10, fontcolor="#b0c4de"]
        
        ROOT [label="ROOT (ALLAH)\\n[Source of Command]", color="#FFD700", fontcolor="black", fillcolor="#FFD700", shape=doubleoctagon, height=1.2]
        
        subgraph cluster_admins {
            label = "ZONE: SYS_ADMINS (R-K-A.)"; 
            style=dashed; 
            color="#00ff41"; 
            fontcolor="#00ff41"
            
            KHALIFA [label="INSAN (User)\\n<TYPE: ADMIN>\\n[Voluntary Sync]", color="#00ff41", fontcolor="black", fillcolor="#00ff41"]
            DJINN [label="JINN (Hidden)\\n<TYPE: ADMIN>\\n[Rational Force]", color="#00aa00", fontcolor="black", fillcolor="#00aa00"]
        }
        
        subgraph cluster_automata {
            label = "ZONE: SYSTEM_DAEMONS (S-J-D)"; 
            style=dashed; 
            color="#ff4b4b"; 
            fontcolor="#ff4b4b"
            
            ANGELS [label="MALA'IKA\\n<TYPE: DAEMON>\\n[Exec Function]", color="#aaaaaa", fontcolor="black", fillcolor="#aaaaaa"]
            NATURE [label="PHYSICS ENGINE\\n<TYPE: KERNEL>\\n[Hard-Coded Laws]", color="#222", fontcolor="white", fillcolor="#222"]
        }
        
        ROOT -> KHALIFA [label="AMANAH (Sudo Access)"]
        ROOT -> ANGELS [label="A-M-R (Command)"]
        ROOT -> NATURE [label="Q-D-R (Measure)"]
        
        KHALIFA -> NATURE [style=dotted]
        ANGELS -> NATURE [style=dotted]
    }
    """
    st.graphviz_chart(gov_code, use_container_width=True)

# ==============================================================================
# MODULE: MATRIX VIEW
# ==============================================================================
elif mode == "MATRIX VIEW":
    st.title("🌐 KERNEL MATRIX")
    st.dataframe(df_roots, use_container_width=True, height=700)
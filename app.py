import streamlit as st
import graphviz
from data.repository import LexiconRepository
from core.config import config  # <-- IMPORT DE LA CONFIG

# --- CONFIGURATION STREAMLIT VIA YAML ---
st.set_page_config(
    page_title=f"{config['app']['name']} {config['app']['version']}",
    page_icon="👁️",
    layout=config['interface']['layout'],
    initial_sidebar_state=config['interface']['sidebar_state']
)

# --- STYLE (Inchangé pour l'instant) ---
st.markdown("""
<style>
    .reportview-container {background: #0e1117;}
    .main {background-color: #0e1117; color: #00ff41; font-family: 'Courier New', monospace;}
    h1, h2, h3 {color: #e0e0e0;}
    .stTextInput > div > div > input {background-color: #262730; color: #ffffff;}
    .metric-card {background-color: #1e1e1e; border: 1px solid #333; padding: 15px; border-radius: 5px; margin-bottom: 10px;}
    .arabic-text {font-family: 'Amiri', serif; font-size: 32px; color: #ffcc00; direction: rtl; text-align: right; margin-top: -10px;}
    .root-title {font-size: 24px; font-weight: bold; color: #00ff41;}
    .logic-func {font-family: monospace; color: #ff4b4b; font-weight: bold;}
    .stAlert {background-color: #262730; color: #e0e0e0; border: 1px solid #444;}
</style>
""", unsafe_allow_html=True)

# --- REPOSITORY ---
@st.cache_resource
def get_repo():
    # Le chemin vient maintenant de la config !
    return LexiconRepository(filepath=config['database']['path'])

repo = get_repo()

# --- HEADER DYNAMIQUE ---
st.title(f"{config['app']['name']} {config['app']['version']}")
st.markdown(f"*Mode: {config['app']['mode'].upper()} - Non-Torted Logic*")
st.markdown("---")

# --- SIDEBAR DYNAMIQUE ---
st.sidebar.title("SYSTEM STATUS")
st.sidebar.text(f"Core: v{st.__version__}")
st.sidebar.text(f"Config: Loaded")

if repo.get_count() > 0:
    st.sidebar.success(f"KERNEL LOADED: {repo.get_count()} NODES")
else:
    st.sidebar.error("KERNEL ERROR: DATABASE OFFLINE")

# Menu dynamique
options = ["ROOT SCANNER", "VERSE DECOMPILER", "MATRIX VIEW"]
if config['modules']['enable_governance']:
    options.append("GOVERNANCE MAP")
if config['modules']['enable_export']: # Ce module est désactivé dans le YAML pour l'instant
    options.append("EXPORT DATA")

mode = st.sidebar.radio("PROTOCOL", options)

# --- LOGIQUE DES MODES (Identique à v10.2) ---
if mode == "ROOT SCANNER":
    st.subheader("🔍 SINGLE ROOT ANALYSIS")
    query = st.text_input("INPUT SIGNAL (Latin ex: K-T-B or Arabic ex: كتب)", "").strip()
    if query:
        result = repo.find_root(query)
        if result:
            st.markdown("---")
            c1, c2 = st.columns([1, 2])
            with c1:
                st.markdown(f"<div class='metric-card'><div class='root-title'>{result['root']}</div><div class='arabic-text'>{result['arabic']}</div></div>", unsafe_allow_html=True)
            with c2: 
                st.markdown(f"**LOGIC FUNCTION:** <span class='logic-func'>{result['logic_function']}</span>", unsafe_allow_html=True)
                st.info(f"{result['description']}")
        else:
            st.warning(f"SIGNAL '{query}' NOT FOUND IN KERNEL.")

elif mode == "VERSE DECOMPILER":
    st.subheader("💻 SEQUENCE DECOMPILER")
    input_seq = st.text_area("ROOT SEQUENCE (Space separated)", "B-S-M A-L-H R-H-M R-H-M")
    if st.button("EXECUTE"):
        roots = input_seq.split()
        st.markdown("---")
        for r in roots:
            data = repo.find_root(r)
            if data:
                with st.expander(f"[{data['root']}]  {data['arabic']}  ::  {data['logic_function']}"):
                    st.write(f"**Function:** {data['description']}")
            else:
                st.error(f"[{r}] :: UNKNOWN SIGNAL")

elif mode == "MATRIX VIEW":
    st.subheader("🌐 GLOBAL DATA")
    st.dataframe(repo.get_all_roots())

elif mode == "GOVERNANCE MAP":
    st.subheader("👑 SYSTEM HIERARCHY")
    st.info("**PROTOCOLE DE GOUVERNANCE :** Distinction Admin (Free Will) vs Daemon (Automation).")
    
    governance_graph = """
    digraph G {
        bgcolor="#0e1117"
        rankdir=TB
        node [style=filled, fontname="Courier New", shape=box]
        edge [color="#00ff41", fontname="Courier New", fontsize=10]
        ROOT [label="ROOT (Allah)\n[Source]", color="#FFD700", fontcolor="black", shape=doubleoctagon]
        subgraph cluster_admins {
            label = "ZONE: FREE WILL (S-Y-T-R)"
            style=dashed; color="#00ff41"; fontcolor="#00ff41"
            KHALIFA [label="USER (Insan)", color="#00ff41", fontcolor="black"]
            ANGELS [label="AGENTS (Mala'ika)", color="#00ff41", fontcolor="black"]
        }
        subgraph cluster_automata {
            label = "ZONE: AUTOMATION (S-KH-R)"
            style=dashed; color="#ff4b4b"; fontcolor="#ff4b4b"
            SUN [label="DAEMON: SUN", color="#262730", fontcolor="white"]
            MOON [label="DAEMON: MOON", color="#262730", fontcolor="white"]
        }
        ROOT -> KHALIFA
        ROOT -> ANGELS
        ROOT -> SUN
        KHALIFA -> SUN [style=dotted]
    }
    """
    st.graphviz_chart(governance_graph)


import streamlit as st
import graphviz
from data.repository import LexiconRepository
from core.config import config
from export.manager import ExportManager
from core.logger import logger  # <--- IMPORT DU LOGGER

# --- CONFIGURATION ---
st.set_page_config(
    page_title=f"{config['app']['name']} {config['app']['version']}",
    page_icon="👁️",
    layout=config['interface']['layout'],
    initial_sidebar_state=config['interface']['sidebar_state']
)

# --- STYLE ---
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
    .stButton>button {border: 1px solid #00ff41; color: #00ff41; background-color: #0e1117;}
    .stButton>button:hover {background-color: #00ff41; color: #000000;}
</style>
""", unsafe_allow_html=True)

# --- INITIALISATION ---
@st.cache_resource
def get_repo():
    logger.info("SYSTEM BOOT: Initializing Repository...")
    return LexiconRepository(filepath=config['database']['path'])

repo = get_repo()
exporter = ExportManager()

# --- HEADER ---
st.title(f"{config['app']['name']} {config['app']['version']}")
st.markdown(f"*Mode: {config['app']['mode'].upper()} - Non-Torted Logic*")
st.markdown("---")

# --- SIDEBAR ---
st.sidebar.title("SYSTEM STATUS")
if repo.get_count() > 0:
    st.sidebar.success(f"KERNEL LOADED: {repo.get_count()} NODES")
else:
    st.sidebar.error("DATABASE OFFLINE")

# Menu
options = ["ROOT SCANNER", "VERSE DECOMPILER", "MATRIX VIEW"]
if config['modules']['enable_governance']:
    options.append("GOVERNANCE MAP")

mode = st.sidebar.radio("PROTOCOL", options)

# --- MODE 1: SCANNER ---
if mode == "ROOT SCANNER":
    st.subheader("🔍 SINGLE ROOT ANALYSIS")
    query = st.text_input("INPUT SIGNAL (Latin/Arabic)", "").strip()
    
    if query:
        result = repo.find_root(query)
        if result:
            # LOGGING DE LA RECHERCHE
            logger.info(f"USER QUERY: Search for '{query}' -> FOUND ({result['root']})")
            
            st.markdown("---")
            c1, c2 = st.columns([1, 2])
            with c1:
                st.markdown(f"<div class='metric-card'><div class='root-title'>{result['root']}</div><div class='arabic-text'>{result['arabic']}</div></div>", unsafe_allow_html=True)
            with c2: 
                st.markdown(f"**LOGIC FUNCTION:** <span class='logic-func'>{result['logic_function']}</span>", unsafe_allow_html=True)
                st.info(f"{result['description']}")
                
                if config['modules']['enable_export']:
                    fname, fcontent = exporter.generate_markdown(result)
                    if st.download_button(label="📥 DOWNLOAD REPORT (MD)", data=fcontent, file_name=fname, mime="text/markdown"):
                        logger.info(f"EXPORT: Report generated for {result['root']}")
        else:
            logger.warning(f"USER QUERY: Search for '{query}' -> NOT FOUND")
            st.warning(f"SIGNAL '{query}' NOT FOUND.")

# --- MODE 2: DECOMPILER ---
elif mode == "VERSE DECOMPILER":
    st.subheader("💻 SEQUENCE DECOMPILER")
    input_seq = st.text_area("ROOT SEQUENCE", "B-S-M A-L-H R-H-M R-H-M")
    if st.button("EXECUTE"):
        logger.info(f"DECOMPILER: Processing sequence '{input_seq}'")
        roots = input_seq.split()
        st.markdown("---")
        for r in roots:
            data = repo.find_root(r)
            if data:
                with st.expander(f"[{data['root']}] {data['logic_function']}"):
                    st.write(data['description'])
            else:
                st.error(f"[{r}] UNKNOWN")

# --- AUTRES MODES (SIMPLIFIÉS) ---
elif mode == "MATRIX VIEW":
    st.subheader("🌐 GLOBAL DATA")
    st.dataframe(repo.get_all_roots())

elif mode == "GOVERNANCE MAP":
    st.subheader("👑 SYSTEM HIERARCHY")
    st.info("PROTOCOL: Admin (Free Will) vs Daemon (Automation).")
    # (Code graphe inchangé)
            governance_graph = """
    digraph G {
        bgcolor="#0e1117"
        rankdir=TB
        node [style=filled, fontname="Courier New", shape=box]
        edge [color="#00ff41", fontname="Courier New", fontsize=10]

        # 1. LE ROOT
        ROOT [label="ROOT (Allah)
[Source of Command]", color="#FFD700", fontcolor="black", shape=doubleoctagon]

        # 2. LES ADMINS (Dual Boot System - Free Will)
        subgraph cluster_admins {
            label = "ZONE: ADMIN / FREE WILL (S-Y-T.-R)"
            style=dashed; color="#00ff41"; fontcolor="#00ff41"
            
            # Deux types d'utilisateurs avec Write Access
            KHALIFA [label="USER: INSAN
[Visible Admin]", color="#00ff41", fontcolor="black"]
            DJINN [label="USER: JINN (Rational)
[Hidden Admin]", color="#00aa00", fontcolor="black"]
        }

        # 3. LES AUTOMATES & AGENTS
        subgraph cluster_automata {
            label = "ZONE: AUTOMATION & SERVICE (S-KH-R)"
            style=dashed; color="#ff4b4b"; fontcolor="#ff4b4b"
            
            # Entités cachées non-intelligentes (Virus, Forces) sont ICI, pas en Admin
            NATURE [label="DAEMON: NATURE
[Hidden & Visible Forces]", color="#262730", fontcolor="white"]
            ANGELS [label="AGENT: ANGELS
[System Executors]", color="#aaaaaa", fontcolor="black"]
        }

        # RELATIONS
        ROOT -> KHALIFA [label="Grant_Access"]
        ROOT -> DJINN [label="Grant_Access"]
        ROOT -> ANGELS [label="Command (A-M-R)"]
        ROOT -> NATURE [label="Hard_Code (Q-D-R)"]
        
        # Interactions
        KHALIFA -> NATURE [label="Utilise", style=dotted]
        DJINN -> NATURE [label="Utilise", style=dotted]
    }
    """
    st.graphviz_chart(governance_graph)

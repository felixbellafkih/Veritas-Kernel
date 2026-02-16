import streamlit as st
import graphviz
from data.repository import LexiconRepository
from core.config import config
from export.manager import ExportManager
from core.logger import logger

# --- FONCTION CALLBACK ---
def update_search(new_term):
    st.session_state["search_input"] = new_term

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
    .stButton>button {border: 1px solid #00ff41; color: #00ff41; background-color: #0e1117; width: 100%;}
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

options = ["ROOT SCANNER", "VERSE DECOMPILER", "MATRIX VIEW"]
if config['modules']['enable_governance']:
    options.append("GOVERNANCE MAP")

mode = st.sidebar.radio("PROTOCOL", options)

# --- MODE 1: ROOT SCANNER ---
if mode == "ROOT SCANNER":
    st.subheader("🔍 SINGLE ROOT ANALYSIS")
    
    if "search_input" not in st.session_state:
        st.session_state["search_input"] = ""

    query = st.text_input("INPUT SIGNAL (Latin/Arabic)", key="search_input").strip()
    
    if query:
        result = repo.find_root(query)
        if result:
            st.markdown("---")
            c1, c2 = st.columns([1, 2])
            with c1:
                st.markdown(f"<div class='metric-card'><div class='root-title'>{result['root']}</div><div class='arabic-text'>{result['arabic']}</div></div>", unsafe_allow_html=True)
                
                # --- MOTEUR BINAIRE INTELLIGENT (MULTI-CHOICE) ---
                if result.get('binary_pair'):
                    raw_pair = result['binary_pair']
                    
                    # Détection de multiples opposés (séparés par /)
                    if "/" in raw_pair:
                        opposites = [p.strip() for p in raw_pair.split("/")]
                        st.markdown(f"**BINARY BRANCHING DETECTED:**")
                        for op in opposites:
                            st.button(
                                f"⇄ SWITCH TO: {op}",
                                key=f"btn_{op}", # Clé unique pour chaque bouton
                                on_click=update_search,
                                args=(op,)
                            )
                    else:
                        # Cas simple (1 vs 1)
                        st.markdown(f"**BINARY OPPOSITE:**")
                        st.button(
                            f"⇄ SWITCH TO: {raw_pair}",
                            on_click=update_search,
                            args=(raw_pair,)
                        )
                # ------------------------------------------------

            with c2: 
                st.markdown(f"**LOGIC FUNCTION:** <span class='logic-func'>{result['logic_function']}</span>", unsafe_allow_html=True)
                st.info(f"{result['description']}")
                
                if config['modules']['enable_export']:
                    fname, fcontent = exporter.generate_markdown(result)
                    st.download_button(
                        label="📥 DOWNLOAD REPORT (MD)",
                        data=fcontent,
                        file_name=fname,
                        mime="text/markdown"
                    )
        else:
            st.warning(f"SIGNAL '{query}' NOT FOUND.")

# --- AUTRES MODES (INCHANGÉS) ---
elif mode == "VERSE DECOMPILER":
    st.subheader("💻 SEQUENCE DECOMPILER")
    input_seq = st.text_area("ROOT SEQUENCE", "B-S-M A-L-H R-H-M R-H-M")
    if st.button("EXECUTE"):
        roots = input_seq.split()
        st.markdown("---")
        for r in roots:
            data = repo.find_root(r)
            if data:
                with st.expander(f"[{data['root']}] {data['logic_function']}"):
                    st.write(data['description'])
            else:
                st.error(f"[{r}] UNKNOWN")

elif mode == "MATRIX VIEW":
    st.subheader("🌐 GLOBAL DATA")
    st.dataframe(repo.get_all_roots())

elif mode == "GOVERNANCE MAP":
    st.subheader("👑 SYSTEM HIERARCHY")
    st.info("PROTOCOL: Admin (Free Will) vs Daemon (Automation).")
    gov_code = """
    digraph G {
        bgcolor="#0e1117"
        rankdir=TB
        node [style=filled, fontname="Courier New", shape=box]
        edge [color="#00ff41", fontname="Courier New", fontsize=10]
        ROOT [label="ROOT (Allah)\\n[Source of Command]", color="#FFD700", fontcolor="black", shape=doubleoctagon]
        subgraph cluster_admins {
            label = "ZONE: ADMIN / FREE WILL (S-Y-T.-R)"
            style=dashed; color="#00ff41"; fontcolor="#00ff41"
            KHALIFA [label="USER: INSAN\\n[Visible Admin]", color="#00ff41", fontcolor="black"]
            DJINN [label="USER: JINN (Rational)\\n[Hidden Admin]", color="#00aa00", fontcolor="black"]
        }
        subgraph cluster_automata {
            label = "ZONE: AUTOMATION & SERVICE (S-KH-R)"
            style=dashed; color="#ff4b4b"; fontcolor="#ff4b4b"
            NATURE [label="DAEMON: NATURE\\n[Hidden & Visible Forces]", color="#262730", fontcolor="white"]
            ANGELS [label="AGENT: ANGELS\\n[System Executors]", color="#aaaaaa", fontcolor="black"]
        }
        ROOT -> KHALIFA [label="Grant_Access"]
        ROOT -> DJINN [label="Grant_Access"]
        ROOT -> ANGELS [label="Command (A-M-R)"]
        ROOT -> NATURE [label="Hard_Code (Q-D-R)"]
        KHALIFA -> NATURE [label="Utilise", style=dotted]
        DJINN -> NATURE [label="Utilise", style=dotted]
    }
    """
    st.graphviz_chart(gov_code)
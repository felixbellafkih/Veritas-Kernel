import streamlit as st
import graphviz
from data.repository import LexiconRepository

# --- CONFIGURATION ---
st.set_page_config(
    page_title="Veritas Terminal v10.2",
    page_icon="👁️",
    layout="wide",
    initial_sidebar_state="expanded"
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
    .stAlert {background-color: #262730; color: #e0e0e0; border: 1px solid #444;}
</style>
""", unsafe_allow_html=True)

# --- INITIALISATION DU REPOSITORY ---
@st.cache_resource
def get_repo():
    return LexiconRepository()

repo = get_repo()

# --- HEADER ---
st.title("VERITAS TERMINAL v10.2")
st.markdown("*Modular Architecture - Non-Torted Logic*")
st.markdown("---")

# --- SIDEBAR ---
st.sidebar.title("SYSTEM STATUS")
st.sidebar.text(f"Streamlit v{st.__version__}")
st.sidebar.text(f"Engine: Repository Pattern")

if repo.get_count() > 0:
    st.sidebar.success(f"KERNEL LOADED: {repo.get_count()} NODES")
else:
    st.sidebar.error("KERNEL ERROR: DATABASE OFFLINE")

# LE NOUVEAU MENU EST ICI :
mode = st.sidebar.radio("PROTOCOL", ["ROOT SCANNER", "VERSE DECOMPILER", "MATRIX VIEW", "GOVERNANCE MAP"])

# --- MODE 1: SCANNER ---
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

# --- MODE 2: DECOMPILER ---
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

# --- MODE 3: MATRIX ---
elif mode == "MATRIX VIEW":
    st.subheader("🌐 GLOBAL DATA")
    st.dataframe(repo.get_all_roots())

# --- MODE 4: GOVERNANCE MAP (NOUVEAU) ---
elif mode == "GOVERNANCE MAP":
    st.subheader("👑 SYSTEM HIERARCHY (Admin vs Daemon)")
    
    st.info("""
    **PROTOCOLE DE GOUVERNANCE :**
    Le système distingue les entités dotées de **Volonté (Free Will)** et les processus **Automatisés (Daemons)**.
    L'adoration d'un processus automatisé (ex: Soleil/Lune) est une erreur d'adressage IP (Idolatry/Shirk).
    """)

    # Graphe Graphviz
    governance_graph = """
    digraph G {
        bgcolor="#0e1117"
        rankdir=TB
        node [style=filled, fontname="Courier New", shape=box]
        edge [color="#00ff41", fontname="Courier New", fontsize=10]

        # 1. LE ROOT
        ROOT [label="ROOT (Allah)\n[Source of Command]", color="#FFD700", fontcolor="black", shape=doubleoctagon]

        # 2. LES ADMINS
        subgraph cluster_admins {
            label = "ZONE: FREE WILL (S-Y-T-R)"
            style=dashed; color="#00ff41"; fontcolor="#00ff41"
            KHALIFA [label="USER (Insan)\n[Read/Write Access]", color="#00ff41", fontcolor="black"]
            ANGELS [label="AGENTS (Mala'ika)\n[Admin Executors]", color="#00ff41", fontcolor="black"]
        }

        # 3. LES AUTOMATES
        subgraph cluster_automata {
            label = "ZONE: AUTOMATION (S-KH-R)"
            style=dashed; color="#ff4b4b"; fontcolor="#ff4b4b"
            SUN [label="DAEMON: SUN\n[Solar_Service]", color="#262730", fontcolor="white"]
            MOON [label="DAEMON: MOON\n[Time_Service]", color="#262730", fontcolor="white"]
            PHYSICS [label="KERNEL: PHYSICS\n[Laws/Gravity]", color="#262730", fontcolor="white"]
        }

        # RELATIONS
        ROOT -> KHALIFA [label="Grant_Access"]
        ROOT -> ANGELS [label="Command (A-M-R)"]
        ROOT -> SUN [label="Hard_Code (Q-D-R)"]
        
        KHALIFA -> SUN [label="Utilise (S-KH-R)", style=dotted]
        ANGELS -> PHYSICS [label="Maintain (D-B-R)"]
    }
    """
    
    st.graphviz_chart(governance_graph)
    
    st.markdown("---")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.error("**S-KH-R (سخر)**\n\nTask Automation.\n(Ex: Soleil, Lune, Animaux)")
    with c2:
        st.success("**S-Y-T-R (سيطر)**\n\nRoot Admin.\n(Ex: Autorité de Contrôle)")
    with c3:
        st.warning("**KH-L-F (خلف)**\n\nSystem Operator.\n(Ex: Humain/Successeur)")


import streamlit as st
from data.repository import LexiconRepository

# --- CONFIGURATION ---
st.set_page_config(
    page_title="Veritas Terminal v10.1",
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
</style>
""", unsafe_allow_html=True)

# --- INITIALISATION DU REPOSITORY ---
@st.cache_resource
def get_repo():
    return LexiconRepository()

repo = get_repo()

# --- HEADER ---
st.title("VERITAS TERMINAL v10.1")
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

mode = st.sidebar.radio("PROTOCOL", ["ROOT SCANNER", "VERSE DECOMPILER", "MATRIX VIEW"])

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
            # Appel au repository pour chaque racine
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


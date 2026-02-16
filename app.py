import streamlit as st
import graphviz
import pandas as pd
from data.repository import LexiconRepository
from core.config import config
from export.manager import ExportManager

# --- FONCTION CALLBACK ---
def update_search(new_term):
    st.session_state["search_input"] = new_term

# --- CONFIGURATION ---
st.set_page_config(
    page_title=f"{config['app']['name']} {config['app']['version']}",
    page_icon="💠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- STYLE CSS (MIDNIGHT BLUE & LIGHT SIDEBAR - GOLDEN MASTER) ---
st.markdown("""
<style>
    /* 1. FOND PRINCIPAL: BLEU NUIT PROFOND */
    .stApp {
        background-color: #0d1b2a; 
    }
    
    /* 2. SIDEBAR: GRIS CLAIR & TEXTE NOIR */
    section[data-testid="stSidebar"] {
        background-color: #f0f2f6;
        border-right: 1px solid #d0d0d0;
    }
    
    /* Force le texte noir dans la sidebar */
    section[data-testid="stSidebar"] h1, 
    section[data-testid="stSidebar"] span, 
    section[data-testid="stSidebar"] label, 
    section[data-testid="stSidebar"] p,
    section[data-testid="stSidebar"] div {
        color: #000000 !important;
    }
    
    /* 3. INPUTS (Fond sombre pour contraste sur le bleu) */
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
    
    /* 4. TEXTES PRINCIPAUX (Blanc cassé) */
    h1, h2, h3 {color: #e0e1dd !important;}
    p, li {color: #b0c4de !important;}
    
    /* 5. CARDS */
    .metric-card {
        background-color: #162544; /* Bleu légèrement plus clair */
        border: 1px solid #415a77;
        padding: 20px;
        border-radius: 8px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.3);
        margin-bottom: 15px;
    }
    .root-title {font-size: 28px; font-weight: bold; color: #00ff41;}
    .arabic-display {font-family: 'Amiri', serif; font-size: 38px; color: #ffd700; direction: rtl; float: right;}
    .logic-func {
        font-family: 'Consolas', monospace; 
        color: #ff9e9e; 
        font-weight: bold; 
        background: #3a0ca3; 
        padding: 4px 8px; 
        border-radius: 4px;
        font-size: 14px;
    }

    /* 6. CONSOLE LOG */
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
</style>
""", unsafe_allow_html=True)

# --- REPO ---
@st.cache_resource
def get_repo():
    return LexiconRepository(filepath=config['database']['path'])

repo = get_repo()
exporter = ExportManager()

# --- SIDEBAR (LIGHT THEME) ---
with st.sidebar:
    st.title("VERITAS KERNEL")
    st.caption(f"v{config['app']['version']} | SYSTEM ONLINE")
    st.markdown("---")
    
    # CHARGEMENT DES DONNÉES EN DATAFRAME
    raw_data = repo.get_all_roots()
    df_roots = pd.DataFrame(raw_data)
    count = len(df_roots) if not df_roots.empty else 0

    col1, col2 = st.columns(2)
    with col1:
        st.metric("ROOTS", count)
    with col2:
        st.metric("STATUS", "OK")
    
    st.markdown("---")
    
    # NAVIGATION
    mode = st.radio("NAVIGATION", 
        ["LOGIC SEQUENCER", "ROOT SCANNER", "GOVERNANCE MAP", "MATRIX VIEW"])
    
    st.markdown("---")
    st.info("Authorized Access Only")

# --- MODE 1: LOGIC SEQUENCER ---
if mode == "LOGIC SEQUENCER":
    st.title("⛓️ LOGIC SEQUENCER")
    
    c1, c2 = st.columns([4, 1])
    with c1:
        input_seq = st.text_input("ROOT SEQUENCE", "B-S-M A-L-H R-H-M-N R-H-Y-M")
    with c2:
        st.write("")
        st.write("")
        run_btn = st.button("▶ EXECUTE", type="primary", use_container_width=True)

    if run_btn or input_seq:
        roots = input_seq.split()
        
        # GRAPHVIZ AVEC FOND BLEU NUIT
        graph = graphviz.Digraph()
        graph.attr(rankdir='LR', bgcolor='#0d1b2a')
        graph.attr('node', shape='box', style='filled', fontname='Segoe UI', margin='0.2')
        graph.attr('edge', fontname='Consolas', fontsize='10', color='#888')

        console_logs = []
        previous_node = None
        cols = st.columns(len(roots))
        
        for i, r in enumerate(roots):
            data = repo.find_root(r)
            if data:
                clean_func = data['logic_function'].split("//")[0].strip()
                arabic = data['arabic']
                binary = data.get('binary_pair', 'N/A')
                
                # NOEUD ACTIF
                node_id = f"node_{i}"
                label = f"<{r}<BR/><FONT POINT-SIZE='10'>{clean_func}</FONT>>"
                graph.node(node_id, label=label, color='#00ff41', fillcolor='#1b263b', fontcolor='#e0e1dd', penwidth='1.5')
                
                # NOEUD REJETÉ (FANTOME)
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
                
                console_logs.append(f"[LOADED] {r} >> {clean_func}")
                
                with cols[i]:
                    st.markdown(f"""
                    <div class='metric-card' style='border-top: 3px solid #00ff41;'>
                        <div style='color:#e0e1dd; font-weight:bold; font-size:18px;'>{r}</div>
                        <div style='color:#ffd700; font-size:24px; direction:rtl;'>{arabic}</div>
                        <div style='font-size:12px; color:#b0c4de; margin-top:5px;'>{clean_func}</div>
                        <div style='font-size:11px; color:#ff9e9e; margin-top:8px; border-top:1px solid #415a77; padding-top:4px;'>
                            ⛔ REJECTS: {binary}
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
            else:
                graph.node(f"node_{i}", label=f"{r} (?)", color='#ff0000')
                with cols[i]:
                    st.error(f"{r} ?")
        
        st.graphviz_chart(graph, use_container_width=True)
        st.markdown("### 📟 CONSOLE")
        log_html = "<div class='console-log'>" + "<br>".join([f"<div>> {l}</div>" for l in console_logs]) + "</div>"
        st.markdown(log_html, unsafe_allow_html=True)

# --- MODE 2: ROOT SCANNER ---
elif mode == "ROOT SCANNER":
    st.title("🔍 ROOT SCANNER")
    
    # LISTE DÉROULANTE VIA PANDAS
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
                st.markdown(f"""
                <div class='metric-card'>
                    <div class='arabic-display'>{result['arabic']}</div>
                    <div class='root-title'>{result['root']}</div>
                    <div style='margin-top:15px;'>
                        <span class='logic-func'>{result['logic_function']}</span>
                    </div>
                </div>
                """, unsafe_allow_html=True)
                
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

# --- MODE 3: GOVERNANCE MAP (RESTORED WITH ADMIN/DAEMON) ---
elif mode == "GOVERNANCE MAP":
    st.title("👑 GOVERNANCE TOPOLOGY")
    
    gov_code = """
    digraph G {
        bgcolor="#0d1b2a"
        rankdir=TB
        node [style=filled, fontname="Segoe UI", shape=box, fontcolor=white, color="#444", fillcolor="#1b263b"]
        edge [color="#888", fontname="Consolas", fontsize=10, fontcolor="#b0c4de"]
        
        ROOT [label="ROOT (ALLAH)\n[Source of Command]", color="#FFD700", fontcolor="black", fillcolor="#FFD700", shape=doubleoctagon, height=1.2]
        
        # ZONE: ADMINS (LIBRE ARBITRE)
        subgraph cluster_admins {
            label = "ZONE: SYS_ADMINS (R-K-')"; style=dashed; color="#00ff41"; fontcolor="#00ff41"
            
            KHALIFA [label="INSAN (User)\n<TYPE: ADMIN>\n[Voluntary Sync]", color="#00ff41", fontcolor="black", fillcolor="#00ff41"]
            DJINN [label="JINN (Hidden)\n<TYPE: ADMIN>\n[Rational Force]", color="#00aa00", fontcolor="black", fillcolor="#00aa00"]
        }
        
        # ZONE: DAEMONS (AUTOMATES)
        subgraph cluster_automata {
            label = "ZONE: SYSTEM_DAEMONS (S-J-D)"; style=dashed; color="#ff4b4b"; fontcolor="#ff4b4b"
            
            ANGELS [label="MALA'IKA\n<TYPE: DAEMON>\n[Exec Function]", color="#aaaaaa", fontcolor="black", fillcolor="#aaaaaa"]
            NATURE [label="PHYSICS ENGINE\n<TYPE: KERNEL>\n[Hard-Coded Laws]", color="#222", fontcolor="white", fillcolor="#222"]
        }
        
        ROOT -> KHALIFA [label="AMANAH (Sudo Access)"]
        ROOT -> ANGELS [label="A-M-R (Command)"]
        ROOT -> NATURE [label="Q-D-R (Measure)"]
        
        KHALIFA -> NATURE [style=dotted]
        ANGELS -> NATURE [style=dotted]
    }
    """
    st.graphviz_chart(gov_code, use_container_width=True)

# --- MODE 4: MATRIX VIEW ---
elif mode == "MATRIX VIEW":
    st.title("🌐 KERNEL MATRIX")
    st.dataframe(df_roots, use_container_width=True, height=700)
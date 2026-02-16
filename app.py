
import streamlit as st
import json
import re
import os

# --- CONFIGURATION ---
st.set_page_config(
    page_title='Veritas Terminal v10.0',
    page_icon='👁️',
    layout='wide',
    initial_sidebar_state='expanded'
)

# --- STYLE CYBERPUNK ---
st.markdown("""
<style>
    .reportview-container {background: #0e1117;}
    .main {background-color: #0e1117; color: #00ff41; font-family: 'Courier New', monospace;}
    h1, h2, h3 {color: #e0e0e0;}
    .stTextInput > div > div > input {background-color: #262730; color: #ffffff;}
    .metric-card {
        background-color: #1e1e1e; border: 1px solid #333;
        padding: 15px; border-radius: 5px; margin-bottom: 10px;
    }
    .arabic-text {
        font-family: 'Amiri', serif; font-size: 32px; color: #ffcc00;
        direction: rtl; text-align: right; margin-top: -10px;
    }
    .root-title {font-size: 24px; font-weight: bold; color: #00ff41;}
    .logic-func {font-family: monospace; color: #ff4b4b; font-weight: bold;}
</style>
""", unsafe_allow_html=True)

# --- CHARGEMENT DU LEXICON ---
@st.cache_data
def load_lexicon():
    if not os.path.exists('LEXICON.json'):
        return [], {}, {}
    try:
        with open('LEXICON.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        latin_index = {}
        arabic_index = {}
        for item in data['universal_functions']:
            root = item.get('root', '').strip().upper()
            arabic = item.get('arabic', '').strip()
            if root: latin_index[root] = item
            if arabic and arabic != '---': arabic_index[arabic] = item
        return data['universal_functions'], latin_index, arabic_index
    except:
        return [], {}, {}

functions_list, latin_index, arabic_index = load_lexicon()

# --- INTERFACE ---
st.title('VERITAS TERMINAL v10.0')
st.markdown('*Non-Torted Computational Theology Interface*')
st.markdown('---')

st.sidebar.title('SYSTEM STATUS')
st.sidebar.text(f"Streamlit v{st.__version__}")
if functions_list:
    st.sidebar.success(f'KERNEL LOADED: {len(functions_list)} NODES')
else:
    st.sidebar.error('KERNEL ERROR: LEXICON NOT FOUND')

mode = st.sidebar.radio('PROTOCOL', ['ROOT SCANNER', 'VERSE DECOMPILER', 'MATRIX VIEW'])

if mode == 'ROOT SCANNER':
    st.subheader('🔍 SINGLE ROOT ANALYSIS')
    query = st.text_input('INPUT SIGNAL (Latin ex: K-T-B or Arabic ex: كتب)', '').strip()
    
    if query:
        result = None
        if re.search(r'[a-zA-Z]', query):
            q_upper = query.upper()
            result = latin_index.get(q_upper)
            if not result: # Auto-fix
                q_fix = q_upper.replace('S', 'S.').replace('D', 'D.').replace('T', 'T.').replace('H', 'H.').replace('Z', 'Z.')
                result = latin_index.get(q_fix)
        else:
            result = arabic_index.get(query)
            
        if result:
            st.markdown('---')
            c1, c2 = st.columns([1, 2])
            with c1:
                st.markdown(f'<div class="metric-card"><div class="root-title">{result["root"]}</div><div class="arabic-text">{result["arabic"]}</div></div>', unsafe_allow_html=True)
            with c2:
                st.markdown(f'**LOGIC FUNCTION:** <span class="logic-func">{result["logic_function"]}</span>', unsafe_allow_html=True)
                st.info(f'{result["description"]}')
        else:
            st.warning(f'SIGNAL {query} NOT FOUND IN KERNEL.')

elif mode == 'VERSE DECOMPILER':
    st.subheader('💻 SEQUENCE DECOMPILER')
    input_seq = st.text_area('ROOT SEQUENCE (Space separated)', 'B-S-M A-L-H R-H-M R-H-M')
    if st.button('EXECUTE'):
        roots = input_seq.split()
        st.markdown('---')
        for r in roots:
            r = r.strip().upper()
            data = latin_index.get(r)
            if not data:
                 r_fix = r.replace('S', 'S.').replace('D', 'D.').replace('T', 'T.').replace('H', 'H.').replace('Z', 'Z.')
                 data = latin_index.get(r_fix)
            if data:
                with st.expander(f'[{r}]  {data["arabic"]}  ::  {data["logic_function"]}'):
                    st.write(f'**Function:** {data["description"]}')
            else:
                st.error(f'[{r}] :: UNKNOWN SIGNAL')

elif mode == 'MATRIX VIEW':
    st.subheader('🌐 GLOBAL DATA')
    st.dataframe(functions_list)

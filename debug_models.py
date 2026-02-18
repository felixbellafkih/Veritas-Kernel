import google.generativeai as genai
import streamlit as st

st.title("🕵️ SCANNER DE MODÈLES GOOGLE")

try:
    api_key = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=api_key)
    
    st.write("Connexion établie. Scan en cours...")
    
    models = []
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            models.append(m.name)
            
    st.success(f"{len(models)} modèles trouvés !")
    st.json(models)
    
except Exception as e:
    st.error(f"Erreur : {e}")
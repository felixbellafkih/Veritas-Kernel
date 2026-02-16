# Ce script réécrit la section GOVERNANCE MAP de app.py pour inclure les Djinns
import os

file_path = 'app.py'

new_graph_code = """    governance_graph = \"\"\"
    digraph G {
        bgcolor="#0e1117"
        rankdir=TB
        node [style=filled, fontname="Courier New", shape=box]
        edge [color="#00ff41", fontname="Courier New", fontsize=10]

        # 1. LE ROOT
        ROOT [label="ROOT (Allah)\\n[Source of Command]", color="#FFD700", fontcolor="black", shape=doubleoctagon]

        # 2. LES ADMINS (Dual Boot System)
        subgraph cluster_admins {
            label = "ZONE: ADMIN / FREE WILL (S-Y-T.-R)"
            style=dashed; color="#00ff41"; fontcolor="#00ff41"
            
            # Deux types d'utilisateurs avec Write Access
            KHALIFA [label="USER: INSAN\\n[Visible Layer]", color="#00ff41", fontcolor="black"]
            DJINN [label="USER: JINN\\n[Hidden Layer]", color="#00aa00", fontcolor="black"]
        }

        # 3. LES AUTOMATES & AGENTS
        subgraph cluster_automata {
            label = "ZONE: AUTOMATION & SERVICE (S-KH-R)"
            style=dashed; color="#ff4b4b"; fontcolor="#ff4b4b"
            
            ANGELS [label="AGENT: ANGELS\\n[System Executors]", color="#aaaaaa", fontcolor="black"]
            SUN [label="DAEMON: SUN\\n[Energy Service]", color="#262730", fontcolor="white"]
        }

        # RELATIONS
        ROOT -> KHALIFA [label="Grant_Access"]
        ROOT -> DJINN [label="Grant_Access"]
        ROOT -> ANGELS [label="Command (A-M-R)"]
        ROOT -> SUN [label="Hard_Code (Q-D-R)"]
        
        # Interactions
        KHALIFA -> SUN [label="Utilise", style=dotted]
        ANGELS -> SUN [label="Gère", style=dotted]
    }
    \"\"\""""

# Lecture du fichier
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Remplacement chirurgical (on cherche le bloc graphviz et on le remplace)
# Note: C'est une méthode brute mais efficace pour ce contexte.
import re
pattern = r'governance_graph = """(.*?)"""'
new_content = re.sub(pattern, new_graph_code, content, flags=re.DOTALL)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("✅ APP.PY MIS À JOUR : Djinns intégrés dans la Zone Admin.")

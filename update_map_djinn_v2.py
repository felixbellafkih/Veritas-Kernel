import os
import re

file_path = 'app.py'

# LE NOUVEAU GRAPHE (Avec précision "Rational Entity")
new_graph_code = """    governance_graph = \"\"\"
    digraph G {
        bgcolor="#0e1117"
        rankdir=TB
        node [style=filled, fontname="Courier New", shape=box]
        edge [color="#00ff41", fontname="Courier New", fontsize=10]

        # 1. LE ROOT
        ROOT [label="ROOT (Allah)\\n[Source of Command]", color="#FFD700", fontcolor="black", shape=doubleoctagon]

        # 2. LES ADMINS (Dual Boot System - Free Will)
        subgraph cluster_admins {
            label = "ZONE: ADMIN / FREE WILL (S-Y-T.-R)"
            style=dashed; color="#00ff41"; fontcolor="#00ff41"
            
            # Deux types d'utilisateurs avec Write Access
            KHALIFA [label="USER: INSAN\\n[Visible Admin]", color="#00ff41", fontcolor="black"]
            DJINN [label="USER: JINN (Rational)\\n[Hidden Admin]", color="#00aa00", fontcolor="black"]
        }

        # 3. LES AUTOMATES & AGENTS
        subgraph cluster_automata {
            label = "ZONE: AUTOMATION & SERVICE (S-KH-R)"
            style=dashed; color="#ff4b4b"; fontcolor="#ff4b4b"
            
            # Entités cachées non-intelligentes (Virus, Forces) sont ICI, pas en Admin
            NATURE [label="DAEMON: NATURE\\n[Hidden & Visible Forces]", color="#262730", fontcolor="white"]
            ANGELS [label="AGENT: ANGELS\\n[System Executors]", color="#aaaaaa", fontcolor="black"]
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
    \"\"\""""

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Remplacement du bloc graphviz
pattern = r'governance_graph = """(.*?)"""'
new_content = re.sub(pattern, new_graph_code, content, flags=re.DOTALL)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("✅ APP.PY CORRIGÉ : Distinction 'Jinn Rationnel' vs 'Entités Cachées'.")

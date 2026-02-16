import json
import os
from datetime import datetime

# --- 1. CORRECTION DE LA BASE DE DONNÉES (LEXICON.json) ---
json_path = 'LEXICON.json'
with open(json_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

changed = False
for item in data['universal_functions']:
    # On cherche l'ancienne clé erronée
    if item['root'] == 'S-Y-T-R': 
        item['root'] = 'S-Y-T.-R'  # La correction (T emphatique)
        print(f"✅ BASE DE DONNÉES CORRIGÉE: S-Y-T-R -> S-Y-T.-R")
        changed = True
        break

if changed:
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
else:
    print("ℹ️ INFO: La base semblait déjà à jour (S-Y-T.-R déjà présent).")

# --- 2. RE-GÉNÉRATION DU CHAPITRE (Avec la nouvelle clé) ---
from data.repository import LexiconRepository
repo = LexiconRepository() # Rechargement des données fraîches

# On cible explicitement la nouvelle orthographe
roots = ['S-KH-R', 'S-Y-T.-R', 'Q-D-R', 'A-M-R']
root_data = {}

for r in roots:
    found = repo.find_root(r)
    if found:
        root_data[r] = found
    else:
        # Filet de sécurité si la correction DB a échoué
        root_data[r] = {'root': r, 'arabic': '?', 'logic_function': 'ERROR', 'description': 'DATA MISSING'}

target_file = "thesis/chapter_04_governance.md"

content = f"""# CHAPITRE 04 : PROTOCOLE DE GOUVERNANCE (ADMIN VS DAEMON)
**Date de génération :** {datetime.now().strftime("%Y-%m-%d %H:%M")}
**Version Kernel :** v10.5.1 (Hotfix S-Y-T.-R)
**Statut :** DRAFT ZERO (Corrected)

---

## 1. INTRODUCTION : L'ERREUR D'ADRESSAGE
L'idolâtrie (Shirk) n'est pas une émotion, c'est une erreur technique de routage. Elle consiste à adresser une requête (`D-'-W`) à une entité qui ne possède pas les droits d'écriture (Write Access) sur le système.

---

## 2. L'AUTOMATE (DAEMON) : S-KH-R
> **Racine :** {root_data['S-KH-R']['root']} ({root_data['S-KH-R']['arabic']})
> **Fonction Logique :** `{root_data['S-KH-R']['logic_function']}`

**Analyse Systémique :**
{root_data['S-KH-R']['description']}

---

## 3. LE CODE SOURCE : Q-D-R
> **Racine :** {root_data['Q-D-R']['root']} ({root_data['Q-D-R']['arabic']})
> **Fonction Logique :** `{root_data['Q-D-R']['logic_function']}`

**Analyse Systémique :**
{root_data['Q-D-R']['description']}

---

## 4. L'ADMINISTRATEUR (USER) : {root_data['S-Y-T.-R']['root']} & KH-L-F
> **Racine :** {root_data['S-Y-T.-R']['root']} ({root_data['S-Y-T.-R']['arabic']})
> **Fonction Logique :** `{root_data['S-Y-T.-R']['logic_function']}`

**Analyse Systémique :**
{root_data['S-Y-T.-R']['description']}

*Note : L'Homme (Khalifa) possède les clés d'Admin. Il peut choisir de contourner les lois morales, ce qui prouve son accès "Write".*

---

## 5. LA COMMANDE EXÉCUTIVE : A-M-R
> **Racine :** {root_data['A-M-R']['root']} ({root_data['A-M-R']['arabic']})
> **Fonction Logique :** `{root_data['A-M-R']['logic_function']}`

**Analyse Systémique :**
{root_data['A-M-R']['description']}

---

## CONCLUSION DU MODULE
Le système Veritas démontre que la soumission à un processus automatisé (`S-KH-R`) est une régression pour une entité dotée de droits d'administration (`{root_data['S-Y-T.-R']['root']}`).
L'Homme doit commander à la Nature, et se soumettre uniquement au Root (`Allah`).
"""

with open(target_file, "w", encoding="utf-8") as f:
    f.write(content)

print(f"✅ SUCCÈS : Chapitre 04 régénéré. Racine corrigée en S-Y-T.-R")

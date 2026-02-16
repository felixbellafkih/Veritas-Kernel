from data.repository import LexiconRepository
from datetime import datetime

# 1. INITIALISATION
repo = LexiconRepository()
target_file = "thesis/chapter_04_governance.md"

# 2. RÉCUPÉRATION DES DONNÉES CLÉS
roots = ['S-KH-R', 'S-Y-T-R', 'Q-D-R', 'A-M-R']
data = {r: repo.find_root(r) for r in roots}

# 3. STRUCTURE DU CONTENU (PLAN VERITAS)
content = f"""# CHAPITRE 04 : PROTOCOLE DE GOUVERNANCE (ADMIN VS DAEMON)
**Date de génération :** {datetime.now().strftime("%Y-%m-%d")}
**Version Kernel :** v10.5.0
**Statut :** DRAFT ZERO (System Generated)

---

## 1. INTRODUCTION : L'ERREUR D'ADRESSAGE
L'idolâtrie (Shirk) n'est pas une émotion, c'est une erreur technique de routage. Elle consiste à adresser une requête (`D-'-W`) à une entité qui ne possède pas les droits d'écriture (Write Access) sur le système.
Pour comprendre cela, il faut distinguer l'Administrateur de l'Automate.

---

## 2. L'AUTOMATE (DAEMON) : S-KH-R
> **Racine :** {data['S-KH-R']['root']} ({data['S-KH-R']['arabic']})
> **Fonction Logique :** `{data['S-KH-R']['logic_function']}`

**Analyse Systémique :**
{data['S-KH-R']['description']}

*Note : Le Soleil et la Lune sont des services exécutables. Ils n'ont pas de libre arbitre.*

---

## 3. LE CODE SOURCE : Q-D-R
> **Racine :** {data['Q-D-R']['root']} ({data['Q-D-R']['arabic']})
> **Fonction Logique :** `{data['Q-D-R']['logic_function']}`

**Analyse Systémique :**
{data['Q-D-R']['description']}

*Note : C'est la limite hard-codée de chaque objet. L'automate suit son Qadar sans déviation.*

---

## 4. L'ADMINISTRATEUR (USER) : S-Y-T-R & KH-L-F
> **Racine :** {data['S-Y-T-R']['root']} ({data['S-Y-T-R']['arabic']})
> **Fonction Logique :** `{data['S-Y-T-R']['logic_function']}`

**Analyse Systémique :**
{data['S-Y-T-R']['description']}

*Note : L'Homme (Khalifa) possède les clés d'Admin. Il peut choisir de contourner les lois morales, ce qui prouve son accès "Write".*

---

## 5. LA COMMANDE EXÉCUTIVE : A-M-R
> **Racine :** {data['A-M-R']['root']} ({data['A-M-R']['arabic']})
> **Fonction Logique :** `{data['A-M-R']['logic_function']}`

**Analyse Systémique :**
{data['A-M-R']['description']}

---

## CONCLUSION DU MODULE
Le système Veritas démontre que la soumission à un processus automatisé (`S-KH-R`) est une régression pour un entité dotée de droits d'administration (`S-Y-T-R`).
L'Homme doit commander à la Nature, et se soumettre uniquement au Root (`Allah`).

*Fin du rapport.*
"""

# 4. ÉCRITURE DU FICHIER
with open(target_file, "w", encoding="utf-8") as f:
    f.write(content)

print(f"✅ SUCCÈS : Chapitre 04 généré dans '{target_file}'")

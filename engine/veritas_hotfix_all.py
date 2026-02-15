import json
import os

# --- DICTIONNAIRE DE PURIFICATION (NO-TORSION STANDARD) ---
corrections = {
    "K-F-R": {
        "logic_function": "Data_Masking",
        "description": "Action technique de couvrir (Covering) ou masquer une donnée source validée pour la rendre inaccessible (Refus d'Input)."
    },
    "Z-L-M": {
        "logic_function": "System_Imbalance",
        "description": "Erreur d'adressage consistant à placer un objet ou une variable dans un emplacement qui n'est pas le sien (Décalage)."
    },
    "F-S-Q": {
        "logic_function": "Protocol_Breach",
        "description": "Sortie illégale d'un nœud hors de son périmètre de sécurité ou de sa structure définie (Désynchronisation)."
    },
    "J-R-M": {
        "logic_function": "Corrupt_Process",
        "description": "Processus qui coupe activement les connexions valides pour isoler des clusters de données (Coupure)."
    },
    "T-W-B": {
        "logic_function": "System_Restore",
        "description": "Retour d'un processus à un point de restauration antérieur stable après une erreur (Retour)."
    },
    "G-F-R": {
        "logic_function": "Error_Shielding",
        "description": "Mécanisme de protection (Casque) empêchant une erreur interne de provoquer un crash système global (Couverture)."
    },
    "S-L-H": {
        "logic_function": "Network_Sync",
        "description": "Maintien actif de la connexion et de la synchronisation entre le nœud client et le Serveur Central (Lien)."
    },
    "J-H-D": {
        "logic_function": "Max_Compute_Load",
        "description": "Allocation maximale des ressources processeur pour résoudre une tâche complexe ou une résistance (Effort)."
    },
    "Q-T-L": {
        "logic_function": "Process_Termination",
        "description": "Arrêt forcé et définitif d'un processus hostile ou buggé (Neutralisation)."
    },
    "A-M-N": {
        "logic_function": "Security_Mode",
        "description": "État de sécurité active où le système est protégé contre les pertes de données et la peur (Sûreté)."
    },
    "R-H-M": {
        "logic_function": "System_Matrix",
        "description": "L'environnement englobant qui génère, nourrit et contient tous les objets du système (Matrice)."
    },
    "K-DH-B": {
        "logic_function": "False_Positive",
        "description": "Génération d'un signal de sortie contradictoire avec la réalité factuelle du système (Déni/Bruit)."
    }
}

FILE_PATH = 'LEXICON.json'

def apply_deep_clean():
    if not os.path.exists(FILE_PATH):
        print(f"❌ ERREUR : {FILE_PATH} introuvable.")
        return

    try:
        with open(FILE_PATH, 'r', encoding='utf-8') as f:
            data = json.load(f)

        # Détection intelligente de la liste
        target_list = []
        if isinstance(data, list):
            target_list = data
        elif isinstance(data, dict):
            # Priorité aux clés connues
            for key in ['universal_functions', 'roots', 'entries']:
                if key in data and isinstance(data[key], list):
                    target_list = data[key]
                    break
        
        if not target_list:
            print("❌ ERREUR : Structure JSON inconnue. Impossible de trouver la liste.")
            return

        # Application des correctifs
        updated_count = 0
        
        print("--- DÉBUT DE LA PURIFICATION ---")
        for item in target_list:
            root_txt = item.get('root', '')
            # Pour chaque correctif, on vérifie si la racine correspond
            for code, new_def in corrections.items():
                # On check si le Code (ex: K-F-R) est dans la racine ET si la déf est différente
                if code in root_txt:
                    current_logic = item.get('logic_function', '')
                    
                    # On applique si ce n'est pas déjà corrigé
                    if current_logic != new_def['logic_function']:
                        print(f"🔄 CORRECTION {code} : {current_logic} -> {new_def['logic_function']}")
                        item['logic_function'] = new_def['logic_function']
                        item['description'] = new_def['description']
                        updated_count += 1

        if updated_count > 0:
            with open(FILE_PATH, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=4, ensure_ascii=False)
            print(f"\n✅ SUCCÈS : {updated_count} racines ont été réalignées sur le standard Veritas.")
        else:
            print("\n✅ SYSTÈME DÉJÀ PUR : Aucune modification nécessaire.")

    except Exception as e:
        print(f"❌ ERREUR CRITIQUE : {e}")

if __name__ == "__main__":
    apply_deep_clean()
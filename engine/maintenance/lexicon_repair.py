import json
import re
import shutil
from datetime import datetime

def repair_lexicon():
    print("🔧 DÉMARRAGE DU PROTOCOLE DE RÉPARATION VERITAS...")
    
    # 1. Sauvegarde de sécurité (Backup)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_file = f"LEXICON_BACKUP_{timestamp}.json"
    shutil.copy('LEXICON.json', backup_file)
    print(f"💾 Backup créé : {backup_file}")

    try:
        with open('LEXICON.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
    except Exception as e:
        print(f"❌ Erreur critique : {e}")
        return

    original_count = len(data['universal_functions'])
    cleaned_map = {}
    
    # Regex pour capturer le Code Latin (Majuscules, tirets, points, apostrophes)
    # Ex: Capture "H-W-A" dans "ه-و (H-W-A/Huwa)"
    code_pattern = re.compile(r"([A-Z\.\-\']{2,})")

    # 2. Itération et Nettoyage
    for item in data['universal_functions']:
        raw_root = item['root']
        
        # Filtrage des déchets
        if "RES-" in raw_root or "X-X-X" in raw_root or "F-60" in raw_root:
            continue

        # Extraction du Code Unique
        match = code_pattern.search(raw_root)
        if match:
            key = match.group(1).strip()
        else:
            # Si pas de code latin trouvé, on garde tel quel (rare)
            key = raw_root.strip()

        # 3. Correction des anomalies spécifiques (Hard Fixes)
        if key == "Z-Y-G": key = "Z-Y-GH"      # Standardisation Ghayn
        if key == "T-G-Y": key = "T.-GH-Y"     # Standardisation Emphatique
        if key == "S-W-A": key = "S-W-'"       # Standardisation Hamza

        # 4. Mise à jour de l'entrée
        # On ne garde que le Code Pur dans le champ 'root' pour uniformiser
        item['root'] = key
        
        # 5. Déduplication (Last Writer Wins)
        # Si la clé existe déjà, on l'écrase. 
        # Comme le Patch est à la fin du fichier, c'est la version corrigée qui gagne.
        cleaned_map[key] = item

    # Reconstruction de la liste
    new_list = list(cleaned_map.values())
    
    # Tri alphabétique pour la propreté
    new_list.sort(key=lambda x: x['root'])

    # Mise à jour des métadonnées
    data['universal_functions'] = new_list
    data['version'] = "22.1.0-Clean-Standardized"
    data['status'] = "Optimized"

    # Écriture du fichier propre
    with open('LEXICON.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    print("-" * 40)
    print(f"📉 Entrées Avant : {original_count}")
    print(f"📈 Entrées Après : {len(new_list)}")
    print(f"🗑  Doublons/Junk supprimés : {original_count - len(new_list)}")
    print("-" * 40)
    print("✅ LEXICON.json est maintenant PROPRE et STANDARDISÉ.")

if __name__ == "__main__":
    repair_lexicon()

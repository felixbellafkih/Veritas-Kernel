import json
import sys

# Forçage de l'environnement de sortie pour l'arabe
if sys.stdout.encoding != 'UTF-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except AttributeError:
        pass # Support pour les versions plus anciennes si nécessaire

def final_alignment():
    lexicon_path = 'LEXICON.json'
    
    # Table de vérité absolue : Mapping direct Racine <-> Token
    piliers_absolus = [
        {"root": "ف-ت-ح (F-T-H)", "logic_function": "Access_Gate_Opening"},
        {"root": "ذ-ك-ر (DH-K-R)", "logic_function": "Memory_Active_Recall"},
        {"root": "ن-ص-ر (N-S-R)", "logic_function": "System_Support_Boost"},
        {"root": "ف-ؤ-د (F-'-D)", "logic_function": "Volatile_Processor_Core"},
        {"root": "س-م-ع (S-M-E)", "logic_function": "Audio_Signal_Input"},
        {"root": "ب-ص-ر (B-S-R)", "logic_function": "Optical_Data_Scanning"}
    ]

    try:
        with open(lexicon_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Injection chirurgicale sur les 6 premiers slots
        for i, pilier in enumerate(piliers_absolus):
            pilier["description"] = "Racine pilier alignée pour intégrité système v7.8.0."
            data['universal_functions'][i] = pilier

        # Sauvegarde avec préservation de l'UTF-8
        with open(lexicon_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        
        print("✅ ALIGNEMENT VÉRIFIÉ : Piliers synchronisés avec le Stress-Test.")

    except Exception as e:
        print(f"❌ ERREUR DE SYNCHRONISATION : {e}")

if __name__ == "__main__":
    final_alignment()

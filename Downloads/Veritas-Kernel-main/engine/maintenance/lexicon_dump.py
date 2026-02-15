import json
import sys

def audit_lexicon():
    try:
        with open('LEXICON.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        print("❌ ERREUR : LEXICON.json introuvable.")
        return
    except json.JSONDecodeError:
        print("❌ ERREUR : Le fichier LEXICON.json est corrompu (Erreur de syntaxe).")
        return

    roots = [item['root'] for item in data['universal_functions']]
    unique_roots = set(roots)
    
    print(f"📊 STATISTIQUES DU NOYAU")
    print(f"========================")
    print(f"Version Actuelle : {data.get('version', 'Unknown')}")
    print(f"Total Entrées    : {len(roots)}")
    print(f"Racines Uniques  : {len(unique_roots)}")
    
    # Détection des doublons
    if len(roots) != len(unique_roots):
        print(f"🚨 ALERTE : {len(roots) - len(unique_roots)} DOUBLONS DÉTECTÉS !")
        from collections import Counter
        dupes = [item for item, count in Counter(roots).items() if count > 1]
        print(f"⚠️ Racines en conflit : {', '.join(dupes)}")
    else:
        print(f"✅ INTÉGRITÉ : 100% (Aucun doublon)")

    print(f"\n📂 CONTENU DU LEXICON (DUMP)")
    print(f"============================")
    # Affichage propre pour l'analyse
    print(json.dumps(data, indent=4, ensure_ascii=False))

if __name__ == "__main__":
    audit_lexicon()

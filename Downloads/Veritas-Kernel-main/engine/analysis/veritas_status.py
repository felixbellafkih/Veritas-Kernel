import json
import os
from datetime import datetime

def audit_system():
    lexicon_path = 'LEXICON.json'
    log_dir = 'logs'
    
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    try:
        with open(lexicon_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        functions = data.get('universal_functions', [])
        total_slots = len(functions)
        
        # Filtrage : On sépare les racines réelles des slots réservés
        real_roots = [f for f in functions if "RESERVED" not in f['logic_function'] and "GENERIC" not in f['logic_function']]
        reserved_slots = total_slots - len(real_roots)
        
        # Calculs mathématiques
        density = (len(real_roots) / 1800) * 100
        coverage = (len(real_roots) / total_slots) * 100 if total_slots > 0 else 0
        
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        report = f"""
--- RAPPORT D'ÉTAT VERITAS KERNEL ---
DATE : {timestamp}
VERSION : {data.get('version', 'Unknown')}
-------------------------------------
CAPACITÉ D'ADRESSAGE : {total_slots}/1800
DENSITÉ DU SIGNAL    : {len(real_roots)} racines réelles
SLOTS EN ATTENTE     : {reserved_slots}
-------------------------------------
SCORE DE DENSITÉ (TOTAL)  : {density:.2f}%
SCORE DE COMPLÉTION (SLOT): {coverage:.2f}%
ÉTAT : {'OPÉRATIONNEL' if len(real_roots) > 500 else 'CRITIQUE'}
-------------------------------------
"""
        # Affichage
        print(report)
        
        # Enregistrement
        log_file = os.path.join(log_dir, 'audit_log.txt')
        with open(log_file, 'a', encoding='utf-8') as l:
            l.write(report)
            
        print(f"✅ Audit enregistré dans : {log_file}")

    except Exception as e:
        print(f"❌ ERREUR D'AUDIT : {e}")

if __name__ == "__main__":
    audit_system()

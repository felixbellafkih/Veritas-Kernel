import json

def expand_v10():
    # Lot 10.0.0 : Security, Rival Systems (Andad) & Noise Filtering
    security_batch = [
        {"root": "ن-ف-ق (N-F-Q/Nifaq)", "logic_function": "Internal_Inconsistency_Leak", "description": "Divergence entre l'en-tête du signal et son contenu réel (Double flux)."},
        {"root": "ض-د (D-D-D/Didd)", "logic_function": "Antagonist_Logic_Conflict", "description": "Force de résistance s'opposant directement à l'exécution d'une instruction Root."},
        {"root": "ن-د (N-D-D/Andad)", "logic_function": "Rival_System_Instance", "description": "Création d'un système de référence alternatif tentant de détourner le flux source."},
        {"root": "ف-ت-ن (F-T-N/Fitna)", "logic_function": "System_Stress_Testing", "description": "Injection contrôlée de bruit pour tester la résilience et la pureté d'un nœud."},
        {"root": "ل-غ-و (L-G-W/Laghw)", "logic_function": "High_Entropy_Noise", "description": "Données vides de sens logique n'apportant aucun gain au système."},
        {"root": "ز-خ-ر-ف (Z-KH-R-F/Zukhruf)", "logic_function": "Obfuscated_Malware_Interface", "description": "Embellissement de surface masquant une corruption structurelle profonde."},
        {"root": "ك-ي-د (K-Y-D/Kayd)", "logic_function": "Adversarial_Algorithm", "description": "Séquence logique cachée visant à subvertir le processus principal."},
        {"root": "م-ك-ر (M-K-R/Makr)", "logic_function": "Counter_Intelligence_Protocol", "description": "Action du système pour piéger et isoler un processus malveillant."},
        {"root": "خ-د-ع (KH-D-A/Khada'a)", "logic_function": "Virtual_Environment_Deception", "description": "Simulation d'un état système pour tromper un agent hostile."},
        {"root": "ص-د (S-D-D/Sadda)", "logic_function": "Execution_Blocking_Barrier", "description": "Interruption physique empêchant le signal d'atteindre sa destination."},
        {"root": "ه-ج-ر (H-G-R/Hajr)", "logic_function": "Node_Quarantine_Isolation", "description": "Mise à l'écart définitive d'un segment corrompu pour protéger le Kernel."},
        {"root": "ر-ج-م (R-G-M/Rajm)", "logic_function": "Active_Threat_Purge", "description": "Expulsion violente d'un agent malveillant hors de l'espace d'adressage (Stoning)."},
        {"root": "خ-ذ-ل (KH-DH-L/Khadhala)", "logic_function": "Support_Drop_Failure", "description": "Rupture de la liaison de secours lors d'une exécution critique."},
        {"root": "غ-ر-ر (G-R-R/Ghurur)", "logic_function": "Buffer_Overflow_Illusion", "description": "Fausse perception de la capacité système menant à un crash par excès de confiance."}
    ]

    try:
        with open('LEXICON.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        lex = {item['root']: item for item in data['universal_functions']}
        added = 0
        merged = 0

        for entry in security_batch:
            root_key = entry['root']
            if root_key in lex:
                # Mise à jour des fonctions de sécurité si déjà existantes
                lex[root_key]['logic_function'] = f"{lex[root_key]['logic_function']}_{entry['logic_function']}"
                merged += 1
            else:
                lex[root_key] = entry
                added += 1
        
        data['universal_functions'] = list(lex.values())
        data['version'] = "10.0.0-Security"
        
        with open('LEXICON.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        
        print(f"✅ EXPANSION DE SÉCURITÉ RÉUSSIE")
        print(f"📈 Nouvelles racines : {added}")
        print(f"🔄 Racines fusionnées : {merged}")
        print(f"💎 Total : {len(data['universal_functions'])}/1800")
        
    except Exception as e:
        print(f"❌ ERREUR : {e}")

if __name__ == "__main__":
    expand_v10()

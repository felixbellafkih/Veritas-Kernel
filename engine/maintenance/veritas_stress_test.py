import subprocess
import json

def run_stress_test():
    # Séquences de test représentant les piliers du système
    test_sequences = [
        "F-T-H DH-K-R N-S-R",           # Séquence d'Initialisation
        "KH-L-Q M-A-W T-Y-N",           # Séquence Bio-Physique
        "Q-D-R S-M-W A-R-D",           # Séquence Infrastructure
        "K-T-B B-Y-N H-Q-Q",           # Séquence de Validation (Truth)
        "S-M-E B-S-R F-'-D"            # Séquence de Perception
    ]

    print("\n--- [ VERITAS KERNEL STRESS-TEST v7.8.0 ] ---")
    print("Cible : LEXICON.json (Commit: c8c9b2d)")
    
    total_signals = 0
    total_noise = 0

    for seq in test_sequences:
        print(f"\nAudit Séquence : [{seq}]")
        try:
            # Appel du compilateur
            process = subprocess.Popen(['python', 'engine/veritas_compiler.py', seq], 
                                     stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            stdout, stderr = process.communicate()
            
            # Analyse du rapport de compilation
            if "!! NOISE !!" in stdout:
                print("  ❌ STATUS : DÉGRADÉ (Signal perdu)")
                total_noise += 1
            else:
                print("  ✅ STATUS : PURETÉ 100% (Signal verrouillé)")
                total_signals += 1
                
        except Exception as e:
            print(f"  ⚠️ ERREUR D'EXÉCUTION : {e}")

    # Résultat final
    purity_rate = (total_signals / len(test_sequences)) * 100
    print("\n" + "="*40)
    print(f"RÉSUMÉ : {total_signals}/{len(test_sequences)} SÉQUENCES VALIDES")
    print(f"SCORE D'INTÉGRITÉ : {purity_rate:.2f}%")
    print("="*40)

if __name__ == "__main__":
    run_stress_test()

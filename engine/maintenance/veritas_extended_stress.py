import subprocess
import sys

def run_extended_stress():
    # Matrice de tests par domaines fonctionnels
    test_suite = {
        "INITIALISATION": ["F-T-H DH-K-R N-S-R", "Q-W-L K-W-N J-E-L"],
        "INFRASTRUCTURE": ["S-M-W A-R-D Q-D-R", "B-N-Y R-F-E S-M-K"],
        "BIO-PHYSIQUE": ["KH-L-Q M-A-W T-Y-N", "H-Y-Y M-W-T B-E-TH"],
        "LOGIQUE/VÉRITÉ": ["K-T-B B-Y-N H-Q-Q", "C-D-Q H-K-M F-S-L"],
        "PERCEPTION": ["S-M-E B-S-R F-'-D", "A-L-M F-K-R N-Z-R"]
    }

    print(f"\n--- [ VERITAS EXTENDED STRESS-TEST v7.8.0 ] ---")
    
    total_tests = 0
    passed_tests = 0

    for domain, sequences in test_suite.items():
        print(f"\n[ DOMAINE : {domain} ]")
        for seq in sequences:
            total_tests += 1
            process = subprocess.Popen(['python', 'engine/veritas_compiler.py', seq], 
                                     stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            stdout, _ = process.communicate()
            
            if "!! NOISE !!" in stdout:
                print(f"  ❌ {seq:<20} | SIGNAL DÉGRADÉ")
            else:
                print(f"  ✅ {seq:<20} | PURETÉ 100%")
                passed_tests += 1

    accuracy = (passed_tests / total_tests) * 100
    print("\n" + "="*50)
    print(f"RÉSULTAT GLOBAL : {passed_tests}/{total_tests} SÉQUENCES VALIDES")
    print(f"DENSITÉ DE COHÉRENCE : {accuracy:.2f}%")
    print("="*50)

if __name__ == "__main__":
    run_extended_stress()

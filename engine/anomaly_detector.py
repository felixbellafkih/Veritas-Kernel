import json, math, os

class VeritasAnomalyDetector:
    def __init__(self, lexicon_path='LEXICON.json'):
        with open(lexicon_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        self.lexicon = {item['root'].split('(')[1].split(')')[0].strip(): item for item in data['universal_functions'] if '(' in item['root']}
        
        # Attributs réservés à l'Autorité Racine (ROOT_ONLY)
        self.root_attributes = ["R-A-W-F", "R-H.-M"]

    def analyze_segment(self, chapter_id, verses_data):
        print(f"\n🔍 AUDIT DE SÉCURITÉ : SOURATE {chapter_id}")
        print("-" * 50)
        
        for v_id, roots in verses_data.items():
            anomaly_score = 0
            flags = []

            # 1. Détection de "Privilege Escalation" (Typage)
            # Si un verset contient un Envoyé (R-S-L) + des attributs ROOT
            if "R-S-L" in roots:
                conflicts = [r for r in roots if r in self.root_attributes]
                if conflicts:
                    anomaly_score += 50
                    flags.append(f"TYPE_MISMATCH: Privilege Escalation {conflicts} on NODE(R-S-L)")

            # 2. Détection de "Sequence Break" (Post-Closure)
            if chapter_id == 9 and v_id in [128, 129]:
                anomaly_score += 40
                flags.append("SEQUENCE_BREAK: Post-Closure Appendice detected")

            # Verdict
            status = "✅ STABLE" if anomaly_score < 30 else "🚨 ANOMALY DETECTED"
            print(f"Verset {v_id:3} | Score: {anomaly_score:2} | {status}")
            for f in flags: print(f"  └─ {f}")

if __name__ == "__main__":
    detector = VeritasAnomalyDetector()
    # Simulation des données de la fin de la Sourate 9
    # 127: Signal de fermeture (Cœurs détournés)
    # 128: L'injection (Attributs ROOT sur Messager)
    # 129: Le secours (Détournement du flux)
    test_data = {
        127: ["KH-T-M", "Q-L-B", "F-Q-H"],
        128: ["J-A-'", "R-S-L", "'-Z-Z", "H.-R-S.", "A-M-N", "R-A-W-F", "R-H.-M"],
        129: ["T-W-L", "H.-S-B", "T-W-K-L", "R-B-B", "'-R-SH"]
    }
    detector.analyze_segment(9, test_data)

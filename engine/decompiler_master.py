import os
from translation_engine import VeritasTranslator

def run_mass_decompilation(input_file, output_file):
    if not os.path.exists(input_file):
        print(f"❌ Erreur : {input_file} introuvable.")
        return

    translator = VeritasTranslator()
    
    print(f"⚙️ DÉCOMPILATION EN COURS : {input_file} -> {output_file}")
    
    with open(input_file, 'r', encoding='utf-8') as f_in, \
         open(output_file, 'w', encoding='utf-8') as f_out:
        
        for line in f_in:
            if line.strip():
                decompiled = translator.translate(line.strip())
                f_out.write(f"SOURCE   : {line.strip()}\n")
                f_out.write(f"FUNCTION : {decompiled}\n")
                f_out.write("-" * 50 + "\n")
                
    print(f"✅ OPÉRATION TERMINÉE. Fichier généré : {output_file}")

if __name__ == "__main__":
    run_mass_decompilation('source_baqara.txt', 'DECOMPILED_QURAN.txt')

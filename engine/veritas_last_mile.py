import os

def last_mile_sync():
    print("⚡ SYNCHRONISATION FINALE DU SPECTRE H. (Last Mile)...")
    
    bench_path = 'engine/veritas_benchmark.py'
    if not os.path.exists(bench_path):
        print("❌ Fichier benchmark introuvable.")
        return

    with open(bench_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remplacement des appels "Soft" par les appels "Heavy" requis par le Lexique
    fixes = {
        '"H-M-D"': '"H.-M-D"',
        '"H-S-B"': '"H.-S-B"'
    }
    
    updated_content = content
    for old, new in fixes.items():
        updated_content = updated_content.replace(old, new)

    with open(bench_path, 'w', encoding='utf-8') as f:
        f.write(updated_content)
    
    print("✅ Benchmark aligné : H.-M-D et H.-S-B verrouillés.")

if __name__ == "__main__":
    last_mile_sync()

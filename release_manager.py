import subprocess
import sys

def run_command(command):
    try:
        result = subprocess.check_output(command, shell=True, text=True).strip()
        return result
    except subprocess.CalledProcessError as e:
        return None

def get_latest_tag():
    # Récupère le dernier tag (ex: v10.0)
    tag = run_command("git describe --tags --abbrev=0")
    if not tag:
        return "v0.0.0" # Valeur par défaut si aucun tag
    return tag

def increment_version(version, upgrade_type):
    # Enlève le 'v' initial
    clean_ver = version.lstrip('v')
    parts = list(map(int, clean_ver.split('.')))
    
    # Assure format X.Y.Z (ajoute des 0 si nécessaire)
    while len(parts) < 3:
        parts.append(0)
        
    major, minor, patch = parts

    if upgrade_type == "major":
        major += 1
        minor = 0
        patch = 0
    elif upgrade_type == "minor":
        minor += 1
        patch = 0
    elif upgrade_type == "patch":
        patch += 1
        
    return f"v{major}.{minor}.{patch}"

def main():
    print("--- 🚀 VERITAS RELEASE MANAGER ---")
    
    # 1. État actuel
    current_tag = get_latest_tag()
    print(f"🔹 VERSION ACTUELLE : {current_tag}")
    
    # 2. Choix de l'incrémentation
    print("\nQuel type de mise à jour ?")
    print(" [1] PATCH (v10.0.0 -> v10.0.1) : Correction de bugs, petites retouches.")
    print(" [2] MINOR (v10.0.0 -> v10.1.0) : Nouvelles fonctions (ex: Ajout de S-KH-R).")
    print(" [3] MAJOR (v10.0.0 -> v11.0.0) : Changement d'architecture critique.")
    
    choice = input("\n👉 Choix (1-3) : ")
    
    if choice == "1":
        new_tag = increment_version(current_tag, "patch")
        msg_type = "Patch"
    elif choice == "2":
        new_tag = increment_version(current_tag, "minor")
        msg_type = "Feature Update"
    elif choice == "3":
        new_tag = increment_version(current_tag, "major")
        msg_type = "Architecture Upgrade"
    else:
        print("❌ Annulation.")
        sys.exit()

    # 3. Message de Release
    custom_msg = input(f"📝 Description optionnelle pour {new_tag} (Entrée pour défaut) : ")
    if not custom_msg:
        final_msg = f"Veritas Kernel {new_tag} - {msg_type}"
    else:
        final_msg = f"Veritas Kernel {new_tag} - {custom_msg}"

    print(f"\n🚀 Lancement de la procédure pour : {new_tag}")
    print(f"   Message : '{final_msg}'")
    
    confirm = input("Confirm ? (y/n) : ")
    if confirm.lower() != 'y':
        sys.exit()

    # 4. Exécution Git
    print("\n[1/2] Création du Tag local...")
    subprocess.call(f'git tag -a {new_tag} -m "{final_msg}"', shell=True)
    
    print("[2/2] Synchronisation avec le Cloud...")
    subprocess.call(f'git push origin {new_tag}', shell=True)
    
    print(f"\n✅ SUCCÈS : {new_tag} EST EN LIGNE.")

if __name__ == "__main__":
    main()

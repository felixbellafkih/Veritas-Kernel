import json
import os

target_file = 'LEXICON.json'

print("⏳ VERITAS : Initialisation du Patch Lexical...")

try:
    with open(target_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
except FileNotFoundError:
    print(f"❌ ERREUR : Le fichier {target_file} est introuvable.")
    exit(1)

# --- MATRICE DES DÉFINITIONS (MAQASID AL-HURUF) ---
corrections = {
    "A.-J-M": {"arabic": "عجم", "logic_function": "OBFUSCATED_SYNTAX // UNPARSABLE", "description": "Code manquant de clarté syntaxique, impossible à compiler sans dictionnaire d'interprétation.", "binary_pair": "A.-R-B"},
    "A.-Q-B": {"arabic": "عقب", "logic_function": "BACKEND_TRACE // CONSEQUENCE", "description": "Séquence de traçage des processus exécutés. Résultat résiduel persistant dans les logs.", "binary_pair": "A.-F-W"},
    "A.-Z-L": {"arabic": "عزل", "logic_function": "PROCESS_ISOLATION // QUARANTINE", "description": "Détachement d'une instance du cluster principal empêchant toute interaction externe.", "binary_pair": "J-A.-L"},
    "A-S.-L": {"arabic": "أصل", "logic_function": "ROOT_DIRECTORY // BASE", "description": "Le répertoire fondamental ou point d'ancrage absolu d'où dérivent toutes les branches.", "binary_pair": "F-R-A."},
    "B-L-D": {"arabic": "بلد", "logic_function": "STATIC_STORAGE_NODE", "description": "Environnement sédentaire structuré accueillant les processus et données persistantes.", "binary_pair": "F-A-D"},
    "B-N-W": {"arabic": "بنو", "logic_function": "CHILD_INSTANCE // DERIVED_NODE", "description": "Instance héritant des propriétés de la matrice parente, opérant dans son sous-répertoire.", "binary_pair": "A-B-W"},
    "F-K-K": {"arabic": "فك", "logic_function": "UNLOCK_PROTOCOL // DECOUPLE", "description": "Dissociation d'éléments liés. Libération d'un processus ou décryptage d'une archive.", "binary_pair": "A-S-R"},
    "F-R-D": {"arabic": "فرد", "logic_function": "UNPAIRED_THREAD // SINGULARITY", "description": "Exécution d'un thread isolé, sans redondance ni couplage avec un processus miroir.", "binary_pair": "Z-W-J"},
    "GH-SH-SH": {"arabic": "غش", "logic_function": "SPOOFED_PAYLOAD // FRAUD", "description": "Injection de données corrompues masquées sous une signature valide pour tromper les filtres.", "binary_pair": "N-S.-H."},
    "H-D-M": {"arabic": "هدم", "logic_function": "SYSTEM_DEMOLITION // DEALLOCATE", "description": "Destruction volontaire et structurée d'une architecture pour libérer les ressources matérielles.", "binary_pair": "B-N-Y"},
    "H.-Q-R": {"arabic": "حقر", "logic_function": "MINIFIED_PROCESS // LOW_PRIORITY", "description": "Rétrogradation d'un processus à un statut mineur, lui allouant le minimum de bande passante.", "binary_pair": "A.-Z.-M"},
    "H.-S.-D": {"arabic": "حصد", "logic_function": "DATA_HARVESTING // COLLECT", "description": "Récupération massive des résultats (outputs) générés par les processus arrivés à maturité.", "binary_pair": "Z-R-A."},
    "I-KH-L-S.": {"arabic": "خلص", "logic_function": "DEDICATED_PURE_THREAD", "description": "Exécution exclusive d'un processus sans aucune interférence tierce ni tâche de fond.", "binary_pair": "N-F-Q"},
    "J-L-Y": {"arabic": "جلي", "logic_function": "HIGH_RES_RENDER // CLEAR", "description": "Affichage explicite et net d'une donnée sur l'interface, sans couche d'obfuscation.", "binary_pair": "T.-M-S"},
    "J-W-F": {"arabic": "جوف", "logic_function": "HOLLOW_CORE // EMPTY_CAVITY", "description": "Zone de mémoire interne vide et non allouée. Espace creux au sein d'une structure.", "binary_pair": "S.-M-D"},
    "J-DH-B": {"arabic": "جذب", "logic_function": "MAGNETIC_PULL // FETCH_FORCE", "description": "Force d'attraction interne forçant le rapatriement d'une donnée distante vers le noyau.", "binary_pair": "D-F-A."},
    "K-M-N": {"arabic": "كمن", "logic_function": "STEALTH_DAEMON // HIDE", "description": "Processus actif mais masqué dans les couches profondes, indétectable par l'interface standard.", "binary_pair": "B-R-Z"},
    "K-TH-R": {"arabic": "كثر", "logic_function": "HIGH_VOLUME_DATA // MASS", "description": "Augmentation massive de la quantité d'instances ou du volume de données, saturant les bus.", "binary_pair": "Q-L-L"},
    "KH-DH-L": {"arabic": "خذل", "logic_function": "SUPPORT_WITHDRAWAL // ABANDON", "description": "Retrait brusque des ressources de soutien en cours d'exécution d'un processus critique.", "binary_pair": "A.-Z-R"},
    "KH-L-A.": {"arabic": "خلع", "logic_function": "HARDWARE_DETACH // UNPLUG", "description": "Détachement physique ou retrait brut d'une surcouche d'interface (Déshabillage logiciel).", "binary_pair": "L-B-S"},
    "KH-R-B": {"arabic": "خرب", "logic_function": "ARCHITECTURE_CORRUPTION // RUIN", "description": "Dégradation structurelle profonde rendant le segment système ou le nœud inutilisable.", "binary_pair": "A.-M-R"},
    "N-B-A.": {"arabic": "نبع", "logic_function": "ORIGIN_STREAM // EMITTER", "description": "Point d'émergence d'un flux continu de données nouvelles depuis les couches profondes.", "binary_pair": "KH-B-R"},
    "N-K-R": {"arabic": "نكر", "logic_function": "UNRECOGNIZED_SIGNATURE", "description": "Paquet ou instance rejeté car dépourvu de signature d'authentification valide.", "binary_pair": "A.-R-F"},
    "R-GH-B": {"arabic": "رغب", "logic_function": "PULL_REQUEST_DESIRE", "description": "Tendance dynamique d'un nœud à solliciter activement une ressource ou à pointer vers une cible.", "binary_pair": "R-H-B"},
    "R-Y-Y": {"arabic": "روي", "logic_function": "HYDRATION_SATURATION // QUENCH", "description": "Remplissage complet et optimal des tampons système par un flux vital (données ou énergie).", "binary_pair": "Z.-M-A"},
    "S-F-L": {"arabic": "سفل", "logic_function": "LOW_LEVEL_STACK // BOTTOM", "description": "Couche inférieure de l'architecture. Processus bas-niveau traitant les opérations matérielles.", "binary_pair": "A.-L-Y"},
    "S.-H.-W": {"arabic": "صحو", "logic_function": "SYSTEM_AWAKE // CLEAR_STATE", "description": "Restauration de la clarté opératoire et de la vigilance du processeur après une latence.", "binary_pair": "S-K-R"},
    "S.-W-B": {"arabic": "صوب", "logic_function": "TARGET_HIT // ACCURATE", "description": "Exécution parfaitement alignée sur les coordonnées prévues. Résultat vrai et exact.", "binary_pair": "KH-T.-A"},
    "SH-B-A.": {"arabic": "شبع", "logic_function": "RESOURCE_SATURATION // FULL", "description": "État d'une partition ayant atteint sa capacité maximale d'absorption de ressources.", "binary_pair": "S-GH-B"},
    "SH-Y-N": {"arabic": "شين", "logic_function": "VISUAL_CORRUPTION // GLITCH", "description": "Dégradation de l'interface ou anomalie visuelle rendant l'exécution inesthétique.", "binary_pair": "Z-Y-N"},
    "T-R-K": {"arabic": "ترك", "logic_function": "PACKET_DROP // ABANDON", "description": "Libération volontaire d'une ressource ou arrêt de suivi d'un paquet. Le système l'ignore.", "binary_pair": "A-KH-DH"},
    "T.-W-Y": {"arabic": "طوي", "logic_function": "DATA_ROLLUP // COMPRESSION", "description": "Contraction et repliement de l'espace de stockage pour archiver le runtime.", "binary_pair": "N-SH-R"},
    "W-Q-F": {"arabic": "وقف", "logic_function": "PROCESS_HALT // BREAKPOINT", "description": "Mise en pause temporelle d'une exécution pour figer un état.", "binary_pair": "J-R-Y"},
    "W-T-R": {"arabic": "وتر", "logic_function": "ODD_PARITY // SINGULAR", "description": "Séquence asymétrique ou impair ne disposant pas de binôme de validation.", "binary_pair": "SH-F-A."},
    "Z-W-L": {"arabic": "زول", "logic_function": "EPHEMERAL_STATE // TIMEOUT", "description": "Processus dont l'existence est programmée pour disparaître avec le temps. Fin de cycle inévitable.", "binary_pair": "S-R-M"},
    "Z-Y-D": {"arabic": "زيد", "logic_function": "RESOURCE_INCREMENT // SCALE_UP", "description": "Ajout de variables ou allocation supplémentaire de capacité à un nœud existant.", "binary_pair": "N-Q-S."}
}

# --- DICTIONNAIRE DE PURGE DES ABERRATIONS ---
typos_to_fix = {
    'A.-DH-DH-B': 'A.-DH-B',
    'T-GH-Y': 'T.-GH-Y',
    'J-Z-B': 'J-DH-B',
    'G-Y-B': 'GH-Y-B'
}

# 1. Correction chirurgicale des pointeurs (binary_pairs)
for entry in data['universal_functions']:
    bp = entry.get('binary_pair')
    if bp in typos_to_fix:
        entry['binary_pair'] = typos_to_fix[bp]

# 2. Reconstruction de la matrice sans le bruit
filtered_data = []
for entry in data['universal_functions']:
    root = entry['root']
    
    # Destruction des aberrations phonétiques générées par erreur
    if root in typos_to_fix:
        if root in ['A.-DH-DH-B', 'T-GH-Y', 'G-Y-B']:
            continue # Destruction totale (elles existent déjà sous leur vraie forme)
        elif root == 'J-Z-B':
            # Remplacement par l'orthographe exacte pour injection Maqasid
            entry['root'] = 'J-DH-B'
            root = 'J-DH-B'

    # Remplacement des Auto-Generated par les données pures
    if root in corrections and "AUTO_GENERATED" in entry.get('logic_function', ''):
        entry['arabic'] = corrections[root]['arabic']
        entry['logic_function'] = corrections[root]['logic_function']
        entry['description'] = corrections[root]['description']
        entry['binary_pair'] = corrections[root]['binary_pair']

    filtered_data.append(entry)

data['universal_functions'] = filtered_data

# 3. Écriture avec indentation stricte (1 ligne par clé/valeur)
with open(target_file, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print("✅ VERITAS : Patch appliqué avec succès. Base de données purgée et complétée.")

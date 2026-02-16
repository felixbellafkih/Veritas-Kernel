import json
import os

file_path = 'LEXICON.json'

# --- PAYLOAD : 30 RACINES (15 PAIRES) ---
batch = [
    # 1. TRUTH (Stable) vs VOID (Null)
    {
        "root": "H.-Q-Q", "arabic": "حقق",
        "logic_function": "SYSTEM_TRUTH // IMMUTABLE_FACT",
        "description": "Donnée stable et vérifiée. Le Haqq est ce qui est fixé dans le système et ne peut être écrasé.",
        "binary_pair": "B-T.-L"
    },
    {
        "root": "B-T.-L", "arabic": "بطل",
        "logic_function": "NULL_POINTER // VOID_DATA",
        "description": "Donnée invalide ou processus qui tourne à vide. Le Batil est voué à être effacé par le Garbage Collector.",
        "binary_pair": "H.-Q-Q"
    },

    # 2. PATIENCE (Buffering) vs HASTE (Premature)
    {
        "root": "S.-B-R", "arabic": "صبر",
        "logic_function": "BUFFERING // PROCESS_CONSTANCY",
        "description": "Maintien de la charge de travail (Workload) sans crash. Capacité à garder un état stable sous pression.",
        "binary_pair": "'-J-L"
    },
    {
        "root": "'-J-L", "arabic": "عجل",
        "logic_function": "PREMATURE_EXECUTION // CLOCK_SPEED_ERROR",
        "description": "Tentative d'exécuter une commande avant que les dépendances ne soient prêtes. Cause d'erreurs d'initialisation.",
        "binary_pair": "S.-B-R"
    },

    # 3. ACKNOWLEDGMENT (Output) vs DENIAL (Masking)
    {
        "root": "SH-K-R", "arabic": "شكر",
        "logic_function": "OUTPUT_ACKNOWLEDGMENT // DATA_RETURN",
        "description": "Signal de retour confirmant la bonne réception des ressources (Rizq). Le système renvoie une valeur positive.",
        "binary_pair": "K-F-R"
    },
    # Note: K-F-R est déjà dans le système, le script fera un Update.

    # 4. UNITY (Single Core) vs ASSOCIATION (Parallel Conflict)
    {
        "root": "W-H.-D", "arabic": "وحد",
        "logic_function": "SINGLE_SOURCE // ROOT_ACCESS",
        "description": "Unicité de la source de commande. Il n'y a qu'un seul Kernel.",
        "binary_pair": "SH-R-K"
    },
    {
        "root": "SH-R-K", "arabic": "شرك",
        "logic_function": "PARALLEL_PROCESSING // CONFLICTING_ADMINS",
        "description": "Tentative d'attribuer des droits Root à une entité qui n'est pas le système. Crée des conflits de version.",
        "binary_pair": "W-H.-D"
    },

    # 5. INPUT (Login) vs OUTPUT (Logout)
    {
        "root": "D-KH-L", "arabic": "دخل",
        "logic_function": "SYSTEM_ENTRY // LOGIN_EVENT",
        "description": "Action d'entrer dans un sous-système ou un environnement.",
        "binary_pair": "KH-R-J"
    },
    {
        "root": "KH-R-J", "arabic": "خرج",
        "logic_function": "SYSTEM_EXIT // LOGOUT_EVENT",
        "description": "Action de sortir d'un état ou d'une boucle.",
        "binary_pair": "D-KH-L"
    },

    # 6. ELEVATION (Upgrade) vs PLACEMENT/DROP (Downgrade)
    {
        "root": "R-F-'", "arabic": "رفع",
        "logic_function": "PRIORITY_ELEVATION // UPGRADE",
        "description": "Augmentation du niveau de privilège ou de la position dans la stack.",
        "binary_pair": "W-D.-'"
    },
    {
        "root": "W-D.-'", "arabic": "وضع",
        "logic_function": "PRIORITY_DROP // PLACEMENT",
        "description": "Déposer ou abaisser une variable. Assignation à un niveau inférieur.",
        "binary_pair": "R-F-'"
    },

    # 7. COLLECTION (Array) vs SEPARATION (Split)
    {
        "root": "J-M-'", "arabic": "جمع",
        "logic_function": "DATA_AGGREGATION // ARRAY_BUILD",
        "description": "Regroupement de données dispersées en une structure unique.",
        "binary_pair": "F-R-Q"
    },
    {
        "root": "F-R-Q", "arabic": "فرق",
        "logic_function": "DATA_SPLITTING // PARSING",
        "description": "Distinction entre deux blocs de données. Le Furqan est le 'Parser' qui sépare le Vrai du Faux.",
        "binary_pair": "J-M-'"
    },

    # 8. EXPANSION (Bandwidth Up) vs CONSTRICTION (Throttling)
    {
        "root": "B-S-T.", "arabic": "بسط",
        "logic_function": "BANDWIDTH_EXPANSION // SCALING_OUT",
        "description": "Extension des capacités ou des ressources allouées.",
        "binary_pair": "Q-B-D."
    },
    {
        "root": "Q-B-D.", "arabic": "قبض",
        "logic_function": "THROTTLING // COMPRESSION",
        "description": "Restriction du flux ou saisie d'un objet. Réduction de l'espace alloué.",
        "binary_pair": "B-S-T."
    },

    # 9. MANIFEST (Frontend) vs HIDDEN (Backend)
    {
        "root": "Z.-H-R", "arabic": "ظهر",
        "logic_function": "FRONTEND_RENDER // GUI_VISIBLE",
        "description": "Ce qui est affiché à l'écran. La couche visible de l'interface.",
        "binary_pair": "B-T.-N"
    },
    {
        "root": "B-T.-N", "arabic": "بطن",
        "logic_function": "BACKEND_CODE // HIDDEN_LAYER",
        "description": "Le code source profond, non visible par l'utilisateur final, mais qui contient la logique interne.",
        "binary_pair": "Z.-H-R"
    },

    # 10. HEARING (Audio Input) vs DEAFNESS (Input Block)
    {
        "root": "S-M-'", "arabic": "سمع",
        "logic_function": "AUDIO_INPUT // LISTENING_PORT",
        "description": "Réception active de signaux sonores/informatifs.",
        "binary_pair": "S.-M-M"
    },
    {
        "root": "S.-M-M", "arabic": "صمم",
        "logic_function": "INPUT_BLOCKING // FIREWALL_DROP",
        "description": "Incapacité technique à recevoir le flux audio. Port fermé.",
        "binary_pair": "S-M-'"
    },

    # 11. SIGHT (Video Input) vs BLINDNESS (No Signal)
    {
        "root": "B-S.-R", "arabic": "بصر",
        "logic_function": "VIDEO_INPUT // PATTERN_RECOGNITION",
        "description": "Traitement visuel des données. Capacité à analyser l'environnement (Insight).",
        "binary_pair": "'-M-Y"
    },
    {
        "root": "'-M-Y", "arabic": "عمي",
        "logic_function": "NO_VIDEO_SIGNAL // BLIND_MODE",
        "description": "Absence de flux visuel. Le système ne peut pas lire les données graphiques.",
        "binary_pair": "B-S.-R"
    },

    # 12. SPEECH (Output Protocol) vs SILENCE (Mute)
    {
        "root": "N-T.-Q", "arabic": "نطق",
        "logic_function": "SPEECH_PROTOCOL // TEXT_TO_SPEECH",
        "description": "Génération de langage articulé compréhensible.",
        "binary_pair": "S.-M-T"
    },
    {
        "root": "S.-M-T", "arabic": "صمت",
        "logic_function": "MUTE_STATE // NO_OUTPUT",
        "description": "Silence complet. Aucun paquet de données vocales envoyé.",
        "binary_pair": "N-T.-Q"
    },

    # 13. FIRST (Boot) vs LAST (Term)
    {
        "root": "A-W-L", "arabic": "أول",
        "logic_function": "INIT_PROCESS // BOOTLOADER",
        "description": "Le premier processus lancé. L'origine de la séquence.",
        "binary_pair": "A-KH-R"
    },
    {
        "root": "A-KH-R", "arabic": "أخر",
        "logic_function": "TERM_PROCESS // END_OF_FILE",
        "description": "La fin de la séquence. L'état final.",
        "binary_pair": "A-W-L"
    },
    
    # 14. PUBLIC (Global) vs PRIVATE (Sudo)
    {
        "root": "'-M-M", "arabic": "عمم",
        "logic_function": "GLOBAL_SCOPE // PUBLIC_ACCESS",
        "description": "S'applique à toutes les instances. Général.",
        "binary_pair": "KH-S.-S."
    },
    {
        "root": "KH-S.-S.", "arabic": "خصص",
        "logic_function": "PRIVATE_SCOPE // SUDO_ACCESS",
        "description": "Spécifique à une instance ou un utilisateur privilégié. Spécial.",
        "binary_pair": "'-M-M"
    },

    # 15. PERMISSION (Allow) vs PROHIBITION (Deny)
    {
        "root": "H.-L-L", "arabic": "حلل",
        "logic_function": "ACCESS_GRANTED // DECRYPTED",
        "description": "Déverrouillage d'un nœud. Autorisation d'accès. (Aussi : délier/analyser).",
        "binary_pair": "H.-R-M"
    },
    {
        "root": "H.-R-M", "arabic": "حرم",
        "logic_function": "ACCESS_DENIED // RESTRICTED_AREA",
        "description": "Zone sacrée ou interdite. Accès restreint par l'Admin.",
        "binary_pair": "H.-L-L"
    }
]

# LOGIQUE D'INJECTION
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

lookup = {item['root']: index for index, item in enumerate(data['universal_functions'])}

print(f"🔄 INJECTION BATCH #19 (PHONOLOGY CHECKED)...")
count_upd = 0
count_new = 0

for item in batch:
    root = item['root']
    if root in lookup:
        idx = lookup[root]
        data['universal_functions'][idx].update(item)
        count_upd += 1
        print(f"   [UPDATE] {root} <-> {item['binary_pair']}")
    else:
        data['universal_functions'].append(item)
        count_new += 1
        print(f"   [NEW]    {root} <-> {item['binary_pair']}")

with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=4, ensure_ascii=False)

print(f"✅ TERMINÉ. New: {count_new} | Updated: {count_upd}")

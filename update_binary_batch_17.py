import json

file_path = 'LEXICON.json'

# BATCH #17: MORAL BINARIES
batch = [
    # PAIR 1: SECURITY vs COVERING
    {
        "root": "A-M-N",
        "arabic": "أمن",
        "logic_function": "SECURE_STATE // TRUSTED_ACCESS",
        "description": "État de sécurité et de confiance. Le système est stable, les ports sont ouverts aux données vérifiées. La foi (Iman) est une 'Sécurisation' de la relation avec le Root.",
        "binary_pair": "K-F-R"
    },
    {
        "root": "K-F-R",
        "arabic": "كفر",
        "logic_function": "DATA_MASKING // ACCESS_DENIAL",
        "description": "Acte de couvrir ou d'enterrer une donnée. Ce n'est pas une simple incrédulité, c'est une action technique de dissimulation de la vérité (Haqq). L'utilisateur 'Kafir' masque sciemment le signal du Root.",
        "binary_pair": "A-M-N"
    },

    # PAIR 2: GUIDANCE vs SIGNAL LOSS (Phonology: D. for Dad)
    {
        "root": "H-D-Y",
        "arabic": "هدي",
        "logic_function": "TARGET_ACQUISITION // SIGNAL_LOCK",
        "description": "Acquisition de la cible. Le système reçoit les données de télémétrie et s'oriente vers la destination prévue. C'est un guidage actif.",
        "binary_pair": "D.-L-L"
    },
    {
        "root": "D.-L-L",
        "arabic": "ضلل",
        "logic_function": "SIGNAL_LOSS // NAVIGATION_ERROR",
        "description": "Perte du signal de guidage. L'entité n'a plus de repère et erre dans le système sans coordonnée valide. Ce n'est pas nécessairement une rébellion, mais une incapacité à trouver le chemin (Null Path).",
        "binary_pair": "H-D-Y"
    },

    # PAIR 3: OPTIMALITY vs ENTROPY
    {
        "root": "KH-Y-R",
        "arabic": "خير",
        "logic_function": "OPTIMAL_SELECTION // SYSTEM_BENEFIT",
        "description": "Ce qui est choisi pour son efficacité supérieure. Le bien est défini par sa capacité à produire un résultat optimal pour le système.",
        "binary_pair": "SH-R-R"
    },
    {
        "root": "SH-R-R",
        "arabic": "شرر",
        "logic_function": "SYSTEM_ENTROPY // HARMFUL_NOISE",
        "description": "Dispersion, étincelles, instabilité. Le mal est ce qui génère du bruit, de la chaleur inutile et de la désorganisation dans le code.",
        "binary_pair": "KH-Y-R"
    }
]

# CHARGEMENT
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

lookup = {item['root']: index for index, item in enumerate(data['universal_functions'])}

print("🔄 INJECTION DU BATCH #17 (MORAL BINARIES)...")

for item in batch:
    root = item['root']
    if root in lookup:
        # Update existing
        idx = lookup[root]
        data['universal_functions'][idx].update(item)
        print(f"   -> [LINKED] : {root} <--> {item['binary_pair']}")
    else:
        # Create new
        data['universal_functions'].append(item)
        print(f"   -> [NEW]    : {root} <--> {item['binary_pair']}")

# SAUVEGARDE
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=4, ensure_ascii=False)

print("✅ BATCH #17 TERMINÉ. Le système distingue maintenant la Sécurité (A-M-N) du Masquage (K-F-R).")

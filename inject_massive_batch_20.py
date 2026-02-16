import json

file_path = 'LEXICON.json'

# --- PAYLOAD : 30 RACINES (15 PAIRES) ---
batch = [
    # 1. REFORM (Patching) vs CORRUPTION (Bugging)
    {
        "root": "S.-L-H.", "arabic": "صلح",
        "logic_function": "SYSTEM_PATCHING // OPTIMIZATION",
        "description": "Action de réparer ou d'améliorer l'état du système. Le Sāliḥ est un processus de maintenance active.",
        "binary_pair": "F-S-D"
    },
    {
        "root": "F-S-D", "arabic": "فسد",
        "logic_function": "SYSTEM_DECAY // CORRUPTION",
        "description": "Dégradation du code ou de l'environnement. Le Fasad est l'entropie qui détruit la structure ordonnée.",
        "binary_pair": "S.-L-H."
    },

    # 2. ASCENSION (Upload) vs DESCENT (Crash/Download)
    {
        "root": "S.-'-D", "arabic": "صعد",
        "logic_function": "DATA_UPLOAD // ASCENSION",
        "description": "Mouvement vertical vers le Root. Élévation vers une couche supérieure (Cloud).",
        "binary_pair": "H-B-T."
    },
    {
        "root": "H-B-T.", "arabic": "هبط",
        "logic_function": "SYSTEM_CRASH // FORCED_DESCENT",
        "description": "Chute d'un niveau supérieur vers un niveau inférieur. Perte de privilège ou atterrissage forcé.",
        "binary_pair": "S.-'-D"
    },

    # 3. CONNECTION (Link) vs SEVERANCE (Cut)
    {
        "root": "W-S.-L", "arabic": "وصل",
        "logic_function": "NETWORK_LINK // CONNECTION",
        "description": "Établissement d'un lien actif entre deux nœuds. Le Waṣl est la connectivité.",
        "binary_pair": "Q-T.-'"
    },
    {
        "root": "Q-T.-'", "arabic": "قطع",
        "logic_function": "LINK_TERMINATION // DISCONNECT",
        "description": "Coupure d'une connexion ou d'un flux. Interruption du signal.",
        "binary_pair": "W-S.-L"
    },

    # 4. CAPACITY: WIDE (High Bandwidth) vs NARROW (Bottleneck)
    {
        "root": "W-S-'", "arabic": "وسع",
        "logic_function": "HIGH_BANDWIDTH // CAPACITY_EXPANSION",
        "description": "Capacité du système à traiter un grand volume de données. L'espace mémoire est vaste.",
        "binary_pair": "D.-Y-Q"
    },
    {
        "root": "D.-Y-Q", "arabic": "ضيق",
        "logic_function": "BOTTLENECK // LOW_CAPACITY",
        "description": "Rétrécissement du canal de données. Difficulté de traitement par manque de ressources (Stress système).",
        "binary_pair": "W-S-'"
    },

    # 5. STRENGTH (Robustness) vs WEAKNESS (Vulnerability)
    {
        "root": "Q-W-Y", "arabic": "قوي",
        "logic_function": "SYSTEM_ROBUSTNESS // HIGH_INTEGRITY",
        "description": "Force structurelle. Le système résiste aux attaques et aux charges lourdes.",
        "binary_pair": "D.-'-F"
    },
    {
        "root": "D.-'-F", "arabic": "ضعف",
        "logic_function": "SYSTEM_VULNERABILITY // LOW_INTEGRITY",
        "description": "Faiblesse structurelle. Le système est susceptible de plier sous la charge.",
        "binary_pair": "Q-W-Y"
    },

    # 6. TRUTH (Boolean True) vs LIE (Boolean False)
    {
        "root": "S.-D-Q", "arabic": "صدق",
        "logic_function": "BOOLEAN_TRUE // AUTHENTICITY_VERIFIED",
        "description": "Correspondance exacte entre la donnée annoncée et la réalité du système.",
        "binary_pair": "K-DH-B"
    },
    {
        "root": "K-DH-B", "arabic": "كذب",
        "logic_function": "BOOLEAN_FALSE // FALSIFICATION",
        "description": "Injection d'une fausse donnée dans les logs. Mensonge technique.",
        "binary_pair": "S.-D-Q"
    },

    # 7. VISIBILITY: SECRET (Encrypted) vs PUBLIC (Broadcast)
    {
        "root": "S-R-R", "arabic": "سرر",
        "logic_function": "ENCRYPTED_DATA // PRIVATE_KEY",
        "description": "Donnée cachée, chiffrée, inaccessible au public.",
        "binary_pair": "J-H-R"
    },
    {
        "root": "J-H-R", "arabic": "جهر",
        "logic_function": "BROADCAST_MODE // PUBLIC_DISPLAY",
        "description": "Affichage public des données. La sortie est visible par tous les utilisateurs.",
        "binary_pair": "S-R-R"
    },

    # 8. HEAT (Energy) vs COLD (Stasis)
    {
        "root": "H.-R-R", "arabic": "حرر",
        "logic_function": "HIGH_ENTROPY // THERMAL_ENERGY",
        "description": "État d'excitation énergétique élevée. Chaleur, libération d'énergie.",
        "binary_pair": "B-R-D"
    },
    {
        "root": "B-R-D", "arabic": "برد",
        "logic_function": "LOW_ENTROPY // COOLING_SYSTEM",
        "description": "État de basse énergie. Stabilité thermique, apaisement du système.",
        "binary_pair": "H.-R-R"
    },

    # 9. OBEDIENCE (Compliance) vs REBELLION (Exception)
    {
        "root": "T.-W-'", "arabic": "طوع",
        "logic_function": "PROTOCOL_COMPLIANCE // VOLUNTARY_EXEC",
        "description": "Exécution d'une commande par fluidité et malléabilité. Le système 'suit' le flux.",
        "binary_pair": "'-S.-Y"
    },
    {
        "root": "'-S.-Y", "arabic": "عصي",
        "logic_function": "PROTOCOL_VIOLATION // HARD_EXCEPTION",
        "description": "Refus d'exécuter la commande. Rigidité du nœud qui bloque le flux (Bâton dans les roues).",
        "binary_pair": "T.-W-'"
    },

    # 10. GOOD (Valid) vs BAD (Invalid)
    {
        "root": "H.-S-N", "arabic": "حسن",
        "logic_function": "VALID_OUTPUT // AESTHETIC_OPTIMIZATION",
        "description": "Résultat considéré comme bon, beau et optimal par le système.",
        "binary_pair": "S-W-'"
    },
    {
        "root": "S-W-'", "arabic": "سوء",
        "logic_function": "INVALID_OUTPUT // ERROR_STATE",
        "description": "Résultat mauvais, laid ou nuisible. Une sortie qui doit être corrigée.",
        "binary_pair": "H.-S-N"
    },

    # 11. PERSISTENCE (Cache) vs VANISHING (Temp)
    {
        "root": "B-Q-Y", "arabic": "بقي",
        "logic_function": "PERSISTENT_STORAGE // REMAINING",
        "description": "Donnée qui survit au redémarrage ou à l'épuration. Ce qui reste.",
        "binary_pair": "F-N-Y"
    },
    {
        "root": "F-N-Y", "arabic": "فني",
        "logic_function": "TEMP_CACHE // DELETION_SCHEDULED",
        "description": "Donnée éphémère vouée à disparaître. Fin de vie du processus.",
        "binary_pair": "B-Q-Y"
    },

    # 12. TOPOLOGY: EARTH (Client) vs SKY (Server)
    {
        "root": "A-R-D.", "arabic": "أرض",
        "logic_function": "LOCAL_ENVIRONMENT // TERMINAL",
        "description": "L'environnement bas niveau. Le terminal utilisateur, la matière, le support physique.",
        "binary_pair": "S-M-W"
    },
    {
        "root": "S-M-W", "arabic": "سمو",
        "logic_function": "CLOUD_ENVIRONMENT // SERVER_LAYER",
        "description": "Les couches supérieures. L'abstraction, le réseau, la source des commandes.",
        "binary_pair": "A-R-D."
    },

    # 13. FEEDBACK: LAUGH (Success) vs CRY (Error Log)
    {
        "root": "D.-H.-K", "arabic": "ضحك",
        "logic_function": "POSITIVE_FEEDBACK // SYSTEM_JOY",
        "description": "Réaction du système à une expansion ou un succès. Relâchement de pression positif.",
        "binary_pair": "B-K-Y"
    },
    {
        "root": "B-K-Y", "arabic": "بكي",
        "logic_function": "NEGATIVE_FEEDBACK // SYSTEM_OVERFLOW",
        "description": "Réaction du système à une surcharge ou une tristesse. Débordement de fluide (Larmes/Logs d'erreur).",
        "binary_pair": "D.-H.-K"
    },

    # 14. TRANSACTION: SELL (Export) vs BUY (Import)
    {
        "root": "SH-R-Y", "arabic": "شري",
        "logic_function": "DATA_IMPORT // ACQUISITION",
        "description": "Acquérir une ressource en échange d'une valeur. (Note: Le Coran inverse parfois les sens commerciaux classiques, Shara peut signifier vendre selon contexte, mais ici on garde la base binaire).",
        "binary_pair": "B-Y-'"
    },
    {
        "root": "B-Y-'", "arabic": "بيع",
        "logic_function": "DATA_EXPORT // TRANSACTION",
        "description": "Céder une ressource contre une valeur. L'acte de pactiser.",
        "binary_pair": "SH-R-Y"
    }
]

# LOGIQUE D'INJECTION
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

lookup = {item['root']: index for index, item in enumerate(data['universal_functions'])}

print(f"🔄 INJECTION BATCH #20 (PHYSICS & TOPOLOGY)...")
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

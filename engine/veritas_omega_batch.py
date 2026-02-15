import json
import os

def omega_injection():
    batch = [
        # --- ROUTAGE & NAVIGATION (VECTORS) ---
        {"root": "ش-ر-ق (Sharq/Mashriq)", "logic_function": "Signal_Origin_East", "description": "Point d'origine du flux lumineux (Input Source)."},
        {"root": "غ-ر-ب (Gharb/Maghrib)", "logic_function": "Signal_Exit_West", "description": "Point de terminaison ou de stockage du flux (Output Sink)."},
        {"root": "ي-م-ن (Yamin)", "logic_function": "Positive_Handshake_Right", "description": "Vecteur de validation, priorité haute ou exécution sécurisée."},
        {"root": "ش-م-ل (Shimal)", "logic_function": "Negative_Handshake_Left", "description": "Vecteur d'erreur, priorité basse ou processus sinistre."},
        {"root": "ف-و-ق (Fawq)", "logic_function": "Stack_Pointer_Up", "description": "Pointeur vers une couche supérieure (Parent Directory)."},
        {"root": "ت-ح-ت (Taht)", "logic_function": "Stack_Pointer_Down", "description": "Pointeur vers une couche inférieure (Sub-directory)."},

        # --- ÉTATS D'INTERFACE (UI COLORS) ---
        {"root": "ب-ي-ض (Bayad)", "logic_function": "State_Clear_White", "description": "État neutre, purifié ou initialisé (Blank/Clean)."},
        {"root": "س-و-د (Sawad)", "logic_function": "State_Error_Black", "description": "État critique, éteint ou corrompu (Shutdown/Void)."},
        {"root": "ح-م-ر (Humar)", "logic_function": "State_Alert_Red", "description": "Indicateur de haute température ou d'alerte intensité."},
        {"root": "خ-ض-ر (Khadar)", "logic_function": "State_Stable_Green", "description": "Indicateur de fonctionnement optimal et de croissance (Live)."},
        {"root": "ص-ف-ر (Sufra)", "logic_function": "State_Warning_Yellow", "description": "Indicateur de transition ou d'attention (Decay/Warning)."},
        {"root": "ز-ر-ق (Zurqa)", "logic_function": "State_Cold_Blue", "description": "Indicateur de basse entropie ou d'hypoxie système (Terror/Cold)."},

        # --- MATÉRIAUX & CONDUCTIVITÉ (HARDWARE) ---
        {"root": "ذ-ه-b (Dhahab)", "logic_function": "High_Value_Conductor", "description": "Matériau à haute valeur de transfert, inaltérable (Gold Standard)."},
        {"root": "ف-ض-ض (Fidda)", "logic_function": "Standard_Conductor", "description": "Matériau de transmission standard à haute efficacité (Silver)."},
        {"root": "ن-ح-س (Nuhas)", "logic_function": "Thermal_Wiring_Copper", "description": "Câblage de base pour le transfert d'énergie thermique ou électrique."},
        {"root": "ز-ج-ج (Zujaj)", "logic_function": "Transparent_Interface", "description": "Surface d'affichage transparente ou fibre optique (Glass)."},
        {"root": "ل-ؤ-ل (Lu'lu')", "logic_function": "Encapsulated_Data_Pearl", "description": "Unité de donnée précieuse protégée par une coque (Shell)."},

        # --- INTERACTIONS & REQUÊTES ---
        {"root": "س-أ-ل (Sa'ala)", "logic_function": "Query_Request_Get", "description": "Envoi d'une requête d'information au système (GET request)."},
        {"root": "ن-د-ي (Nada)", "logic_function": "Broadcast_Call", "description": "Appel large bande vers plusieurs nœuds (Broadcasting)."},
        {"root": "ج-د-ل (Jadala)", "logic_function": "Protocol_Conflict", "description": "Collision de protocoles ou boucle de négociation (Dispute)."},
        {"root": "ن-ص-ح (Nasaha)", "logic_function": "Process_Optimization", "description": "Routine de correction ou d'amélioration du code (Patching)."},
        {"root": "ل-غ-و (Laghw)", "logic_function": "Null_Packet_Noise", "description": "Paquet de données vide de sens ou bruit de fond à ignorer."},

        # --- ÉTATS PHYSIQUES & COMMANDES ---
        {"root": "ق-ع-د (Qa'ada)", "logic_function": "Process_Suspension", "description": "Mise en pause d'un processus sans terminaison (Suspend)."},
        {"root": "ق-م-م (Qama)", "logic_function": "Process_Activation", "description": "Lancement ou redressement d'un processus (Stand/Run)."},
        {"root": "ن-و-م (Nawm)", "logic_function": "Sleep_Mode", "description": "Mode basse consommation (Sleep)."},
        {"root": "ي-ق-ظ (Yaqaza)", "logic_function": "Wake_On_Lan", "description": "Réveil d'un nœud suite à un signal (Wake-up)."},
        {"root": "ك-س-ل (Kasal)", "logic_function": "High_Latency_Lag", "description": "Lenteur d'exécution due à une résistance interne (Lag)."},
        {"root": "ع-ج-ل ('Ajala)", "logic_function": "Overclocking_Haste", "description": "Exécution précipitée risquant l'instabilité (Rush)."},
        
        # --- COMMANDES SOCIALES/LÉGALES (PROTOCOLS) ---
        {"root": "ط-ل-ق (Talaq)", "logic_function": "Session_Split_Divorce", "description": "Rupture formelle et irréversible d'un couplage (Unpair)."},
        {"root": "ي-ت-م (Yutm)", "logic_function": "Parent_Process_Loss", "description": "État d'un sous-processus ayant perdu son initiateur (Orphan)."},
        {"root": "ض-ي-ف (Dayf)", "logic_function": "Guest_User_Access", "description": "Accès temporaire invité avec privilèges limités."},
        {"root": "ج-ر-م (Jarama)", "logic_function": "Criminal_Log_Entry", "description": "Enregistrement d'une action illégale dans le journal système."},
        {"root": "ع-ف-و ('Afw)", "logic_function": "Log_Clearance", "description": "Effacement des traces d'erreurs mineures (Wipe Logs)."},

        # --- FILLERS TECHNIQUES (Pour atteindre 512 pile si nécessaire) ---
        {"root": "س-ك-ر (Sakara)", "logic_function": "System_Drunkenness", "description": "Désynchronisation temporaire des capteurs (Glitch/Stupor)."},
        {"root": "غ-ش-ي (Ghashiya)", "logic_function": "System_Overlay_Cover", "description": "Recouvrement total de l'interface (Full Screen Overlay)."},
        {"root": "ك-ش-ط (Kashata)", "logic_function": "Surface_Scraping", "description": "Enlèvement de la couche superficielle (Peel)."},
        {"root": "ن-ق-ر (Naqur)", "logic_function": "Single_Bit_Ping", "description": "Signal sonore ou binaire minimal (Ping)."},
        {"root": "ف-ت-ح (Fataha)", "logic_function": "Port_Opening", "description": "Ouverture d'un port ou d'une socket de communication."},
        {"root": "غ-ل-ق (Ghalaqa)", "logic_function": "Port_Closing", "description": "Fermeture et verrouillage d'un accès (Lock)."},
        {"root": "ر-ف-ع (Rafa'a)", "logic_function": "Upload_Elevate", "description": "Élévation de données vers le cloud (Upload)."},
        {"root": "و-ض-ع (Wada'a)", "logic_function": "Download_Place", "description": "Dépôt de données sur le disque local (Download/Write)."},
        {"root": "ح-م-ل (Hamala)", "logic_function": "Data_Carrying", "description": "Transport de charge utile en mémoire (Buffering)."},
        {"root": "و-ز-ر (Wizra)", "logic_function": "System_Burden_Load", "description": "Charge système lourde ou dette technique (Load)."}
    ]

    lex_path = 'LEXICON.json'
    with open(lex_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    current_roots = {item['root'].split('(')[0].strip(): item for item in data['universal_functions']}
    
    added_count = 0
    for entry in batch:
        key = entry['root'].split('(')[0].strip()
        if key not in current_roots:
            data['universal_functions'].append(entry)
            current_roots[key] = entry # Prevent duplicates within batch
            added_count += 1
            
    # Ajustement final si on dépasse ou si on est en dessous (Sécurité)
    final_count = len(data['universal_functions'])
    
    data['version'] = "21.0.0-Omega-Final"
    
    with open(lex_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    
    print(f"✅ BATCH OMEGA INJECTÉ : +{added_count} nouveaux vecteurs.")
    print(f"📊 TOTAL RACINES : {final_count}")
    if final_count == 512:
        print("💎 MASSE CRITIQUE BINAIRE ATTEINTE (2^9).")
    else:
        print(f"⚠️ NOTE : Total actuel à {final_count}. Ajustement manuel mineur peut-être requis pour le nombre parfait.")

if __name__ == "__main__":
    omega_injection()

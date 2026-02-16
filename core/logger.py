import logging
import os

class SystemLogger:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SystemLogger, cls).__new__(cls)
            cls._instance._setup()
        return cls._instance

    def _setup(self):
        self.logger = logging.getLogger("VeritasKernel")
        self.logger.setLevel(logging.INFO)
        
        # Eviter les doublons de logs si rechargé
        if not self.logger.handlers:
            # Format: [DATE] [NIVEAU] MESSAGE
            formatter = logging.Formatter('%(asctime)s - [%(levelname)s] - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

            # 1. Écriture dans un fichier
            file_handler = logging.FileHandler("system.log", encoding='utf-8')
            file_handler.setFormatter(formatter)
            self.logger.addHandler(file_handler)

            # 2. Affichage dans la console (pour le débug)
            console_handler = logging.StreamHandler()
            console_handler.setFormatter(formatter)
            self.logger.addHandler(console_handler)

    def info(self, message):
        self.logger.info(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)

# Instance unique accessible partout
logger = SystemLogger()

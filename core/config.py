import yaml
import os

class ConfigLoader:
    _instance = None
    _config = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ConfigLoader, cls).__new__(cls)
            cls._instance._load_config()
        return cls._instance

    def _load_config(self):
        # On remonte d'un niveau pour trouver config.yaml à la racine
        base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        config_path = os.path.join(base_path, "config.yaml")
        
        if os.path.exists(config_path):
            with open(config_path, "r", encoding="utf-8") as f:
                self._config = yaml.safe_load(f)
        else:
            self._config = {
                "app": {"name": "Veritas Kernel", "version": "UNKNOWN", "mode": "debug"},
                "interface": {"layout": "wide", "sidebar_state": "expanded"},
                "database": {"path": "LEXICON.json"},
                "modules": {"enable_governance": True, "enable_export": False}
            }

    @property
    def settings(self):
        return self._config

config = ConfigLoader().settings

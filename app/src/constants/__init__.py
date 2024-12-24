from pathlib import Path

#CONFIG_FILE_PATH = Path("config/config.yaml")
#PARAMS_FILE_PATH = Path("params.yaml")

BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent
CONFIG_FILE_PATH = BASE_DIR / "app" / "config" / "config.yaml"
PARAMS_FILE_PATH = BASE_DIR / "app" / "params.yaml"
import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')


project_name = "textSummarizer"

list_of_files = [
    "app/.github/workflows/.gitkeep",
    "app/src/__init__.py",
    "app/src/components/__init__.py",
    "app/src/utils/__init__.py",
    "app/src/utils/common.py",
    "app/src/logging/__init__.py",
    "app/src/config/__init__.py",
    "app/src/config/configuration.py",
    "app/src/pipeline/__init__.py",
    "app/src/entity/__init__.py",
    "app/src/constants/__init__.py",
    "app/config/config.yaml",
    "app/params.yaml",
    "app/app.py",
    "app/main.py",
    "app/Dockerfile",
    "app/requirements.txt",
    "app/setup.py",
    "app/research/trials.ipynb",

]


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory:{filedir} for the file {filename}")

    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath,'w') as f:
            pass
            logging.info(f"Creating empty file: {filepath}")


    
    else:
        logging.info(f"{filename} is already exists")
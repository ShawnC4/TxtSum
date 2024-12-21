import os
from box.exceptions import BoxValueError
import yaml
from src.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any



@ensure_annotations
def read_yaml(path_to_yaml:Path) -> ConfigBox:
    """
    Read yaml file and return the content

    Args:
        path_to_yaml (Path): Path to the yaml file
    
    Raises:
        BoxValueError: If the yaml file is empty
        e: empty file

    Returns:
        ConfigBox: The content of the yaml file
    """

    try:
        with open(path_to_yaml, 'r') as file:
            content = yaml.safe_load(file)
            logger.info(f"Reading {path_to_yaml} file")
            return ConfigBox(content)
        
    except BoxValueError as e:
        logger.error(f"Empty file: {path_to_yaml}")
        raise ValueError(f"Empty file: {path_to_yaml}")
    
    except Exception as e:
        logger.error(f"Error reading {path_to_yaml} file")
        raise e
    
@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """
    Create directories

    Args:
        path_to_directories (list): List of directories to create
        verbose (bool, optional): Print logs. Defaults to True.
    """
    for path in path_to_directories:
        try:
            os.makedirs(path, exist_ok=True)
            if verbose:
                logger.info(f"Directory created: {path}")

        except Exception as e:
            logger.error(f"Error creating directory: {path}")
            raise e
    

@ensure_annotations
def get_size(path: Path) -> str:
    """
    Get the size of a file in Kb

    Args:
        path (Path): Path to the file

    Returns:
        str: The size of the file in Kb
    """
    size_in_Kb = round(os.path.getsize(path) / 1024)
    return f"~ {size_in_Kb} Kb"
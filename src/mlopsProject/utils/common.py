import os
from box.exceptions import BoxValueError
import yaml
from mlopsProject.logging import logger
from ensure import ensuree_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any

@ensuree_annotations
def read_yaml(filepath: Path) -> ConfigBox:
    """
    Read yaml file and return a ConfigBox object.

    Args:
        filepath (Path): path to yaml file
    
    Raises:
        ValueError: if yaml file is empty
        e: empty file
    
    Returns:
        ConfigBox: ConfigBox type
    """
    try:
        with open(filepath) as file:
            content = yaml.safe_load(file)
            logger.info(f"file: {filepath} loaded correctly")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    
@ensuree_annotations
def create_directory(dirpaths: list, verbose = True) -> None:
    """
    Create list of directories

    Args:
        dirpaths (list): list of directory paths
        verbose (bool, optional): verbosity (True to print logs). Defaults to True.
    """
    
    for path in dirpaths:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"directory {path} created")


def get_size(path: Path) -> str:
    """
    Get size of file in KB

    Args:
        path (Path): path to file
    
    Returns:
        str: size of file in KB
    """
    
    size_in_kb = round(os.path.getsize(path) / 1024, 3)
    return f"approx {size_in_kb} KB"


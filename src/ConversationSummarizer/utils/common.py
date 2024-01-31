import os
import yaml
from ConversationSummarizer.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from box.exceptions import BoxValueError
from pathlib import Path

#@esnure_annotationsis a decorator that checks the type of the arguments and the return type of the function

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Read a yaml file

    Args:
        path_to_yaml (Path): path like input

    Raises:
        ValueError: if yaml file is empty or not a yaml file

    Returns:
        ConfigBox: ConfigBox type
    """
    if path_to_yaml.suffix != '.yaml':
        raise ValueError("Provided file is not a yaml file")

    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            if not content:
                raise ValueError("yaml file is empty")
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
 
    


@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """
    Create directories
    
    
    Raises:
        TypeError: if path_to_directories is not a list

    Args:
        path_to_directories (list): list of directory paths to create
        verbose (bool): Whether to print verbose output. Default is True.
    """
    # Loop through the list of paths to directories
    for path in path_to_directories:
        # Create the directory if it does not exist
        os.makedirs(path, exist_ok=True)
        # Log the creation of the directory if verbose is True
        if verbose:
            logger.info(f"created directory at: {path}")



@ensure_annotations
def get_size(path: Path) -> str:
    """
    Get the size of a file in KB

    Args:
        path (Path): path of the file

    Returns:
        str: size in KB
    """
    # Get the size of the file in KB rounded to 4 decimals
    size_in_kb = round(os.path.getsize(path)/1024, 4)
    return f"~ {size_in_kb} KB"


@ensure_annotations
def get_size(path: Path) -> str:
    """
    Get the size of a file in KB

    Args:
        path (Path): path of the file

    Raises:
        FileNotFoundError: if the path does not exist or is not a file

    Returns:
        str: size of the file in KB
    """
    if not path.exists() or not path.is_file():
        raise FileNotFoundError(f"{path} does not exist or is not a file")

    size_in_kb = round((path.stat().st_size)/1024, 4) # path.stat().st_size returns the size of the file in bytes
    return f"~ {size_in_kb} KB"
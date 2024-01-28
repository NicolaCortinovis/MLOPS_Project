import os
from box.exceptions import BoxValueError
import yaml
from mlopsProject.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
from datasets import Dataset
import pandas as pd
import jsonlines

@ensure_annotations
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
    
@ensure_annotations
def create_directory(dirpaths: list, verbose = True):
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

def read_jsonl_to_dataset(path : Path) -> Dataset:
    """
    Read jsonl file and return a Dataset object.

    Args:
        path (Path): path to jsonl file
    
    Returns:
        Dataset: Dataset type
    """
    data = []
    with jsonlines.open(path) as reader:
        for obj in reader:
            data.append(obj)
    df = pd.DataFrame(data)
    return Dataset.from_dict(df.to_dict('list'))
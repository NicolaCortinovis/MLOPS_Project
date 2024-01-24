import os
from pathlib import Path
import logging

## Type of logging to be used

time_format = "%d-%m-%Y %H:%M:%S"
logging.basicConfig(level=logging.INFO, format = '[%(asctime)s] - %(levelname)s - %(message)s', datefmt = time_format)

project_name = "mlopsProject"

## List of files to be included in the project

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "research/demo.ipynb",
]

## Creating the project structure: files and folders

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir , filename = os.path.split(filepath)

    # Creating the directory if it does not exist
    if filedir != "":
        os.makedirs(filedir, exist_ok = True) 
        logging.info(f"Creating directory: {filedir} for the file {filename}")
    
    # Creating the file if it does not exist
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            logging.info(f"Creating file: {filepath}")
            pass
            
    # If the file already exists
    else:
        logging.info(f"{filename} already exists")

        
        

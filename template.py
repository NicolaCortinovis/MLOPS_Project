import os
from pathlib import Path
import logging

## Type of logging to be used

time_format = "%d-%m-%Y %H:%M:%S" # e.g. 01-01-2021 12:00:00
logging.basicConfig(level=logging.INFO, format = '[%(asctime)s] - %(levelname)s - %(message)s', datefmt = time_format)

project_name = "ConversationSummarizer"

## List of files to be included in the project

list_of_files = [
    ".github/workflows/.gitkeep",                       # contains github actions
    f"src/{project_name}/__init__.py",                  # contains the constructor for the project
    f"src/{project_name}/components/__init__.py",       # contains the constructor for the components
    f"src/{project_name}/utils/__init__.py",            # contains the constructor for the utils
    f"src/{project_name}/utils/common.py",              # contains the common functions
    f"src/{project_name}/logging/__init__.py",          # contains the constructor for the logger
    f"src/{project_name}/config/__init__.py",           # contains the constructor for the config
    f"src/{project_name}/config/configuration.py",      # contains the config handlers for the project steps
    f"src/{project_name}/pipeline/__init__.py",         # contains the constructor for the pipeline
    f"src/{project_name}/entity/__init__.py",           # contains the constructor for the entities
    f"src/{project_name}/constants/__init__.py",        # contains the constructor for the constants
    "config/config.yaml",                               # contains instructions for the sorting of data, model
    "params.yaml",                                      # contains the parameters for training the model
    "app.py",                                           # contains the app 
    "main.py",                                          # contains the main: data -> train -> evaluate
    "Dockerfile",                                       # contains the instructions to build the docker image
    "requirements.txt",                                 # contains the list of packages to be installed
    "setup.py",                                         # contains the instructions to install the package
    "research/ConversationSummarizer.ipynb"                     # contains a notebook mimicking the main.py
]
## Creating the project structure: files and folders

for filepath in list_of_files:                          # looping through the list of files defined above
    filepath = Path(filepath)                           # converting the string to a Path object
    filedir , filename = os.path.split(filepath)        # separating the directory and the filename from the path

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

        
        

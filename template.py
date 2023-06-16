# importing libraries
import os
from pathlib import Path
import logging

# intializing logging
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

# name of project
project_name = "mushroom_classifier"

# list of files in our project

"""
    By including the .gitkeep file in the .github/workflows directory, 
    you ensure that the directory is not empty and is tracked by Git. 
    This can be useful when using GitHub Actions or other CI/CD workflows
"""
list_of_files = [

    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html"

]

for filepath in list_of_files:
    # convert the filepath to windows path
    filepath = Path(filepath)
    # get file and directories name from path
    filedir, filename = os.path.split(filepath)

    if filedir!="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"creating directory: {filedir} for the file: {filename}")

    # create file if not exists or file size is equal to zero
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath, "w") as f :
            pass
            logging.info(f"Creating empty file:{filepath}")
    
    # log if the file exists
    else:
        logging.info(f"{filename} is already exists")


            
        



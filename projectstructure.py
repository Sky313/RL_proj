import os
from pathlib import Path

project_name="src"

list_of_files=[

    f"{project_name}/__init__.py",
    f"{project_name}/components/__init__.py",
    f"{project_name}/components/data_ingestion.py",
    f"{project_name}/components/data_validation.py",
    f"{project_name}/components/data_transformation.py",
    f"{project_name}/components/model_trainer.py",
    f"{project_name}/constants/__init__.py",
    f"{project_name}/constants/constants.py",
    f"{project_name}/exception/__init__.py",
    f"{project_name}/exception/exception.py",
    f"{project_name}/logging/__init__.py",
    f"{project_name}/logging/logger.py",
    f"{project_name}/utils/__init__.py",
    f"{project_name}/utils/utils.py"

]

for path in list_of_files:
    filepath=Path(path)

    filedir,filename=os.path.split(path)
    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
from setuptools import find_packages,setup
from typing import List

HYPENEDOT="-e ."

def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","")for req in requirements]

        if HYPENEDOT in requirements:
            requirements.remove(HYPENEDOT)
    return requirements
           

setup(
    name="MLPROJECT",
    version="0.0.1",
    author="Manoj",
    author_email="bm22btech11008@iith.ac.in",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")

)
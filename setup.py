from setuptools import setup, find_packages
from typing import List

HYPHE_E_DOT = "-e ."

def get_requirements(filepath: str) -> List[str]:
    """This function reads a requirements file and returns a list of required packages."""
    requirements = []
    with open(filepath) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements]   

        if HYPHE_E_DOT in requirements:
            requirements.remove(HYPHE_E_DOT)

    return requirements
setup(
    name="mlproject",
    version="0.0.1",
    author="Jsnodal",
    author_email="mwirigialex351@gmail.com",
    packages= find_packages(),
    install_requires= get_requirements("requirements.txt")

)
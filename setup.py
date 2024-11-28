from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    '''
    This function reads a requirements file and returns a list of package requirements.
    It excludes the entry '-e .' if present.
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        # Strip newlines and whitespace
        requirements = [req.strip() for req in requirements if req.strip()]
        # Remove '-e .' if present
        requirements = [req for req in requirements if req != HYPHEN_E_DOT]
    return requirements

setup(
    name="ML_Project",
    version='0.0.1',
    author="Sukshith",
    author_email="sukshigowda736@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)

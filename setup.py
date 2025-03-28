from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path: str) -> List[str]:
    """
    Reads the requirements.txt file and returns a list of dependencies.
    It removes '-e .' if present to prevent setup.py from failing.
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.read().splitlines()  # Reads all lines and removes '\n'
        requirements = [req for req in requirements if req and req != "-e ."]  # Filters '-e .'
    
    return requirements

# Package setup configuration
setup(
    name='MLproject1',  # Name of the package/project
    version='0.0.1',  # Initial version
    author='Kalyan',  # Your name
    author_email='vknarasimharao@gmail.com',  # Your email
    packages=find_packages(),  # Automatically finds all packages in the directory
    install_requires=get_requirements('requirements.txt'),  # Reads dependencies from requirements.txt
)

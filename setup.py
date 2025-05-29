## Used for building your application as a package itself
from setuptools import find_packages, setup
from typing import List

#there can be many packages in the directory, so we use find_packages() to find all the packages in the current directory
# ## The find_packages() function will automatically find all the packages in the current directory and return a list of their names

HYPHEN_E_DOT = '-e .' # This is used to remove the -e . from the requirements file

def get_requirements(file_path: str)-> List[str]:
    """
    This function returns a list of requirements from the requirements file.
    """
    requirements=[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements=[req.replace("\n", "") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    
    return requirements

setup(
    name="mlproject",
    version="0.0.1",
    author="Gautam",
    author_email="gautam9394@gmail.com",
    packages=find_packages(), # Automatically find packages in the current directory
    #install_requires=['pandas', 'numpy', 'seaborn'] 
    install_requires=get_requirements('requirements.txt'), # Automatically find packages in the current directory


)
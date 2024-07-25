from setuptools import find_packages,setup
from typing import List

def get_requirements(file_path:str)->list[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [i.replace('\n',' ') for i in requirements]

        HYPEN_E_DOT='-e .'

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements

setup(
name = 'ML_project',
version = '0.0.1',
author = 'Abhishek',
author_email = 'abhi.bgt@gmail.com',
packages = find_packages(),
install_requires  = get_requirements('requirements.txt')

)
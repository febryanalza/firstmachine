from setuptools import setup, find_packages
from typing import List

HYPE_TEXT= '-e .'

def get_requirement(file_path:str)->List[str]:

    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements= [req.replace("\n","") for req in requirements]

        if HYPE_TEXT in requirements:
            requirements.remove(HYPE_TEXT)

    return requirements

setup(
name='firstmachine',
version='1.0.0',
author='FebryanAlZaqri',
author_email='febryanalzaqri27@gmail.com',
packages=find_packages(),
install_requires=get_requirement('requirements.txt')
)
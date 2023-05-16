#if i convert this project into packages we use setup.puy
from setuptools import find_packages,setup
from typing import List


HYPEN_E_DOT = '-e .'

def get_requriements(file_path:str)-> List[str]:
    requriements=[]
    with open(file_path) as file_obj:
        requriements=file_obj.readlines()
        requriements=[req.replace("\n","") for req in requriements]

        if HYPEN_E_DOT in requriements:
            requriements.remove(HYPEN_E_DOT)

    return requriements


setup(

    name='RegressorProject',
    version='0.0.1',
    author='Abhi',
    author_email='mr.potdarabhi@gmail.com',
    install_requires=get_requriements('requirements.txt'),
    packages=find_packages()
)
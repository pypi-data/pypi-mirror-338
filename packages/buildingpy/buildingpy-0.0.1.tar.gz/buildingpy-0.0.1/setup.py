from setuptools import setup, find_packages
import shutil
#copy buildingpy.py
shutil.copyfile('../BuildingPy.py', 'buildingpy/buildingpy.py')

#finally, convert to package
setup(
    name='buildingpy',
    version='v0.2-beta',
    packages=find_packages(),
    install_requires=[
    ],
)
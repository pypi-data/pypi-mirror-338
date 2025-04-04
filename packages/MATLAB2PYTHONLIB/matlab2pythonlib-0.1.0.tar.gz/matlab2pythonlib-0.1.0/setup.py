# Script para instalar la librería
from setuptools import setup, find_packages

setup(
    name="mi_libreria",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[],
    author="BelloDev",
    author_email="fernandojbf123@gmail.com",
    description="Una librería con funciones útiles",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Fernandojbf123/MATLAB2PYTHONLIB",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)
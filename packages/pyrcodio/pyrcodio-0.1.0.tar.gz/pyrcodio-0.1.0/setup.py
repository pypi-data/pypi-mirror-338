# setup.py
from setuptools import setup, find_packages
import os

def read_file(filename):
    with open(os.path.join(os.path.dirname(__file__), filename)) as file:
        return file.read()

setup(
    name="pyrcodio",
    version="0.1.0",
    author="Eugenio Del Male",
    description="Una utility CLI blasfema che genera nomi combinando soggetti e attributi.",
    long_description=read_file("README.md"),
    long_description_content_type="text/markdown",
    url="https://github.com/nicoDs96/pyrcodio",
    packages=find_packages(),
    include_package_data=True,
    package_data={
        'pyrcodio': ['data/*'],
    },
    entry_points={
        'console_scripts': [
            'pyrcodio=pyrcodio.cli:main',
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
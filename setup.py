import os
from setuptools import setup, find_packages

__version__ = "1.0.0"

BASE_DIR = os.path.dirname(os.path.realpath(__file__))


with open(os.path.join(BASE_DIR, "requirements.txt")) as f:
    requirements = f.read().split("\n")


setup(
    name="fast-installer",
    version=__version__,
    description="fast pythonic installer for projects using yaml config",
    author="Elran Shefer",
    keywords="fast installer",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "fastinstall = fast_installer:main"
        ]
    },
    packages=find_packages("src"),
    package_dir={"": "src"}
)

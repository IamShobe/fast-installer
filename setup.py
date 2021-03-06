import os
from setuptools import setup, find_packages

__version__ = "1.2.0"

BASE_DIR = os.path.dirname(os.path.realpath(__file__))


with open(os.path.join(BASE_DIR, "requirements.txt")) as f:
    requirements = f.read().split("\n")

with open(os.path.join(BASE_DIR, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name="fast-installer",
    version=__version__,
    url="https://github.com/IamShobe/fast-installer",
    description="fast pythonic installer for projects using yaml config",
    long_description=long_description,
    long_description_content_type='text/markdown',
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

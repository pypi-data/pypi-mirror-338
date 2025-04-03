# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open("README.rst") as f:
    readme = f.read()

setup(
    name="OptlangHelper",
    version="0.0.2",
    description="Python package for building Linear Programming models that are compatible with Optlang",
    long_description_content_type="text/x-rst",
    long_description=readme,
    author="Andrew Freiburger",
    author_email="afreiburger@anl.gov",
    url="https://github.com/Freiburgermsu/OptlangHelper",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
        "Intended Audience :: Science/Research",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Natural Language :: English",
    ],
    install_requires=[
        "optlang",
        # "glpk",
        # "cplex",
        # "gurobipy"
    ],
    # tests_require=[
    #     "pytest",
    # ],
    project_urls={
        # "Documentation": "https://modelseedpy.readthedocs.io/en/latest/",
        "Issues": "https://github.com/Freiburgermsu/OptlangHelper/issues",
    },
)

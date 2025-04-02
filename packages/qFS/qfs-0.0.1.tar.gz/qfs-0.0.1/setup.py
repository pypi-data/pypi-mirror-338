# setup.py for qFS package
from setuptools import setup, find_packages

setup(
    name="qFS",
    version="0.0.1",
    description="A Python package for Quantum Feature Selection (qFS).",
    author="Ayushmaan Singh",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "scikit-learn"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7'
)
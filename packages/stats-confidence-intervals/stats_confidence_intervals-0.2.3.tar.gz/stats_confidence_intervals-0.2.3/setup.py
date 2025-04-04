import os
from setuptools import setup, find_packages

# Ensure the current directory is correctly set
current_directory = os.path.abspath(os.path.dirname(__file__))

def read_file(filename):
    with open(os.path.join(current_directory, filename), encoding='utf-8') as f:
        long_description = f.read()
    return long_description

setup(
    name="stats_confidence_intervals",
    version="0.2.3",
    author="Subashanan Nair",
    author_email="subashanan.nair@gmail.com",
    description="A comprehensive library for calculating and visualizing confidence intervals",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/SubaashNair/Confidence-Interval-Library",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Education",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Scientific/Engineering",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.7",
    install_requires=[
        "numpy>=1.20.0",
        "scipy>=1.7.0",
        "matplotlib>=3.4.0",
    ],
)


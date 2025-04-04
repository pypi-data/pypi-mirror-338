# setup.py

from setuptools import setup, find_packages

setup(
    name="oceanmaster-password-generator",
    version="0.1.0",
    author="Abhishek Kumar / ocean-masterO",
    description="An advanced password generator library with multiple security features",
    packages=find_packages(),
    install_requires=[],  # No external dependencies
    python_requires='>=3.6',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

from setuptools import setup, find_packages
import os

setup(
    name="autopip-Ninja-22",
    version="0.5",
    packages=find_packages(),
    description="Python modüllerini otomatik yükleyen kütüphane",
    long_description=open("README.md").read() if os.path.exists("README.md") else "",
    long_description_content_type="text/markdown",
    author="Ninja-22",
    author_email="sametcevik88@gmail.com",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
) 
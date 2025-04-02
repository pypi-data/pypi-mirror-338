from setuptools import setup, find_packages
import os

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="apirotater",
    version="0.4.1",
    description="Python library for API key rotation, rate limit control and load balancing",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="mre31",
    packages=find_packages(),
    install_requires=[
        "python-dotenv>=0.19.0",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
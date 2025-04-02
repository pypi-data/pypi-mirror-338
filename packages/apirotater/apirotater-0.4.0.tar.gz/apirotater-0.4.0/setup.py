from setuptools import setup, find_packages

setup(
    name="apirotater",
    version="0.4.0",
    description="Python library for API key rotation, rate limit control and load balancing",
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
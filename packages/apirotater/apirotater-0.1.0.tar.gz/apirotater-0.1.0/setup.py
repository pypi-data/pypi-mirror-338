from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="apirotater",
    version="0.1.0",
    author="mre31",
    author_email="y.e.karabag@gmail.com",
    description="A library to help prevent rate limits by using API keys in rotation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mre31/apirotater",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.6",
    keywords="api, key rotation, rate limit",
)
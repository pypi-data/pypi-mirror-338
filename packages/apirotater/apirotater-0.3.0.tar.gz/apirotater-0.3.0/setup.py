from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="apirotater",
    version="0.3.0",
    author="mre31",
    author_email="y.e.karabag@gmail.com",
    description="A library to help prevent rate limits or load balance by using API keys in rotation",
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
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.6",
    keywords="api, key rotation, rate limit",
    install_requires=[
        "python-dotenv>=1.0.0",
    ],
    entry_points={
        "console_scripts": [
            "apirotater-setup=apirotater.setup_keys:main",
        ],
    },
)
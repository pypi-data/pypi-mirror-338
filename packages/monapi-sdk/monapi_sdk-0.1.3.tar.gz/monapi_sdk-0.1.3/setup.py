from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="monapi-sdk",
    version="0.1.3",
    author="Monapi Team",
    author_email="info@monapi.io",
    description="SDK for integrating with the Monapi Marketplace",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/monapi-sdk",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=[
        "fastapi>=0.95.0",
    ],
) 
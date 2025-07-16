from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="mosaia",
    version="0.1.0",
    author="Mosaia",
    author_email="development@mosaia.com",
    description="A Python SDK for Mosaia API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mosaia-development/mosaia-python-sdk",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10",
    install_requires=[
        "requests>=2.25.0",
        "pydantic>=2.0.0",
        "bson>=0.5.0",
        "aiohttp>=3.8.0"
    ],
    extras_require={
        'test': [
            'pytest>=7.0',
            'pytest-asyncio>=0.21.0',
            # other test dependencies
        ],
    }
) 
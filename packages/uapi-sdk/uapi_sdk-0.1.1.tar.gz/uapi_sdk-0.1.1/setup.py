from setuptools import setup, find_packages

setup(
    name="uapi-sdk",
    version="0.1.1",
    description="A simple SDK for discovering and accessing API endpoints",
    packages=find_packages(),
    python_requires=">=3.7",
    install_requires=[
        "requests>=2.31.0",
        "typing-extensions>=4.5.0",
    ],
) 
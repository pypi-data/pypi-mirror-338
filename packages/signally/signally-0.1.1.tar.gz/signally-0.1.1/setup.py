from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="signally",
    version="0.1.1",
    author="Marjon Godito",
    packages=find_packages(include=['pyevent']),
    long_description=long_description,
    long_description_content_type="text/markdown",
)

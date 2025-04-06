"""
Setup script for LlamaPlastics.
"""

from setuptools import setup, find_packages

# Read the contents of README.md file
with open("README.md", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="llamaplastics-llamasearch",
    version="0.1.0",
    description="LlamaPlastics - A LlamaBench project",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="LlamaSearch AI",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.8",
)

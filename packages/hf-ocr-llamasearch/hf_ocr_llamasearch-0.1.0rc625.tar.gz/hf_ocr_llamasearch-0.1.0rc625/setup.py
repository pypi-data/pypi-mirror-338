
from setuptools import setup, find_packages

"""
Setup module for hf_ocr.

This module provides functionality for the hf_ocr project.
"""

setup(
    name="hf_ocr-llamasearch",
    version="0.1.0rc625",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=[
        "numpy>=1.20.0",
        "pandas>=1.3.0",
        "scikit-learn>=1.0.0",
        "matplotlib>=3.5.0",
        "tqdm>=4.60.0",
        "pyyaml>=6.0.0",
    ],
    author="LlamaSearch AI",
    author_email="nikjois@llamasearch.ai",
    description="LlamaSearch AI Package",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://llamasearch.ai",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
)

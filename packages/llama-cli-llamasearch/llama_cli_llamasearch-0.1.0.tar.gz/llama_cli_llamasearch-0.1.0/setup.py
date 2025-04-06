#!/usr/bin/env python
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="llama-cli-llamasearch",
    version="0.1.0",
    author="LlamaSearch AI",
    author_email="nikjois@llamasearch.ai",
    description="Command-line interface for LlamaSearch.ai tools",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://llamasearch.ai",
    project_urls={
        "Bug Tracker": "https://github.com/llamasearch/llama-cli/issues",
        "Documentation": "https://docs.llamasearch.ai/llama-cli",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
    ],
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.8",
    install_requires=[
        "click>=8.0.0",
        "pyyaml>=6.0",
        "requests>=2.25.0",
        "rich>=10.0.0",
        "typer>=0.4.0",
        "pydantic>=1.8.0",
        "tabulate>=0.8.9",
        "prompt-toolkit>=3.0.0",
        "PyInquirer>=1.0.3",
        "colorama>=0.4.4",
        "keyring>=23.0.0",
    ],
    extras_require={
        "dev": [
            "pytest>=6.0.0",
            "pytest-cov>=2.12.0",
            "black>=21.5b2",
            "flake8>=3.9.2",
            "mypy>=0.812",
            "isort>=5.9.1",
            "tox>=3.24.0",
        ],
        "docs": [
            "sphinx>=4.0.2",
            "sphinx-rtd-theme>=0.5.2",
            "sphinx-click>=3.0.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "llama=llama_cli.main:main",
        ],
    },
    include_package_data=True,
    zip_safe=False,
) 
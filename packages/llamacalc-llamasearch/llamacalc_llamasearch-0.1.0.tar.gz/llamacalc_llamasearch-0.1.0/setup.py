"""
Setup script for LlamaCalc package.
"""

from setuptools import setup, find_packages
import os
import re

# Read the version from the __init__.py file
def get_version():
    init_path = os.path.join("src", "llamacalc", "__init__.py")
    
    with open(init_path, "r") as f:
        init_content = f.read()
    
    # Extract the version using regex
    version_match = re.search(r'__version__\s*=\s*["\']([^"\']+)["\']', init_content)
    if version_match:
        return version_match.group(1)
    
    # Default version if not found
    return "0.1.0"

# Read the long description from README.md
def get_long_description():
    try:
        with open("README.md", "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return "LlamaCalc - Advanced relevance scoring for LLM outputs"

setup(
    name="llamacalc-llamasearch",
    version=get_version(),
    description="Advanced relevance scoring for LLM outputs",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="LlamaSearch AI",
    author_email="nikjois@llamasearch.ai",
    url="https://llamasearch.ai",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.8",
    install_requires=[
        "numpy>=1.20.0",  # Fallback for MLX
    ],
    extras_require={
        "ui": ["rich>=10.0.0"],
        "mlx": ["mlx>=0.0.5"],  # For Apple Silicon acceleration
        "dev": [
            "pytest>=7.0.0",
            "black>=23.0.0",
            "isort>=5.12.0",
            "mypy>=1.0.0",
            "flake8>=6.0.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "llamacalc=llamacalc.cli:main",
        ],
    },
    keywords="llm, relevance, scoring, nlp, evaluation, mlx",
    project_urls={
        "Bug Reports": "https://github.com/llamasearch/llamacalc/issues",
        "Source": "https://github.com/llamasearch/llamacalc",
    },
) 
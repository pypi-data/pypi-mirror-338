from setuptools import setup, find_packages
import os
import sys

# Add the current directory to sys.path
sys.path.insert(0, os.path.abspath('.'))

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="wandb-logger",
    version="0.1.1",
    author="SabaPivot",
    author_email="careforme.dropout@gmail.com",  # Replace with your email
    description="A command-line tool for managing Weights & Biases (W&B) training logs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SabaPivot/wandb-logger",
    project_urls={
        "Bug Tracker": "https://github.com/SabaPivot/wandb-logger/issues",
    },
    packages=find_packages(),
    include_package_data=True,
    license="MIT",
    install_requires=[
        "click>=8.0.0",
        "wandb>=0.12.0",
        "rich>=10.0.0",
        "pandas>=1.0.0",
        "matplotlib>=3.0.0",
        "seaborn>=0.11.0",
    ],
    entry_points={
        "console_scripts": [
            "wandb-logger=wandb_logger_app.main:cli",
        ],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.8",
) 
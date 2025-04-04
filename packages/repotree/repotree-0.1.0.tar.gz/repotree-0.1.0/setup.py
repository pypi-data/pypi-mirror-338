from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="repotree",
    version="0.1.0",
    author="Eng-Elias",
    author_email="elias@engelias.website",
    description="A CLI tool for displaying files tree with Git integration",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Eng-Elias/repotree",
    packages=find_packages(),
    classifiers=[
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
    ],
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "repotree=repotree.main:main",
        ],
    },
)

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="atomorph",
    version="0.3.0",
    author="yyxwjq",
    author_email="yyxwjq@example.com",
    description="A powerful tool for converting and manipulating crystal structure files",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yyxwjq/atomorph",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering :: Physics",
        "Topic :: Scientific/Engineering :: Chemistry",
    ],
    python_requires=">=3.7",
    install_requires=[
        "numpy>=1.19.0",
        "ase>=3.21.0",
        "tqdm>=4.65.0",
    ],
    entry_points={
        "console_scripts": [
            "conv=atomorph.converter.cli:main",
        ],
    },
    package_data={
        "atomorph": ["py.typed"],
    },
)
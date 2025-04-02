#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name="trueroll",
    version="0.2.1",
    description="A ten-pin bowling simulation library for modeling games",
    author="Michael Borck",
    author_email="michael@borck.me",
    url="https://github.com/michael-borck/trueroll",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.10",
    install_requires=[
        "numpy>=1.26.4",
        "typer>=0.9.0",
        "rich>=13.7.0",
        "textual>=0.52.1",
        "python-fasthtml>=0.8.2",
    ],
    entry_points={
        "console_scripts": [
            "trueroll=trueroll.cli.commands:app",
        ],
    },
)
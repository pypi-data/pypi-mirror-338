#!/usr/bin/env python3

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="cronflow",
    version="0.1.0",
    author="Xileven",
    author_email="hi@bringyouhome.org",
    description="A Python package for controlling cron job execution",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jinwenliu/cronflow",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: System :: Systems Administration",
        "Topic :: Utilities",
    ],
    python_requires=">=3.9",
    keywords="cron, scheduling, job control, automation",
)

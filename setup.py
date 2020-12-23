#
# Copyright (c) 2020 Kian Cross
#

from setuptools import setup

import pixy.metadata

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="pixy",
    author="Kian Cross",
    author_email="kian@kiancross.co.uk",
    url="https://github.com/kiancross/pixy/",
    version=pixy.metadata.version,
    licence="MIT",
    packages=["pixy", "pixy.colours"],
    description="Add colour and style to terminal text",
    long_description=long_description,
    long_description_content_type="text/markdown",
    python_requires="~=3.6",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)

#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
from setuptools import setup

if sys.argv[-1] == "publish":
    os.system("python setup.py sdist upload")
    sys.exit()

setup(
    name="my_functions",
    version="1.0",
    author="Maude Charmetant",
    author_email="mcharmetant@astro.uni-bonn.de",
    packages=["my_functions"],
    url="https://github.com/AIfA-Radio/my_functions",
    license="MIT License",
    description=("Python package containing my functions"),
    long_description=open("README.rst").read(),
    package_data={"my_functions": ["LICENSE"]},
    include_package_data=True,
    install_requires=["numpy", "healpy"], #list all the package your functions need.
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
    ],
    zip_safe=False,
)

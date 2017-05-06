#!/usr/bin/env python3
from setuptools import setup

#setup the package as the default application

setup(
    name = 'videowatcher',
    packages = ['videowatcher'],
    include_package_data = True,
    install_requires = [
        'flask',
    ],
)

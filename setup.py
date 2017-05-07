#!/usr/bin/env python3
from setuptools import setup

#setup the package as the default application

setup(
    name = 'videowatcher',
    packages = ['videowatcher'],
    version = '1.0.0',
    author = 'Gabriel Boorse',
    description = 'Shared video playback package',
    include_package_data = True,
    install_requires = [
        'flask',
    ],
)

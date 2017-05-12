#!/usr/bin/env bash

### SERVER SETUP SCRIPT
### Complete environment setup for server
### Make sure virtualenv, setuptools, and python3.5 are installed
echo '--- SERVER SETUP ---'

#this is the path to the python binary
PYPATH="$(which python3.5)"
echo $PYPATH

#make sure it's fresh
rm -rf venv

#create the python virtual environment
virtualenv --python=$PYPATH venv #or something like this

#activate the virtual environment
. venv/bin/activate

#make sure all packages are installed properly

#this installs the "videowatcher" package (run setup.py)
pip3 install -e .

#install packages in requirements list
pip3 install -r requirements.txt

#deactivate the python virtual environment
deactivate

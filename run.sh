#!/usr/bin/env bash

### SERVER SETUP SCRIPT
### Tested on Fedora 25 and Debian Jessie
### be sure to have python3, pip3, and virtualenv installed


#set environment variables
export SECRET_KEY=328626694831757786207988970988
export FLASK_APP=videowatcher
export FLASK_DEBUG=true ##set to false in production

#create the python virtual environment
virtualenv venv

#activate the virtual environment
. venv/bin/activate

#makes sure all packages are installed properly
#this includs the "videowatcher" package
#this also calls the setup.py script
pip3 install -e .
pip3 install -r requirements.txt

#run the actual server on localhost
flask run --host=0.0.0.0

#usually a Ctrl+C here

#deactivate the python virtual environment
deactivate

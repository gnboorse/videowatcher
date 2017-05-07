#!/usr/bin/env bash

###
### Server setup script
### 


#set environment variables
export SECRET_KEY=328626694831757786207988970988
export FLASK_APP=videowatcher
export FLASK_DEBUG=true ##set to false in production

#start python virtual environment
#(assumes we've already made the virtual environment)
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

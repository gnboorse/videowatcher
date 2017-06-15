#!/usr/bin/env bash

### SERVER RUN SCRIPT
### Use this to start the development environment server

##call the setup script just to be sure
if [ ! -d venv/ ]; then
    . setup.sh
fi

#export the package environment variable
export FLASK_APP=videowatcher

#activate our virtual environment
. venv/bin/activate

#run the server
flask run --host=0.0.0.0

#once we're done, deactivate
#deactivate

#!/usr/bin/env python3

from videowatcher import app
from videowatcher import winf
from flask import url_for, render_template
import json

#views for this flask application

@app.route('/')
def index():
    return render_template('index.htm', w=winf)

'''    
#json handler
@app.route('/status/<'
def getStatus():
'''

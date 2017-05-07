#!/usr/bin/env python3

from . import app, winf, db
from .models import watchuser, watchsession
from flask import url_for, render_template

import json

#views for this flask application

@app.route('/')
def index():
    newuser = watchuser(username='Gabriel', email='gnboorse@gmail.com')
    db.session.add(newuser)
    db.session.commit()
    
    s = str(watchuser.query.filter_by(username='Gabriel').first())
    return render_template('index.htm', w=winf, test_var = s)

@app.route('/login', methods = ['GET', 'POST'])
def login():
    return 'hello login!'
'''    
#json handler
@app.route('/status/<'
def getStatus():
'''

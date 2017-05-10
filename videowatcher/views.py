#!/usr/bin/env python3

from . import app, winf, db, login_manager
from .models import watchuser, watchsession
from .forms import LoginForm 
from flask import url_for, render_template, redirect, request, url_for, flash
from flask_login import login_required, login_user

import json

#views for this flask application

#home page
@app.route('/')
def index():

    return render_template('index.htm', w=winf)


#login page makes sure login is validated
#otherwise it will flash a response back
@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = watchuser.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            return redirect(request.args.get('next') or url_for('index'))
        flash('Invalid username or password.')
    return render_template('login.htm', w = winf, form=form)


#basic about page
@app.route('/about')
def about():
    return render_template('about.htm', w=winf)


#HTML5 player
@app.route('/session/')
@app.route('/session/<sid>')
@login_required
def session(sid=None):
    
    if sid != None:
        session = watchsession.query.filter_by(id=sid).first()
        if session != None:
        
            return render_template('session.htm', w = winf, session = session)
        #else: fail gracefully
    return redirect(url_for('index')) #change this to be sessions list page


#this is the main JSON handler for synchronizing playback
@app.route('/session_handle/', methods=['GET', 'POST'])
@app.route('/session_handle/<sid>', methods=['GET', 'POST'])
@login_required
def session_handle(sid=None):
    if sid != None:
        session = watchsession.query.filter_by(id=sid).first()
        if session != None:
            return repr(session)
    return 'nothing'
    

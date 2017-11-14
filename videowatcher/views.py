#!/usr/bin/env python3

from . import app, winf, db, login_manager
from .models import watchuser, watchsession
from .forms import LoginForm, PasswordChangeForm, NewUserForm, NewSessionForm
from flask import url_for, render_template, redirect, request, url_for, flash
from flask_login import login_required, login_user, logout_user, current_user

import json


#views for this flask application

#home page
@app.route('/')
def index():
    sessionList = watchsession.query.all() #all sessions in database
    sUrl = url_for('session')
    return render_template('index.htm', w=winf, s_url = sUrl, sessions = sessionList)


#login page makes sure login is validated
#otherwise it will flash a response back
@app.route('/login', methods = ['GET', 'POST'])
def login():
    #create the loginform from forms.py
    form = LoginForm()
    
    if current_user.is_authenticated:
        #if they're already signed in, go to the list
        return redirect(url_for('session_list'))
        
    if form.validate_on_submit():
        user = watchuser.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            return redirect(request.args.get('next') or url_for('session_list'))
        flash('Invalid username or password.', 'error')
    return render_template('login.htm', w = winf, form=form)

#handle logout
@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('index'))

#basic about page
@app.route('/about')
def about():
    sessionList = watchsession.query.all() #all sessions in database
    sUrl = url_for('session')
    return render_template('about.htm', w=winf, s_url = sUrl, sessions = sessionList)


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

#directory of all open sessions to join
#automatically generates a list of all links
@app.route('/session_list')
@login_required
def session_list():
    sessionList = watchsession.query.all() #all sessions in database
    sUrl = url_for('session')
    return render_template('sessions.htm', w = winf, sessions = sessionList, s_url = sUrl)

@app.route('/newsession', methods=['GET', 'POST'])
@login_required
def new_session():
    sessionList = watchsession.query.all() #all sessions in database
    sUrl = url_for('session')
    
    form = NewSessionForm()
    
    if form.validate_on_submit():
        #we have a valid form submission

        new_session_ = watchsession(title=form.title.data, video_src=form.video_link.data, is_paused=True, time=0)
        db.session.add(new_session_)
        db.session.commit()

        return redirect(url_for('session_list'))
    
    
    return render_template('newsession.htm', w = winf, sessions = sessionList, s_url = sUrl, form = form)

#this is the main JSON handler for synchronizing playback
@app.route('/session_handle/', methods=['GET', 'POST'])
@app.route('/session_handle/<sid>', methods=['GET', 'POST'])
@login_required
def session_handle(sid=None):
    if sid != None:
        session = watchsession.query.filter_by(id=sid).first()
        if session != None:
            if request.method =='POST' and request.is_json:
                #update
                myjson = request.get_json()
                
                # if isinstance(myjson['is_paused'], bool) and isinstance(myjson['time'], int):
                session.time = myjson['time']
                session.is_paused = myjson['is_paused']
                db.session.commit()
            else:
                return repr(session)
    return 'nothing'
    
#settings directory for 
@app.route('/settings', methods=['GET', 'POST'])
@login_required
def settings():
    sessionList = watchsession.query.all() #all sessions in database
    sUrl = url_for('session')
    form = PasswordChangeForm()
    
    # we have a validated form
    if form.validate_on_submit():
        #this is the current user object
        user = watchuser.query.filter_by(email=current_user.email).first()
        #make sure the current user validates themself
        if user is not None and user.verify_password(form.old_password.data):
            #we have a valid authentication
            if form.new_password.data == form.confirm.data:
                #new passwords are equal, so set password to new password
                user.password = form.new_password.data
                db.session.add(user) #this is basically an SQL insert
                db.session.commit()
                #should flash success
            else:
                flash('Password changed successfully.', 'success')
        else:
            flash('Passwords do not match.', 'error')
    else:
        flash('Invalid password.', 'error')
    
    return render_template('settings.htm', w = winf, form = form, sessions = sessionList, s_url = sUrl)
    
#add user page
@app.route('/adduser', methods=['GET', 'POST'])
@login_required
def adduser():
    sessionList = watchsession.query.all() #all sessions in database
    sUrl = url_for('session')
    
    #administrators only
    if not current_user.is_admin:
        return redirect(url_for('settings'))
    
    form = NewUserForm()
    
    if form.validate_on_submit():
        new_user = watchuser(email=form.email.data, username=form.email.data, password=form.password.data, is_admin=form.administrator.data)
        db.session.add(new_user)
        db.session.commit()
        flash("User created successfully.")
    
    return render_template('adduser.htm', w = winf, sessions = sessionList, s_url = sUrl, form = form)
    
#users deletion page (lists all users)
@app.route('/users', methods=['GET','POST'])
@login_required
def users():
    sessionList = watchsession.query.all() #all sessions in database
    usersList = watchuser.query.all() #all sessions in database
    sUrl = url_for('session')
    cUrl = url_for('config')
    #administrators only
    if not current_user.is_admin:
        return redirect(url_for('settings'))
        
    return render_template('users.htm', w = winf, users = usersList, sessions = sessionList, s_url = sUrl, c_url = cUrl)
    
@app.route('/config', methods=['GET', 'POST'])
@login_required
def config():
    sessionList = watchsession.query.all() #all sessions in database
    sUrl = url_for('session')
    
    #administrators only
    if not current_user.is_admin:
        return redirect(url_for('settings'))
        
    return render_template('config.htm', w = winf, sessions = sessionList, s_url = sUrl)
    

#!/usr/bin/env python3

import os

basedir = os.path.abspath(os.path.dirname(__file__))

#init for the videowatcher package

from flask import Flask
from videowatcher.watchinfo import watchinfo
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)

#assuming the application has been started correctly,
#secret key has already been added as an environment variable
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

#setup SQLAlchemy configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

#uses Flask-Login to manage login session
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'login'

#create main database object
db = SQLAlchemy(app)

#import database models
from .models import watchuser, watchsession

#reset everything
db.drop_all() #eventually use migration tools
db.create_all()

winf = watchinfo()


import videowatcher.views


#!/usr/bin/env python3

#package initialization creates the main flask app
#decided against using Blueprints here because
#they would introduce more complexity than is necessary

import os

basedir = os.path.abspath(os.path.dirname(__file__))

#init for the videowatcher package

from flask import Flask
from videowatcher.watchinfo import watchinfo
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bootstrap import Bootstrap

#here's the app
app = Flask(__name__)

#assuming the application has been started correctly,
#secret key has already been added as an environment variable
app.config['SECRET_KEY'] = '328626694831757786207988970988'

#this is for making forms (see forms.py)
bootstrap = Bootstrap(app)

#setup SQLAlchemy configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#uses Flask-Login to manage login session
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'login'
login_manager.init_app(app)
#create main database object
db = SQLAlchemy(app)

#import database models
from .models import watchuser, watchsession

#reset everything
db.drop_all() #eventually use migration tools
db.create_all()
newuser = watchuser(username='gnboorse@gmail.com', email='gnboorse@gmail.com', password="password", is_admin=True)

newsession = watchsession(title='test session', video_src='http://julie.gnboor.se/SPACE.mp4', is_paused=True, time=120)
db.session.add(newuser)

db.session.add(newsession)
db.session.commit()

#app info passed to all templates
winf = watchinfo()

#register application views on app
import videowatcher.views


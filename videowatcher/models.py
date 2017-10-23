#classes that implement SQLAlchemy models

from . import db, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
import json


#database model for storing user information
class watchuser(UserMixin, db.Model):
    __tablename__ = 'watchusers'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    email = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    is_admin = db.Column(db.Boolean)
    
    # password hashing and checking through werkzeug
    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')
        
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)
        
    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    #string representation
    def __repr__(self):
        return '<watchuser %r>' % self.username
        
        
#user loader required for doing flask-login
@login_manager.user_loader
def load_user(user_id):
    return watchuser.query.get(int(user_id))
    
#database model for storing session information
class watchsession(db.Model):
    __tablename__ = 'watchsessions'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), index=True)
    video_src = db.Column(db.String(256))
    is_paused = db.Column(db.Boolean)
    time = db.Column(db.Integer)
    
    #add created_by as watchuser
    
    #modified to provide JSON representation
    def __repr__(self): 
        session_dict = {}
        session_dict["id"] = self.id
        session_dict["title"] = self.title
        session_dict["video_src"] = self.video_src
        session_dict["is_paused"] = self.is_paused
        session_dict["time"] = self.time
        #add created_by (just the name)        
        return json.dumps(session_dict)
        

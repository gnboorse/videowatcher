from flask_wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Required, Email, Length, EqualTo, URL
from .models import watchuser

#this is the form used to authorize users 
class LoginForm(Form):
    email = StringField('Email', validators=[Required(), Length(1, 64), Email()])
    password = PasswordField('Password', validators=[Required()])
    remember_me = BooleanField('Keep me logged in')
    
    submit = SubmitField('Log In')
    
    
#default login form
class PasswordChangeForm(Form):
    #email = StringField('Email', validators = [Required(), Length(1, 64), Email()])
    old_password = PasswordField('Old Password', validators=[Required()])
    new_password = PasswordField('New Password', validators=[Required()])
    confirm = PasswordField('Confirm Password', validators = [Required(),  EqualTo('new_password', message='Passwords must match')])
    
    submit = SubmitField('Submit')

#form used to create a new user
class NewUserForm(Form):
    email = StringField('Email', validators=[Required(), Length(1, 64), Email()])
    #username is email address
    password = PasswordField('Password', validators=[Required()])
    confirm = PasswordField('Confirm Password', validators = [Required(),  EqualTo('password', message='Passwords must match')])
    administrator = BooleanField('Administrative user')
    
    submit = SubmitField('Submit')

#form used ot create a new session
class NewSessionForm(Form):
    title = StringField('Session Title', validators=[Required(), Length(1, 120)])
    video_link = StringField('Video URL', validators=[Required(), URL(require_tld=True, message='Provide a valid URL')])
    # add more here?
    submit = SubmitField('Submit')

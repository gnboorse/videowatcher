from flask_wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Required, Email, Length, EqualTo
from .models import watchuser

#this is the form used to authorize users 
class LoginForm(Form):
    email = StringField('Email', validators=[Required(), Length(1, 64), Email()])
    password = PasswordField('Password', validators=[Required()])
    remember_me = BooleanField('Keep me logged in')
    
    submit = SubmitField('Log In')
    
    
        
class PasswordChangeForm(Form):
    #email = StringField('Email', validators = [Required(), Length(1, 64), Email()])
    old_password = PasswordField('Old Password', validators=[Required()])
    new_password = PasswordField('New Password', validators=[Required()])
    confirm = PasswordField('Confirm Password', validators = [Required(),  EqualTo('new_password', message='Passwords must match')])
    
    submit = SubmitField('Submit')

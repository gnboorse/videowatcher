#this contains a class that gets basic runtime info about the application
#from videowatcher import app
from flask import url_for, render_template

class watchinfo:
    def __init__(self):
        pass
        
    @property
    def jquery(self):
        return url_for('static', filename='jquery-3.2.1.min.js')
    
    @property
    def appTitle(self):
        return 'videowatcher'
    

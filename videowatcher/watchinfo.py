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
        
    @property
    def semanticui(self):
        return url_for('static', filename='semantic/dist/semantic.min.css')
        
    @property
    def semanticjs(self):
        return url_for('static', filename='semantic/dist/semantic.min.js')
        
    @property
    def videojs(self):
        return "http://vjs.zencdn.net/5.19.2/video-js.css"
     
    @property
    def js(self):
        return url_for('static', filename='site.css')
        
    @property
    def css(self):
        return url_for('static', filename='site.js')

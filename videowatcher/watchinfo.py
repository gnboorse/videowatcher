#this contains a class that gets basic runtime info about the application

from flask import url_for

class watchinfo:
    def __init__(self):
        pass
    
    #link to jquery package
    @property
    def jquery(self):
        return url_for('static', filename='jquery-3.2.1.min.js')
    
    #title of the app
    @property
    def appTitle(self):
        return 'videowatcher'
    
    #link to semantic ui css (not used?)
    @property
    def semanticui(self):
        return url_for('static', filename='semantic/dist/semantic.min.css')
    
    #link to semantic js (not used?)
    @property
    def semanticjs(self):
        return url_for('static', filename='semantic/dist/semantic.min.js')
    
    #link to video js source (put at bottom of session template)
    @property
    def videojs(self):
        return "http://vjs.zencdn.net/5.19.2/video.js"
    
    #link to video css (top of session template)
    @property
    def videocss(self):
        return "http://vjs.zencdn.net/5.19.2/video-js.css"
    
    #backwards compatibility for internet explorer
    @property
    def videojs_ie(self):
        return "http://vjs.zencdn.net/ie8/1.1.2/videojs-ie8.min.js"
    
    #main js library for polling server
    @property
    def js(self):
        return url_for('static', filename='site.js')
    
    #main css for session styles
    @property
    def css(self):
        return url_for('static', filename='site.css')
    
    #link to help user diagnose html5 issues
    @property
    def javascript_link(self):
        return "http://videojs.com/html5-video-support/"
    
    #link to python logo
    @property
    def pythonpowered(self):
        return 'https://www.python.org/static/community_logos/python-powered-w-100x40.png'
        
    #link to github project
    @property
    def github(self):
        return 'https://github.com/gnboorse/videowatcher'

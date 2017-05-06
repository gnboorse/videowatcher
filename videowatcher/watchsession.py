# class watchsession holds an individual video watching session
# has an id and offset (current time in seconds of the video)
# users can be added to this session so that when they poll the page
# they can sync with the curent time of the video

import json

class watchsession:
    
    __sid = None
    __filename = None
    __offsetseconds = None
    __ispaused = None
    
    def __init__(self, new_sid = None, new_filename = None, new_offsetseconds = None, new_ispaused = None):
        self.__sid = new_sid
        self.__filename = new_filename
        self.__offsetseconds = new_offsetseconds
        self.__ispaused = new_ispaused
        
    ## session ID property (with setter)
    @property
    def sid(self):
        return self.__sid
        
    @sid.setter
    def sid(self, new_sid):
        self.__sid = new_sid
    
    ## session filename property (with setter)
    @property
    def filename(self):
        return self.__filename
        
    @filename.setter
    def sid(self, new_filename):
        self.__filename = new_filename
    
    ## session offset (with setter)
    @property
    def offsetseconds(self):
        return self.__offsetseconds
        
    @offsetseconds.setter
    def sid(self, new_offsetseconds):
        self.__offsetseconds = new_offsetseconds
        
    ## session paused flag (with setter)
    @property
    def ispaused(self):
        return self.__ispaused
        
    @ispaused.setter
    def sid(self, new_ispaused):
        self.__ispaused = new_ispaused
        
    
    

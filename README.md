# About

This is a fairly basic web application for shared video streaming, meaning that users on multiple endpoints can watch an mp4 or webm file together synchronously and use a chat overly to discuss the video while watching.

This project does not endorse illegal aquisition of pirated media. The software is offered as a free and fun source of entertainment under the GNU Public License.

Everything should run out of the box 


# Installation

Currently, videowatcher is only compatible with Unix-based systems. 

## Prerequisites

To make the magic happen, videowatcher relies on a complex package management system wrapped inside a virtual environment.

Make sure you have installed **python3** and **virtualenv** using your package manager of choice. For example on Fedora-based systems:

~~~
sudo dnf install python3
sudo dnf install python-virtualenv
~~~

Also install pip3 by downloading [get-pip.py](https://bootstrap.pypa.io/get-pip.py "get-pip.py") and installing like so:

~~~
sudo python3 get-pip.py
~~~

## Running the server

Once you've installed the prerequisites, navigate into the base directory and run

~~~
./run.sh
~~~

Everything should be live at http://localhost:5000/

# This is very, very much a work in progress

See the Trello board here: https://trello.com/b/99Q4Ur4Q


# Links for research:

## Javascript

* http://stackoverflow.com/questions/31645307/how-to-play-mp4-video-all-major-browsers
* https://www.w3schools.com/html/html5_video.asp
* http://stackoverflow.com/questions/18670728/how-to-embed-video-using-html5-with-local-file
* http://stackoverflow.com/questions/8885701/play-local-hard-drive-video-file-with-html5-video-tag
* http://jsfiddle.net/dsbonev/cCCZ2/embedded/result,js,html,css/
* https://www.w3schools.com/tags/av_prop_currenttime.asp
* http://stackoverflow.com/questions/5981427/start-html5-video-at-a-particular-position-when-loading
* https://davidwalsh.name/html5-video-current-time
* https://davidwalsh.name/html5-video-duration


## Python

* http://stackoverflow.com/questions/682504/what-is-a-clean-pythonic-way-to-have-multiple-constructors-in-python
* http://www.python-course.eu/python3_properties.php
* http://flask.pocoo.org/docs/0.12/installation/#virtualenv

## Flask

* http://stackoverflow.com/questions/11994325/how-to-divide-flask-app-into-multiple-py-files
* http://flask.pocoo.org/docs/0.12/patterns/packages/
* http://flask.pocoo.org/docs/0.12/blueprints/#blueprints
* http://flask.pocoo.org/docs/0.12/quickstart/#static-files
* http://jinja.pocoo.org/docs/2.9/templates/
* http://stackoverflow.com/questions/31727367/call-a-python-function-from-a-jinja-template
* http://flask.pocoo.org/docs/0.12/quickstart/



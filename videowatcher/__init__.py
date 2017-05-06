#!/usr/bin/env python3

#init for the videowatcher package

from flask import Flask
from videowatcher.watchinfo import watchinfo

app = Flask(__name__)
winf = watchinfo()


import videowatcher.views


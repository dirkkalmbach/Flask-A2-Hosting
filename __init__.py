# Standard library imports
import os
import sys
import datetime

# Third party imports  
from flask import Flask, request, render_template, redirect, url_for, flash

# Local application importsimport sys
from pathlib import Path
sys.path.append(str(Path('.').absolute().parent))

from config import BaseConfig, DevelopmentConfig

app = Flask(__name__)

@app.route("/")
def index():
	return "{} <h1>Hello Planet from A2 </h1>".format(datetime.datetime.now())


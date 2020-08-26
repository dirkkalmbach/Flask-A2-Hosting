# Standard library imports
import os
import datetime

# Third party imports 
from flask import Flask

project_root = os.path.dirname(os.path.realpath('__file__'))
template_path = os.path.join(project_root, 'templates')
static_path = os.path.join(project_root, 'static')

# Local application imports

# from ../
from config import BaseConfig, DevelopmentConfig

# from /application'
from .forms import *
from .models import *


def create_app():
	app = Flask(
	    __name__,
	    template_folder = template_path,
	    static_folder = static_path
	)
	app.config.from_object(BaseConfig)

	return app

app = create_app()

# routes always AFTER app instance created
from . import routes
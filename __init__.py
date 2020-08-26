from flask import Flask
import datetime

app = Flask(__name__)

@app.route("/")
def index():
	return "{} <h1>Hello Planet from A2 </h1>".format(datetime.datetime.now())

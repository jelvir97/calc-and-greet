# Put your app in here.
from flask import Flask, request
from operations import *

app = Flask(__name__)

@app.route('/add')
def add_request():
    """Handle add request"""
    a = int(request.args["a"])
    b = int(request.args["b"])

    return f"{a} plus {b} equals {add(a,b)}"


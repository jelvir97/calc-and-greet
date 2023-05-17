# Put your app in here.
from flask import Flask, request
from operations import *

app = Flask(__name__)

@app.route('/math/<operation>')
def math_operation(operation):
    """ Do math on a and b"""
    a = int(request.args["a"])
    b = int(request.args["b"])
    funcs = {'div':div, 'add': add, 'sub': sub, 'mult':mult}
    return f'{funcs[operation](a,b)}'

@app.route('/add')
def add_request():
    """Handle add request"""
    a = int(request.args["a"])
    b = int(request.args["b"])

    return f"{a} plus {b} equals {add(a,b)}"

@app.route('/sub')
def sub_request():
    """Handle subtract request"""
    a = int(request.args["a"])
    b = int(request.args["b"])

    return f"{a} minus {b} equals {sub(a,b)}"

@app.route('/mult')
def mult_request():
    """Handle multiply request"""
    a = int(request.args["a"])
    b = int(request.args["b"])

    return f"{a} times {b} equals {mult(a,b)}"

@app.route('/div')
def div_request():
    """Handle divide request"""
    a = int(request.args["a"])
    b = int(request.args["b"])

    return f"{a} divided by {b} equals {div(a,b)}"

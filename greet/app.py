from flask import Flask ,request

app = Flask(__name__)

@app.route('/welcome')
def welcome():
    """Returns 'Welcome' from /welcome request"""
    return '<h1>Welcome</h1>'

@app.route('/welcome/home')
def welcome():
    """Returns 'Welcome Home' from /welcome/home request"""
    return '<h1>Welcome Home</h1>'

@app.route('/welcome/back')
def welcome():
    """Returns 'Welcome back' from /welcome/back request"""
    return '<h1>Welcome Back</h1>'
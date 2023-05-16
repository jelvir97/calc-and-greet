from flask import Flask ,request

app = Flask(__name__)

@app.route('/welcome')
def welcome():
    """Returns 'Welcome' from /welcome request"""
    return '<h1>Welcome</h1>'


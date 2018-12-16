from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    """
    Print response body
    """
    return 'Hello World!'

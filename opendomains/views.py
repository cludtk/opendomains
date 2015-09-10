__author__ = 'cvl'

from opendomains import app

@app.route('/')
def index():
    return 'Hello World!'
import os
from flask import send_from_directory, render_template, request

__author__ = 'cvl'

from opendomains import app

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/<path:path>/<file>')
def dynamic_files(path, file):
    abs_path = os.path.dirname(os.path.abspath(__file__))
    od_path = abs_path.replace('/' + os.path.basename(abs_path), '')
    path_with_file = od_path + '/templates/' + path

    response = send_from_directory(path_with_file, file, as_attachment=True)
    return response
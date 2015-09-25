import os
from flask import send_from_directory, render_template, request

__author__ = 'cvl'

from opendomains import app

@app.route('/')
def index():
    return render_template("index.html")

def get_abs_path():
    abs_path = os.path.dirname(os.path.abspath(__file__))
    current_folder = '/' + os.path.basename(abs_path)
    abs_path = abs_path[0:] + abs_path[:len(abs_path)-len(current_folder)]
    return abs_path + '/templates/'

@app.route('/<path:path>/<file>')
def get_file_in_folder(path, file):
    path_to_file = get_abs_path() + path
    response = send_from_directory(path_to_file, file, as_attachment=True)
    return response

@app.route('/<file>')
def get_file(file):
    response = send_from_directory(get_abs_path(), file, as_attachment=True)
    return response
import os
from flask import send_from_directory, render_template

__author__ = 'cvl'

from opendomains import app

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/<path:url_path>')
def content(url_path):
    length = len(url_path) - 1

    file_name = ''
    path = ''
    while 1:
        if not (url_path[length] == '/') | (length == 0):
            file_name = file_name[:0] + url_path[length] + file_name[0:]
            length -= 1
        else:
            break
    path = url_path.replace(file_name, '')

    abs_path = os.path.dirname(os.path.abspath(__file__))
    od_path = abs_path.replace('/' + os.path.basename(abs_path), '')

    path_with_file = od_path + '/templates/' + path
    response = send_from_directory(path_with_file, file_name, as_attachment=True)
    return response
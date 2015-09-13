__author__ = 'cvl'
from opendomains import app
import sys

app_port = 80
app_ip = '172.31.27.41'
app_debug = False

amount_args = len(sys.argv)

def run_app(ip, port, debug):
    app.run(host=ip, port=port, debug=debug)

def setPort(p):
    index = sys.argv.index(p)
    global app_port
    app_port = int(sys.argv[index+1])

def setIP(i):
    index = sys.argv.index(i)
    global app_ip
    app_ip = str(sys.argv[index+1])

def setDebug(d):
    index = sys.argv.index(d)
    global app_debug
    app_debug = bool(sys.argv[index+1])

def switch_args(argument):
    if argument == "-i":
        setIP(argument)
    if argument == "-p":
        setPort(argument)
    if argument == "-d":
        setDebug(argument)

if len(sys.argv) > 1:
    for argument in sys.argv:
        if not argument == sys.argv[0]:
            switch_args(argument)

run_app(app_ip, app_port, app_debug)

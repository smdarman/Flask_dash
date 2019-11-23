from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.serving import run_simple
from app import app as app1
from app2 import app as app2
from flask import Flask
from flaskblog import flask_app



application = DispatcherMiddleware(flask_app, {
    '/app1': app1.server,
    '/app2': app2.server

})

#Alternatively, you can use the Werkzeug development server (which is not suitable for production) to run the app
if __name__ == '__main__':
    run_simple('localhost', 8050, application)
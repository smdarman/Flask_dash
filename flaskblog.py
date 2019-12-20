
from flask import Flask, render_template, url_for

import flask


flask_app = flask.Flask(__name__)


@flask_app.route('/')
def index():
    return render_template('home.html')





@flask_app.route("/about")
def about():
    return render_template('about.html', title='About')



@flask_app.route("/home")
def home():
    return render_template('home.html')



@flask_app.route("/stock")
def stock():
    return render_template('Stock_chart.html', title= 'stock')







#
# if __name__ == "__main__":
#     flask_app.run_server(debug=True, port=5006)


if __name__ == '__main__':
    flask_app.run(debug=True)

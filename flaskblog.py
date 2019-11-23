
from flask import Flask, render_template, url_for

import flask







flask_app = flask.Flask(__name__)










@flask_app.route('/')
def index():
    return 'Hello Flask app'





@flask_app.route("/about")
def about():
    return render_template('about.html', title='About')



@flask_app.route("/home")
def home():
    return render_template('home.html')






# posts = [
#     {
#         'author': 'Salaiman darman',
#         'title': 'Blog Post 1',
#         'content': 'first post content',
#         'date_posted': 'april 20, 2019',
#     },
#     {
#         'author': 'janckie dee',
#         'title': 'Blog Post 2',
#         'content': 'second post content',
#         'date_posted': 'april 21s32'
#                        ', 2019',
#     }
#




#
# if __name__ == "__main__":
#     flask_app.run_server(debug=True, port=5006)


if __name__ == '__main__':
    flask_app.run(debug=True)

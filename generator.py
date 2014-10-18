#!/usr/bin/env python

from flask import Flask
from flask import render_template

import markdown

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/blog/post/')
def post():
    return render_template('post.html', post_content="HELLO!")

if __name__ == '__main__':
    app.run(port=8000)

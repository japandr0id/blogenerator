#!/usr/bin/env python

from flask import Flask
from flask import render_template

import markdown

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(port=8000)

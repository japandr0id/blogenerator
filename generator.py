#!/usr/bin/env python

from flask import Flask
from flask import render_template
from werkzeug import cached_property

import markdown
import os

POSTS_FILE_EXTENSION = '.md'

app = Flask(__name__)

class Post(object):
    def __init__(self, path):
        self.path = path

    @cached_property
    def html(self):
        with open(self.path, 'r') as fin:
            content = fin.read().split('\n\n', 1)[1].strip()
        return markdown.markdown(content)

    def _initialize_metadata(self):
        content = ''
        with open(self.path, 'r') as fin:
            for line in fin:
                if not line.strip():
                    break
                content += line
        self.__dict__.update(yaml.load(content))

@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/blog/<path:path>')
def post(path):
    path = os.path.join('posts', path + POSTS_FILE_EXTENSION)
    post = Post(path)
    return render_template('post.html', path=path)

if __name__ == '__main__':
    app.run(port=8000, debug=True)

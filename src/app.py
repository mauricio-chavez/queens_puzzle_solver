"""Flask app"""

import os

from flask import Flask, render_template

from task_queue.tasks import add


app = Flask(__name__)
app.config['DEBUG'] = os.environ.get('FLASK_DEBUG', False)


@app.route('/')
def index():
    """Asks for a n problem"""
    add.delay(4,4)
    return render_template('index.html')

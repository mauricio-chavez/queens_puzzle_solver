"""Flask app"""

import os

from flask import Flask, render_template


app = Flask(__name__)
app.config['DEBUG'] = os.environ.get('FLASK_DEBUG', False)


@app.route('/')
def index():
    """Asks for a n problem"""
    return render_template('index.html')

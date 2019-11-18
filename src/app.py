"""Flask app"""

import os

from flask import Flask, render_template, request, redirect, url_for

from database import session_factory, create_solution_query
from database.models import SolutionQuery


app = Flask(__name__)
app.config['DEBUG'] = os.environ.get('FLASK_DEBUG', False)


@app.route('/')
def index():
    """Asks for a n problem"""
    return render_template('index.html')


@app.route('/solutions')
def solutions():
    """Asks for a n problem"""
    n = request.args.get('n')
    if not n:
        return redirect(url_for('index'))
    n = int(n)
    session = session_factory()

    query = session.query(SolutionQuery).filter_by(n=n)

    if query.count() == 0:
        status = 0
        create_solution_query(n, 1)
    else:
        status = query.first().status

    return render_template('solutions.html', status=status, n=n)

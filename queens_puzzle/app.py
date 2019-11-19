"""Flask app"""

import os
from threading import Thread

from flask import Flask, render_template, request, redirect, url_for

from database import session_factory, create_solution_query, Solution, \
    SolutionQuery
from utils import save_solutions


app = Flask(__name__)
app.config['DEBUG'] = os.environ.get('FLASK_DEBUG', False)


@app.route('/')
def index():
    """Asks for a n problem"""
    return render_template('index.html')


@app.route('/solutions')
def solutions():
    """Asks for a n problem"""
    context = {}
    n = request.args.get('n')
    context['n'] = n
    if not n:
        return redirect(url_for('index'))

    n = int(n)
    session = session_factory()
    query = session.query(SolutionQuery).filter_by(n=n)

    if query.count() == 0:
        status = 0
        create_solution_query(n, 1)
        Thread(
            target=save_solutions,
            args=[n]
        ).start()
    else:
        status = query.first().status
        if status == 2:
            context['solutions'] = session.query(Solution).filter_by(n=n)

    context['status'] = status
    session.close()

    return render_template('solutions.html', **context)

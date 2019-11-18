from .celery import app

@app.task
def add(x, y):
    print("I'm adding")
    return x + y
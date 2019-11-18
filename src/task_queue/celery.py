"""Celery initialization"""

from celery import Celery

app = Celery(
    'task_queue',
    broker='redis://redis:6379',
    include=['task_queue.tasks']
)

if __name__ == '__main__':
    app.start()

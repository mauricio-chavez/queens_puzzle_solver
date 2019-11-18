"""Celery initialization"""

from celery import Celery

app = Celery('tasks', broker='redis://redis:6379')

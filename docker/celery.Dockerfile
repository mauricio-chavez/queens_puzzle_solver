FROM python:3.6.1-alpine

RUN mkdir /usr/src/app
WORKDIR /usr/src/app
RUN pip install --upgrade pip
RUN pip install "celery>=4.3.0,<4.4.0"
RUN pip install "redis>=3.3.11,<3.4.0"
COPY src/ .
ENTRYPOINT celery -A task_queue worker --concurrency=20 --loglevel=info 
FROM python:3.6.1-alpine

RUN apk update \
  && apk add \
    build-base \
    postgresql \
    postgresql-dev \
    libpq \
    bash

RUN mkdir /usr/src/app
WORKDIR /usr/src/app
COPY ./requirements/app.txt ./requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENV PYTHONUNBUFFERED 1

COPY queens_puzzle/ .
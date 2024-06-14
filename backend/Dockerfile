FROM python:3.10-slim-buster

ENV PYTHONUNBUFFERED 1

RUN useradd -ms /bin/bash myuser

WORKDIR /backend

USER myuser

COPY requirements.txt /backend

RUN pip install --no-cache-dir -r requirements.txt

COPY . /backend

ENV PATH="/home/myuser/.local/bin:${PATH}"
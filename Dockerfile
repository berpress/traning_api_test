FROM python:3.6-alpine

COPY requirements.txt /opt/app/requirements.txt

WORKDIR /opt/app

RUN pip install -r requirements.txt

COPY . /opt/app

CMD pytest

# docker build -t python-test-api .
# docker run python-test-api


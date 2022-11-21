FROM python:3.9

WORKDIR /usr/src/django_app

COPY requirements.txt ./
COPY django_app/ ./

RUN pip3 install --no-cache-dir -r requirements.txt


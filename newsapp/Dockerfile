FROM python:3.8.10-alpine

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /webapp

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev jpeg-dev zlib-dev libjpeg

COPY ./requirements.txt /webapp
RUN pip3 install --upgrade pip wheel setuptools
RUN pip3 install -r requirements.txt

COPY . /webapp

EXPOSE 8000
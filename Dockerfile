FROM python:3
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y \
    libgl1-mesa-dev

RUN mkdir /app
WORKDIR /app

COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

COPY . /app/



FROM python:3.8-slim

ENV PATH="/scripts:${PATH}"

COPY ./requirements.txt /requirements.txt

RUN apt-get update
RUN apt-get install build-essential -y
RUN apt-get install gcc -y
RUN apt-get install libpq-dev -y
RUN apt-get install linux-headers-$(uname -r) -y
RUN pip install -r /requirements.txt


RUN mkdir /app
COPY . /app
WORKDIR /app
COPY ./scripts /scripts

RUN chmod +x /scripts/*

RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/static

RUN adduser alexandre
RUN chown -R alexandre:alexandre /vol
RUN chmod -R 755 /vol/web
USER alexandre

CMD ["entrypoint.sh"]

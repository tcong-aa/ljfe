FROM ubuntu:latest

MAINTAINER tengc "tcong@appannie.com"

RUN apt-get update -y
RUN apt-get --no-install-recommends install -y \
                        python-pip python-dev build-essential \
                        wget unzip libpq-dev python git

RUN pip install --upgrade pip
RUN pip install gunicorn setuptools

COPY requirements.txt /code/
WORKDIR /code
RUN pip install -r requirements.txt

COPY . /code
#RUN groupadd -r appannie -g 1000 && useradd -r -g appannie appannie -u 1000
#USER appannie

EXPOSE 5000

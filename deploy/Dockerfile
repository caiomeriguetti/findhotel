FROM ubuntu:16.04

RUN apt-get update \
    && apt-get install -y python curl \
    && curl -O https://bootstrap.pypa.io/get-pip.py \
    && python get-pip.py \
    && apt-get install -y python-dev build-essential openssh-client


RUN pip install fabric==1.14

COPY . /src

WORKDIR /src
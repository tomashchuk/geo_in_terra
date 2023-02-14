# syntax=docker/dockerfile:1
FROM python:3.7

ENV PYTHONUNBUFFERED 1

RUN apt-get update -y && apt-get upgrade -y

# GDAL, PROJ
RUN apt-get install -y gdal-bin libgdal-dev
RUN apt-get install -y python3-gdal
RUN apt-get install -y binutils libproj-dev

COPY . /srv/app
WORKDIR /srv/app
RUN pip install --no-cache -r /srv/app/requirements.txt
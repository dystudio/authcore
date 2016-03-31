# Connectors API.
FROM python:3.5.1-slim
MAINTAINER dodd.anthonyjosiah@gmail.com

WORKDIR /authcore
COPY ./requirements requirements
COPY ./authcore authcore
COPY ./authcore_project authcore_project

# RUN apk update && apk add gcc && apk add postgresql && apk add python-dev
# RUN apt-get -q update && apt-get -qy upgrade && apt-get install -y postgresql
RUN apt-get -qq update
RUN apt-get install -yqq postgresql-9.4
RUN apt-get install -yqq postgresql-server-dev-9.4
# RUN apt-get install -yqq libqp-dev
RUN apt-get install -yqq gcc
RUN pip install -r requirements/prod.txt && rm -rf requirements

# TODO(TheDodd): replace this with gunicorn setup when ready.
# Use a CMD here, instead of ENTRYPOINT, for easy overwrite in docker compose.
CMD python manage.py runserver 0.0.0.0:8000

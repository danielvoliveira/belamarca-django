FROM python:3.8-slim
ENV PYTHONUNBUFFERED=1

# Ajustando TimeZone
ENV TZ=America/Fortaleza
RUN cp /usr/share/zoneinfo/America/Fortaleza /etc/localtime
RUN echo "America/Fortaleza" > /etc/timezone

# set work directory
WORKDIR /belamarca

RUN apt-get update && apt-get install -y nodejs npm build-essential gettext default-libmysqlclient-dev libwebp-dev
RUN pip install gunicorn supervisor

# Instalando requirements
COPY ./belamarca/requirements.txt .
RUN pip install -r requirements.txt

COPY ./nginx.conf /etc/nginx/nginx.conf
COPY ./supervisord.conf /etc/supervisord.conf
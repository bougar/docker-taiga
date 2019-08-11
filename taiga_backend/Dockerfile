FROM python:3.6.9-buster

MAINTAINER Carlos Bouzón García

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y \
        zlib1g-dev \
        libjpeg-dev \
        git \
        nginx \
        supervisor \
        gettext \
        netcat \
        sqlite3 && \
   pip3 install -U pip setuptools && \
   rm -rf /var/lib/apt/lists/*

# install uwsgi now because it takes a little while
RUN pip3 install uwsgi

# setup all the configfiles
RUN echo "daemon off;" >> /etc/nginx/nginx.conf

RUN git clone https://github.com/taigaio/taiga-back.git /taiga_backend --branch stable
WORKDIR /taiga_backend
RUN pip3 install -r requirements.txt
RUN mkdir -p /var/log/uwsgi/
COPY nginx-app.conf /etc/nginx/sites-available/default
COPY supervisor-app.conf /etc/supervisor/conf.d/
COPY uwsgi_params /taiga_backend/uwsgi_params
COPY uwsgi.ini /taiga_backend/uwsgi.ini
COPY config.py /taiga_backend/settings/local.py
COPY entrypoint.sh /entrypoint.sh
RUN ln -sf /dev/stdout /var/log/nginx/access.log \
    && ln -sf /dev/stderr /var/log/nginx/error.log

EXPOSE 80
ENTRYPOINT ["/entrypoint.sh"]

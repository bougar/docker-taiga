FROM nginx:stable

MAINTAINER Carlos Bouzón García

RUN apt update && \
    apt install -y git

RUN git clone https://github.com/taigaio/taiga-front-dist.git /taiga_frontend --branch stable

COPY taiga.conf /taiga_frontend/dist/conf.json
COPY taiga.nginx.conf /etc/nginx/conf.d/default.conf
COPY run.sh /run.sh

ENTRYPOINT ["/run.sh"]

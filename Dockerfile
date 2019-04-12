FROM ubuntu:18.04

WORKDIR cv
COPY requirements.txt requirements.txt
COPY package*.json ./
COPY provision.* ./

RUN sh provision.prod.sh

COPY . /cv/

VOLUME ["/cv"]

ENTRYPOINT ["sh", "entry.prod.sh"]


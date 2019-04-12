FROM ubuntu:18.04

WORKDIR cv
COPY requirements.txt requirements.txt
COPY package*.json ./
COPY provision.* ./

RUN sh provision.dev.sh

COPY . /cv/

VOLUME ["/cv"]

ENTRYPOINT ["sh", "provision.dev.entry.sh"]

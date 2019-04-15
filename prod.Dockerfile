FROM alpine:3.9

WORKDIR cv
COPY requirements.txt requirements.txt
COPY package*.json ./
COPY provision/prod ./provision/prod

RUN sh provision/prod/install.sh

COPY . /cv/

VOLUME ["/cv"]

ENTRYPOINT ["sh", "provision/prod/entry.sh"]

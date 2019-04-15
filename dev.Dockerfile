FROM alpine:3.9

WORKDIR cv
COPY requirements.txt requirements.txt
COPY package*.json ./
COPY provision/dev ./provision/dev

RUN sh provision/dev/install.sh

COPY . /cv/

VOLUME ["/cv"]

ENTRYPOINT ["sh", "provision/dev/entry.sh"]

FROM ubuntu:18.04

RUN apt-get update

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get install -y python3 python3-pip nodejs npm xvfb libfontconfig wkhtmltopdf
RUN npm install -g npx
WORKDIR cv

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY package*.json ./
RUN npm install && mv node_modules /node_modules

RUN printf '#!/bin/bash\nxvfb-run -a --server-args="-screen 0, 1024x768x24" /usr/bin/wkhtmltopdf -q $*' > /usr/bin/wkhtmltopdf.sh \
&& chmod a+x /usr/bin/wkhtmltopdf.sh \
&& ln -s /usr/bin/wkhtmltopdf.sh /usr/local/bin/wkhtmltopdf

VOLUME ["/cv"]

ENTRYPOINT ["sh", "-c", "rm -rf /cv/node_modules 2>/dev/null && mv /node_modules /cv/node_modules && bash"]

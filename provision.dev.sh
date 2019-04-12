apt-get update
DEBIAN_FRONTEND=noninteractive
apt-get install -y python3 python3-pip nodejs npm xvfb libfontconfig wkhtmltopdf
npm install -g npx
pip3 install -r requirements.txt
npm install
mv node_modules /node_modules
printf '#!/bin/bash\nxvfb-run -a --server-args="-screen 0, 1024x768x24" /usr/bin/wkhtmltopdf -q $*' > /usr/bin/wkhtmltopdf.sh
chmod a+x /usr/bin/wkhtmltopdf.sh
ln -s /usr/bin/wkhtmltopdf.sh /usr/local/bin/wkhtmltopdf

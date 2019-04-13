apt-get update
DEBIAN_FRONTEND=noninteractive
apt-get install -y python3 python3-pip nodejs npm wget xvfb


wget "https://downloads.wkhtmltopdf.org/0.12/0.12.5/wkhtmltox_0.12.5-1.bionic_amd64.deb"
apt install -y ./wkhtmltox_0.12.5-1.bionic_amd64.deb
rm ./wkhtmltox_0.12.5-1.bionic_amd64.deb


npm install -g npx
pip3 install -r requirements.txt
npm install
mv node_modules /node_modules


printf '#!/bin/bash\nxvfb-run -a --server-args="-screen 0, 1024x768x24" /usr/local/bin/wkhtmltopdf-orig -q $*' > /usr/bin/wkhtmltopdf.sh
chmod a+x /usr/bin/wkhtmltopdf.sh
mv /usr/local/bin/wkhtmltopdf /usr/local/bin/wkhtmltopdf-orig
ln -s /usr/bin/wkhtmltopdf.sh /usr/local/bin/wkhtmltopdf

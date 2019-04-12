rm -rf /cv/node_modules
mv /node_modules /cv/node_modules
echo "PATH='$(pwd):$PATH'" >> ~/.bashrc
bash

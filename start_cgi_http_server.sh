#!/bin/bash

mkdir -p ./cgi-bin/
cp upload.cgi ./cgi-bin/
chmod +x ./cgi-bin/upload.cgi
mkdir ./upload/
# default ist port 8000, alternativ auch mit folgendem syntax
#python -m http.server --cgi --bind 127.0.0.1 8080
python -m http.server --cgi


#!/bin/sh

sudo apt-get update && sudo apt-get upgrade

wget -c https://raw.github.com/RobertCNelson/tools/master/pkgs/dtc.sh
chmod +x dtc.sh
./dtc.sh

sudo apt-get install -y python-pip pps-tools gpsd gpsd-clients ntp

sudo pip install Adafruit_BBIO

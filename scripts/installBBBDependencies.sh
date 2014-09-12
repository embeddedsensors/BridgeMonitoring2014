#!/bin/sh

# System upgrade
sudo apt-get update && sudo apt-get upgrade

# Install the device tree compiler
wget -c https://raw.github.com/RobertCNelson/tools/master/pkgs/dtc.sh
chmod +x dtc.sh
./dtc.sh

# GPS tools
sudo apt-get install -y python-pip pps-tools gpsd gpsd-clients ntp

# Adafruit libraries
sudo pip install Adafruit_BBIO

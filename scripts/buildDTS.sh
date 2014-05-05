#!/bin/sh

cd SeniorDesign/firmware/
dtc -O dtb -o gps-ntp-00A0.dtbo -b 0 -@ gps-ntp.dts
mv gps-ntp-00A0.dtbo /lib/firmware/

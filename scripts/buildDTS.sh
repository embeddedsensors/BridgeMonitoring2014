#!/bin/sh


'''
This assumes you are the root user.
It uses the Device Tree Compiler to create dtbo files to set the firmware so we can access it.
Device Tree Files are all stored in the firmware directory
'''

cd ../firmware/
dtc -O dtb -o gps-ntp-00A0.dtbo -b 0 -@ gps-ntp.dts
mv gps-ntp-00A0.dtbo /lib/firmware/

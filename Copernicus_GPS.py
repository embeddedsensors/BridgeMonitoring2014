#!/usr/bin/python

'''
Copernicus 2 GPS Python Module

Library to get and return data from a Copernicus GPS board
with a BeagleBone Black using Python. For now, constructing
the object will create the serial instance. Then calling getData
will return an array with data strings from the GPS.

Written By: Matthew Iannucci
Fall 2013
_______________________________________________________________
Connections

GPS Module  Beaglebone Black
VCC         P9 3
GND         P9 1
TX-B        P9 26
RX-B        P9 24
'''

import serial, os

class GPS:
    prev = []

    def __init__(self, port):
        ''' Call the constructor to set up the object '''
        os.system('echo uart1 > /sys/devices/bone_capemgr.9/slots')
        self.com = serial.Serial(port=port)
        # Send the init string to tell the GPS to send NMEA at 1 Hz
        nmeaCmd = '$PTNLSNM,0100,01*56\r\n'
        self.com.write(nmeaCmd)

    def getData(self):
        '''
        Get all of the data from a packet into a string

        Returns [UTC, DATE, NLAT, WLONG] as ints
        '''
        resp = ''
        info = []
        if (self.com.inWaiting() > 0):
            resp += self.com.read()
            if '\r\n' in resp:
                if '$GPRMC' in resp:
                    data = resp.split(',')
                    # Info = [UTC, DATE, NLAT, WLONG]
                    info = [data[1], data[9], data[3], data[5]]
                    #print info
                    self.prev = info
                    return info
        else:
            return self.prev

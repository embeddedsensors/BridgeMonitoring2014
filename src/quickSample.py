#!/usr/bin/python

'''
OCE 495 Senior Design Bridge Monitoring

Written By: Matthew Iannucci
Spring 2014

'''
import signal
import sys
import time
from libs.Adafruit_ADS1x15 import ADS1x15

ADS1115 = 0x01  # 16-bit ADC Address
ADC_ADDRESS_1 = 0x48

SAMPLE_RATE = 100
DURATION = 60
LOGFILE_NAME = 'rawData'
CHANNELS = [0, 1, 2]

def signal_handler(signal, frame):
    '''
    Handle a keyboard interrupt
    '''
    print 'You pressed Ctrl+C! Exiting...\n'
    sys.exit(0)

def sampleRun(duration, sampleRate, channels):
    '''
    Sample from the ADC and log into an array
    '''
    # Initialise the ADC using the default mode
    # For now only use one ADC, so only create one ADC object
    print 'Data collection started...Press Ctrl+C to exit\n'
    adc = ADS1x15(address=ADC_ADDRESS_1, ic=ADS1115)
    samples = range(0, ((duration*sampleRate)-1))
    volts = [None] * len(samples)
    for sample in samples:
        if not isinstance(channels, int):
            volts[sample] = [adc.readADCSingleEnded(channels[0], 3300, sampleRate) / 1000,
                             adc.readADCSingleEnded(channels[1], 3300, sampleRate) / 1000,
                             adc.readADCSingleEnded(channels[2], 3300, sampleRate) / 1000]
        else:
            volts[sample] = adc.readADCSingleEnded(channels, 3300, SAMPLE_RATE) / 1000
    return volts

def log(filename, data, sampleRate, duration, channels, rectime):
    '''
    Log the data collected in an array to a file to be used for later
    '''
    fp = open(filename + '-' + str(rectime) + '.txt', 'w+')
    fp.write('ADS 1115 Data Collection\nSample Rate: ' + str(sampleRate) + ' Herz\nDuration: ' + str(duration) + ' Seconds\n')
    fp.write(time.strftime('%X %x %Z') + '\n--------------------------------------------------------------\n')
    for dataset in data:
        if isinstance(channels, int):
            fp.write(str(dataset) + '\n')
        else:
            j = 0
            j = range(0,len(channels))
            for k in j:
                if k == max(j):
                    fp.write(str(dataset[k]) + '\n')
                else:
                    fp.write(str(dataset[k]) + ',')
    print 'Data logged to ' + filename + str(rectime) + '.txt' + '\n'

def main(filename, sampleRate, duration, channels):
    '''
    Run the main log for the data logging application
    '''
    i = 0
    while i < 8:
        rectime = time.clock()
        data = sampleRun(duration, sampleRate, channels)
        print 'Finished data collection. Logging...\n'
        log(filename, data, sampleRate, duration, channels, rectime)
        time.sleep(60*15)  # Sleep for 15 minutes
        i += 1

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    main(LOGFILE_NAME, SAMPLE_RATE, DURATION, CHANNELS)
    print 'Data logging successful. Exiting...\n'
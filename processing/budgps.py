'''
Process data from the Newport Bridge from OCE 496

'''
import csv
import scipy.io as sio

from gpsutil import lat2meter

origin_lat = 41.50495
origin_lon = -71.348831

files = ['../data/BRIDGE-SE3.dat',
         '../data/BRIDGE-SW3.dat',
         '../data/BRIDGE-NW3.dat',
         '../data/BRIDGE-NE3.dat']

SE3 = []
SW3 = []
NE3 = []
NW3 = []

datastruct = [
    SE3,
    SW3,
    NE3,
    NW3
]

# Cycle through the files and get the meter coordinates into a large data structure
print 'Starting to read data from gps files'
ind = 0
for fi in files:
    print 'Converting ' + fi 
    with open(fi, 'rb') as f:
        reader = csv.reader(f, delimiter=' ', )
        # Skip the header lines
        line = 0
        for row in reader:
            if line < 22:
                line += 1
                pass
            else:
                lat = float(row[3])
                lon = float(row[4])
                datastruct[ind].append(lat2meter(lat, lon, origin_lat, origin_lon))
    ind += 1

# Create a MATLAB data file
print 'Writing data to MATLAB file'
matdata = {}
matdata['SE3meter'] = datastruct[0]
matdata['SW3meter'] = datastruct[1]
matdata['NW3meter'] = datastruct[2]
matdata['NE3meter'] = datastruct[3]
sio.savemat('../data/bridge_gps.mat', matdata)
print 'Finished!'

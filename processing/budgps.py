'''
Process data from the Newport Bridge from OCE 496

'''
import csv
import matplotlib.pylab as pl

from gpsutil import lat2meter

origin_lon = -71.348831
origin_lat = 41.50495

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

ind = 0
for fi in files:
    print fi
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

print datastruct